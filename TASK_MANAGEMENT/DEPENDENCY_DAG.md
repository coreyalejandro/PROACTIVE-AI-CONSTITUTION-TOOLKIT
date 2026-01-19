# Dependency DAG: PROACTIVE Toolkit

## Visual Representation

```text
                    [P0: Foundation]
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
    [A01-T1]          [A02-T1]          [A03-T1]
        │                 │                 │
        ▼                 ▼                 ▼
    [A01-T2]          [A02-T2]          [A03-T2]
        │                 │                 │
    ┌───┴───┐         ┌───┴───┐         ┌───┴───┐
    │       │         │       │         │       │
    ▼       ▼         ▼       ▼         ▼       ▼
[A01-T3] [A01-T4] [A02-T3] [A02-T4] [A03-T3] [A03-T4]
    │       │         │       │         │       │
    └───┬───┘         └───┬───┘         └───┬───┘
        │                 │                 │
        ▼                 ▼                 ▼
    [A01-T5]          [A02-T5]          [A03-T5]
        │                 │                 │
        ▼                 ▼                 ▼
    [A01-T6]          [A02-T6]          [A03-T6]
        │                 │                 │
        └────────────────┬┴─────────────────┘
                         │
                         ▼
                    [A04-T1]
                         │
                         ▼
                    [A04-T2]
                         │
                         ▼
                    [A04-T3] ◄── MERGE POINT
                         │
                    ... (T4-T6)
```

## Critical Path

P0 → A01-T1 → A01-T2 → A01-T3 → A01-T5 → A01-T6 → A04-T3 → A04-T5

## Parallelization Opportunities

- A01, A02, A03 can run in parallel after P0
- Within each adapter: T3 and T4 can run in parallel (both depend on T2)

## Recovery Checkpoints

| Checkpoint | After Task | State | Can Ship? |
|------------|------------|-------|-----------|
| CP0 | P0-09 | All foundation docs exist | Pitch only |
| CP1 | A01-T3 | Working W&B adapter | Demo |
| CP2 | A01-T6 | Full Slice 1 complete | Mini-paper |
| CP3 | A02-T6 + A03-T6 | All slices complete | Full paper |
| CP4 | A04-T6 | Synthesis complete | Toolkit release |

---

## V&T

- Created: 2026-01-19T07:00:00Z
- Status: COMPLETE
- Blocked by: nothing
