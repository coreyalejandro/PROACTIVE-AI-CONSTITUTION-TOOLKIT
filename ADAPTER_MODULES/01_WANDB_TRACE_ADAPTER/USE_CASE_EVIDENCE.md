# Use Case Evidence: W&B Trace Adapter

## Status: PILOT COMPLETE

## Executive Summary

We tested whether the PROACTIVE W&B Trace Adapter improves root cause attribution compared to baseline approaches using raw JSON and standard W&B tables. In a pilot study with 9 synthetic trace log cases covering F1 (overconfidence), F2 (phantom work), and F4 (incomplete trace) failure modes, the adapter reduced attribution time by 52% while improving accuracy from 67-89% to 100%.

## Validation Approach

- **Type**: Qualitative pilot (Pipeline B scope)
- **Cases**: N=9 trace logs with known failure modes (2 clean, 2 F1, 2 F2, 2 F4, 1 mixed)
- **Evaluator**: Self (author)
- **Pre-registration**: Commit 5f12480 dated 2026-01-19

## Key Finding

The PROACTIVE adapter's explicit I1-I6 validator columns and trace_complete indicator enabled immediate identification of failure patterns that required manual JSON parsing or indirect table filtering in baseline conditions. The structured columns transform invariant violations from hidden nested data into visible, sortable, filterable attributes.

## Quantitative Results

| Condition | Mean Time (min) | Accuracy |
|-----------|-----------------|----------|
| Baseline A (raw JSON) | 15.48 | 66.7% |
| Baseline B (standard W&B) | 10.77 | 88.9% |
| Treatment (PROACTIVE adapter) | 5.20 | 100.0% |

**Improvement over Baseline B**: 52% time reduction, +11 percentage points accuracy  
**Statistical significance**: p < 0.0001 (t-test), Cohen's d = 3.31 (large effect)

## Qualitative Observations

1. **What worked well**: The I1-I6 columns provided immediate visibility into which invariant failed. Filtering on `I4=FAIL` instantly surfaced all F4 (incomplete trace) cases. The `trace_complete` boolean was particularly useful for distinguishing F2/F4 from clean entries.

2. **What was difficult**: Interpreting combinations of failures in the mixed case (case_09) still required some mental effort. The schema knowledge needed upfront investment - auditors unfamiliar with PROACTIVE invariants would need training.

3. **What surprised us**: 
   - Baseline B (standard W&B) performed better than raw JSON by a significant margin, suggesting table visualization alone provides substantial value
   - The `failure_mode` column, while informative, was less actionable than the I1-I6 breakdown
   - 100% accuracy with the adapter may indicate the test cases were too easy (ceiling effect)

## Limitations

- **Author-as-evaluator introduces bias**: The evaluator designed both the adapter and test cases, likely inflating performance
- **N=9 is insufficient for statistical claims**: Wide confidence intervals; cannot reliably estimate true effect size
- **Synthetic cases may not represent real-world complexity**: Actual trace logs may have noisier patterns, partial failures, or unexpected structures
- **Single evaluator**: Cannot measure inter-rater reliability or generalize to other auditors
- **Ceiling effect possible**: 100% treatment accuracy suggests test cases may be too straightforward

## Implications for Safety Case

This evidence supports **Argument Strand O (Observability)**:

- **Claim**: The trace adapter makes failure modes visible to auditors, enabling faster and more accurate root cause attribution than inspection of raw trace data or generic table views
- **Confidence**: Medium (promising pilot results, but author-evaluated with synthetic data)
- **Next steps to strengthen**: 
  1. Pipeline A study with 8-12 external auditors
  2. Real-world trace logs from PROACTIVE-instrumented systems
  3. Pre-registered hypotheses with power analysis
  4. Blinded evaluation protocol

## Artifacts

- Full validation report: [`validation_report.md`](validation_report.md)
- Raw data: [`data/validation_results.json`](data/validation_results.json)
- Test cases: [`data/test_cases/`](data/test_cases/)
- Adapter code: [`adapter.py`](adapter.py)
- Schema: [`schema.json`](schema.json)
- Analysis script: [`scripts/analyze_validation.py`](scripts/analyze_validation.py)

## Safety Case Integration

This evidence is registered in the [Safety Case Skeleton](../../09_SAFETY_CASE/SAFETY_CASE_SKELETON.md):

| ID | Description | Source | Status |
|----|-------------|--------|--------|
| E-O1 | W&B Adapter pilot results | Adapter 01 | Complete (Pilot) |

**Argument Strand**: O (Observability Enables Auditing)  
**Sub-Goal**: G1.3 - Trace chain enables meaningful auditability  
**Confidence Level**: Medium (pilot data, author-evaluated)

**Trace Chain**:
```
Principle O (Observability)
    │
    ▼
Invariant I4 (Traceability Mandatory)
    │
    ▼
Adapter 01 (W&B Trace Adapter)
    │
    ▼
Evidence E-O1 (Pilot: 52% time reduction, 100% accuracy)
    │
    ▼
Claim: "Trace adapter improves root cause attribution"
    │
    ▼
Safety Case Strand O: "Observability enables auditing"
```

---

## V&T Statement

### EXISTS
- Pilot validation study with 9 test cases
- Quantitative metrics: time (min), accuracy (%)
- Statistical analysis: t-test, Cohen's d
- Complete USE_CASE_EVIDENCE.md (no brackets)
- All artifacts referenced and present

### FUNCTIONAL STATUS
- Adapter functional (A01-T3 verified)
- Analysis pipeline functional (A01-T4 verified)
- Pilot validation complete (A01-T5 verified)
- Evidence registered for safety case integration

### NOT CLAIMED
- External auditor validation
- Real-world trace log coverage
- Generalization beyond synthetic test cases
- Inter-rater reliability metrics

---

*Completed: 2026-01-19 | A01-T5 | Session 8*
