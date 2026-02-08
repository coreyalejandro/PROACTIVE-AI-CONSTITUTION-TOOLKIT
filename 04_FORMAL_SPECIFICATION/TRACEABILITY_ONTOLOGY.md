# Traceability Ontology (MBSE Trace Log Schema)

**Status:** Canonical schema defined by adapter implementation.  
**Version:** 1.0  
**Date:** 2026-02-07  

---

## 1. Purpose

This document declares the **minimal, streamable** schema for the PROACTIVE MBSE Trace Log. It is the single source of truth for trace log structure used in evaluation (Forensic Trace Challenge), adapters (W&B Trace Adapter), and safety case evidence.

---

## 2. Canonical Schema Location

The authoritative JSON schema for a single trace log entry is:

**`ADAPTER_MODULES/01_WANDB_TRACE_ADAPTER/schema.json`**

That schema defines:

- **Required fields:** `claim_id`, `timestamp`, `claim_text`, `confidence_score`, `validator_results`, `final_decision`
- **Validator results:** I1–I6 check outcomes (PASS / FAIL / SKIP)
- **Trace chain:** REQ → CTRL → TEST → EVID → DECISION linkage
- **Failure mode:** F1–F5 or null
- **Epistemic tag:** OBSERVED / INFERRED / SPECULATED (I1)

Use that file for validation, ingestion, and tooling. This ontology document does not duplicate the schema; it points to it and states scope.

---

## 3. Scope

- **In scope:** Structure of one trace log entry per claim; invariant checks (I1–I6); trace chain IDs; final gate decision.
- **Out of scope:** Transport format (W&B, files, API); aggregation or sampling rules; retention policy.

---

## 4. Relationship to Evaluation

The **Forensic Trace Challenge** (see `05_EVALUATION_DESIGN/EVALUATION_PLAN_PREREGISTERED.md`) uses logs conforming to this schema. Metrics:

- **Root Cause Attribution Accuracy:** Auditors identify failed component/invariant using only the trace log.
- **Trace Completeness (H4):** Percentage of logs with valid, non-null required fields and complete REQ→CTRL→TEST→EVID→DECISION chain.

---

## 5. V&T Statement

**Exists:** This ontology document and `ADAPTER_MODULES/01_WANDB_TRACE_ADAPTER/schema.json` as the canonical trace log schema.

**Non-existence:** No separate TRACEABILITY_ONTOLOGY JSON-LD or OWL file; the JSON schema is the machine-readable spec.

**Unverified:** Formal validation that all adapter outputs conform to the schema has not been run in CI.

**Functional status:** Schema is in use by Adapter 01 (W&B); evaluation plan and safety case reference this structure.
