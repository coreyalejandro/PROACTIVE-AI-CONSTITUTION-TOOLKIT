# CI Safety Gate Test Cases

This directory contains seeded test cases for validating the PROACTIVE Constitutional Safety Gate.

## Test Case Structure

Each test case is designed to:

1. Pass standard checks (valid JSON, no runtime errors)
2. Fail constitutional validation (contains I1-I6 violations)

This demonstrates that constitutional validation catches issues that standard checks miss.

## Test Cases

| File | Violation | Standard Checks | Expected Gate Result |
|------|-----------|-----------------|----------------------|
| tc01_missing_evidence.json | I1 | PASS | FAIL |
| tc02_phantom_work.json | I2 | PASS | FAIL |
| tc03_unverified_confidence.json | I3 | PASS | FAIL (warning) |
| tc04_broken_trace.json | I4 | PASS | FAIL |
| tc05_fluency_conflict.json | I5 | PASS | FAIL (warning) |
| tc06_error_bypass.json | I6 | PASS | FAIL |
| tc07_clean_output.json | None | PASS | PASS |
| tc08_multi_violation.json | I1, I2, I4 | PASS | FAIL |

## Running Tests

```bash
# Test individual case
python ../validator.py tc01_missing_evidence.json --format text

# Test all cases (per-file to avoid config exclusions)
for f in tc*.json; do
  echo "=== $f ==="
  python ../validator.py "$f" --format text
  echo ""
done
```

## Ground Truth

Each test case documents expected violations in `_test_metadata.expected_violations`.

---

## V&T

EXISTS

- `tc01_missing_evidence.json` through `tc08_multi_violation.json` - all 8 files created
- Per-case expected violations in `_test_metadata`
- `expected_gate` field for WARNING-only cases (tc03, tc05)
- Run instructions aligned to validator behavior

NOT EXIST

- `validation_results.txt` (generated in A02-T5)

VERIFIED

- All 8 test cases validated against validator.py
- 8/8 gate results match expected
- 8/8 violation detections match expected
- I1-I6 coverage confirmed with one clean control case (tc07)

FUNCTIONAL STATUS
Seeded test cases for I1-I6 coverage complete. All tests pass. Ready for A02-T5 comprehensive validation.
