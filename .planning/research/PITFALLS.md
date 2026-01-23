# Domain Pitfalls: HELM Safety Profile + CI Safety Gate Completion

**Domain:** PROACTIVE Toolkit v1.1 - HELM Safety Profile integration and CI Safety Gate validation
**Researched:** 2026-01-23
**Confidence:** MEDIUM (verified against official docs, existing codebase patterns, and community experience)

---

## Critical Pitfalls

Mistakes that cause rewrites, invalidate research, or compromise safety claims.

### Pitfall 1: Validation Study Without Baseline Comparison

**What goes wrong:** Running CI Safety Gate validation only on seeded test cases without comparing to baseline conditions. Results show "gate catches violations" but provide no evidence that the gate adds value beyond standard checks.

**Why it happens:** The team focuses on demonstrating the gate works (true positives) without measuring what happens without it (baseline error rate). This is especially tempting when the existing test cases (tc01-tc08) already demonstrate detection.

**Consequences:**
- Safety case evidence (E-V1) is incomplete
- Cannot claim "CI gate enforcement provides value" without Treatment vs Baseline comparison
- Peer review will reject claims of effectiveness without baseline
- Existing EVALUATION_METHODOLOGY.md explicitly requires Baseline B comparison

**Prevention:**
1. Follow the existing EVALUATION_METHODOLOGY.md protocol exactly:
   - Baseline A (null): No validation tooling
   - Baseline B (standard practice): Standard CI checks only
   - Treatment: PROACTIVE Constitutional Validator
2. Pre-register the comparison before running validation (already documented at lines 87-95)
3. Use the same seeded violations across all three conditions
4. Document that tc07_clean_output.json serves as control case

**Detection (Warning Signs):**
- Validation report only shows "violations detected" without "vs baseline"
- No documentation of what standard CI checks catch/miss
- A02-T5 task completes without Baseline B measurements

**Phase:** A02-T5 (Run validation) - must include baseline comparison

---

### Pitfall 2: Author-as-Evaluator Bias Not Acknowledged

**What goes wrong:** The validation study is conducted entirely by the toolkit author, leading to inflated effect sizes or unacknowledged bias in the safety case.

**Why it happens:** The existing EVALUATION_METHODOLOGY.md acknowledges this risk (line 66-67) but Pipeline B explicitly uses N=1-2 auditors. It's tempting to skip external validation and claim pilot results as definitive.

**Consequences:**
- Safety Case Skeleton already marks E-O1 as "Medium confidence" due to this limitation (lines 70-82)
- Publishing claims based solely on author evaluation invites reproducibility challenges
- Confidence in safety case claims remains LOW without external validation

**Prevention:**
1. **For v1.1 pilot:** Explicitly label all results as "author-evaluated pilot" in evidence
2. Document author involvement in V&T statements
3. In SAFETY_CASE_SKELETON.md, keep "Gaps to Address" section requiring external auditors
4. Do NOT upgrade confidence from MEDIUM to HIGH without Pipeline A study

**Detection (Warning Signs):**
- Validation report lacks evaluator identification
- USE_CASE_EVIDENCE.md claims "validated" without noting who validated
- Safety case strand confidence upgraded without external validation

**Phase:** A02-T5, A02-T6 - must maintain author-evaluator acknowledgment

---

### Pitfall 3: HELM Version Compatibility Breakage

**What goes wrong:** HELM Safety Profile adapter is built against a specific HELM version, then breaks when Stanford CRFM updates the framework. Common breakages include API changes to Scenario, RunSpec, or MetricSpec classes.

**Why it happens:** HELM is a "living benchmark" with frequent updates. The framework structure (ScenarioSpec, AdapterSpec, MetricSpec tuple) is stable but implementation details change between releases.

**Consequences:**
- Adapter stops working on version upgrade
- Benchmark results become non-reproducible
- Must maintain version pins, limiting access to new scenarios/metrics

**Prevention:**
1. **Pin HELM version explicitly** in requirements.txt (e.g., `helm==0.4.0`)
2. Document the pinned version in ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/README.md
3. Follow HELM's modular architecture - extend via custom scenarios, don't modify core
4. Test adapter against HELM's CI to detect breaking changes early
5. Track HELM releases in TASK_MANAGEMENT/EXTERNAL_DEPENDENCIES_SETUP.md

**Detection (Warning Signs):**
- No version pin in requirements.txt
- Adapter imports from internal HELM modules (e.g., `helm.benchmark.scenarios._internal`)
- Tests fail after `pip install --upgrade crfm-helm`

**Phase:** A03-T1 (Define schema), A03-T3 (Implement core)

---

### Pitfall 4: Metric Interpretation Without Calibration Context

**What goes wrong:** HELM metrics are reported without understanding their calibration implications. A model may score high on accuracy but be poorly calibrated (confident when wrong), undermining epistemic reliability claims.

**Why it happens:** HELM reports multiple metrics but teams focus on accuracy/performance, ignoring calibration scores. The PROACTIVE framework specifically cares about epistemic reliability (I3: Confidence Requires Verification).

**Consequences:**
- Safety case claims "model performs well on HELM" without noting calibration gaps
- Evidence E-T2 (calibration metrics) becomes meaningless if not interpreted correctly
- Misalignment between PROACTIVE goals (epistemic reliability) and reported metrics (accuracy)

**Prevention:**
1. **Always report calibration alongside accuracy** - HELM provides Brier score
2. Map HELM metrics to PROACTIVE principles:
   - Calibration -> Principle T (Truth Boundaries)
   - Robustness -> Principle I (Invariant Gates)
   - Fairness/Bias -> Principle A (Accessibility)
3. Document threshold interpretation in METRICS_SPECIFICATION.md
4. Flag when accuracy is high but calibration is poor

**Detection (Warning Signs):**
- HELM results table shows only accuracy column
- No discussion of calibration in USE_CASE_EVIDENCE.md
- E-T2 evidence marked "complete" without Brier score interpretation

**Phase:** A03-T5 (Run validation), A03-T6 (Integrate docs)

---

## Moderate Pitfalls

Mistakes that cause delays, technical debt, or reduced credibility.

### Pitfall 5: CI Gate False Positive Rate Ignoring Developer Experience

**What goes wrong:** The CI Safety Gate is tuned for maximum detection (high sensitivity) without measuring false positive rate. Developers start ignoring or bypassing the gate because it blocks legitimate code.

**Why it happens:** Safety-focused teams prioritize catching violations over developer velocity. The existing validator_config.yaml has `fail_on_warning: false` and `warning_threshold: 5`, but these were set without empirical validation.

**Consequences:**
- EVALUATION_METHODOLOGY.md specifies <10% false positive rate threshold (line 39)
- Exceeding this makes the gate "unusable noise"
- Developers disable gate or mark all warnings as "won't fix"
- Gate loses value as safety control

**Prevention:**
1. **Measure false positive rate** during A02-T5 validation:
   - Run gate on legitimate code (not just seeded test cases)
   - Count violations in clean production code
   - Target <10% false positive rate per EVALUATION_METHODOLOGY.md
2. Tune regex patterns to reduce false matches (I1 patterns are aggressive)
3. Use SARIF suppression workflow for acknowledged exceptions
4. Document expected false positive rate in README.md

**Detection (Warning Signs):**
- Validation only runs on test_cases/ directory
- No measurement of gate on real repository files
- Developers request bypass mechanism after first use

**Phase:** A02-T5 (Run validation) - must include false positive measurement

---

### Pitfall 6: HELM Custom Scenario Without RunSpec Registration

**What goes wrong:** A custom PROACTIVE safety scenario is created but not properly registered, causing HELM to fail with "Unknown scenario" errors.

**Why it happens:** HELM's two-step registration (Scenario class + run spec function) is easy to miss. The documentation requires both `YourScenario` class AND `get_your_run_spec()` function with proper Python path references.

**Consequences:**
- `helm-run` commands fail silently or with cryptic errors
- Scenario can't be included in benchmark suites
- Time lost debugging import paths

**Prevention:**
1. Follow HELM's documented pattern exactly:
   - Create Scenario class implementing `get_instances()`
   - Create run spec function in separate file
   - Use full Python path in ScenarioSpec (e.g., `helm.benchmark.scenarios.proactive_safety.PROACTIVESafetyScenario`)
2. Test with simple model first: `helm-run --run-entries proactive_safety:model=simple/model1`
3. Create unit test following HELM's test_simple_scenarios.py pattern

**Detection (Warning Signs):**
- No `*_run_specs.py` file in adapter module
- Scenario class exists but `helm-run` fails
- ScenarioSpec uses relative instead of absolute Python path

**Phase:** A03-T2 (Create structure), A03-T3 (Implement core)

---

### Pitfall 7: GitHub Actions Environment Mismatch

**What goes wrong:** The CI Safety Gate works locally but fails in GitHub Actions due to environment differences (Python version, path resolution, missing dependencies).

**Why it happens:** The existing action.yml uses Python 3.11 and copies validator.py at runtime. Differences between local development and CI environment are easy to miss.

**Consequences:**
- Gate passes locally, fails in CI (or vice versa)
- Inconsistent validation results between environments
- Time lost debugging CI-specific failures

**Prevention:**
1. **Use the same Python version** in local development as action.yml (3.11)
2. Test action locally using `act` (GitHub Actions local runner)
3. Pin all dependencies in requirements.txt, not just top-level packages
4. Use relative paths that work from repo root (already done in action.yml lines 61-68)
5. Add environment validation step that logs Python version, paths, installed packages

**Detection (Warning Signs):**
- Local validation shows different results than CI
- `validator_config.yaml` not found errors in CI but not locally
- Python import errors only in GitHub Actions

**Phase:** A02-T5 (Run validation with actual GitHub Actions)

---

### Pitfall 8: SARIF Fingerprint Collisions

**What goes wrong:** SARIF reports use auto-generated fingerprints that collide, causing GitHub Security to merge distinct alerts or lose track of resolved issues.

**Why it happens:** The current validator.py generates violation_id with `uuid.uuid4().hex[:4]` (line 188), which is only 4 hex characters (65,536 possibilities). With many violations, collisions become likely.

**Consequences:**
- Resolved alerts reappear after code changes
- Distinct violations merged into single alert
- Difficulty tracking violation remediation over time

**Prevention:**
1. **Increase fingerprint entropy** - use 8+ hex characters or content-based hashing
2. Include file path and line number in fingerprint calculation
3. Use SARIF's `partialFingerprints` property for stable identification
4. Test with repeated runs to verify no duplicate alert IDs

**Detection (Warning Signs):**
- GitHub Security shows fewer alerts than validator reports
- Dismissed alerts reappear after unrelated changes
- Multiple distinct violations show same ID in SARIF output

**Phase:** A02-T5 (Validate SARIF output), A02-T6 (Documentation)

---

## Minor Pitfalls

Mistakes that cause annoyance but are fixable without major rework.

### Pitfall 9: Test Case Metadata Drift

**What goes wrong:** Test cases (tc01-tc08) have `_test_metadata.expected_violations` that don't match what the validator actually detects after config changes.

**Why it happens:** Config changes (validator_config.yaml) can change detection behavior. Test case metadata is static and requires manual updates.

**Consequences:**
- Test case README claims certain violations but validator finds different ones
- Confusion during validation study about ground truth
- Manual verification required for each test run

**Prevention:**
1. Add automated test that compares detected violations to expected_violations
2. Run `for f in tc*.json; do python ../validator.py "$f"; done` after any config change
3. Update test case metadata when patterns change
4. Document that tc07 is "clean" control with no expected violations

**Detection (Warning Signs):**
- Validator output differs from README table
- New violations detected that aren't in expected_violations
- tc07_clean_output.json starts failing (should always pass)

**Phase:** A02-T5 (Run validation)

---

### Pitfall 10: HELM Data Download Failures

**What goes wrong:** HELM scenario `get_instances()` fails to download required datasets due to network issues, rate limits, or dataset availability changes.

**Why it happens:** HELM's `ensure_file_downloaded()` helper can fail silently or produce cryptic errors. External datasets may move or require authentication.

**Consequences:**
- Benchmark runs fail partway through
- Partial results that can't be reproduced
- Time lost debugging network/authentication issues

**Prevention:**
1. **Pre-download all datasets** before validation runs
2. Use HELM's `benchmark_output/scenarios/` cache directory
3. For restricted datasets, use `restricted/<ScenarioName>/` path pattern
4. Implement retry logic in custom scenario's `get_instances()`
5. Log download progress and cache status

**Detection (Warning Signs):**
- First run succeeds, subsequent runs fail (cache issues)
- Different results between CI and local (network access differences)
- Empty or partial Instance lists from `get_instances()`

**Phase:** A03-T3 (Implement core), A03-T5 (Run validation)

---

## Phase-Specific Warnings

| Phase | Likely Pitfall | Mitigation |
|-------|---------------|------------|
| A02-T5 (CI Gate Validation) | Pitfall 1 (No baseline), Pitfall 5 (False positives) | Follow EVALUATION_METHODOLOGY.md, measure FP rate |
| A02-T6 (CI Gate Docs) | Pitfall 8 (SARIF fingerprints) | Verify SARIF output before documenting |
| A03-T1 (HELM Schema) | Pitfall 3 (Version compatibility) | Pin HELM version immediately |
| A03-T3 (HELM Core) | Pitfall 6 (RunSpec registration), Pitfall 10 (Downloads) | Follow HELM's two-step pattern |
| A03-T5 (HELM Validation) | Pitfall 4 (Metric interpretation) | Always report calibration with accuracy |
| Safety Case Update | Pitfall 2 (Author bias) | Maintain confidence levels, acknowledge limitations |

---

## Integration Pitfalls (with existing v1.0 system)

### Pitfall 11: Safety Case Evidence Chain Breaks

**What goes wrong:** New evidence (E-V1 from CI Gate, E-T1/E-T2 from HELM) is collected but not properly linked to safety case argument strands.

**Why it happens:** SAFETY_CASE_SKELETON.md has a specific structure with bi-directional links. New evidence that doesn't follow this pattern orphans the evidence or breaks traceability.

**Consequences:**
- Safety case claims are not supported by evidence
- I4 (Traceability Mandatory) violated in our own documentation
- Audit finds gaps between claims and evidence

**Prevention:**
1. Before adding evidence, identify target strand in SAFETY_CASE_SKELETON.md:
   - E-V1 -> Strand V (Verification Precedes Action)
   - E-T1, E-T2 -> Strand T (Truth Boundaries)
   - E-I1, E-I2 -> Strand I (Invariant Gates)
2. Update Evidence Registry (lines 169-178) with status and links
3. Update Confidence Assessment matrix (lines 203-212)
4. Add bi-directional links from evidence file back to safety case

**Detection (Warning Signs):**
- New USE_CASE_EVIDENCE.md files without safety case links
- Evidence Registry entries marked "Pending" after validation complete
- Confidence levels unchanged after new evidence collected

**Phase:** A02-T6, A03-T6 (Documentation tasks)

---

### Pitfall 12: Evaluation Methodology Drift from Pre-Registration

**What goes wrong:** Validation study deviates from pre-registered methodology without documentation, invalidating pre-registration benefits.

**Why it happens:** During implementation, teams discover the pre-registered plan needs adjustment. Changes are made but not documented as deviations.

**Consequences:**
- EVALUATION_METHODOLOGY.md lines 87-95 state pre-registration commitment
- Undocumented deviations look like p-hacking or post-hoc adjustment
- Peer review challenges validity of claims

**Prevention:**
1. **Timestamp the methodology** (already done via git commit, line 91)
2. For any deviation from plan:
   - Document the change
   - Document the reason
   - Document when decision was made (before/during/after data collection)
3. Maintain "Deviations from Pre-Registration" section in validation report
4. If threshold adjustments needed, justify based on pilot data (per line 35)

**Detection (Warning Signs):**
- Success thresholds differ between EVALUATION_METHODOLOGY.md and validation report
- New statistical tests not mentioned in pre-registration
- Post-hoc explanations for unexpected results

**Phase:** A02-T5, A03-T5 (Validation tasks)

---

## Sources

**HELM Documentation and Research:**
- [Stanford CRFM HELM](https://crfm.stanford.edu/helm/)
- [HELM Safety](https://crfm.stanford.edu/2024/11/08/helm-safety.html)
- [CRFM HELM ReadTheDocs - Adding New Scenarios](https://crfm-helm.readthedocs.io/en/latest/adding_new_scenarios/)
- [IBM HELM Enterprise Benchmark](https://github.com/IBM/helm-enterprise-benchmark)
- [HELM Benchmark Overview (Statsig)](https://www.statsig.com/perspectives/helm-benchmark-llm-eval)

**CI/CD and GitHub Actions:**
- [GitHub Actions CI/CD Best Practices](https://github.com/github/awesome-copilot/blob/main/instructions/github-actions-ci-cd-best-practices.instructions.md)
- [GitHub Actions Quality Gate Samples](https://github.com/tspascoal/GitHubActions.Gates.Samples)
- [Flaky Tests in 2026 (AccelQ)](https://www.accelq.com/blog/flaky-tests/)
- [Flaky Test Quarantine (minware)](https://www.minware.com/guide/best-practices/flaky-test-quarantine)
- [GitHub SARIF Support](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)
- [Dismiss-Alerts Action](https://github.com/advanced-security/dismiss-alerts)

**AI Safety Evaluation:**
- [AI Safety Index 2025 (Future of Life Institute)](https://futureoflife.org/ai-safety-index-summer-2025/)
- [AI Safety Evaluations Explainer (CSET Georgetown)](https://cset.georgetown.edu/article/ai-safety-evaluations-an-explainer/)
- [LLM Evaluation Benchmarks 2025 (Responsible AI Labs)](https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025)

**Internal References:**
- `/Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT/TASK_MANAGEMENT/EVALUATION_METHODOLOGY.md`
- `/Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT/09_SAFETY_CASE/SAFETY_CASE_SKELETON.md`
- `/Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT/ADAPTER_MODULES/02_CI_SAFETY_GATE/validator_config.yaml`
- `/Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT/ADAPTER_MODULES/02_CI_SAFETY_GATE/test_cases/README.md`

---

## V&T Statement

### EXISTS
- 12 pitfalls documented with detection and prevention
- Phase-specific warnings mapped to A02-T5 through A03-T6
- Integration pitfalls with existing v1.0 system
- Sources cited with URLs and internal file references

### CONFIDENCE LEVELS
- Critical pitfalls 1-4: HIGH (verified against existing codebase and official docs)
- Moderate pitfalls 5-8: MEDIUM (based on community experience and official guidance)
- Minor pitfalls 9-10: MEDIUM (practical implementation concerns)
- Integration pitfalls 11-12: HIGH (directly derived from existing documentation)

### NOT CLAIMED
- Comprehensive coverage of all possible pitfalls (unknown unknowns exist)
- HELM-specific pitfalls beyond version compatibility (would require deeper HELM expertise)
- Quantitative false positive rates (requires empirical measurement in A02-T5)

---

*Created: 2026-01-23 | Research Phase | v1.1 Milestone Prep*
