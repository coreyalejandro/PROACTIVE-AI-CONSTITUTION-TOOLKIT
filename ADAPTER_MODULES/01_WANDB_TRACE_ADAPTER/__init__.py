"""PROACTIVE W&B Trace Adapter

Converts PROACTIVE trace logs to Weights & Biases Tables for auditor analysis.

Validates Principle: O (Observability) + I4 (Traceability Mandatory)
Success Metric: Auditors find root cause significantly faster than baseline
"""

__version__ = "0.1.0"
__author__ = "PROACTIVE Research Toolkit"

from .adapter import load_trace_log, convert_to_wandb_table, upload_to_wandb
