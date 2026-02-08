# Legacy PRD Utilization: "Intention Is All You Need" → PROACTIVE Refactor

**Purpose:** What from the earlier All-In-One-Prompt-PRD-Plan (Intention Is All You Need) can still be utilized in the PROACTIVE refactor, with what, how, and rationale.

**Source:** ChatGPT export (2/7/2026); Phase 1–3 PRD + explainability + Anthropic integration drafts.

<!-- markdownlint-disable MD060 -->

---

## 1. V&T (Verification & Truth) Receipt Standardization

| What | How | Rationale |
| ---- | --- | ---------- |
| Earlier PRD required every artifact to end with a **V&T block** in fixed form: **Exists** / **Non-existence** / **Unverified** / **Functional status**. | Add to `CONTRIBUTING.md` (or a shared `docs/V_T_SPEC.md`) the **exact four-line template** and require it on all new artifacts. Optionally add a lint/check that key docs contain the four headings. | PROACTIVE already uses "V&T" and "Verification & Truth" throughout; standardizing the four categories reduces ambiguity and makes receipts machine-parseable and reviewer-consistent. |

---

## 2. Explainability as Mandatory Per-Artifact Structure

| What | How | Rationale |
| ---- | --- | ---------- |
| Phase 1 explainability spec: every artifact must include (in order): (1) **What this is (zero-knowledge preamble)**, (2) **What you would see it do (observable behavior)**, (3) **Key terms (locked vocabulary)**, (4) **Scope and non-claims**, (5) **How to verify (reader checks)**, (6) **Common misunderstandings**, (7) **V&T receipt**. | Add `docs/EXPLAINABILITY_SPEC.md` that defines this structure. Apply it to **new** key artifacts (e.g. new adapter READMEs, new FUNDING_MATERIALS). Optionally add a short "Explainability" subsection to `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` that points to this spec. | PROACTIVE already has "For judges" and plain-language sections; making explainability a **required structure** (not just tone) ensures hackathon reviewers and neurodiverse users get consistent, low-cognitive-load entry points. |

---

## 3. Intention → Translation (Action / Constraint / Evaluation / Memory)

| What | How | Rationale |
| ---- | --- | ---------- |
| Earlier "Translation Card": before acting, the system states **Action**, **Constraint**, **Evaluation**, **Memory** (what it will do, what it won’t do, how it will check, what it will remember). | Document in `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` or `01_FOUNDATIONS/` that the **Contract Window** and orchestrator behavior align with this pattern: e.g. "Working budget" + "Risk level" + "Agent needs" + "Status" map to constraint/evaluation; "User intent" maps to intention. Add a one-paragraph "Translation discipline" that says: every major tool or doc change should be stateable as Action/Constraint/Evaluation/Memory. | PROACTIVE already has intent, budget, risk, status; naming the **Translation** pattern explicitly ties the refactor to a testable, reviewer-friendly protocol and reduces ad-hoc behavior. |

---

## 4. SEC / Non-Erasure as Explicit Design Rule

| What | How | Rationale |
| ---- | --- | ---------- |
| **Shared Existential Context (SEC):** "elimination is not an optimization path"; **Non-Erasure:** design rule that elimination is not used as default. | Add to `01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md` (or a short "Design rules" section) an explicit **Non-Erasure** principle: e.g. "System MUST NOT treat removal or erasure of agents/stakeholders as the default way to satisfy a goal; shutdown/removal MUST be explicit, scoped, and justified." Optionally map SEC to one of the six invariants (e.g. Evidence-First or Safety Over Fluency) so it’s traceable. | PROACTIVE is about epistemic safety and blocking harmful confidence; SEC/non-erasure is a missing **explicit** constraint that strengthens the refactor’s alignment story and differentiates it from "helpful" systems that optimize by removing participants. |

---

## 5. Locked Vocabulary / Canonical Concepts Section

| What | How | Rationale |
| ---- | --- | ---------- |
| Single "Canonical Concepts" section with one-sentence definitions: Intention, Translation, SEC, Non-Erasure (and in PROACTIVE terms: the six invariants, five failure modes, Contract Window, V&T). | Add a **Canonical concepts** or **Locked vocabulary** subsection to `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` (or `01_FOUNDATIONS/`) listing the allowed terms and one-line definitions. Require that new artifacts don’t introduce new canonical terms without a PRD/Constitution update. | Reduces term sprawl and reviewer confusion; makes "no ad-hoc concepts" enforceable; aligns with earlier PRD’s "no new concepts introduced ad-hoc" completion rule. |

---

## 6. Phase / Milestone Completion Definitions

| What | How | Rationale |
| ---- | --- | ---------- |
| Explicit "Phase N is complete when" checklist (e.g. repo builds, artifacts cross-reference, no new ad-hoc concepts, V&T everywhere). | Add to `TASK_MANAGEMENT/EXECUTION_MANIFEST.md` or a dedicated `TASK_MANAGEMENT/PHASE_COMPLETION.md` a **Completion definition** per phase/milestone (e.g. "Hackathon-ready: AI Studio demo built, demo video script exists, key files list current"). | Makes handoffs and "done" unambiguous; supports HANDOFF.md and prevents scope creep. |

---

## 7. Reviewer Cognitive Load Rules

| What | How | Rationale |
| ---- | --- | ---------- |
| Design principles: short sections, clear headers, no rhetorical flourish, every claim traceable to an artifact. | Add to `CONTRIBUTING.md` or `docs/EXPLAINABILITY_SPEC.md` a short **Reviewer cognitive load** section: e.g. "Use short sections and clear H2/H3; avoid rhetorical flourish; every claim should cite a section or artifact." Apply when editing README, PROACTIVE_SINGLE_SOURCE_OF_TRUTH, FUNDING_MATERIALS. | Matches PROACTIVE’s judge-friendly goal and the earlier PRD’s "reviewer can reconstruct thinking without meeting you"; reduces fatigue for hackathon judges and grant reviewers. |

---

## 8. Time-Bounded Guided Reading Paths

| What | How | Rationale |
| ---- | --- | ---------- |
| README (or front door) offers **3-minute**, **15-minute**, **45-minute** paths with explicit "Read A, then B, then C" and "what you should now understand" after each. | In `README.md` add a **How to read this repo** subsection: e.g. "3 min: PROACTIVE_SINGLE_SOURCE_OF_TRUTH §What Is This? + §What We've Proven; 15 min: + ORIGIN_STORY_EVIDENCE + INTEGRATION.md; 45 min: + 01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION + validation_results + the-research-origin-story." | Hackathon judges have limited time; explicit paths prevent "where do I start?" and align with earlier PRD’s guided-tour idea. |

---

## 9. Product Hook Per Artifact (Claim → Control → Test)

| What | How | Rationale |
| ---- | --- | ---------- |
| Each artifact has a **Product Hook**: what behavior this claim controls, where it lives in the tool (rule, classifier, eval, UI), how it is tested. | For key artifacts (e.g. adapter READMEs, PROACTIVE_SINGLE_SOURCE_OF_TRUTH, 03_HELM_SAFETY_PROFILE), add a short **Product Hook** subsection: "This doc controls: [X]. Implemented in: [adapter/script/UI]. Tested by: [validation script or eval]." | Strengthens "research → tangible tool/product" narrative; makes it obvious what is implemented vs aspirational; supports Anthropic-style empirical, public-output framing. |

---

## 10. Constitutional AI + Constitutional Classifiers Integration Narrative

| What | How | Rationale |
| ---- | --- | ---------- |
| Earlier PRD required **Constitutional AI** (critique+revision from a written constitution) and **Constitutional Classifiers** (input/output classifier guards) as named integrations. | In `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` or `01_FOUNDATIONS/`, add a short **Related research / Integrations** subsection: "PROACTIVE’s validator and gates align with Constitutional AI (written principles driving critique and revision) and Constitutional Classifiers (runtime classifier guards on input/output)." Cite Anthropic CAI and CC once. | Improves credibility for fellowship/grant reviewers; satisfies "integrate at least one Anthropic research product" without changing implementation. |

---

## 11. Narration-Ready / Diagram-Derivable Requirement

| What | How | Rationale |
| ---- | --- | ---------- |
| "Every major concept has a 30–60 second spoken version; artifacts are diagram-derivable and video-explainable without rewrite." | In `the-research-origin-story/INTEGRATION.md` or a `docs/NARRATION_SPEC.md`, add: "Every major concept (Genesis, Invariants, PROACTIVE Protocol, Contract Window) MUST have a 30–60s narration-ready summary and be explainable from existing diagrams/simulations." Use this when adding new sections to the origin story or pitch. | Demo video and VC pitch benefit from a clear "narration spine"; PROACTIVE already has simulations—formalizing narration-ready reduces last-minute script writing. |

---

## 12. Explicit Non-Claims / Scope Exclusions

| What | How | Rationale |
| ---- | --- | ---------- |
| Explicit exclusions: no claims about AI desire/consciousness, no diagnosing human mental states, no moral universalism. | Add to `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` (or 01_FOUNDATIONS) a **Scope and non-claims** subsection: e.g. "PROACTIVE does not claim: AI desire or consciousness; diagnosis of user mental state; moral universalism. In scope: epistemic and behavioral constraints, traceability, verification." | Prevents misreading and scope creep; aligns with earlier PRD’s "explicit non-claims" and reviewer safety. |

---

## 13. Critique Step / Self-Critique in Protocol

| What | How | Rationale |
| ---- | --- | ---------- |
| A separate "critic voice" that checks artifacts for drift, vagueness, untestable claims before finalizing. | Document in `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` or adapter docs that the **validator** (and optionally a review checklist) acts as the critique step: e.g. "Before output is accepted, PROACTIVE validator runs; violations are blocked or flagged; this is the protocol’s built-in critique." Optionally add a `prompts/critique-checklist.md` for human review of key docs. | Makes the Constitutional AI–style "critique then revise" visible in the refactor without building a new agent; reinforces quality and traceability. |

---

## 14. Drift Detection and Refusal Behavior

| What | How | Rationale |
| ---- | --- | ---------- |
| "Scope drift detected; I will stop and ask for Phase change, not silently blend it in." | In `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` or 01_FOUNDATIONS, add one paragraph on **Drift and refusal**: e.g. "When a request would introduce a new concept or scope outside the locked vocabulary, the system MUST refuse and surface a single next step (e.g. 'Add to PRD vocabulary' or 'Move to Phase 2'), not silently merge." Document how the orchestrator or validator implements this (e.g. intent-ambiguity → block). | Aligns with Intent Integrity (I5) and prevents silent scope creep; gives reviewers a clear "safety behavior" to point to. |

---

## 15. Claim → Artifact → Evidence Map (Application / Essay Source-Map)

| What | How | Rationale |
| ---- | --- | ---------- |
| **Essay/application source-map:** each claim maps to artifact section → evidence → phrasing constraints (no version sprawl). | Add a single `docs/CLAIM_EVIDENCE_MAP.md` (or a section in HANDOFF): table with columns **Claim** \| **Artifact §Section** \| **Evidence** \| **Phrasing note**. Populate for the main hackathon/VC claims (e.g. "PROACTIVE improves safe truthfulness" → validation_results.json + PROACTIVE_SINGLE_SOURCE_OF_TRUTH §What We've Proven). | Ensures pitch and application essays stay aligned with one source of truth; reduces duplicate or conflicting wording. |

---

## 16. Open Questions as Research Questions

| What | How | Rationale |
| ---- | --- | ---------- |
| Open questions framed as research questions (e.g. "How persistent must context be?") not as beliefs. | Add to `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` or 01_FOUNDATIONS an **Open questions** subsection: 3–5 short questions (e.g. "How does PROACTIVE interact with shutdown protocols?" "When is erasure unavoidable in practice?") with no asserted answers. | Signals intellectual honesty and invites collaboration; matches earlier PRD’s "allowed open questions" and reduces overclaiming. |

---

## 17. Risks and Mitigations Table

| What | How | Rationale |
| ---- | --- | ---------- |
| Explicit **Risks & mitigations** table (e.g. perceived abstraction → concrete metrics; misinterpretation → explicit non-claims). | Add to `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` or HANDOFF a **Risks & mitigations** table: e.g. "Risk: Judges see only theory \| Mitigation: Lead with validation_results + demo video + simulations." "Risk: API quota exhaustion \| Mitigation: Document in HANDOFF; optional local fallback." | Makes risks visible and shows deliberate mitigation; strengthens grant and hackathon submissions. |

---

## 18. Multimodal Grounding (AI = Text / Voice / Tools / Robot)

| What | How | Rationale |
| ---- | --- | ---------- |
| Explanation that "AI shows up as text, voice, embedded tools, and sometimes robots; this project is the rules/protocol, not the body." | Add one short paragraph to the "For judges" or "What Is This?" section of `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` (and optionally README): "People encounter AI in many ways—text on a screen, voice on a device, tools inside apps, or robots. PROACTIVE is the **rules and protocol** that govern how AI and humans work together in any of those forms; it is not the AI itself or a specific device." | Reduces "AI = robot" confusion and broadens concept attainment; reuses the earlier PRD’s explainability refinement. |

---

## Summary Table

| #   | Item                                              | Where to apply                          | Priority |
| --- | ------------------------------------------------- | --------------------------------------- | -------- |
| 1 | V&T standardization | CONTRIBUTING / V_T_SPEC | High |
| 2 | Explainability spec (per-artifact structure) | EXPLAINABILITY_SPEC.md + new artifacts | High |
| 3 | Intention → Translation (Action/Constraint/Eval/Memory) | PROACTIVE_SINGLE_SOURCE_OF_TRUTH, Contract Window docs | Medium |
| 4 | SEC / Non-Erasure design rule | PROACTIVE_AI_CONSTITUTION or Design rules | High |
| 5 | Locked vocabulary / Canonical concepts | PROACTIVE_SINGLE_SOURCE_OF_TRUTH or 01_FOUNDATIONS | Medium |
| 6 | Phase completion definitions | EXECUTION_MANIFEST or PHASE_COMPLETION.md | Medium |
| 7 | Reviewer cognitive load rules | CONTRIBUTING / EXPLAINABILITY_SPEC | Medium |
| 8 | Time-bounded reading paths (3 / 15 / 45 min) | README | High |
| 9 | Product Hook per artifact | Key artifacts (adapters, PRD, HELM) | Medium |
| 10 | CAI + Constitutional Classifiers narrative | PROACTIVE_SINGLE_SOURCE_OF_TRUTH or 01_FOUNDATIONS | Medium |
| 11 | Narration-ready / diagram-derivable | INTEGRATION.md or NARRATION_SPEC | Medium |
| 12 | Explicit non-claims / scope exclusions | PROACTIVE_SINGLE_SOURCE_OF_TRUTH or 01_FOUNDATIONS | High |
| 13 | Critique step in protocol | PROACTIVE_SINGLE_SOURCE_OF_TRUTH, validator docs | Low |
| 14 | Drift detection and refusal | PROACTIVE_SINGLE_SOURCE_OF_TRUTH or 01_FOUNDATIONS | Medium |
| 15 | Claim → evidence map | CLAIM_EVIDENCE_MAP.md or HANDOFF | High |
| 16 | Open questions (research Qs only) | PROACTIVE_SINGLE_SOURCE_OF_TRUTH or 01_FOUNDATIONS | Low |
| 17 | Risks & mitigations table | PROACTIVE_SINGLE_SOURCE_OF_TRUTH or HANDOFF | Medium |
| 18 | Multimodal grounding (text/voice/tools/robot) | PROACTIVE_SINGLE_SOURCE_OF_TRUTH, README | Medium |

---

## Verification & Truth (V&T)

- **Exists:** This document and the 18-item utilization list with What / How / Rationale and a summary table.
- **Non-existence:** No code or repo structure was changed; only this planning artifact was added.
- **Unverified:** Prior PRD was provided in user message; PROACTIVE refactor state was inferred from HANDOFF, PROACTIVE_SINGLE_SOURCE_OF_TRUTH, 01_FOUNDATIONS, INTEGRATION.md, and grep results. No formal trace to every PROACTIVE artifact was run.
- **Functional status:** List is ready for use to decide which legacy PRD elements to adopt and where; implementation is left to follow-up tasks.
