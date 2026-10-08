# Set up your project

## Describe the actual project

Start with [the project-scoping template](project-scope.template.md), copied to
`docs/project-scope.md`. Capture the problem, users, evidence, proposed approach,
MVP boundaries, dependencies, and the first uncertainty to validate. Keep it brief;
use its optional AI questions only if the product itself uses AI. Revisit the scope
when evidence changes the project's direction.

Fill in the project name, purpose, users, and boundaries in `ARCHITECTURE.md`.
Describe the actual components, entry points, dependency direction, data flows,
external services, and important failure boundaries as they take shape.
Write your product introduction and development commands in `README.md`.

Translate the relevant scope into a first durable spec using
[the spec template](product-specs/template.md). The scope explains project direction;
specs define detailed behavior, and execution plans organize implementation work.
Link detailed records from the scope as they appear instead of duplicating them.
Keep acceptance criteria observable. Record consequential design choices using
[the ADR template](design-decisions/template.md); label new proposals honestly.
Define the user/operator outcome and its evidence in the spec. Add measurement
methods, baselines, targets, limits, and decision thresholds where meaningful.
Mark unknown baselines and plan their measurement; qualitative tasks need no
invented numbers. Keep later product measures separate from delivery acceptance
and give them a follow-up trigger or owner.
Specifications, decisions, and task directories are ready for your project's first
records. The template includes reusable guidance and templates without pre-filled
task history.

## Clarify the initial architecture

Before the first implementation that establishes structural boundaries, choose
an initial architectural direction from the project scope and first relevant spec.
For an existing project, inspect its code, deployment, and decisions first;
describe the actual architecture and work within it unless a change is justified
by the task. For a new project, clarify the constraints before scaffolding fixes
the structure implicitly.

Use the questions that materially affect the decision:

- What are the core workflows, domain areas, and external integrations?
- Who develops and operates the system, and what delivery or operating limits apply?
- What data, consistency, security, availability, and scaling requirements are known?
- Do parts need independent development, deployment, or scaling? What evidence
  supports those needs, and what remains an assumption?

Separate compatible decision dimensions instead of treating all architecture
patterns as mutually exclusive alternatives:

| Dimension | Examples | Decision to explain |
| --- | --- | --- |
| System and deployment structure | Monolith, modular monolith, microservices | Which parts run and deploy together, and why? |
| Code organization | By technical layer, by feature or domain | Where does related code live, and what are the module boundaries? |
| Dependency rules | Layered, hexagonal, Clean Architecture | Which components may depend on which others, and where are external systems isolated? |

For example, a modular monolith can organize code by feature and use layers inside
each module. These examples are orientation, not a required menu or a default
architecture. Compare only a few plausible options, explain their material costs
and benefits, and recommend the simplest structure that meets the known needs.
Match the depth to the project: a small application may need only a few paragraphs.
Ask the user about unresolved constraints when answers would materially change
the choice. Apply the existing [authorization rules](../agent/README.md#authorization)
to consequential decisions before implementation.

Record rationale, alternatives, assumptions, decision status, and revisit triggers
in an [ADR](design-decisions/template.md). A provisional direction is valid when
its uncertainties are explicit; do not mark a proposal accepted without evidence.
Describe the chosen structure, module boundaries, and allowed dependencies in
`ARCHITECTURE.md`, keeping it accurate as implementation takes shape. Revisit the
direction when evidence or requirements change, rather than deciding every future
architectural detail at setup.

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

Read relevant backlog/tracker entries when choosing task scope. Larger plans can
use phases with deliverables, prerequisites, exit evidence, and any required human
decision; small plans can stay flat. Continue within authorization after phase
checks. Record unresolved requirements or unavailable checks and continue useful
independent work. Identify affected documentation while planning.

After implementation and relevant checks, review the diff. For HIGH risk, use a
fresh session for independent review before merge. Resolve documentation impact
with links to updated artifacts or reasons unchanged. Write an outcome comparing
delivery with the original criteria, including deviations, evidence, and limitations.
Use the [follow-up lifecycle](exec-plans/README.md#follow-ups-and-backlog) for genuine
deferred items; create `docs/backlog.md` only when needed, or use the existing
tracker. Required acceptance work remains in the active plan.

Move the plan into `completed/` when its criteria and required reviews are satisfied.
Fix links affected by that move, including backlog references, then run `make check`.
Promote only demonstrated, reusable lessons into maintained artifacts.

## Add machinery when it solves an observed problem

Add path-specific instructions when components have different constraints. Add a
hook when a deterministic check needs an earlier event trigger; keep the check in
CI as well. Avoid regex-based shell deny lists presented as security boundaries.
Keep permissions and secrets in appropriate local or managed settings.

Add MCP/native integrations only for needed systems with suitable permissions.
Add agent evals after collecting real repeated tasks; track successful outcomes,
rework, interventions, and cost. Run live evaluations separately and with explicit
cost/data authorization. Do not select default models based on unmeasured claims.
