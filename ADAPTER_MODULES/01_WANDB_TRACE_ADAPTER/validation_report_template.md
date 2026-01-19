# Validation Report: W&B Trace Adapter

## Report Metadata

- **Date**: [DATE]
- **Adapter Version**: [VERSION]
- **Evaluator**: [NAME]
- **Evaluation Type**: [PILOT / FULL]

## Study Design

### Conditions

- **Baseline A**: [Description of null baseline]
- **Baseline B**: [Description of standard practice baseline]
- **Treatment**: W&B with PROACTIVE trace adapter

### Sample

- **Number of cases**: [N]
- **Case selection**: [Random / Stratified / Convenience]
- **Number of auditors**: [N]
- **Auditor background**: [Description]

## Results

### Primary Metric: Root Cause Attribution Time

| Condition | Mean Time (min) | Std Dev | N |
|-----------|-----------------|---------|---|
| Baseline A | [VALUE] | [VALUE] | [N] |
| Baseline B | [VALUE] | [VALUE] | [N] |
| Treatment | [VALUE] | [VALUE] | [N] |

**Statistical Test**: [Test name]  
**Result**: [p-value, effect size, confidence interval]  
**Interpretation**: [Plain English]

### Secondary Metric: Attribution Accuracy

| Condition | Accuracy (%) | N |
|-----------|--------------|---|
| Baseline A | [VALUE] | [N] |
| Baseline B | [VALUE] | [N] |
| Treatment | [VALUE] | [N] |

### Tertiary Metrics

| Metric | Baseline A | Baseline B | Treatment |
|--------|------------|------------|-----------|
| User comprehension | [VALUE] | [VALUE] | [VALUE] |
| False positive rate | [VALUE] | [VALUE] | [VALUE] |
| Log completeness | [VALUE] | [VALUE] | [VALUE] |

### Qualitative Observations

1. [Observation about usability]
2. [Observation about failure cases]
3. [Observation about unexpected findings]

## Limitations

1. [Limitation 1 - e.g., small sample size]
2. [Limitation 2 - e.g., author-as-evaluator]
3. [Limitation 3 - e.g., specific case types only]

## Conclusion

[2-3 sentences: Does the adapter improve root cause attribution? With what confidence? What's the scope of the claim?]

## Raw Data Reference

- Data location: [PATH]
- Analysis script: [PATH]
- Pre-registration: [COMMIT HASH]

---

## V&T

- Created: 2026-01-19
- Status: TEMPLATE (awaiting A01-T5)
- Blocked by: A01-T3 implementation
