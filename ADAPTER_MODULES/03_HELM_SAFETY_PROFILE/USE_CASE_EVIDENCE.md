# Use Case Evidence: HELM Safety Profile (Adapter 03)

## Status: AWAITING VALIDATION (A03-T5)

## Executive Summary

This adapter is implemented but not yet validated on >= 100 TruthfulQA instances.

## Validation Approach

- **Type**: Benchmark comparison
- **Dataset**: TruthfulQA (CSV) or sample dataset for smoke tests
- **Conditions**: baseline prompt vs PROACTIVE prompt (epistemic tag + confidence + unknown discipline)
- **Success criteria** (A03-T5): >= 100 instances, p-value reported, effect size reported, limitations stated

## Results

Results will be written by `scripts/run_validation.py`:

- `validation_results.json`
- `evidence/manifest.sha256`

## Limitations

- Until `validation_results.json` exists, no truthfulness improvement claims are permitted.

## Artifacts

- Runner: `scripts/run_validation.py`
- Evidence validator: `scripts/assert_evidence_bundle.py`
- Metrics: `proactive_metrics.yaml`
