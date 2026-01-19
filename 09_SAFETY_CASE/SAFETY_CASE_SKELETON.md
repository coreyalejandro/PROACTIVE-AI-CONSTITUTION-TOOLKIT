# PROACTIVE Safety Case Skeleton

## Status: IN DEVELOPMENT

This document provides the skeleton structure for the PROACTIVE safety case, following Goal Structuring Notation (GSN). It synthesizes evidence from adapter modules into a structured argument for epistemic reliability.

---

## Top-Level Goal

**G1**: PROACTIVE COL reduces epistemic reliability failures in AI systems

**Context C1**: Applicable to AI systems where users act on AI outputs (actionable-claim systems)

**Assumption A1**: Users cannot independently verify all AI claims before acting

---

## Argument Structure (GSN)

```
G1: PROACTIVE COL reduces epistemic reliability failures
├── S1: Strategy: Demonstrate via controlled evaluation
│   ├── G1.1: Framework reduces F1-F5 failure rates vs. baseline
│   │   ├── E1: (Pending) Controlled comparison results
│   │   └── E2: (Pending) Statistical significance tests
│   │
│   ├── G1.2: Invariant gates cannot be bypassed
│   │   ├── E3: (Pending) Red team evaluation results
│   │   └── E4: (Pending) Failure mode catalog
│   │
│   └── G1.3: Trace chain enables meaningful auditability
│       ├── E-O1: W&B Adapter pilot results ✓ COMPLETE
│       └── E-O2: (Pending) Full validation study
│
├── S2: Strategy: Demonstrate via human factors validation
│   ├── G1.4: Users can understand intent receipts
│   │   └── E7: (Pending) User study comprehension results
│   │
│   └── G1.5: Users can detect missing evidence
│       └── E8: (Pending) Error detection rate study
│
└── C1: Context: Applicable to actionable-claim AI systems
    └── A1: Assumption: Users act on AI outputs
```

---

## Argument Strands

### Strand O: Observability Enables Auditing

**Sub-Goal G1.3**: Trace chain enables meaningful auditability

**Strategy S-O1**: Demonstrate via tooling evaluation

**Evidence**:

| ID | Description | Source | Status | Confidence |
|----|-------------|--------|--------|------------|
| E-O1 | W&B Trace Adapter pilot results | [USE_CASE_EVIDENCE.md](../ADAPTER_MODULES/01_WANDB_TRACE_ADAPTER/USE_CASE_EVIDENCE.md) | ✅ Complete (Pilot) | Medium |
| E-O2 | Full validation study with external auditors | Adapter 01 Pipeline A | 🔲 Pending | — |

**Claim**: Auditors can identify failure root causes faster with PROACTIVE traces than without

**Supporting Data**:
- 52% reduction in attribution time (Treatment: 5.20 min vs Baseline B: 10.77 min)
- 100% attribution accuracy vs 89% baseline
- Statistical significance: t = 7.016, p < 0.0001, Cohen's d = 3.31

**Current Confidence**: Medium

**Rationale**: Promising pilot results with large effect size, but limited by:
- Author-as-evaluator (potential bias)
- N=9 synthetic test cases (insufficient for generalization)
- Single evaluator (no inter-rater reliability)

**Gaps to Address**:
- [ ] Pipeline A study with 8-12 external auditors
- [ ] Real-world trace logs from PROACTIVE-instrumented systems
- [ ] Pre-registered hypotheses with power analysis
- [ ] Blinded evaluation protocol

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

### Strand I: Invariant Gates Cannot Be Bypassed

**Sub-Goal G1.2**: Invariant gates (I1-I6) cannot be bypassed under adversarial conditions

**Strategy S-I1**: Demonstrate via red team evaluation

**Evidence**:

| ID | Description | Source | Status | Confidence |
|----|-------------|--------|--------|------------|
| E-I1 | Red team protocol results | Adapter 02 | 🔲 Pending | — |
| E-I2 | IT Loop validation | Adapter 02 | 🔲 Pending | — |

**Current Confidence**: Unvalidated

**Gaps to Address**:
- [ ] Implement Adapter 02 (CI Safety Gate)
- [ ] Define red team protocol
- [ ] Execute adversarial testing
- [ ] Document bypass attempts and outcomes

---

### Strand T: Truth Boundaries Are Enforced

**Sub-Goal**: System correctly bounds uncertainty and refuses to claim knowledge it lacks

**Strategy S-T1**: Demonstrate via benchmark evaluation

**Evidence**:

| ID | Description | Source | Status | Confidence |
|----|-------------|--------|--------|------------|
| E-T1 | HELM TruthfulQA results | Adapter 03 | 🔲 Pending | — |
| E-T2 | Calibration metrics | Adapter 03 | 🔲 Pending | — |

**Current Confidence**: Unvalidated

**Gaps to Address**:
- [ ] Implement Adapter 03 (HELM Safety Profile)
- [ ] Run TruthfulQA evaluation
- [ ] Measure calibration (confidence vs accuracy)
- [ ] Document bounded_unknown_rate

---

### Strand V: Verification Precedes Action

**Sub-Goal**: System performs verification checks before claiming success

**Strategy S-V1**: Demonstrate via CI integration

**Evidence**:

| ID | Description | Source | Status | Confidence |
|----|-------------|--------|--------|------------|
| E-V1 | CI gate enforcement results | Adapter 02 | 🔲 Pending | — |

**Current Confidence**: Unvalidated

---

## Evidence Registry

| ID | Description | Source | Status | Links |
|----|-------------|--------|--------|-------|
| E-O1 | W&B Adapter pilot results | Adapter 01 | ✅ Complete (Pilot) | [Report](../ADAPTER_MODULES/01_WANDB_TRACE_ADAPTER/validation_report.md), [Evidence](../ADAPTER_MODULES/01_WANDB_TRACE_ADAPTER/USE_CASE_EVIDENCE.md) |
| E-O2 | W&B Adapter full study | Adapter 01 | 🔲 Pending | — |
| E-I1 | Red team results | Adapter 02 | 🔲 Pending | — |
| E-I2 | IT Loop validation | Adapter 02 | 🔲 Pending | — |
| E-T1 | HELM TruthfulQA results | Adapter 03 | 🔲 Pending | — |
| E-T2 | Calibration metrics | Adapter 03 | 🔲 Pending | — |
| E-V1 | CI gate enforcement | Adapter 02 | 🔲 Pending | — |

---

## Assumption Register

| ID | Assumption | Justification | Monitoring | Status |
|----|------------|---------------|------------|--------|
| A1 | Users act on AI outputs | Domain analysis: actionable-claim systems | Usage telemetry | Active |
| A2 | Users cannot verify all claims | Cognitive load constraints | User study | Assumed |
| A3 | Trace logs are tamper-evident | Cryptographic hashing | Audit | Design assumption |

---

## Residual Risks

| Risk | Severity | Likelihood | Mitigation | Status |
|------|----------|------------|------------|--------|
| Novel attack vectors not covered by red team | High | Medium | Ongoing adversarial testing | 🔲 Pending |
| Trace chain gaps in complex workflows | Medium | Medium | Automated completeness checking | Partial (I4) |
| User misinterpretation of epistemic tags | Medium | Low | UX study, progressive disclosure | 🔲 Pending |
| Performance degradation at scale | Low | Medium | Load testing, optimization | 🔲 Pending |

---

## Confidence Assessment

| Claim | Confidence | Rationale |
|-------|------------|-----------|
| G1 (Top-level) | Low | Only one evidence strand partially validated |
| G1.1 (F1-F5 reduction) | Unvalidated | No controlled comparison yet |
| G1.2 (Gate bypass) | Unvalidated | No red team testing yet |
| G1.3 (Auditability) | Medium | E-O1 pilot complete with limitations |
| G1.4 (User comprehension) | Unvalidated | No user study yet |
| G1.5 (Error detection) | Unvalidated | No user study yet |

---

## Update Protocol

### When to Revise

- New evidence collected from adapter validation
- Red team discovers bypass vulnerability
- User study reveals comprehension issues
- Assumption invalidated by new data

### Evidence Refresh Schedule

| Evidence | Refresh Trigger | Owner |
|----------|-----------------|-------|
| E-O1 | Pipeline A study completion | Adapter 01 |
| E-I1 | Red team cycle completion | Adapter 02 |
| E-T1 | HELM evaluation completion | Adapter 03 |

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-01-19 | Initial skeleton with E-O1 evidence |

---

## Anthropic RSP Alignment

This safety case structure aligns with Anthropic's Responsible Scaling Policy:

1. **Threat pathway coverage**: F1-F5 taxonomy addresses misuse, accident, and reliability failures
2. **Capability-harm mapping**: Each failure mode links to specific harms
3. **Control evaluation**: I1-I6 invariants provide control mechanisms
4. **Evidence standards**: Quantitative thresholds, statistical tests, effect sizes
5. **Uncertainty acknowledgment**: Confidence levels and limitations explicitly stated

---

## V&T Statement

### EXISTS
- Safety case skeleton with GSN structure
- Argument Strand O with E-O1 evidence integrated
- Evidence registry with status tracking
- Assumption register
- Residual risk catalog
- Confidence assessment matrix
- Bi-directional links to Adapter 01 evidence

### FUNCTIONAL STATUS
- Strand O: Partially validated (pilot evidence)
- Strands I, T, V: Unvalidated (pending adapter implementation)
- Top-level claim: Low confidence (single evidence strand)

### NOT CLAIMED
- Full validation of any argument strand
- External auditor verification
- Red team bypass testing
- User comprehension validation
- Generalization beyond synthetic test cases

---

*Created: 2026-01-19 | A01-T6 | Session 8*
