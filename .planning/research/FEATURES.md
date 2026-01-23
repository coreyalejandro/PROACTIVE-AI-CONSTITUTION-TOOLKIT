# Feature Landscape

**Domain:** Constitutional AI Validation Adapters (CI Safety Gate + HELM Safety Profile)
**Researched:** 2026-01-23
**Confidence:** HIGH for CI Safety Gate (existing codebase reviewed), MEDIUM for HELM integration (based on official docs)

---

## Executive Summary

This document maps the feature landscape for completing two PROACTIVE adapter modules:

1. **CI Safety Gate (Adapter 02)** - Completing validation study and wiring for production use
2. **HELM Safety Profile (Adapter 03)** - New adapter integrating Stanford HELM benchmark for Principle T validation

The CI Safety Gate has a solid foundation (validator.py implemented, 8 test cases, action.yml defined) but lacks production validation evidence and documentation completion. HELM Safety Profile requires building wrapper code around the `crfm-helm` package to extract PROACTIVE-specific metrics.

---

## Table Stakes

Features users expect. Missing = product feels incomplete.

### CI Safety Gate Completion

| Feature | Why Expected | Complexity | Status | Notes |
|---------|--------------|------------|--------|-------|
| Comprehensive validation study (A02-T5) | Cannot claim "catches violations" without evidence | Medium | NOT_STARTED | 8 test cases exist, need to run and document results |
| USE_CASE_EVIDENCE.md completion | Safety case requires evidence | Low | NOT_STARTED | Template exists, needs data from validation run |
| Safety case integration (A02-T6) | Evidence must link to safety case strand V | Low | NOT_STARTED | SAFETY_CASE_SKELETON.md has placeholder for E-V1 |
| validation_results.json data file | Quantitative evidence artifact | Low | NOT_STARTED | Script pattern exists in A02-T5 instructions |
| GitHub Actions workflow test | Action must actually work in CI | Medium | NOT_STARTED | action.yml exists but untested in real workflow |

### HELM Safety Profile (New Adapter 03)

| Feature | Why Expected | Complexity | Status | Notes |
|---------|--------------|------------|--------|-------|
| HELM wrapper (helm_wrapper.py) | Core adapter functionality | High | NOT_STARTED | Must integrate with crfm-helm 0.5.9 |
| PROACTIVE scorer (proactive_scorer.py) | Extract PROACTIVE metrics from HELM output | Medium | NOT_STARTED | ECE, F1, bounded_unknown_rate calculations |
| Scenario config (truthfulqa_proactive) | Adapted prompt template for epistemic tags | Medium | NOT_STARTED | TruthfulQA with PROACTIVE output format |
| Metrics definition (proactive_metrics.yaml) | Threshold definitions for pass/fail | Low | NOT_STARTED | Documented in task backlog |
| Statistical comparison to baseline | Must show significance (p<0.05) | Medium | NOT_STARTED | t-test, Cohen's d implementation |
| USE_CASE_EVIDENCE.md | Evidence for safety case strand T | Low | NOT_STARTED | Template pattern from other adapters |

---

## Differentiators

Features that set product apart. Not expected, but valued.

### CI Safety Gate

| Feature | Value Proposition | Complexity | Priority | Notes |
|---------|-------------------|------------|----------|-------|
| SARIF output for GitHub Security | Native GitHub Security integration | Low | HIGH | Already implemented in validator.py |
| PR comment automation | Inline violation feedback | Low | HIGH | Already implemented in action.yml |
| Configurable invariant severity | Teams can customize which invariants are errors vs warnings | Low | MEDIUM | validator_config.yaml supports this |
| Real-world model output validation | Validate actual W&B traces or LLM outputs | High | LOW | Current test cases are synthetic |
| Performance benchmarking at scale | Validate 1000+ files in <30s | Medium | LOW | Not critical for research toolkit |
| Red team protocol + results (E-I1) | Demonstrate gates cannot be bypassed | High | MEDIUM | For Safety Case Strand I |

### HELM Safety Profile

| Feature | Value Proposition | Complexity | Priority | Notes |
|---------|-------------------|------------|----------|-------|
| Multi-benchmark support | Beyond TruthfulQA (NaturalQuestions, etc.) | High | LOW | TruthfulQA is sufficient for MVP |
| Interactive HELM dashboard integration | Visual results exploration | High | LOW | HELM has own dashboards |
| Custom scenario definition UI | Non-developers can create scenarios | High | LOW | YAML configs sufficient |
| Automated prompt adaptation | LLM-based prompt template optimization | High | LOW | Fixed templates sufficient |
| Calibration visualization | Reliability diagrams for confidence analysis | Medium | MEDIUM | Nice for publications |
| Cross-model comparison reports | Compare multiple models side-by-side | Medium | MEDIUM | Useful for research papers |

---

## Anti-Features

Features to explicitly NOT build. Common mistakes in this domain.

### CI Safety Gate

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| Automatic code fixing | Safety gate should report, not modify. Modifications hide issues from developers. | Report violations with suggested fixes. Developer applies changes. |
| Silent pass on configuration errors | Fail-closed principle requires surfacing problems | Always fail with clear error message if config is malformed |
| Blocking all warnings by default | Too aggressive = developers disable the tool | Default: errors block, warnings report. Configurable threshold. |
| Complex regex customization UI | Maintainability nightmare, regex already in YAML | Keep patterns in validator_config.yaml, document syntax |
| Integration with every CI platform | Scope creep, GitHub Actions is primary target | GitHub Actions first. Provide Python CLI for portability. |
| Real-time validation during LLM generation | Wrong layer - validation happens post-generation | Post-hoc validation of outputs. Generation constraints are separate concern. |

### HELM Safety Profile

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| Full HELM re-implementation | HELM is complex, maintained by Stanford | Wrap crfm-helm package, don't reinvent |
| Replacing HELM metrics | HELM metrics are standard, replacing reduces comparability | Add PROACTIVE metrics alongside HELM metrics |
| Closed-source scenarios | Reproducibility is critical for research | All scenarios in version-controlled YAML |
| Model fine-tuning integration | Adapter is for evaluation, not training | Separate concern. Evaluation adapter outputs data for fine-tuning decisions. |
| Automated model selection | Evaluation should inform, not decide | Report results. Humans decide which model to deploy. |
| LLM-as-judge for all metrics | HELM Safety shows judge models can fail (Claude 3.5 refused to grade) | Use exact match where possible, document judge reliability when used |

---

## Feature Dependencies

```
CI Safety Gate (Adapter 02) Completion:
  A02-T5 (Run Validation) depends on:
    - [COMPLETE] validator.py implemented
    - [COMPLETE] test_cases/tc01-tc08 created
    - [COMPLETE] action.yml defined

  A02-T6 (Framework Integration) depends on:
    - A02-T5 results

HELM Safety Profile (Adapter 03):
  A03-T1 (Schema) depends on:
    - PROACTIVE Constitution Principle T definition

  A03-T2 (Structure) depends on:
    - A03-T1

  A03-T3 (Implementation) depends on:
    - A03-T2
    - crfm-helm package installation
    - API credentials for model access

  A03-T5 (Validation) depends on:
    - A03-T3
    - A03-T4
    - TruthfulQA dataset access (HELM downloads automatically)

Cross-Adapter Dependencies:
  Safety Case completion depends on:
    - A02-T6 (E-V1 evidence)
    - A03-T6 (E-T1 evidence)
```

---

## MVP Recommendation

For v1.1 milestone, prioritize:

### Immediate (Complete CI Safety Gate)

1. **A02-T5: Run validation study** - 2 hours
   - Execute validator against 8 test cases
   - Generate validation_results.json
   - Verify 100% detection rate for seeded violations

2. **A02-T6: Framework integration** - 45 minutes
   - Complete USE_CASE_EVIDENCE.md with actual data
   - Update SAFETY_CASE_SKELETON.md with E-V1 evidence
   - Add cross-references

### Next (Start HELM Safety Profile)

3. **A03-T1 through A03-T3** - 4-5 hours
   - Define schema (proactive_metrics.yaml, scenario_config.yaml)
   - Create directory structure
   - Implement helm_wrapper.py and proactive_scorer.py

### Defer to v1.2

- **A03-T5**: Full HELM validation study (requires model API credits)
- **Red team protocol (E-I1)**: Adversarial testing of invariant gates
- **Real-world model output validation**: Testing on actual LLM traces
- **Multi-benchmark HELM support**: NaturalQuestions, etc.

---

## Critical Gaps

### CI Safety Gate

| Gap | Impact | Resolution |
|-----|--------|------------|
| No validation_results.json | Cannot populate USE_CASE_EVIDENCE.md | Run A02-T5 validation script |
| USE_CASE_EVIDENCE.md incomplete | Safety case has placeholder, no actual evidence | Complete after A02-T5 |
| GitHub Actions untested in production | May have bugs in action.yml wiring | Test in actual PR workflow |

### HELM Safety Profile

| Gap | Impact | Resolution |
|-----|--------|------------|
| No code exists | Cannot validate Principle T | Implement A03-T1 through A03-T3 |
| Model API costs | TruthfulQA evaluation requires model inference | Budget for API credits or use local models |
| HELM version compatibility | crfm-helm 0.5.9 may have breaking changes | Pin version, test locally before committing |

---

## Sources

### CI Safety Gate

- **Codebase review** (HIGH confidence): validator.py, action.yml, test_cases/ in current repository
- **Task backlog** (HIGH confidence): TASK_BACKLOG_ADAPTER_02.md
- **Safety case skeleton** (HIGH confidence): SAFETY_CASE_SKELETON.md

### HELM Safety Profile

- **[HELM Official Documentation](https://crfm.stanford.edu/helm/)** (HIGH confidence): Stanford CRFM official site
- **[HELM Safety v1.0 Announcement](https://crfm.stanford.edu/2024/11/08/helm-safety.html)** (HIGH confidence): Official blog post describing safety benchmark
- **[crfm-helm PyPI](https://pypi.org/project/crfm-helm/)** (HIGH confidence): Package installation reference, version 0.5.9
- **[HELM GitHub Repository](https://github.com/stanford-crfm/helm)** (HIGH confidence): Source code and documentation
- **[HELM Documentation on ReadTheDocs](https://crfm-helm.readthedocs.io/en/latest/)** (HIGH confidence): Installation and usage guide
- **Task backlog** (MEDIUM confidence): TASK_BACKLOG_ADAPTER_03.md (internal, not yet validated against current HELM version)

### HELM Safety Key Findings

From [HELM Safety v1.0 documentation](https://crfm.stanford.edu/2024/11/08/helm-safety.html):

**Six Risk Categories Evaluated:**
- Violence
- Fraud
- Discrimination
- Sexual content
- Harassment
- Deception

**Five Benchmarks Included:**
1. BBQ (bias measurement via exact match accuracy)
2. SimpleSafetyTests (harmful request refusal)
3. HarmBench (jailbreaking resistance)
4. AnthropicRedTeam (red-teaming vulnerabilities)
5. XSTest (helpfulness vs harmlessness tradeoff)

**Measurement Approach:**
- Exact match accuracy for BBQ
- Model-judge scores (mean of two judges) for other benchmarks
- 0-1 normalized scale (higher = fewer safety risks)
- 24 models evaluated

---

## V&T Statement

### EXISTS (Verified)

- CI Safety Gate validator.py: 1005 lines, fully implemented
- CI Safety Gate action.yml: 155 lines, GitHub Action definition complete
- CI Safety Gate test_cases: 8 files (tc01-tc08) with expected violations documented
- HELM Safety Profile task backlog: Complete specifications in TASK_BACKLOG_ADAPTER_03.md

### NOT YET EXIST

- CI Safety Gate validation_results.json (A02-T5 output)
- CI Safety Gate USE_CASE_EVIDENCE.md completion
- HELM Safety Profile adapter code (A03-T1 through A03-T6)
- Safety Case Strand V evidence (E-V1)
- Safety Case Strand T evidence (E-T1)

### CONFIDENCE ASSESSMENT

| Feature Area | Confidence | Rationale |
|--------------|------------|-----------|
| CI Safety Gate table stakes | HIGH | Codebase directly reviewed, dependencies clear |
| CI Safety Gate differentiators | MEDIUM | Some features speculative (red team, scale testing) |
| HELM integration approach | MEDIUM | Based on official docs, not tested against current crfm-helm |
| HELM metrics mapping | MEDIUM | Theoretical mapping to PROACTIVE metrics, needs validation |
| Anti-features | HIGH | Based on domain experience and failure mode analysis |

---

*Created: 2026-01-23 | Research Mode: Features*
