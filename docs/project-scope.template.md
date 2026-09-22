# Project scope: <name>

Status: draft | accepted | superseded
Owner: <person/team>
Updated: <YYYY-MM-DD>

Copy this template to `docs/project-scope.md` when starting a project. Keep the
general sections brief; remove optional AI sections that do not apply. Unknowns
are valid findings: label assumptions and proposed targets instead of inventing
evidence or treating them as accepted requirements.

This document captures project direction. Keep detailed behavior and acceptance
criteria in [product specs](product-specs/README.md), the current system in
[architecture](../ARCHITECTURE.md), technical rationale in
[design decisions](design-decisions/README.md), and implementation tasks and
progress in [execution plans](exec-plans/README.md). Link those records as they
appear rather than maintaining duplicate details here. Revisit this scope when
evidence materially changes the problem, audience, or MVP boundaries.

## Summary

<In a short paragraph: who needs what, why it matters, the proposed approach,
and the largest unresolved assumption.>

## Problem, users, and evidence

<Who experiences the problem, in which workflow, and how do they handle it today?
What observations, interviews, examples, or measurements demonstrate the need?
Link prior attempts or related work and explain what remains unsolved.>

## Desired outcome

<What would improve for users/operators, and what evidence would show that?
State a baseline and proposed target only when useful; otherwise describe an
observable qualitative improvement. Identify unknown baselines and how to learn
them. For outcomes requiring later observation, name an owner or follow-up trigger.
Link detailed success measures in product specs when available; delivery alone
does not establish product success.>

## Proposed approach and alternatives

<Describe the simplest plausible approach and why it fits the problem. Compare
realistic alternatives, including improving the current workflow. What evidence
supports the choice, and what is still an assumption? Avoid selecting a stack
before it is needed; link consequential technical decisions separately.>

## MVP and boundaries

- First useful workflow: <the smallest end-to-end experience worth delivering.>
- In scope: <essential capabilities for that experience.>
- Non-goals: <explicit exclusions from this project.>
- Deferred beyond the MVP: <possible later capabilities, without committing to them.>

## Inputs, constraints, and dependencies

<What inputs are available, what outputs are needed, and what data must be stored?
Identify access, data quality, privacy, compatibility, cost, latency, time, or
operating constraints where relevant. Name stakeholders, ownership, external
dependencies, and unresolved access needs. Keep proposed limits distinguishable
from confirmed constraints; link detailed contracts in specs.>

## Risks and first validation

<Which uncertainty could invalidate the approach or materially change the scope?
Choose the smallest useful check before committing to more implementation.>

| Assumption / unknown | Evidence or smallest validation | Decision it informs | Owner / timing |
| --- | --- | --- | --- |
| <Highest-priority uncertainty> | <Existing evidence or proposed check> | <When to proceed, revise, or stop> | <Who / when> |

## AI considerations (optional)

Use these prompts only when the product itself uses AI. Developing conventional
software with a coding agent does not require this section. Keep applicable
answers short and link detailed specs, decisions, or evaluation records.

- **Suitability and baseline:** Why use AI for this workflow? What simpler
  non-AI, rule-based, or classical ML approach provides a useful comparison?
- **Evaluation:** Which representative examples and failure cases will assess
  quality? What rubric or expected behavior defines success, and what needs human
  judgment? Compare prompt/model changes against a baseline when relevant;
  choose the breadth of experiments to resolve actual uncertainty.
- **Data and retrieval, if needed:** Are source data accessible, suitable, and
  current enough? How will source access be respected, and how will evaluation
  distinguish retrieval failures from generation failures?
- **Tools and autonomy, if needed:** What may the system read or change, which
  actions need human approval, and what should happen on tool failure? Identify
  appropriate execution limits and recovery or fallback behavior.
- **Operating limits and feedback:** What quality, latency, and cost limits matter?
  How will failures and user feedback inform improvements? Specify what may be
  logged, including sensitive-data handling, rather than assuming full request
  and response logging is appropriate.
