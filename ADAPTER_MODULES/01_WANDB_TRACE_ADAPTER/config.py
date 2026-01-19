"""
Configuration for W&B Trace Adapter

Status: STUB - Complete in A01-T3
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AdapterConfig:
    """Configuration for the W&B Trace Adapter."""
    
    # W&B settings
    wandb_project: str = "proactive-traces"
    wandb_entity: Optional[str] = None  # Uses default entity if None
    
    # Schema settings
    schema_version: str = "1.0.0"
    strict_validation: bool = True
    
    # Table settings
    max_claim_text_length: int = 500  # Truncate for display
    include_trace_chain: bool = True
    
    # Columns to include in W&B Table
    table_columns: tuple = (
        "claim_id",
        "timestamp", 
        "claim_text",
        "confidence_score",
        "epistemic_tag",
        "I1", "I2", "I3", "I4", "I5", "I6",
        "failure_mode",
        "final_decision"
    )


# Default configuration instance
DEFAULT_CONFIG = AdapterConfig()
