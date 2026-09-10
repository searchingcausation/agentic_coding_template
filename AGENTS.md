# Codex repository entry point

Read [the shared working agreement](agent/README.md) before working in this repository.
It is the canonical source for risk tiers, authorization boundaries, commands,
workflow routing, and completion criteria. User instructions take precedence over
repository defaults, within system and tool permissions.

- [README](README.md): usage and repository map.
- [Architecture](ARCHITECTURE.md): current components and invariants.
- [Documentation](docs/README.md): specs, decisions, and execution plans.
- [Active work](docs/exec-plans/active/): resume the relevant task, not every task.
- Run `make check` from the repository root for the template's required checks.

Codex skills live in `.agents/skills/`. Load the relevant workflow on demand:
`$plan-from-spec`, `$debug-fix`, or `$independent-review`.
For review, establish the spec and diff scope before reading implementation plans.
