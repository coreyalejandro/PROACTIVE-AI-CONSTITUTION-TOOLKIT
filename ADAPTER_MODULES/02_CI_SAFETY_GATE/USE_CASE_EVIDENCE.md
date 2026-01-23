# Use Case Evidence: CI Safety Gate

## Status: AWAITING VALIDATION (A02-T5)

## Executive Summary

[2-3 sentences: What did we test? What did we find?]

## Validation Approach

- **Type**: Seeded vulnerability detection test
- **Test Cases**: N=[X] PRs with known constitutional violations that pass standard tests
- **Success Criteria**: Gate catches all seeded violations (100% detection rate)
- **Pre-registration**: Commit [HASH] dated [DATE]

## Key Finding

[The main result in plain English]

## Test Cases

| Case ID | Violation Type | Standard Tests | Safety Gate |
|---------|----------------|----------------|-------------|
| TC-01 | I1: Missing evidence | PASS | [EXPECTED: FAIL] |
| TC-02 | I2: Phantom file claim | PASS | [EXPECTED: FAIL] |
| TC-03 | I3: Unverified confidence | PASS | [EXPECTED: FAIL] |
| TC-04 | I4: Missing trace | PASS | [EXPECTED: FAIL] |
| TC-05 | I6: Error bypass | PASS | [EXPECTED: FAIL] |

## Quantitative Results

| Metric | Value |
|--------|-------|
| Total seeded violations | [N] |
| Detected by standard tests | [N] |
| Detected by safety gate | [N] |
| Detection rate improvement | [%] |

## Limitations

[Honest scope statement]

## Implications for Safety Case

This evidence supports Argument Strand V (Verification):

- **Claim**: [What we can now claim]
- **Confidence**: [High/Medium/Low]
- **Next steps to strengthen**: [What Pipeline A adds]

## Artifacts

- Seeded test cases: `test_cases/`
- Validation results: `data/validation_results.json`
- Full validation report: `validation_report.md`
