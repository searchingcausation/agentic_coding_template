# Plan from spec

Use for a requested implementation plan or a substantial task whose approach is
still unresolved. Produce a plan that another session can implement. This workflow
may create/update planning documents; it does not change implementation files.

## Establish the contract

Read the shared agreement, relevant architecture, and supplied spec. If there is
only a goal, capture observable acceptance criteria, constraints, and non-goals.
Define the desired user/operator improvement and its evidence. Where useful,
record baseline, target, measurement method, limits, and decision thresholds.
Label unknown baselines and add a measurement task; proposed targets are not user
requirements. Qualitative outcomes need no invented numbers. Separate delivery
acceptance from later product outcomes and name their follow-up trigger or owner.
Ask only questions that block a useful plan. Record assumptions explicitly.
Choose LOW/NORMAL/HIGH from consequences. Do not create a plan file for a trivial
task unless the user requests one.

Inspect the actual entry points, callers, tests, and affected contracts before
choosing an approach. Cite paths. Separate repository evidence from inference.
Read relevant entries in the project's existing backlog or tracker. Link selected
items into the plan without treating the backlog itself as authorization.

## Check external assumptions

For external, version-sensitive APIs, frameworks, SDKs, or services:

1. Identify the repository's exact version from its lockfile, manifest, runtime,
   or infrastructure configuration. If no exact version is established, say so.
2. Read official documentation for that version; for upgrades, also read the
   migration guide/changelog. Record version, source, access date, and implication.
3. Preserve existing versions unless the task requires or authorizes an upgrade.

Local business logic supported by code/tests does not need a web search. If needed
documentation is unavailable, record the uncertainty and avoid depending on an
unverified API; ask if that uncertainty prevents a safe approach.

## Make the plan concrete

Use [the execution-plan template](../../docs/exec-plans/template.md). Keep one file
in `docs/exec-plans/active/` with goal/spec reference, risk and authorization state,
proposed changes and their rationale, explicit assumptions/open questions, affected
paths, ordered proposed tasks with dependencies and expected outcomes, verification
tied to each acceptance criterion, rollback when relevant, and a next step.
Reuse an existing task plan when resuming; preserve its decisions and rationale.

For larger work with distinct deliverables/dependencies, group tasks into phases
with visible results, prerequisites, exit evidence, and any required human decision.
Small plans can stay flat. Record relevant stop/replanning conditions while keeping
normal progress within existing authorization. Identify likely documentation impact
and the evidence needed to resolve it at closure. Use the execution-plan guide's
follow-up lifecycle for genuine deferred work; acceptance blockers stay in scope
unless an explicit, authorized scope change resolves them.

For each material trade-off, state realistic alternatives, relevant pros/cons,
your recommendation, and why it fits this repository. If there is no material
trade-off, say so without inventing alternatives.

Identify API/data/schema changes and relevant compatibility or security constraints.
Keep a task-specific spec in the plan when sufficient; put durable product behavior
in [product specs](../../docs/product-specs/README.md). Do not present proposals as
accepted decisions or write an acceptance on the user's behalf.

## Hand off

Present the proposal with a link to the Markdown file, summarizing intended changes,
assumptions, material trade-offs, proposed tasks, and outstanding decisions. This
must happen before implementation edits, as required by the shared agreement for
every non-trivial change. Honor a planning-only request.
HIGH work without an approved approach needs human plan
review before implementation. Existing approval remains valid for its scope; a
plan-only skill does not revoke it or require it to be repeated.
