---
name: plan
description: Use when the goal is mostly clear but implementation is non-trivial and requires a reviewed plan before coding.
---

# Plan Workflow

## Goal

Turn a clarified goal into a small, reviewable implementation plan.

The plan must make approval meaningful. Do not implement during planning.

## When To Use

Use when:

- the goal is mostly clear
- implementation has not started
- the change is non-trivial
- multiple files or modules may be affected
- a technical approach needs to be selected
- the user asks for a plan, design, or breakdown

## Process

1. Restate the goal.
2. Define non-goals.
3. Identify affected files/modules.
4. Propose the smallest useful vertical slice.
5. Define expected inputs and outputs.
6. Identify interface, schema, prompt, model, or dependency changes.
7. Identify tests or verification steps.
8. List risks and trade-offs.
9. Ask for explicit approval.
10. Stop.

## Planning Principles

- Prefer small vertical slices over broad unfinished foundations.
- Prefer simple interfaces over premature abstraction.
- Prefer explicit contracts over implicit behavior.
- Prefer testable core logic over framework-heavy code.
- Prefer isolated external API calls over scattered provider logic.
- Prefer configuration over hardcoded values.
- Prefer reproducibility and debuggability.

## Small Vertical Slice

A good vertical slice:

- produces observable value
- can be tested or manually verified
- touches the minimum necessary code
- avoids broad rewrites
- can be reviewed in one diff
- leaves the system in a working state

Example for an LLM pipeline: one sample input, one prompt or mock provider call, one parser,
one validated output, and one focused verification path.

## Output Format

Use the full format for non-trivial plans. Keep it compact when the change is small but
still needs approval.

```md
## Goal

...

## Non-Goals

- ...

## Proposed Approach

...

## Smallest Vertical Slice

...

## Affected Files / Modules

- ...

## Interfaces / Schemas / Prompts

...

## Tests / Verification

...

## Risks / Trade-offs

...

## Open Questions

...

## Approval Request

Please confirm before I implement this plan.
```

## Do Not

- Do not implement during planning.
- Do not create a huge roadmap unless asked.
- Do not hide trade-offs.
- Do not silently choose architecture for the user.
- Do not add dependencies without calling them out.
- Do not continue past the approval request until approval is given.

