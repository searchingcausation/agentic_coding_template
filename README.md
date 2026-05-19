# Agentic Coding Template

This repository is a reusable template for controlled AI-assisted coding.

It is designed for projects where the human owns architecture and long-term technical
direction, while agents help with clarification, planning, implementation, debugging,
documentation, and review.

The default posture is intentionally conservative: small steps, explicit plans, and no
silent architecture decisions.

## Files

- `AGENTS.md`: agent rules, approval gates, hard stops, and workflow routing
- `context.md`: stable project background and reusable AI/LLM project assumptions
- `continuity.md`: short-term project memory for future agent sessions
- `decisions.md`: durable technical decisions
- `skills/clarify/SKILL.md`: workflow for vague, risky, broad, or underspecified tasks
- `skills/plan/SKILL.md`: workflow for non-trivial planning before implementation
- `skills/implement/SKILL.md`: workflow for approved implementation work
- `skills/review/SKILL.md`: workflow for critical review and scope checks

## How To Use

At the start of a new agent session, ask the agent to read:

```text
Read AGENTS.md, continuity.md, context.md, and the relevant workflow file in skills/.
```

For unclear work:

```text
Use skills/clarify/SKILL.md first.
Do not code yet.

My goal is: ...
```

For planning:

```text
Use skills/plan/SKILL.md.
Create a small implementation plan.
Do not code yet.
Wait for my explicit approval.

My goal is: ...
```

For implementation after approval:

```text
Use skills/implement/SKILL.md.
Implement only the approved vertical slice.
Keep the diff small.
Update continuity.md afterwards if the project state changed.
```

For review:

```text
Use skills/review/SKILL.md.
Review the current diff critically.
Check for scope creep, silent behavior changes, and missing tests.
```

## Workflow

For non-trivial changes:

1. Clarify the goal.
2. Plan the smallest useful vertical slice.
3. Ask for explicit approval.
4. Implement only the approved scope.
5. Review the result.
6. Update project memory when needed.

Small, low-risk changes can be made directly when the task is clear, but they should be
mentioned in the final response.

## Small Vertical Slices

Prefer the smallest end-to-end change that produces observable value and can be reviewed,
tested, and adjusted before expanding scope.

For example, in an LLM pipeline, prefer one sample input that produces one validated
output over building every abstraction layer upfront.

## Template Maintenance

Update `continuity.md` after non-trivial work when project state, next steps, open
questions, known issues, or temporary assumptions changed.

Update `decisions.md` when a durable technical decision is made.

Update `context.md` when stable project background changes.

Update this `README.md` when the way to use the template or project changes.
