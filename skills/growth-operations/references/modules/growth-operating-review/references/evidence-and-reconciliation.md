# Evidence And Reconciliation

## Validate The Signal First

Before explaining movement, check:

- source availability, freshness, latency, late arrival, backfill, and revision;
- event, state, identity, eligibility, denominator, attribution, currency, and accounting definition changes;
- duplicate, missing, suppressed, sampled, censored, or filtered records;
- product, tracking, consent, channel, billing, contract, and source-system releases;
- time zone, calendar, seasonality, market holidays, and cohort maturity;
- reconciliation with independent or downstream records where authorized evidence exists.

Separate a measurement change, mix shift, temporary variance, execution miss, structural change, and unresolved signal. Route detailed unexpected-movement work to `growth-diagnosis`.

## Decompose Before Explaining

Use exact compatible identities where available:

```text
rate = qualified numerator / original eligible denominator
revenue = active paying entities x purchase frequency x realized value per purchase
recurring value close = opening + new + resurrected + expansion - contraction - churn + adjustments
cash change = collected inflow - paid outflow, reconciled to timing and working capital
```

Show numerator and denominator, stock and flow, volume and value, average and marginal, within-segment and mix effects separately. Do not force a formula that does not fit the business model.

## Preserve Causal Boundaries

A target variance, time sequence, correlation, attribution model, customer quote, stakeholder belief, competitor action, or dashboard annotation does not establish cause. For each material explanation record:

- hypothesized mechanism and alternatives;
- evidence expected if each mechanism were true;
- supporting, contradictory, unavailable, and maturity-limited evidence;
- confounding, selection, interference, spillover, and concurrent changes;
- next discriminating observation or test, owner, and decision date.

Route causal tests to `growth-measurement`. Preserve negative, flat, harmful, delayed, inconclusive, and contradictory evidence.

## Reconcile Forecasts

Compare actuals only with the forecast version available at the original as-of date. Record horizon, entity, method, assumptions, scenario, interval, revisions, error, direction, bias, maturity, and structural changes. Do not replace the forecast with actuals or claim accuracy from a rewritten history.

The review can decide whether recalibration is needed. Route model rebuild, back-testing, uncertainty calibration, and new projections to `growth-measurement`.

## Review Experiments As A Portfolio

Record decision, hypothesis, assignment, exposure, sample maturity, metric contracts, SRM, power, peeking, multiplicity, interference, guardrails, estimate, uncertainty, negative or harmful outcomes, decision, and follow-up maturity. Do not select only significant wins, add uplifts, or insert an experiment estimate into a forecast without a separate transfer and calibration decision.

## Version Corrections

When evidence changes, retain the prior value, source, version, decision, and rationale. Record the corrected value, reason, affected decisions, owner, and whether the review must be reopened. A corrected record does not make the original evidence fraudulent or the original decision automatically unsound.
