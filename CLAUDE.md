# Claude Code repository entry point

The shared working agreement below is the canonical source for repository rules,
commands, workflow routing, and completion criteria.

@agent/README.md

Read [the architecture](ARCHITECTURE.md) and [relevant documentation](docs/README.md)
as needed. Claude Code skills live in `.claude/skills/`: `/plan-from-spec`,
`/debug-fix`, and `/independent-review`. Load workflow details only when relevant.
For review, establish the spec and diff scope before reading implementation plans.
