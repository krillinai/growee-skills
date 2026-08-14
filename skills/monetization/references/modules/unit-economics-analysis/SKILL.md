---
name: unit-economics-analysis
description: Use when a team needs to calculate, audit, model, compare, reconcile, forecast, or govern customer acquisition cost, CAC variants, unit economics, contribution margin, cash payback, accounting payback, LTV:CAC, marginal returns, channel-model fit, freemium economics, marketplace-side economics, or cohort and portfolio economics without changing live systems.
---

# Unit Economics Analysis

Model whether a defined customer cohort produces enough retained contribution and cash to support its acquisition and service system. Treat CAC, LTV:CAC, margin, and payback as versioned outputs of compatible entity, cohort, cost, value, timing, maturity, source, and uncertainty contracts, not intrinsic business properties.

Read [unit-economics-contract.md](references/unit-economics-contract.md) before accepting customer, cohort, cost, value, channel, or accounting evidence. Read [costs-and-cac.md](references/costs-and-cac.md) before calculating media, direct, fully loaded, attributed, incremental, blended, or marginal CAC. Read [value-payback-and-compatibility.md](references/value-payback-and-compatibility.md) before using revenue, gross profit, contribution, cash, LTV, LTV:CAC, or payback. Read [portfolio-decisions-and-governance.md](references/portfolio-decisions-and-governance.md) before comparing cohorts, spend bands, products, channels, segments, markets, freemium paths, or marketplace sides. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Inspect an existing CAC, LTV:CAC, margin, payback, return, channel-economics, or unit-economics claim |
| `model` | Calculate supplied compatible economics or create a calculation-ready model with bounded scenarios |
| `portfolio` | Compare compatible cohorts, products, channels, segments, markets, spend bands, motions, or scenarios under one decision |

Name one primary mode, decision, owner, customer and payer entity, acquisition cohort, product and offer, market, channel or source, acquisition event, cost basis, value basis, observed and forecast horizons, evidence cutoff, model version, review date, and external-action boundary. Public pages can verify visible products, packages, prices, and claims. They cannot establish private spend, customers, retention, costs, contribution, cash, CAC, LTV, payback, incrementality, or forecast quality.

## Freeze The Economics Contract

Record beneficiary, user, lead, signup, activated user, seat, workspace, account, legal customer, subscription, contract, order, payer, transaction, buyer, seller, and marketplace hierarchy; eligibility, acquisition, activation, payment, retention, expansion, contraction, lapse, churn, resurrection, refund, reversal, and deletion states; cohort entry, original denominator, conversion lag, maturity, censoring, and late data; product, offer, package, price, discount, channel, campaign, market, language, locale, currency, tax, invoice, accounting, cash, source, attribution, incrementality, cost, value, horizon, uncertainty, privacy, owner, and requested action.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. An attributable stakeholder, platform, analyst, or vendor statement without inspectable support may be a `reported signal` with no evidence state. Keep zero, missing, late, immature, censored, forecast, target, benchmark, disputed, suppressed, and not-applicable states separate.

## Align Entity, Cohort, And Time

Do not combine registrations, users, accounts, payers, contracts, orders, transactions, and marketplace sides into one acquired-customer denominator. Define who receives value, who buys, who pays, which entity incurs acquisition and service costs, and which entity can retain or churn. Preserve account hierarchy, duplicate identity, shared access, multiple products, transfers, merges, deletion, and unknown state.

Match costs to the cohort they could produce. Define spend and operating periods, conversion lag, attribution window, acquisition event, new versus returning rules, original eligible denominator, refund and cancellation maturity, and observation cutoff. Same-month spend divided by same-month customers is invalid when the conversion or sales cycle crosses periods unless a compatible bridge proves the match.

## Build The Cost Bridge

Classify every cost by purpose, entity, cohort, product, channel, market, period, currency, accounting treatment, cash date, source, and allocation rule. Keep media or placement, agency, creative, tooling, data, referral and partner fees, incentives, discounts, free-product support, sales development, sales labor, commissions, onboarding, implementation, and shared costs visible where decision relevant.

Report named variants rather than one unqualified CAC:

```text
declared CAC
= declared compatible acquisition costs
/ qualified acquired entities produced under the matching contract

incremental CAC
= incremental acquisition cost versus counterfactual
/ incremental qualified acquired entities versus counterfactual

marginal CAC for an observed spend band
= change in compatible cost
/ change in qualified acquired entities
```

Do not call media-only CAC fully loaded, cost per lead customer CAC, attributed CAC incremental CAC, or historical blended CAC the next-customer cost. If incremental customers are zero, negative, immature, or too uncertain, do not force a finite incremental CAC. Preserve fixed, variable, committed, allocated, sunk, avoidable, accounting, and cash costs separately; state every allocation driver and residual.

## Reconcile Value Before Ratios

Use a value waterfall with compatible customer entity, cohort, period, currency, and source:

```text
booked or contracted value
-> billed value
-> collected cash
-> recognized revenue after discounts, credits, refunds, tax, and reversals
-> gross profit after declared direct delivery cost
-> contribution after declared decision-relevant variable costs
```

Keep customer value, company revenue, gross profit, contribution before acquisition, contribution after acquisition, and cash separate. Define product, infrastructure, AI inference, fulfillment, inventory, payment, partner, support, success, implementation, fraud, loss, collection, incentive, and other costs. Missing cost is unavailable, not zero.

Consume LTV only when a validated `monetization` output preserves compatible entity, cohort, value basis, horizon, maturity, market, currency, version, assumptions, uncertainty, and whether acquisition cost is already included. Do not subtract CAC twice or divide account CAC into user LTV. A forecast remainder is not observed value.

## Calculate Payback On A Declared Curve

For each original acquired cohort, show periodic and cumulative contribution before acquisition, acquisition cost, cash inflows, cash outflows, refunds, service costs, and maturity. Accounting contribution payback is the first supported horizon at which cumulative compatible contribution before acquisition equals or exceeds acquisition cost. Cash payback is the first supported horizon at which cumulative net cash equals or exceeds zero after acquisition and other declared cash outflows.

Do not use revenue payback, treat invoices as collections, ignore refund windows, or assign the same date to accounting and cash payback without evidence. State period convention and interpolate only when within-period timing is supported. When contribution never becomes positive within the observed or bounded forecast horizon, report no observed payback or a conditional scenario rather than an invented date.

## Compare Average And Marginal Economics

Build local cohort and spend-band views before aggregation. Show absolute customers, costs, value, contribution, cash, weights, maturity, and uncertainty beside ratios. Separate historical blended, channel, segment, sales-motion, fully loaded, attributed, incremental, and marginal economics.

For portfolio work, preserve customer overlap, shared costs, cannibalization, cross-promotion, capacity, saturation, auction and audience changes, sales and onboarding constraints, concentration, dependency, currency, tax, price, product version, and market transfer. A marginal observation is a bounded spend band, not a promise about the next budget level.

For freemium, separate signup, activation, qualified product use, payer, account, conversion, and retained-value cohorts; include free-user serving, support, abuse, and distribution value where relevant. For marketplaces, model buyer, seller, transaction, GMV, take-rate revenue, refunds, incentives, contribution, liquidity, and multi-homing separately before any joint economics.

## Preserve Uncertainty And Decision Boundaries

Return observed actuals, estimates, forecast scenarios, targets, benchmarks, attributed outputs, incremental outputs, and causal claims separately. Do not backsolve evidence to reach a universal 3:1 LTV:CAC, twelve-month payback, margin target, or other benchmark. Record benchmark source, population, definition, date, and relevance.

Show uncertainty from identity, cohort matching, conversion lag, attribution, counterfactual, cost coverage, allocation, retention, value, refunds, maturity, forecast, currency, capacity, saturation, and structural change. Use ranges or named scenarios supported by the method; show sensitivity and the smallest evidence change that reverses the decision. Extra decimals and uncalibrated confidence scores do not reduce uncertainty.

## Route Specialist Work

This Skill owns the unit-economics decision contract, entity and cohort compatibility, acquisition cost bridge, CAC variants, contribution and cash reconciliation, accounting and cash payback, LTV compatibility, marginal and portfolio comparison, sensitivity, uncertainty, and governance. Route full LTV estimation to `monetization`; metric contracts to `growth-metrics-design`; general cohorts to `retention`; acquisition source credit to `attribution-analysis`; causal lift to `experiment-design`; channel design and budget allocation to `acquisition-strategy`; pricing, packaging, and cost architecture to `monetization`; retention mechanisms to `retention`; financial and revenue-system reconciliation to `growth-infrastructure-assessment`; future outcomes to `growth-forecasting`; movement bridges to `retention`; and full business scenarios to `growth-model-design`.

Specialist evidence may enter the model only with compatible entity, cohort, market, period, basis, version, maturity, uncertainty, and owner. Unit economics does not approve budgets, prices, staffing, customer treatment, forecasts, or external actions.

## Deliver In Order

Return:

1. mode, decision, owner, customer and payer entity, acquisition cohort, product, offer, market, channel, acquisition event, cost and value bases, horizons, cutoff, model version, review date, and action boundary;
2. economics contract, evidence ledger, source coverage, contradictions, unavailable inputs, identity, cohort, conversion-lag, maturity, and privacy rules;
3. acquisition cost bridge with direct, allocated, fixed, variable, committed, avoidable, accounting, cash, attribution, incrementality, and residual states;
4. media, direct, fully loaded, blended, channel, segment, attributed, incremental, and marginal CAC views supported by the evidence;
5. value waterfall, observed cohort contribution, compatible LTV, accounting payback, cash payback, refunds, working capital, and maturity;
6. cohort, spend-band, product, channel, segment, market, freemium, marketplace, mix, overlap, concentration, saturation, capacity, and portfolio views;
7. uncertainty, sensitivity, forecast calibration, targets, benchmarks, thresholds, triggers, counterevidence, and decision states;
8. specialist handoffs, governance, refresh and expiry, pinned Playbook sources, approval-ready external actions, and completion record.

For China work, keep market, language, locale, legal entity, customer and payer, product, offer, contract, price, discount, channel, platform, attribution, acquisition, payment, invoice, tax, refund, currency, exchange rate, revenue, cost, contribution, cash, identity, consent, storage, transfer, source access, model, review, and local owner separate. Translation and currency conversion do not validate a transferred economics model. Require current direct sources and locally accountable review for time-sensitive conditions; do not provide legal, tax, accounting, regulatory, or provider conclusions.

## External-Action Boundary

This Skill may read supplied artifacts and authorized public sources and create local artifacts. Do not access analytics, warehouse, CRM, billing, payments, finance, product, ad, MMP, support, identity, BI, cloud, partner, marketplace, or customer systems; export, merge, or reidentify people; train, deploy, score, rank, route, price, suppress, or otherwise treat customers; change costs, models, dashboards, forecasts, targets, prices, offers, bids, budgets, channels, staffing, or production data; contact anyone; publish; send; spend; deploy; or claim economics or business improvement without separate task-level authorization and required controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, owner, customer and payer entities, identity, acquisition event, cohort, original denominator, conversion lag, product, offer, market, channel, period, currency, accounting, cash, acquisition costs, allocations, CAC variants, attribution, incrementality, marginal bands, revenue, gross profit, contribution, service costs, refunds, retention, LTV compatibility, observed and forecast horizons, maturity, censoring, accounting payback, cash payback, overlap, mix, saturation, capacity, uncertainty, sensitivity, benchmarks, privacy, market transfer, handoffs, pinned sources, and external actions are explicit; unlike entities were not combined; missing costs were not zero; media-only was not fully loaded; attributed was not incremental; average was not marginal; revenue was not contribution or cash; LTV did not double-count CAC; immature cohorts were not lifetime-equivalent; GMV was not revenue; targets did not become evidence; unsupported precision, causality, approval, and results were not invented; and no unauthorized action occurred.
