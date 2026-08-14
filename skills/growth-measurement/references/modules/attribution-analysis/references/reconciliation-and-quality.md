# Reconciliation And Quality

## Reconciliation Waterfall

Build the waterfall with declared entities and windows:

```text
eligible company outcomes
-> observed in outcome source truth
-> identity-resolved and deduplicated
-> eligible for attribution
-> matched to one or more eligible journeys
-> credited under the named model
-> unmatched, unknown, excluded, disputed, or late
-> paid, refunded, cancelled, or reversed
-> recognized business outcome
-> mature product and retained-value outcome
```

Show absolute counts and rates at every transition. Never sum provider claims to create unique company outcomes.

## Source-Truth Matrix

| Layer | Typical source role | Do not assume |
| --- | --- | --- |
| Platform or partner | Provider delivery and self-attributed claim | Unique customer, company reconciliation, causal lift |
| MMP | App install or event attribution under configured rules | Complete web, account, revenue, or incrementality view |
| Product analytics | Product events and identity under instrumentation rules | Payment, recognized revenue, or perfect source capture |
| CRM | Contact, account, opportunity, stage, ownership, source fields | Product value, contract truth, finance truth, causality |
| Billing | Orders, subscriptions, invoices, payments, refunds | Recognized revenue, contribution, customer value |
| Finance | Recognized revenue, cash, currency and accounting states | Product behavior, touchpoint truth, causal contribution |
| Support or success | Customer burden, incidents, implementation, outcomes | Complete population or unbiased attribution |

Map each field to one accountable source truth or a declared reconciliation rule. Do not select the largest total or overwrite disagreement silently.

## Quality Checks

| Check | Question |
| --- | --- |
| Coverage | What share of eligible outcomes has sufficient source and identity evidence? |
| Uniqueness | Do entities, orders, subscriptions, and outcomes deduplicate under declared rules? |
| Completeness | Are required sources, campaigns, markets, devices, and states represented? |
| Validity | Do values, timestamps, currencies, and taxonomies meet the contract? |
| Consistency | Do equivalent definitions reconcile across systems and snapshots? |
| Timeliness | Are event time, processing time, late data, refunds, and maturity visible? |
| Stability | Does credit move materially with data refreshes, identity, windows, or rule versions? |
| Explainability | Can a credited outcome be reconstructed without exposing a named customer? |

Report numerator, denominator, cutoff, owner, severity, and completion proof. Missing evidence is not zero attribution.

## Economic Reconciliation

Keep:

```text
booked amount
-> invoiced amount
-> paid and cash amount
-> refunds, credits, cancellations, chargebacks, and tax
-> recognized revenue
-> gross profit
-> contribution after declared decision-relevant costs
```

State currency, exchange rate, tax, discount, refund, recognition, cost scope, cohort, maturity, and source. Include media, creative, incentive, partner, sales, onboarding, support, fraud, tools, and variable service cost where material. Do not call attributed revenue incremental revenue, ROAS contribution, or average CAC marginal CAC.

## Cohort Reconciliation

Freeze customer entity, source, intent, product, market, entry state, cohort start, cutoff, first-value and retention windows, refund and revenue maturity, product and attribution versions, and exclusions. Compare compatible cohorts and report absolute retained outcomes, rates, costs, and uncertainty.

Unknown source stays in the common denominator when it is eligible. Diagnose mix shift separately from within-source changes. Attribution differences are descriptive unless a credible causal design supports more.

## Remediation Order

1. Fix decision and outcome ambiguity.
2. Reconcile entity and identity definitions.
3. Stabilize source taxonomy and touchpoint eligibility.
4. Align time, currency, snapshots, and reversals.
5. Reconcile product, CRM, billing, and finance outcomes.
6. Quantify missing, unknown, overlap, and model sensitivity.
7. Improve instrumentation or models only where the decision benefit justifies cost and risk.
8. Revalidate before automating or reallocating.
