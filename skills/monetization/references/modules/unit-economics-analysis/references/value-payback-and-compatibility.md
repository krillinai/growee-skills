# Value, Payback, And Compatibility

Build customer and company value views before using CAC, LTV:CAC, payback, return, or scale claims.

## Value Waterfall

For a compatible customer cohort and period, reconcile:

```text
contracted or booked value
- cancellations and contract changes
= billed value
- credits, discounts, tax excluded from revenue, refunds, and reversals
= recognized net revenue
- declared direct delivery cost
= gross profit
- declared decision-relevant variable service, support, success, payment,
  partner, incentive, fraud, collection, and risk costs
= contribution before acquisition
- declared acquisition cost
= contribution after acquisition
```

Maintain a separate cash bridge from acquisition outflow through customer collection, refunds, chargebacks, supplier and partner payments, service outflows, tax, and working capital. Revenue recognition is not collection. Contribution is not cash.

State the treatment of inventory, fulfillment, hosting, AI inference, third-party APIs, data, moderation, human review, payment fees, partner share, support, customer success, implementation, warranties, bad debt, fraud, incentives, discounts, refunds, taxes, fixed cost, and shared overhead. Missing inputs are unavailable, not zero.

## Observed Cohort Economics

For original acquired cohort size `N0`, keep `N0` fixed unless another estimand is explicitly selected:

```text
period contribution per acquired entity_t
= compatible cohort contribution before acquisition_t / N0

cumulative observed contribution per acquired entity_h
= sum(period contribution through h)
```

Show cohort age, active and payer counts, revenue, contribution, cash, refund maturity, reporting lag, and source coverage. Do not divide cumulative value by only customers still active or compare cohorts at unlike maturity as lifetime-equivalent.

## LTV Compatibility

Use a validated LTV output only when these match CAC:

| Dimension | Required match |
| --- | --- |
| Entity | User, account, payer, contract, order, or marketplace side |
| Cohort | Entry event, start period, source, segment, product, market, and original denominator |
| Value | Revenue, gross profit, contribution before acquisition, contribution after acquisition, or cash |
| Time | Observed cutoff, forecast horizon, maturity, tail, refund window, and model date |
| Cost | Service and acquisition cost inclusion, allocation, currency, tax, accounting, and cash timing |
| Evidence | Observed and forecast split, assumptions, uncertainty, calibration, version, and owner |

Prefer contribution-before-acquisition LTV divided by compatible CAC when the decision asks for LTV:CAC. If the LTV already subtracts acquisition cost, do not subtract or divide by CAC again without an explicit alternate metric. Route full observed and forecast LTV work to `monetization`.

LTV:CAC is incomplete without payback, cash requirement, forecast error, marginal economics, retention, capacity, concentration, and customer value. Do not enforce a universal ratio.

## Accounting Contribution Payback

Define accounting contribution payback as the earliest supported horizon `h` where:

```text
cumulative compatible contribution before acquisition through h
>= compatible acquisition cost
```

Return `no observed payback` if the cohort has not crossed the threshold by the mature observed cutoff. A forecast payback date must be labeled conditional, use a compatible forecast, expose uncertainty, and preserve the observed portion. Do not use revenue or gross billings as periodic contribution.

State whether payback is evaluated at period start, end, or from supported within-period timing. Do not interpolate uniformly when contribution or acquisition timing is lumpy.

## Cash Payback

Define cash payback as the earliest supported horizon where cumulative net cohort cash after declared acquisition and service outflows reaches or exceeds zero. Model:

- committed and paid acquisition cost;
- invoice, collection, deposit, installment, and receivable timing;
- refunds, chargebacks, credits, bad debt, and tax;
- supplier, inventory, inference, partner, support, sales, and implementation cash outflows;
- annual prepayment, deferred revenue, working capital, currency, and FX.

Annual prepayment can improve cash payback without proving retention or accounting contribution. Long receivable terms can weaken cash payback despite recognized revenue. Keep both views.

## Forecast, Sensitivity, And Calibration

Separate actual-to-date contribution and cash from forecast remainder. Expose retention, expansion, contraction, price, cost, refund, collection, tail, currency, and capacity assumptions. Back-test decision-relevant forecasts against mature cohorts with signed error, segment calibration, drift, and decision impact.

Use bounded intervals when supported or named downside, base, and upside scenarios when probability calibration is absent. Show which input changes reverse the decision. Do not use extra decimals, a point-estimate confidence score, or a best cohort as certainty.
