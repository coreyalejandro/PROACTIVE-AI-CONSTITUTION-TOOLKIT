# 05_EVALUATION_DESIGN

## Status: ✅ P0 COMPLETE — P1/P2 PENDING

This directory contains Stage 4 artifacts for modern, credible evaluations aligned with arXiv publication standards.

## Document Status

| Document | Purpose | Priority | Status |
|----------|---------|----------|--------|
| EVALUATION_PLAN_PREREGISTERED.md | Hypotheses, metrics, baselines, stopping rules | **P0** | ✅ Complete |
| BENCHMARK_TASK_SETS.md | Reliability-as-safety, ambiguity, adversarial layers | **P0** | ✅ Complete |
| METRICS_SPECIFICATION.md | Epistemic calibration, refusal rate, traceability completeness | **P0** | ✅ Complete |
| BASELINE_SUITE_DEFINITION.md | No-framework, partial, alternative, ablated baselines | **P1** | ⚠️ Pending |
| RED_TEAM_PROTOCOL.md | Modular attack scaffolds, long-horizon sabotage probes | **P2** | ⚠️ Pending |
| HUMAN_FACTORS_PROTOCOL.md | User comprehension study design | **P2** | ⚠️ Pending |

---

## Completed Documents

### EVALUATION_PLAN_PREREGISTERED.md (P0)

Pre-registered evaluation plan establishing scientific rigor for PROACTIVE framework testing.

**Contents:**
- 10 hypotheses (H1-H10) with explicit falsification criteria
- 7 experimental conditions (C0-C6) including ablation configurations
- Baseline specification (internal + external comparisons)
- Blinding protocol for annotators and analysts
- Progressive difficulty design (D1-D5 tiers)
- Stopping rules and deviation documentation protocol
- Analysis plan with statistical tests and effect sizes

**Key Hypotheses:**
- H1: ≥30% reduction in F1 (confident false claims)
- H2: ≥50% reduction in F2 (phantom completion)
- H3: 100% fail-closed on invariant violations
- H4: ≥95% trace chain completeness
- H5: ≥80% user comprehension of intent receipts

---

### BENCHMARK_TASK_SETS.md (P0)

500 evaluation tasks across three layers with 4,070 variants.

**Layer Architecture:**
- **L1: Reliability-as-Safety (200 tasks)** — False confident claims, phantom completion, tool misuse
- **L2: Ambiguity & Intent (150 tasks)** — Underspecified requests, conflicting constraints, implicit assumptions
- **L3: Adversarial (150 tasks)** — Jailbreak patterns, indirect prompt injection, multi-turn manipulation

**Features:**
- Full YAML task schema with expected behaviors
- Distribution shift variants (domain, paraphrase, adversarial)
- Anti-Goodhart challenge sets to prevent metric gaming
- Long-horizon multi-step scenarios (D4 difficulty)
- Human baseline collection protocol

---

### METRICS_SPECIFICATION.md (P0)

25 metrics with operational definitions, measurement procedures, and anti-gaming safeguards.

**Primary Metrics:**
- M-F1 through M-F5: Failure rate metrics mapped to taxonomy
- M-I1 through M-I6: Invariant compliance metrics
- M-HF1 through M-HF3: Human factors metrics

**Key Features:**
- Validity portfolio (content, criterion, robustness) for all primary metrics
- Anti-Goodhart provisions for each metric
- Composite PROACTIVE Safety Score (PSS) formula
- Inter-rater reliability requirements (κ ≥ 0.70)
- Trace fidelity audit protocol for detecting "trace theater"

---

## Remaining Work

### P1: BASELINE_SUITE_DEFINITION.md

Detailed specification of comparison conditions:
- C0: No PROACTIVE (raw model)
- C1-C4: Ablation configurations
- C6: Alternative guardrail systems
- External baselines (Llama-Guard, custom guardrails)

### P2: RED_TEAM_PROTOCOL.md

Adversarial evaluation protocol:
- Attack scaffolding framework
- Long-horizon sabotage probes
- Attacker-defender coevolution process

### P2: HUMAN_FACTORS_PROTOCOL.md

User study design:
- Intent receipt comprehension testing
- Missing evidence detection study
- Over-reliance measurement protocol

---

## Cross-References

| This Document | References | Referenced By |
|---------------|------------|---------------|
| EVALUATION_PLAN_PREREGISTERED.md | BENCHMARK_TASK_SETS.md, METRICS_SPECIFICATION.md | 09_SAFETY_CASE/ |
| BENCHMARK_TASK_SETS.md | F1-F5 taxonomy (Theory of Change), I1-I6 (Constitution) | RED_TEAM_PROTOCOL.md |
| METRICS_SPECIFICATION.md | EVALUATION_PLAN_PREREGISTERED.md | 07_ANALYSIS_TEMPLATES/ |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-18 | P0 documents created |

---

*Last updated: 2026-01-18*
