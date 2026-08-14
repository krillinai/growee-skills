# LTV Contract

Complete this contract before calculating, forecasting, comparing, or acting on lifetime value.

## Decision Header

| Field | Requirement |
| --- | --- |
| Mode | `audit`, `estimate`, or `portfolio` |
| Decision | The bounded decision LTV may inform; LTV alone does not authorize action |
| Owner | Accountable human role and review date |
| Customer unit | Beneficiary, user, workspace, account, legal customer, subscription, payer, order, or another explicit entity |
| Cohort | Entry event, eligibility, start period, market, product, source, exclusions, and original denominator |
| Value basis | Customer value, revenue, gross profit, or contribution with a complete definition |
| Horizon | Observed cutoff, maturity, forecast horizon, tail, refunds, and re-read date |
| Model | Method, features or assumptions, version, training cutoff, effective dates, and owner |
| Action boundary | Local analysis, specification, or separately authorized implementation |

## Evidence States

Use only `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. Keep a stakeholder, platform, model-vendor, or finance statement without inspectable support as a `reported signal` with no evidence state.

For every item record source, extract or query version, entity, cohort, product, market, currency, event time, processing time, cutoff, owner, limitation, and counterevidence. Unavailable evidence is not zero value or model failure.

## Customer And Payer Hierarchy

Map applicable layers:

```text
person -> user or seat -> workspace, household, team, or account
-> legal customer, contract, subscription, order, or marketplace participant
-> payer, invoice, payment, revenue, and contribution entity
```

Define identity keys, hierarchy, merge and split, multiple products, multiple payers, account transfer, cancellation, deletion, reactivation, resurrection, and unknown states. Value, retention, revenue, cost, and the denominator must reconcile at the declared customer unit.

## Cohort Contract

Record cohort entry, eligible population, original denominator, acquisition or start state, exclusions, deduplication, market, product, offer, package, price version, source, intent, start timezone, late entry, re-entry, cohort reassignment, cutoff, and maturity.

Keep the original eligible denominator for acquired-customer LTV. If the decision uses per-payer, per-account, per-active-user, per-order, or per-opportunity value, name that estimand separately and do not label it acquired-customer LTV.

## State And Opportunity Contract

Define natural value or purchase frequency and the states that can produce value: eligible, activated, active, transacting, at-risk, inactive, lapsed, churned, cancelled, contracted, expanded, resurrected, reactivated, and unknown. For low-frequency products, distinguish absence from a missed eligible opportunity. For contracts, distinguish renewal eligibility, renewal decision, renewal, cancellation, contraction, and implementation.

## Value Waterfall

Define each included layer and source truth:

```text
booked -> billed -> paid -> refunds, credits, chargebacks, discounts, and tax
-> recognized revenue -> gross profit
-> contribution after declared variable and decision-relevant costs
```

Record currency, exchange rate, recognition, cash timing, payment and platform fees, partner share, cost of goods, inference or service delivery, fulfillment, fraud, incentives, implementation, support, success, and other included costs. State whether sales, creative, fixed overhead, or acquisition cost is included. Prevent double counting when comparing LTV with CAC.

## Time And Forecast Contract

Record period grain, event time, processing time, timezone, lag, observed cutoff, refund maturity, censoring, seasonality, age or tenure, forecast origin, horizon, survival or opportunity, conditional value, price, expansion, contraction, cost, discount, tail, terminal, scenario, and reforecast cadence.

Never hide which periods are observed and which are forecast. Do not assume an infinite lifetime, permanent plateau, constant hazard, or terminal value without evidence and sensitivity.

## Privacy Boundary

Prefer aggregate, redacted, or pseudonymous cohort tables. Request only fields required for the named estimand and validation. Record purpose, authority, consent, joins, access, retention, minimum cells, suppression, correction, deletion, and reidentification risk. Exclude credentials, tax identifiers, exact location, protected traits, raw communications, employee notes, and named customer rankings unless separately necessary, authorized, and governed.
