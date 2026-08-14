# Model And Data Contract

## Model Contract

| Field | Required content |
| --- | --- |
| Identity | Model ID, version, mode, state, prior version, owner, reviewers, approvers |
| Decision | Decision served, alternatives, horizon, acceptable uncertainty, review and expiry |
| Outcome | Entity, eligibility, state, event, unit, value meaning, source, maturity, accounting and revisions |
| Panel | Market or aggregate unit, time grain, history, cutoff, timezone, products, currencies, hierarchy |
| Inputs | Paid, owned, earned, product, price, promotion, inventory, distribution, competition and external context |
| Evidence | `verified`, `inferred`, `unavailable`, or `not applicable`; source, as-of, version, limitation |
| Governance | Privacy, access, correction, calibration, refresh, external actions, supersession |

Keep observed outcome, platform report, attributed credit, association, modeled contribution, calibrated incrementality, forecast, target, scenario, plan, budget, recommendation, approval, spend, and verified result separate.

## Outcome Reconciliation

Choose the outcome that matches the decision. Define customer, account, order, transaction, subscription, marketplace side, legal entity, or other unit; eligibility; acquisition, activation, retained value, payment, refund, cancellation, reversal, churn, and deletion states; time and maturity; market and product; currency, tax, recognition, and cash basis; source and revision policy.

Build a waterfall from the authoritative company total through excluded, duplicate, unknown, immature, refunded, reversed, and residual states. Platform-reported conversions, view-through credit, modeled conversions, MMP credit, CRM stages, invoices, recognized revenue, contribution, and cash are separate observations. Never add overlapping self-attribution as the dependent outcome.

If the mature decision outcome is too delayed or sparse, define separate proxy and mature-outcome models. Record the proxy-to-outcome bridge, lag, cohort, censoring, calibration, expiry, and uncertainty. Do not call proxy response retained or profitable growth.

## Media Input Ledger

| Media series | Market / product / audience | Spend / exposure unit | Currency / cost basis | Source / coverage / availability | Missing / zero / revision | Known change / limitation |
| --- | --- | --- | --- | --- | --- | --- |

Separate spend, planned spend, committed spend, billed spend, accrued spend, cash, impressions, viewable impressions, reach, frequency, GRPs, clicks, platform conversions, and company outcomes. Define gross and net media, fees, rebates, agency cost, production cost, incentives, tax, exchange rate, and shared allocations when relevant.

A zero means the source confirms none in the defined cell. Missing, not available, not applicable, late, suppressed, below reporting threshold, disconnected, and changed definition remain distinct.

## Context And Control Ledger

For price, promotion, inventory, distribution, product releases, owned channels, earned media, referrals, sales capacity, competitor activity, auction conditions, macroeconomics, weather, holidays, incidents, trend, and seasonality, record definition, unit, market, time, source, availability, evidence, expected timing, causal role, change history, and limitation.

Do not add a control because it improves fit. Distinguish confounder, mediator, collider, proxy, common cause, outcome consequence, and external shock for the declared causal question. Preserve omitted-variable risk.

## Data Vintages

Record event time, aggregation period, ingestion time, availability time, revision time, finalization time, extraction cutoff, source version, transformation version, and the value known at each model decision. Do not train, select, calibrate, or back-test with future finalized outcomes or revised inputs unavailable at the declared cutoff.

Preserve missingness, late arrival, backfills, source incidents, taxonomy changes, platform privacy changes, currency restatements, and historical revisions. Create a bridge rather than overwriting old vintages.

## Feasibility Gate

Evaluate:

1. history length and effective observations after lag, seasonality, holdout, and missingness;
2. time grain versus media flighting, outcome lag, and decision cadence;
3. independent temporal or geographic variation by decision-relevant input;
4. dimension count, interactions, hierarchical levels, sparsity, and degrees of freedom;
5. outcome volume, maturation, censoring, noise, and structural breaks;
6. source coverage, compatible definitions, currencies, markets, and revisions;
7. confounding, endogeneity, collinearity, measurement error, and experiment support;
8. spend and exposure support for the requested response scenarios.

Return `infeasible` or `partially specified` when the decision cannot be supported. Offer aggregation, a longer history, fewer predeclared variables, channel grouping, market panels, planned variation, experiment calibration, or a non-MMM evidence design. Never create synthetic history or false precision to force estimation.

## B2B And Marketplace Adaptation

For B2B, preserve contact, account, buying group, opportunity, stage, contract, booking, revenue, contribution, cash, territory, sales capacity, definition changes, long conversion lags, censoring, and sparse wins. Weekly immediate-response MMM may be infeasible even when weekly lead volume exists.

For marketplaces, preserve participant sides, local network, geography, time, supply, demand, match, fulfillment, cancellation, quality, GMV, take rate, contribution, media, incentives, liquidity, support, capacity, cross-side effects, multi-homing, congestion, and equilibrium. Do not collapse them into one outcome or assume side independence.
