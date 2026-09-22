# Agentic Coding Template

A reusable engineering workspace for **Codex and Claude Code**. One shared set of
instructions, three focused workflows, and executable checks support the cycle:

**Specify → explore → plan → implement → verify → review → learn.**

The template is stack-neutral. Project specifications, architecture decisions, and
task records start empty, ready for your project.

## Quick start

1. Create a project from this template, including its hidden directories.
2. Run `make setup` and `make check` with Python 3.11+ installed.
3. Follow [Set up your project](docs/adopting.md) to add project context and commands.
4. Open the repository in Codex or Claude Code and describe the desired outcome.

```sh
make setup
make check
```

The helper scripts use the Python standard library. Make is optional:

```sh
python3 agent/scripts/check_harness.py
python3 -m unittest discover -s agent/tests -v
```

On systems that expose Python 3 as `python`, use that command or
`make PYTHON=python check`.

## Work with an agent

| What you need | Codex | Claude Code |
| --- | --- | --- |
| A plan grounded in the spec and repository | `$plan-from-spec` | `/plan-from-spec` |
| A reproduced and verified bug fix | `$debug-fix` | `/debug-fix` |
| A review from fresh context | `$independent-review` | `/independent-review` |

You can also describe a task in plain language. Both tools use
[the shared working agreement](agent/README.md); skill details load when relevant.

Before every non-trivial change, the agent saves a Markdown proposal in
`docs/exec-plans/active/<task>.md` and presents it with a link before implementation.
It includes the understood goal, proposed changes, assumptions/open questions,
material trade-offs, and ordered tasks with verification. The same file records
progress and decisions, then moves to `completed/` when finished. This also applies
without invoking a skill. Trivial corrections need no plan unless requested.
Already authorized implementation can proceed after presenting the proposal;
planning-only requests and HIGH-risk work retain their approval boundaries.

The proposal defines the intended improvement and how to verify it, using measured
baselines and targets where useful. Larger tasks have phases with visible outcomes
and exit checks; small plans keep a flat task list. At handoff or completion, the
same Markdown file records results against the original criteria, deviations,
documentation updates, and limitations. Genuine deferred work goes into an
on-demand backlog or existing tracker with a source link and revisit trigger;
unfinished acceptance work remains in the active plan. See the
[execution-plan guide](docs/exec-plans/README.md) for the lifecycle and formats.

For a feature, give the agent a goal, constraints, and observable acceptance criteria.
For a bug, describe expected and actual behavior plus a reproduction. For a review,
provide the spec and a precise diff scope in a fresh session.

```text
Plan this feature:
Users can cancel an export while it is running.
Preserve completed files and the existing public API.
Acceptance: cancellation stops new work and reports a cancelled status.
Inspect the repository and save an implementation plan. Do not implement yet.
```

After reviewing the plan, ask the agent to implement it. To resume a task, point it
to that task's file in `docs/exec-plans/active/`.
Whenever a response includes repository file changes, the agent provides a copyable
English commit-message suggestion, including for small edits and partial handoffs.
Committing, amending commits, and pushing require an explicit request.

## Match the process to the risk

| Risk | Typical change | Process |
| --- | --- | --- |
| LOW | Local, reversible correction | Explore → proposal if non-trivial → implement → relevant checks. |
| NORMAL | Feature or substantial bug fix | Spec → explore and check external docs → save and present proposal → implement → verify. |
| HIGH | Architecture, security, public contract, migration | NORMAL plus human plan review and fresh independent review before merge. |

Risk comes from the consequences of a mistake. Small tasks stay lightweight;
consequential decisions and external actions have explicit authorization boundaries.
See the [working agreement](agent/README.md) for the full rules.

## Find the right artifact

| Artifact | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md) | Tool entry points |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Current system map and project architecture outline |
| [agent/README.md](agent/README.md) | Shared commands, rules, and completion criteria |
| [agent/workflows/](agent/workflows/) | Canonical planning, debugging, and review procedures |
| [docs/product-specs/](docs/product-specs/) | What the project should do |
| [docs/design-decisions/](docs/design-decisions/) | Why a technical direction was chosen |
| [docs/exec-plans/](docs/exec-plans/) | How to carry out and resume a task |
| [agent/scripts/](agent/scripts/) and [agent/tests/](agent/tests/) | Offline checks and their regression suite |
| [.github/workflows/](.github/workflows/) | CI using the same local check command |

The three skills have thin adapters under `.agents/skills/` and `.claude/skills/`.
Shared workflow behavior is maintained once in `agent/workflows/`.

## Verification

`make check` validates the harness structure, local documentation links, shared
workflow references, skill metadata, helper syntax, and regression tests. During
project setup, extend it with your actual application tests, linting, typecheck,
and build. The included checks establish the integrity of the template itself.

## Design principles

[The design guide](docs/principles.md) explains the report-based approach:
progressive disclosure, task-local continuity, risk-proportional planning, closed
feedback loops, and promotion of demonstrated lessons into tests or other assets.
The complete [background report](docs/references/agentic-engineering-playbook.pdf)
is included for reference and can be read when needed.
