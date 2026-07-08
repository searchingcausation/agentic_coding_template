# Agentic Coding Template

A reusable template for controlled AI-assisted coding.

The template is intentionally conservative: small steps, explicit approval for
non-trivial changes, and no silent architecture decisions. The human owns long-term
direction; agents help with clarification, planning, implementation, debugging,
documentation, and review.

## Files

- `CLAUDE.md`: central agent rules, approval gates, hard stops, and memory rules
  (loaded automatically by Claude Code)
- `AGENTS.md`: thin pointer to `CLAUDE.md` for other agent tools
- `context.md`: stable project background and assumptions
- `continuity.md`: short-term project memory
- `decisions.md`: durable technical decisions
- `.claude/skills/clarify/`: clarify vague, risky, broad, or underspecified work
- `.claude/skills/repo-tour/`: explore an unfamiliar repo without editing files
- `.claude/skills/grill-me/`: test and strengthen your understanding of a repo
- `.claude/skills/plan/`: plan non-trivial work before implementation
- `.claude/skills/implement/`: implement approved plans or small safe changes
- `.claude/skills/review/`: review diffs, scope, risks, and verification
- `.claude/settings.json`: read-only command allowlist to reduce approval prompts

## How To Use

Claude Code loads `CLAUDE.md` automatically, and `CLAUDE.md` imports `continuity.md`
and `context.md`. So the session starts with the rules and current state already in
context — no manual "read these files" step is needed.

The workflows in `.claude/skills/` are native skills. Invoke them as slash commands, or
just describe the task and let Claude route to the right one.

For a new or unfamiliar repo:

```text
/repo-tour
Map the repo and explain the main execution path. Do not edit files.
```

To check your understanding:

```text
/grill-me
Ask one question at a time about architecture, data flow, entry points, tests, and failure modes.
```

For unclear work:

```text
/clarify
My goal is: ...
```

For non-trivial implementation:

```text
/plan
Create a small implementation plan and wait for my explicit approval.
My goal is: ...
```

After approving a plan:

```text
/implement
Implement only the approved vertical slice. Keep the diff small.
Report whether continuity.md, decisions.md, context.md, or README.md needed updates.
```

For review:

```text
/review
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
9. Include a suggested commit message after file changes.

Small, low-risk changes can be made directly when the task is clear, but they should
be mentioned in the final response.

## Template Maintenance

Keep `CLAUDE.md` as the source of truth (`AGENTS.md` only points to it). Keep the other
files short and project-specific.

Update:

- `continuity.md` for current project state and next steps
- `decisions.md` for durable decisions
- `context.md` for stable background and assumptions
- `README.md` when usage or workflow changes
