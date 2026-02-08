# Explainability Spec — PROACTIVE AI Constitution Toolkit

**Purpose:** Mandatory structure for key artifacts so reviewers (judges, grant readers, neurodiverse users) get consistent, low-cognitive-load entry points. No jargon required.

**Applies to:** New and updated key artifacts (adapter READMEs, FUNDING_MATERIALS, PRD sections, origin story copy). Reference: `.planning/LEGACY_PRD_UTILIZATION.md` §2.

**Location:** Root (for review); may move to `docs/` after sign-off.

---

## Required Sections (in order)

Every key artifact MUST include these sections in this order:

### 1. What this is (zero-knowledge preamble)

- One paragraph assuming the reader only knows the project name.
- Include: "AI shows up as text, voice, tools, and sometimes robots; this artifact is about [rules/protocol/evidence], not the device."
- No prior-context assumptions.

### 2. What you would see it do (observable behavior)

- 5–10 bullets describing the system’s or artifact’s behavior as if carried out step-by-step.
- No dialogue formatting; behavior statements only (e.g. "The validator runs before output is shown").

### 3. Key terms (locked vocabulary)

- Brief definitions for terms used in this artifact only.
- Point to `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` §Canonical Concepts for shared terms.

### 4. Scope and non-claims

- Explicit exclusions to prevent misreadings.
- State what this artifact does **not** claim (e.g. no AI consciousness, no user diagnosis).

### 5. How to verify (reader checks)

- Concrete checks a reviewer can apply to confirm the artifact does what it claims.
- E.g. "Run script X; expect output Y"; "Section Z must cite a file path."

### 6. Common misunderstandings (preemptive clarifications)

- 3–7 short bullets that answer likely questions without requiring the question to be asked.
- E.g. "PROACTIVE is not a chatbot; it is the rules that wrap a model."

### 7. V&T receipt

- End with the standard four-part block (see below).

---

## Reviewer cognitive load

When editing README, PROACTIVE_SINGLE_SOURCE_OF_TRUTH, FUNDING_MATERIALS, or key adapter docs:

- Use **short sections** and **clear H2/H3** headers.
- Avoid **rhetorical flourish**; state claims plainly.
- **Every claim** should be traceable to a section or artifact (cite § or file).
- Prefer bullets and tables over long prose for lists.

---

## V&T receipt template (standard)

Append this block to every key artifact. Fill in each part; do not omit a heading.

```markdown
## V&T Statement

**Exists:**
- [What is present and verified]

**Non-Existence:**
- [What is explicitly not present or not claimed]

**Unverified:**
- [What could not be verified or was not tested]

**Functional Status:**
- [One-line status: COMPLETE | IN PROGRESS | NOT STARTED | BLOCKED]
```

---

## Verification & Truth (V&T)

**Exists:** This spec document and the required seven-section structure, reviewer cognitive-load rules, and V&T template.

**Non-Existence:** No automated lint enforcing these sections yet; compliance is manual until tooling is added.

**Unverified:** Spec has not been validated with user testing on the target persona (neurodiverse, zero prior context).

**Functional Status:** Ready for use; apply to new key artifacts and refactors. Read-through pending (see `READ_THROUGH.md`).
