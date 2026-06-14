# Agentic Coding Template

A reusable template for controlled AI-assisted coding.

The template is intentionally conservative: small steps, explicit approval for
non-trivial changes, and no silent architecture decisions. The human owns long-term
direction; agents help with clarification, planning, implementation, debugging,
documentation, and review.

## Files

- `AGENTS.md`: central agent rules, approval gates, hard stops, and memory rules
- `context.md`: stable project background and assumptions
- `continuity.md`: short-term project memory
- `decisions.md`: durable technical decisions
- `skills/clarify/SKILL.md`: clarify vague, risky, broad, or underspecified work
- `skills/plan/SKILL.md`: plan non-trivial work before implementation
- `skills/implement/SKILL.md`: implement approved plans or small safe changes
- `skills/review/SKILL.md`: review diffs, scope, risks, and verification

## How To Use

At the start of a new agent session, ask the agent to read:

```text
Read AGENTS.md, continuity.md, context.md, and the relevant workflow file in skills/.
```

For unclear work:

```text
Use skills/clarify/SKILL.md first. Do not code yet.
My goal is: ...
```

For non-trivial implementation:

```text
Use skills/plan/SKILL.md.
Create a small implementation plan and wait for my explicit approval.
My goal is: ...
```

After approving a plan:

```text
Use skills/implement/SKILL.md.
Implement only the approved vertical slice.
Keep the diff small.
Report whether continuity.md, decisions.md, context.md, or README.md needed updates.
```

For review:

```text
Use skills/review/SKILL.md.
Review the current diff critically for correctness, scope creep, and missing verification.
```

## Workflow

For non-trivial changes:

1. Clarify the goal.
2. Plan the smallest useful vertical slice.
3. Ask for explicit approval.
4. Implement only the approved scope.
5. Review the result.
6. Update or explicitly skip project memory/docs.

Small, low-risk changes can be made directly when the task is clear, but they should
be mentioned in the final response.

## Template Maintenance

Keep `AGENTS.md` as the source of truth. Keep the other files short and project-specific.

Update:

- `continuity.md` for current project state and next steps
- `decisions.md` for durable decisions
- `context.md` for stable background and assumptions
- `README.md` when usage or workflow changes
