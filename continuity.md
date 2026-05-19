# continuity.md

## Purpose

This file is short-term project memory for future agent sessions.

It should answer:

- what is currently being worked on
- what is already implemented
- what is not implemented
- what decisions currently matter
- what the next steps are
- what should not be changed without approval

Keep this file concise and current.

## Current Focus

Current goal: establish a reusable controlled agentic coding template.

Current task: initial template files have been created.

Current working mode: Implement

## Current Project State

Implemented:

- agent governance file: `AGENTS.md`
- human usage guide: `README.md`
- project memory files: `continuity.md`, `decisions.md`, `context.md`
- repo-local workflow instructions under `skills/`

Not implemented:

- project-specific application code
- project-specific architecture context
- project-specific decisions beyond template defaults

Partially implemented:

- none

Known issues:

- none

## Current Architecture

High-level structure:

```text
repo/
  AGENTS.md
  README.md
  continuity.md
  decisions.md
  context.md
  skills/
    clarify/
    plan/
    implement/
    review/
```

Important modules:

- none yet

Main entry points:

- none yet

Important configs:

- `AGENTS.md`
- `context.md`
- `decisions.md`

Important tests/evals:

- none yet

## Current Interfaces / Contracts

Public functions/classes:

- none yet

Input schemas:

- none yet

Output schemas:

- none yet

Config contracts:

- none yet

External APIs/providers:

- none yet

## Current AI / ML / LLM Behavior

Relevant only when this template is adopted by a project with AI/ML/LLM components.

Prompts:

- none yet

Models/providers:

- none yet

Evaluation:

- none yet

Open eval gaps:

- define project-specific eval strategy when AI behavior is introduced

## Current Decisions

- Normal unit tests must not require live external API calls. See `decisions.md`.
- Non-trivial changes require a plan and explicit approval before implementation.
- Architecture and long-term design decisions belong to the human.

## Open Questions

- Replace template context with project-specific facts when this template is adopted.

## Next Steps

- Review the initial template contents.
- Adjust the strictness and wording based on real usage.
- Fill `context.md` with project-specific facts in each new project.

## Do Not Change Without Approval

- architecture rules
- approval gates
- public API/schema/prompt/model behavior rules
- testing rule that normal unit tests must not require live external calls

