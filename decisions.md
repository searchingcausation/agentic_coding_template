# decisions.md

## Purpose

Durable technical decisions that future agents should not accidentally reverse.

Use this file for lasting decisions about architecture, dependencies, schemas,
interfaces, evaluation strategy, prompt/model strategy, testing strategy, provider
abstractions, or deployment assumptions.

## Entry Format

```md
## YYYY-MM-DD: <Decision Title>

Status: proposed / accepted / superseded

Decision:

Reason:

Consequences:
```

## Decisions

## 2026-07-08: Use native Claude Code integration

Status: accepted

Decision:

`CLAUDE.md` is the single source of truth for agent rules and is loaded automatically by
Claude Code. Workflow skills live in `.claude/skills/` so Claude Code discovers them as
native skills. `CLAUDE.md` imports
`continuity.md` and `context.md`. A read-only command allowlist lives in
`.claude/settings.json`.

Reason:

The template targets Claude Code. Native placement makes skills invocable and
auto-triggerable, removes the manual "read these files" session ritual, and cuts
approval prompts for safe read-only commands.

Consequences:

- Skills are invocable as slash commands (`/plan`, `/review`, ...).
- Session context loads automatically via imports; keep imported files concise.
- The template targets Claude Code only; no cross-tool `AGENTS.md` pointer is kept.
- Enforcement hooks and subagents remain optional, per-project choices.

## 2026-05-19: Unit tests must not require live external API calls

Status: accepted

Decision:

Normal unit tests must not require live calls to LLM, OCR, VLM, database, cloud, or
other external providers. External calls should be mocked in unit tests. Live calls may
be used in explicit integration tests, manual scripts, or eval runs.

Reason:

Live external calls are slower, more expensive, less deterministic, harder to run in CI,
and more likely to fail due to credentials, rate limits, or network issues.

Consequences:

- Local development and CI stay faster, cheaper, and more stable.
- Provider wiring still needs separate opt-in integration coverage where useful.
