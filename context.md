# context.md

## Purpose

This file contains stable project context.

It is not for current task status. Use `continuity.md` for current status and
`decisions.md` for durable decisions.

This template is optimized for backend, data, AI, ML, and LLM-heavy projects. Replace
template assumptions with project-specific facts when adopting it.

## Project Overview

This repository is currently a reusable agentic coding template.

When adopted by a real project, replace this section with:

- project purpose
- users or downstream consumers
- domain terminology
- important constraints
- non-goals

## Default Project Assumptions

Unless project-specific context says otherwise:

- no frontend should be assumed
- no production deployment should be modified
- no new dependencies should be added without approval
- no public interface should be changed without approval
- no schema should be changed without approval
- no prompt or model behavior should be changed without approval
- no normal unit test should require live external services

## Architecture Principles

- Keep pipeline stages explicit.
- Keep inputs and outputs clear.
- Separate orchestration from core logic.
- Isolate external providers behind adapters.
- Keep business logic testable without live external services.
- Prefer small public interfaces.
- Prefer typed data structures where useful.
- Prefer reproducibility and observability.
- Avoid premature abstraction.
- Avoid hidden side effects.
- Prefer small vertical slices over large unfinished foundations.

## Common AI / LLM Pipeline Shape

Typical backend AI pipeline:

```text
input
  -> validation
  -> loading
  -> preprocessing
  -> model / LLM / OCR / retrieval step
  -> parsing
  -> validation
  -> postprocessing
  -> evaluation
  -> output / storage
```

Not every project needs every stage.

## Common Concerns

For AI/ML/LLM projects, consider:

- input quality
- schema stability
- prompt versioning
- model/provider configuration
- output validation
- malformed model outputs
- reproducibility
- cost
- latency
- observability
- evaluation
- regression testing
- data privacy
- secrets handling

## Coding Conventions

Prefer:

- readable, explicit code
- clear module boundaries
- focused files and functions
- typed signatures where useful
- dataclasses, Pydantic, or TypedDict where useful
- configuration for environment-specific settings
- tests for pure logic
- mocks for external services

Avoid:

- hardcoded secrets
- hardcoded absolute local paths
- giant functions or scripts
- hidden network calls
- broad exception swallowing
- global mutable state
- unclear dictionaries passed across many boundaries
- unversioned prompt changes
- silent schema changes

Scripts or modules over about 300 lines should be treated as a warning sign. Split them
where practical, or explain why the larger file is clearer.

## Testing Philosophy

Use the lightest meaningful test.

- Unit tests for pure logic.
- Contract tests for schemas and interfaces.
- Integration tests for provider wiring.
- Eval cases for AI behavior.
- Manual sample runs for early prototypes.

Do not require live external API calls for normal unit tests.

## AI Behavior Philosophy

For LLM/VLM/OCR/model behavior:

- validate outputs
- expect malformed responses
- prefer deterministic settings for extraction, classification, and routing
- track prompt/model/config metadata when useful
- do not call a prompt/model change an improvement without evaluation
- separate prompt construction from API calling
- separate API calling from output parsing
- separate parsing from evaluation

## Non-Goals

Unless explicitly requested, do not assume:

- frontend development
- production deployment
- cloud infrastructure changes
- database migrations
- new dependencies
- major architecture rewrites
- broad refactoring
- live external API usage in tests

