# Execution plan: Capture conversation learnings

Status: completed
Risk: LOW — local documentation and working-agreement changes.
Updated: 2026-10-15
Authorization: User accepted the proposal to capture open topics and improve documentation from clarification questions.

## Goal / specification

Preserve actionable discoveries from conversations in existing task records or the
backlog. Improve the relevant documentation when a clarification reveals a reusable
explanation gap. Acceptance: distinguish confirmed problems, hypotheses, and open
decisions; capture proportionate options and trade-offs; retain authorization
boundaries; avoid duplicate records and automatic edits for every question.

## Repository evidence

The shared working agreement already requires durable task state and documentation
updates. The execution-plan guide defines the backlog lifecycle but lacks explicit
conversation discovery and clarification guidance.

## External documentation / freshness

Repository-local process only; no external dependencies.

## Proposed changes

Extend `agent/README.md` with conversation-driven discovery and documentation rules.
Extend `docs/exec-plans/README.md` with compact discovery details and backlog usage.
Keep existing artifact locations and the current backlog table.

## Assumptions / open questions

No unresolved questions. Individual learning preferences alone do not establish a
documentation defect; reusable gaps do justify a targeted clarification.

## Plan

1. Save and present this proposal.
2. Update the shared agreement and execution-plan guide.
3. Review the diff, run `make check`, record results, and archive this plan.

## Trade-offs / decisions

Use short prose beneath backlog entries for discovery detail rather than widening
the table or adding a new tracker. This keeps scanning easy while allowing richer
reasoning when needed. Elaborate options only when evidence supports them; retain
unknowns explicitly instead of inventing solutions.

## Verification

| Acceptance criterion / risk | Command or observation | Actual result |
| --- | --- | --- |
| Guidance covers both requested behaviors and their limits | Review documentation diff | Passed: both behaviors, proportional detail, existing records, and authorization boundaries covered |
| Repository checks pass | `make check` | Passed: harness checks and all 17 regression tests |

## Documentation impact

Update the shared agreement and execution-plan guide. No runtime, architecture,
product specification, or skill adapter changes are needed.

## Progress

- [x] Proposal saved.
- [x] Proposal presented; guidance updated and verified.

## Failed approaches

None.

## Learnings and promotion

Promoted both accepted conversation improvements into the shared working agreement
and execution-plan guide.

## Follow-ups

None.

## Risks / rollback

Excess documentation could obscure useful guidance. Keep changes local and
proportionate; revert the added paragraphs if the policy needs revision.

## Review

Implementation-session self-review completed against the acceptance criteria.
No findings remain. `git diff --check` passed. Independent review is not required.

## Outcome

Delivered both requested behaviors in [the working agreement](../../../agent/README.md)
and [execution-plan guidance](../README.md). Discoveries retain evidence status,
proportionate options/trade-offs, and next steps. Reusable clarification gaps lead
to targeted documentation improvements. No deviations or outstanding limitations;
checks validate repository integrity, while future conversations will demonstrate
how consistently the guidance is applied.

## Next step

None; completed.

## Subsequent revision — 2026-10-16

At the user's request, removed the clarification-driven documentation improvement
rule from the shared agreement and execution-plan guide. Automatically revising
explanations creates unwanted overhead. Conversation discovery and backlog guidance
remain in place; the earlier outcome above records the original delivery.
