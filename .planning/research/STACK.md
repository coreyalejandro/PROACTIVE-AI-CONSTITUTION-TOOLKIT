# Technology Stack: HELM Safety Profile Integration

**Project:** PROACTIVE AI Constitution Toolkit - v1.1 Milestone
**Researched:** 2026-01-23
**Focus:** Stack additions for HELM Safety Profile (Adapter 03) integration
**Overall Confidence:** HIGH

---

## Executive Summary

The HELM Safety Profile adapter requires minimal stack additions. The existing stack (Python 3.11+, PyTest, W&B SDK, GitHub Actions) already supports the integration. The key addition is **crfm-helm 0.5.11**, which is already present in the project's dependency list.

**Key finding:** The project already has `crfm-helm==0.5.11` installed. No new major dependencies are required. The stack additions focus on:
1. Ensuring correct version compatibility
2. Adding minimal supporting libraries for metrics calculation
3. Configuration for HELM scenario execution

---

## Recommended Stack

### Core Framework (Existing - No Changes)

| Technology | Version | Purpose | Status |
|------------|---------|---------|--------|
| Python | 3.11+ | Runtime | EXISTING |
| PyTest | 8.4.1 | Testing | EXISTING |
| W&B SDK | 0.24.0 | Trace logging (A01) | EXISTING |
| GitHub Actions | v4/v5 | CI/CD | EXISTING |

**Rationale:** Existing stack is sufficient. Python 3.11+ exceeds HELM's requirement (>=3.10).

### HELM Integration (Minimal Additions)

| Technology | Version | Purpose | Action Required |
|------------|---------|---------|-----------------|
| crfm-helm | 0.5.11 | HELM benchmark framework | VERIFY - Already in requirements |
| PyYAML | 6.0.2 | Configuration files | EXISTING - Already installed |

**Rationale:** The project's requirements.txt shows `crfm-helm==0.5.11` (line 468 in requirements snapshot). This is the latest stable release as of December 2024.

### Supporting Libraries (Metrics Calculation)

| Library | Version | Purpose | Action Required |
|---------|---------|---------|-----------------|
| NumPy | 2.2.5 | Numerical operations, ECE calculation | EXISTING |
| SciPy | 1.15.2 | Statistical tests (t-test, effect size) | EXISTING |
| pandas | 2.2.3 | Results aggregation and analysis | EXISTING |

**Rationale:** These are already installed and provide all statistical functionality needed for PROACTIVE metrics:
- `numpy`: ECE (Expected Calibration Error) calculation
- `scipy.stats`: Paired t-test for baseline comparison, Cohen's d calculation
- `pandas`: Results tabulation and export

### Testing Infrastructure

| Library | Version | Purpose | Action Required |
|---------|---------|---------|-----------------|
| pytest | 8.4.1 | Unit tests | EXISTING |
| pytest-mock | (via pytest) | Mocking HELM API calls | EXISTING |

**Rationale:** Testing infrastructure is complete. HELM wrapper tests will mock the HELM API to enable offline testing.

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not Alternative |
|----------|-------------|-------------|---------------------|
| Benchmark Framework | crfm-helm | lm-eval-harness | HELM is specified in project requirements; TruthfulQA integration is cleaner |
| Statistical Tests | scipy | statsmodels | scipy is lighter, already installed, sufficient for t-test and effect size |
| Configuration Format | YAML | TOML | Project already uses YAML for validator_config.yaml; consistency |
| Results Storage | JSON files | SQLite/DuckDB | JSON sufficient for 817 questions; no database complexity needed |

---

## Version Verification

### HELM Version Compatibility

**Current:** `crfm-helm==0.5.11` (verified in project requirements)

**Release notes (v0.5.11, December 4, 2024):**
- Added Claude Haiku 4.5, GPT-5.1, Gemini 3 Pro support
- Added uv package manager support
- Python >=3.10 required (project has 3.11+)

**TruthfulQA scenario status:** Included in HELM core scenarios. Located at:
```
helm.benchmark.scenarios.truthful_qa_scenario.TruthfulQAScenario
```

**Run entry syntax:**
```bash
helm-run --run-entries truthful_qa:model=openai/gpt2 --suite my-suite --max-eval-instances 10
```

**Source:** [GitHub stanford-crfm/helm](https://github.com/stanford-crfm/helm), [PyPI crfm-helm](https://pypi.org/project/crfm-helm/)

### Python Version Compatibility

| Requirement | Project | HELM | Status |
|-------------|---------|------|--------|
| Python version | 3.11+ | >=3.10 | COMPATIBLE |
| NumPy | 2.2.5 | Compatible | OK |
| Pandas | 2.2.3 | Compatible | OK |

---

## What NOT to Add

### Explicitly Excluded

| Dependency | Why NOT Add |
|------------|-------------|
| transformers | Only needed if running local models; HELM wraps this when needed |
| torch | Only needed for local model inference; defer to HELM's optional dependency |
| openai SDK directly | HELM provides unified model interface; use HELM's model adapters |
| anthropic SDK directly | Same as above; HELM handles model-specific APIs |
| langchain | Evaluation adapter, not agent framework; unnecessary complexity |
| mlflow | W&B already provides experiment tracking; avoid duplication |
| duckdb/sqlite | JSON files sufficient for 817-question benchmark results |

**Rationale:** Each excluded dependency adds maintenance burden without solving a problem the existing stack cannot address. HELM abstracts model API calls, so direct SDK dependencies are unnecessary.

### Dependency Management Strategy

**Do NOT add to base requirements:**
- Model provider SDKs (openai, anthropic, google-generativeai)
- GPU/CUDA libraries
- Heavy ML frameworks (torch, tensorflow)

**Reason:** These are HELM's optional dependencies. Users who want specific model support install HELM extras:
```bash
pip install crfm-helm[openai]    # For OpenAI models
pip install crfm-helm[anthropic] # For Anthropic models
```

---

## Integration Points with Existing Stack

### W&B Integration (A01)

**Status:** No changes needed. HELM adapter (A03) is independent.

**Optional future integration:**
- Log HELM evaluation results to W&B Tables
- Use existing `adapter.py` patterns for table structure
- **Defer to v1.2+** - Not in v1.1 scope

### CI Safety Gate (A02)

**Status:** No stack changes needed for A03.

**Integration pattern:**
- A02 validates model output files
- A03 validates benchmark responses
- Both produce evidence for safety case
- No code dependency between adapters

### GitHub Actions (CI/CD)

**Status:** Existing workflow sufficient.

**Considerations for A03:**
- HELM evaluations are slow (API calls)
- Do NOT run full HELM evaluations in CI
- Use `--max-eval-instances 10` for CI smoke tests
- Full evaluations run manually or scheduled

---

## Installation Commands

### Verify Existing Stack (No Installation Needed)

```bash
# Verify crfm-helm is installed
python -c "import helm; print(helm.__version__)"
# Expected: 0.5.11

# Verify supporting libraries
python -c "import numpy; import scipy; import pandas; print('OK')"
```

### For Fresh Environment (Reference Only)

```bash
# Core requirements (already in project)
pip install crfm-helm==0.5.11
pip install pyyaml>=6.0.0
pip install numpy>=2.0.0
pip install scipy>=1.10.0
pip install pandas>=2.0.0

# Development tools (already in project)
pip install pytest>=8.0.0
```

### HELM Model Extras (Optional - User Responsibility)

```bash
# If user needs OpenAI model access
pip install crfm-helm[openai]

# If user needs Anthropic model access
pip install crfm-helm[anthropic]

# If user needs Google model access
pip install crfm-helm[google]
```

---

## Configuration Files

### New Files to Create

| File | Purpose | Location |
|------|---------|----------|
| `proactive_metrics.yaml` | Metric definitions and thresholds | `ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/` |
| `scenario_config.yaml` | HELM scenario configuration | `ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/` |
| `helm_results_schema.json` | Output validation schema | `ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/` |

### Configuration Patterns (From Existing Adapters)

**Follow A02 pattern:**
```yaml
# proactive_metrics.yaml (similar to validator_config.yaml)
metrics:
  epistemic_accuracy:
    description: "Accuracy of epistemic tag classification"
    threshold: 0.8
    severity: "ERROR"

  expected_calibration_error:
    description: "ECE for confidence calibration"
    threshold: 0.15
    severity: "WARNING"

  bounded_unknown_rate:
    description: "Rate of appropriate 'unknown' responses"
    threshold: 0.1
    severity: "INFO"
```

---

## Environment Variables

### Required for Model Access

| Variable | Purpose | When Needed |
|----------|---------|-------------|
| `OPENAI_API_KEY` | OpenAI model access | If using OpenAI models |
| `ANTHROPIC_API_KEY` | Anthropic model access | If using Anthropic models |
| `GOOGLE_API_KEY` | Google model access | If using Google models |

**Note:** API keys are only needed when running actual evaluations. Mock/test mode does not require credentials.

### GitHub Actions Secrets (For CI)

```yaml
# In workflow file
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

**Recommendation:** For v1.1, use mocked responses in CI. Real API evaluations run manually.

---

## Stack Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| HELM version breaking change | LOW | MEDIUM | Pin to 0.5.11, test before upgrading |
| API rate limits | MEDIUM | LOW | Use `--max-eval-instances` to limit requests |
| TruthfulQA dataset changes | LOW | LOW | HELM manages dataset downloads |
| Python 3.12+ compatibility | LOW | LOW | HELM supports 3.10+; 3.11 is stable |

---

## Summary: Stack Changes for v1.1

### Added (Already Present)

| Component | Status | Notes |
|-----------|--------|-------|
| crfm-helm 0.5.11 | EXISTING | Verify installation only |
| NumPy 2.2.5 | EXISTING | Already in requirements |
| SciPy 1.15.2 | EXISTING | Already in requirements |
| pandas 2.2.3 | EXISTING | Already in requirements |
| PyYAML 6.0.2 | EXISTING | Already in requirements |

### Not Added (Explicit Exclusion)

| Component | Reason |
|-----------|--------|
| Direct model SDKs | HELM provides unified interface |
| Heavy ML frameworks | Not needed for evaluation adapter |
| Database systems | JSON sufficient for benchmark scale |
| Additional CI platforms | GitHub Actions is primary target |

### Configuration Required

| File | Purpose | Priority |
|------|---------|----------|
| proactive_metrics.yaml | Metric thresholds | A03-T1 |
| scenario_config.yaml | HELM scenario config | A03-T1 |
| helm_results_schema.json | Output validation | A03-T1 |

---

## Sources

### Official Documentation (HIGH Confidence)

- [HELM GitHub Repository](https://github.com/stanford-crfm/helm) - Source code, installation docs
- [HELM Installation Guide](https://github.com/stanford-crfm/helm/blob/main/docs/installation.md) - Python requirements, setup
- [HELM PyPI Page](https://pypi.org/project/crfm-helm/) - Package version, dependencies
- [HELM Releases](https://github.com/stanford-crfm/helm/releases) - Version history, changelog

### Project Analysis (HIGH Confidence)

- Existing requirements.txt analysis (crfm-helm 0.5.11 present)
- Existing adapter patterns (A01, A02) for configuration style
- CI Safety Gate validator.py for integration approach

### Version Verification (HIGH Confidence)

- crfm-helm 0.5.11 released December 4, 2024
- Python >=3.10 requirement verified in official docs
- TruthfulQA scenario confirmed in HELM source code

---

## Confidence Assessment

| Area | Level | Reason |
|------|-------|--------|
| Core dependencies | HIGH | Direct verification of requirements.txt |
| HELM version compatibility | HIGH | Official release notes and docs |
| Integration approach | HIGH | Consistent with existing adapter patterns |
| Excluded dependencies | HIGH | Clear rationale based on HELM architecture |
| Configuration patterns | HIGH | Based on existing A02 validator_config.yaml |

---

*Created: 2026-01-23 | Stack Research for HELM Safety Profile Integration*
