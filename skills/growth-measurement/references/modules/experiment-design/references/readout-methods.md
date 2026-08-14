# Experiment Readout Methods

## Readout Sequence

1. Confirm the frozen specification, assignment population, exposure dates, and analysis version.
2. Verify maturity, data freshness, identity, exclusions, invariants, SRM, logging, and implementation.
3. Report control and treatment counts and metric values under the frozen definitions.
4. Report absolute effect, relative effect only when its denominator is meaningful, and uncertainty interval.
5. Compare the interval with material benefit, harm, non-inferiority, or equivalence boundaries.
6. Read guardrails, diagnostics, segments, interference, and long-term risk.
7. Apply the predefined decision rule or document an accountable override.

```text
absolute_effect = treatment_value - control_value
relative_effect = absolute_effect / control_value
```

Report percentage points for absolute differences between rates. Do not call a relative percentage change a percentage-point change.

## Interpretation Boundaries

Statistical significance does not prove practical value, mechanism, quality, or durability. Non-significance does not prove no effect. Equivalence or non-inferiority requires a prespecified margin and suitable design.

An interval spanning meaningful benefit and meaningful harm is inconclusive even if the point estimate is positive. An interval excluding material harm may support a cost- or complexity-reducing change only when that decision rule was appropriate and guardrails pass.

## Analysis Integrity

Do not stop at the first favorable look without a valid sequential rule. Do not select the primary metric, segment, window, denominator, or exclusion after seeing results. Correct or bound multiple-comparison risk when several confirmatory hypotheses are tested; label exploratory findings for follow-up.

Preserve original assignment and denominator. Do not remove churned, failed, unexposed, or noncompliant units when treatment could affect those states. Report missingness and differential attrition by condition.

## Segments, Interference, And Time

Use prespecified segment analysis when heterogeneity changes a real scoped decision. Do not generalize a segment effect beyond its tested population or treat noisy subgroup differences as interaction evidence without appropriate analysis.

For teams, networks, marketplaces, shared inventory, geographies, and time systems, report spillovers, equilibrium, carryover, and unit mismatch. A standard user-level readout is not causal when users affect one another across conditions.

Mark immature outcomes unavailable. Use longer holds, follow-up windows, repeated cohorts, persistent controls, or validated surrogates for delayed retention, revenue, trust, supply, or ecosystem effects. Treat novelty and primacy as alternatives until the outcome stabilizes.

## Decision Record

Use one result state:

- `benefit`: meaningful benefit and guardrails pass;
- `harm`: primary or guardrail evidence reaches the predefined harm rule;
- `flat`: valid design rules out material harm and benefit inside the declared boundary;
- `directional`: evidence is useful but below the action threshold;
- `inconclusive`: power, maturity, quality, assumptions, or interval do not resolve the decision.

Record the action, owner, scope, rollback, monitoring, unresolved uncertainty, and next evidence. Preserve negative, flat, harmful, contradictory, and failed-quality results for reuse.
