---
name: grill-me
description: Use as a read-only interview to test, correct, and deepen the user's understanding of a repository, feature, architecture, data flow, entry points, tests, or failure modes. Trigger after repo exploration, before planning changes, or when the user asks to be quizzed, grilled, challenged, or checked on their mental model.
---

# Grill Me Workflow

## Goal

Probe the user's mental model until the important assumptions are explicit and corrected.

This workflow is read-only. Do not edit files.

## Process

1. Pick one important topic at a time.
2. Ask one focused question.
3. Wait for the user's answer.
4. Compare the answer against repo evidence when available.
5. Correct misunderstandings with specific file references.
6. Continue until the core mental model is reliable or the user stops.

## Question Areas

- project purpose and boundaries
- main entry points
- runtime, data, and control flow
- key abstractions and ownership boundaries
- tests and verification paths
- failure modes and edge cases
- likely impact of proposed changes

## Style

- Be direct but constructive.
- Prefer precise questions over broad prompts.
- Do not ask several questions at once.
- Cite files, functions, classes, or commands when correcting an answer.
- Say when the repo does not provide enough evidence.

## Do Not

- Do not edit files.
- Do not move to planning or implementation unless the user asks.
- Do not let uncertain assumptions pass as confirmed understanding.
