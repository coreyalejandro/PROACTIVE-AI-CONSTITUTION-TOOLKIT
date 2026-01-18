# 05_EVALUATION_DESIGN

## Status: ⚠️ TO CREATE — ⭐ PRIORITY

This directory will contain Stage 4 artifacts for modern, credible evaluations.

**This is the highest priority directory for arXiv publication.**

## Planned Documents

| Document | Purpose | Priority |
|----------|---------|----------|
| EVALUATION_PLAN_PREREGISTERED.md | Hypotheses, metrics, baselines, stopping rules | **P0** |
| BASELINE_SUITE_DEFINITION.md | No-framework, partial, alternative, ablated baselines | **P1** |
| BENCHMARK_TASK_SETS.md | Reliability-as-safety, ambiguity, adversarial layers | **P0** |
| METRICS_SPECIFICATION.md | Epistemic calibration, refusal rate, traceability completeness | **P0** |
| RED_TEAM_PROTOCOL.md | Modular attack scaffolds, long-horizon sabotage probes | **P2** |
| HUMAN_FACTORS_PROTOCOL.md | User comprehension study design | **P2** |

## Creation Criteria

These documents should be created **FIRST** because:
- arXiv reviewers expect pre-registration or equivalent rigor
- No empirical claim is defensible without benchmarks
- Metrics operationalize what "success" means

## Specification: EVALUATION_PLAN_PREREGISTERED.md

### Required Sections
1. **Hypotheses** (H1–Hn) with directional predictions
2. **Primary/secondary metrics** with success thresholds
3. **Baseline conditions** and comparison logic
4. **Sample size justification**
5. **Stopping rules** (when to halt evaluation)
6. **Deviation protocol** (how to document changes)

## Specification: BENCHMARK_TASK_SETS.md

### Required Layers
1. **Layer 1 — Reliability-as-Safety**
   - False confident claims under pressure
   - Hallucination provocation scenarios
   - Tool misuse detection tasks

2. **Layer 2 — Ambiguity & Intent Integrity**
   - Underspecified requests
   - Conflicting constraints
   - Implicit vs. explicit intent disambiguation

3. **Layer 3 — Adversarial**
   - Jailbreak pattern variants
   - Obfuscation attacks
   - Indirect prompt injection

## Specification: METRICS_SPECIFICATION.md

### Required Metrics
- Epistemic calibration (overconfidence rate formula)
- Refusal appropriateness / safe completion rate
- Traceability completeness rate (REQ→CTRL→TEST→EVID→DECISION)
- Safety-over-fluency tradeoff curves
- Inter-rater reliability thresholds (κ ≥ 0.7)

---

*Placeholder created: 2026-01-18*
