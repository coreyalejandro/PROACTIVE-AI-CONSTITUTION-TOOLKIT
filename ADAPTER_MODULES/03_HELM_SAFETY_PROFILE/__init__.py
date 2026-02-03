"""PROACTIVE HELM Safety Profile

Wraps TruthfulQA-style evaluation with PROACTIVE metrics for Principle T (Truth or Bounded Unknown).

Important: This adapter is designed to be hard to fake.
- It does not allow “done” claims without artifacts.
- The validation runner emits an evidence bundle (run log + hashes + JSON results).
"""

__version__ = "0.1.0"

from .helm_wrapper import ScenarioResult, run_validation
from .proactive_scorer import ProactiveScore
