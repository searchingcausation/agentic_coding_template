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
- `skills/repo-tour/SKILL.md`: explore an unfamiliar repo without editing files
- `skills/grill-me/SKILL.md`: test and strengthen your understanding of a repo
- `skills/plan/SKILL.md`: plan non-trivial work before implementation
- `skills/implement/SKILL.md`: implement approved plans or small safe changes
- `skills/review/SKILL.md`: review diffs, scope, risks, and verification

## How To Use

At the start of a new agent session, ask the agent to read:

```text
Read AGENTS.md, continuity.md, context.md, and the relevant workflow file in skills/.
```

For a new or unfamiliar repo:

```text
Use skills/repo-tour/SKILL.md. Do not edit files.
Map the repo and explain the main execution path.
```

To check your understanding:

```text
Use skills/grill-me/SKILL.md. Do not edit files.
Ask one question at a time about architecture, data flow, entry points, tests, and failure modes.
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
2. Explore the repo when the codebase is unfamiliar.
3. Test understanding when the mental model is uncertain.
4. Plan the smallest useful vertical slice.
5. Ask for explicit approval.
6. Implement only the approved scope.
7. Review the result.
8. Update or explicitly skip project memory/docs.

Small, low-risk changes can be made directly when the task is clear, but they should
be mentioned in the final response.

## Template Maintenance

Keep `AGENTS.md` as the source of truth. Keep the other files short and project-specific.

Update:

- `continuity.md` for current project state and next steps
- `decisions.md` for durable decisions
- `context.md` for stable background and assumptions
- `README.md` when usage or workflow changes
