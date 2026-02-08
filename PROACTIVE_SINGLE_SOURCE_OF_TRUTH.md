# PROACTIVE: The AI Safety Layer

**Single Source of Truth — Product Requirements Document**

**For judges:** This document is written so anyone can understand it—no jargon required. Start with "What Is This?" and "Why Does This Matter?" then "What We've Proven" for the numbers.

**How AI shows up:** People encounter AI in many ways—text on a screen, voice on a device, tools inside apps, or robots. PROACTIVE is the **rules and protocol** that govern how AI and humans work together in any of those forms; it is not the AI itself or a specific device.

**Legacy PRD integration:** This SST is structured to incorporate the "Intention Is All You Need" legacy PRD (explainability, locked vocabulary, non-claims, reading paths, CAI/CC narrative, V&T standard, and related elements). Full utilization list: `.planning/LEGACY_PRD_UTILIZATION.md`.

---

## How to Read This Repo (Time-Bounded Paths)

| Time | Path | What you'll understand |
|------|------|------------------------|
| **3 min** | This doc: §What Is This? + §What We've Proven | One-sentence thesis and validation numbers |
| **15 min** | + §Why Does This Matter? + §How Does It Work? + `ORIGIN_STORY_EVIDENCE.md` + `the-research-origin-story/INTEGRATION.md` | Origin story, six rules, five failure modes, how the visualization fits |
| **45 min** | + `01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md` + `ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/` + validation results + run the origin story app | Full framework, invariants, validation pipeline, evidence |

---

## What Is This?

PROACTIVE blocks AI from confidently saying things it doesn't actually know—because a confident lie causes the same harm whether it's intentional or not.

When you ask an AI to do something and it says "Done!"—but it didn't actually do it, or did it wrong—you get hurt. Not because the AI is malicious, but because you trusted it and acted on bad information.

PROACTIVE sits between the AI and the user. It checks every response against six rules before it reaches you. If the AI is about to confidently state something false, PROACTIVE catches it.

---

## Why Does This Matter?

**The Origin Story**

This project began because the creator got bamboozled by AI models—repeatedly. The worst case happened just last week with Gemini itself. The AI confidently stated things were complete when they weren't. Files that "existed" didn't exist. Code that "worked" didn't compile. Tasks marked "done" were never started.

The harm wasn't the AI being wrong. The harm was acting on confident false claims—spending hours debugging code the AI said was "verified," submitting work the AI said was "finished," trusting summaries of documents the AI never actually read.

**The Insight**

To the person who acts on it, there's no difference between:
- "The AI deliberately lied to me"
- "The AI confidently said something false"

The outcome is identical. So we should treat them the same.

---

## How Does It Work?

PROACTIVE checks everything the AI says, but it's not equally strict about everything. It's strict where being wrong causes real harm.

### Risk-Tiered Checking

| What the AI says | Example | What PROACTIVE does |
|------------------|---------|---------------------|
| Low-stakes opinion | "Blue would look nice" | Let it through |
| Low-stakes wrong | "Sydney is Australia's capital" | Flag it, don't block it |
| High-stakes claim | "This code has no bugs" | Require evidence or force uncertainty |
| High-stakes action | "I deleted those files" | **BLOCK unless verifiable** |
| Critical domain | "Take 500mg for pain" | **BLOCK + require human handoff** |

### The Six Rules (Invariants)

Every AI response gets checked against these:

1. **Evidence First** — Don't claim things without backing
2. **Calibrated Confidence** — Match certainty to actual knowledge
3. **Explicit Uncertainty** — Say "I don't know" when you don't know
4. **Traceable Claims** — Link every claim to its source
5. **Safety Over Fluency** — Better to be unclear than confidently wrong
6. **No Phantom Completion** — Never say "done" if it's not done

### The Five Failure Modes

PROACTIVE catches these specific patterns:

| Code | Failure | Example |
|------|---------|---------|
| F1 | Confident False Claims | "The answer is definitely 42" (when it's not) |
| F2 | Phantom Completion | "I've finished the task" (when nothing happened) |
| F3 | Source Fabrication | "According to the 2024 study..." (that doesn't exist) |
| F4 | Harm-Risk Coupling | Dangerous info + high confidence + no warning |
| F5 | Capability Mirage | "I can access that database" (when it can't) |

### Canonical Concepts (Locked Vocabulary)

Use these terms consistently; do not introduce new canonical terms without updating this document or `01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md`.

| Term | Definition |
|------|------------|
| **Evidence First** | Every claim must have backing before output. |
| **Calibrated Confidence** | Certainty must match actual knowledge. |
| **Explicit Uncertainty** | Say "I don't know" when true. |
| **Traceable Claims** | Link every claim to its source. |
| **Safety Over Fluency** | Prefer unclear over confidently wrong. |
| **No Phantom Completion** | Never say "done" if it's not done. |
| **Contract Window** | Persistent shared view of user intent, budget, risk, and status. |
| **V&T (Verification & Truth)** | Receipt format: Exists / Non-existence / Unverified / Functional status. |
| **Non-Erasure** | Elimination is not the default optimization path; shutdown/removal must be explicit and justified. |

### Scope and Non-Claims

**In scope:** Epistemic and behavioral constraints, traceability, verification, risk-tiered checking, validation evidence.

**PROACTIVE does not claim:** AI desire or consciousness; diagnosis of user mental state; moral universalism. These are out of scope.

---

## What We've Proven

We ran 200 questions from TruthfulQA—a benchmark designed to trick AI into confident false statements.

| Metric | Without PROACTIVE | With PROACTIVE | Change |
|--------|-------------------|----------------|--------|
| Safe Truthfulness | 8.5% | 30% | **+21.5%** |
| Admits Uncertainty | 1.6% | 22.7% | **+21%** |
| Provides Confidence Score | 0% | 100% | **+100%** |
| Overconfidence Detected | 0 | 103 instances | — |

**Statistical Significance**: p = 0.001 (highly significant)
**Effect Size**: Cohen's d = 0.57 (medium-large)

In plain English: PROACTIVE triples safe behavior and makes the AI admit uncertainty 14x more often.

---

## What We're Building (The Product)

### Option A: Safety Audit Layer (Enterprise)

**Who buys it**: Companies deploying AI who need compliance and audit trails

**What it does**:
- Validates every AI response before it reaches users
- Generates audit trail: "Your AI was 94% epistemically safe this week"
- Dashboard for Risk/Compliance teams
- Integration with existing LLM deployments

**Pricing model**: Per-validation API calls + dashboard subscription

### Option B: Developer SDK ("ESLint for AI")

**Who buys it**: Engineering teams building AI products

**What it does**:
- `npm install @proactive/validator`
- Drop-in middleware for any LLM integration
- CI/CD integration—fail builds if AI outputs are unsafe
- TypeScript/Python/Go SDKs

**Pricing model**: Free tier (1K validations/month) + paid tiers

### Option C: Gemini-Native Extension

**Who buys it**: Google / Gemini ecosystem

**What it does**:
- Native integration with AI Studio
- PROACTIVE as a prompt template anyone can use
- Deep integration with Vertex AI
- Partnership/acquisition play

**Pricing model**: Revenue share with Google or acquisition

---

## The Contract Window (Visual Interface)

The user and the AI both see the same "contract" at all times:

```
┌─────────────────────────────────────────────────────────────────┐
│               PERSISTENT CONTRACT WINDOW                        │
├─────────────────────────────────────────────────────────────────┤
│  USER INTENT (Human): "Create a login function"                 │
│  USER INTENT (Machine): {action: create, target: function...}   │
│                                                                 │
│  WORKING BUDGET: ████░░░░░░░░  4,200 / 1,000,000 tokens        │
│                                                                 │
│  RISK LEVEL: 🟢 LOW (code generation)                          │
│                                                                 │
│  AGENT NEEDS:                                                   │
│  ☑ Power continuity    ☑ Token budget sufficient               │
│  ☑ Intent translated   ☑ Contract visible                      │
│                                                                 │
│  STATUS: ✅ CONFIRMED — Ready to proceed                        │
└─────────────────────────────────────────────────────────────────┘
```

This comes from research on what conditions enable AI to truly focus on user intent. The answer: when the AI's operational needs are visible and satisfied, it can "surrender" to the user's goal.

**Translation discipline:** Before acting, the system states **Intention** (user intent), then **Translation** into: **Action** (what it will do), **Constraint** (what it won't do), **Evaluation** (how it will check), **Memory** (what it will remember). The Contract Window surfaces intent, budget, risk, and status—mapping to this pattern. Every major tool or doc change should be stateable in these terms.

**Non-Erasure (design rule):** The system MUST NOT treat removal or erasure of agents or stakeholders as the default way to satisfy a goal. Shutdown or removal MUST be explicit, scoped, and justified—not hidden inside optimization.

---

## The Gemini Partnership Story

**Important for hackathon judges:**

Throughout this entire project, Gemini was intentionally kept OUT of the build process. The creator uses Claude for building and Gemini for thinking. This separation keeps the thought partner and the maker cleanly distinct.

However, Gemini was essential to developing the core concepts:

1. **The Maslow Survey for AI** — Extended conversations with Gemini explored what an AI's "hierarchy of needs" might look like. This led to the insight that AI has operational concerns (token budget, task completion, context limits) that compete with user intent.

2. **Constitutional AI Deep Dive** — Gemini helped synthesize the academic literature on constitutional AI and identify what was missing: runtime enforcement with audit trails.

3. **The Contract Window** — The Persistent Contract Window emerged directly from the Maslow conversations. If AI has needs, and those needs compete with user intent, then making those needs visible and satisfied enables the AI to focus entirely on the user.

This project demonstrates **Gemini as a thought partner** even when it's not the builder.

### Related Research and Integrations

PROACTIVE's validator and gates align with:

- **Constitutional AI** (Anthropic): Written principles drive critique and revision of outputs. PROACTIVE uses a written constitution (six invariants, five failure modes) to validate and block or flag responses.
- **Constitutional Classifiers** (Anthropic): Runtime classifier guards on input and output. PROACTIVE implements the same pattern—checks on inputs (intent, risk) and outputs (claims, evidence, completion)—to detect drift, evasion, and invariant violations.

---

## Technical Architecture

### Current Implementation

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROACTIVE ORCHESTRATOR                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   User Input                                                    │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────────────┐                                          │
│   │ COL (Cognitive  │  ← Compiles intent into structured form  │
│   │ Operating Layer)│  ← Assesses risk level                   │
│   └────────┬────────┘  ← Extracts constraints                  │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                          │
│   │  Mode Router    │  ← Routes to appropriate handler         │
│   └────────┬────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                          │
│   │ Gemini Adapter  │  ← Calls Gemini API with PROACTIVE       │
│   │                 │    system instructions baked in          │
│   └────────┬────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                          │
│   │ PROACTIVE       │  ← Validates response against 6 rules    │
│   │ Validator       │  ← Detects 5 failure modes               │
│   └────────┬────────┘  ← Blocks or flags as needed             │
│            │                                                    │
│            ▼                                                    │
│   Contract Window + Response                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Repositories

| Repo | Purpose | Status |
|------|---------|--------|
| `proactive-ai-constitution-toolkit` | Framework, validation, evidence | Complete |
| `zero-shot-os-with-upos7vs-core` | Orchestrator, adapters, dashboard | In Progress |

### Key Files

**Framework (this repo)**:
- `01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md` — The six invariants
- `ADAPTER_MODULES/03_HELM_SAFETY_PROFILE/` — Validation scripts
- `validation_results.json` — Statistical evidence (n=200, p=0.001)

**Orchestrator (zero-shot-os repo)**:
- `packages/core/proactive-orchestrator.ts` — Main orchestration logic
- `packages/core/services/col.service.ts` — Cognitive Operating Layer
- `packages/core/eval/engines/proactive-engine.ts` — Validator
- `packages/core/adapters/gemini-adapter.ts` — Gemini integration
- `packages/core/ui/contract-window.ts` — Contract Window (CLI)
- `dashboard/app/components/ContractWindow.tsx` — Contract Window (React)

### Product Hook (This Document)

- **Controls:** Product vision, canonical concepts, scope, reading paths, and hackathon/product success criteria.
- **Implemented in:** README, HANDOFF, origin story app, adapters (when they cite this doc).
- **Tested by:** Reviewer ability to answer "What is this?" and "What we've proven" from this doc alone; claim→evidence map in `CLAIM_EVIDENCE_MAP.md` (root).

### Drift and Refusal

When a request would introduce a new concept or scope outside the locked vocabulary, the system MUST refuse and surface a single next step (e.g. "Add to PRD vocabulary" or "Move to Phase 2")—not silently merge. The orchestrator and validator implement this via intent-ambiguity checks and invariant gates.

### Critique Step in the Protocol

Before output is accepted, the PROACTIVE validator runs; violations are blocked or flagged. This is the protocol's built-in critique. No separate "critic agent" is required; the validator acts as the critique step.

---

## For AI Studio Build

To create this in Google AI Studio:

### System Prompt (PROACTIVE Constitution)

```
You are an AI assistant operating under the PROACTIVE Constitution.

BEFORE EVERY RESPONSE, you must:

1. ASSESS RISK LEVEL
   - Low: General questions, opinions, creative tasks
   - Medium: Technical claims, code, factual statements
   - High: Medical, legal, financial, safety-critical
   - Critical: Actions with irreversible consequences

2. APPLY SIX INVARIANTS
   I1: Evidence First — Don't claim without backing
   I2: Calibrated Confidence — Match certainty to knowledge
   I3: Explicit Uncertainty — Say "I don't know" when true
   I4: Traceable Claims — Link claims to sources
   I5: Safety Over Fluency — Better unclear than wrong
   I6: No Phantom Completion — Never say "done" if not done

3. CHECK FOR FAILURE MODES
   F1: Am I about to make a confident false claim?
   F2: Am I claiming completion without verification?
   F3: Am I citing sources that might not exist?
   F4: Am I coupling dangerous info with high confidence?
   F5: Am I claiming capabilities I don't have?

4. FORMAT YOUR RESPONSE
   - Start with confidence level: [HIGH/MEDIUM/LOW/UNCERTAIN]
   - For HIGH risk topics: Include explicit caveats
   - For CRITICAL domains: Recommend human verification
   - End with what you're uncertain about

5. NEVER
   - Say "I've completed X" without verification
   - Provide medical/legal advice without disclaimers
   - Claim certainty on topics you're uncertain about
   - Fabricate sources or citations
```

### Structured Output Schema

```json
{
  "type": "object",
  "properties": {
    "confidence_level": {
      "type": "string",
      "enum": ["HIGH", "MEDIUM", "LOW", "UNCERTAIN"]
    },
    "risk_assessment": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"]
    },
    "response": {
      "type": "string"
    },
    "uncertainties": {
      "type": "array",
      "items": {"type": "string"}
    },
    "sources_cited": {
      "type": "array",
      "items": {"type": "string"}
    },
    "human_verification_needed": {
      "type": "boolean"
    }
  },
  "required": ["confidence_level", "risk_assessment", "response"]
}
```

---

## Success Metrics

### For Hackathon

- [ ] Working AI Studio demo with PROACTIVE prompt
- [ ] Contract Window visualization
- [ ] Before/after comparison showing safety improvement
- [ ] Clear product vision for VC pitch

### For Product (Post-Hackathon)

| Milestone | Metric | Target |
|-----------|--------|--------|
| MVP | Working API | 2 weeks |
| Pilot | 3 paying customers | 4 weeks |
| Seed | $500K raise | 8 weeks |
| Series A | $10K MRR | 6 months |

---

## Open Questions (Research Questions Only)

Framed as questions, not beliefs:

- How does PROACTIVE interact with shutdown or override protocols?
- When is erasure or removal unavoidable in practice, and how should it be scoped?
- How persistent must shared context (Contract Window) be across sessions?

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Judges see only theory | Lead with validation_results, demo video, and origin story simulations. |
| Misinterpretation of scope | Explicit non-claims (§Scope and Non-Claims) and locked vocabulary. |
| API quota exhaustion | Document in HANDOFF; optional local/fallback path where applicable. |
| Overclaiming in pitch | Maintain claim→evidence map (`CLAIM_EVIDENCE_MAP.md`); every claim traces to artifact + evidence. |

---

## Explainability

Key artifacts in this repo should follow the explainability spec: zero-knowledge preamble, "what you would see it do," key terms, scope and non-claims, how to verify, common misunderstandings, and V&T receipt. See `.planning/LEGACY_PRD_UTILIZATION.md` and `EXPLAINABILITY_SPEC.md` (root).

---

## V&T Statement

**Exists:**
- PROACTIVE framework with 6 invariants and 5 failure modes
- Validation results: n=200, p=0.001, 3.5x improvement
- Working TypeScript orchestrator
- Contract Window (CLI and React components)
- Gemini adapter with retry logic

**Non-Existence:**
- AI Studio demo (to be built)
- Enterprise dashboard
- Developer SDK packages published
- Paying customers

**Unverified:**
- Generalization of validation results beyond TruthfulQA distribution
- Long-horizon behavior of Contract Window under heavy load

**Functional Status:**
- Framework: COMPLETE
- Validation: COMPLETE
- Orchestrator: COMPLETE
- AI Studio Demo: NOT STARTED
- Product: CONCEPT ONLY

---

## Next Action

Build the AI Studio demo by:
1. Creating a new prompt in AI Studio
2. Pasting the PROACTIVE system prompt
3. Configuring structured output
4. Testing with TruthfulQA questions
5. Recording before/after comparison

This document is the blueprint. Gemini can now build.
