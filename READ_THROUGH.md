# Read-Through: Human + Code Assistant

**Purpose:** Run a structured read-through of the SST integration artifacts (and related docs) using a **human reviewer** and a **code assistant** so clarity, consistency, and traceability are checked before moving specs to `docs/` or locking copy.

**Artifacts in scope (root, for review):**

- `EXPLAINABILITY_SPEC.md`
- `CLAIM_EVIDENCE_MAP.md`
- `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` (reference; ensure it points to root specs)

---

## 1. Human reviewer instructions

**Role:** Judge / grant reader / zero-prior-context user. You are checking: Can I understand this without meeting the author? Is every claim backed? Is the wording consistent?

**Steps (in order):**

1. **Time-bounded pass (3 min)**  
   - Read only: `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` §What Is This? + §What We've Proven.  
   - **Check:** Can you state in one sentence what PROACTIVE is and what was proven?  
   - **Note:** Any phrase that confused you or required prior knowledge.

2. **Explainability spec pass**  
   - Open `EXPLAINABILITY_SPEC.md`.  
   - **Check:** Does each required section (1–7) have a clear, actionable description?  
   - **Check:** Would you know how to apply this to a new adapter README?  
   - **Note:** Missing or ambiguous instructions; suggest one concrete example (e.g. "Example for §1: …").

3. **Claim–evidence pass**  
   - Open `CLAIM_EVIDENCE_MAP.md`.  
   - **Check:** For each row, can you locate the **Artifact § Section** and **Evidence** in the repo?  
   - **Check:** Does the **Phrasing note** prevent overclaim? Note any claim you’ve seen in pitch/funding docs that is **not** in the map.  
   - **Note:** Broken links, wrong section refs, or claims that need a new row.

4. **Consistency pass**  
   - Skim `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` for: Canonical concepts, Scope and non-claims, Open questions, Risks and mitigations.  
   - **Check:** Does the SST use the same terms as `EXPLAINABILITY_SPEC` and `CLAIM_EVIDENCE_MAP` (e.g. V&T, Non-Erasure)?  
   - **Note:** Inconsistencies (e.g. "Non-existence" vs "Verified Non-Existing").

5. **Sign-off**  
   - If you’re satisfied: note "Human read-through complete — [date]" and any remaining caveats.  
   - If not: list blocking issues (with file + section or claim row) so they can be fixed before moving to `docs/`.

---

## 2. Code assistant instructions

**Role:** Structural and traceability check. You are checking: Do references resolve? Are required sections present? Is the V&T template correct?

**Steps (in order):**

1. **Reference resolution**  
   - In `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md`, find every reference to `EXPLAINABILITY_SPEC`, `CLAIM_EVIDENCE_MAP`, `LEGACY_PRD_UTILIZATION`, and `docs/` paths.  
   - **Check:** Each reference points to an existing file (root or `.planning/`).  
   - **Report:** Any broken path or reference to a file that does not exist.

2. **Explainability spec structure**  
   - Parse `EXPLAINABILITY_SPEC.md` for the seven required section titles (What this is, What you would see it do, Key terms, Scope and non-claims, How to verify, Common misunderstandings, V&T receipt).  
   - **Check:** All seven are present and in the stated order.  
   - **Report:** Missing or out-of-order sections.

3. **V&T template**  
   - In `EXPLAINABILITY_SPEC.md`, locate the V&T receipt template.  
   - **Check:** It contains exactly four headings: **Exists**, **Non-Existence**, **Unverified**, **Functional Status**.  
   - **Report:** If any heading is different or missing.

4. **Claim–evidence map table**  
   - In `CLAIM_EVIDENCE_MAP.md`, verify the table has columns: Claim | Artifact § Section | Evidence | Phrasing note.  
   - **Check:** Each row’s "Artifact § Section" refers to a real document (e.g. PROACTIVE_SINGLE_SOURCE_OF_TRUTH) and, where applicable, a section that exists in that document.  
   - **Report:** Rows with invalid or unresolvable artifact/section refs.

5. **Cross-doc consistency**  
   - Grep for "V&T", "Verification & Truth", "Non-Existence", "Non-Erasure" across `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md`, `EXPLAINABILITY_SPEC.md`, `CLAIM_EVIDENCE_MAP.md`.  
   - **Check:** No conflicting definitions (e.g. "Verified Non-Existing" vs "Non-Existence"); SST and specs use the same V&T headings where applicable.  
   - **Report:** Inconsistencies with file and line or section.

6. **Output**  
   - Produce a short report: **Pass** / **Fail** for each step, plus the **Report** items.  
   - If all steps pass: "Code assistant read-through complete — no blocking issues."  
   - If any fail: list blocking issues so they can be fixed before moving to `docs/`.

---

## 3. After the read-through

- **Human** and **code assistant** outputs should be recorded in **`READ_THROUGH_RESULTS.md`** (code-assistant report + time-boxed human run sheet).
- Fix any blocking issues; then re-run the relevant step(s).
- When both human and code assistant sign off (or document non-blocking caveats), the root artifacts are ready to:
  - stay in root for ongoing review, or
  - be copied/moved to `docs/` and references updated accordingly.

---

## V&T Statement

**Exists:** This read-through procedure and the separate instructions for human reviewer and code assistant.

**Non-Existence:** No completed run of the read-through has been recorded in-repo yet.

**Unverified:** Procedure has not been tested end-to-end with an actual human and assistant run.

**Functional Status:** Ready to use; run when SST integration artifacts are to be reviewed before finalizing or moving to `docs/`.
