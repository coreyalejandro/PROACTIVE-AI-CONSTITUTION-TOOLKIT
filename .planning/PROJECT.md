# PROACTIVE AI Constitution Toolkit

## What This Is

A practical toolkit that bridges the gap between AI ethics research and engineering practice. Provides adapter modules that integrate constitutional AI constraints into existing ML infrastructure (W&B, CI/CD, HELM benchmarks) to enable auditable, verifiable AI safety guarantees.

## Core Value

**Prove constitutional AI constraints are enforceable through existing tools.** Every adapter must demonstrate measurable improvement in safety observability, traceability, or verification.

## Current Milestone: v1.1 CI Safety Gate + HELM

**Goal:** Complete CI Safety Gate validation and begin HELM Safety Profile integration to extend constitutional verification into benchmark evaluation.

**Target features:**
- CI Safety Gate validation study demonstrating violation detection
- GitHub Actions workflow enforcing constitutional checks
- HELM Safety Profile adapter translating PROACTIVE invariants to benchmark metrics

## Requirements

### Validated

<!-- Shipped and confirmed valuable in v1.0. -->

- ✓ **Trace Log Schema** — PROACTIVE trace format with I1-I6 validator results (v1.0)
- ✓ **W&B Integration** — Trace logs to W&B Tables for auditor analysis (v1.0)
- ✓ **Validation Evidence** — 52% reduction in root cause attribution time (v1.0)
- ✓ **Safety Case Integration** — Adapter evidence linked to safety case strands (v1.0)
- ✓ **CI Validator Core** — I1-I6 invariant checks for model outputs (v1.0)
- ✓ **Test Cases** — Seeded violations for validation testing (v1.0)
- ✓ **Foundation Docs** — Funding materials and execution infrastructure (v1.0)
- ✓ **Evaluation Methodology** — Pre-registered evaluation design (v1.0)

### Active

<!-- Current scope for v1.1. -->

- [ ] CI Safety Gate validation study (A02-T5)
- [ ] CI Safety Gate documentation integration (A02-T6)
- [ ] GitHub Actions workflow wiring (uses CI Safety Gate action)
- [ ] HELM Safety Profile schema definition (A03-T1)
- [ ] HELM adapter structure (A03-T2)
- [ ] HELM adapter core implementation (A03-T3)
- [ ] HELM adapter documentation (A03-T4)
- [ ] HELM validation study (A03-T5)
- [ ] HELM documentation integration (A03-T6)

### Out of Scope

<!-- Explicit boundaries for v1.1. -->

- Safety Case Generator (A04) — Deferred to v1.2+, requires A03 completion
- External auditor validation — Requires funding for participant compensation
- Red team testing — Requires adversarial testing expertise
- Multi-evaluator validation — Deferred; acknowledge single-evaluator bias in limitations

## Context

**Technical environment:**
- Python 3.11+ with W&B SDK, PyTest
- GitHub Actions for CI/CD
- HELM benchmark framework for evaluation
- Safety case methodology (GSN-style argument notation)

**Prior work established:**
- I1-I6 constitutional invariants (Identity through Verifiability)
- PROACTIVE trace schema with validator results
- W&B adapter demonstrating 52% improvement in root cause attribution
- CI Safety Gate with 8 seeded test cases (tc01-tc08)

**Known issues to address:**
- GitHub Actions workflow not yet enforcing CI Safety Gate
- Single evaluator bias in A01 validation (documented in limitations)
- Safety Case Evidence E-V1 pending A02-T5 completion
- SARIF upload uses continue-on-error: true (needs review)

## Constraints

- **Tech stack**: Python, W&B SDK, GitHub Actions, HELM — no new dependencies without justification
- **Evidence standard**: Every adapter must demonstrate measurable improvement with statistical validation
- **Neurodivergent-first execution**: Tasks tiered by cognitive load (RED/YELLOW/GREEN)
- **Context resilience**: Context recovery docs maintained for session continuity

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Use neurodivergent-first execution design | Reduce cognitive overhead, improve consistency | ✓ Good |
| Author-as-evaluator for pilot validation | Resource constraint; bias acknowledged in limitations | ⚠️ Revisit for A03 |
| I1-I6 invariant structure | Maps to PROACTIVE principles, testable | ✓ Good |
| Defer A04 to v1.2+ | A03 completion needed first | — Pending |

---
*Last updated: 2026-01-23 after v1.1 milestone initialization*
