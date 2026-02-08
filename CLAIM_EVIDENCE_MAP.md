# Claim → Evidence Map — PROACTIVE AI Constitution Toolkit

**Purpose:** Map each main claim used in pitch, hackathon submission, or application to an artifact section and evidence. Use this so wording stays aligned with one source of truth and overclaiming is avoided.

**Location:** Root (for review); may move to `docs/` after sign-off.

**Reference:** `.planning/LEGACY_PRD_UTILIZATION.md` §15; `PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md` §Risks and Mitigations.

---

## Map

| Claim | Artifact § Section | Evidence | Phrasing note |
|-------|--------------------|----------|---------------|
| PROACTIVE blocks AI from confidently saying things it doesn't know | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §What Is This? | — | One-sentence thesis; do not add "only" or "always." |
| Confident lie causes same harm whether intentional or not | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §Why Does This Matter? (The Insight) | — | Keep "operationally indistinguishable" optional; plain "same harm" is enough. |
| PROACTIVE triples safe behavior / 14x more uncertainty admission | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §What We've Proven | `ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/validation_results.json` (or equivalent); n=200, p=0.001 | Use "triples" and "14x" only with "in our TruthfulQA evaluation"; do not generalize beyond that benchmark. |
| Safe truthfulness 8.5% → 30% (+21.5%) | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §What We've Proven | validation_results.json; TruthfulQA subset | Cite "TruthfulQA" and sample size (n=200). |
| Statistical significance p = 0.001, Cohen's d = 0.57 | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §What We've Proven | validation_results.json; analysis output | "Highly significant" and "medium-large effect" are allowed; do not claim "proven in production." |
| Six rules (invariants) / five failure modes | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §How Does It Work?; 01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md | — | List I1–I6 and F1–F5 by name when detail needed; otherwise "six rules, five failure modes." |
| Risk-tiered checking (low/medium/high/critical) | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §How Does It Work? (Risk-Tiered Checking) | — | Table is canonical; do not add new tiers without PRD update. |
| Contract Window: intent, budget, risk, status | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §The Contract Window | zero-shot-os: contract-window.ts, ContractWindow.tsx | "Persistent shared view"; do not claim "solves" intent without citing validation. |
| Gemini as thought partner, not builder | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §The Gemini Partnership Story | — | Keep "Claude for building, Gemini for thinking"; do not imply Gemini wrote code. |
| Aligns with Constitutional AI and Constitutional Classifiers | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §Related Research and Integrations | — | "Aligns with" / "same pattern"; cite Anthropic CAI and CC once; do not claim endorsement. |
| Non-erasure: elimination not default optimization | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §Canonical Concepts; §Non-Erasure (design rule) | — | "Shutdown/removal must be explicit and justified." |
| Product options A (Audit), B (SDK), C (Gemini-Native) | PROACTIVE_SINGLE_SOURCE_OF_TRUTH §What We're Building | — | Options are concept only unless otherwise stated; no "we will ship" without milestone. |

---

## How to use

- **Pitch / demo:** Use only claims that have a row above; use the **Phrasing note** to avoid overclaim.
- **Application / essay:** For each assertion, look up the row and cite **Artifact § Section** and **Evidence** where required.
- **Updates:** When adding a new public claim, add a row. When changing wording in the SST or evidence, update the **Phrasing note** if needed.

---

## V&T Statement

**Exists:** This map and the 12 claim rows for the main hackathon/VC claims listed above.

**Non-Existence:** Not every sentence in FUNDING_MATERIALS or README has been audited against this map yet; treat as target state.

**Unverified:** Map has not been cross-checked line-by-line against all pitch and funding docs.

**Functional Status:** Ready for use in read-through (see `READ_THROUGH.md`); update as claims or evidence change.
