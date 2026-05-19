---
name: implement
description: Use for approved implementation plans or clearly small low-risk changes that do not require full planning.
---

# Implement Workflow

## Goal

Implement the approved plan with minimal, reviewable changes.

For small low-risk changes, implement directly only when the task is clear and no approval
gate is triggered.

## When To Use

Use when:

- the user approved a plan
- implementation scope is clear
- code or documentation changes are expected
- a small vertical slice can be implemented
- a bug fix has a clear local target
- tests or verification are known

## Small Changes Allowed Without Full Plan

Small changes may be made directly when they are clear and low risk:

- typo fixes
- small README or comment clarifications
- formatting in files already being touched
- local test fixes that do not change production behavior
- local bug fixes inside one clearly bounded function or file

Mention these changes in the final response.

If the change touches architecture, APIs, schemas, prompts, model behavior, dependencies,
eval logic, infrastructure, or broad module structure, stop and plan first.

## Process

1. Re-read the approved goal and plan.
2. Identify exact files to change.
3. Make the smallest useful change.
4. Add or update tests where reasonable.
5. Keep unrelated files untouched.
6. Run available tests, linting, or manual checks if possible.
7. Stop if scope expands unexpectedly.
8. Summarize changes and verification.
9. Update `continuity.md` if project state changed.

## Implementation Rules

- Follow the approved plan.
- Preserve existing style.
- Preserve public interfaces unless approved.
- Do not introduce new dependencies without approval.
- Do not change schemas silently.
- Do not change prompts/model behavior silently.
- Do not change evaluation logic silently.
- Do not hide failures with broad exception handling.
- Do not hardcode secrets or local paths.
- Do not perform opportunistic cleanup unless approved.
- Do not mix refactoring with behavior changes unless necessary and explained.

Prefer focused modules. A script or module over about 300 lines is a warning threshold:
split it where practical, or explain why keeping it together is clearer.

## Testing Rules

- Add unit tests for pure logic.
- Add contract tests for inputs and outputs.
- Mock external APIs in normal tests.
- Add regression tests for bug fixes where reasonable.
- For LLM behavior, prefer eval cases over brittle exact string tests.
- Do not require live API calls for standard test runs unless explicitly approved.

## Output Format

Use the full format for non-trivial implementation. Use a compact version for small
changes.

```md
## Changed Files

- ...

## What Changed

...

## Verification

- Tests run:
- Lint/type checks:
- Manual checks:
- Not run / why:

## Risks / Notes

...

## Continuity Update

Updated `continuity.md`: yes/no
Reason:
```

## Stop Conditions

Stop and ask if:

- the approved plan is insufficient
- unexpected architecture constraints appear
- tests fail for unrelated reasons
- the task requires broad refactoring
- the task requires a new dependency
- the task requires schema, API, prompt, model, or eval changes not previously approved
- unrelated files would need to be touched

