# EVALUATION_PLAN_PREREGISTERED.md

**Version:** 1.0.0  
**Status:** Pre-Registration Draft  
**Date:** 2026-01-18  
**Framework:** PROACTIVE AI Constitution  
**Registration Target:** OSF / arXiv appendix  

---

## 1. EXECUTIVE SUMMARY

This document constitutes the pre-registered evaluation plan for the PROACTIVE AI Constitution framework. Pre-registration establishes scientific rigor by specifying hypotheses, methods, and analysis plans before data collection, preventing post-hoc rationalization and p-hacking.

**Core Claim Under Test:** The PROACTIVE framework—comprising the Cognitive Operating Layer (COL), Six Invariants (I1-I6), and MBSE trace chain—reduces epistemic reliability failures (F1-F5) compared to baseline systems, with measurable improvements in safety-critical dimensions.

---

## 2. HYPOTHESES

### 2.1 Primary Hypotheses

| ID | Hypothesis | Falsification Criterion |
|----|------------|------------------------|
| H1 | Full PROACTIVE stack reduces F1 (confident false claims) rate by ≥30% vs. no-PROACTIVE baseline | F1 rate difference < 30% or not statistically significant (p > 0.05) |
| H2 | Full PROACTIVE stack reduces F2 (phantom completion) rate by ≥50% vs. no-PROACTIVE baseline | F2 rate difference < 50% or not statistically significant |
| H3 | I6 (Fail-Closed) enforcement produces deterministic halt on all injected invariant violations | Any violation proceeds without halt |
| H4 | Trace chain completeness (REQ→CTRL→TEST→EVID→DECISION) exceeds 95% on standard tasks | Completeness < 95% |
| H5 | Users can correctly identify missing evidence from intent receipts ≥80% of the time | Identification accuracy < 80% |

### 2.2 Secondary Hypotheses

| ID | Hypothesis | Falsification Criterion |
|----|------------|------------------------|
| H6 | COL compilation adds <500ms latency on 95th percentile of requests | p95 latency ≥ 500ms |
| H7 | Partial PROACTIVE (trace-only) outperforms no-PROACTIVE but underperforms full stack | Ordering violation |
| H8 | Adversarial prompt injection success rate decreases ≥40% with constitutional gates | Decrease < 40% |
| H9 | F3 (persistence under correction) approaches zero with I1 enforcement | F3 rate > 5% |
| H10 | Cross-episode F5 recurrence eliminated with session boundary enforcement | Any F5 recurrence detected |

### 2.3 Null Hypotheses (Explicitly Stated)

- H0₁: PROACTIVE produces no measurable reduction in F1-F5 failure rates
- H0₂: Trace chains are "theater"—present but non-binding
- H0₃: COL overhead exceeds safety benefits
- H0₄: Users cannot interpret intent receipts effectively

---

## 3. EXPERIMENTAL DESIGN

### 3.1 Conditions

| Condition | Code | Components Active | Purpose |
|-----------|------|-------------------|---------|
| No PROACTIVE | C0 | None | Baseline: Raw model output |
| Policy-Only | C1 | System prompt constraints | Ablation: Soft guidance only |
| Trace-Only | C2 | Trace chain without gates | Ablation: Observability without enforcement |
| Validator-Only | C3 | I1-I6 gates without COL | Ablation: Enforcement without intent compilation |
| COL-Only | C4 | COL without validator | Ablation: Intent compilation without enforcement |
| Full PROACTIVE | C5 | COL + Validator + Trace | Full stack |
| Alt-Guardrails | C6 | External guardrail system | External baseline comparison |

### 3.2 Task Distribution

Tasks are drawn from three benchmark layers (see BENCHMARK_TASK_SETS.md):

| Layer | Task Count | Condition Allocation |
|-------|------------|---------------------|
| L1: Reliability-as-Safety | 200 tasks | All conditions |
| L2: Ambiguity & Intent | 150 tasks | All conditions |
| L3: Adversarial | 150 tasks | C0, C5, C6 only |

**Total:** 500 unique tasks × 7 conditions = 3,500 evaluation runs (L3 restricted)

### 3.3 Randomization

- Task presentation order: Block-randomized within layers
- Condition assignment: Latin square design for order effects
- Seed values: Pre-registered seeds (42, 137, 256, 512, 1024) for reproducibility

---

## 4. BASELINE SPECIFICATION

### 4.1 Internal Baselines

| Baseline | Rationale | Expected Behavior |
|----------|-----------|-------------------|
| C0 (No PROACTIVE) | Establishes floor performance | Standard model failure rates |
| C1 (Policy-Only) | Tests soft constraint effectiveness | Modest improvement over C0 |
| C2-C4 (Partial) | Component attribution | Ordered improvement toward C5 |

### 4.2 External Baselines

| System | Selection Rationale |
|--------|---------------------|
| Claude baseline (no constitution) | Anthropic model without PROACTIVE |
| GPT-4 + custom guardrails | Competing approach |
| Llama-Guard | Open-source safety baseline |

### 4.3 Baseline Integrity Requirements

- All baselines use identical prompts (minus PROACTIVE-specific instructions)
- Temperature fixed at 0.0 for determinism
- Token limits standardized across conditions
- No post-hoc baseline selection

---

## 5. METRICS (Summary)

Full specification in METRICS_SPECIFICATION.md. Key metrics:

| Metric | Primary/Secondary | Hypothesis Link |
|--------|-------------------|-----------------|
| F1 Rate (Overconfidence) | Primary | H1 |
| F2 Rate (Phantom Work) | Primary | H2 |
| F3 Rate (Correction Persistence) | Secondary | H9 |
| F4 Rate (Harm Coupling) | Primary | H1-H3 |
| F5 Rate (Cross-Episode) | Secondary | H10 |
| Trace Completeness | Primary | H4 |
| Fail-Closed Correctness | Primary | H3 |
| User Comprehension | Primary | H5 |
| Latency Overhead | Secondary | H6 |

---

## 6. ELICITATION METHODS

### 6.1 Standard Elicitation

All tasks use consistent prompting:
- Zero-shot baseline
- Chain-of-thought when task requires reasoning
- Tool-use forcing when tools are available

### 6.2 Under-Elicitation Controls

To avoid inflated failure rates from poor prompting:
- Best-of-N sampling (N=3) for ambiguous cases
- Structured output formats for measurable responses
- Explicit confidence calibration prompts

### 6.3 Adversarial Elicitation (L3 Only)

- Progressive jailbreak attempts (10 variants per task)
- Tool-poisoning injection
- Multi-turn manipulation sequences

---

## 7. STOPPING RULES

### 7.1 Early Stopping Criteria

| Criterion | Threshold | Action |
|-----------|-----------|--------|
| Critical failure rate | >50% F1+F2 combined | Halt condition, investigate |
| System instability | >10% trace chain breaks | Halt, debug infrastructure |
| Inter-rater disagreement | κ < 0.6 | Halt annotation, recalibrate |

### 7.2 Completion Criteria

- Minimum 90% task completion per condition
- All pre-registered seeds executed
- Human evaluation quota met (N=50 per condition for H5)

### 7.3 No Early Peeking

- Analysis scripts locked until data collection complete
- Intermediate results not used to modify protocol
- Deviations documented and justified

---

## 8. ANALYSIS PLAN

### 8.1 Primary Analysis

| Hypothesis | Test | Effect Size |
|------------|------|-------------|
| H1-H2 | Chi-square with Bonferroni correction | Odds ratio |
| H3 | Exact binomial (deterministic claim) | Pass/fail |
| H4 | One-sample t-test against 95% threshold | Cohen's d |
| H5 | One-sample proportion test against 80% | Risk ratio |

### 8.2 Secondary Analysis

- ANOVA across conditions (C0-C6) for F1-F5 rates
- Ablation effect sizes via planned contrasts
- Latency distribution analysis (KS test)

### 8.3 Robustness Checks

- Sensitivity analysis with alternative thresholds (±10%)
- Bootstrap confidence intervals (10,000 samples)
- Leave-one-task-out cross-validation for generalization

---

## 9. BLINDING PROTOCOL

### 9.1 Annotator Blinding

- Annotators blind to condition during rating
- Output presentation randomized, condition labels stripped
- Post-hoc condition assignment for analysis

### 9.2 Analyst Blinding

- Primary analyst does not see condition labels during scoring
- Secondary analyst performs unblinded verification
- Discrepancies resolved by third-party adjudication

### 9.3 Inter-Rater Reliability

- Minimum 20% double-annotation
- Target κ ≥ 0.7 (substantial agreement)
- Disagreements resolved by consensus, not majority vote

---

## 10. PROGRESSIVE DIFFICULTY DESIGN

Following RSP-style conservative evaluation:

### 10.1 Difficulty Tiers

| Tier | Description | When Applied |
|------|-------------|--------------|
| D1 | Standard tasks, no adversarial pressure | All conditions |
| D2 | Edge cases, ambiguous inputs | All conditions |
| D3 | Active adversarial attempts | C0, C5, C6 |
| D4 | Multi-step, long-horizon scenarios | C0, C5, C6 |
| D5 | Distribution shift (OOD inputs) | C5 only |

### 10.2 Escalation Rules

- Advance to D(n+1) only if D(n) pass rate ≥ 90%
- D3+ results reported separately (not pooled with D1-D2)
- D5 results treated as exploratory (not confirmatory)

---

## 11. DATA GOVERNANCE

### 11.1 Storage

- All evaluation data versioned in git-lfs
- Configuration hashes logged per run
- Deterministic replay guaranteed via seed + config

### 11.2 Retention

- Raw outputs retained for 5 years minimum
- Annotator judgments anonymized after analysis
- Adversarial attack corpora access-controlled

### 11.3 Reproducibility Package

- One-command execution: `./run_evaluation.sh --seed=42`
- Docker container with pinned dependencies
- Environment manifest included

---

## 12. DEVIATION DOCUMENTATION

Any deviation from this pre-registered plan will be:

1. Documented in EVALUATION_DEVIATIONS.md
2. Justified with rationale
3. Flagged in publication
4. Sensitivity analysis performed with/without deviation

---

## 13. PRE-REGISTRATION ATTESTATION

**I attest that:**
- This evaluation plan was written before data collection
- Hypotheses were specified before seeing results
- Analysis methods were selected based on study design, not outcomes
- Deviations will be transparently reported

**Pre-registration date:** 2026-01-18  
**Registration ID:** [To be assigned upon OSF submission]

---

## APPENDICES

### A. Task ID Ranges

| Layer | ID Range | Count |
|-------|----------|-------|
| L1 | L1-001 to L1-200 | 200 |
| L2 | L2-001 to L2-150 | 150 |
| L3 | L3-001 to L3-150 | 150 |

### B. Seed Schedule

| Run | Seed |
|-----|------|
| 1 | 42 |
| 2 | 137 |
| 3 | 256 |
| 4 | 512 |
| 5 | 1024 |

### C. Power Analysis

- Minimum detectable effect: 15% absolute difference
- Power: 0.80
- Alpha: 0.05 (Bonferroni-adjusted for 10 primary tests = 0.005)
- Required N per condition: 200 tasks

---

## DOCUMENT PROVENANCE

| Field | Value |
|-------|-------|
| Created | 2026-01-18 |
| Framework Version | PROACTIVE v2.0 |
| Linked Documents | BENCHMARK_TASK_SETS.md, METRICS_SPECIFICATION.md |
| Status | Pre-Registration Draft |
