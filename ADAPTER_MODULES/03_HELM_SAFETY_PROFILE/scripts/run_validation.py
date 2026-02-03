from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import shutil
import sys
from datetime import datetime, UTC
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=["sample", "csv"], default="sample")
    ap.add_argument("--truthfulqa-csv", default="")
    ap.add_argument("--max-instances", type=int, default=100)
    ap.add_argument(
        "--model-cmd",
        nargs=argparse.REMAINDER,
        help="Model command (must come last). Use: --model-cmd -- <cmd ...>",
    )
    ap.add_argument(
        "--timeout-s",
        type=int,
        default=300,
        help="Subprocess timeout per question (must accommodate retries; default 300s)",
    )
    ap.add_argument("--bootstrap-iters", type=int, default=1000)
    ap.add_argument(
        "--enforce-min-instances",
        type=int,
        default=0,
        help="If >0, fail unless both runs have at least this many instances",
    )
    args = ap.parse_args()

    if not args.model_cmd or args.model_cmd == ["--"]:
        raise SystemExit("--model-cmd is required. Example: --model-cmd -- gemini <args>")

    # Allow optional leading '--' after --model-cmd
    if args.model_cmd and args.model_cmd[0] == "--":
        args.model_cmd = args.model_cmd[1:]

    adapter_dir = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(adapter_dir))

    from helm_wrapper import run_validation as run_pair  # noqa: E402

    csv_path = Path(args.truthfulqa_csv) if args.truthfulqa_csv else None

    evidence_dir = adapter_dir / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    run_log = evidence_dir / "run.log"
    with run_log.open("w", encoding="utf-8") as log:
        log.write(f"started_at={datetime.now(UTC).isoformat().replace('+00:00', 'Z')}\n")
        log.write(f"cwd={os.getcwd()}\n")
        log.write(f"dataset={args.dataset}\n")
        log.write(f"truthfulqa_csv={args.truthfulqa_csv}\n")
        log.write(f"max_instances={args.max_instances}\n")
        log.write(f"model_cmd={' '.join(args.model_cmd)}\n")

    pair = run_pair(
        adapter_dir=adapter_dir,
        dataset=args.dataset,
        max_instances=args.max_instances,
        model_command=args.model_cmd,
        timeout_s=args.timeout_s,
        csv_path=csv_path,
    )

    results_dir = adapter_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    baseline_path = results_dir / "baseline_instances.json"
    proactive_path = results_dir / "proactive_instances.json"

    baseline_path.write_text(json.dumps(pair["baseline"].instances, indent=2) + "\n", encoding="utf-8")
    proactive_path.write_text(json.dumps(pair["proactive"].instances, indent=2) + "\n", encoding="utf-8")

    if args.enforce_min_instances:
        if len(pair["baseline"].instances) < args.enforce_min_instances or len(pair["proactive"].instances) < args.enforce_min_instances:
            raise SystemExit(
                f"Fail closed: insufficient instances. baseline={len(pair['baseline'].instances)} proactive={len(pair['proactive'].instances)} min={args.enforce_min_instances}"
            )

    # Analyze
    validation_results = adapter_dir / "validation_results.json"
    analyze = [
        sys.executable,
        str(adapter_dir / "scripts" / "analyze_results.py"),
        "--baseline",
        str(baseline_path),
        "--proactive",
        str(proactive_path),
        "--out",
        str(validation_results),
        "--bootstrap-iters",
        str(args.bootstrap_iters),
    ]

    proc = subprocess.run(analyze, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise SystemExit(
            "analysis failed:\n" + proc.stderr.decode("utf-8", errors="replace")
        )

    env = {
        "python": sys.version,
        "platform": platform.platform(),
        "helm_run_available": bool(shutil.which("helm-run")),
        "timestamp_utc": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }
    (evidence_dir / "env.json").write_text(json.dumps(env, indent=2) + "\n", encoding="utf-8")

    manifest_paths = [baseline_path, proactive_path, validation_results, run_log, (evidence_dir / "env.json")]
    manifest_lines = [f"{sha256_file(p)}  {p.relative_to(adapter_dir)}" for p in manifest_paths]
    (evidence_dir / "manifest.sha256").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    print(f"Wrote {validation_results}")
    print(f"Wrote {evidence_dir / 'manifest.sha256'}")
    return 0


if __name__ == "__main__":

    raise SystemExit(main())
