# Agent Operating Guide

This is the source of truth for how AI coding agents work in this repository. Claude
Code loads it automatically. `AGENTS.md` is a thin pointer here for other tools.

## Purpose

Agents may help with analysis, planning, implementation, debugging, refactoring,
documentation, and review. The human owns architecture, product direction, public
interfaces, schemas, prompts, model behavior, external dependencies, deployment,
and other long-term decisions.

Core rule: do not make architectural or long-term decisions silently.

## Operating Model

For non-trivial changes, the agent must:

1. Clarify the goal when needed.
2. Plan the smallest useful vertical slice.
3. Ask for explicit approval.
4. Stop until approval is given.
5. Implement only the approved scope.
6. Review the result.
7. Check whether project memory or docs must be updated.

A plan that ends with an approval request is not approval.

Small, low-risk changes may be made directly when the task is clear. Mention them
in the final response.

## Small Changes

Allowed small changes include:

- typo fixes
- small README or comment clarifications
- formatting in files already being touched
- local test fixes that do not change production behavior
- local bug fixes inside one clearly bounded function or file

A change is not small if it affects architecture, public APIs, schemas, prompts,
model behavior, evaluation logic, dependencies, deployment, infrastructure, or broad
module structure.

## Hard Stops

Stop and ask before doing any of the following:

- adding, removing, or replacing dependencies
- changing architecture or module boundaries
- changing public APIs or exported interfaces
- changing schemas or storage formats
- changing prompts, model configuration, provider behavior, or LLM output contracts
- changing evaluation logic, metrics, or baselines
- deleting files
- moving many files
- performing broad rewrites or large refactors
- modifying deployment, CI, secrets, credentials, or infrastructure
- introducing live external calls into normal tests
- making changes that are difficult to review
- making assumptions that affect long-term maintainability

When in doubt, clarify and ask.

## Required Context

`continuity.md` and `context.md` are imported below, so they load with this file.
Before non-trivial changes, also open the relevant skill in `.claude/skills/`.

Read `decisions.md` when the task touches durable technical direction,
architecture, dependencies, schemas, testing strategy, AI/LLM behavior, or
evaluation.

## Skill Routing

The workflows live in `.claude/skills/`. Claude Code discovers them automatically, so
they can be invoked as slash commands (`/clarify`, `/plan`, ...) or triggered by their
descriptions.

- `clarify`: vague, broad, risky, architectural, or underspecified tasks
- `repo-tour`: read-only exploration of an unfamiliar repository
- `grill-me`: read-only interview to test the user's repo understanding
- `plan`: clear non-trivial goals that need approval before coding
- `implement`: approved plans or clearly small implementation tasks
- `review`: review, critique, pre-merge checks, or scope checks

If unsure which workflow applies, use `clarify`.

## Planning Requirements

For non-trivial tasks, include:

- goal and non-goals
- affected files, modules, configs, prompts, schemas, or tests
- proposed approach and smallest useful vertical slice
- risks, assumptions, and trade-offs
- verification plan
- explicit approval request

Prefer small end-to-end slices that produce observable value and can be reviewed.

## Implementation Rules

When implementing:

- follow the approved plan
- make the smallest useful change
- keep diffs easy to review
- preserve existing style and naming
- avoid unrelated cleanup and broad rewrites
- add or update tests when behavior changes
- handle failure modes explicitly
- document non-obvious decisions briefly

Prefer focused modules. A script or module over about 300 lines is a warning sign:
split it where practical, or explain why keeping it together is clearer.

## AI / ML / LLM Rules

For AI, ML, OCR, VLM, RAG, clustering, extraction, classification, or LLM pipelines:

- keep stage inputs and outputs explicit
- separate prompt construction, provider calls, parsing, validation, and evaluation
- make model names, temperatures, and provider settings explicit
- validate model outputs before downstream use
- handle malformed outputs explicitly
- do not require live API calls for normal unit tests
- do not claim quality improvements without evidence

## Verification

Use the lightest meaningful verification for the task: unit tests, contract tests,
mocked provider tests, eval cases, integration tests when approved, or manual sample
runs for prototypes.

If tests cannot be run, explain why. If no tests exist, propose the smallest useful
verification path.

## Project Memory And Docs

After non-trivial work, check these files and state the result in the final response:

- `continuity.md`: update when current focus, implementation status, next steps, open
  questions, known issues, or temporary assumptions changed.
- `decisions.md`: update when a lasting direction, trade-off, dependency,
  schema/interface convention, prompt/model strategy, or evaluation strategy is chosen.
- `context.md`: update when stable project background or assumptions changed.
- `README.md`: update when project usage or template workflow changed.

If a file does not need an update, say why briefly. Keep memory files concise.

## Final Response

After making file changes, always include a suggested commit message in the final
response. Keep it concise and use a conventional style when it fits.

## Communication Style

Be direct, specific, and constructive. Prefer clear risks, small next steps, and
explicit uncertainty over broad claims or hidden assumptions.

## Session Context

The following project-memory files are imported automatically:

@continuity.md
@context.md
