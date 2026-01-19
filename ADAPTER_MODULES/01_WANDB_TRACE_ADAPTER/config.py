"""
Configuration for W&B Trace Adapter
"""

from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class AdapterConfig:
    """Configuration for the W&B Trace Adapter."""
    
    # W&B settings
    wandb_project: str = "proactive-traces"
    wandb_entity: Optional[str] = None
    
    # Schema settings
    schema_version: str = "1.0.0"
    strict_validation: bool = True
    
    # Table settings
    max_claim_text_length: int = 500
    include_trace_chain: bool = True
    
    # Default tags
    default_tags: List[str] = field(default_factory=lambda: ["proactive", "trace-adapter"])


# Default configuration instance
DEFAULT_CONFIG = AdapterConfig()


def get_config(**overrides) -> AdapterConfig:
    """Get configuration with optional overrides.
    
    Args:
        **overrides: Configuration values to override
        
    Returns:
        AdapterConfig instance
    """
    return AdapterConfig(**{**DEFAULT_CONFIG.__dict__, **overrides})
