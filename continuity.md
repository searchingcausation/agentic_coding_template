# continuity.md

## Purpose

Short-term project memory for future agent sessions.

Keep this file concise. It should capture current focus, implementation status, next
steps, open questions, known issues, and temporary assumptions.

## Current Focus

Current goal: maintain a reusable controlled agentic coding template.

Current task: final-response guidance is being updated so agents include a suggested
commit message after making file changes.

Current working mode: Implement

## Project State

Implemented:

- `AGENTS.md` as the central agent governance file
- `README.md` as the human usage guide
- `context.md`, `continuity.md`, and `decisions.md` as concise project memory files
- repo-local workflows under `skills/`
- read-only repo-understanding workflows: `repo-tour` and `grill-me`
- final responses after file changes include a suggested commit message
- no application/runtime scaffold; this repository is documentation/workflow-only

Not implemented:

- project-specific application code
- project-specific architecture context
- project-specific decisions beyond template defaults

Known issues:

- none

## Current Decisions

- Non-trivial changes require a plan and explicit approval before implementation.
- Architecture and long-term design decisions belong to the human.
- Normal unit tests must not require live external API calls. See `decisions.md`.
- After non-trivial work, agents must report whether project memory/docs were updated
  or why no update was needed.
- After file changes, agents must include a suggested commit message in the final
  response.

## Next Steps

- Use the template in real projects and tune strictness based on observed friction.
- Replace template context with project-specific facts when adopted.

## Do Not Change Without Approval

- approval gates
- hard stops for architecture, APIs, schemas, prompts, models, dependencies, tests, and
  infrastructure
- the rule that normal unit tests must not require live external calls
