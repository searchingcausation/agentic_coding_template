# Debug and fix

Use for an observed defect with expected behavior. Apply the shared risk tiers;
LOW bugs need no plan document, and HIGH changes still need an approved approach.

## Establish a reproduction

Read the relevant code and contract. Record expected versus actual behavior and
the smallest input/environment that demonstrates it. Diagnose the failure before
editing production code. Inspect official version-specific docs when an external
dependency's behavior is uncertain.

Create a focused regression test and run it against the unfixed implementation.
Confirm that it fails because of the reported defect, not a broken fixture,
missing dependency, or unrelated error. Record the command and observed failure.
Use fixtures/fakes instead of normal tests calling live providers.

If automation cannot reproduce the defect, explain the constraint and use the
smallest repeatable manual check. Do not fabricate a red-test result or add a test
that only mirrors implementation details.

## Fix without moving the target

Once the test demonstrates the bug, preserve its input and expected behavior while
making the minimal fix. A legitimate correction to the test/contract must be
explained and revalidated against the unfixed behavior. Do not weaken assertions,
skip the test, or silently change the specification to make it pass.

Run the regression test again, then the relevant surrounding tests and required
repository checks. Inspect failure paths and the final diff for collateral changes.
If broader changes become necessary, make the scope/decision visible and apply
the risk and authorization boundaries before proceeding.

## Finish with evidence

Report the root cause, affected behavior, reproduction command and failing result,
passing verification, and remaining limits. Update the active execution plan for
substantial work. Keep the regression as the durable lesson; add another rule or
workflow only if evidence shows a reusable need.
