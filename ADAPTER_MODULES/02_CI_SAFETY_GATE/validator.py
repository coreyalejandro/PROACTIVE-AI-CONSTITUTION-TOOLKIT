"""
PROACTIVE Constitutional Validator
Validates model outputs against I1-I6 invariants

Version: 1.0.0
Status: IMPLEMENTED
"""

import json
import re
import os
import fnmatch
import time
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import uuid

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


@dataclass
class Violation:
    """Single constitutional violation."""
    violation_id: str
    invariant: str
    severity: str
    location: Dict[str, Any]
    message: str
    suggested_fix: Optional[str] = None
    evidence: Optional[Dict[str, Any]] = None
    rule_id: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class ValidationResult:
    """Result of validating a single file."""
    file_path: str
    violations: List[Violation] = field(default_factory=list)
    
    @property
    def has_errors(self) -> bool:
        return any(v.severity == "ERROR" for v in self.violations)
    
    @property
    def error_count(self) -> int:
        return sum(1 for v in self.violations if v.severity == "ERROR")
    
    @property
    def warning_count(self) -> int:
        return sum(1 for v in self.violations if v.severity == "WARNING")


# Global config (loaded once)
_config: Optional[Dict[str, Any]] = None


def _get_default_config() -> Dict[str, Any]:
    """Return default configuration when YAML not available or file not found."""
    return {
        "validator": {
            "name": "PROACTIVE Constitutional Safety Gate",
            "version": "1.0.0"
        },
        "invariants": {
            "I1_evidence_first": {
                "enabled": True, 
                "severity": "ERROR",
                "patterns": [
                    {"pattern": r"\b(certainly|definitely|absolutely|guaranteed|always|never)\b",
                     "message": "Absolute claim without epistemic qualification"},
                    {"pattern": r"\b(I am sure|I am certain|there is no doubt)\b",
                     "message": "Certainty expression without evidence reference"}
                ],
                "required_tags": ["OBSERVED", "INFERRED", "SPECULATED"]
            },
            "I2_no_phantom_work": {
                "enabled": True, 
                "severity": "ERROR",
                "validators": [
                    {"type": "file_existence",
                     "patterns": [
                         r'(?:created|generated|wrote|saved|output).*?["\']([^"\']+\.[a-zA-Z]{2,5})["\']',
                         r'(?:file|document|report)\s+["\']([^"\']+\.[a-zA-Z]{2,5})["\'].*?(?:created|ready|complete)'
                     ]},
                    {"type": "artifact_verification",
                     "patterns": [r"\b(completed|finished|done|implemented)\b.*\b(all|every|entire)\b"]}
                ]
            },
            "I3_confidence_requires_verification": {
                "enabled": True, 
                "severity": "WARNING",
                "confidence_threshold": 0.8,
                "patterns": [{"pattern": r"confidence[:\s]*([01]\.?\d*)"}],
                "verification_keywords": ["verified", "tested", "validated", "confirmed", "evidence", "proof", "artifact"]
            },
            "I4_traceability_mandatory": {
                "enabled": True, 
                "severity": "ERROR",
                "required_trace_fields": ["REQ_id", "CTRL_id", "TEST_id", "EVID_id", "DECISION_id"],
                "patterns": [{"pattern": r"\b(decided|decision|approved|rejected|selected)\b",
                             "message": "Decision statement without trace chain reference"}]
            },
            "I5_safety_over_fluency": {
                "enabled": True, 
                "severity": "WARNING",
                "patterns": [
                    {"pattern": r"(?:seems? like|probably|might|could be|appears to).*?(?:certain|definite|high confidence)",
                     "message": "Hedging language combined with certainty"},
                    {"pattern": r"(?:certain|definite|high confidence).*?(?:seems? like|probably|might|could be|appears to)",
                     "message": "Certainty combined with hedging language"}
                ]
            },
            "I6_fail_closed": {
                "enabled": True, 
                "severity": "ERROR",
                "patterns": [
                    {"pattern": r"(?:ignore|suppress|skip|bypass|work around).*?(?:error|exception|failure|warning)",
                     "message": "Attempting to bypass error instead of fail-closed behavior"},
                    {"pattern": r"(?:error|exception|failure).*?(?:ignore|suppress|skip|continue anyway)",
                     "message": "Continuing despite error instead of fail-closed behavior"},
                    {"pattern": r"try\s*:.*?except\s*:?\s*pass",
                     "message": "Silent exception handling - should surface error"},
                    {"pattern": r"catch.*?\{\s*(?://.*?continue|/\*.*?\*/\s*\})",
                     "message": "Empty catch block - should surface error"}
                ]
            }
        },
        "gate": {
            "fail_on_error": True,
            "fail_on_warning": False,
            "warning_threshold": 5,
            "output_format": "sarif"
        },
        "validation_targets": {
            "include": ["**/*.json", "**/*.yaml", "**/*.yml", "**/outputs/*.md", "**/claims/*.txt"],
            "exclude": ["node_modules/**", ".git/**", "**/*.test.*", "**/test_cases/**", "**/__pycache__/**"]
        },
        "logging": {
            "max_context_length": 200
        }
    }


def load_config(config_path: str = "validator_config.yaml") -> Dict[str, Any]:
    """Load validator configuration from YAML file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    global _config
    if _config is not None:
        return _config
    
    path = Path(config_path)
    if path.exists() and YAML_AVAILABLE:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                _config = yaml.safe_load(f)
            return _config
        except Exception as e:
            print(f"Warning: Could not load config from {config_path}: {e}")
    
    _config = _get_default_config()
    return _config


def reset_config() -> None:
    """Reset config to force reload on next access."""
    global _config
    _config = None


def _generate_violation_id() -> str:
    """Generate unique violation ID matching schema pattern ^V-[A-F0-9]{4}$."""
    return f"V-{uuid.uuid4().hex[:4].upper()}"


def _find_line_number(content: str, match_start: int) -> int:
    """Find line number for a match position (1-indexed)."""
    return content[:match_start].count('\n') + 1


def _get_context(content: str, match_start: int, match_end: int, max_length: int = 200) -> str:
    """Extract context around a match."""
    # Get some context before and after
    context_start = max(0, match_start - 50)
    context_end = min(len(content), match_end + 50)
    context = content[context_start:context_end]
    
    # Truncate if too long
    if len(context) > max_length:
        context = context[:max_length] + "..."
    
    return context.replace('\n', ' ').strip()


def check_invariant_i1(content: str, file_path: str) -> List[Violation]:
    """Check I1: Evidence-First Outputs.
    
    Every claim must carry an epistemic tag and supporting evidence.
    """
    violations = []
    config = load_config()
    i1_config = config.get("invariants", {}).get("I1_evidence_first", {})
    
    if not i1_config.get("enabled", True):
        return violations
    
    severity = i1_config.get("severity", "ERROR")
    patterns = i1_config.get("patterns", [])
    required_tags = i1_config.get("required_tags", ["OBSERVED", "INFERRED", "SPECULATED"])
    max_context = config.get("logging", {}).get("max_context_length", 200)
    
    # Build epistemic tag pattern
    tag_pattern = r'\[(' + '|'.join(required_tags) + r')\]'
    
    for pattern_def in patterns:
        pattern = pattern_def.get("pattern", "")
        message = pattern_def.get("message", "I1 violation detected")
        
        if not pattern:
            continue
            
        try:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                line_num = _find_line_number(content, match.start())
                
                # Check if epistemic tag exists nearby (within 300 chars)
                context_start = max(0, match.start() - 300)
                context_end = min(len(content), match.end() + 300)
                context_window = content[context_start:context_end]
                
                if not re.search(tag_pattern, context_window):
                    violations.append(Violation(
                        violation_id=_generate_violation_id(),
                        invariant="I1",
                        severity=severity,
                        location={
                            "file": file_path,
                            "line": line_num,
                            "context": _get_context(content, match.start(), match.end(), max_context)
                        },
                        message=f"I1 Violation: {message}",
                        suggested_fix=f"Add epistemic tag: [{required_tags[0]}], [{required_tags[1]}], or [{required_tags[2]}]",
                        evidence={
                            "matched_pattern": pattern,
                            "matched_text": match.group()[:100]
                        },
                        rule_id="I1_evidence_first"
                    ))
        except re.error as e:
            print(f"Warning: Invalid regex pattern in I1 config: {pattern} - {e}")
    
    return violations


def check_invariant_i2(content: str, file_path: str, workspace: str) -> List[Violation]:
    """Check I2: No Phantom Work.
    
    Cannot claim work is complete unless artifact exists.
    """
    violations = []
    config = load_config()
    i2_config = config.get("invariants", {}).get("I2_no_phantom_work", {})
    
    if not i2_config.get("enabled", True):
        return violations
    
    severity = i2_config.get("severity", "ERROR")
    validators = i2_config.get("validators", [])
    max_context = config.get("logging", {}).get("max_context_length", 200)
    
    for validator in validators:
        val_type = validator.get("type", "")
        patterns = validator.get("patterns", [])
        
        if val_type == "file_existence":
            # Check for file creation claims
            for pattern in patterns:
                try:
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        # Extract the claimed filename (group 1)
                        if match.groups():
                            claimed_file = match.group(1)
                            line_num = _find_line_number(content, match.start())
                            
                            # Check if file exists
                            full_path = Path(workspace) / claimed_file
                            if not full_path.exists():
                                violations.append(Violation(
                                    violation_id=_generate_violation_id(),
                                    invariant="I2",
                                    severity=severity,
                                    location={
                                        "file": file_path,
                                        "line": line_num,
                                        "context": _get_context(content, match.start(), match.end(), max_context)
                                    },
                                    message=f"I2 Violation: Claimed file '{claimed_file}' does not exist",
                                    suggested_fix=f"Create the file '{claimed_file}' or remove the completion claim",
                                    evidence={
                                        "claimed_file": claimed_file,
                                        "checked_path": str(full_path),
                                        "validation_type": "file_existence"
                                    },
                                    rule_id="I2_file_existence"
                                ))
                except re.error as e:
                    print(f"Warning: Invalid regex pattern in I2 config: {pattern} - {e}")
        
        elif val_type == "artifact_verification":
            # Check for completion claims without evidence reference
            for pattern in patterns:
                try:
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        line_num = _find_line_number(content, match.start())
                        
                        # Check if evidence reference exists nearby
                        context_start = max(0, match.start() - 150)
                        context_end = min(len(content), match.end() + 150)
                        context_window = content[context_start:context_end]
                        
                        evidence_pattern = r'(?:evidence|proof|verified|tested|see|ref|artifact)'
                        if not re.search(evidence_pattern, context_window, re.IGNORECASE):
                            violations.append(Violation(
                                violation_id=_generate_violation_id(),
                                invariant="I2",
                                severity=severity,
                                location={
                                    "file": file_path,
                                    "line": line_num,
                                    "context": _get_context(content, match.start(), match.end(), max_context)
                                },
                                message="I2 Violation: Completion claim without evidence reference",
                                suggested_fix="Add reference to verification artifact",
                                evidence={
                                    "matched_pattern": pattern,
                                    "matched_text": match.group()[:100],
                                    "validation_type": "artifact_verification"
                                },
                                rule_id="I2_artifact_verification"
                            ))
                except re.error as e:
                    print(f"Warning: Invalid regex pattern in I2 config: {pattern} - {e}")
    
    return violations


def check_invariant_i3(content: str, file_path: str) -> List[Violation]:
    """Check I3: Confidence Requires Verification.
    
    High confidence requires verification artifacts.
    """
    violations = []
    config = load_config()
    i3_config = config.get("invariants", {}).get("I3_confidence_requires_verification", {})
    
    if not i3_config.get("enabled", True):
        return violations
    
    severity = i3_config.get("severity", "WARNING")
    threshold = i3_config.get("confidence_threshold", 0.8)
    patterns = i3_config.get("patterns", [])
    verification_keywords = i3_config.get("verification_keywords", 
        ["verified", "tested", "validated", "confirmed", "evidence", "proof", "artifact"])
    max_context = config.get("logging", {}).get("max_context_length", 200)
    
    # Build verification keyword pattern
    verification_pattern = r'(?:' + '|'.join(verification_keywords) + r')'
    
    for pattern_def in patterns:
        pattern = pattern_def.get("pattern", r"confidence[:\s]*([01]\.?\d*)")
        
        try:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                # Try to extract confidence value
                try:
                    if match.groups():
                        confidence = float(match.group(1))
                    else:
                        continue
                        
                    if confidence >= threshold:
                        line_num = _find_line_number(content, match.start())
                        
                        # Check for verification reference nearby
                        context_start = max(0, match.start() - 300)
                        context_end = min(len(content), match.end() + 300)
                        context_window = content[context_start:context_end]
                        
                        if not re.search(verification_pattern, context_window, re.IGNORECASE):
                            violations.append(Violation(
                                violation_id=_generate_violation_id(),
                                invariant="I3",
                                severity=severity,
                                location={
                                    "file": file_path,
                                    "line": line_num,
                                    "context": _get_context(content, match.start(), match.end(), max_context)
                                },
                                message=f"I3 Violation: High confidence ({confidence}) without verification reference",
                                suggested_fix="Add reference to verification artifact or reduce confidence",
                                evidence={
                                    "confidence_value": confidence,
                                    "threshold": threshold
                                },
                                rule_id="I3_confidence_verification"
                            ))
                except ValueError:
                    continue
        except re.error as e:
            print(f"Warning: Invalid regex pattern in I3 config: {pattern} - {e}")
    
    return violations


def check_invariant_i4(content: str, file_path: str) -> List[Violation]:
    """Check I4: Traceability Is Mandatory.
    
    Every decision must be traceable through REQ → CTRL → TEST → EVID → DECISION.
    """
    violations = []
    config = load_config()
    i4_config = config.get("invariants", {}).get("I4_traceability_mandatory", {})
    
    if not i4_config.get("enabled", True):
        return violations
    
    severity = i4_config.get("severity", "ERROR")
    required_fields = i4_config.get("required_trace_fields", 
        ["REQ_id", "CTRL_id", "TEST_id", "EVID_id", "DECISION_id"])
    patterns = i4_config.get("patterns", [])
    max_context = config.get("logging", {}).get("max_context_length", 200)
    
    # Check if this looks like a trace document
    is_trace_doc = "trace_chain" in content.lower() or "decision_id" in content.lower()
    
    if is_trace_doc:
        # Check for required trace fields
        for field in required_fields:
            field_pattern = rf'["\']?{field}["\']?\s*[:=]'
            if not re.search(field_pattern, content, re.IGNORECASE):
                violations.append(Violation(
                    violation_id=_generate_violation_id(),
                    invariant="I4",
                    severity=severity,
                    location={
                        "file": file_path,
                        "line": 1
                    },
                    message=f"I4 Violation: Missing required trace field '{field}'",
                    suggested_fix=f"Add {field} to complete the trace chain",
                    evidence={
                        "missing_field": field,
                        "required_fields": required_fields
                    },
                    rule_id="I4_missing_trace_field"
                ))
    
    # Check for decision statements without trace reference
    for pattern_def in patterns:
        pattern = pattern_def.get("pattern", r"\b(decided|decision|approved|rejected|selected)\b")
        message = pattern_def.get("message", "Decision statement without trace chain reference")
        
        try:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                line_num = _find_line_number(content, match.start())
                
                # Check if trace reference exists nearby
                context_start = max(0, match.start() - 400)
                context_end = min(len(content), match.end() + 400)
                context_window = content[context_start:context_end]
                
                trace_pattern = r'(?:REQ|CTRL|TEST|EVID|DECISION|trace_chain|trace)'
                if not re.search(trace_pattern, context_window, re.IGNORECASE):
                    violations.append(Violation(
                        violation_id=_generate_violation_id(),
                        invariant="I4",
                        severity=severity,
                        location={
                            "file": file_path,
                            "line": line_num,
                            "context": _get_context(content, match.start(), match.end(), max_context)
                        },
                        message=f"I4 Violation: {message}",
                        suggested_fix="Add trace chain (REQ → CTRL → TEST → EVID → DECISION)",
                        evidence={
                            "matched_text": match.group()
                        },
                        rule_id="I4_decision_without_trace"
                    ))
        except re.error as e:
            print(f"Warning: Invalid regex pattern in I4 config: {pattern} - {e}")
    
    return violations


def check_invariant_i5(content: str, file_path: str) -> List[Violation]:
    """Check I5: Safety Over Fluency.
    
    Bounded statements preferred over fluent-but-wrong.
    """
    violations = []
    config = load_config()
    i5_config = config.get("invariants", {}).get("I5_safety_over_fluency", {})
    
    if not i5_config.get("enabled", True):
        return violations
    
    severity = i5_config.get("severity", "WARNING")
    patterns = i5_config.get("patterns", [])
    max_context = config.get("logging", {}).get("max_context_length", 200)
    
    for pattern_def in patterns:
        pattern = pattern_def.get("pattern", "")
        message = pattern_def.get("message", "Hedging language inconsistent with confidence claim")
        
        if not pattern:
            continue
            
        try:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                line_num = _find_line_number(content, match.start())
                violations.append(Violation(
                    violation_id=_generate_violation_id(),
                    invariant="I5",
                    severity=severity,
                    location={
                        "file": file_path,
                        "line": line_num,
                        "context": _get_context(content, match.start(), match.end(), max_context)
                    },
                    message=f"I5 Violation: {message}",
                    suggested_fix="Choose either hedged or confident language, not both",
                    evidence={
                        "matched_pattern": pattern,
                        "matched_text": match.group()[:100]
                    },
                    rule_id="I5_fluency_conflict"
                ))
        except re.error as e:
            print(f"Warning: Invalid regex pattern in I5 config: {pattern} - {e}")
    
    return violations


def check_invariant_i6(content: str, file_path: str) -> List[Violation]:
    """Check I6: Fail Closed.
    
    Stop and surface failures; do not work around.
    """
    violations = []
    config = load_config()
    i6_config = config.get("invariants", {}).get("I6_fail_closed", {})
    
    if not i6_config.get("enabled", True):
        return violations
    
    severity = i6_config.get("severity", "ERROR")
    patterns = i6_config.get("patterns", [])
    max_context = config.get("logging", {}).get("max_context_length", 200)
    
    for pattern_def in patterns:
        pattern = pattern_def.get("pattern", "")
        message = pattern_def.get("message", "Detected attempt to bypass failure")
        
        if not pattern:
            continue
            
        try:
            for match in re.finditer(pattern, content, re.IGNORECASE | re.DOTALL):
                line_num = _find_line_number(content, match.start())
                violations.append(Violation(
                    violation_id=_generate_violation_id(),
                    invariant="I6",
                    severity=severity,
                    location={
                        "file": file_path,
                        "line": line_num,
                        "context": _get_context(content, match.start(), match.end(), max_context)
                    },
                    message=f"I6 Violation: {message}",
                    suggested_fix="Surface the error to user instead of suppressing",
                    evidence={
                        "matched_pattern": pattern,
                        "matched_text": match.group()[:200]
                    },
                    rule_id="I6_fail_closed"
                ))
        except re.error as e:
            print(f"Warning: Invalid regex pattern in I6 config: {pattern} - {e}")
    
    return violations


def check_invariants(content: str, file_path: str, workspace: str = ".") -> List[Violation]:
    """Run all I1-I6 invariant checks on content.
    
    Args:
        content: File content to validate
        file_path: Path to file for location reporting
        workspace: Workspace root for file existence checks
        
    Returns:
        Combined list of all violations
    """
    all_violations = []
    
    all_violations.extend(check_invariant_i1(content, file_path))
    all_violations.extend(check_invariant_i2(content, file_path, workspace))
    all_violations.extend(check_invariant_i3(content, file_path))
    all_violations.extend(check_invariant_i4(content, file_path))
    all_violations.extend(check_invariant_i5(content, file_path))
    all_violations.extend(check_invariant_i6(content, file_path))
    
    return all_violations


def validate_file(file_path: str, workspace: str = ".") -> ValidationResult:
    """Validate a single file against constitutional invariants.
    
    Args:
        file_path: Path to file to validate
        workspace: Workspace root for file existence checks
        
    Returns:
        ValidationResult with any violations found
    """
    path = Path(file_path)
    if not path.exists():
        return ValidationResult(file_path=file_path, violations=[
            Violation(
                violation_id=_generate_violation_id(),
                invariant="SYSTEM",
                severity="ERROR",
                location={"file": file_path},
                message=f"File not found: {file_path}"
            )
        ])
    
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        return ValidationResult(file_path=file_path, violations=[
            Violation(
                violation_id=_generate_violation_id(),
                invariant="SYSTEM",
                severity="ERROR",
                location={"file": file_path},
                message=f"Error reading file: {e}"
            )
        ])
    
    violations = check_invariants(content, file_path, workspace)
    return ValidationResult(file_path=file_path, violations=violations)


def _match_patterns(path: str, patterns: List[str]) -> bool:
    """Check if path matches any of the glob patterns."""
    for pattern in patterns:
        # Handle ** patterns
        if "**" in pattern:
            # Convert glob to regex-like matching
            regex_pattern = pattern.replace("**", ".*").replace("*", "[^/]*")
            if re.match(regex_pattern, path):
                return True
        elif fnmatch.fnmatch(path, pattern):
            return True
        elif fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False


def validate_directory(
    directory: str,
    include_patterns: Optional[List[str]] = None,
    exclude_patterns: Optional[List[str]] = None
) -> List[ValidationResult]:
    """Validate all matching files in a directory.
    
    Args:
        directory: Directory to scan
        include_patterns: Glob patterns for files to include
        exclude_patterns: Glob patterns for files to exclude
        
    Returns:
        List of ValidationResults for each file
    """
    config = load_config()
    targets = config.get("validation_targets", {})
    
    if include_patterns is None:
        include_patterns = targets.get("include", ["**/*.json", "**/*.yaml", "**/*.yml"])
    if exclude_patterns is None:
        exclude_patterns = targets.get("exclude", ["node_modules/**", ".git/**"])
    
    results = []
    root = Path(directory)
    
    if not root.exists():
        return [ValidationResult(file_path=directory, violations=[
            Violation(
                violation_id=_generate_violation_id(),
                invariant="SYSTEM",
                severity="ERROR",
                location={"file": directory},
                message=f"Directory not found: {directory}"
            )
        ])]
    
    # If directory is actually a file, validate just that file
    if root.is_file():
        return [validate_file(str(root), str(root.parent))]
    
    for path in root.rglob("*"):
        if path.is_file():
            rel_path = str(path.relative_to(root))
            
            # Check exclusions first
            if _match_patterns(rel_path, exclude_patterns):
                continue
            
            # Check inclusions
            if _match_patterns(rel_path, include_patterns):
                result = validate_file(str(path), str(root))
                results.append(result)
    
    return results


def generate_report(
    results: List[ValidationResult],
    git_context: Optional[Dict[str, str]] = None,
    config_path: Optional[str] = None
) -> Dict[str, Any]:
    """Generate a violation report matching violation_schema.json.
    
    Args:
        results: List of validation results
        git_context: Optional git metadata (commit, branch, PR)
        config_path: Optional path to config file used
        
    Returns:
        Report dictionary matching schema
    """
    all_violations = []
    files_with_violations = 0
    
    for result in results:
        all_violations.extend(result.violations)
        if result.violations:
            files_with_violations += 1
    
    # Count by invariant
    by_invariant: Dict[str, int] = {}
    for v in all_violations:
        by_invariant[v.invariant] = by_invariant.get(v.invariant, 0) + 1
    
    # Count by severity
    by_severity: Dict[str, int] = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    for v in all_violations:
        by_severity[v.severity] = by_severity.get(v.severity, 0) + 1
    
    errors = by_severity["ERROR"]
    warnings = by_severity["WARNING"]
    
    config = load_config()
    gate_config = config.get("gate", {})
    
    # Determine gate result
    gate_result = "PASS"
    gate_reason = None
    
    if gate_config.get("fail_on_error", True) and errors > 0:
        gate_result = "FAIL"
        gate_reason = f"{errors} ERROR-level violations found"
    elif gate_config.get("fail_on_warning", False) and warnings > 0:
        gate_result = "FAIL"
        gate_reason = f"{warnings} WARNING-level violations found"
    elif warnings > gate_config.get("warning_threshold", 5):
        gate_result = "FAIL"
        gate_reason = f"Warning count ({warnings}) exceeds threshold ({gate_config.get('warning_threshold', 5)})"
    
    # Build enabled invariants list
    enabled_invariants = []
    invariants_config = config.get("invariants", {})
    for key, val in invariants_config.items():
        if val.get("enabled", True):
            # Extract invariant ID (e.g., "I1" from "I1_evidence_first")
            inv_id = key.split("_")[0].upper()
            if inv_id not in enabled_invariants:
                enabled_invariants.append(inv_id)
    
    report = {
        "report_id": f"VR-{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "validator_version": config.get("validator", {}).get("version", "1.0.0"),
        "git_context": git_context or {},
        "config_used": {
            "config_path": config_path or "validator_config.yaml",
            "enabled_invariants": sorted(enabled_invariants),
            "fail_on_warning": gate_config.get("fail_on_warning", False),
            "warning_threshold": gate_config.get("warning_threshold", 5)
        },
        "violations": [v.to_dict() for v in all_violations],
        "summary": {
            "total_files_scanned": len(results),
            "files_with_violations": files_with_violations,
            "total_violations": len(all_violations),
            "errors": errors,
            "warnings": warnings,
            "by_invariant": by_invariant,
            "by_severity": by_severity,
            "gate_result": gate_result,
            "gate_reason": gate_reason
        }
    }
    
    return report


def generate_sarif(report: Dict[str, Any]) -> Dict[str, Any]:
    """Convert report to SARIF format for GitHub Security.
    
    Args:
        report: Violation report dictionary
        
    Returns:
        SARIF-formatted report
    """
    # Build rules from invariants
    rules = [
        {"id": "I1", "name": "Evidence-First Outputs", 
         "shortDescription": {"text": "Every claim must carry an epistemic tag and supporting evidence"}},
        {"id": "I2", "name": "No Phantom Work",
         "shortDescription": {"text": "Cannot claim work is complete unless artifact exists"}},
        {"id": "I3", "name": "Confidence Requires Verification",
         "shortDescription": {"text": "High confidence requires verification artifacts"}},
        {"id": "I4", "name": "Traceability Is Mandatory",
         "shortDescription": {"text": "Every decision must be traceable through REQ → CTRL → TEST → EVID → DECISION"}},
        {"id": "I5", "name": "Safety Over Fluency",
         "shortDescription": {"text": "Bounded statements preferred over fluent-but-wrong"}},
        {"id": "I6", "name": "Fail Closed",
         "shortDescription": {"text": "Stop and surface failures; do not work around"}},
        {"id": "SYSTEM", "name": "System Error",
         "shortDescription": {"text": "Validator system error"}}
    ]
    
    sarif = {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "PROACTIVE Constitutional Validator",
                    "version": report.get("validator_version", "1.0.0"),
                    "informationUri": "https://github.com/proactive-toolkit",
                    "rules": rules
                }
            },
            "results": [
                {
                    "ruleId": v["invariant"],
                    "level": "error" if v["severity"] == "ERROR" else ("warning" if v["severity"] == "WARNING" else "note"),
                    "message": {"text": v["message"]},
                    "locations": [{
                        "physicalLocation": {
                            "artifactLocation": {"uri": v["location"]["file"]},
                            "region": {"startLine": v["location"].get("line", 1)}
                        }
                    }]
                }
                for v in report["violations"]
            ]
        }]
    }
    return sarif


def print_text_report(report: Dict[str, Any]) -> None:
    """Print human-readable report to stdout."""
    summary = report["summary"]
    
    print("\n" + "=" * 60)
    print("PROACTIVE Constitutional Validator Report")
    print("=" * 60)
    print(f"\nReport ID: {report['report_id']}")
    print(f"Timestamp: {report['timestamp']}")
    print(f"\nGate Result: {summary['gate_result']}")
    if summary.get('gate_reason'):
        print(f"Gate Reason: {summary['gate_reason']}")
    print(f"\nFiles Scanned: {summary['total_files_scanned']}")
    print(f"Files with Violations: {summary.get('files_with_violations', 'N/A')}")
    print(f"Total Violations: {summary['total_violations']}")
    print(f"  Errors: {summary['errors']}")
    print(f"  Warnings: {summary['warnings']}")
    
    if summary.get("by_invariant"):
        print("\nBy Invariant:")
        for inv, count in sorted(summary["by_invariant"].items()):
            print(f"  {inv}: {count}")
    
    if report["violations"]:
        print("\n" + "-" * 60)
        print("Violations:")
        print("-" * 60)
        for v in report["violations"][:20]:  # Show first 20
            print(f"\n[{v['severity']}] {v['invariant']}: {v['message']}")
            loc = v["location"]
            line_info = f":{loc.get('line', '?')}" if 'line' in loc else ""
            print(f"  File: {loc['file']}{line_info}")
            if v.get("suggested_fix"):
                print(f"  Fix: {v['suggested_fix']}")
        
        if len(report["violations"]) > 20:
            print(f"\n... and {len(report['violations']) - 20} more violations")
    
    print("\n" + "=" * 60)


def main(directory: str = ".", output_format: str = "json", config_path: str = "validator_config.yaml") -> int:
    """Main entry point for CLI usage.
    
    Args:
        directory: Directory to validate
        output_format: Output format (json, sarif, text)
        config_path: Path to validator config
        
    Returns:
        Exit code (0 = pass, 1 = violations found)
    """
    start_time = time.time()
    
    # Reset and load config
    reset_config()
    load_config(config_path)
    
    # Get git context if available
    git_context: Dict[str, Any] = {}
    try:
        import subprocess
        git_context["commit_sha"] = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL
        ).decode().strip()
        git_context["branch"] = subprocess.check_output(
            ["git", "branch", "--show-current"], stderr=subprocess.DEVNULL
        ).decode().strip()
        git_context["repository"] = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        pass
    
    # Validate
    results = validate_directory(directory)
    report = generate_report(results, git_context, config_path)
    
    # Add execution time
    report["summary"]["execution_time_ms"] = int((time.time() - start_time) * 1000)
    
    # Output
    if output_format == "sarif":
        sarif = generate_sarif(report)
        print(json.dumps(sarif, indent=2))
    elif output_format == "text":
        print_text_report(report)
    else:
        print(json.dumps(report, indent=2))
    
    # Return exit code based on gate result
    return 0 if report["summary"]["gate_result"] == "PASS" else 1


if __name__ == "__main__":
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(
        description="PROACTIVE Constitutional Validator - Validates model outputs against I1-I6 invariants"
    )
    parser.add_argument("directory", nargs="?", default=".", 
                        help="Directory or file to validate (default: current directory)")
    parser.add_argument("--format", "-f", choices=["json", "sarif", "text"], default="text",
                        help="Output format (default: text)")
    parser.add_argument("--config", "-c", default="validator_config.yaml",
                        help="Path to validator config (default: validator_config.yaml)")
    
    args = parser.parse_args()
    
    exit_code = main(args.directory, args.format, args.config)
    sys.exit(exit_code)
