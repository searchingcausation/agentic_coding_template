# decisions.md

## Purpose

This file records durable technical decisions that future agents should not accidentally
reverse.

Use this file for decisions such as:

- architecture choices
- dependency decisions
- schema or interface conventions
- evaluation strategy
- prompt/model strategy
- testing strategy
- provider abstraction choices
- deployment assumptions

## Decision Template

```md
## YYYY-MM-DD: <Decision Title>

Status: proposed / accepted / superseded

### Decision

...

### Reason

...

### Consequences

Positive:

- ...

Negative / trade-offs:

- ...

### Alternatives Considered

1. ...
2. ...

### Follow-up

- ...
```

## Decisions

## 2026-05-19: Unit tests must not require live external API calls

Status: accepted

### Decision

Normal unit tests must not require live calls to LLM, OCR, VLM, database, cloud, or
other external providers.

External calls should be mocked in unit tests. Live calls may be used in explicit
integration tests, manual scripts, or eval runs.

### Reason

Live external calls are slower, more expensive, less deterministic, harder to run in CI,
and more likely to fail due to credentials, rate limits, or network issues.

### Consequences

Positive:

- faster local development
- more stable tests
- easier CI
- lower cost

Negative / trade-offs:

- requires mocks or fixtures
- integration issues need separate coverage

### Alternatives Considered

1. Allow live calls in all tests. Rejected because it makes tests slow, flaky, and costly.
2. Avoid tests for provider logic. Rejected because parsing, validation, and failure
   handling still need coverage.

### Follow-up

- Add integration tests only where they provide clear value.
- Make live tests opt-in.

