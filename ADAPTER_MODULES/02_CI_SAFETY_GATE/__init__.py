"""PROACTIVE CI Safety Gate

GitHub Actions workflow that validates model outputs against PROACTIVE
constitutional invariants I1-I6.

Validates Principle: V (Verification Before Action)
Success Metric: Gate catches seeded vulnerabilities that pass standard tests
"""

__version__ = "1.0.0"
__author__ = "PROACTIVE Research Toolkit"

from .validator import (
    validate_file,
    validate_directory,
    generate_report,
    generate_sarif,
    check_invariants,
    check_invariant_i1,
    check_invariant_i2,
    check_invariant_i3,
    check_invariant_i4,
    check_invariant_i5,
    check_invariant_i6,
    load_config,
    Violation,
    ValidationResult
)
