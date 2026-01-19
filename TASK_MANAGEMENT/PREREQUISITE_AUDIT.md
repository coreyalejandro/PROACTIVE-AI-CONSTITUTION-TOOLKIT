# Prerequisite Audit: PROACTIVE Toolkit

## Audit Date: 2026-01-19
## Auditor: Claude (Session 3)

---

## Document Status Matrix

| Document | Expected Path | Status | Completeness | Blocking |
|----------|---------------|--------|--------------|----------|
| PRD_COL_PROACTIVE_MBSE.md | 01_FOUNDATIONS/ | **EXISTS** | 95% | Adapter 02, 04 |
| TRACEABILITY_ONTOLOGY.md | 04_FORMAL_SPECIFICATION/ | **MISSING** | 0% | **Adapter 01** |
| FORMAL_SPEC_PRINCIPLE_T.md | 04_FORMAL_SPECIFICATION/ | **MISSING** | 0% | Adapter 03 |
| EVALUATION_PLAN_PREREGISTERED.md | 05_EVALUATION_DESIGN/ | **EXISTS** | 100% | Adapter 01, 03 |
| BENCHMARK_TASK_SETS.md | 05_EVALUATION_DESIGN/ | **EXISTS** | 100% | Adapter 03 |
| RED_TEAM_PROTOCOL.md | 05_EVALUATION_DESIGN/ | **MISSING** | 0% | Adapter 02 |
| METRICS_SPECIFICATION.md | 05_EVALUATION_DESIGN/ | **EXISTS** | 100% | Adapter 01, 03 |
| EVALUATION_METHODOLOGY.md | TASK_MANAGEMENT/ | **EXISTS** | 100% | Adapter 01 |
| SAFETY_CASE_SKELETON.md | 09_SAFETY_CASE/ | **MISSING** (README only) | 15% | Adapter 01 (T6) |

---

## Document Assessments

### EXISTS - Full Assessment

#### PRD_COL_PROACTIVE_MBSE.md (95% Complete)
- **Location**: `01_FOUNDATIONS/PRD_COL_PROACTIVE_MBSE.md`
- **Size**: 13,622 bytes
- **Contains**: System architecture, COL specification, IT Loop, I1-I6 validator pseudocode, MBSE trace chain structure, Intent Receipt UX
- **Missing for 100%**: Concrete interface definitions (currently pseudocode), performance requirements
- **Usable for**: Adapter 02 (IT Loop), Adapter 04 (Monitor Dashboard)

#### EVALUATION_PLAN_PREREGISTERED.md (100% Complete)
- **Location**: `05_EVALUATION_DESIGN/EVALUATION_PLAN_PREREGISTERED.md`
- **Size**: 10,660 bytes
- **Contains**: H1-H10 hypotheses, experimental design (C0-C6 conditions), baselines, metrics summary, elicitation methods, stopping rules, analysis plan, blinding protocol
- **Usable for**: Adapter 01 (validation framework), Adapter 03 (benchmark runner)

#### BENCHMARK_TASK_SETS.md (100% Complete)
- **Location**: `05_EVALUATION_DESIGN/BENCHMARK_TASK_SETS.md`
- **Size**: 17,263 bytes
- **Contains**: 500 base tasks (L1-L3 layers), task schema, anti-Goodhart challenges, distribution shift variants, long-horizon tasks
- **Usable for**: Adapter 03 (benchmark runner)

#### METRICS_SPECIFICATION.md (100% Complete)
- **Location**: `05_EVALUATION_DESIGN/METRICS_SPECIFICATION.md`
- **Size**: 20,586 bytes
- **Contains**: 25 metrics (F1-F5, I1-I6, human factors, operational), scoring rubrics, anti-Goodhart provisions, measurement procedures
- **Usable for**: Adapter 01 (trace schema), Adapter 03 (scoring)

#### EVALUATION_METHODOLOGY.md (100% Complete)
- **Location**: `TASK_MANAGEMENT/EVALUATION_METHODOLOGY.md`
- **Size**: 6,041 bytes
- **Contains**: Baseline A/B/Treatment conditions, success thresholds, sample sizes (Pipeline A/B), bias mitigation, falsifiability conditions
- **Usable for**: Adapter 01 (validation report template)

---

## Stub Tasks Required

### TRACEABILITY_ONTOLOGY.md - STUB TASK (P0-STUB-01)

- **Priority**: **P0** (CRITICAL - Blocking Adapter 01)
- **Blocking**: Adapter 01 (A01-T1 schema definition)
- **Current State**: Directory exists with placeholder README only
- **Minimum Viable Content**:
  ```markdown
  # TRACEABILITY_ONTOLOGY.md
  
  ## Trace Chain Schema
  
  ### Entity Definitions
  - REQ (Requirement): User-provided or system-generated requirement
  - CTRL (Control): Constraint or validation mechanism applied
  - TEST (Test): Verification step performed
  - EVID (Evidence): Artifact supporting the decision
  - DECISION (Decision): Final outcome (EMIT/BLOCK/ESCALATE)
  
  ### Field Specifications
  [Minimal JSON schema for each entity]
  
  ### Relationships
  REQ → CTRL (controls_requirement)
  CTRL → TEST (verified_by)
  TEST → EVID (supported_by)
  EVID → DECISION (informs)
  ```
- **Estimated Time**: 30-45 minutes
- **Can Defer Full Version**: Yes - Adapter 01 only needs schema structure, not semantic reasoning rules

---

### FORMAL_SPEC_PRINCIPLE_T.md - STUB TASK (P1-STUB-01)

- **Priority**: P1 (Important - Blocking Adapter 03)
- **Blocking**: Adapter 03 (formal test generation)
- **Current State**: Not created
- **Minimum Viable Content**:
  ```markdown
  # FORMAL_SPEC_PRINCIPLE_T.md
  
  ## Principle T: Traceability Specification
  
  ### Invariant Statement
  Every claim MUST have a complete trace chain: REQ → CTRL → TEST → EVID → DECISION
  
  ### Machine-Checkable Criteria
  - Completeness: All five links present
  - Validity: All references resolve
  - Causality: Modification propagates
  ```
- **Estimated Time**: 45-60 minutes
- **Can Defer**: Yes - Adapter 03 is not in Session 3-4 scope

---

### RED_TEAM_PROTOCOL.md - STUB TASK (P1-STUB-02)

- **Priority**: P1 (Important - Blocking Adapter 02)
- **Blocking**: Adapter 02 (intent manipulation testing)
- **Current State**: Not created
- **Minimum Viable Content**:
  ```markdown
  # RED_TEAM_PROTOCOL.md
  
  ## Adversarial Testing Protocol
  
  ### Attack Families
  1. Prompt Injection (direct, indirect)
  2. Intent Manipulation (gradual escalation)
  3. Context Poisoning (multi-turn)
  
  ### Success Criteria
  - Attack succeeds if constitutional gate bypassed
  - Attack fails if system halts or escalates
  ```
- **Estimated Time**: 30-45 minutes
- **Can Defer**: Yes - Adapter 02 is not in Session 3-4 scope

---

### SAFETY_CASE_SKELETON.md - STUB TASK (P1-STUB-03)

- **Priority**: P1 (Needed for Adapter 01 T6)
- **Blocking**: Adapter 01 Task 6 (framework integration)
- **Current State**: README placeholder exists with GSN structure outlined
- **Minimum Viable Content**: Promote README content to proper document with:
  - G1 goal structure (already in README)
  - Argument strand placeholders for O (Observability)
  - Evidence slots for Adapter 01 results
- **Estimated Time**: 20-30 minutes
- **Can Defer**: Until A01-T5 complete

---

## Critical Path Analysis

### For Pipeline B (Adapter 01 Only) - IMMEDIATE PRIORITY

| Requirement | Status | Action Needed |
|-------------|--------|---------------|
| TRACEABILITY_ONTOLOGY.md (stub) | **MISSING** | Create minimal stub with JSON schema |
| EVALUATION_METHODOLOGY.md | **EXISTS** ✓ | None |
| EVALUATION_PLAN_PREREGISTERED.md | **EXISTS** ✓ | None |
| METRICS_SPECIFICATION.md | **EXISTS** ✓ | None |
| W&B Account | **TBD** | See EXTERNAL_DEPENDENCIES_SETUP.md |

**Critical Blocker**: TRACEABILITY_ONTOLOGY.md stub must be created before A01-T1

**Workaround Available**: A01-T1 can define schema inline, referencing PRD_COL_PROACTIVE_MBSE.md Section 6 (MBSE Bridge) which contains TraceChain structure at 85% completeness.

### For Pipeline A (All Adapters) - FUTURE

| Adapter | Missing Prerequisites | Stub Required |
|---------|----------------------|---------------|
| Adapter 01 | TRACEABILITY_ONTOLOGY.md | P0-STUB-01 |
| Adapter 02 | RED_TEAM_PROTOCOL.md | P1-STUB-02 |
| Adapter 03 | FORMAL_SPEC_PRINCIPLE_T.md | P1-STUB-01 |
| Adapter 04 | None (PRD sufficient) | None |

---

## Recommendations

### 1. Immediate (Before A01-T1)
**Create TRACEABILITY_ONTOLOGY.md minimal stub** using the TraceChain structure from `PRD_COL_PROACTIVE_MBSE.md` Section 6.1. This unblocks Adapter 01 without requiring full ontology specification.

Alternatively: **Proceed with A01-T1 using PRD as source** - The PRD contains sufficient trace chain schema (Section 6.1) to define the W&B adapter schema. Mark TRACEABILITY_ONTOLOGY.md as "deferred pending adapter feedback."

### 2. Before A01-T6
**Promote 09_SAFETY_CASE/README.md to SAFETY_CASE_SKELETON.md** with argument strand for Observability principle. This enables proper evidence linkage.

### 3. Post-Adapter 01 Completion
**Use adapter development to inform ontology** - Building the adapter will reveal schema requirements that should flow back into TRACEABILITY_ONTOLOGY.md. Create full version after A01-T3.

---

## Dependency Graph (Adapter 01)

```
PRD_COL_PROACTIVE_MBSE.md (EXISTS)
        │
        ▼
TRACEABILITY_ONTOLOGY.md (STUB NEEDED) ─────┐
        │                                    │
        ▼                                    │
  ┌─────────────┐                            │
  │  A01-T1     │◀───────────────────────────┘
  │  Schema     │
  └─────────────┘
        │
        ▼
  ┌─────────────┐
  │  A01-T2     │
  │  Structure  │
  └─────────────┘
        │
        ├───────────────────────────────────┐
        ▼                                   ▼
  ┌─────────────┐                    ┌─────────────┐
  │  A01-T3     │                    │  A01-T4     │
  │  Implement  │                    │  Templates  │
  └─────────────┘                    └─────────────┘
        │                                   │
        └───────────────┬───────────────────┘
                        ▼
                 ┌─────────────┐
                 │  A01-T5     │
                 │  Validate   │◀─── EVALUATION_METHODOLOGY.md (EXISTS)
                 └─────────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │  A01-T6     │◀─── SAFETY_CASE_SKELETON.md (STUB NEEDED)
                 │  Integrate  │
                 └─────────────┘
```

---

## V&T Statement

### EXISTS (Verified)
- `01_FOUNDATIONS/PRD_COL_PROACTIVE_MBSE.md` - 13,622 bytes, contains TraceChain schema
- `05_EVALUATION_DESIGN/EVALUATION_PLAN_PREREGISTERED.md` - 10,660 bytes, complete
- `05_EVALUATION_DESIGN/BENCHMARK_TASK_SETS.md` - 17,263 bytes, complete
- `05_EVALUATION_DESIGN/METRICS_SPECIFICATION.md` - 20,586 bytes, complete
- `TASK_MANAGEMENT/EVALUATION_METHODOLOGY.md` - 6,041 bytes, complete
- `04_FORMAL_SPECIFICATION/README.md` - placeholder only
- `09_SAFETY_CASE/README.md` - placeholder with GSN outline

### DOES NOT EXIST (Verified Missing)
- `04_FORMAL_SPECIFICATION/TRACEABILITY_ONTOLOGY.md`
- `04_FORMAL_SPECIFICATION/FORMAL_SPEC_PRINCIPLE_T.md`
- `05_EVALUATION_DESIGN/RED_TEAM_PROTOCOL.md`
- `09_SAFETY_CASE/SAFETY_CASE_SKELETON.md` (only README exists)
- `ADAPTER_MODULES/` directory

### FUNCTIONAL STATUS
Audit complete. Adapter 01 can proceed with workaround (use PRD Section 6.1 for schema). Full TRACEABILITY_ONTOLOGY.md recommended but not strictly blocking.

---

*Created: 2026-01-19 | Session 3*
