"""
W&B Trace Adapter
Converts PROACTIVE trace logs to W&B Tables

Status: STUB - Implementation in A01-T3
"""

import json
from typing import List, Dict, Any, Optional

# Placeholder for wandb import (installed in A01-T3)
# import wandb


def load_trace_log(filepath: str) -> List[Dict[str, Any]]:
    """Load PROACTIVE trace log from JSON file.
    
    Args:
        filepath: Path to JSON trace log file
        
    Returns:
        List of trace log entries
        
    Raises:
        FileNotFoundError: If file does not exist
        json.JSONDecodeError: If file is not valid JSON
    """
    raise NotImplementedError("Implement in A01-T3")


def validate_entry(entry: Dict[str, Any]) -> List[str]:
    """Validate a single trace log entry against schema.
    
    Args:
        entry: Single trace log entry
        
    Returns:
        List of validation errors (empty if valid)
    """
    raise NotImplementedError("Implement in A01-T3")


def convert_to_wandb_table(trace_entries: List[Dict[str, Any]]):  # -> wandb.Table
    """Convert trace log entries to W&B Table format.
    
    Args:
        trace_entries: List of validated trace log entries
        
    Returns:
        wandb.Table object ready for upload
    """
    raise NotImplementedError("Implement in A01-T3")


def upload_to_wandb(
    table,  # wandb.Table
    project: str = "proactive-traces",
    run_name: Optional[str] = None
) -> str:
    """Upload table to W&B and return run URL.
    
    Args:
        table: wandb.Table to upload
        project: W&B project name
        run_name: Optional run name (auto-generated if None)
        
    Returns:
        URL of the W&B run
    """
    raise NotImplementedError("Implement in A01-T3")


def main(input_file: str, project: str = "proactive-traces") -> str:
    """Main entry point: load, convert, upload.
    
    Args:
        input_file: Path to trace log JSON file
        project: W&B project name
        
    Returns:
        URL of the W&B run
    """
    raise NotImplementedError("Implement in A01-T3")


if __name__ == "__main__":
    print("W&B Trace Adapter - STUB")
    print("Run A01-T3 to implement")
    print()
    print("Expected usage after implementation:")
    print("  python adapter.py <trace_log.json> [project_name]")
