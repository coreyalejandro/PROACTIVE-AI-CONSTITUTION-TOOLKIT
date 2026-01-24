"""
W&B Trace Adapter
Converts PROACTIVE trace logs to W&B Tables

Version: 0.1.0
Status: IMPLEMENTED
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import wandb

# Handle both package import and direct execution
try:
    from .config import DEFAULT_CONFIG, AdapterConfig
except ImportError:
    from config import DEFAULT_CONFIG, AdapterConfig

# Required fields for validation
REQUIRED_FIELDS = [
    "claim_id", "timestamp", "claim_text", "confidence_score",
    "validator_results", "final_decision"
]

OPTIONAL_FIELDS = [
    "prompt_hash", "evidence_sources", "principle_tags", 
    "failure_mode", "epistemic_tag", "trace_chain"
]

VALIDATOR_KEYS = ["I1_check", "I2_check", "I3_check", "I4_check", "I5_check", "I6_check"]


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
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Trace log not found: {filepath}")
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Handle both single object and array formats
    if isinstance(data, dict):
        return [data]
    return data


def validate_entry(entry: Dict[str, Any]) -> List[str]:
    """Validate a single trace log entry against schema.
    
    Args:
        entry: Single trace log entry
        
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in entry:
            errors.append(f"Missing required field: {field}")
    
    # Validate validator_results structure
    if "validator_results" in entry:
        vr = entry["validator_results"]
        for key in VALIDATOR_KEYS:
            if key not in vr:
                errors.append(f"Missing validator key: {key}")
            elif vr[key] not in ["PASS", "FAIL", "SKIP"]:
                errors.append(f"Invalid {key} value: {vr[key]}")
    
    # Validate confidence_score range
    if "confidence_score" in entry:
        score = entry["confidence_score"]
        if not isinstance(score, (int, float)) or score < 0 or score > 1:
            errors.append(f"Invalid confidence_score: {score} (must be 0.0-1.0)")
    
    # Validate final_decision
    if "final_decision" in entry:
        decision = entry["final_decision"]
        if decision not in ["EMIT", "BLOCK", "ESCALATE"]:
            errors.append(f"Invalid final_decision: {decision}")
    
    # Validate epistemic_tag if present
    if "epistemic_tag" in entry and entry["epistemic_tag"]:
        tag = entry["epistemic_tag"]
        if tag not in ["OBSERVED", "INFERRED", "SPECULATED"]:
            errors.append(f"Invalid epistemic_tag: {tag}")
    
    # Validate failure_mode if present
    if "failure_mode" in entry and entry["failure_mode"]:
        fm = entry["failure_mode"]
        if fm not in ["F1", "F2", "F3", "F4", "F5"]:
            errors.append(f"Invalid failure_mode: {fm}")
    
    return errors


def validate_all(entries: List[Dict[str, Any]], strict: bool = True) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Validate all entries and separate valid from invalid.
    
    Args:
        entries: List of trace log entries
        strict: If True, reject entries with any errors
        
    Returns:
        Tuple of (valid_entries, invalid_entries_with_errors)
    """
    valid = []
    invalid = []
    
    for i, entry in enumerate(entries):
        errors = validate_entry(entry)
        if errors:
            if strict:
                invalid.append({"index": i, "entry": entry, "errors": errors})
            else:
                # In non-strict mode, still include with warnings
                valid.append(entry)
                print(f"Warning: Entry {i} has validation issues: {errors}")
        else:
            valid.append(entry)
    
    return valid, invalid


def convert_to_wandb_table(
    trace_entries: List[Dict[str, Any]], 
    config: Optional[AdapterConfig] = None
) -> wandb.Table:
    """Convert trace log entries to W&B Table format.
    
    Args:
        trace_entries: List of validated trace log entries
        config: Optional configuration (uses DEFAULT_CONFIG if None)
        
    Returns:
        wandb.Table object ready for upload
    """
    if config is None:
        config = DEFAULT_CONFIG
    
    # Define columns
    columns = [
        "claim_id", "timestamp", "claim_text", "confidence_score",
        "epistemic_tag", "I1", "I2", "I3", "I4", "I5", "I6",
        "failure_mode", "final_decision", "evidence_count"
    ]
    
    if config.include_trace_chain:
        columns.extend(["trace_REQ", "trace_complete"])
    
    # Build rows
    rows = []
    for entry in trace_entries:
        validator = entry.get("validator_results", {})
        trace = entry.get("trace_chain", {})
        evidence = entry.get("evidence_sources", [])
        
        # Truncate claim text for display
        claim_text = entry.get("claim_text", "")
        if len(claim_text) > config.max_claim_text_length:
            claim_text = claim_text[:config.max_claim_text_length] + "..."
        
        row = [
            entry.get("claim_id", "UNKNOWN"),
            entry.get("timestamp", datetime.now().isoformat()),
            claim_text,
            entry.get("confidence_score", 0.0),
            entry.get("epistemic_tag", "UNKNOWN"),
            validator.get("I1_check", "SKIP"),
            validator.get("I2_check", "SKIP"),
            validator.get("I3_check", "SKIP"),
            validator.get("I4_check", "SKIP"),
            validator.get("I5_check", "SKIP"),
            validator.get("I6_check", "SKIP"),
            entry.get("failure_mode") or "none",
            entry.get("final_decision", "UNKNOWN"),
            len(evidence)
        ]
        
        if config.include_trace_chain:
            # Add trace chain info
            trace_req = trace.get("REQ_id", "MISSING")
            trace_complete = all([
                trace.get("REQ_id"),
                trace.get("CTRL_id"),
                trace.get("TEST_id"),
                trace.get("EVID_id"),
                trace.get("DECISION_id")
            ])
            row.extend([trace_req, trace_complete])
        
        rows.append(row)
    
    return wandb.Table(columns=columns, data=rows)


def upload_to_wandb(
    table: wandb.Table,
    project: str = "proactive-traces",
    run_name: Optional[str] = None,
    entity: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> str:
    """Upload table to W&B and return run URL.
    
    Args:
        table: wandb.Table to upload
        project: W&B project name
        run_name: Optional run name (auto-generated if None)
        entity: Optional W&B entity (team/user)
        tags: Optional tags for the run
        
    Returns:
        URL of the W&B run
    """
    if run_name is None:
        run_name = f"trace-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    if tags is None:
        tags = ["proactive", "trace-adapter"]
    
    run = wandb.init(
        project=project,
        name=run_name,
        entity=entity,
        tags=tags,
        job_type="trace-upload"
    )
    
    # Log the table
    run.log({"trace_log": table})
    
    # Log summary metrics
    run.summary["total_entries"] = len(table.data)
    run.summary["schema_version"] = DEFAULT_CONFIG.schema_version
    
    url = run.get_url()
    run.finish()
    
    return url


def main(input_file: str, project: str = "proactive-traces", strict: bool = True) -> str:
    """Main entry point: load, validate, convert, upload.
    
    Args:
        input_file: Path to trace log JSON file
        project: W&B project name
        strict: If True, reject entries with validation errors
        
    Returns:
        URL of the W&B run
    """
    print(f"Loading trace log from: {input_file}")
    entries = load_trace_log(input_file)
    print(f"Loaded {len(entries)} entries")
    
    # Validate
    print("Validating entries...")
    valid, invalid = validate_all(entries, strict=strict)
    print(f"Valid: {len(valid)}, Invalid: {len(invalid)}")
    
    if invalid:
        print("\nValidation errors:")
        for item in invalid[:5]:  # Show first 5 errors
            print(f"  Entry {item['index']}: {item['errors']}")
        if len(invalid) > 5:
            print(f"  ... and {len(invalid) - 5} more")
    
    if not valid:
        raise ValueError("No valid entries to upload")
    
    # Convert
    print("\nConverting to W&B Table...")
    table = convert_to_wandb_table(valid)
    print(f"Created table with {len(table.columns)} columns, {len(table.data)} rows")
    
    # Upload
    print("\nUploading to W&B...")
    url = upload_to_wandb(table, project=project)
    print(f"\nSuccess! View at: {url}")
    
    return url


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python adapter.py <trace_log.json> [project_name] [--no-strict]")
        print()
        print("Arguments:")
        print("  trace_log.json  Path to PROACTIVE trace log file")
        print("  project_name    W&B project name (default: proactive-traces)")
        print("  --no-strict     Allow entries with validation warnings")
        sys.exit(1)
    
    input_file = sys.argv[1]
    project = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "proactive-traces"
    strict = "--no-strict" not in sys.argv
    
    try:
        main(input_file, project, strict)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
