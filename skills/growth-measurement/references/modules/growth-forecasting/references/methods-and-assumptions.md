# Methods And Assumptions

Choose the simplest method that matches the outcome topology, beats a declared baseline out of sample, and remains governable for the decision.

## Baselines

Always retain a reproducible comparison such as last observed value, seasonal naive, same period last cycle, trailing average, unchanged cohort curve, or approved incumbent forecast. A complex model that does not improve the decision over the baseline should not replace it.

## Method Selection

| Topology | Suitable starting methods | Required controls |
| --- | --- | --- |
| Stable repeated time series | Naive, seasonal naive, smoothing, trend-seasonal, regression, or time-series model | Frequency, seasonality, interventions, breaks, autocorrelation, horizon |
| Cohort maturation | Age-by-cohort accumulation, survival, renewal, repeat opportunity, or bounded curve | Original denominator, maturity, censoring, mix, product and price versions |
| Stock and flow | Opening stock plus inflows, transitions, outflows, re-entry, ending stock | Reconciliation, identity, lags, rates, capacity, overlapping flows |
| Driver model | Outcome as compatible drivers with explicit relationships | Driver forecast, lag, saturation, interaction, endogeneity, range, owner |
| Marketplace or network | Local supply, demand, matching, fulfillment, liquidity, congestion, and economics | Atomic unit, sides, multi-homing, local capacity, quality, interference |
| Hierarchical portfolio | Bottom-up, top-down, middle-out, or reconciled component forecasts | Overlap, hierarchy, currency, totals, residuals, local versus shared drivers |
| Commercial pipeline | Stage, timing, amount, slippage, loss, capacity, booking and revenue bridge | Route entity and finance controls to `growth-operations` |

Route full business topology and mechanism equations to `growth-model-design`; LTV models to `monetization`.

## Driver Contract

For each driver record definition, entity, unit, source, as-of availability, observed and forecast periods, relationship, lag, saturation, range, uncertainty, segment, interaction, causal status, owner, expiry, and update trigger. State whether it is observed, externally forecast, inferred, assumed, targeted, planned, or scenario-only.

Do not forecast an outcome from target drivers while calling it unbiased. Do not use post-outcome features, later classifications, or final-period values at an earlier origin.

## Cohorts, Maturity, And Lags

Keep original eligibility and denominators. Define entry, age, opportunity, conversion, retention, renewal, refund, recognition, and finalization windows. Treat recent outcomes as immature or right-censored, not zero. Compare actual-to-date cohorts at compatible ages or use separately calibrated forecasts.

Use nowcasting when current-period actuals are incomplete but partial evidence is available. Label it separately from final actual and future forecast. Preserve expected revision and finalization.

## Seasonality And Structural Change

Separate recurring calendar or operational seasonality from one-time shocks. Record holidays, promotions, product releases, pricing and packaging changes, channel starts and stops, platform events, outages, policy changes, market entry, supply disruptions, and macro conditions.

Test or at least flag changes in level, trend, variance, relationships, seasonality, and data definitions. Use intervention terms, segmented windows, shorter training ranges, scenarios, or method reset when supported. Define what evidence triggers re-estimation, fallback, or retirement.

## Constraints And Reconciliation

Apply physical, economic, cash, staffing, sales, support, supply, inventory, fulfillment, platform, trust, safety, and policy constraints where they bind. An unconstrained forecast can exceed reachable demand, capacity, cash, or participant supply.

For portfolio forecasts, reconcile component and total views without hiding residuals. State whether total controls components, components control total, or a reconciliation method adjusts both. Preserve local drivers and market-specific constraints.

## Assumption Register

Each assumption includes exact statement, value or range, unit, basis, evidence state, owner, affected outputs, sensitivity, expiry, trigger, and substitute when unavailable. Keep coherent scenario bundles. Never combine every favorable assumption into the baseline or invent scenario probabilities.
