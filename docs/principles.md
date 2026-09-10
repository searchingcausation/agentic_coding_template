# Engineering principles

This template follows the approach described in
[Agentic Engineering mit Codex & Claude Code](references/agentic-engineering-playbook.pdf):
make the repository understandable, make feedback executable, and keep engineering
work resumable.

## A repository the agent can navigate

Small tool entry points lead to a shared working agreement and a documentation
map. Load detailed workflow or component guidance only when relevant. Keep product
behavior, current architecture, decision rationale, and temporary task state in
separate artifacts with clear ownership.

## Process proportional to consequences

A small reversible correction needs inspection and verification. Substantial work
needs an explicit outcome and a concrete plan. Architecture, security, migrations,
and public contracts need deeper human and independent review. Risk is about the
cost of a mistake rather than the size of the diff.

## Plans grounded in evidence

Inspect actual code, callers, tests, and interfaces. For external, version-sensitive
behavior, establish the version and read official documentation before relying on
an API. Make material trade-offs and the verification strategy visible.

## Closed feedback loops

An agent needs to observe the effects of its work. Give it runnable tests, linting,
typechecks, builds, E2E checks, screenshots, or logs appropriate to the system. For a
bug, demonstrate the failure before fixing it and retain a meaningful regression.
Keep local and CI commands aligned.

## Independent review

Review the specification and change in fresh context before consulting the
implementation plan. Check behavior, compatibility, security, operability, and
scope. Passing tests are evidence alongside these other constraints.

## Durable task state

Keep a substantial task's plan and continuity in one file. Record progress and
failed approaches so another session can resume efficiently. At completion,
promote confirmed reusable lessons into documentation, tests, linters, workflows,
or other appropriate assets.

## Grow from demonstrated need

Start with planning, debugging, and review workflows. Add component rules when
components have different constraints; hooks when a check needs an event trigger;
integrations when an agent needs a particular external system; and evals when real
repeated tasks justify comparing agent behavior. Keep the application stack and
model selection project-specific.

## Report references

| Topic | Report pages |
| --- | --- |
| Navigability and progressive disclosure | 2–5, 9 |
| Knowledge structure and execution plans | 3–4, 9 |
| Risk tiers and task lifecycle | 6–9 |
| Version-sensitive documentation | 7 |
| Regression tests and verification | 7–8 |
| Review and three core skills | 8–10 |
| Deterministic enforcement and integrations | 10–11 |
| Evals and iterative improvement | 12–15 |

Page numbers refer to the [included PDF](references/agentic-engineering-playbook.pdf).
Read it when background is useful; the repository's working agreement and workflows
provide the instructions for everyday tasks.
