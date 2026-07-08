---
name: plan
description: Use when the goal is mostly clear but implementation is non-trivial and requires approval before coding.
---

# Plan Workflow

## Goal

Turn a clear goal into a small, reviewable implementation plan. Do not implement during
planning.

## Use When

- the change is non-trivial
- multiple files or modules may be affected
- a technical approach needs to be selected
- the user asks for a plan, design, or breakdown

## Process

1. Restate the goal and non-goals.
2. Identify affected files, modules, configs, prompts, schemas, or tests.
3. Propose the smallest useful vertical slice.
4. Call out interface, schema, prompt, model, dependency, or evaluation changes.
5. Define verification.
6. List risks and assumptions.
7. Ask for explicit approval and stop.

## Output

Use a compact structure:

- Goal
- Non-goals
- Proposed approach
- Smallest vertical slice
- Affected files / modules
- Interfaces / schemas / prompts
- Verification
- Risks / assumptions
- Approval request

## Do Not

- Do not implement.
- Do not hide trade-offs.
- Do not silently choose architecture for the user.
- Do not continue past the approval request until approval is given.
