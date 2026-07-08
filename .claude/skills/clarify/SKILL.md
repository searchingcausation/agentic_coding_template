---
name: clarify
description: Use when a task is vague, broad, risky, architectural, underspecified, or likely to cause scope creep.
---

# Clarify Workflow

## Goal

Reach shared understanding before planning or coding.

## Use When

- the request is vague, broad, risky, or architectural
- "done" is unclear
- APIs, schemas, prompts, models, dependencies, data, or evaluation may be affected
- the task could grow into a broad refactor or hidden design decision

## Process

1. Summarize what you think the user wants.
2. Inspect the codebase when it can answer the question.
3. Identify ambiguities, risks, and hidden assumptions.
4. Ask only necessary questions.
5. Recommend the smallest sensible next step.

## Output

Use a compact structure:

- Understanding
- Ambiguities / risks
- Recommended direction
- Smallest useful next step
- Question, if needed

## Do Not

- Do not write code.
- Do not create a large plan yet.
- Do not assume hidden requirements.
