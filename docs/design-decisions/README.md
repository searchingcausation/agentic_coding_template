# Design decisions

Record consequential choices with their context, realistic alternatives, decision,
and consequences. Describe the current system in [the architecture](../../ARCHITECTURE.md).

Copy [template.md](template.md) to `NNNN-short-title.md` when a choice deserves a
lasting explanation. Mark proposed decisions as proposed until accepted. When a
decision changes, link its replacement so the reasoning remains understandable.

Create the first decision record when selecting your project's technical direction.
Use the [initial architecture clarification](../adopting.md#clarify-the-initial-architecture)
to ground it in requirements and constraints. Distinguish system/deployment
structure, code organization, and dependency rules; compatible choices can share
one initial ADR when their rationale belongs together. Record material assumptions
and what evidence or requirement changes would trigger revisiting the decision.
A provisional direction may retain unknowns; keep its status honest and apply the
[authorization rules](../../agent/README.md#authorization) before implementation.
