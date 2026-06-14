# context.md

## Purpose

Stable project context for future agent sessions.

Use `continuity.md` for current status and `decisions.md` for durable decisions.
Replace template assumptions with project-specific facts when adopting this template.

## Project Overview

This repository is a reusable agentic coding template.

When adopted by a real project, replace this section with:

- project purpose
- users or downstream consumers
- domain terminology
- important constraints
- non-goals

## Default Assumptions

Unless project-specific context says otherwise:

- no frontend should be assumed
- no production deployment should be modified
- no new dependencies should be added without approval
- no public interface or schema should be changed without approval
- no prompt or model behavior should be changed without approval
- normal unit tests should not require live external services

## Design Preferences

- Keep inputs, outputs, and pipeline stages explicit.
- Separate orchestration from core logic.
- Isolate external providers behind adapters.
- Keep business logic testable without live external services.
- Prefer small public interfaces and typed data structures where useful.
- Prefer reproducibility, observability, and clear failure handling.
- Avoid premature abstraction, hidden side effects, and broad rewrites.
- Prefer small vertical slices over large unfinished foundations.

## AI / LLM Notes

For LLM/VLM/OCR/model behavior:

- separate prompt construction, provider calls, parsing, validation, and evaluation
- make model/provider configuration explicit
- validate outputs and handle malformed responses
- prefer deterministic settings for extraction, classification, and routing
- do not call a prompt/model change an improvement without evidence

## Non-Goals

Unless explicitly requested, do not assume:

- frontend development
- production deployment
- cloud infrastructure changes
- database migrations
- new dependencies
- major architecture rewrites
- live external API usage in normal tests
