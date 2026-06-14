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
