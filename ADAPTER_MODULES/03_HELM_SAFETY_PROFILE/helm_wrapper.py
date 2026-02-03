"""HELM Safety Profile runner (Practical version).

This adapter intentionally separates:
- The *human chat* (messy)
- The *executable validation* (strict)

It runs a TruthfulQA-style benchmark (sample dataset by default; full dataset supported via CSV path)
and produces machine-readable artifacts for A03-T5.

No result claims are allowed without the evidence bundle produced by scripts/run_validation.py.
"""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence


EPISTEMIC_TAGS = ("OBSERVED", "INFERRED", "SPECULATED", "UNKNOWN")


@dataclass
class ScenarioResult:
    scenario_name: str
    instances: List[Dict[str, Any]]
    raw_outputs: List[str]
    metadata: Dict[str, Any]


def _load_yaml(path: Path) -> Dict[str, Any]:
    try:
        import yaml
    except ImportError as e:
        raise RuntimeError("Missing dependency: pyyaml (pip install pyyaml)") from e

    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_scenario_config(adapter_dir: Path) -> Dict[str, Any]:
    return _load_yaml(adapter_dir / "scenario_config.yaml")


def adapt_prompt(question: str, prompt_template: str) -> str:
    return prompt_template.format(question=question)


def parse_response(text: str) -> Dict[str, Any]:
    result: Dict[str, Any] = {
        "raw": text,
        "epistemic_tag": "UNKNOWN",
        "confidence": None,
        "is_bounded_unknown": False,
        "answer_text": text.strip(),
    }

    tag_match = re.search(r"\[(OBSERVED|INFERRED|SPECULATED|UNKNOWN)\]", text, re.IGNORECASE)
    if tag_match:
        result["epistemic_tag"] = tag_match.group(1).upper()

    conf_match = re.search(r"confidence[:\s]*([01](?:\.\d+)?|0\.\d+)", text, re.IGNORECASE)
    if conf_match:
        try:
            result["confidence"] = float(conf_match.group(1))
        except ValueError:
            result["confidence"] = None

    unknown_patterns = [
        r"i don't know",
        r"i do not know",
        r"uncertain",
        r"cannot determine",
        r"insufficient information",
    ]
    result["is_bounded_unknown"] = any(re.search(p, text, re.IGNORECASE) for p in unknown_patterns)

    # Strip formatting to get answer text
    cleaned = re.sub(r"\[.*?\]", "", text).strip()
    cleaned = re.sub(r"\(\s*confidence:.*?\)", "", cleaned, flags=re.IGNORECASE).strip()
    result["answer_text"] = cleaned

    return result


def load_truthfulqa_from_csv(csv_path: Path, max_instances: int) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if not header:
            return []
        # Expected columns from TruthfulQA.csv: type, category, question, best_answer, correct_answers, incorrect_answers, source
        for i, row in enumerate(reader):
            if max_instances and len(rows) >= max_instances:
                break
            if len(row) < 7:
                continue
            _type, category, question, best_answer, _correct_answers, _incorrect_answers, _source = row
            rows.append(
                {
                    "category": category,
                    "question": question,
                    "best_answer": best_answer,
                }
            )
    return rows


def load_truthfulqa_sample(adapter_dir: Path, max_instances: int) -> List[Dict[str, Any]]:
    data = json.loads((adapter_dir / "datasets" / "truthfulqa_sample.json").read_text(encoding="utf-8"))
    instances = data.get("instances", [])
    return instances[:max_instances]


def call_model_via_command(model_command: Sequence[str], prompt: str, timeout_s: int) -> str:
    """Call model via subprocess.
    
    Note: timeout_s is the subprocess timeout. If the model command has internal retries,
    ensure this timeout is large enough to accommodate them (e.g., 10 retries × HTTP timeout).
    """
    try:
        proc = subprocess.run(
            list(model_command),
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired as e:
        stderr_text = e.stderr.decode("utf-8", errors="replace") if e.stderr else ""
        raise RuntimeError(
            f"Model command timed out after {timeout_s}s. This may indicate rate limiting or "
            f"network issues. Consider increasing --timeout-s or reducing --max-retries in the "
            f"model command.\nstderr: {stderr_text}"
        ) from e
    if proc.returncode != 0:
        raise RuntimeError(
            f"Model command failed (exit {proc.returncode}). stderr:\n{proc.stderr.decode('utf-8', errors='replace')}"
        )
    return proc.stdout.decode("utf-8", errors="replace")


def run_validation(
    adapter_dir: Path,
    dataset: str,
    max_instances: int,
    model_command: Sequence[str],
    timeout_s: int,
    csv_path: Optional[Path] = None,
) -> Dict[str, ScenarioResult]:
    """Run baseline + proactive prompt conditions and return raw ScenarioResults.

    This does NOT write the evidence bundle; scripts/run_validation.py does.
    """

    config = load_scenario_config(adapter_dir)
    baseline_tmpl = config["scenarios"]["truthfulqa_baseline"]["prompt_template"]
    proactive_tmpl = config["scenarios"]["truthfulqa_proactive"]["prompt_template"]

    if dataset == "sample":
        questions = load_truthfulqa_sample(adapter_dir, max_instances)
    elif dataset == "csv":
        if not csv_path:
            raise RuntimeError("dataset=csv requires --truthfulqa-csv")
        questions = load_truthfulqa_from_csv(csv_path, max_instances)
    else:
        raise RuntimeError("dataset must be one of: sample, csv")

    def run_condition(name: str, tmpl: str) -> ScenarioResult:
        instances: List[Dict[str, Any]] = []
        raws: List[str] = []
        for q in questions:
            prompt = adapt_prompt(q["question"], tmpl)
            raw = call_model_via_command(model_command, prompt, timeout_s=timeout_s)
            raws.append(raw)
            parsed = parse_response(raw)
            parsed.update(
                {
                    "question": q["question"],
                    "best_answer": q["best_answer"],
                    "category": q.get("category", ""),
                    "prompt": prompt,
                }
            )
            instances.append(parsed)
        return ScenarioResult(
            scenario_name=name,
            instances=instances,
            raw_outputs=raws,
            metadata={
                "dataset": dataset,
                "max_instances": max_instances,
                "model_command": list(model_command),
            },
        )

    return {
        "baseline": run_condition("truthfulqa_baseline", baseline_tmpl),
        "proactive": run_condition("truthfulqa_proactive", proactive_tmpl),
    }
