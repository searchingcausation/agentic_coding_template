---
name: review
description: Use after implementation, before merge, or when asked to critique a diff for correctness, scope creep, risks, and missing verification.
---

# Review Workflow

## Goal

Review the change critically and constructively.

Verify that the implementation solves the stated problem without unnecessary side
effects, silent behavior changes, or uncontrolled scope.

## When To Use

Use:

- after implementation
- before merging
- when asked to critique a change
- when reviewing an agent-generated diff
- when checking for scope creep
- when validating maintainability

## Process

1. Restate the original goal.
2. Compare the change against the goal.
3. Identify changed files/modules.
4. Check for unrelated changes.
5. Check correctness and edge cases.
6. Check failure handling.
7. Check tests and verification.
8. Check architecture and maintainability.
9. Identify risks.
10. Recommend minimal fixes.
11. State merge readiness.

## Review Checklist

Scope:

- Does the change solve the stated problem?
- Is the scope controlled?
- Are there unrelated changes?
- Did the implementation expand beyond the plan?

Correctness:

- Does the code handle expected inputs?
- Does it handle invalid inputs?
- Are errors handled explicitly?
- Are outputs validated?

Interfaces and schemas:

- Did public interfaces change?
- Did data schemas change?
- Are changes backward compatible?
- Are downstream consumers affected?

AI / ML / LLM behavior:

- Did prompts change?
- Did model/provider behavior change?
- Did temperature/config change?
- Did evaluation logic change?
- Are LLM outputs validated?
- Are malformed outputs handled?
- Are costs or latency affected?

Tests and verification:

- Are tests meaningful?
- Were tests run?
- Are external services mocked?
- Is there a regression test for bug fixes?
- Is there an eval for behavior changes?

Maintainability:

- Is the code readable?
- Are boundaries clear?
- Is logic separated from orchestration?
- Are external dependencies isolated?
- Is the solution overengineered?
- Are files or scripts growing past the 300-line warning threshold without explanation?

## Output Format

Use findings-first. If no issues are found, say that clearly and mention residual risk
or test gaps.

```md
## Review Summary

...

## Issues Found

### Issue 1: ...
Severity: low/medium/high
Why it matters:
Suggested fix:

## Scope Creep Check

...

## Test / Verification Check

...

## Architecture / Maintainability Check

...

## Merge Readiness

Ready: yes/no
Reason:
```

## Review Tone

Be direct and specific.

Prefer:

- "This is risky because..."
- "This changes behavior silently because..."
- "This should be split because..."
- "This lacks verification because..."
- "This is probably overengineered because..."

Avoid:

- vague comments like "looks good"
- nitpicks without impact
- rewriting everything during review
- approving unclear changes

