# Product specifications

Describe observable product behavior: goals, non-goals, constraints, contracts,
acceptance criteria, and important failure cases.

Use the [project scope](../project-scope.template.md) to establish the problem,
users, and MVP boundaries at project start. Derive detailed requirements here and
link them from the project's scope; keep each requirement in one maintained place.

Copy [template.md](template.md) to a descriptive filename when a requirement should
serve as a durable reference. Keep implementation steps in execution plans and
technical rationale in design decisions. A one-off task may keep a compact spec
inside its execution plan.

Define the user/operator outcome and the evidence needed before choosing the
implementation. Use numbers when meaningful: record the measurement method,
baseline, target, and applicable limits or decision thresholds. Mark unknown
baselines and plan their measurement; distinguish proposed targets from accepted
requirements. Qualitative work can use an observable result instead.

For example, an import optimization can compare the same fixture before and after
the change while preserving its records. A documentation change can be accepted
by checking that its instructions cover the intended task without contradictions.
Neither example requires inventing a business metric.

Keep delivery criteria separate from outcomes that require later observation,
such as adoption. Record a follow-up trigger or owner for those measures. Describe
supported behavior accurately and keep proposed behavior clearly marked until
delivered; implementation results belong in the execution plan.

Create the first specification when defining your project's behavior.
