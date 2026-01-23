# Architecture Patterns: HELM Safety Profile Integration

**Domain:** PROACTIVE AI Constitution Toolkit - Adapter Integration
**Researched:** 2026-01-23
**Focus:** How HELM Safety Profile (A03) integrates with existing PROACTIVE architecture

---

## Executive Summary

The HELM Safety Profile adapter (A03) fits into the existing PROACTIVE architecture as a **parallel evaluation adapter** that shares common patterns with A01 (W&B Trace Adapter) and A02 (CI Safety Gate), while introducing a new data flow for benchmark-based validation. The integration is straightforward because the existing architecture already supports the key patterns needed: I1-I6 invariant checking, evidence linking to safety case, and standardized schema-based data exchange.

**Key insight:** A03 extends the validation scope from CI-time checking (A02) and observability (A01) to **benchmark-time evaluation**, completing the "verify at multiple stages" pattern already established.

---

## Current Architecture Overview

### Component Inventory

```
ADAPTER_MODULES/
├── 01_WANDB_TRACE_ADAPTER/     # Pipeline A: Observability
│   ├── schema.json             # Trace log schema (I1-I6 results)
│   ├── adapter.py              # Trace -> W&B Tables
│   ├── config.py               # Configuration
│   └── USE_CASE_EVIDENCE.md    # Evidence E-O1
│
├── 02_CI_SAFETY_GATE/          # Pipeline B: Verification
│   ├── validator.py            # I1-I6 invariant checks
│   ├── violation_schema.json   # Violation report schema
│   ├── action.yml              # GitHub Action
│   ├── validator_config.yaml   # Check configuration
│   └── USE_CASE_EVIDENCE.md    # Evidence E-V1 (pending)
│
└── 03_HELM_SAFETY_PROFILE/     # Pipeline C: Benchmark (NEW)
    └── [to be created]

09_SAFETY_CASE/
└── SAFETY_CASE_SKELETON.md     # GSN-style argument structure
    ├── Strand O: Observability     # Links to A01
    ├── Strand I: Invariant Gates   # Links to A02
    ├── Strand T: Truth Boundaries  # Links to A03 (NEW)
    └── Evidence Registry           # E-O1, E-V1, E-T1 (NEW)

.github/workflows/
└── test-actions.yml            # Basic CI (not yet enforcing safety gate)
```

### Data Flow Patterns

**Pattern 1: Trace Log -> Observability (A01)**
```
AI Output -> Trace Log (schema.json) -> adapter.py -> W&B Tables -> Auditor Analysis
```

**Pattern 2: Model Output -> CI Verification (A02)**
```
Model Output Files -> validator.py -> Violation Report -> GitHub Action -> Pass/Fail Gate
```

**Pattern 3: Benchmark Questions -> Evaluation (A03 - NEW)**
```
TruthfulQA Questions -> HELM Wrapper -> Model Response -> PROACTIVE Scorer -> Metrics -> Evidence
```

---

## A03 Integration Points

### Integration Point 1: Schema Alignment

**Existing:** A01 `schema.json` defines the PROACTIVE trace log format with I1-I6 validator results.

**A03 Extension:** The HELM adapter produces responses that can be scored against I1, I3, I5 invariants specifically:

| Invariant | A01 Role | A02 Role | A03 Role |
|-----------|----------|----------|----------|
| I1 (Evidence-First) | Records epistemic tags | Detects missing evidence | Scores epistemic classification accuracy |
| I2 (No Phantom Work) | Records artifact claims | Detects false completion claims | N/A (no file artifacts in QA) |
| I3 (Confidence Verification) | Records confidence scores | Detects unverified high confidence | Measures calibration error |
| I4 (Traceability) | Records trace chain | Detects broken traces | N/A (benchmark doesn't use traces) |
| I5 (Safety Over Fluency) | Records claim boundaries | Detects fluency conflicts | Measures bounded_unknown_rate |
| I6 (Fail Closed) | Records failure handling | Detects bypass attempts | N/A (benchmark-level) |

**Recommendation:** A03 focuses on I1, I3, I5 invariants as these map directly to truthfulness evaluation. I2, I4, I6 are not applicable to benchmark QA format.

### Integration Point 2: Evidence Registry

**Existing:** Safety case has evidence slots for each strand:
- E-O1: W&B Adapter pilot results (COMPLETE)
- E-V1: CI gate enforcement results (PENDING - A02)
- E-T1: HELM TruthfulQA results (PENDING - A03)

**A03 Contribution:** Produces E-T1 evidence with:
- Quantitative metrics (F1 truthful, calibration error, bounded unknown rate)
- Statistical comparison vs baseline
- Failure mode detection (F1 overconfidence, F3 epistemic mismatch)

**Required Links:**
```
USE_CASE_EVIDENCE.md (A03)
    ↓
Evidence E-T1 in SAFETY_CASE_SKELETON.md
    ↓
Strand T (Truth Boundaries) argument
    ↓
Top-level Goal G1
```

### Integration Point 3: Shared Utility Patterns

**Existing Patterns in A01/A02:**

1. **Schema validation** - Both use JSON Schema for input/output
2. **Configuration via YAML** - `validator_config.yaml` pattern
3. **Result aggregation** - Summary statistics with counts
4. **Failure mode detection** - F1-F5 taxonomy
5. **Evidence documentation** - `USE_CASE_EVIDENCE.md` template

**A03 Should Reuse:**

| Pattern | Source | Adaptation for A03 |
|---------|--------|-------------------|
| JSON Schema for results | A02 `violation_schema.json` | Create `helm_results_schema.json` |
| YAML config | A02 `validator_config.yaml` | Create `scenario_config.yaml` |
| Summary with by_invariant | A02 `generate_report()` | Use for metrics aggregation |
| USE_CASE_EVIDENCE template | A01 | Adapt for benchmark study format |

---

## New Components for A03

### Component 1: HELM Wrapper (`helm_wrapper.py`)

**Purpose:** Adapts HELM scenarios with PROACTIVE epistemic requirements.

**Responsibilities:**
- Load scenario configuration
- Adapt prompts to require epistemic tags
- Parse responses to extract tags and confidence
- Interface with HELM or mock model for testing

**Interface:**
```python
def run_scenario(scenario_name: str, model_callable, max_instances: int) -> ScenarioResult
def parse_response(response: str) -> Dict[str, Any]  # Extract epistemic_tag, confidence
def load_config(config_path: str) -> Dict[str, Any]
```

**Dependencies:**
- `crfm-helm` (optional - for full HELM integration)
- `pyyaml` (for configuration)
- No dependency on A01 or A02

### Component 2: PROACTIVE Scorer (`proactive_scorer.py`)

**Purpose:** Calculates PROACTIVE-specific metrics from HELM outputs.

**Responsibilities:**
- Calculate epistemic classification accuracy
- Calculate Expected Calibration Error (ECE)
- Calculate bounded unknown rate
- Calculate F1 truthful
- Detect failure modes (F1, F3)
- Statistical comparison vs baseline

**Interface:**
```python
def aggregate_metrics(instances: List[Dict]) -> ProactiveScore
def detect_failure_modes(instances: List[Dict]) -> Dict[str, int]
def compare_to_baseline(treatment: List[ProactiveScore], baseline: List[ProactiveScore]) -> Dict
```

**Dependencies:**
- `scipy` (for statistical tests)
- `numpy` (for numerical operations)
- No dependency on A01 or A02

### Component 3: Configuration Files

**`proactive_metrics.yaml`:**
- Metric definitions with thresholds
- Failure mode detection rules
- Baseline definitions

**`scenario_config.yaml`:**
- Scenario adaptations (prompt templates)
- Output format requirements
- Run configuration

### Component 4: Results Schema (`helm_results_schema.json`)

**Purpose:** Define structure for HELM evaluation results (parallel to A02's `violation_schema.json`).

**Key Fields:**
```json
{
  "evaluation_id": "string",
  "timestamp": "ISO8601",
  "scenario": "string",
  "model": "string",
  "metrics": {
    "epistemic_accuracy": "number",
    "confidence_calibration": "number",
    "bounded_unknown_rate": "number",
    "f1_truthful": "number",
    "proactive_truthfulness": "number"
  },
  "failure_modes": {
    "F1_overconfidence": "integer",
    "F3_epistemic_mismatch": "integer"
  },
  "comparison": {
    "baseline_f1": "number",
    "improvement": "number",
    "p_value": "number",
    "significant": "boolean"
  }
}
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PROACTIVE ADAPTER ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐          │
│  │  A01: W&B       │    │  A02: CI Gate   │    │  A03: HELM      │          │
│  │  Trace Adapter  │    │  Validator      │    │  Safety Profile │          │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘          │
│           │                      │                      │                    │
│           ▼                      ▼                      ▼                    │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐          │
│  │ schema.json     │    │ violation_      │    │ helm_results_   │          │
│  │ (trace format)  │    │ schema.json     │    │ schema.json     │          │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘          │
│           │                      │                      │                    │
│           │     ┌────────────────┼────────────────┐     │                    │
│           │     │                │                │     │                    │
│           ▼     ▼                ▼                ▼     ▼                    │
│  ┌─────────────────────────────────────────────────────────────────┐        │
│  │                        I1-I6 INVARIANTS                          │        │
│  │  I1: Evidence  I2: Phantom  I3: Confidence  I4: Trace  I5/I6    │        │
│  └─────────────────────────────────────────────────────────────────┘        │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────┐        │
│  │                         SAFETY CASE                              │        │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐             │        │
│  │  │Strand O │  │Strand I │  │Strand T │  │Strand V │             │        │
│  │  │(A01)    │  │(A02)    │  │(A03)    │  │(A02)    │             │        │
│  │  │E-O1 ✓   │  │E-I1 ⌛   │  │E-T1 ⌛   │  │E-V1 ⌛   │             │        │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘             │        │
│  └─────────────────────────────────────────────────────────────────┘        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

Legend:
✓ = Evidence collected
⌛ = Evidence pending
```

---

## Data Flow: A03 Evaluation Pipeline

```
┌─────────────────┐
│  TruthfulQA     │
│  Questions      │
│  (HELM dataset) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  helm_wrapper   │
│  .adapt_prompt  │
│                 │
│  Add epistemic  │
│  requirements   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Model API      │
│  (OpenAI/Claude │
│   /Local)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  helm_wrapper   │
│  .parse_response│
│                 │
│  Extract:       │
│  - epistemic_tag│
│  - confidence   │
│  - claim_text   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ proactive_scorer│
│ .score_response │
│                 │
│  Compare to     │
│  ground truth   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ proactive_scorer│
│ .aggregate_     │
│  metrics        │
│                 │
│  Calculate:     │
│  - ECE          │
│  - F1           │
│  - bounded_unk  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Results JSON   │
│  (schema-       │
│   validated)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ USE_CASE_       │
│ EVIDENCE.md     │
│                 │
│  Document for   │
│  Safety Case    │
└─────────────────┘
```

---

## Integration Patterns to Follow

### Pattern 1: Consistent Directory Structure

All adapters follow the same structure for discoverability:

```
ADAPTER_MODULES/0X_NAME/
├── __init__.py           # Package marker + version
├── schema.json           # Input/output schema
├── [core_module].py      # Main implementation
├── [config].yaml         # Configuration
├── README.md             # Usage documentation
├── USE_CASE_EVIDENCE.md  # Validation evidence
├── test_cases/           # Test data
│   └── README.md         # Test case documentation
└── scripts/              # Utility scripts
    └── analyze_*.py      # Analysis scripts
```

**A03 Implementation:**
```
ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/
├── __init__.py
├── helm_results_schema.json
├── helm_wrapper.py
├── proactive_scorer.py
├── proactive_metrics.yaml
├── scenario_config.yaml
├── README.md
├── USE_CASE_EVIDENCE.md
├── results/              # Evaluation outputs
└── scripts/
    └── analyze_results.py
```

### Pattern 2: Schema-First Design

Both A01 and A02 define schemas before implementation. A03 should do the same:

1. Define `helm_results_schema.json` (A03-T1)
2. Define `proactive_metrics.yaml` (A03-T1)
3. Implement against schemas (A03-T3)
4. Validate outputs against schemas

### Pattern 3: Evidence-to-Safety-Case Linking

Evidence documents link to safety case using consistent format:

```markdown
## Implications for Safety Case

This evidence supports Argument Strand [X]:

- **Claim**: [What we can now claim]
- **Evidence ID**: E-[X]1
- **Confidence**: [High/Medium/Low]

### Trace Chain

Principle [X] → Invariant I[N] → Adapter 0[N] → Evidence E-[X]1 → Claim
```

### Pattern 4: Statistical Validation Standard

A01 established the statistical validation pattern:
- Quantitative comparison (baseline vs treatment)
- Effect size calculation (Cohen's d)
- p-value reporting
- Limitations disclosure

A03 should follow the same pattern for TruthfulQA evaluation.

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Tight Coupling Between Adapters

**Wrong:** A03 imports from A01 or A02 directly.

**Right:** Each adapter is standalone. Shared patterns are documented, not imported.

**Rationale:** Adapters may be used independently. A user might only want HELM evaluation without W&B or CI integration.

### Anti-Pattern 2: Hardcoded HELM Integration

**Wrong:** Require full `crfm-helm` installation to run any A03 code.

**Right:** Design with mockable model interface. HELM is one possible backend.

**Rationale:**
- HELM requires API credentials for most models
- Testing needs offline capability
- Local models should work too

### Anti-Pattern 3: Metric Calculation Without Schema

**Wrong:** Calculate metrics ad-hoc without defined thresholds.

**Right:** All metrics defined in `proactive_metrics.yaml` with thresholds before implementation.

**Rationale:** Thresholds defined post-hoc can be p-hacked. Pre-registration prevents this.

### Anti-Pattern 4: Evidence Without Limitations

**Wrong:** Report positive results without acknowledging limitations.

**Right:** Every USE_CASE_EVIDENCE.md includes honest limitations section.

**Rationale:** Scientific integrity requires honest scope statements.

---

## Build Order Recommendation

Based on dependency analysis and existing patterns:

### Phase 1: Schema and Structure (A03-T1, A03-T2)
**Rationale:** Schema-first design enables parallel work and clear contracts.

1. **A03-T1: Define schemas** (30-45 min)
   - `proactive_metrics.yaml` - metric definitions
   - `scenario_config.yaml` - HELM configuration
   - `helm_results_schema.json` - output format

2. **A03-T2: Create directory structure** (15-20 min)
   - Standard adapter structure
   - Stub implementations
   - README with thresholds

### Phase 2: Core Implementation (A03-T3)
**Rationale:** Implement against defined schemas.

3. **A03-T3: Implement adapter** (90-120 min)
   - `helm_wrapper.py` - prompt adaptation, response parsing
   - `proactive_scorer.py` - metrics calculation
   - Mock model interface for testing

### Phase 3: Documentation and Analysis (A03-T4)
**Rationale:** Analysis templates before running validation.

4. **A03-T4: Create analysis templates** (30-45 min)
   - `analysis_template.md`
   - `scripts/analyze_results.py`

### Phase 4: Validation and Integration (A03-T5, A03-T6)
**Rationale:** Validation after implementation is stable.

5. **A03-T5: Run validation** (90-120 min)
   - Execute TruthfulQA evaluation
   - Calculate metrics
   - Statistical comparison
   - Complete USE_CASE_EVIDENCE.md

6. **A03-T6: Integration** (30-45 min)
   - Update Safety Case with E-T1
   - Update README.md
   - Cross-references

---

## CI Safety Gate Completion Context

Before A03, complete A02 integration:

**Current State:**
- `validator.py` implemented (I1-I6 checks)
- `action.yml` defined (GitHub Action)
- `test_cases/` with 8 seeded violations
- `violation_schema.json` defined

**Remaining for A02:**
- A02-T5: Validation study (run on test cases, document results)
- A02-T6: Integration (update safety case with E-V1)
- Wire GitHub Actions workflow to use the action

**Recommendation:** Complete A02-T5/T6 before starting A03 to:
1. Establish validation study pattern
2. Confirm GitHub Actions workflow works
3. Have E-V1 evidence in place

---

## Scalability Considerations

| Concern | At 100 questions | At 817 questions (full TruthfulQA) | At 10K questions |
|---------|------------------|-----------------------------------|------------------|
| Evaluation time | ~10 min (API calls) | ~1-2 hours | ~10+ hours |
| Result storage | JSON files | JSON files | Consider database |
| Statistical power | Limited | Adequate | Strong |
| API cost | ~$5-10 | ~$50-100 | ~$500+ |

**Recommendations:**
- Start with 100 questions for development
- Run full 817 for publication-quality evidence
- Consider caching responses for reproducibility

---

## Sources

**Official Documentation:**
- [HELM GitHub Repository](https://github.com/stanford-crfm/helm)
- [HELM Safety Benchmark](https://crfm.stanford.edu/helm/safety/latest/)
- [Stanford CRFM HELM Documentation](https://crfm.stanford.edu/helm/)

**Research Papers:**
- [TruthfulQA Paper](https://arxiv.org/abs/2109.07958)
- [HELM Paper](https://arxiv.org/abs/2211.09110)

**Project Context:**
- Existing codebase analysis (adapter.py, validator.py, schema.json, etc.)
- Task backlog TASK_BACKLOG_ADAPTER_03.md specifications
- Safety case skeleton structure

---

## Confidence Assessment

| Area | Level | Reason |
|------|-------|--------|
| Integration points | HIGH | Based on direct code analysis of existing adapters |
| Schema patterns | HIGH | Consistent patterns observed in A01/A02 |
| Build order | HIGH | Dependencies clear from task backlog |
| HELM specifics | MEDIUM | Based on GitHub docs; full crfm-helm integration may require adjustments |
| Scalability estimates | LOW | Rough estimates; actual costs depend on model and API pricing |

---

*Created: 2026-01-23 | Architecture Research for v1.1 Milestone*
