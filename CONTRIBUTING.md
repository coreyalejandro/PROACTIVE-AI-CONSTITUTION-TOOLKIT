# Contributing to PROACTIVE AI Constitution Toolkit

## Document Creation Priority

When contributing new documents, follow this priority order:

### P0 — Critical for arXiv (Create First)
- `05_EVALUATION_DESIGN/EVALUATION_PLAN_PREREGISTERED.md`
- `05_EVALUATION_DESIGN/BENCHMARK_TASK_SETS.md`
- `05_EVALUATION_DESIGN/METRICS_SPECIFICATION.md`

### P1 — High Priority
- `08_PUBLICATION/PAPER_TEMPLATE_ARXIV.md`
- `05_EVALUATION_DESIGN/BASELINE_SUITE_DEFINITION.md`
- `09_SAFETY_CASE/SAFETY_CASE_FULL.md`

### P2 — Medium Priority
- `03_LITERATURE_POSITIONING/LITERATURE_MAP.md`
- `05_EVALUATION_DESIGN/RED_TEAM_PROTOCOL.md`
- `06_DATA_QUALITY/REPRODUCIBILITY_CHECKLIST.md`

### P3 — Lower Priority
- Remaining documents in each directory

## Document Standards

### Required Sections

Every document must include:

1. **Header Block**
   ```markdown
   # [DOCUMENT TITLE]
   ## [Subtitle]
   **Version:** X.Y
   **Date:** YYYY-MM-DD
   **Status:** Draft | Review | Foundation
   ```

2. **Verification & Truth Statement** (at end)
   ```markdown
   ## Verification & Truth Statement

   ### EXISTS (Verified Present)
   - [List what this document contains]

   ### VERIFIED AGAINST
   - [List source documents/standards]

   ### NOT CLAIMED
   - [Explicit non-claims]

   ### FUNCTIONAL STATUS
   [What role this document serves]
   ```

### Naming Convention

- Use SCREAMING_SNAKE_CASE for document names
- Include version in document, not filename
- Keep filenames descriptive but concise

### Cross-References

When referencing other documents:
- Use relative paths: `../01_FOUNDATIONS/THEORY_OF_ACTION.md`
- Include section numbers: `THEORY_OF_ACTION.md §3.2`
- Link to specific claims when possible

## Review Process

1. Create document following template
2. Self-review against V&T checklist
3. Cross-reference against source documents
4. Submit for peer review
5. Address feedback
6. Merge when approved

## Questions

Open an issue for:
- Clarification on document scope
- Template modifications
- Priority adjustments
- Cross-reference conflicts
