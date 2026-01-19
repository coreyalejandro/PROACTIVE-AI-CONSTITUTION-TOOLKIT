# Related Work Positioning: PROACTIVE Framework

## Landscape Overview

PROACTIVE occupies a specific niche: **runtime safety enforcement for AI systems with full audit trail**. This differs from:
- Training-time alignment (Constitutional AI, RLHF)
- Benchmark-only evaluation (HELM, BIG-bench)
- Observability-only tooling (LangSmith, W&B vanilla)

## Comparative Matrix

| Approach | Training-Time | Runtime | Enforcement | Audit Trail | Toolchain Integration |
|----------|---------------|---------|-------------|-------------|----------------------|
| Constitutional AI (Anthropic) | ✓ | ✗ | Soft | ✗ | ✗ |
| RLHF | ✓ | ✗ | Soft | ✗ | ✗ |
| HELM | ✗ | Eval only | ✗ | Partial | ✗ |
| LangSmith | ✗ | ✓ | ✗ | ✓ | ✓ |
| OpenTelemetry for LLMs | ✗ | ✓ | ✗ | ✓ | ✓ |
| **PROACTIVE** | ✗ | ✓ | ✓ | ✓ | ✓ |

## Gap PROACTIVE Fills

1. **Constitutional AI** aligns models at training time but provides no runtime guarantees or audit capability
2. **HELM** evaluates models but doesn't enforce constraints in production
3. **LangSmith/OpenTelemetry** provide observability but no constitutional validation layer
4. **PROACTIVE** combines: runtime enforcement + constitutional validation + full MBSE trace + toolchain adapters

## Key Differentiators

1. **Failure Mode Taxonomy (F1-F5)**: Specific, testable failure categories vs. vague "alignment" concerns
2. **Six Invariants (I1-I6)**: Enforceable gates, not aspirational principles
3. **MBSE Trace Chain**: Engineering-grade audit trail (Requirement→Control→Test→Evidence→Decision)
4. **Adapter Architecture**: Integrates with existing tools rather than replacing them

## Positioning Statement
PROACTIVE is not a replacement for training-time alignment or benchmark evaluation. It is the **runtime enforcement and audit layer** that makes alignment claims verifiable in production.

## Citations to Include
- Bai et al. (2022) - Constitutional AI
- Liang et al. (2022) - HELM
- [OpenTelemetry LLM semantic conventions]
- [LangSmith documentation]
- Anthropic RSP documentation

---
## V&T

- Created: 2026-01-19T06:00:00Z
- Status: COMPLETE
- Blocked by: nothing
