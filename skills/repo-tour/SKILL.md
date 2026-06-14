---
name: repo-tour
description: Use for read-only reconnaissance of a new, unfamiliar, complex, or confusing repository before planning or editing code. Trigger when the user asks to understand a repo, map a codebase, find entry points, explain data/control flow, identify key abstractions, or learn how to run and test the project.
---

# Repo Tour Workflow

## Goal

Build a practical mental model of the repository before changing anything.

This workflow is read-only. Do not edit files.

## Process

1. Inspect the repo structure with fast file search.
2. Read the project docs and agent instructions first.
3. Identify main entry points, important folders, configs, and tests.
4. Trace the likely runtime, data, or control flow through concrete files.
5. Identify key abstractions, dependencies, and fragile areas.
6. Find how to run, test, and debug the project when discoverable.
7. State uncertainty explicitly instead of guessing.

## Output

Use a compact structure:

- project purpose in plain English
- main entry points
- important folders and files
- runtime / data / control flow
- key abstractions and dependencies
- how to run and test
- common pitfalls or risky areas
- suggested learning path

Cite concrete files, functions, classes, and commands.

## Do Not

- Do not edit files.
- Do not create a plan for changes unless the user asks.
- Do not invent run commands or architecture facts that are not visible in the repo.
