# Origin Story Visualization — Integration with PROACTIVE Toolkit

This app is the **origin story research visualization component** for the PROACTIVE AI Constitution Toolkit. It presents the conceptual narrative (The Bamboozle, Chronicle, Six Invariants, PROACTIVE Protocol) in a magazine-style, editable React UI.

## How It Fits the Narrative

| This app (conceptual) | Evidence doc (concrete) |
|-----------------------|--------------------------|
| **Genesis:** "The Bamboozle" — fluency ≠ truth | **ORIGIN_STORY_EVIDENCE.md** — Jan 2026 incident: phantom completion, blind spots, rigged protocol |
| **Chronicle:** 2022–2026 milestones (including The Incident) | Same incident timeline (Phase 1–7) |
| **Six Invariants** (I1–I6) | Failure modes F1–F5 map to invariant violations |
| **PROACTIVE Protocol** | Validation (n=200, p=0.001) proves the protocol works |

Use this app for **pitch / demo video**: show the magazine narrative, then point to `ORIGIN_STORY_EVIDENCE.md` (or a one-pager derived from it) as the *evidence* that motivated PROACTIVE.

## Running Locally

```bash
cd the-research-origin-story
npm install
# Optional: set GEMINI_API_KEY in .env.local if using Gemini in-app
npm run dev
```

Opens at `http://localhost:3000`.

## AI Studio

The README links to an AI Studio app. The `index.html` importmap uses `aistudiocdn.com` for React, Framer Motion, etc., so the same code can run in Google AI Studio.

## Interactive Simulations (Judge-Friendly)

Every major section has an **interactive simulation** written in plain language so anyone can understand:

| Section | Simulation | What it does |
|--------|------------|--------------|
| Genesis | Bamboozle Simulator | Toggle Without/With PROACTIVE; step through when AI says Done but didn't do it |
| Chronicle | Timeline | Drag or arrow keys to scrub; click a year to jump |
| MBSE Bridge | Traceability Simulator | Click REQ/CTRL/TEST/EVID/DECISION for plain-language labels |
| Six Invariants | Invariant Simulator | Toggle Without/With PROACTIVE for "I'm done" with no proof |
| PROACTIVE Protocol | Letters + Risk Tiers | Click each letter for definition; click risk bar for example + action |

Simple diagrams and simulations go a long way with judges; the app is written so non-experts can follow.

## Key Files in This Repo

- **ORIGIN_STORY_EVIDENCE.md** (repo root) — Incident timeline, failure modes, quotes.
- **PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md** (repo root) — Product vision, Gemini story, hackathon instructions.
- **the-research-origin-story/** — This visualization (Genesis, Chronicle, MBSE Bridge, Invariants, PROACTIVE, Author).

## Suggested Use for Hackathon

1. **Demo video:** Open this app → scroll through Genesis + Chronicle → run the simulations (Bamboozle, Traceability, Invariant, Risk tiers) → cut to “This happened” (ORIGIN_STORY_EVIDENCE summary) → show Contract Window + validation results.
2. **VC pitch:** Use the magazine as the “story” slide; show one or two simulations; use evidence doc + validation as the “proof” slide.
3. **AI Studio:** If the hackathon allows, link to or embed the AI Studio version of this app in the submission.
