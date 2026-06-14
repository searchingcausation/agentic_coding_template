---
name: implement
description: Use for approved implementation plans or clearly small low-risk changes.
---

# Implement Workflow

## Goal

Implement the approved scope with minimal, reviewable changes.

Small low-risk changes may be implemented directly only when no hard stop in
`AGENTS.md` is triggered.

## Use When

- the user approved a plan
- implementation scope is clear
- a small vertical slice can be implemented
- a bug fix has a clear local target
- tests or verification are known

## Process

1. Re-read the approved goal and plan.
2. Identify exact files to change.
3. Make the smallest useful change.
4. Add or update tests when behavior changes.
5. Keep unrelated files untouched.
6. Run available checks or explain why they were not run.
7. Stop if scope expands unexpectedly.
8. Check whether `continuity.md`, `decisions.md`, `context.md`, or `README.md` need updates.
9. Summarize changes, verification, and memory/docs updates.

## Rules

- Follow the approved plan.
- Preserve existing style and public interfaces unless approved.
- Do not add dependencies, change schemas, prompts, model behavior, eval logic, or
  infrastructure unless approved.
- Do not mix unrelated cleanup with the requested change.
- Mock external APIs in normal tests.

## Final Response

Use a compact summary:

- changed files
- what changed
- verification run or not run
- memory/docs updates made or skipped, with brief reasons
- remaining risks or notes
- suggested commit message

## Stop If

- the approved plan is insufficient
- unexpected architecture constraints appear
- tests fail for unrelated reasons
- broad refactoring or a new dependency is required
- unapproved schema, API, prompt, model, or eval changes are needed
