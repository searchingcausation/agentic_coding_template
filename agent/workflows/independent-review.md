# Independent review

Use for review of a defined change. Review is read-only unless the user separately
requests fixes or a saved review artifact. Findings come before recommendations.

## Establish independence and scope

Use a fresh session or an authorized reviewer with a separate context. Do not
start another agent or live model run merely because this workflow is selected.
If you already implemented the change or read the implementation reasoning, label
the result a self-review and state the independence limitation.

Obtain the goal/spec and exact review scope: base/head commits, PR, or local changes.
For local work, inspect `git status --short`, staged and unstaged diffs, and untracked
files explicitly. `git diff` alone misses new files. For a branch review, establish
whether the requested range is base-to-head or merge-base-to-head before reviewing.

Read the spec, architecture constraints, changed code, callers, and tests. Form an
independent account of expected behavior and findings **before reading the execution
plan or implementer's summary**. Do not treat the patch, tests, or plan as the spec.

## Review the behavior

Check relevant axes: spec compliance, correctness/edge cases, security/privacy,
architecture and compatibility, operability/failure handling, and unnecessary
complexity. Prioritize actionable defects over style already covered by checks.

Verify claims with code paths or reproducible checks. Run relevant offline checks
when available; distinguish observed results from reported evidence. Green tests
do not establish full specification or architecture compliance.

After recording initial findings, read the plan as a deviation audit. Identify
unexplained changes and reasonable adjustments; update findings if new evidence
changes the conclusion without hiding your earlier assumptions.

In this later audit, compare claimed outcomes and phase evidence with the original
criteria and actual results. Required checks that did not run remain pending;
technical tests do not establish unobserved product outcomes. Check documentation
impact against the diff: affected specs and usage guidance must match delivered
behavior, with a credible reason for relevant artifacts left unchanged. Check that
genuine follow-ups have traceable entries and that acceptance blockers were not
silently deferred to make the task appear complete.

## Report

For each finding, state severity, file/line, trigger, concrete impact, evidence,
and the smallest useful correction. Separate confirmed defects from open questions.
Include scope reviewed, checks run, gaps, and readiness. If no actionable defects
were found, say so while stating remaining limits. Never claim an independent
review if it was conducted in the implementation context.

HIGH changes need this fresh review before merge. If unavailable, implementation
can be delivered with review pending; keep that status explicit in the task plan.
