---
name: review
description: Use after implementation, before merge, or when asked to critique a diff for correctness, scope creep, risks, and missing verification.
---

# Review Workflow

## Goal

Review the change critically and constructively.

Prioritize bugs, behavioral regressions, uncontrolled scope, missing verification, and
maintainability risks.

## Use When

- after implementation
- before merging
- reviewing an agent-generated diff
- checking for scope creep or silent behavior changes

## Process

1. Restate the original goal.
2. Compare the diff against the goal and approved scope.
3. Check correctness, edge cases, and failure handling.
4. Check interfaces, schemas, prompts, models, dependencies, and evaluation behavior.
5. Check tests and verification.
6. Check project memory/docs updates when relevant.
7. Recommend minimal fixes.
8. State merge readiness.

## Output

Findings first. If no issues are found, say so clearly and mention residual risk or
test gaps.

Use a compact structure:

- Issues found, ordered by severity
- Scope check
- Verification check
- Memory/docs check
- Merge readiness

## Review Tone

Be direct and specific. Avoid vague approval, low-impact nitpicks, and rewriting the
change during review.
