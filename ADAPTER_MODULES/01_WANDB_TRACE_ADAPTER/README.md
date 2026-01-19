# W&B Trace Adapter

Converts PROACTIVE trace logs to Weights & Biases Tables for auditor analysis.

## Status: IN DEVELOPMENT

Current version: 0.1.0 (STUB)

## Purpose

This adapter validates **Principle O (Observability)** and **I4 (Traceability Mandatory)** by:
- Converting PROACTIVE trace logs to W&B Tables
- Enabling visual inspection of claim provenance
- Supporting root cause attribution in failure analysis

## Success Metric

Auditors find root cause **significantly faster** than baseline (see validation report).

## Installation

```bash
pip install wandb
wandb login  # Configure API key
```

## Usage (after A01-T3 implementation)

```python
from adapter import load_trace_log, convert_to_wandb_table, upload_to_wandb

# Load trace log
entries = load_trace_log("path/to/trace.json")

# Convert to W&B Table
table = convert_to_wandb_table(entries)

# Upload to W&B
url = upload_to_wandb(table, project="proactive-traces", run_name="test-run")
print(f"View at: {url}")
```

## CLI Usage

```bash
python adapter.py trace_log.json proactive-traces
```

## Schema

See `schema.json` for the PROACTIVE trace log format.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| claim_id | string | UUID of the claim |
| timestamp | datetime | ISO8601 timestamp |
| claim_text | string | The output claim |
| confidence_score | float | 0.0-1.0 confidence |
| validator_results | object | I1-I6 check results |
| final_decision | string | EMIT/BLOCK/ESCALATE |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| prompt_hash | string | SHA256 of triggering prompt |
| epistemic_tag | string | OBSERVED/INFERRED/SPECULATED |
| evidence_sources | array | Evidence URIs or hashes |
| trace_chain | object | REQ→CTRL→TEST→EVID→DECISION linkage |
| principle_tags | array | Active PROACTIVE principles (P,R,O,A,C,T,I,V,E) |
| failure_mode | string | F1-F5 or null |

### Sample Data

See `sample_input.json` for example trace log entries covering:
- EMIT decisions (clean pass)
- BLOCK decisions (failures detected)
- F1 failure mode (overconfidence)
- F2 failure mode (phantom work)
- Complete and incomplete trace chains

## Validation

See `validation_report_template.md` for the evaluation methodology.

## Links

- [PROACTIVE Framework](../../01_FOUNDATIONS/PRD_COL_PROACTIVE_MBSE.md)
- [Evaluation Methodology](../../TASK_MANAGEMENT/EVALUATION_METHODOLOGY.md)
- [W&B Tables Documentation](https://docs.wandb.ai/guides/tables)

---

## V&T

- Created: 2026-01-19
- Status: STUB (A01-T2 complete, awaiting A01-T3)
- Blocked by: W&B account setup (see EXTERNAL_DEPENDENCIES_SETUP.md)
