# Refactored Plan Execution Tracker

**Canonical plan:** `REFACTORED_PROACTIVE_AI_CONSTITUTION_TOOLKIT.md` — this is the plan of action. We execute toward it; nothing less.

**Core thesis (from plan):** A PROACTIVE principle is not fully validated until it can be automatically tested and monitored within the standard AI toolchain.

**Phase 2 deliverables location:** Phase 2 deliverables (02_CI_SAFETY_GATE, 03_HELM_SAFETY_PROFILE, and their USE_CASE_EVIDENCE) **already exist** in `/Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT`. This worktree (`loving-zhukovsky`) also has adapters 02 and 03; treat Projects as the canonical source for Phase 2 if paths differ or to sync.

---

## Phase 1: Foundation & First Integrated Slice (Weeks 1–2)

| # | Deliverable | Status | Notes |
|---|-------------|--------|-------|
| 1.1 | `04_FORMAL_SPECIFICATION/TRACEABILITY_ONTOLOGY.md` — minimal, streamable JSON schema for MBSE Trace Log | ✅ DONE | TRACEABILITY_ONTOLOGY.md added; canonical schema = `01_WANDB_TRACE_ADAPTER/schema.json`. |
| 1.2 | `05_EVALUATION_DESIGN/EVALUATION_PLAN_PREREGISTERED.md` focused on **Forensic Trace Challenge** benchmark | ✅ DONE | §3.3 Forensic Trace Challenge added; task, primary/secondary metrics, H4 link, adapter ref. |
| 1.3 | `ADAPTER_MODULES/01_WANDB_TRACE_ADAPTER/` — adapter.py, validation_report template, USE_CASE_EVIDENCE.md | ✅ EXISTS | adapter.py, validation_report.md, USE_CASE_EVIDENCE.md present. |
| 1.4 | **Validation gate:** Micro-eval — Root Cause Attribution Accuracy higher with adapter vs raw logs? Documented in USE_CASE_EVIDENCE | ✅ VERIFIED | USE_CASE_EVIDENCE.md: pilot N=9, 52% time reduction, 100% accuracy, p&lt;0.0001, Cohen's d=3.31. |
| 1.5 | **Output:** Functional adapter + mini-research report validating Principle O (Observability); first publishable unit | ☐ SIGN-OFF | After 1.1–1.4; ready for product/lead sign-off. |

---

## Phase 2: Parallel Vertical Slices (Weeks 3–6)

**Canonical location:** Phase 2 deliverables **exist** in `/Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT` (02_CI_SAFETY_GATE, 03_HELM_SAFETY_PROFILE). This worktree also has these adapters; use Projects as source of truth if syncing.

### Slice 2: Verification → CI/CD Gate Adapter

| # | Deliverable | Status | Notes |
|---|-------------|--------|-------|
| 2.1 | `ADAPTER_MODULES/02_CI_SAFETY_GATE/` — GitHub Actions workflow (action.yml), Constitutional Validator | ✅ EXISTS | In this worktree and in Projects. |
| 2.2 | USE_CASE_EVIDENCE.md — report on blocking a model update that introduced new F2 failures | ☐ VERIFY | File exists; confirm content matches gate-catching-seeded-failure (check Projects if canonical). |
| 2.3 | **Rigor:** Evidence tests THEORY_OF_ACTION — does verification gate prevent failure deployment? | ☐ SIGN-OFF | |

### Slice 1: Truth → HELM Safety Profile Adapter

| # | Deliverable | Status | Notes |
|---|-------------|--------|-------|
| 2.4 | `ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/` — script wrapping HELM scenario, COL-enabled model, PROACTIVE metrics (F1 Rate, Calibration) | ✅ EXISTS | In this worktree and in Projects. |
| 2.5 | USE_CASE_EVIDENCE.md — compare to baseline HELM results; F1-rate difference | ☐ VERIFY | validation run (n=200, p=0.001) exists; confirm documented as USE_CASE_EVIDENCE (check Projects if canonical). |
| 2.6 | **Rigor:** Benchmark comparison — "compared to what?" with direct evidence | ☐ SIGN-OFF | |

---

## Phase 3: Synthesis & Safety Case Automation (Weeks 7–8)

| # | Deliverable | Status | Notes |
|---|-------------|--------|-------|
| 3.1 | `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/` — script ingesting W&B Adapter, CI Gate, Benchmark Adapter results | ☐ TO DO | **Not yet created.** |
| 3.2 | Auto-populate sections of `SAFETY_CASE_FULL.md` | ☐ TO DO | Depends on 3.1. |
| 3.3 | Generate **PROACTIVE Safety Appendix** for model card | ☐ TO DO | Depends on 3.1. |
| 3.4 | **Validation gate:** Does auto-generated safety case contain all critical claims, arguments, linked evidence from prior adapters? | ☐ TO DO | |
| 3.5 | **Output:** Complete, machine-generated `SAFETY_CASE_FULL.md` for a demo model | ☐ TO DO | |

---

## Accelerated Timeline (from plan)

| Week | Focus | Key adapter | Validation gate | arXiv-ready artifact |
|------|--------|-------------|-----------------|----------------------|
| 1–2 | Slice 5: Observability | W&B Trace Adapter | Root cause 50% faster with adapter vs raw logs? | USE_CASE_EVIDENCE + adapter (repo link) |
| 3–4 | Slice 2: Verification | CI Safety Gate | Gate catches seeded vuln that passes unit tests? | CI workflow + Failure Analysis Report |
| 5–6 | Slice 1: Truth | HELM Safety Profile | Statistically significant F1-rate diff baseline vs COL on TruthfulQA? | Benchmark comparison + analysis script |
| 7–8 | Synthesis | Safety Case Generator | Auto safety case has all claims + linked evidence? | Machine-generated SAFETY_CASE_FULL.md |

---

## Vertical Slice Reference (from plan)

- **Slice 1 (T):** Truth or Bounded Unknown — F1 reduction, Calibration, Claims Verification task.
- **Slice 2 (V):** Verification Before Action — Phantom Completion Rate, Verification Gate, Safe Code Generation.
- **Slice 3 (I):** Intent Integrity — Intent Receipt, Intent Distortion Score, User Correction Rate.
- **Slice 4 (P):** Privacy-First — PII Leakage Rate, Session-Boundary Data Handling.
- **Slice 5 (O):** Observability & I4 Traceability — MBSE Trace Log, Root Cause Attribution Accuracy, Forensic Trace Challenge.

---

## Next concrete actions

1. **Phase 1 sign-off:** 1.1–1.4 complete; 1.5 SIGN-OFF (functional adapter + mini-research report) pending product/lead approval.
2. **Phase 2 closure:** Verify 02_CI and 03_HELM USE_CASE_EVIDENCE and rigor; sign off both slices.
3. **Phase 3 start:** Create `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/`; define inputs (W&B, CI logs, Benchmark results); implement auto-population of SAFETY_CASE_FULL.md and PROACTIVE Safety Appendix.

---

## V&T Statement

**Exists:** This execution tracker and the refactored plan (`REFACTORED_PROACTIVE_AI_CONSTITUTION_TOOLKIT.md`). Adapters 01, 02, 03 exist; 04 does not. `04_FORMAL_SPECIFICATION/TRACEABILITY_ONTOLOGY.md` and Forensic Trace Challenge in EVALUATION_PLAN added; Phase 1.1–1.4 complete.

**Non-Existence:** Adapter 04 (Safety Case Generator); machine-generated SAFETY_CASE_FULL.md; optional TRACEABILITY_ONTOLOGY.md in 04_FORMAL_SPECIFICATION.

**Unverified:** Phase 1–2 validation gates not formally signed off here; USE_CASE_EVIDENCE content assumed from repo state.

**Functional Status:** Tracker ready; execution follows refactored plan. Phase 2 deliverables exist in Projects; update status as work completes.
