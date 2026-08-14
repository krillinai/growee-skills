# Forecasting And Reconciliation

## Pipeline Contract

For every pipeline view define opportunity or other entity, eligibility, owner, segment, source, stage, buyer evidence, amount basis, currency, probability basis, expected close or realization date, forecast category, product, new, renewal or expansion type, snapshot timestamp, exclusions, and reversals.

Show counts and amounts. Preserve created, progressed, regressed, slipped, increased, decreased, split, merged, won, lost, disqualified, no-decision, expired, reopened, and deleted movement. A current-state export cannot reconstruct historical pipeline or forecast behavior without trustworthy snapshots or change history.

## Forecast Audit

Keep these separate:

- seller or manager judgment;
- stage or category rules;
- statistical or model prediction;
- weighted pipeline arithmetic;
- capacity and supply constraints;
- finance plan, target, quota, and scenario;
- observed bookings, revenue, contribution, and cash.

Audit eligible forecast population, as-of snapshot, horizon, amount, timing, stage and category, overrides, changes, age, slippage, calibration, bias, concentration, new-pipeline dependency, seasonality, cancellations, and actual reconciliation.

Measure error only from compatible historical snapshots and actual definitions. Report direction and distribution, not one average alone. Do not infer accuracy from a current snapshot, confidence label, or a small set of won deals. Do not prescribe a universal pipeline coverage ratio or forecast accuracy threshold.

## Commercial And Finance Chain

Map explicitly:

```text
approved offer and price
-> quote and discount
-> signed contract or accepted order
-> subscription, entitlement, or delivery obligation
-> invoice and payment due
-> payment and cash
-> fulfillment, refund, credit, cancellation, or reversal
-> recognized revenue and contribution
```

Definitions can differ by business model and accounting policy. Use only supplied approved finance definitions; do not make accounting, tax, or legal conclusions.

## Reconciliation Table

For every comparison capture source A, source B, canonical decision use, entity, field, definition, version, population, period, snapshot, currency, timezone, transformation, expected tolerance and basis, observed total, variance, unknowns, timing difference, exclusions, owner, status, and resolution date.

Common reconciliations include:

- marketing response to CRM person, account, source, and opportunity;
- CRM opportunity to quote, contract, order, and partner record;
- contract or order to subscription, entitlement, implementation, and billing;
- billing to invoice, payment, refund, credit, cash, and finance ledger;
- booked, contracted, billed, collected, recognized, retained, and contribution views;
- account and opportunity to product usage, first value, support, renewal, and churn;
- original assignment and attribution to downstream customer and economic cohorts.

Do not erase discrepancies or select the source with the preferred total. Preserve legitimate timing, scope, accounting, and entity differences.

## Attribution And Causality

Operational attribution routes ownership and credit under declared rules. Financial reconciliation confirms compatible amounts and states. Association describes co-occurrence. Prediction estimates a future state. Causality estimates what changed because of an intervention.

Never add platform, marketing, partner, sales, product, and finance attribution views as though they represent unique revenue. Use causal designs for budget or policy decisions when feasible and route them to `experiment-design`.

## Renewal And Expansion

Separate renewal eligibility, customer value, usage, relationship, support, risk, price change, contract event, invoice, payment, retained revenue, expansion, contraction, and churn. Health scores are predictions or operating signals until calibrated; they are not customer truth.

Connect original promise and qualification to implementation, first value, recurring value, renewal, expansion, and churn. A renewal booking can coexist with weak adoption, unresolved risk, price-only growth, or later contraction.
