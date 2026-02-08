# PROACTIVE · Research Origin Story

A magazine-style visualization of why PROACTIVE exists: the origin story (being misled by AI), the research path (2022–2026), and the six rules we enforce. Written so anyone can follow—Genesis (The Bamboozle), Chronicle (timeline), Six Invariants, and PROACTIVE Protocol.

Part of the [PROACTIVE-AI-CONSTITUTION-TOOLKIT](https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT) repo. See [INTEGRATION.md](./INTEGRATION.md) for how this app fits the hackathon narrative and evidence.

## Run locally

**Prerequisites:** Node.js 18+

1. Install dependencies: `npm install`
2. (Optional) For AI-powered content editing, set `GEMINI_API_KEY` in `.env.local`
3. Run: `npm run dev`

Open [http://localhost:3000](http://localhost:3000).

## AI Studio

This app can run in Google AI Studio. The `index.html` import map uses `aistudiocdn.com` for React, Framer Motion, etc.

## Contents

- **Genesis** — “The Bamboozle” (Malcolm X quote), origin narrative
- **Chronicle** — Interactive timeline: 2022 Disconnect → 2023 Mapping the Void → 2024 MBSE Bridge → 2025 Invariant Lock → 2026 The Incident
- **MBSE Bridge** — REQ → CTRL → TEST → EVID → DECISION traceability
- **Six Invariants** — I1–I6 from the PROACTIVE Constitution
- **PROACTIVE Protocol** — P-R-O-A-C-T-I-V-E mnemonic and risk tiers
- **Author** — Lead researcher section

All simulations use simple diagrams and plain language so anyone can understand. Editable sections (Genesis, Chronicle, Invariants) can be updated via the Neural Content Editor when `GEMINI_API_KEY` is set.
