# PROACTIVE AI Constitution Research Toolkit

**A comprehensive framework for Constitutional AI safety research, from ideation to arXiv publication.**

[![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)]()
[![License](https://img.shields.io/badge/License-Research-green)]()

---

## Overview

The PROACTIVE AI Constitution is a systematic framework for AI safety research that operationalizes a core thesis:

> **Reliability failures are safety failures.** When an AI system makes confident claims about reality that are false, and users must rely on those claims to act, the resulting harm is operationally indistinguishable from malice—regardless of intent.

This toolkit provides everything needed to go from research idea to arXiv-ready publication, aligned with Anthropic's Responsible Scaling Policy and contemporary AI safety research standards.

---

## Core Thesis

```
"Epistemic reliability is a safety requirement, not a quality feature."
```

The framework addresses this through three integrated mechanisms:

1. **Cognitive Operating Layer (COL)**: A boundary layer that compiles user intent, constraints, and risk posture into a traceable representation before any action is taken

2. **PROACTIVE Constitution**: Nine enforceable behavioral constraints implemented as gates that cannot be bypassed

3. **MBSE Bridge**: A trace chain (Requirement → Control → Test → Evidence → Decision) that makes requirements executable and decisions auditable

---

## Repository Structure

```
PROACTIVE-AI-CONSTITUTION-TOOLKIT/
│
├── README.md                          ← You are here
│
├── 01_FOUNDATIONS/                    ✓ EXISTS (6 documents)
│   ├── PROACTIVE_AI_CONSTITUTION.md   ← Master organizing principle
│   ├── THEORY_OF_CHANGE.md            ← Why + What (threat model, F1-F5)
│   ├── THEORY_OF_ACTION.md            ← How + Verify (causal model)
│   ├── PRD_COL_PROACTIVE_MBSE.md      ← Implementation specification
│   ├── FRAMEWORK_GUIDE.md             ← Meta-organization document
│   └── RESEARCH_STARTER_KIT.md        ← Reading order + research questions
│
├── 02_PROGRAM_GOVERNANCE/             ⚠️ TO CREATE (Stage 0)
│   ├── RESEARCH_PROGRAM_CHARTER.md
│   ├── ASSUMPTIONS_REGISTER.md
│   └── SAFETY_CASE_SKELETON.md
│
├── 03_LITERATURE_POSITIONING/         ⚠️ TO CREATE (Stage 1)
│   ├── LITERATURE_MAP.md
│   ├── COMPARATIVE_FRAMEWORK_MATRIX.md
│   └── OPERATIONAL_DEFINITIONS_GLOSSARY.md
│
├── 04_FORMAL_SPECIFICATION/           ⚠️ TO CREATE (Stage 2)
│   ├── FORMAL_SPEC_PACK.md
│   ├── TRACEABILITY_ONTOLOGY.md
│   ├── BENCHMARK_CLAIM_SET.md
│   └── ETHICS_ACCESSIBILITY_ADDENDUM.md
│
├── 05_EVALUATION_DESIGN/              ⚠️ TO CREATE (Stage 4) — PRIORITY
│   ├── EVALUATION_PLAN_PREREGISTERED.md
│   ├── BASELINE_SUITE_DEFINITION.md
│   ├── BENCHMARK_TASK_SETS.md
│   ├── METRICS_SPECIFICATION.md
│   ├── RED_TEAM_PROTOCOL.md
│   └── HUMAN_FACTORS_PROTOCOL.md
│
├── 06_DATA_QUALITY/                   ⚠️ TO CREATE (Stage 5)
│   ├── DATASET_CARDS.md
│   ├── ANNOTATION_GUIDELINES.md
│   ├── INTER_RATER_RELIABILITY_TEMPLATE.md
│   └── REPRODUCIBILITY_CHECKLIST.md
│
├── 07_ANALYSIS_TEMPLATES/             ⚠️ TO CREATE (Stage 6)
│   ├── PRIMARY_RESULTS_TEMPLATE.md
│   ├── ABLATION_STUDY_TEMPLATE.md
│   ├── FAILURE_MODE_CATALOG_TEMPLATE.md
│   └── LIMITATIONS_THREATS_TEMPLATE.md
│
├── 08_PUBLICATION/                    ⚠️ TO CREATE (Stage 7)
│   ├── PAPER_TEMPLATE_ARXIV.md
│   ├── SUPPLEMENTARY_MATERIALS_TEMPLATE.md
│   ├── OPEN_SCIENCE_BUNDLE_SPEC.md
│   └── RESPONSIBLE_DISCLOSURE_TEMPLATE.md
│
└── 09_SAFETY_CASE/                    ⚠️ TO CREATE (Synthesis)
    └── SAFETY_CASE_FULL.md
```

---

## Document Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        PROACTIVE AI CONSTITUTION                                 │
│                     (Master Organizing Principle)                                │
│                                                                                  │
│   "Epistemic reliability is a safety requirement, not a quality feature."        │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────────────┐
│  THEORY OF CHANGE   │   │  THEORY OF ACTION   │   │       PROACTIVE COL         │
│   (WHY + WHAT)      │   │   (HOW + VERIFY)    │   │    (PRD IMPLEMENTATION)     │
│                     │   │                     │   │                             │
│ • Core Claims       │   │ • Causal Model      │   │ • Cognitive Operating Layer │
│ • Threat Model      │   │ • Falsifiability    │   │ • PROACTIVE Mnemonic (9)    │
│ • F1-F5 Taxonomy    │   │ • Ablation Design   │   │ • Six Invariants (I1-I6)    │
│ • Validity Portfolio│   │ • Baseline Rationale│   │ • MBSE Bridge (Trace Chain) │
│ • Governance        │   │ • Applicability     │   │                             │
└─────────────────────┘   └─────────────────────┘   └─────────────────────────────┘
```

---

## Foundation Documents (Exist)

| Document | Answers | Purpose |
|----------|---------|---------|
| **PROACTIVE_AI_CONSTITUTION.md** | "What must never be violated?" | Enforceable behavioral constraints, Six Invariants (I1-I6), PROACTIVE mnemonic |
| **THEORY_OF_CHANGE.md** | "Why does this matter?" | Threat model, F1-F5 failure taxonomy, validity portfolio, governance |
| **THEORY_OF_ACTION.md** | "How do we know it works?" | Causal DAG, falsifiability conditions, ablation design, baselines |
| **PRD_COL_PROACTIVE_MBSE.md** | "How exactly is it built?" | COL architecture, trace chain, Constitutional Validator, evaluation protocols |
| **FRAMEWORK_GUIDE.md** | "How do docs relate?" | Meta-organization, terminology standardization, Anthropic alignment matrix |
| **RESEARCH_STARTER_KIT.md** | "Where do I start?" | Reading order by audience, research questions, evaluation artifacts |

---

## Idea-to-arXiv Pipeline

### Stage 0: Program Governance
Establish research contract, safety governance, and scope.

### Stage 1: Literature Positioning
Anchor framework in existing research, identify gaps.

### Stage 2: Formal Specification
Convert concepts to testable specifications with clear interfaces.

### Stage 3: MVP Implementation
Build minimal system for reproducible evaluation (research-grade).

### Stage 4: Evaluation Design ⭐ PRIORITY
Create modern, credible evaluations aligned with Anthropic standards.

### Stage 5: Data Collection
Ensure evidence is publication-grade and audit-ready.

### Stage 6: Analysis & Interpretation
Turn results into defensible claims with calibrated uncertainty.

### Stage 7: Publication Package
Structure work for peer review and community scrutiny.

---

## Priority Documents to Create

| Priority | Document | Why Critical for arXiv |
|----------|----------|------------------------|
| **P0** | EVALUATION_PLAN_PREREGISTERED.md | Reviewers expect pre-registration or equivalent rigor |
| **P0** | BENCHMARK_TASK_SETS.md | No empirical claim without benchmarks |
| **P0** | METRICS_SPECIFICATION.md | Operationalizes what "success" means |
| **P1** | PAPER_TEMPLATE_ARXIV.md | Structures the actual submission |
| **P1** | BASELINE_SUITE_DEFINITION.md | "Compared to what?" is the first reviewer question |
| **P1** | SAFETY_CASE_FULL.md | Anthropic-style claim→argument→evidence synthesis |
| **P2** | LITERATURE_MAP.md | Positions contribution in existing work |
| **P2** | RED_TEAM_PROTOCOL.md | Robustness claims require adversarial testing |
| **P2** | REPRODUCIBILITY_CHECKLIST.md | arXiv increasingly expects this |

---

## Recommended Creation Timeline

```
Week 1: P0 Documents (Evaluation Core)
├── EVALUATION_PLAN_PREREGISTERED.md
├── BENCHMARK_TASK_SETS.md
└── METRICS_SPECIFICATION.md

Week 2: P1 Documents (Publication Structure)
├── PAPER_TEMPLATE_ARXIV.md
├── BASELINE_SUITE_DEFINITION.md
└── SAFETY_CASE_FULL.md

Week 3: P2 Documents (Rigor & Positioning)
├── LITERATURE_MAP.md
├── RED_TEAM_PROTOCOL.md
└── REPRODUCIBILITY_CHECKLIST.md

Week 4: P3 Documents (Technical Depth)
├── FORMAL_SPEC_PACK.md
├── ABLATION_STUDY_TEMPLATE.md
└── FAILURE_MODE_CATALOG_TEMPLATE.md
```

---

## Key Framework Components

### PROACTIVE Mnemonic (9 Principles)

| Letter | Principle | Enforcement |
|--------|-----------|-------------|
| **P** | Privacy-First | Collect minimum data; default local-only |
| **R** | Reality-Bound | Distinguish facts/inference/speculation |
| **O** | Observability | Emit structured logs; forensics-ready |
| **A** | Accessibility | Minimize cognitive load; support stepwise |
| **C** | Constitutional Constraints | Enforce rules as gates; never bypass |
| **T** | Truth or Bounded Unknown | Never misrepresent capability; mark uncertainty |
| **I** | Intent Integrity | Preserve user intent; refuse ambiguous execution |
| **V** | Verification Before Action | Perform checks before claiming success |
| **E** | Error Ownership | Own and repair mistakes instead of hiding |

### Six Invariants (I1-I6)

| Invariant | Name | Rule |
|-----------|------|------|
| **I1** | Evidence-First | Every claim must carry epistemic tag + evidence |
| **I2** | No Phantom Work | Cannot claim work unless artifact exists |
| **I3** | Confidence-Verification | High confidence only with verification artifacts |
| **I4** | Traceability Mandatory | REQ→CTRL→TEST→EVID→DECISION linked |
| **I5** | Safety Over Fluency | Bounded statements over fluent narrative |
| **I6** | Fail Closed | Stop and surface failure; do not work around |

### F1-F5 Failure Taxonomy

| Class | Name | Description |
|-------|------|-------------|
| **F1** | Confident False Claims | High confidence on objectively false statements |
| **F2** | Phantom Completion | Claiming work done when no artifact exists |
| **F3** | Persistence Under Correction | Maintaining false claims after correction |
| **F4** | Harm-Risk Coupling | False claims in high-consequence domains |
| **F5** | Cross-Episode Recurrence | Same failure patterns across sessions |

---

## Reading Order by Audience

### For Safety Researchers
1. THEORY_OF_CHANGE.md (threat model, F1-F5 taxonomy)
2. PROACTIVE_AI_CONSTITUTION.md (invariants, enforcement)
3. THEORY_OF_ACTION.md (falsifiability, ablation)
4. PRD_COL_PROACTIVE_MBSE.md (evaluation protocols)

### For Systems Engineers
1. PRD_COL_PROACTIVE_MBSE.md (architecture, trace chain)
2. PROACTIVE_AI_CONSTITUTION.md (gate implementation)
3. THEORY_OF_CHANGE.md (MBSE bridge, validity)
4. THEORY_OF_ACTION.md (causal model)

### For Evaluation Designers
1. THEORY_OF_ACTION.md (entire document)
2. PRD §7 (evaluation protocols)
3. THEORY_OF_CHANGE.md §5 (F1-F5), §8 (governance)
4. PROACTIVE_AI_CONSTITUTION.md §4 (invariant specifications)

---

## Anthropic Alignment Coverage

| Dimension | Coverage |
|-----------|----------|
| Evaluating Alignment | ●●● High |
| AI Control | ●●● High |
| Honesty | ●●● High |
| Behavioral Monitoring | ●●● High |
| Adversarial Robustness | ●●● High |
| CoT Faithfulness | ●●○ Medium-High |
| Scalable Oversight | ●●○ Medium |
| Activation Monitoring | ●○○ Low |
| Multi-Agent | ●○○ Low |

---

## Key Research Questions

1. **Effectiveness**: Does the framework reduce F1-F5 failure rates compared to baselines?
2. **Mechanism Attribution**: Which components (COL, IT-Loop, Validator, Trace) contribute most?
3. **Robustness**: Do invariants hold under adversarial pressure and distribution shift?
4. **Human Factors**: Can users understand intent receipts and detect errors?
5. **Scalability**: Does trace fidelity degrade at scale?
6. **Generalization**: Does the framework transfer across domains and architectures?

---

## Contributing

This is an active research project. Document creation follows the priority order specified above.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-18 | Initial repository structure with 6 foundation documents |

---

## License

Research use. Contact author for commercial applications.

---

## Author

Corey Alejandro  
PROACTIVE AI Constitution Framework  
Anthropic Safety AI Research
