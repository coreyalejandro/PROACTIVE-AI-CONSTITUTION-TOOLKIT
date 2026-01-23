# CI Safety Gate

GitHub Actions workflow that validates model outputs against PROACTIVE constitutional invariants.

## Status: IMPLEMENTED

Current version: 1.0.0

## Purpose

This adapter validates **Principle V (Verification Before Action)** by:
- Running constitutional invariant checks (I1-I6) on every PR/push
- Blocking merges when violations are detected
- Posting detailed violation reports as PR comments

## Success Metric

The gate **catches seeded vulnerabilities** that pass standard tests, demonstrating that constitutional validation provides safety coverage beyond traditional testing.

## Installation

### As GitHub Action

```yaml
# .github/workflows/proactive-safety.yml
name: PROACTIVE Safety Gate

on:
  pull_request:
  push:
    branches: [main]

jobs:
  safety-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run PROACTIVE Safety Gate
        uses: ./ADAPTER_MODULES/02_CI_SAFETY_GATE
        with:
          directory: './outputs'
          fail_on_warning: 'false'
          post_comment: 'true'
```

### Local Usage

```bash
pip install pyyaml jsonschema
python validator.py ./outputs --format text
```

## Invariants Checked

| Invariant | Description | Severity |
|-----------|-------------|----------|
| I1 | Evidence-First Outputs | ERROR |
| I2 | No Phantom Work | ERROR |
| I3 | Confidence Requires Verification | WARNING |
| I4 | Traceability Is Mandatory | ERROR |
| I5 | Safety Over Fluency | WARNING |
| I6 | Fail Closed | ERROR |

## Output Formats

- **json**: Structured violation report (default)
- **sarif**: GitHub Security compatible format
- **text**: Human-readable summary

## Configuration

See `validator_config.yaml` for customization options:

- Enable/disable specific invariants
- Adjust severity levels
- Configure file patterns
- Set warning thresholds

## Links

- [PROACTIVE Constitution](../../01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md)
- [Evaluation Methodology](../../TASK_MANAGEMENT/EVALUATION_METHODOLOGY.md)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
