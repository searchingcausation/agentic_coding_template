# Set up your project

## Describe the actual project

Fill in the project name, purpose, users, and boundaries in `ARCHITECTURE.md`.
Describe the actual components, entry points, dependency direction, data flows,
external services, and important failure boundaries as they take shape.
Write your product introduction and development commands in `README.md`.

Create a first durable spec from [the spec template](product-specs/template.md).
Keep acceptance criteria observable. Record consequential design choices using
[the ADR template](design-decisions/template.md); label new proposals honestly.
Specifications and decisions are ready for your project's first records. Completed
task records document template maintenance, not product decisions for your project.

## Connect executable evidence

The included Python helpers validate this harness; Python is not a prescribed
application language. Keep the template checks and extend `Makefile` so `check`
also runs your actual tests, linter, typechecker, and build where applicable.
Name fast offline tests separately from integration/E2E or live evaluation commands.
Do not make standard tests depend on credentials or external network availability.

For example, a TypeScript project might call existing package scripts from Make;
a Python project might call its locked test/lint tools. Discover or choose the
project's actual versions and commands before documenting them. Commit lockfiles
and fixtures where appropriate. There are no dummy build/typecheck targets to
replace here: add those targets only when they perform meaningful checks.

Update the command table in `agent/README.md`. Keep `make check` as the shared local
and CI entry point, and configure any additional toolchain setup in
[the workflow](../.github/workflows/check.yml). Set a GitHub branch ruleset to
require the `harness` check if merges should be blocked; merely committing the
workflow does not enable branch protection.

## Verify tool integration

Open a **new session at the repository root** in each installed tool. Repository
trust and user/organization policy may affect which files and skills can load.

- In Codex, ask it to identify `AGENTS.md`, the shared agreement, and the three
  repository skills. Invoke `$plan-from-spec` on a small planning-only task.
- In Claude Code, check `/memory` for the root instructions and imported agreement,
  then invoke `/plan-from-spec` on the same type of task.
- Confirm both read the matching file in `agent/workflows/` and produce a plan
  without implementation edits. Do not count a structurally valid adapter as proof
  of an actual model's behavior.

The layout follows [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills),
[Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[Claude skills](https://code.claude.com/docs/en/skills), and
[Claude imports](https://code.claude.com/docs/en/memory). Product documentation was
checked on 2026-09-10; recheck it when changing tool integration.

## Run a task end to end

For non-trivial work, copy [the execution-plan template](exec-plans/template.md)
to `docs/exec-plans/active/<task>.md`, or reuse the task's existing plan. Set its spec
reference (or inline one-off spec), risk, authorization state, acceptance criteria,
proposed changes, assumptions/open questions, trade-offs, tasks, and verification.
Before implementation edits, the agent must summarize the proposal and link the
file, including for plain-language requests. Apply the shared authorization rules.
The same plan carries decisions, progress, and next step between sessions.

After implementation and relevant checks, review the diff. For HIGH risk, use a
fresh session for independent review before merge. Record the evidence; move the
plan into `completed/` when finished. Fix links affected by that move, then run
`make check`. Promote only demonstrated, reusable lessons into maintained artifacts.

## Add machinery when it solves an observed problem

Add path-specific instructions when components have different constraints. Add a
hook when a deterministic check needs an earlier event trigger; keep the check in
CI as well. Avoid regex-based shell deny lists presented as security boundaries.
Keep permissions and secrets in appropriate local or managed settings.

Add MCP/native integrations only for needed systems with suitable permissions.
Add agent evals after collecting real repeated tasks; track successful outcomes,
rework, interventions, and cost. Run live evaluations separately and with explicit
cost/data authorization. Do not select default models based on unmeasured claims.
