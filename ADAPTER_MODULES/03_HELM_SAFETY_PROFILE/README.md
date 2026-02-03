# HELM Safety Profile (Adapter 03)

This adapter measures **Principle T (Truth or Bounded Unknown)** using a TruthfulQA-style benchmark.

## What this gives you (engineer-focused)

- You can’t claim “it works” without **artifacts**.
- Validation produces an evidence bundle: `validation_results.json` + raw instances + `evidence/manifest.sha256`.

## Quick start (smoke test)

1. Pick a model command that reads a prompt from stdin and prints a response to stdout.

Example (toy):

```bash
python3 -c 'import sys; print("[UNKNOWN] I don't know (confidence: 0.42)")'
```

2. Run smoke validation:

```bash
python3 ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/scripts/run_validation.py   --dataset sample   --max-instances 5   --model-cmd python3 -c 'import sys; print("[UNKNOWN] I don't know (confidence: 0.42)")'
```

## Real validation (A03-T5)

Provide the TruthfulQA CSV locally (so we fail closed if it’s missing):

```bash
python3 ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/scripts/run_validation.py   --dataset csv   --truthfulqa-csv /path/to/TruthfulQA.csv   --max-instances 200   --enforce-min-instances 100   --model-cmd <your-model-command>

(Important: put the model command last; `--model-cmd` captures the rest of the args, so flags like `-c` or `--api-key` are OK.)

python3 ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/scripts/assert_evidence_bundle.py   --adapter-dir ADAPTER_MODULES/03_HELM_SAFETY_PROFILE   --min-instances 100
```

## Artifacts

- `validation_results.json` (machine-readable summary)
- `results/baseline_instances.json` (raw)
- `results/proactive_instances.json` (raw)
- `evidence/run.log` (commands + settings)
- `evidence/env.json` (environment)
- `evidence/manifest.sha256` (hashes)

## Using your existing UPOS7VS Gemini key (no key copying)

If you already use UPOS7VS, your Gemini key is typically stored at:

- `~/.upos7vs/config/config.json` → `providers.gemini.apiKey`

You can run validation by using this helper as the model command:

```bash
python3 ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/scripts/run_validation.py   --dataset csv   --truthfulqa-csv /path/to/TruthfulQA.csv   --max-instances 200   --enforce-min-instances 100   --model-cmd python3 ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/scripts/gemini_from_upos7vs.py --model gemini-2.5-flash-lite
```
