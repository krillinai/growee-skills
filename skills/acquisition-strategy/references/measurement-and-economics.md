# Acquisition Measurement And Economics

## Operational Attribution And Causal Incrementality

Keep these views separate:

| View | Decision use | Required warning |
| --- | --- | --- |
| Platform attribution | delivery and optimization inside one platform | can overlap channels, organic demand, returning customers, and company totals |
| First or last touch | routing and simple journey reporting | assigns credit by rule rather than causal contribution |
| Multi-touch model | describing observed paths under model assumptions | weights do not establish incrementality |
| Partner code or link | settlement and operational reconciliation | code use can be selected, shared, duplicated, or non-incremental |
| Company source cohorts | reconciling identities, starts, downstream value, and finance | observed cohort differences can reflect selection and mix |
| Counterfactual estimate | budget and causal allocation | validity depends on design, contamination, maturity, and assumptions |

Never sum overlapping channel conversions. Reconcile eligible population, customer entity, identity, new and returning state, timestamps, organic classification, source changes, view-through rules, refunds, and company totals. Preserve original assignment and source lineage through mature outcomes.

## Counterfactual Selection

Use a design compatible with the mechanism:

- randomized user or account holdout when exposure is controllable and interference is low;
- cluster or sender assignment for referral, collaboration, account, or social spillover;
- geographic or market test for broad media or offline exposure;
- switchback for time-varying market or supply conditions;
- phased rollout, threshold, matched comparison, shutdown, or time series when randomization is infeasible.

Freeze decision, eligibility, assignment, exposure, identity, interference, primary outcome, guardrails, minimum effect, power or precision, maturity, exclusions, amendments, diagnostics, and decision rule. Route statistical implementation and causal readout to `growth-measurement`.

## Cost And Contribution Contracts

Use only compatible supplied values:

```text
full acquisition cost
  = media + creative + agency + incentive + tools
  + variable sales + partner + implementation + onboarding + support
  + fraud and other decision-relevant operating cost

cost per reconciled new customer
  = full acquisition cost / reconciled new customers

incremental CAC
  = incremental acquisition cost / incremental customers

net retained incremental contribution
  = retained contribution caused by acquisition - full incremental acquisition cost

payback periods
  = acquisition cost / compatible periodic contribution margin
```

Label every numerator and denominator. State entity, currency, exchange rate, tax, time basis, cash timing, cohort, maturity, contribution definition, cost inclusions, exclusions, source, and uncertainty. Check whether refunds, discounts, cost of goods, service, commissions, or fraud are already included before subtracting them.

ACV, bookings, revenue, ROAS, gross profit, contribution, LTV, and cash are not interchangeable. Forecasted LTV cannot repair weak observed retention or unknown cost. A channel can have positive lifetime expectation but violate cash, payback, capacity, or risk limits.

## Marginal Scale And Saturation

Read results by spend, audience, frequency, geography, creative, partner, sales-capacity, or time band. Track:

- qualified remaining demand and overlap;
- marginal exposure, new customers, activation, retention, and contribution;
- marginal full cost, incremental CAC, payback, and cash;
- frequency, response, conversion, creative fatigue, auction pressure, and competitor change;
- complaints, trust, fraud, policy, delivery, support, and operational capacity;
- uncertainty and outcome maturity.

Do not project an early or average rate as constant. Scale only while the next band meets retained incremental contribution, payback, capacity, quality, and risk gates. Define cap, pause, redesign, reallocation, and stop actions before crossing the band.

## Cohort Comparability

Compare only compatible entity, eligibility, intent, source state, cohort start, product version, value event, denominator, observation window, maturity, market, currency, and contribution definition. Report rates and absolute contribution. Separate source-mix change from within-source change and selection from intervention effect.
