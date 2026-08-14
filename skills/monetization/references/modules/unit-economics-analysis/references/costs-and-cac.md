# Costs And CAC

CAC is valid only for a named acquired entity, cohort, acquisition event, cost scope, period, market, attribution or incrementality basis, and maturity.

## Cost Ledger

For every cost record:

- purpose, owner, vendor, channel, campaign, product, market, and customer entity;
- committed, incurred, accrued, invoiced, paid, refunded, credited, capitalized, and allocated dates;
- direct, shared, fixed, variable, step-fixed, sunk, avoidable, incremental, and marginal status;
- currency, FX, tax, accounting, cash, source, allocation driver, coverage, and uncertainty;
- whether the cost appears in acquisition, delivery, LTV, contribution, or another model.

Inspect media and placements; agency and contractor fees; creative research, production, localization, and rights; tooling, data, measurement, and platform fees; referral, affiliate, partner, and marketplace fees; discounts, credits, rewards, subsidies, samples, and trials; events and field programs; sales development, sales labor, commissions, travel, solution engineering, and procurement; free-tier product and support; onboarding and implementation; fraud, reversals, and shared overhead where the decision requires them.

Do not include every company expense by default. Declare the decision logic for inclusion, exclusion, capitalization, allocation, and cash timing. Prevent one cost from appearing in CAC, service cost, contribution, and LTV more than once.

## Named CAC Variants

| Variant | Numerator | Denominator | Boundary |
| --- | --- | --- | --- |
| Media-only CAC | Matching media or placement cost | Qualified acquired entities | Not fully loaded |
| Direct program CAC | Direct avoidable program costs | Qualified acquired entities | State labor, creative, tools, and incentive coverage |
| Fully loaded CAC | Declared direct and allocated acquisition system costs | Qualified acquired entities | State allocation drivers and residuals |
| Blended CAC | Compatible acquisition costs across named sources | Compatible acquired entities | Hides mix and marginal differences |
| Attributed CAC | Costs and customers joined under a source-credit model | Attributed acquired entities | Descriptive credit, not causal lift |
| Incremental CAC | Incremental cost versus counterfactual | Incremental acquired entities versus counterfactual | Requires credible causal evidence |
| Marginal CAC | Change in compatible cost over a bounded spend band | Change in qualified acquired entities | Does not automatically extrapolate |

Also keep cost per reach, click, visit, lead, signup, install, trial, activation, opportunity, order, and payer separate. They become customer CAC only when that entity is the declared customer acquisition unit.

## Matching Costs To Customers

Build a bridge:

```text
cost commitment and cash date
-> eligible exposure or sales effort
-> lead, signup, or opportunity
-> qualified acquisition event
-> original acquired cohort
-> activation, retention, value, and refund maturity
```

Use cohort or lag allocation when sales cycles cross periods. State whether costs are assigned by direct join, spend cohort, lead cohort, acquisition cohort, contract, weighted lag distribution, or another reproducible rule. Preserve unattributed cost and unknown-source customers. Do not force every cost or customer into a channel.

## Attribution And Incrementality

Attribution assigns descriptive credit under a model. Incrementality estimates outcomes caused relative to a counterfactual. Keep platform-reported, last-touch, first-touch, multi-touch, sales-sourced, partner-sourced, self-reported, and unknown views separate.

For incremental CAC, define eligible population, assignment, exposure, spillover, counterfactual, incremental cost, incremental acquired entity, maturity, power, uncertainty, and guardrails. If estimated incremental customers are zero or negative, report the estimate and uncertainty; do not divide into an attractive positive CAC. Route causal design and interpretation to `experiment-design`.

## Average And Marginal Economics

For spend band `b`:

```text
observed marginal CAC_b
= (compatible cost_b - compatible cost_(b-1))
/ (qualified acquired entities_b - qualified acquired entities_(b-1))
```

Use this only when bands use compatible time, audience, product, market, creative, attribution, quality, and maturity. Otherwise label the difference descriptive. Show auction price, frequency, audience expansion, creative fatigue, organic overlap, brand demand, sales capacity, conversion lag, and customer quality.

Historical blended CAC cannot forecast the next dollar. Fit a response curve only with enough variation, stable measurement, a declared functional form, uncertainty, out-of-sample checks, and structural-change review.

## Cost QA

Reconcile cost ledger totals to the supplied source; show missing periods, duplicate invoices, credits, taxes, cross-channel allocations, capitalized amounts, cash timing, and residuals. Report coverage beside every CAC. A precise ratio from partial cost data remains partial.
