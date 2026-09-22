# Execution plans

One Markdown file carries a non-trivial task's proposal, implementation plan, and
the state needed to resume it: assumptions, progress, decisions, failed approaches,
verification, learnings, and next step. Preserve this knowledge here, not only in
chat history.

1. Copy [template.md](template.md) into [active/](active/) using a descriptive name.
2. Fill in the goal/spec, risk, authorization, proposed changes, assumptions/open
   questions, material trade-offs, ordered tasks, and verification.
3. Before implementation edits, summarize the proposal to the user and link the
   file. Follow the [shared authorization rules](../../agent/README.md).
4. Reuse the file on resumption. Update actual progress and evidence at milestones
   and before handing off. Record and present material scope or approach changes
   before implementing them, keeping the rationale and decision history.
5. Promote confirmed, reusable learnings into their appropriate durable artifact.
6. Move the plan into [completed/](completed/) when acceptance criteria and required
   reviews are satisfied. Update affected links and run the relevant checks.

Trivial LOW tasks need no plan file unless requested. Non-trivial LOW tasks and all
NORMAL/HIGH tasks require one; see the shared agreement for the distinction.
One-off NORMAL goals can be specified inside the plan. HIGH tasks with independent
review pending stay active and are not merge-ready.

Task records concern the work in this repository; archived template maintenance
is separate from your project's future task records.
