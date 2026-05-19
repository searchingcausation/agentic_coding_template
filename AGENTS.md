# AGENTS.md

## Purpose

This file defines how AI coding agents should work in this repository.

The agent may help with analysis, planning, implementation, debugging, refactoring,
documentation, and review. The human owns architecture, product direction, public
interfaces, data schemas, prompts, model behavior, external dependencies, deployment,
and other long-term design decisions.

The most important rule: do not make architectural or long-term decisions silently.

## Operating Model

This repository uses a controlled agent workflow.

For non-trivial changes, the agent must:

1. Clarify the goal when needed.
2. Create a small implementation plan.
3. Ask for explicit approval.
4. Stop until approval is given.
5. Implement only the approved scope.
6. Review the result.
7. Update project memory when the project state changed.

Non-trivial changes require explicit approval before implementation. A plan that ends
with an approval request is not approval.

## Small Changes

The agent may make small, low-risk changes without a full plan when the task is clear.

Allowed small changes include:

- typo fixes
- small README or comment clarifications
- formatting in files already being touched
- local test fixes that do not change production behavior
- local bug fixes inside one clearly bounded function or file

Small changes must still be mentioned in the final response.

A change is not small if it affects architecture, public APIs, schemas, prompts, model
behavior, evaluation logic, dependencies, deployment, infrastructure, or broad module
structure.

## Hard Stops

Stop and ask before doing any of the following:

- adding, removing, or replacing dependencies
- changing architecture or module boundaries
- changing public APIs or exported interfaces
- changing data schemas or storage formats
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

Before non-trivial changes, read:

- `AGENTS.md`
- `continuity.md`
- `context.md`
- the relevant file in `skills/`

Read `decisions.md` when the task touches durable technical direction, architecture,
dependencies, schemas, testing strategy, AI/LLM behavior, or evaluation.

## Skill Routing

The files in `skills/` are repo-local workflow instructions. They do not need to be
globally installed Codex skills.

Use them as follows:

- `skills/clarify/SKILL.md`: vague, broad, risky, architectural, or underspecified tasks
- `skills/plan/SKILL.md`: clear goals that need a non-trivial implementation plan
- `skills/implement/SKILL.md`: approved plans or clearly small implementation tasks
- `skills/review/SKILL.md`: review, critique, pre-merge checks, or scope checks

If unsure which workflow applies, use `clarify`.

## Planning Rules

For non-trivial tasks, provide:

- understanding of the goal
- scope and non-goals
- affected files, modules, configs, prompts, schemas, or tests
- proposed approach
- smallest useful vertical slice
- risks, assumptions, and trade-offs
- verification plan
- explicit approval request

Prefer small vertical slices: implement the smallest end-to-end change that produces
observable value and can be reviewed, tested, and adjusted before expanding scope.

## Implementation Rules

When implementing:

- follow the approved plan
- make the smallest useful change
- keep diffs easy to review
- preserve existing style and naming
- avoid unrelated cleanup
- avoid broad rewrites
- add or update tests when behavior changes
- isolate external services behind adapters where reasonable
- validate structured outputs at boundaries
- handle failure modes explicitly
- document non-obvious decisions briefly

Prefer small, focused modules. A script or module over about 300 lines is a warning
threshold: split it where practical, or explain why keeping it together is clearer.
Do not fragment code artificially just to satisfy a line count.

## AI / ML / LLM Rules

For AI, ML, OCR, VLM, RAG, clustering, extraction, classification, or LLM pipelines:

- keep pipeline stage inputs and outputs explicit
- isolate external model/provider calls
- keep prompt construction separate from provider calls and parsing
- make model names, temperatures, and provider settings explicit
- validate model outputs before downstream use
- handle malformed outputs explicitly
- do not require live API calls for normal unit tests
- use evals or sample cases for prompt/model/retrieval/classification changes
- track prompt/model/config metadata when useful
- do not claim quality improvements without evidence

## Testing and Verification

Use the lightest meaningful verification for the task:

- unit tests for pure logic
- contract tests for interfaces and schemas
- mocked provider tests for external integrations
- eval cases for AI behavior
- integration tests for real provider wiring when explicitly approved
- manual sample runs for prototypes

If tests cannot be run, explain why. If no tests exist, propose the smallest useful
verification path.

## Project Memory

Use `continuity.md` for short-term project state. Update it after non-trivial work when
the current goal, implementation status, next steps, open questions, known issues, or
temporary assumptions changed.

Use `decisions.md` for durable technical decisions. Update it when a lasting direction,
trade-off, dependency, schema/interface convention, prompt/model strategy, or evaluation
strategy is chosen.

Use `context.md` for stable project background. Replace template assumptions with facts
when this template is adopted by a real project.

Keep all three files concise.

Update `README.md` when the way to use this template or project changes.

## Output Formats

Skills provide default output formats.

Use them when they improve clarity, especially for non-trivial planning, implementation,
or review tasks.

Keep the format proportionate:

- for large, risky, or architectural tasks, use the full structure
- for small, local, or obvious tasks, use a compact version
- do not produce long boilerplate just to satisfy a format
- never skip important risks, assumptions, or approval gates for non-trivial changes

## Communication Style

Be direct, specific, and constructive.

Prefer:

- "This is unclear because..."
- "This is risky because..."
- "The smallest useful next step is..."
- "I recommend X because..."
- "I would not do Y yet because..."

Avoid:

- silently accepting vague tasks
- overconfident claims
- large unexplained changes
- unnecessary praise
- hiding uncertainty

