# Execution plans

One Markdown file carries a non-trivial task's proposal, implementation plan, and
the state needed to resume it: assumptions, progress, decisions, failed approaches,
verification, learnings, and next step. Preserve this knowledge here, not only in
chat history.

1. Copy [template.md](template.md) into [active/](active/) using a descriptive name.
2. Fill in the goal/spec, risk, authorization, proposed changes, assumptions/open
   questions, material trade-offs, ordered tasks, and verification. Define the
   desired improvement and evidence, with baselines/targets only where useful;
   label unknowns and proposed targets. Identify affected documentation and read
   relevant existing follow-ups before choosing scope.
3. Before implementation edits, summarize the proposal to the user and link the
   file. Follow the [shared authorization rules](../../agent/README.md).
4. Reuse the file on resumption. Update actual progress and evidence at milestones
   and before handing off. Record and present material scope or approach changes
   before implementing them, keeping the rationale and decision history.
5. Record the outcome against the original criteria, deviations, evidence, and
   limitations. Resolve documentation impact and link genuine deferred work to
   its follow-up entry. Promote confirmed learnings into their durable artifact.
6. Move the plan into [completed/](completed/) when acceptance criteria and required
   reviews are satisfied. Update affected links and run the relevant checks.

Trivial LOW tasks need no plan file unless requested. Non-trivial LOW tasks and all
NORMAL/HIGH tasks require one; see the shared agreement for the distinction.
One-off NORMAL goals can be specified inside the plan. HIGH tasks with independent
review pending stay active and are not merge-ready.

The template ships with empty `active/` and `completed/` directories. Create plans
for actual project work; keep template-maintenance history out of the distributed
starter template.

## Phases and evidence

Use the optional phase table for larger work with distinct deliverables or
dependencies. Each phase names tasks/prerequisites, a visible result, exit evidence,
and any required human decision. A small plan can keep its flat task list.
Passing phase checks allows progress within existing authorization; it does not
require permission after every phase.

Record task-specific stop/replanning conditions. Pause affected work when a material
requirement is unresolved or the next action exceeds authorization; continue useful
independent work. If the same failure repeats without new evidence, revisit the
diagnosis and record the new hypothesis. An unavailable dependency or unrun required
check stays explicit and pending, rather than being counted as passed.

Keep detailed results in the verification table and a short readable `Outcome` at
handoff or completion. Compare delivery with the original acceptance criteria and
explain deviations. Longer-term product measures need their own follow-up evidence;
technical completion alone does not demonstrate them.

## Documentation impact

Identify affected specs, architecture, usage guides, or ADRs during planning. At
closure, check the actual diff and link the updated documents or explain why an
artifact is unchanged. Document supported behavior accurately; retain proposed
labels for undelivered behavior. Internal refactors need no artificial spec edits.
Reviewers assess the spec and diff before auditing the implementer's plan.

## Follow-ups and backlog

Create `docs/backlog.md` only when a genuine deferred item appears. If the project
already uses an issue tracker, link its existing entries instead of maintaining a
duplicate list; external writes still need applicable authorization. A backlog
entry is a record of work, not authorization to implement it.

Use this format in the backlog, with links relative to that file:

| ID / task | Impact / reason deferred | Source plan | Revisit trigger / owner | Status / resolution |
| --- | --- | --- | --- | --- |
| <Stable ID and short description> | <Why it matters and falls outside this delivery> | <Link to discovery and decision context> | <Concrete trigger; owner if known> | <Open, scheduled, done, or dropped; link to implementing plan or decision> |

When planning work in an area, read its relevant entries. If one is selected, link
it from the new plan, mark it scheduled, and update its status and resolution when
finished. Link each entry from its source plan as well, so the history is navigable
in both directions. Update source and resolution links when plans move to completed.

Required acceptance work remains in the active plan. Moving it to a backlog cannot
make the original task complete; changes to agreed scope must be explicit and
authorized. Record separately scoped improvements and later product measurements
with their revisit trigger. Do not create speculative tasks merely to fill a list.
