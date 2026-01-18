# 07_ANALYSIS_TEMPLATES

## Status: ⚠️ TO CREATE

This directory will contain Stage 6 artifacts for turning results into defensible claims.

## Planned Documents

| Document | Purpose | Priority |
|----------|---------|----------|
| PRIMARY_RESULTS_TEMPLATE.md | Main findings with statistical tests and effect sizes | P2 |
| ABLATION_STUDY_TEMPLATE.md | Component contribution analysis format | P2 |
| FAILURE_MODE_CATALOG_TEMPLATE.md | Systematic failure documentation structure | P2 |
| LIMITATIONS_THREATS_TEMPLATE.md | Internal/external validity threats | P2 |

## Creation Criteria

These documents should be created when:
- Evaluation produces results
- Analysis phase begins
- Paper writing starts

## Specification: PRIMARY_RESULTS_TEMPLATE.md

### Required Structure
```markdown
## Hypothesis H[n]

### Prediction
[Directional prediction from pre-registration]

### Results
| Condition | Metric | Value | 95% CI | p-value | Effect Size |
|-----------|--------|-------|--------|---------|-------------|
| Framework | F1-F5 Rate | X% | [a, b] | < 0.05 | d = X |
| Baseline | F1-F5 Rate | Y% | [c, d] | — | — |

### Interpretation
[What this means for the hypothesis]

### Caveats
[Limitations specific to this result]
```

## Specification: ABLATION_STUDY_TEMPLATE.md

### Required Structure
```markdown
## Component: [Name]

### Ablation Condition
[What was removed/disabled]

### Expected Effect
[Prediction from Theory of Action]

### Observed Effect
| Metric | Full System | Ablated | Δ | p-value |
|--------|-------------|---------|---|---------|
| X | a | b | c | d |

### Attribution Conclusion
[What this tells us about component contribution]
```

## Specification: FAILURE_MODE_CATALOG_TEMPLATE.md

### Required Structure
```markdown
## Failure Mode: FM-[ID]

### Classification
- F1/F2/F3/F4/F5: [Which taxonomy class]
- Severity: Low/Medium/High/Critical
- Frequency: Rare/Occasional/Common

### Description
[What happened]

### Trigger Conditions
[What caused it]

### Example Instance
[Specific case]

### Root Cause Analysis
[Why the framework failed to prevent it]

### Mitigation Status
- [ ] Identified
- [ ] Fix proposed
- [ ] Fix implemented
- [ ] Fix verified
```

---

*Placeholder created: 2026-01-18*
