# Methods And Formulas

Choose the simplest method compatible with the customer, value process, horizon, maturity, and decision. Show inputs, units, assumptions, and missing evidence beside every result.

## Actual-To-Date Cohort Value

For original eligible cohort size `N0` and total observed cohort value `V_t` in period `t`:

```text
Observed cumulative LTV through h = sum(V_t, t = 0..h) / N0
```

Use the same value basis in every period. Display period value, cumulative value, refunds or reversals, costs, active or eligible state, and coverage. Keep `N0` fixed for acquired-customer LTV; dividing by survivors answers a different question.

If `S_t` is the share of the original cohort active or eligible in period `t` and `v_t` is value per active or eligible customer:

```text
Observed cumulative LTV through h = sum(S_t * v_t, t = 0..h)
```

Verify that `S_t` and `v_t` use compatible entities, periods, and denominators. Prefer direct cohort totals when available because averaging averages can conceal weighting errors.

## Revenue And Contribution

Calculate and label separate views:

```text
Revenue LTV_h = cumulative recognized cohort revenue through h / N0
Contribution LTV_h = cumulative declared cohort contribution through h / N0
```

Reconcile refunds, discounts, chargebacks, taxes, fees, cost of goods, delivery, inference, fulfillment, partner share, fraud, incentives, support, implementation, and service cost according to the contract. Do not subtract CAC inside contribution LTV and then compare the result with the same CAC again.

## Contractual Retention

For subscription or renewable contracts, model eligibility, renewal, cancellation, contraction, expansion, resurrection, and timing explicitly. A bounded expected-value forecast may use:

```text
Forecast LTV_H = observed value through k
               + sum(P(active or renewed at t) * E[value_t | active], t = k+1..H)
```

Use survival or hazard estimates that preserve right censoring and tenure. Keep logo, seat, usage, revenue, and contribution retention separate. For annual contracts, do not treat months before renewal eligibility as independent monthly retention events.

## Stationary Shortcut

The common shortcut:

```text
LTV = contribution per active customer per period / churn probability per period
```

requires constant hazard, constant contribution, compatible period units, no meaningful expansion, contraction, resurrection, seasonality, cohort change, discounting, or finite-horizon constraint. Present it only as a stationary geometric scenario. Never call it permanent truth or use it when tenure-varying hazards materially affect the decision.

## Repeat Purchase And Low Frequency

Define purchase opportunity, observation window, seasonality, category cadence, delayed repeat, returns, and dormant versus lost states. Forecast expected future transaction count and value conditional on a declared opportunity process; do not classify every quiet period as churn.

For marketplaces, separate participant side, local network, successful interaction, transaction, take rate, incentives, fulfillment, refunds, and contribution. For advertising-supported products, separate user value and retention from advertiser demand, inventory, price, and revenue. For usage-based products, separate successful usage, variable cost, account retention, and budget or contract limits.

## Expansion And Multi-Product Value

Decompose value changes into price, seats, usage, products, foreign exchange, expansion, contraction, churn, return, and one-time adjustments. Preserve cross-sell exposure, overlap, cannibalization, transfer, and incremental versus reclassified value. Higher NRR does not by itself establish better customer value or healthier forecast LTV.

## Discounting, Cash, And Tail

When timing and capital matter, use a period-compatible discount rate:

```text
Present value = sum(expected contribution_t / (1 + r)^t)
```

State rate, period, nominal or real basis, inflation, currency, cash timing, and whether discounting is omitted. Use an explicit finite horizon unless a terminal method is justified. Show tail contribution separately and test zero-tail, conservative-tail, and alternative-horizon scenarios. Do not let terminal value dominate without visible sensitivity and calibration.

## Model Choice

| Evidence and topology | Suitable starting view |
| --- | --- |
| Mature cohort totals | Actual-to-date cumulative value at common landmarks |
| Contractual retention with censoring | Cohort survival or hazard plus conditional value |
| Repeat purchase with observable opportunity | Opportunity-aware repeat and value model |
| Sparse or changing environment | Bounded scenarios with explicit assumptions |
| Rich customer-level prediction | Pre-outcome features, temporal holdout, calibration, abstention, and governance |
| Several products or markets | Compatible scenario portfolio with overlap and cannibalization |

Use a more complex model only when out-of-time performance and decision value justify added data, privacy, maintenance, and governance cost.
