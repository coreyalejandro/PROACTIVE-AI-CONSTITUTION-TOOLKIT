# Budget Estimate: PROACTIVE Toolkit Development

## Pipeline B: Minimum Viable Funding Package (2 weeks)

| Category | Hours/Units | Rate/Cost | Total |
| -------- | ----------- | --------- | ----- |
| Researcher time | 80 hours | $75/hr | $6,000 |
| Compute (API calls) | ~10K calls | — | $300 |
| W&B Pro (optional) | 1 month | — | $50 |
| GitHub Copilot | 1 month | — | $20 |
| Contingency (15%) | — | — | $956 |
| **TOTAL PIPELINE B** | — | — | **$7,326** |

### Pipeline B Deliverables

- Adapter 01: W&B Trace Adapter (functional)
- Adapter 02: CI Safety Gate (functional)
- Pilot validation with N=5-10 cases
- Feasibility demonstration report
- All code open-sourced

## Pipeline A: Full Research Toolkit (4 weeks)

| Category | Hours/Units | Rate/Cost | Total |
| -------- | ----------- | --------- | ----- |
| Researcher time | 160 hours | $75/hr | $12,000 |
| Compute (API calls) | ~25K calls | — | $750 |
| External auditor time | 20 hours | $100/hr | $2,000 |
| Participant compensation | 10 auditors | $50 each | $500 |
| W&B Pro | 1 month | — | $50 |
| GitHub Copilot | 1 month | — | $20 |
| HELM compute | — | — | $200 |
| Contingency (15%) | — | — | $2,328 |
| **TOTAL PIPELINE A** | — | — | **$17,848** |

### Pipeline A Deliverables

- All 4 adapters (W&B, CI Gate, HELM, Safety Case Generator)
- Quantitative validation study (N=8-12 auditors, N=20-30 cases)
- Pre-registered methodology with published raw data
- arXiv-ready paper draft
- Open-source toolkit release
- Safety case documentation

## Rate Justification

- **$75/hr researcher rate**: Based on AI safety research contractor rates; below market for specialized ML safety work but appropriate for independent researcher building portfolio
- **$100/hr external auditor rate**: Senior engineer rate for blind evaluation participation
- **$50 participant compensation**: Standard rate for 1-2 hour evaluation task

## Compute Assumptions

- **API calls**: Primarily Claude/GPT-4 for testing adapter behavior, generating test cases, and validation runs
- **W&B**: Trace logging during development and validation
- **HELM**: Integration testing with benchmark scenarios

## Risk Factors

| Risk | Impact | Mitigation |
| ---- | ------ | ---------- |
| Auditor recruitment | Could delay Pipeline A | Start recruitment early; have backup pool |
| API cost overrun | 10-20% budget impact | Built into contingency; optimize prompts |
| Scope creep | Timeline extension | Strict task backlog; ship minimum viable |

## Funding Sources Under Consideration

- Anthropic AI Safety Fellows Program
- Open Philanthropy
- LTFF (Long-Term Future Fund)
- Independent researcher grants
- Self-funded (Pipeline B if necessary)

## In-Kind Contributions (Already Completed)

The following work has been completed without funding:

- Complete conceptual framework (6 foundation documents)
- F1-F5 failure taxonomy with documented cases
- PROACTIVE mnemonic specification
- Evaluation design and pre-registration plan
- Repository infrastructure and documentation

Estimated value: 100+ hours of research and documentation work.

---

## V&T

- Created: 2026-01-19T05:41:00Z
- Status: COMPLETE
- Blocked by: nothing
