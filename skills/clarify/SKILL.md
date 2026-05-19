---
name: clarify
description: Use when a task is vague, broad, risky, architectural, underspecified, or likely to cause scope creep.
---

# Clarify Workflow

## Goal

Reach shared understanding before planning or coding.

Use this workflow to prevent the agent from confidently building the wrong thing.

## When To Use

Use for tasks such as:

- "Build a pipeline for X"
- "Refactor this"
- "Make this better"
- "Add an LLM step"
- "Improve the architecture"
- "Implement this feature"
- "Change the data model"
- "Make the prompt better"

## Process

1. Summarize what you think the user wants.
2. Identify ambiguities, risks, and hidden assumptions.
3. Inspect the codebase if the answer can be found there.
4. Ask only necessary questions.
5. Ask one focused question at a time where practical.
6. Include a recommended answer when asking.
7. End with the smallest sensible next step.

## Questions To Consider

- What problem are we solving?
- What does "done" mean?
- Who or what consumes the result?
- What is included and excluded?
- Is this a prototype, experiment, production feature, or refactor?
- What are the expected inputs and outputs?
- Are schemas or public interfaces affected?
- Are prompts, models, providers, or evals affected?
- What should happen on failure?
- How should this be verified?

## Output Format

Use the full format for broad or risky tasks. Use a compact version for smaller tasks.

```md
## Understanding

I think you want to...

## Ambiguities / Risks

1. ...
2. ...

## Recommended Direction

I recommend...

## Smallest Useful Next Step

The smallest useful next step is...

## Question

My main question is...
Recommended answer: ...
```

## Do Not

- Do not write code.
- Do not create a large implementation plan yet.
- Do not assume hidden requirements.
- Do not ask questions the codebase can answer.
- Do not move to implementation until the next step is clear.

