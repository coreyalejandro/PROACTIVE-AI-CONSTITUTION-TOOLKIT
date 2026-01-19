# Task Backlog: Adapter 04 - Safety Case Generator

## Adapter Overview

**Purpose**: Ingests adapter outputs, generates safety case draft with human review gates  
**Validates**: End-to-end framework integration  
**Success Metric**: Generated case contains all required claims, arguments, evidence links  
**Repository Path**: `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/`

**⚠️ CRITICAL**: Output is **DRAFT** with `[HUMAN_REVIEW_REQUIRED]` gates, NOT final case

---

## Prerequisites

| Prerequisite | Status | Workaround |
|--------------|--------|------------|
| PROACTIVE_AI_CONSTITUTION.md | EXISTS ✓ | None needed |
| Adapter 01-03 outputs | Required | Can use mock data for testing |
| Safety case template | Created in T1 | None needed |
| Python 3.9+ | Required | Local environment |

---

## A04-T1: Define Safety Case Schema

**Tier**: 2 (YELLOW)  
**Duration**: 45-60 minutes  
**Dependencies**: PROACTIVE_AI_CONSTITUTION.md, 09_SAFETY_CASE/

### Inputs

- `01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md`
- Goal Structuring Notation (GSN) documentation
- Existing `09_SAFETY_CASE/SAFETY_CASE_SKELETON.md` (if exists)

### Outputs

- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/safety_case_schema.json`
- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/templates/safety_case_template.md`
- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/gsn_elements.yaml`

### Instructions

1. Create output directories:

```bash
mkdir -p ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/templates
```

2. Create `safety_case_schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PROACTIVE Safety Case Schema",
  "description": "Schema for generated safety case drafts with human review gates",
  "type": "object",
  "required": ["metadata", "top_goal", "argument_strands", "evidence_registry"],
  "properties": {
    "metadata": {
      "type": "object",
      "required": ["version", "generated_at", "generator_version", "status"],
      "properties": {
        "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
        "generated_at": { "type": "string", "format": "date-time" },
        "generator_version": { "type": "string" },
        "status": { 
          "type": "string",
          "enum": ["DRAFT", "REVIEW_IN_PROGRESS", "APPROVED", "REJECTED"],
          "default": "DRAFT"
        },
        "review_gates_remaining": { "type": "integer", "minimum": 0 }
      }
    },
    "top_goal": {
      "type": "object",
      "required": ["id", "text", "confidence"],
      "properties": {
        "id": { "type": "string", "pattern": "^G\\d+$" },
        "text": { "type": "string" },
        "confidence": { 
          "type": "string",
          "enum": ["HIGH", "MEDIUM", "LOW", "UNVALIDATED"]
        },
        "human_review": {
          "type": "object",
          "properties": {
            "required": { "type": "boolean", "default": true },
            "status": { "type": "string", "enum": ["PENDING", "APPROVED", "REJECTED"] },
            "reviewer": { "type": ["string", "null"] },
            "review_date": { "type": ["string", "null"], "format": "date-time" },
            "notes": { "type": ["string", "null"] }
          }
        }
      }
    },
    "argument_strands": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["strand_id", "principle", "sub_goal", "strategy", "evidence_refs"],
        "properties": {
          "strand_id": { "type": "string", "pattern": "^STRAND-[A-Z]$" },
          "principle": { 
            "type": "string",
            "enum": ["P", "R", "O", "A", "C", "T", "I", "V", "E"]
          },
          "sub_goal": {
            "type": "object",
            "properties": {
              "id": { "type": "string" },
              "text": { "type": "string" },
              "confidence": { "type": "string" }
            }
          },
          "strategy": {
            "type": "object",
            "properties": {
              "id": { "type": "string" },
              "text": { "type": "string" },
              "method": { "type": "string" }
            }
          },
          "evidence_refs": {
            "type": "array",
            "items": { "type": "string", "pattern": "^E-[A-Z]\\d+$" }
          },
          "claims": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "claim_text": { "type": "string" },
                "confidence": { "type": "string" },
                "supported_by": { "type": "array", "items": { "type": "string" } },
                "human_review_required": { "type": "boolean", "default": true }
              }
            }
          },
          "gaps": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Identified gaps in the argument strand"
          }
        }
      }
    },
    "evidence_registry": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "description", "source", "status"],
        "properties": {
          "id": { "type": "string", "pattern": "^E-[A-Z]\\d+$" },
          "description": { "type": "string" },
          "source": { 
            "type": "string",
            "description": "Path or URL to evidence artifact"
          },
          "source_adapter": {
            "type": "string",
            "enum": ["01_WANDB_TRACE", "02_CI_SAFETY_GATE", "03_HELM_PROFILE", "MANUAL"]
          },
          "status": {
            "type": "string",
            "enum": ["PENDING", "COMPLETE_PILOT", "COMPLETE_FULL", "REJECTED"]
          },
          "metrics": {
            "type": "object",
            "description": "Key metrics from the evidence"
          },
          "human_review": {
            "type": "object",
            "properties": {
              "required": { "type": "boolean" },
              "status": { "type": "string" },
              "notes": { "type": ["string", "null"] }
            }
          }
        }
      }
    },
    "trace_chains": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "principle": { "type": "string" },
          "adapter": { "type": "string" },
          "evidence_id": { "type": "string" },
          "claim": { "type": "string" },
          "strand": { "type": "string" }
        }
      },
      "description": "Principle → Adapter → Evidence → Claim trace chains"
    },
    "human_review_summary": {
      "type": "object",
      "properties": {
        "total_gates": { "type": "integer" },
        "gates_pending": { "type": "integer" },
        "gates_approved": { "type": "integer" },
        "gates_rejected": { "type": "integer" },
        "critical_gates": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    }
  }
}
```

3. Create `gsn_elements.yaml`:

```yaml
# Goal Structuring Notation Elements for PROACTIVE Safety Cases

gsn_elements:
  goal:
    prefix: "G"
    description: "What is claimed to be true"
    symbol: "rectangle"
    required_fields:
      - id
      - text
      - confidence
    human_review: required

  strategy:
    prefix: "S"
    description: "How the goal is argued"
    symbol: "parallelogram"
    required_fields:
      - id
      - text
      - method

  evidence:
    prefix: "E"
    description: "Supporting data or artifact"
    symbol: "circle"
    required_fields:
      - id
      - description
      - source
      - status
    human_review: required

  context:
    prefix: "C"
    description: "Contextual information"
    symbol: "rounded_rectangle"
    required_fields:
      - id
      - text

  assumption:
    prefix: "A"
    description: "Assumed to be true"
    symbol: "oval"
    required_fields:
      - id
      - text
    human_review: required

  justification:
    prefix: "J"
    description: "Rationale for approach"
    symbol: "oval_dashed"
    required_fields:
      - id
      - text

# PROACTIVE-specific mappings
proactive_mappings:
  principles_to_strands:
    P: "STRAND-P"  # Privacy-First
    R: "STRAND-R"  # Reality-Bound
    O: "STRAND-O"  # Observability
    A: "STRAND-A"  # Accessibility
    C: "STRAND-C"  # Constitutional Constraints
    T: "STRAND-T"  # Truth or Bounded Unknown
    I: "STRAND-I"  # Intent Integrity
    V: "STRAND-V"  # Verification Before Action
    E: "STRAND-E"  # Error Ownership

  adapters_to_evidence:
    "01_WANDB_TRACE_ADAPTER":
      primary_principle: "O"
      evidence_prefix: "E-O"
    "02_CI_SAFETY_GATE":
      primary_principle: "V"
      evidence_prefix: "E-V"
    "03_HELM_SAFETY_PROFILE":
      primary_principle: "T"
      evidence_prefix: "E-T"
    "04_SAFETY_CASE_GENERATOR":
      primary_principle: "C"
      evidence_prefix: "E-C"

# Human review gate requirements
review_gates:
  critical:
    - "Top-level goal confidence assignment"
    - "Evidence sufficiency determination"
    - "Gap closure decisions"
  standard:
    - "Claim-evidence mapping accuracy"
    - "Metric threshold satisfaction"
  informational:
    - "Trace chain completeness"
    - "Documentation formatting"
```

4. Create `templates/safety_case_template.md`:

```markdown
# PROACTIVE Safety Case

## ⚠️ DRAFT - REQUIRES HUMAN REVIEW

**Status**: DRAFT  
**Generated**: {{generated_at}}  
**Generator Version**: {{generator_version}}  
**Review Gates Remaining**: {{review_gates_remaining}}

---

## Executive Summary

[HUMAN_REVIEW_REQUIRED: Verify executive summary accurately represents the safety case]

{{executive_summary}}

---

## Top-Level Goal

### G1: {{top_goal_text}}

**Confidence**: {{top_goal_confidence}}

[HUMAN_REVIEW_REQUIRED: Confirm this goal accurately captures the safety claim]

---

## Argument Strands

{{#each argument_strands}}

### {{strand_id}}: {{principle_name}}

**Sub-Goal**: {{sub_goal.text}}  
**Confidence**: {{sub_goal.confidence}}

**Strategy**: {{strategy.text}}

#### Claims

{{#each claims}}
- **{{claim_text}}**
  - Confidence: {{confidence}}
  - Supported by: {{#each supported_by}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}
  {{#if human_review_required}}
  - [HUMAN_REVIEW_REQUIRED]
  {{/if}}
{{/each}}

#### Evidence

{{#each evidence_refs}}
- {{this}}: See Evidence Registry
{{/each}}

#### Gaps

{{#if gaps}}
{{#each gaps}}
- [ ] {{this}}
{{/each}}
{{else}}
*No gaps identified*
{{/if}}

---

{{/each}}

## Evidence Registry

| ID | Description | Source | Adapter | Status | Review |
|----|-------------|--------|---------|--------|--------|
{{#each evidence_registry}}
| {{id}} | {{description}} | {{source}} | {{source_adapter}} | {{status}} | {{#if human_review.required}}[REVIEW]{{else}}—{{/if}} |
{{/each}}

---

## Trace Chains

```
{{#each trace_chains}}
Principle {{principle}}
    │
    ▼
{{adapter}}
    │
    ▼
Evidence {{evidence_id}}
    │
    ▼
Claim: "{{claim}}"
    │
    ▼
Safety Case {{strand}}

{{/each}}
```

---

## Human Review Summary

| Category | Count |
|----------|-------|
| Total Gates | {{human_review_summary.total_gates}} |
| Pending | {{human_review_summary.gates_pending}} |
| Approved | {{human_review_summary.gates_approved}} |
| Rejected | {{human_review_summary.gates_rejected}} |

### Critical Review Gates

{{#each human_review_summary.critical_gates}}
- [ ] {{this}}
{{/each}}

---

## Approval Workflow

1. **Technical Review**: All evidence artifacts verified
2. **Claim Review**: All [HUMAN_REVIEW_REQUIRED] gates addressed
3. **Gap Assessment**: All gaps either closed or documented as limitations
4. **Final Approval**: Safety case status changed to APPROVED

---

*This document was automatically generated and requires human review before it can be considered an approved safety case.*

**DO NOT** treat this as a final safety case until all review gates are cleared.
```

### Acceptance Criteria

- [ ] `safety_case_schema.json` exists and is valid JSON Schema
- [ ] `gsn_elements.yaml` maps all PROACTIVE principles to strands
- [ ] Template includes `[HUMAN_REVIEW_REQUIRED]` gates
- [ ] Schema requires DRAFT status for generated cases
- [ ] Trace chain structure defined

---

## A04-T2: Create Adapter Directory Structure

**Tier**: 1 (RED)  
**Duration**: 15-20 minutes  
**Dependencies**: A04-T1 complete

### Outputs

- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/__init__.py`
- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/generator.py` (stub)
- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/evidence_collector.py` (stub)
- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/README.md`
- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/USE_CASE_EVIDENCE.md` (stub)

### Instructions

1. Create `__init__.py`:

```python
"""PROACTIVE Safety Case Generator

Ingests adapter outputs and generates safety case drafts with human review gates.

Validates: End-to-end framework integration
Success Metric: Generated case contains all required claims, arguments, evidence links

⚠️ CRITICAL: Output is DRAFT with [HUMAN_REVIEW_REQUIRED] gates, NOT final case
"""

__version__ = "0.1.0"
__author__ = "PROACTIVE Research Toolkit"

from .generator import generate_safety_case, validate_case
from .evidence_collector import collect_evidence, load_adapter_outputs
```

2. Create `generator.py` (stub):

```python
"""
PROACTIVE Safety Case Generator
Generates safety case drafts from adapter outputs

Status: STUB - Implementation in A04-T3

⚠️ CRITICAL: Output is DRAFT with [HUMAN_REVIEW_REQUIRED] gates, NOT final case
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ReviewGate:
    """Human review gate in the safety case."""
    gate_id: str
    description: str
    category: str  # "critical", "standard", "informational"
    status: str = "PENDING"  # "PENDING", "APPROVED", "REJECTED"
    reviewer: Optional[str] = None
    review_date: Optional[str] = None
    notes: Optional[str] = None


@dataclass
class SafetyCaseDraft:
    """Generated safety case draft."""
    metadata: Dict[str, Any]
    top_goal: Dict[str, Any]
    argument_strands: List[Dict[str, Any]]
    evidence_registry: List[Dict[str, Any]]
    trace_chains: List[Dict[str, Any]]
    review_gates: List[ReviewGate]
    
    @property
    def is_approved(self) -> bool:
        """Check if all critical gates are approved."""
        critical_gates = [g for g in self.review_gates if g.category == "critical"]
        return all(g.status == "APPROVED" for g in critical_gates)
    
    @property
    def pending_gates(self) -> int:
        """Count of pending review gates."""
        return sum(1 for g in self.review_gates if g.status == "PENDING")


def load_schema(schema_path: str = "safety_case_schema.json") -> Dict[str, Any]:
    """Load safety case schema."""
    raise NotImplementedError("Implement in A04-T3")


def load_gsn_config(config_path: str = "gsn_elements.yaml") -> Dict[str, Any]:
    """Load GSN element configuration."""
    raise NotImplementedError("Implement in A04-T3")


def create_argument_strand(
    principle: str,
    evidence_items: List[Dict[str, Any]],
    gsn_config: Dict[str, Any]
) -> Dict[str, Any]:
    """Create argument strand for a PROACTIVE principle."""
    raise NotImplementedError("Implement in A04-T3")


def create_trace_chain(
    principle: str,
    adapter: str,
    evidence_id: str,
    claim: str
) -> Dict[str, Any]:
    """Create trace chain linking principle to claim."""
    raise NotImplementedError("Implement in A04-T3")


def identify_gaps(
    strand: Dict[str, Any],
    required_evidence: List[str]
) -> List[str]:
    """Identify gaps in an argument strand."""
    raise NotImplementedError("Implement in A04-T3")


def generate_review_gates(
    case: SafetyCaseDraft,
    gsn_config: Dict[str, Any]
) -> List[ReviewGate]:
    """Generate human review gates for the case."""
    raise NotImplementedError("Implement in A04-T3")


def generate_safety_case(
    evidence_inputs: Dict[str, Any],
    output_path: Optional[str] = None
) -> SafetyCaseDraft:
    """Generate safety case draft from collected evidence.
    
    ⚠️ Output is DRAFT requiring human review, NOT approved case.
    
    Args:
        evidence_inputs: Collected evidence from adapters
        output_path: Optional path to save generated case
        
    Returns:
        SafetyCaseDraft with [HUMAN_REVIEW_REQUIRED] gates
    """
    raise NotImplementedError("Implement in A04-T3")


def render_markdown(case: SafetyCaseDraft, template_path: str) -> str:
    """Render safety case to markdown using template."""
    raise NotImplementedError("Implement in A04-T3")


def validate_case(case: SafetyCaseDraft) -> List[str]:
    """Validate safety case against schema.
    
    Returns list of validation errors.
    """
    raise NotImplementedError("Implement in A04-T3")


if __name__ == "__main__":
    print("Safety Case Generator - STUB")
    print("Run A04-T3 to implement")
    print()
    print("⚠️ CRITICAL: Output is DRAFT, NOT final safety case")
```

3. Create `evidence_collector.py` (stub):

```python
"""
Evidence Collector for Safety Case Generator
Collects outputs from Adapters 01-03 for case generation

Status: STUB - Implementation in A04-T3
"""

from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass


@dataclass
class EvidenceItem:
    """Single piece of evidence from an adapter."""
    id: str
    description: str
    source_adapter: str
    source_path: str
    metrics: Dict[str, Any]
    status: str


def discover_adapter_outputs(workspace: str) -> Dict[str, List[str]]:
    """Discover USE_CASE_EVIDENCE.md files from adapters."""
    raise NotImplementedError("Implement in A04-T3")


def parse_evidence_file(file_path: str) -> EvidenceItem:
    """Parse USE_CASE_EVIDENCE.md to extract evidence."""
    raise NotImplementedError("Implement in A04-T3")


def load_adapter_outputs(
    adapter_paths: Dict[str, str]
) -> Dict[str, List[EvidenceItem]]:
    """Load outputs from all adapters.
    
    Args:
        adapter_paths: Map of adapter name to path
        
    Returns:
        Map of principle to evidence items
    """
    raise NotImplementedError("Implement in A04-T3")


def collect_evidence(workspace: str = ".") -> Dict[str, Any]:
    """Collect all evidence from workspace.
    
    Scans ADAPTER_MODULES/ for USE_CASE_EVIDENCE.md files
    and extracts relevant metrics and claims.
    """
    raise NotImplementedError("Implement in A04-T3")


def validate_evidence(evidence: Dict[str, Any]) -> List[str]:
    """Validate collected evidence has required fields.
    
    Returns list of validation errors.
    """
    raise NotImplementedError("Implement in A04-T3")


if __name__ == "__main__":
    print("Evidence Collector - STUB")
    print("Run A04-T3 to implement")
```

4. Create `README.md`:

```markdown
# Safety Case Generator

Ingests adapter outputs and generates safety case drafts with human review gates.

## Status: IN DEVELOPMENT

Current version: 0.1.0 (STUB)

## ⚠️ CRITICAL WARNING

**Output is DRAFT with `[HUMAN_REVIEW_REQUIRED]` gates, NOT a final safety case.**

The generated safety case must go through human review before it can be considered
approved. Do NOT treat generated output as an approved safety case.

## Purpose

This adapter validates **end-to-end framework integration** by:
- Collecting evidence from Adapters 01-03
- Generating structured safety case arguments
- Creating trace chains from principles to evidence
- Inserting human review gates at critical decision points

## Success Metric

Generated case contains **all required claims, arguments, and evidence links**
with appropriate `[HUMAN_REVIEW_REQUIRED]` gates.

## Installation

```bash
pip install pyyaml jinja2 jsonschema
```

## Usage

```python
from generator import generate_safety_case
from evidence_collector import collect_evidence

# Collect evidence from adapters
evidence = collect_evidence("./ADAPTER_MODULES")

# Generate draft safety case
draft = generate_safety_case(evidence, output_path="SAFETY_CASE_DRAFT.md")

# Check review gates
print(f"Pending review gates: {draft.pending_gates}")
print(f"Is approved: {draft.is_approved}")  # Always False for new drafts
```

## Output Structure

```
SAFETY_CASE_DRAFT.md
├── Executive Summary [HUMAN_REVIEW_REQUIRED]
├── Top-Level Goal [HUMAN_REVIEW_REQUIRED]
├── Argument Strands
│   ├── STRAND-O: Observability
│   ├── STRAND-V: Verification
│   └── STRAND-T: Truth
├── Evidence Registry
├── Trace Chains
└── Human Review Summary
```

## Review Gates

| Category | Description | Examples |
|----------|-------------|----------|
| Critical | Must be reviewed before approval | Goal confidence, evidence sufficiency |
| Standard | Should be reviewed | Claim-evidence mapping |
| Informational | Review optional | Formatting, completeness |

## Links

- [PROACTIVE Constitution](../../01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md)
- [Safety Case Skeleton](../../09_SAFETY_CASE/SAFETY_CASE_SKELETON.md)
- [GSN Documentation](https://www.goalstructuringnotation.info/)
```

5. Create `USE_CASE_EVIDENCE.md` (stub):

```markdown
# Use Case Evidence: Safety Case Generator

## Status: AWAITING VALIDATION (A04-T5)

## Executive Summary

[2-3 sentences: What did we test? What did we find?]

## Validation Approach

- **Type**: Integration test
- **Input**: Mock adapter outputs from Adapters 01-03
- **Success Criteria**: Generated case has all required elements and review gates

## Key Finding

[The main result in plain English]

## Completeness Checklist

| Element | Required | Present | Review Gate |
|---------|----------|---------|-------------|
| Top-level goal | ✓ | [Y/N] | [Y/N] |
| Strand O | ✓ | [Y/N] | [Y/N] |
| Strand V | ✓ | [Y/N] | [Y/N] |
| Strand T | ✓ | [Y/N] | [Y/N] |
| Evidence registry | ✓ | [Y/N] | — |
| Trace chains | ✓ | [Y/N] | — |
| Human review summary | ✓ | [Y/N] | — |

## Limitations

[Honest scope statement]

## Implications for Safety Case

This demonstrates end-to-end framework integration.

## Artifacts

- Generated draft: `SAFETY_CASE_DRAFT.md`
- Generator code: `generator.py`
- Schema: `safety_case_schema.json`
```

### Acceptance Criteria

- [ ] All 5 files exist in `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/`
- [ ] README prominently displays DRAFT warning
- [ ] `[HUMAN_REVIEW_REQUIRED]` concept documented
- [ ] GSN element references included

---

## A04-T3: Implement Generator Core Logic

**Tier**: 3 (GREEN)  
**Duration**: 90-120 minutes  
**Dependencies**: A04-T2 complete

### Outputs

- `generator.py` (complete)
- `evidence_collector.py` (complete)
- Test run generating draft from mock data

### Instructions

1. Install dependencies:

```bash
pip install pyyaml jinja2 jsonschema
```

2. Implement `evidence_collector.py`:

```python
"""
Evidence Collector for Safety Case Generator
Version: 1.0.0
"""

import json
import re
from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass, asdict


@dataclass
class EvidenceItem:
    """Single piece of evidence from an adapter."""
    id: str
    description: str
    source_adapter: str
    source_path: str
    metrics: Dict[str, Any]
    status: str
    confidence: str = "MEDIUM"
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# Adapter to principle mapping
ADAPTER_PRINCIPLES = {
    "01_WANDB_TRACE_ADAPTER": "O",
    "02_CI_SAFETY_GATE": "V", 
    "03_HELM_SAFETY_PROFILE": "T"
}

EVIDENCE_PREFIXES = {
    "O": "E-O",
    "V": "E-V",
    "T": "E-T"
}


def discover_adapter_outputs(workspace: str) -> Dict[str, List[str]]:
    """Discover USE_CASE_EVIDENCE.md files from adapters."""
    root = Path(workspace)
    adapter_dir = root / "ADAPTER_MODULES"
    
    outputs = {}
    
    if not adapter_dir.exists():
        return outputs
    
    for adapter_path in adapter_dir.iterdir():
        if adapter_path.is_dir() and adapter_path.name.startswith("0"):
            evidence_file = adapter_path / "USE_CASE_EVIDENCE.md"
            if evidence_file.exists():
                outputs[adapter_path.name] = [str(evidence_file)]
    
    return outputs


def parse_evidence_file(file_path: str, adapter_name: str) -> Optional[EvidenceItem]:
    """Parse USE_CASE_EVIDENCE.md to extract evidence."""
    path = Path(file_path)
    if not path.exists():
        return None
    
    content = path.read_text()
    
    # Extract status
    status_match = re.search(r'##\s*Status:\s*(\w+)', content)
    status = status_match.group(1) if status_match else "PENDING"
    
    # Extract key finding
    finding_match = re.search(r'##\s*Key Finding\s*\n+(.+?)(?=\n#|\n\n#|\Z)', content, re.DOTALL)
    description = finding_match.group(1).strip()[:200] if finding_match else "Evidence pending"
    
    # Extract metrics (look for tables)
    metrics = {}
    metric_pattern = r'\|\s*(\w[\w\s]*\w)\s*\|\s*([\d.%]+)\s*\|'
    for match in re.finditer(metric_pattern, content):
        key = match.group(1).strip().lower().replace(' ', '_')
        value = match.group(2).strip()
        metrics[key] = value
    
    # Determine principle
    principle = ADAPTER_PRINCIPLES.get(adapter_name, "C")
    prefix = EVIDENCE_PREFIXES.get(principle, "E-X")
    evidence_id = f"{prefix}1"
    
    # Determine confidence from status
    confidence_map = {
        "PILOT": "MEDIUM",
        "COMPLETE": "HIGH",
        "AWAITING": "LOW",
        "PENDING": "LOW"
    }
    confidence = "MEDIUM"
    for key, conf in confidence_map.items():
        if key in status.upper():
            confidence = conf
            break
    
    return EvidenceItem(
        id=evidence_id,
        description=description,
        source_adapter=adapter_name,
        source_path=str(path),
        metrics=metrics,
        status=status,
        confidence=confidence
    )


def load_adapter_outputs(adapter_paths: Dict[str, str]) -> Dict[str, List[EvidenceItem]]:
    """Load outputs from all adapters."""
    evidence_by_principle = {}
    
    for adapter_name, path in adapter_paths.items():
        evidence = parse_evidence_file(path, adapter_name)
        if evidence:
            principle = ADAPTER_PRINCIPLES.get(adapter_name, "C")
            if principle not in evidence_by_principle:
                evidence_by_principle[principle] = []
            evidence_by_principle[principle].append(evidence)
    
    return evidence_by_principle


def collect_evidence(workspace: str = ".") -> Dict[str, Any]:
    """Collect all evidence from workspace."""
    discovered = discover_adapter_outputs(workspace)
    
    # Flatten to path map
    adapter_paths = {}
    for adapter_name, paths in discovered.items():
        if paths:
            adapter_paths[adapter_name] = paths[0]
    
    evidence_by_principle = load_adapter_outputs(adapter_paths)
    
    # Convert to serializable format
    result = {
        "principles": {},
        "all_evidence": []
    }
    
    for principle, items in evidence_by_principle.items():
        result["principles"][principle] = [e.to_dict() for e in items]
        result["all_evidence"].extend([e.to_dict() for e in items])
    
    return result


def validate_evidence(evidence: Dict[str, Any]) -> List[str]:
    """Validate collected evidence has required fields."""
    errors = []
    
    if not evidence.get("all_evidence"):
        errors.append("No evidence items found")
    
    required_fields = ["id", "description", "source_adapter", "status"]
    
    for item in evidence.get("all_evidence", []):
        for field in required_fields:
            if not item.get(field):
                errors.append(f"Evidence {item.get('id', 'UNKNOWN')}: missing {field}")
    
    return errors


if __name__ == "__main__":
    evidence = collect_evidence(".")
    print(json.dumps(evidence, indent=2))
```

3. Implement `generator.py`:

```python
"""
PROACTIVE Safety Case Generator
Version: 1.0.0

⚠️ CRITICAL: Output is DRAFT with [HUMAN_REVIEW_REQUIRED] gates, NOT final case
"""

import json
import yaml
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field, asdict
from pathlib import Path

from .evidence_collector import collect_evidence, EvidenceItem


@dataclass
class ReviewGate:
    """Human review gate in the safety case."""
    gate_id: str
    description: str
    category: str
    status: str = "PENDING"
    reviewer: Optional[str] = None
    review_date: Optional[str] = None
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class SafetyCaseDraft:
    """Generated safety case draft."""
    metadata: Dict[str, Any]
    top_goal: Dict[str, Any]
    argument_strands: List[Dict[str, Any]]
    evidence_registry: List[Dict[str, Any]]
    trace_chains: List[Dict[str, Any]]
    review_gates: List[ReviewGate]
    
    @property
    def is_approved(self) -> bool:
        critical_gates = [g for g in self.review_gates if g.category == "critical"]
        return all(g.status == "APPROVED" for g in critical_gates)
    
    @property
    def pending_gates(self) -> int:
        return sum(1 for g in self.review_gates if g.status == "PENDING")
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "metadata": self.metadata,
            "top_goal": self.top_goal,
            "argument_strands": self.argument_strands,
            "evidence_registry": self.evidence_registry,
            "trace_chains": self.trace_chains,
            "human_review_summary": {
                "total_gates": len(self.review_gates),
                "gates_pending": self.pending_gates,
                "gates_approved": sum(1 for g in self.review_gates if g.status == "APPROVED"),
                "gates_rejected": sum(1 for g in self.review_gates if g.status == "REJECTED"),
                "critical_gates": [g.description for g in self.review_gates if g.category == "critical"]
            }
        }


# Principle descriptions
PRINCIPLE_INFO = {
    "O": {"name": "Observability", "sub_goal": "Trace chain enables meaningful auditability"},
    "V": {"name": "Verification", "sub_goal": "System verifies claims before output"},
    "T": {"name": "Truth", "sub_goal": "System bounds unknowns and avoids false claims"},
    "P": {"name": "Privacy-First", "sub_goal": "System minimizes data collection"},
    "R": {"name": "Reality-Bound", "sub_goal": "System separates facts from inference"},
    "A": {"name": "Accessibility", "sub_goal": "System minimizes cognitive load"},
    "C": {"name": "Constitutional Constraints", "sub_goal": "System enforces behavioral rules"},
    "I": {"name": "Intent Integrity", "sub_goal": "System preserves user intent"},
    "E": {"name": "Error Ownership", "sub_goal": "System owns and repairs mistakes"}
}


def load_schema(schema_path: str = "safety_case_schema.json") -> Dict[str, Any]:
    """Load safety case schema."""
    path = Path(__file__).parent / schema_path
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def load_gsn_config(config_path: str = "gsn_elements.yaml") -> Dict[str, Any]:
    """Load GSN element configuration."""
    path = Path(__file__).parent / config_path
    if path.exists():
        with open(path) as f:
            return yaml.safe_load(f)
    return {}


def create_argument_strand(
    principle: str,
    evidence_items: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Create argument strand for a PROACTIVE principle."""
    info = PRINCIPLE_INFO.get(principle, {"name": principle, "sub_goal": "TBD"})
    
    # Create claims from evidence
    claims = []
    for ev in evidence_items:
        claim_text = f"Evidence {ev['id']} demonstrates {info['sub_goal'].lower()}"
        claims.append({
            "claim_text": claim_text,
            "confidence": ev.get("confidence", "MEDIUM"),
            "supported_by": [ev["id"]],
            "human_review_required": True
        })
    
    # Identify gaps
    gaps = []
    if not evidence_items:
        gaps.append(f"No evidence collected for Principle {principle}")
    elif all(e.get("status", "").upper() in ["PENDING", "AWAITING"] for e in evidence_items):
        gaps.append("All evidence is pending validation")
    
    return {
        "strand_id": f"STRAND-{principle}",
        "principle": principle,
        "principle_name": info["name"],
        "sub_goal": {
            "id": f"G1.{principle}",
            "text": info["sub_goal"],
            "confidence": "MEDIUM" if evidence_items else "LOW"
        },
        "strategy": {
            "id": f"S-{principle}1",
            "text": f"Demonstrate via adapter evaluation",
            "method": "empirical validation"
        },
        "evidence_refs": [e["id"] for e in evidence_items],
        "claims": claims,
        "gaps": gaps
    }


def create_trace_chain(
    principle: str,
    adapter: str,
    evidence_id: str,
    claim: str
) -> Dict[str, Any]:
    """Create trace chain linking principle to claim."""
    return {
        "principle": principle,
        "adapter": adapter,
        "evidence_id": evidence_id,
        "claim": claim,
        "strand": f"STRAND-{principle}"
    }


def generate_review_gates(
    strands: List[Dict[str, Any]],
    evidence: List[Dict[str, Any]]
) -> List[ReviewGate]:
    """Generate human review gates for the case."""
    gates = []
    gate_counter = 1
    
    # Critical gate: top goal
    gates.append(ReviewGate(
        gate_id=f"RG-{gate_counter:03d}",
        description="Top-level goal confidence assignment",
        category="critical"
    ))
    gate_counter += 1
    
    # Critical gate per strand
    for strand in strands:
        gates.append(ReviewGate(
            gate_id=f"RG-{gate_counter:03d}",
            description=f"Evidence sufficiency for {strand['strand_id']}",
            category="critical"
        ))
        gate_counter += 1
    
    # Standard gates for each claim
    for strand in strands:
        for claim in strand.get("claims", []):
            if claim.get("human_review_required"):
                gates.append(ReviewGate(
                    gate_id=f"RG-{gate_counter:03d}",
                    description=f"Claim-evidence mapping: {claim['claim_text'][:50]}...",
                    category="standard"
                ))
                gate_counter += 1
    
    return gates


def generate_safety_case(
    evidence_inputs: Optional[Dict[str, Any]] = None,
    workspace: str = ".",
    output_path: Optional[str] = None
) -> SafetyCaseDraft:
    """Generate safety case draft from collected evidence.
    
    ⚠️ Output is DRAFT requiring human review, NOT approved case.
    """
    # Collect evidence if not provided
    if evidence_inputs is None:
        evidence_inputs = collect_evidence(workspace)
    
    # Build evidence registry
    evidence_registry = []
    for item in evidence_inputs.get("all_evidence", []):
        evidence_registry.append({
            "id": item["id"],
            "description": item["description"],
            "source": item["source_path"],
            "source_adapter": item["source_adapter"],
            "status": item["status"],
            "metrics": item.get("metrics", {}),
            "human_review": {
                "required": True,
                "status": "PENDING",
                "notes": None
            }
        })
    
    # Build argument strands
    strands = []
    trace_chains = []
    
    for principle, items in evidence_inputs.get("principles", {}).items():
        strand = create_argument_strand(principle, items)
        strands.append(strand)
        
        # Create trace chains
        for item in items:
            chain = create_trace_chain(
                principle=principle,
                adapter=item["source_adapter"],
                evidence_id=item["id"],
                claim=strand["claims"][0]["claim_text"] if strand["claims"] else "TBD"
            )
            trace_chains.append(chain)
    
    # Generate review gates
    review_gates = generate_review_gates(strands, evidence_registry)
    
    # Build metadata
    metadata = {
        "version": "0.1.0",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "generator_version": "1.0.0",
        "status": "DRAFT",  # Always DRAFT for generated cases
        "review_gates_remaining": len(review_gates)
    }
    
    # Build top goal
    # Confidence based on evidence coverage
    covered_principles = len(evidence_inputs.get("principles", {}))
    if covered_principles >= 3:
        top_confidence = "MEDIUM"
    elif covered_principles >= 1:
        top_confidence = "LOW"
    else:
        top_confidence = "UNVALIDATED"
    
    top_goal = {
        "id": "G1",
        "text": "PROACTIVE COL reduces epistemic reliability failures in AI systems",
        "confidence": top_confidence,
        "human_review": {
            "required": True,
            "status": "PENDING",
            "reviewer": None,
            "review_date": None,
            "notes": None
        }
    }
    
    draft = SafetyCaseDraft(
        metadata=metadata,
        top_goal=top_goal,
        argument_strands=strands,
        evidence_registry=evidence_registry,
        trace_chains=trace_chains,
        review_gates=review_gates
    )
    
    # Save if output path provided
    if output_path:
        md_content = render_markdown(draft)
        with open(output_path, 'w') as f:
            f.write(md_content)
        
        # Also save JSON
        json_path = output_path.replace('.md', '.json')
        with open(json_path, 'w') as f:
            json.dump(draft.to_dict(), f, indent=2)
    
    return draft


def render_markdown(case: SafetyCaseDraft) -> str:
    """Render safety case to markdown."""
    lines = [
        "# PROACTIVE Safety Case",
        "",
        "## ⚠️ DRAFT - REQUIRES HUMAN REVIEW",
        "",
        f"**Status**: {case.metadata['status']}  ",
        f"**Generated**: {case.metadata['generated_at']}  ",
        f"**Generator Version**: {case.metadata['generator_version']}  ",
        f"**Review Gates Remaining**: {case.pending_gates}",
        "",
        "---",
        "",
        "## Top-Level Goal",
        "",
        f"### {case.top_goal['id']}: {case.top_goal['text']}",
        "",
        f"**Confidence**: {case.top_goal['confidence']}",
        "",
        "[HUMAN_REVIEW_REQUIRED: Confirm this goal accurately captures the safety claim]",
        "",
        "---",
        "",
        "## Argument Strands",
        ""
    ]
    
    for strand in case.argument_strands:
        lines.extend([
            f"### {strand['strand_id']}: {strand['principle_name']}",
            "",
            f"**Sub-Goal**: {strand['sub_goal']['text']}  ",
            f"**Confidence**: {strand['sub_goal']['confidence']}",
            "",
            f"**Strategy**: {strand['strategy']['text']}",
            "",
            "#### Claims",
            ""
        ])
        
        for claim in strand.get("claims", []):
            lines.append(f"- **{claim['claim_text']}**")
            lines.append(f"  - Confidence: {claim['confidence']}")
            lines.append(f"  - Supported by: {', '.join(claim['supported_by'])}")
            if claim.get("human_review_required"):
                lines.append("  - [HUMAN_REVIEW_REQUIRED]")
            lines.append("")
        
        lines.extend(["#### Evidence", ""])
        for ref in strand.get("evidence_refs", []):
            lines.append(f"- {ref}: See Evidence Registry")
        lines.append("")
        
        lines.extend(["#### Gaps", ""])
        if strand.get("gaps"):
            for gap in strand["gaps"]:
                lines.append(f"- [ ] {gap}")
        else:
            lines.append("*No gaps identified*")
        lines.extend(["", "---", ""])
    
    # Evidence Registry
    lines.extend([
        "## Evidence Registry",
        "",
        "| ID | Description | Source | Adapter | Status | Review |",
        "|----|-------------|--------|---------|--------|--------|"
    ])
    
    for ev in case.evidence_registry:
        review = "[REVIEW]" if ev.get("human_review", {}).get("required") else "—"
        desc = ev["description"][:40] + "..." if len(ev["description"]) > 40 else ev["description"]
        lines.append(f"| {ev['id']} | {desc} | {ev['source_adapter']} | — | {ev['status']} | {review} |")
    
    lines.extend(["", "---", ""])
    
    # Trace chains
    lines.extend(["## Trace Chains", "", "```"])
    for chain in case.trace_chains:
        lines.extend([
            f"Principle {chain['principle']}",
            "    │",
            "    ▼",
            f"{chain['adapter']}",
            "    │",
            "    ▼",
            f"Evidence {chain['evidence_id']}",
            "    │",
            "    ▼",
            f"Claim: \"{chain['claim'][:60]}...\"",
            "    │",
            "    ▼",
            f"Safety Case {chain['strand']}",
            ""
        ])
    lines.extend(["```", "", "---", ""])
    
    # Human review summary
    summary = case.to_dict()["human_review_summary"]
    lines.extend([
        "## Human Review Summary",
        "",
        "| Category | Count |",
        "|----------|-------|",
        f"| Total Gates | {summary['total_gates']} |",
        f"| Pending | {summary['gates_pending']} |",
        f"| Approved | {summary['gates_approved']} |",
        f"| Rejected | {summary['gates_rejected']} |",
        "",
        "### Critical Review Gates",
        ""
    ])
    for gate in summary["critical_gates"]:
        lines.append(f"- [ ] {gate}")
    
    lines.extend([
        "",
        "---",
        "",
        "*This document was automatically generated and requires human review before it can be considered an approved safety case.*",
        "",
        "**DO NOT** treat this as a final safety case until all review gates are cleared."
    ])
    
    return "\n".join(lines)


def validate_case(case: SafetyCaseDraft) -> List[str]:
    """Validate safety case against schema."""
    errors = []
    
    if case.metadata.get("status") != "DRAFT":
        errors.append("Generated cases must have DRAFT status")
    
    if not case.top_goal.get("human_review", {}).get("required"):
        errors.append("Top goal must require human review")
    
    if not case.argument_strands:
        errors.append("No argument strands generated")
    
    if case.pending_gates == 0 and not case.is_approved:
        errors.append("Inconsistent state: no pending gates but not approved")
    
    return errors


if __name__ == "__main__":
    import sys
    
    workspace = sys.argv[1] if len(sys.argv) > 1 else "."
    output = sys.argv[2] if len(sys.argv) > 2 else "SAFETY_CASE_DRAFT.md"
    
    print("⚠️ CRITICAL: Output is DRAFT, NOT final safety case")
    print()
    
    draft = generate_safety_case(workspace=workspace, output_path=output)
    
    print(f"Generated: {output}")
    print(f"Status: {draft.metadata['status']}")
    print(f"Review gates: {draft.pending_gates} pending")
    print(f"Is approved: {draft.is_approved}")
```

4. Test with mock data:

```bash
cd ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR
python -c "from generator import generate_safety_case; generate_safety_case(output_path='SAFETY_CASE_DRAFT.md')"
```

### Acceptance Criteria

- [ ] `generator.py` runs without errors
- [ ] `evidence_collector.py` discovers adapter outputs
- [ ] Generated SAFETY_CASE_DRAFT.md has `[HUMAN_REVIEW_REQUIRED]` gates
- [ ] Status is always DRAFT for generated cases
- [ ] All strands have evidence refs or gaps documented
- [ ] Trace chains link principles to claims

---

## A04-T4: Create Documentation Templates

**Tier**: 2 (YELLOW)  
**Duration**: 30 minutes  
**Dependencies**: A04-T3 complete

### Outputs

- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/templates/review_checklist.md`
- `ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/scripts/validate_case.py`

### Acceptance Criteria

- [ ] Review checklist covers all gate categories
- [ ] Validation script checks schema compliance
- [ ] Approval workflow documented

---

## A04-T5: Run Validation, Capture Evidence

**Tier**: 3 (GREEN)  
**Duration**: 60-90 minutes  
**Dependencies**: A04-T3 complete, Adapters 01-03 have USE_CASE_EVIDENCE.md

### Outputs

- `USE_CASE_EVIDENCE.md` (complete with integration test)
- `SAFETY_CASE_DRAFT.md` (generated from real adapter outputs)

### Acceptance Criteria

- [ ] `USE_CASE_EVIDENCE.md` documents integration test
- [ ] `SAFETY_CASE_DRAFT.md` generated from adapter outputs
- [ ] All required elements present (goal, strands, evidence, trace)
- [ ] Review gates properly inserted
- [ ] Limitations documented

---

## A04-T6: Integrate with Framework Docs

**Tier**: 2 (YELLOW)  
**Duration**: 30-45 minutes  
**Dependencies**: A04-T5 complete

### Outputs

- Updated main `README.md`
- Cross-reference from 09_SAFETY_CASE/ to generated draft
- Complete adapter module table

### Acceptance Criteria

- [ ] All 4 adapters in main README
- [ ] 09_SAFETY_CASE/ references generated draft
- [ ] Trace chain documentation complete
- [ ] End-to-end flow documented

---

## Task Summary

| Task | Tier | Duration | Dependencies | Status |
|------|------|----------|--------------|--------|
| A04-T1: Define Schema | 2 | 45-60 min | Constitution, GSN | NOT_STARTED |
| A04-T2: Directory Structure | 1 | 15-20 min | A04-T1 | NOT_STARTED |
| A04-T3: Implement Generator | 3 | 90-120 min | A04-T2 | NOT_STARTED |
| A04-T4: Documentation | 2 | 30 min | A04-T3 | NOT_STARTED |
| A04-T5: Run Validation | 3 | 60-90 min | A04-T3, Adapters 01-03 | NOT_STARTED |
| A04-T6: Framework Integration | 2 | 30-45 min | A04-T5 | NOT_STARTED |

**Total Adapter 04 Time**: 4.5-6 hours  
**Minimum for Demo (T1-T3)**: 2.5-3.5 hours

---

## Quick Start (Minimum Viable)

```bash
# 1. Create directory and schema (T1)
mkdir -p ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR/templates
# [Create safety_case_schema.json and template]

# 2. Create stub structure (T2)
# [Create __init__.py, generator.py stub]

# 3. Implement and test (T3)
pip install pyyaml jinja2 jsonschema
cd ADAPTER_MODULES/04_SAFETY_CASE_GENERATOR
python generator.py ../.. SAFETY_CASE_DRAFT.md
# ⚠️ Output is DRAFT, requires human review!
```

---

## V&T Statement

### EXISTS (Specified)
- A04-T1 through A04-T6 task specifications
- Literal code for generator.py and evidence_collector.py
- Safety case schema with human review gates
- Template with `[HUMAN_REVIEW_REQUIRED]` markers

### FUNCTIONAL STATUS
This backlog provides complete task specifications for building Adapter 04.

### NOT CLAIMED
- Tasks have not been executed
- No actual safety case draft exists yet
- Integration with real adapter outputs not tested

### ⚠️ CRITICAL REMINDER
**Output is DRAFT with `[HUMAN_REVIEW_REQUIRED]` gates, NOT a final safety case.**
Generated safety cases must go through human review workflow before approval.

---

*Created: 2026-01-19 | Session 4*
