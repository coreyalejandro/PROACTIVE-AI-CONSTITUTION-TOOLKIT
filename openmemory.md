# OpenMemory Guide: PROACTIVE-AI-CONSTITUTION-TOOLKIT

## Overview

The PROACTIVE AI Constitution Toolkit is a research framework for building epistemic reliability into AI systems through a structured Constitution + Operational Layer (COL) approach. It addresses five failure modes (F1-F5) through nine PROACTIVE principles and six invariant gates (I1-I6).

## Architecture

### Directory Structure

| Directory | Purpose | Status |
| --- | --- | --- |
| `01_FOUNDATIONS/` | Core framework documents (Constitution, Theory of Change/Action, PRD) | Complete (6 docs) |
| `02_PROGRAM_GOVERNANCE/` | Governance protocols | Stub |
| `03_LITERATURE_POSITIONING/` | Related work analysis | Stub |
| `04_FORMAL_SPECIFICATION/` | Formal specifications | Stub |
| `05_EVALUATION_DESIGN/` | Evaluation methodology, benchmarks, metrics | Complete (4 docs) |
| `06_DATA_QUALITY/` | Data quality protocols | Stub |
| `07_ANALYSIS_TEMPLATES/` | Analysis templates | Stub |
| `08_PUBLICATION/` | Publication materials | Stub |
| `09_SAFETY_CASE/` | Safety case documentation | Stub |
| `FUNDING_MATERIALS/` | Elevator pitch, budget, positioning | Created |
| `TASK_MANAGEMENT/` | Execution infrastructure | Complete |
| `ADAPTER_MODULES/` | Adapter implementations (01-04) | In Progress |

### Key Documents

- **PROACTIVE_AI_CONSTITUTION.md**: Master organizing principle defining P-R-O-A-C-T-I-V-E
- **THEORY_OF_CHANGE.md**: Threat model (F1-F5 failure modes) and problem statement
- **THEORY_OF_ACTION.md**: Causal model and intervention design
- **PRD_COL_PROACTIVE_MBSE.md**: Implementation specification with MBSE bridge

## User Defined Namespaces

- [Leave blank - user populates]

## Components

| Component | Location | Purpose |
| --- | --- | --- |
| Foundation Docs | `01_FOUNDATIONS/` | Core framework specification |
| Evaluation Design | `05_EVALUATION_DESIGN/` | Pre-registered evaluation methodology |
| Execution Infrastructure | `TASK_MANAGEMENT/` | DAG, pipelines, manifest, task backlogs |
| Funding Materials | `FUNDING_MATERIALS/` | Pitch, budget, researcher positioning |
| W&B Trace Adapter | `ADAPTER_MODULES/01_WANDB_TRACE_ADAPTER/` | Trace log → W&B Tables (A01 COMPLETE) |
| CI Safety Gate | `ADAPTER_MODULES/02_CI_SAFETY_GATE/` | GitHub Actions constitutional validator (A02-T1-T4 COMPLETE) |
| CI Safety Gate Test Cases | `ADAPTER_MODULES/02_CI_SAFETY_GATE/test_cases/` | 8 seeded I1-I6 test cases (all pass) |
| Safety Case Skeleton | `09_SAFETY_CASE/SAFETY_CASE_SKELETON.md` | GSN structure with E-O1 evidence integrated |

## Patterns

### Document Structure

- All documents end with V&T (Verification & Truth) statement
- Status tracked as: NOT_STARTED | IN_PROGRESS | COMPLETE | BLOCKED | SKIPPED
- Cognitive load tiers: RED (Tier 1) / YELLOW (Tier 2) / GREEN (Tier 3)

### Task Management

- Tasks organized by Adapter (A01-A04) and sub-task (T1-T6)
- Two pipelines: B (2-week MVP) and A (4-week full)
- Recovery checkpoints: CP0 (foundation) → CP1 (demo) → CP2 (mini-paper) → CP3 (full paper) → CP4 (release)

---

Last updated: 2026-01-23 | v1.0 MILESTONE SHIPPED (Pipeline B MVP complete)

## Milestone Status

**v1.0 Pipeline B MVP:** SHIPPED 2026-01-23

- P0 Foundation: 9/9 COMPLETE
- A01 W&B Trace Adapter: 6/6 COMPLETE (E-O1 evidence integrated)
- A02 CI Safety Gate: 4/6 COMPLETE (T5-T6 deferred to v1.1)

**Archive:** `.planning/milestones/v1.0-*`

**Next:** v1.1 - Complete A02 validation, wire GitHub Actions, begin A03 HELM
