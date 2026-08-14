# Funnel Analysis Methods

## Choose The Model

Use a linear funnel only when the same eligible entity moves through an ordered sequence and the order matters. Use a state-transition model for branching, skipping, retries, returns, resurrection, parallel roles, or repeated transactions. Use a customer journey for contextual questions that are not reliably measurable as ordered states.

Keep a canonical total view. Add cohort or segment views only when the distinction can change a decision and has sufficient volume, maturity, and privacy protection.

## Calculation Gate

Before calculating, confirm:

1. one compatible entity and identity rule;
2. frozen eligibility and cohort membership;
3. exact state events and timestamps;
4. compatible numerator and denominator;
5. complete observation and maturation windows;
6. explicit exclusions, missingness, retries, and re-entry;
7. one definition version, cutoff, and timezone;
8. reconciled source counts.

If any required field is unresolved, mark the affected result `unavailable` and provide a measurement specification. Do not manufacture a denominator from page views, sessions, leads, users, accounts, or orders that belong to another unit.

## Core Measures

For a sequential funnel with canonical start population `N0` and state counts `Ni`:

```text
step conversion i -> i+1 = N(i+1) / Ni
step loss i -> i+1 = Ni - N(i+1)
end-to-end conversion = Nfinal / N0
absolute downstream movement scenario
= eligible transition volume x plausible transition lift x downstream survival x confidence
```

Always display each numerator and denominator beside the rate. Label relative lift, percentage-point change, and absolute unit change separately. The downstream movement expression is a prioritization scenario, not a forecast or causal estimate.

Also report when available:

- median and distribution of time to transition, not only the mean;
- mature conversion after every eligible unit reaches the cutoff;
- retained conversion from the canonical start to recurring value;
- economic yield or contribution from the canonical start;
- error, support, trust, quality, refund, margin, or capacity guardrails.

## Maturity And Right Censoring

A unit is right-censored when its conversion opportunity is still open at the analysis cutoff. Do not classify it as a failure. Show:

- mature eligible units and their outcomes;
- immature or censored units;
- the cutoff and allowed window;
- delayed event or source-latency risk;
- sensitivity to alternative justified windows.

Compare cohorts only after applying the same start definition, window, and maturity rule. For long or variable durations, use time-to-event or survival methods when the supplied data and expertise support them; otherwise report a bounded mature-cohort view.

## Cohorts, Segments, And Mix

Compare like with like. Keep cohort start, maturity, entity, source, product version, market, and other structural conditions visible. An aggregate change can result from:

- within-segment conversion change;
- segment-mix change;
- definition or instrumentation change;
- maturation or seasonality;
- a real system change.

Report canonical totals, segment counts, segment rates, and contribution to total movement. Do not search many cuts until one appears favorable. Mark exploratory cuts and protect small groups from re-identification.

## Identity And Repeated Behavior

For anonymous-to-known, multi-device, multi-user account, recurring order, subscription, or marketplace data, specify whether the analysis uses people, accounts, episodes, orders, listings, or another unit. Do not treat repeated attempts as new people or combine user activation with account conversion.

For B2B, separate lead, contact, opportunity, account, buyer, user, workspace, implementation, and revenue states. For marketplaces, define each side and local network unit. For AI products, distinguish prompts and generated outputs from verified successful tasks and repeated value.

## Uncertainty And Change

For supplied counts, report uncertainty appropriate to the design and sample. Do not call a difference significant, causal, or generalizable without a valid comparison method. Historical before-after movement may be affected by mix, seasonality, concurrent changes, instrumentation, and regression to the mean.

Use `experiment-design` when assignment is feasible. Otherwise specify the strongest feasible bounded design, such as a staged pilot, interrupted time series, matched comparison, switchback, process observation, or qualitative mechanism study, with explicit limitations.

## Reconciliation Table

Return at minimum:

| State or transition | Entity | Eligible N | Success N | Rate | Absolute loss | Window | Mature N | Evidence | Notes |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | --- |

If calculations are unavailable, keep the same table and replace unsupported values with `unavailable`; then add the exact event, field, query logic, source, owner, and validation required to populate each row.
