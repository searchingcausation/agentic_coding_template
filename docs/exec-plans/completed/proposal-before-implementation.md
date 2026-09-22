# Execution plan: Proposal before non-trivial implementation

Status: completed
Risk: NORMAL — shared workflow changes across several documentation files.
Updated: 2026-09-22
Authorization: The user requested checking and adding this behavior to the template.

## Goal / specification

Before every non-trivial implementation, Codex and Claude Code must save and
present a proposal explaining the intended changes, assumptions, material
trade-offs, and proposed implementation tasks. Keep this knowledge in one Markdown
execution plan and maintain it through completion.

Acceptance criteria:
- The shared agreement applies this requirement without an explicit skill invocation.
- Non-trivial work is distinguished from trivial corrections, including LOW-risk work.
- The template captures the proposal, assumptions, ordered tasks, and verification.
- Planning, debugging, and user-facing guidance agree on timing and persistence.
- Existing authorization and independent-review boundaries remain explicit.

## Repository evidence

- [Shared agreement](../../../agent/README.md) already requires NORMAL plans, but
  does not explicitly require presenting a proposal before implementation.
- [Plan template](../template.md) has steps and trade-offs, but no dedicated
  proposed-change or assumptions section.
- Both tool entry points load the same agreement; no adapter changes are needed.

## Proposed changes

Make saving and presenting a proposal an explicit prerequisite for non-trivial
implementation. Extend the existing execution plan instead of adding a second
artifact. Align workflow and onboarding documentation with that rule.

## Assumptions / open questions

- Presenting a proposal does not itself add a universal approval gate. Existing
  implementation authorization remains valid; planning-only requests and HIGH
  changes retain their current boundaries.
- Trivial corrections can remain lightweight. LOW risk alone does not make work
  trivial; substantive design choices or coordinated changes still need a proposal.

## External documentation / freshness

Repository-only process documentation; local evidence suffices.

## Plan

1. Update the shared lifecycle with the trigger, proposal contents, timing, and
   authorization behavior. Verify that both tool entry points inherit the rule.
2. Extend the execution-plan template and lifecycle guide with explicit proposal,
   assumptions, and ordered task fields. Retain one file throughout the task.
3. Align planning/debugging workflows, README, principles, and adoption guidance.
4. Review the diff for consistency, run `make check`, record evidence, and archive.

## Trade-offs / decisions

Use one execution plan for proposal and implementation history. A separate proposal
file would separate review from progress but duplicate task context and decisions.
Keep approval tied to existing risk and authorization rules; the user's request
requires visibility before implementation, without explicitly requiring a new
approval round for every task.

## Verification

| Acceptance criterion / risk | Command or observation | Actual result |
| --- | --- | --- |
| Shared rule and aligned guidance | Review entry points and final documentation diff | Both tools inherit the shared rule; workflows and guidance aligned |
| Valid template structure and links | `make check` | Passed: harness checks and all 17 regression tests |
| Behavior actually followed by agents | Future task observation in Codex and Claude | Not exercised by documentation checks |

## Progress

- [x] Inspect existing instructions and identify gaps.
- [x] Save the proposal and explain the approach to the user.
- [x] Update agreement, template, workflows, and guidance.
- [x] Verify and archive.

## Failed approaches

None.

## Learnings and promotion

An existing requirement to record a plan did not explicitly require presenting it
before implementation. Promoted the timing and contents into the shared agreement
and execution-plan template.

## Risks / rollback

Avoid conflating complexity with risk or introducing contradictory approval rules.
Revert the task's documentation changes if needed; no runtime behavior changes.

## Review

Implementation-session self-review completed across the shared rule, template,
workflows, README, adoption guide, and principles. Resolved outdated claims that
task directories are empty now that this maintenance record is archived. No
independent review claimed. Actual agent compliance remains outside harness checks.

## Next step

None; implementation and required checks complete.
