# Project Research Summary

**Project:** PROACTIVE AI Constitution Toolkit v1.1
**Domain:** Constitutional AI Validation Framework (Subsequent Milestone)
**Researched:** 2026-01-23
**Confidence:** HIGH

## Executive Summary

The v1.1 milestone completes two parallel adapter modules: finalizing the CI Safety Gate (A02) with a validation study, and implementing the HELM Safety Profile adapter (A03) for benchmark-based truthfulness evaluation. The existing v1.0 foundation (W&B Trace Adapter shipped) provides proven patterns that A02/A03 can follow directly. The stack is already in place: `crfm-helm==0.5.11` is installed, Python 3.11+ exceeds requirements, and supporting libraries (NumPy, SciPy, pandas) cover all statistical needs.

The recommended approach is **sequential completion**: finish A02 validation first (2-3 hours) to establish the validation study pattern and ensure the GitHub Actions workflow functions correctly, then proceed to A03 implementation (4-6 hours). This order maximizes learning transfer between adapters and ensures all evidence strands (E-V1 for CI gate, E-T1 for HELM) are properly linked to the Safety Case. The CI Safety Gate already has validator.py (1005 lines), action.yml, and 8 test cases ready; it only needs the validation run and documentation.

Key risks center on **baseline comparison omission** (running validation without Treatment vs Baseline comparison invalidates evidence claims), **author-evaluator bias** (all pilot results must explicitly acknowledge this limitation), and **HELM version compatibility** (pin crfm-helm 0.5.11 to avoid future breakage). The existing EVALUATION_METHODOLOGY.md prescribes the exact protocol to follow, and the Safety Case Skeleton has evidence slots waiting for E-V1 and E-T1.

## Key Findings

### Recommended Stack

The existing stack is sufficient with no new dependencies required. The project already has `crfm-helm==0.5.11` (verified in requirements.txt, line 468), which is the latest stable release with Python >=3.10 support. All supporting libraries are installed and compatible.

**Core technologies:**
- **crfm-helm 0.5.11**: HELM benchmark framework for TruthfulQA evaluation - already installed, provides unified model interface
- **Python 3.11+**: Runtime exceeds HELM's >=3.10 requirement - no version upgrade needed
- **SciPy 1.15.2**: Statistical tests (paired t-test, Cohen's d) for baseline comparison - already installed
- **PyYAML 6.0.2**: Configuration files (scenario_config.yaml, proactive_metrics.yaml) - already installed

**Explicitly excluded** (HELM abstracts these):
- Direct model SDKs (openai, anthropic) - HELM provides unified interface
- Heavy ML frameworks (torch, tensorflow) - not needed for evaluation adapter
- Database systems - JSON sufficient for 817-question benchmark scale

### Expected Features

**Must have (table stakes):**
- **CI Safety Gate validation study (A02-T5)**: Cannot claim "catches violations" without quantitative evidence; 8 test cases exist, need execution and documentation
- **Safety case integration (A02-T6, A03-T6)**: Evidence must link to safety case strands V and T; USE_CASE_EVIDENCE.md templates exist
- **HELM wrapper (helm_wrapper.py)**: Core adapter functionality for prompt adaptation and response parsing
- **PROACTIVE scorer (proactive_scorer.py)**: Calculate epistemic accuracy, ECE, bounded_unknown_rate, F1 truthful
- **Statistical comparison to baseline**: Must show significance (p<0.05) per EVALUATION_METHODOLOGY.md

**Should have (differentiators):**
- **SARIF output for GitHub Security**: Already implemented in validator.py, enables native Security tab integration
- **PR comment automation**: Already in action.yml, provides inline violation feedback
- **Calibration metrics alongside accuracy**: PROACTIVE specifically cares about epistemic reliability (I3)

**Defer (v1.2+):**
- Full HELM validation study with real model API calls (requires API credits)
- Red team protocol (E-I1) for adversarial testing
- Multi-benchmark HELM support (NaturalQuestions, etc.)
- Real-world model output validation beyond synthetic test cases

### Architecture Approach

A03 fits as a **parallel evaluation adapter** sharing patterns with A01/A02: schema-first design, YAML configuration, standardized evidence linking. The three adapters cover complementary stages: observability (A01/W&B traces), CI-time verification (A02), and benchmark-time evaluation (A03). Each adapter is standalone with no code dependencies between them, following existing anti-coupling patterns.

**Major components:**
1. **helm_wrapper.py**: Adapt prompts with epistemic requirements, parse responses to extract tags and confidence, interface with HELM or mock model
2. **proactive_scorer.py**: Calculate PROACTIVE metrics (ECE, F1, bounded_unknown_rate), detect failure modes (F1 overconfidence, F3 epistemic mismatch), statistical comparison
3. **Configuration files**: proactive_metrics.yaml (thresholds), scenario_config.yaml (HELM adaptation), helm_results_schema.json (output validation)
4. **Evidence chain**: Results JSON -> USE_CASE_EVIDENCE.md -> Safety Case Strand T (E-T1)

**Key integration points:**
- A03 focuses on I1, I3, I5 invariants (Evidence-First, Confidence Verification, Safety Over Fluency) as these map to truthfulness evaluation
- Evidence Registry in SAFETY_CASE_SKELETON.md has slots for E-V1, E-T1 pending completion

### Critical Pitfalls

1. **Validation Without Baseline Comparison** (Critical): Running validation only on seeded test cases without Treatment vs Baseline comparison invalidates evidence claims. EVALUATION_METHODOLOGY.md explicitly requires Baseline A (null), Baseline B (standard CI), Treatment comparison. **Prevention**: Follow pre-registered protocol exactly, use same seeded violations across all conditions.

2. **Author-as-Evaluator Bias** (Critical): All v1.1 results will be author-evaluated pilots. Claiming "validated" without acknowledging this limitation undermines safety case credibility. **Prevention**: Explicitly label all results as "author-evaluated pilot", keep confidence at MEDIUM until external validation.

3. **HELM Version Compatibility** (Critical): HELM is a "living benchmark" with frequent updates. Building against unspecified version risks future breakage. **Prevention**: Pin `crfm-helm==0.5.11` explicitly, document version in README, avoid internal HELM module imports.

4. **Metric Interpretation Without Calibration Context** (Critical): Reporting HELM accuracy without calibration metrics undermines PROACTIVE's epistemic reliability claims. **Prevention**: Always report Brier score/ECE alongside accuracy, map to Principle T (Truth Boundaries).

5. **CI Gate False Positive Rate Ignoring** (Moderate): Tuning for maximum detection without measuring false positives leads to developer frustration and bypass. **Prevention**: Measure FP rate during A02-T5 on legitimate code (not just test cases), target <10% per EVALUATION_METHODOLOGY.md.

## Implications for Roadmap

Based on research, suggested phase structure:

### Phase 1: CI Safety Gate Completion (A02)
**Rationale:** Validation infrastructure already exists (validator.py, test cases, action.yml). Completing A02 first establishes the validation study pattern that A03 will follow. Also unblocks E-V1 evidence for Safety Case.
**Delivers:** Validated CI gate with quantitative evidence, complete USE_CASE_EVIDENCE.md, E-V1 in safety case
**Addresses:** A02-T5 (validation study), A02-T6 (framework integration)
**Avoids:** Pitfall 1 (no baseline) by following EVALUATION_METHODOLOGY.md protocol
**Estimated effort:** 2-3 hours

### Phase 2: HELM Schema and Structure (A03-T1, A03-T2)
**Rationale:** Schema-first design enables clear contracts before implementation. Defines proactive_metrics.yaml thresholds pre-registration (avoids post-hoc p-hacking).
**Delivers:** proactive_metrics.yaml, scenario_config.yaml, helm_results_schema.json, directory structure
**Uses:** PyYAML, existing A02 validator_config.yaml as pattern
**Implements:** Configuration architecture following existing adapter patterns
**Estimated effort:** 45-60 minutes

### Phase 3: HELM Core Implementation (A03-T3)
**Rationale:** Implement against defined schemas. Mock model interface enables testing without API credentials.
**Delivers:** helm_wrapper.py, proactive_scorer.py with full metric calculation
**Uses:** crfm-helm, scipy for statistical tests, numpy for ECE calculation
**Implements:** Core adapter components with HELM integration
**Avoids:** Pitfall 6 (RunSpec registration) by following HELM's two-step pattern exactly
**Estimated effort:** 90-120 minutes

### Phase 4: HELM Analysis Templates (A03-T4)
**Rationale:** Analysis infrastructure before running validation ensures consistent reporting format.
**Delivers:** analysis_template.md, scripts/analyze_results.py
**Implements:** Statistical comparison functions, failure mode detection
**Estimated effort:** 30-45 minutes

### Phase 5: HELM Validation and Integration (A03-T5, A03-T6)
**Rationale:** Run validation after implementation is stable. Integration updates Safety Case with E-T1.
**Delivers:** TruthfulQA pilot results, USE_CASE_EVIDENCE.md for A03, E-T1 evidence in Safety Case
**Avoids:** Pitfall 2 (author bias) by explicitly labeling as pilot study, Pitfall 4 (no calibration) by requiring ECE alongside F1
**Note:** Full validation with real model API calls deferred to v1.2; v1.1 uses mock/limited evaluation
**Estimated effort:** 90-120 minutes

### Phase Ordering Rationale

- **A02 before A03**: A02 is closer to completion (just needs validation run and docs). Establishes validation study pattern for A03 to follow. Reduces context switching by completing one adapter before starting another.
- **Schema before implementation**: Pre-registration of thresholds avoids post-hoc adjustment accusations. Clear contracts enable parallel work on different components.
- **Templates before validation**: Having analysis infrastructure ready ensures consistent reporting when results arrive.
- **Defer full HELM validation**: Real model API calls require budget and are time-intensive. v1.1 establishes infrastructure; v1.2 runs comprehensive evaluation.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 3 (HELM Core)**: HELM's two-step registration pattern (Scenario + RunSpec) requires careful attention. Follow HELM docs exactly.
- **Phase 5 (HELM Validation)**: API credential management and cost estimation need attention before full runs.

Phases with standard patterns (skip research-phase):
- **Phase 1 (CI Gate Completion)**: Well-documented in EVALUATION_METHODOLOGY.md, existing test cases cover approach
- **Phase 2 (Schema)**: Follows existing validator_config.yaml pattern, no novel research needed
- **Phase 4 (Analysis Templates)**: Standard statistical reporting, scipy documentation sufficient

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Direct verification of requirements.txt; crfm-helm 0.5.11 confirmed installed |
| Features | HIGH | Codebase directly reviewed; CI gate has validator.py/action.yml ready |
| Architecture | HIGH | Consistent patterns observed in A01/A02; integration points clear |
| Pitfalls | MEDIUM-HIGH | Critical pitfalls verified against existing docs; HELM-specific pitfalls based on community experience |

**Overall confidence:** HIGH

The v1.1 milestone is well-scoped. Stack is ready (no new dependencies), architecture patterns are proven (A01 shipped), features are clearly defined (existing task backlogs), and pitfalls have specific prevention strategies.

### Gaps to Address

- **Model API credentials for HELM**: Real TruthfulQA evaluation requires API keys. For v1.1 pilot, use mocked responses or limited evaluation (--max-eval-instances 10). Budget for full evaluation in v1.2.
- **External validation**: All v1.1 results are author-evaluated. Flag in evidence that confidence upgrade to HIGH requires external auditors (Pipeline A study).
- **False positive rate measurement**: A02-T5 must include FP measurement on legitimate code, not just seeded test cases. tc07_clean_output.json is control case.
- **SARIF fingerprint entropy**: Current validator.py uses 4-char hex (uuid4().hex[:4]). Consider increasing to 8+ chars if collision issues arise.

## Sources

### Primary (HIGH confidence)
- [HELM GitHub Repository](https://github.com/stanford-crfm/helm) - Source code, installation docs, scenario patterns
- [HELM PyPI crfm-helm](https://pypi.org/project/crfm-helm/) - Package version 0.5.11, dependencies
- Project codebase analysis - validator.py, action.yml, schema.json, adapter.py patterns
- EVALUATION_METHODOLOGY.md - Pre-registered validation protocol
- SAFETY_CASE_SKELETON.md - Evidence Registry structure

### Secondary (MEDIUM confidence)
- [HELM Safety v1.0 Announcement](https://crfm.stanford.edu/2024/11/08/helm-safety.html) - Safety benchmark approach, six risk categories
- [TruthfulQA Paper](https://arxiv.org/abs/2109.07958) - Benchmark design and evaluation methodology
- [HELM Documentation on ReadTheDocs](https://crfm-helm.readthedocs.io/en/latest/) - Installation and scenario creation guides

### Tertiary (LOW confidence)
- Community experience on HELM version compatibility - based on general benchmark framework patterns
- API cost estimates - rough estimates, actual costs depend on model selection

---
*Research completed: 2026-01-23*
*Ready for roadmap: yes*
