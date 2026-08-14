# Cohort Analysis Methods

## Calculation Gate

Before calculating, confirm:

1. one explicit entity and identity rule;
2. frozen eligibility, assignment, and original membership;
3. exact start and qualifying outcome definitions;
4. compatible numerator, denominator, age, and window;
5. observation cutoff, timezone, latency, and maturity;
6. one source and definition version or a documented normalization;
7. explicit exclusions, missingness, re-entry, deletion, and deduplication;
8. reconciled canonical and segment totals.

If a required field is unresolved, mark affected results `unavailable` and return the missing contract or query logic. Do not fill the gap with a benchmark, calendar aggregate, extrapolation, or synthetic cohort.

## Assign Cohort Age

Assign each entity according to the frozen first, latest, every, or episode rule. For time-based cohorts:

```text
cohort_age
= floor((qualifying_period_start - cohort_start_period) / declared_interval)
```

Use one timezone before period assignment. Preserve source timestamps and document daylight-saving, late-arrival, backfill, and event-version handling.

For opportunity cohorts, increment age only when a verified opportunity occurs. Do not classify entities without a verified opportunity as failures.

## Build The Matrix

For a rate at cohort age `t`:

```text
cohort_rate(t)
= qualifying entities at age t under the declared outcome definition
/ eligible original-cohort entities mature through age t
```

Show rate, numerator, denominator, and maturity. A later cohort with an open outcome window is right-censored, not zero.

Illustrative exact weekly value table:

| Start cohort | Eligible N | Week 1 | Week 2 | Week 4 |
| --- | ---: | ---: | ---: | ---: |
| June 1 | 100 | 52/100 = 52% | 39/100 = 39% | 31/100 = 31% |
| July 20 | 120 | 68/120 = 56.7% | Unavailable | Unavailable |

Only Week 1 is comparable at the stated cutoff. Do not use early events to populate an exact later-age cell.

## Keep Definitions Distinct

| Definition | Required boundary |
| --- | --- |
| Exact or bounded | Outcome occurs in the named age period or interval |
| Rolling | Outcome occurs at or after the named age through a declared cutoff |
| Bracket | Outcome occurs inside a declared age range |
| Opportunity | Outcome occurs when a verified opportunity exists |
| Survival | Time until a declared event while preserving censoring |
| Period value | Revenue, contribution, cost, or usage in the named age period |
| Cumulative value | Sum through the named age and cutoff |

Never collapse exact and rolling rates into one value. Never compare cumulative value at different ages as though horizons were equal. Keep forecasts separate from observed values and require model horizon, uncertainty, calibration, and mature back-testing.

## Reconcile Identity And Levels

- Deduplicate repeated events under the declared entity and outcome rule.
- Resolve or expose anonymous-to-known, cross-device, merged-account, deletion, and re-entry effects.
- Keep unknown identities and segments visible instead of silently discarding them.
- Separate user, seat, workspace, account, product, order, subscription, revenue, contribution, and cost views.
- Define explicit joins for linked views; invitation is not activation, and user activity is not account renewal.

## Decompose Aggregate Movement

An aggregate change can reflect:

- within-group outcome change;
- group-mix or cohort-composition change;
- maturity, seasonality, or opportunity change;
- definition, identity, instrumentation, or product-version change;
- a real system change.

Keep a canonical total and report each mutually exclusive group's count, rate, and absolute contribution. Preserve an unknown group. When group rates are unchanged but composition changes, label the movement as a supplied mix effect, not product improvement.

Do not search many cuts until one appears favorable. Predeclare decision-relevant cuts where possible, show sample sizes and uncertainty, suppress or combine privacy-risk cells, and label exploratory findings as hypotheses.

## Causal Boundary

Cohort analysis is descriptive unless assignment or another credible causal design supports a treatment effect. Exposure, activation behavior, product adoption, and channel cohorts may differ because of selection, intent, customer mix, concurrent change, or measurement.

Route causal validation to `growth-measurement`. Route funnel constraints to `growth-diagnosis`, recurring-value and churn mechanisms to `retention`, first-value mechanisms to `activation`, and commercial policy to `monetization`.
