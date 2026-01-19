# Evaluation Methodology: PROACTIVE Adapters

## Baseline Conditions

### Baseline A (Null)

- Raw JSON logs viewed in text editor
- No tooling assistance
- No schema or structure
- Represents: "What if we built nothing?"

### Baseline B (Standard Practice)

- W&B default logging (unstructured)
- No PROACTIVE schema
- Standard dashboard views
- Represents: "Current industry practice"

### Treatment

- W&B with PROACTIVE trace adapter
- Full schema with constitutional validation markers
- Epistemic tags on all claims
- Trace chain linking decisions to evidence
- Represents: "PROACTIVE-enabled workflow"

**Primary comparison**: Treatment vs. Baseline B (does PROACTIVE improve on current practice?)

**Secondary comparison**: Treatment vs. Baseline A (does any tooling help?)

## Success Thresholds

| Metric | Threshold | Justification |
| ------ | --------- | ------------- |
| Root cause attribution time | Statistically significant reduction (p<0.05) | Effect size TBD from pilot; "50% faster" is aspirational |
| Attribution accuracy | ≥80% correct root cause identification | Baseline for "useful" tooling; below this, tool adds noise |
| Log completeness | ≥99% valid fields per schema | System reliability standard; missing data = audit failure |
| User comprehension | ≥80% accurate interpretation of intent receipts | Oversight viability; users must understand what they're approving |
| False positive rate | <10% spurious constitutional violations | Usability; too many false alarms = ignored alarms |

**Note**: Actual thresholds will be grounded in pilot data. Claims will be scope-appropriate to sample size. We will not claim "50% improvement" without statistical power to support it.

## Sample Size and Scope

### Pipeline B (MVFP)

- **Type**: Qualitative pilot / feasibility demonstration
- **Auditors**: N=1-2 (researcher + one volunteer if available)
- **Cases**: N=5-10 curated failure scenarios
- **Design**: Think-aloud protocol with time tracking
- **Outcome**: "This approach is feasible and promising" (not statistical claims)
- **Limitations**: Cannot generalize; author involvement noted

### Pipeline A (Full)

- **Type**: Quantitative study with confidence intervals
- **Auditors**: N=8-12 (recruited, compensated, diverse backgrounds)
- **Cases**: N=20-30 (stratified across F1-F5 failure types)
- **Design**: Randomized assignment to conditions; blind to hypotheses
- **Outcome**: Publishable effect sizes with confidence intervals
- **Power**: Sufficient for medium effect size detection (d=0.5)

## Bias Mitigation

| Risk | Mitigation |
| ---- | ---------- |
| Author-as-evaluator | Protocol pre-registered before data collection; external auditors for Pipeline A |
| Hypothesis awareness | Auditors blind to specific hypotheses; generic "evaluate this tool" framing |
| Cherry-picking | All raw data published alongside results; no post-hoc case selection |
| Reproducibility | Analysis scripts published; random seeds fixed; exact versions documented |
| Overfitting narrative | Limitations section explicitly addresses author involvement and small samples |
| Confirmation bias | Pre-specify what would falsify claims; report null results |
| Selection bias | Auditor recruitment from diverse pools; not just ML experts |

## Falsifiability Conditions

The framework would be considered **not validated** if:

1. Attribution time shows no improvement over Baseline B (p>0.05)
2. Attribution accuracy falls below 70% (worse than guessing with context)
3. Users cannot interpret intent receipts accurately (comprehension <60%)
4. Log completeness falls below 95% (systematic schema failures)
5. Constitutional validator produces >20% false positives (unusable noise)

These conditions will be reported honestly regardless of outcome.

## Pre-Registration Commitment

Before any validation data is collected:

1. This methodology document is timestamped (git commit)
2. Success/failure criteria are locked (no post-hoc threshold adjustment)
3. Analysis plan is specified (statistical tests, effect size calculations)
4. Deviations from plan will be documented and justified
5. Protocol registered on OSF or equivalent before data collection begins

## Data Collection Protocol

### For Each Evaluation Session

1. Auditor receives brief training on interface (5 minutes)
2. Auditor assigned to condition (randomized for Pipeline A)
3. Present failure scenario without revealing root cause
4. Record: time to attribution, attributed cause, confidence rating
5. Reveal ground truth; record accuracy
6. Collect qualitative feedback (what helped, what confused)

### Ground Truth Establishment

- Each case has documented ground truth root cause
- Ground truth established by researcher before evaluation
- Cases drawn from real failure patterns (anonymized if necessary)
- F1-F5 classification applied to each case

## Analysis Plan

### Primary Analysis

- **Attribution time**: Two-sample t-test or Mann-Whitney U (depending on normality)
- **Attribution accuracy**: Chi-square test or Fisher's exact
- **Effect sizes**: Cohen's d for continuous, odds ratio for categorical
- **Confidence intervals**: 95% CI for all point estimates

### Secondary Analysis

- Stratification by F1-F5 failure type
- Stratification by auditor experience level
- Qualitative coding of feedback themes

### Reporting

- All analyses run with published R/Python scripts
- Raw (anonymized) data published alongside paper
- Negative results reported with same rigor as positive

## Timeline

| Phase | Duration | Activities |
| ----- | -------- | ---------- |
| Preparation | 3 days | Finalize cases, test protocol, recruit auditors |
| Pilot (Pipeline B) | 3 days | N=1-2 auditors, N=5-10 cases, iterate protocol |
| Main study (Pipeline A) | 5 days | N=8-12 auditors, N=20-30 cases |
| Analysis | 3 days | Run analyses, generate figures, draft results |
| Write-up | 3 days | Complete paper sections, limitations, discussion |

---

## V&T

- Created: 2026-01-19T05:41:00Z
- Status: COMPLETE
- Blocked by: nothing
