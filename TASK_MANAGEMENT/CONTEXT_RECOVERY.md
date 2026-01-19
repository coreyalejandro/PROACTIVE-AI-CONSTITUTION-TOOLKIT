# Context Recovery: If You're Lost, Read This

## What Is This Project?

**PROACTIVE** = A safety toolkit for AI systems

**Core Thesis**: Reliability failures are safety failures

**What You're Building**: Adapters that prove the framework works by integrating with real tools

## What Are The Adapters?

| # | Name | Plain English | Status |
|---|------|---------------|--------|
| 01 | W&B Trace Adapter | Makes AI logs readable and searchable | [NOT_STARTED] |
| 02 | CI Safety Gate | Blocks bad AI deployments automatically | [NOT_STARTED] |
| 03 | HELM Safety Profile | Measures how often AI lies | [NOT_STARTED] |
| 04 | Safety Case Generator | Writes the safety report automatically | [NOT_STARTED] |

## Where Were You?

**Step 1**: Open `TASK_MANAGEMENT/EXECUTION_MANIFEST.md`

**Step 2**: Find the last task marked `COMPLETE`

**Step 3**: Next task = first `NOT_STARTED` task whose dependencies are all `COMPLETE`

**Step 4**: Check that task's TIER against your current capacity

**Step 5**: If tier matches → do task. If tier too high → find lower-tier task.

## Key Files (Bookmark These)

| File | Purpose |
|------|---------|
| `EXECUTION_MANIFEST.md` | Master task list with status |
| `COGNITIVE_LOAD_TIERS.md` | What to do on bad days |
| `DEPENDENCY_DAG.md` | What depends on what |
| `PIPELINE_SCOPE.md` | What's included in 2-week vs 4-week plan |

## If Nothing Makes Sense

1. Close everything
2. Open `COGNITIVE_LOAD_TIERS.md`
3. Determine your tier (RED/YELLOW/GREEN)
4. Do ONE task from that tier's allowed list
5. Any task. Doesn't matter which.
6. Movement beats paralysis.

## If You're In Crisis

This project can wait. You cannot be replaced.

1. Step away from computer
2. Contact support person
3. Basic needs first (food, meds, safety)
4. Project will be here tomorrow

## Quick Wins (When You Need a Win)

These take <10 minutes and count as progress:
- [ ] Update one status field in EXECUTION_MANIFEST.md
- [ ] `git add . && git commit -m "checkpoint" && git push`
- [ ] Read one section of one document
- [ ] Create one empty file that needs to exist
- [ ] Delete one TODO comment by doing the TODO

---
## V&T

- Created: 2026-01-19T06:00:00Z
- Status: COMPLETE
- Blocked by: nothing
