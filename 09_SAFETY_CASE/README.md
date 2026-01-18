# 09_SAFETY_CASE

## Status: ⚠️ TO CREATE

This directory will contain the synthesis artifact—the complete safety case.

## Planned Documents

| Document | Purpose | Priority |
|----------|---------|----------|
| SAFETY_CASE_FULL.md | Complete claim→argument→evidence synthesis | **P1** |

## Creation Criteria

This document should be created when:
- All evaluation results are complete
- All failure modes are catalogued
- All mitigations are verified

## Specification: SAFETY_CASE_FULL.md

### Safety Case Structure (Goal Structuring Notation)

```
G1: PROACTIVE COL reduces epistemic reliability failures
├── S1: Strategy: Demonstrate via controlled evaluation
│   ├── G1.1: Framework reduces F1-F5 failure rates vs. baseline
│   │   ├── E1: Controlled comparison results (05_EVALUATION)
│   │   └── E2: Statistical significance tests (07_ANALYSIS)
│   │
│   ├── G1.2: Invariant gates cannot be bypassed
│   │   ├── E3: Red team evaluation results (05_EVALUATION)
│   │   └── E4: Failure mode catalog shows no gate bypasses (07_ANALYSIS)
│   │
│   └── G1.3: Trace chain enables meaningful auditability
│       ├── E5: Trace completeness metrics (05_EVALUATION)
│       └── E6: Audit time comparison (07_ANALYSIS)
│
├── S2: Strategy: Demonstrate via human factors validation
│   ├── G1.4: Users can understand intent receipts
│   │   └── E7: User study comprehension results (05_EVALUATION)
│   │
│   └── G1.5: Users can detect missing evidence
│       └── E8: Error detection rate study (05_EVALUATION)
│
└── C1: Context: Applicable to actionable-claim AI systems
    └── A1: Assumption: Users act on AI outputs
```

### Required Sections

#### 1. Executive Summary
- Top-level safety claim
- Evidence strength assessment
- Residual risk acknowledgment

#### 2. Claim Hierarchy
- G1: Top goal
- G1.n: Sub-goals
- S: Strategies linking goals
- E: Evidence items
- A: Assumptions
- C: Context

#### 3. Evidence Mapping

| Claim | Evidence | Source | Strength |
|-------|----------|--------|----------|
| G1.1 | Comparison results | 05_EVALUATION | Strong |
| G1.2 | Red team results | 05_EVALUATION | Medium |
| ... | ... | ... | ... |

#### 4. Assumption Register

| ID | Assumption | Justification | Monitoring |
|----|------------|---------------|------------|
| A1 | Users act on outputs | Domain analysis | Usage telemetry |
| ... | ... | ... | ... |

#### 5. Residual Risks

| Risk | Severity | Likelihood | Mitigation Status |
|------|----------|------------|-------------------|
| Novel attack vectors | High | Medium | Ongoing red-teaming |
| ... | ... | ... | ... |

#### 6. Confidence Assessment

| Claim | Confidence | Rationale |
|-------|------------|-----------|
| G1 | Medium-High | Strong quantitative evidence; some gaps in adversarial coverage |
| G1.1 | High | Multiple controlled studies, consistent results |
| G1.2 | Medium | Red team found no bypasses, but coverage incomplete |
| ... | ... | ... |

#### 7. Update Protocol
- When to revise safety case
- Evidence refresh schedule
- Assumption validation frequency

---

## Anthropic RSP Alignment

The safety case structure aligns with Anthropic's Responsible Scaling Policy by:

1. **Threat pathway coverage:** Misuse, accident, emergent autonomy addressed
2. **Capability-harm mapping:** F1-F5 taxonomy links capabilities to harms
3. **Control evaluation:** Gate architecture provides control mechanism
4. **Evidence standards:** Quantitative thresholds, statistical tests
5. **Uncertainty acknowledgment:** Residual risks explicitly stated

---

*Placeholder created: 2026-01-18*
