---
name: ltv-analysis
description: Use when a team needs to calculate, audit, forecast, compare, validate, or govern customer lifetime value, actual-to-date cohort value, revenue or contribution LTV, retention and survival assumptions, censoring, contractual or repeat-purchase models, expansion and contraction, LTV:CAC, predictive LTV, calibration, uncertainty, or portfolio decisions without changing live systems.
---

# LTV Analysis

Estimate how much value a defined customer cohort has produced and may produce over an explicit horizon. Keep realized value, forecast value, customer value, revenue, contribution, and causal allocation separate; LTV is a versioned decision model, not an intrinsic customer property.

Read [ltv-contract.md](references/ltv-contract.md) before accepting customer, cohort, retention, revenue, cost, or forecast evidence. Read [methods-and-formulas.md](references/methods-and-formulas.md) before calculating observed or forecast LTV. Read [calibration-and-uncertainty.md](references/calibration-and-uncertainty.md) before comparing predictions, cohorts, models, or maturity. Read [decisions-and-governance.md](references/decisions-and-governance.md) before using LTV for acquisition, pricing, treatment, portfolio, privacy, or market-transfer decisions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Inspect an existing LTV definition, calculation, model, report, ratio, forecast, or decision |
| `estimate` | Calculate actual-to-date value or create a bounded forecast from supplied cohort, value, retention, and cost evidence |
| `portfolio` | Compare compatible cohorts, products, channels, markets, or scenarios under one decision and capital boundary |

Name one primary mode, decision, owner, customer and payer entity, cohort, product, market, value basis, horizon, evidence cutoff, model version, and external-action boundary. Public pages may verify visible prices, packages, products, and claims; they cannot establish realized customers, retention, costs, contribution, LTV, CAC, payback, forecast quality, or incrementality.

## Freeze The LTV Contract

Record beneficiary, user, seat, workspace, household, account, legal customer, subscription, contract, order, payer, and marketplace participant hierarchy; acquisition, eligibility, activation, value, purchase, renewal, expansion, contraction, lapse, cancellation, churn, resurrection, reactivation, refund, and deletion states; cohort entry and original denominator; natural frequency and opportunity; product, offer, package, price, market, language, locale, currency, tax, revenue, cost, contribution, discount, cash, horizon, maturity, censoring, tail, terminal, identity, source, quality, privacy, model, uncertainty, calibration, owner, and requested action.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder or vendor statement without inspectable support may be a `reported signal` with no evidence state. Keep observed actual-to-date value, forecast value, scenario, target, benchmark, attributed value, and incremental value distinct.

## Define Customer And Value At The Same Level

Do not combine users, seats, workspaces, accounts, subscriptions, orders, payers, and transactions into one denominator. Define who receives value, who buys, who pays, which entity can retain or churn, and which entity owns revenue and cost. Preserve account hierarchy, multiple products, split payers, mergers, deletions, transfers, reactivation, and unknown identity.

Choose a value basis before calculation:

```text
customer value and eligible opportunity
-> product or service value received
-> booked, billed, paid, refunded, and recognized revenue
-> gross profit
-> contribution after declared decision-relevant costs
```

Revenue LTV is not contribution LTV. Include discounts, refunds, credits, taxes, payment and partner fees, cost of goods, inference or service delivery, fraud, support, implementation, success, incentives, and other variable costs only where the named basis and decision require them. Do not invent missing costs.

## Calculate Observed Value Before Forecasting

For a cohort with original eligible size `N0`, report cumulative actual-to-date value through horizon `h` as the sum of observed cohort value through `h`, divided by `N0`. Keep the original denominator unless the contract explicitly defines another estimand. Show period value, cumulative value, active or opportunity state, refunds, costs, coverage, cutoff, and maturity.

Do not call a two-month cohort lifetime-equivalent to a twelve-month cohort. Compare actual-to-date cohorts only at compatible landmarks, or use separately validated forecasts with uncertainty. Preserve right censoring, late events, seasonality, acquisition mix, product and price versions, market changes, and incomplete refunds.

## Choose A Model For The Value Topology

Classify the process before forecasting: contractual subscription or renewal, usage-based, repeat purchase, seasonal or low-frequency transaction, enterprise contract, marketplace, advertising-supported, or multi-product portfolio. Define active, eligible, at-risk, lapsed, churned, cancelled, resurrected, and reactivated states for that topology.

Use cohort accumulation, survival or hazard, renewal, repeat-purchase opportunity, customer-level prediction, or bounded scenarios only when their assumptions match the decision. A constant-margin divided by constant-churn result is a stationary shortcut, not permanent truth. Never infer an infinite tail, permanent plateau, universal horizon, or one churn rate from short or mixed evidence.

## Expose Forecast Assumptions And Uncertainty

Separate observed periods from forecast periods. State survival or purchase opportunity, value conditional on activity, expansion, contraction, price, cost, refund, discount, tail, terminal, and cash assumptions. Return base, downside, and upside scenarios or an interval appropriate to the evidence; show sensitivity to the assumptions that change the decision.

Back-test every decision-relevant model against mature holdout cohorts. Report aggregate and segment calibration, error distribution, rank quality only where useful, drift, stability, and decision impact. Positive ranking does not excuse systematic overprediction. Do not use future outcomes, post-decision notes, protected traits, or unnecessary private communications as prediction-time features.

## Compare Compatible Economics

Match LTV and CAC on customer entity, cohort, market, product, currency, value basis, horizon, maturity, cost scope, attribution or incrementality basis, and model date. Do not apply a universal LTV:CAC target or scale and stop channels from a ratio alone. Include payback, cash timing, marginal economics, saturation, capacity, concentration, uncertainty, customer value, and risk.

For portfolio work, keep product, market, channel, customer overlap, cannibalization, cross-promotion, transfer pricing, legal entity, currency, tax, and forecast calibration visible. Return comparable scenarios and gates, not an opaque ranking or budget move.

## Route Specialist Work

Route metric contracts to `growth-measurement`; general cohort construction to `retention`; retention-state mechanisms to `retention`; pricing, packaging, and cost architecture to `monetization`; source credit to `growth-measurement`; causal acquisition cost and allocation to `growth-measurement` and `acquisition-strategy`; account expansion to `customer-expansion-strategy`; revenue-system reconciliation to `growth-operations`; and full-system scenarios to `growth-model-design`.

This Skill owns the LTV decision contract, observed cohort value, forecast selection and assumptions, value basis, horizon, censoring, uncertainty, calibration, compatible comparisons, and LTV decision boundaries. It does not redefine adjacent metrics, diagnose retention causes, set prices, assign channel credit, approve budgets, or operate systems.

## Deliver In Order

Return:

1. mode, decision, owner, customer and payer entity, cohort, product, market, value basis, horizon, cutoff, model version, and action boundary;
2. LTV contract, evidence ledger, source coverage, contradictions, and unavailable inputs;
3. entity hierarchy, cohort entry, original denominator, state model, opportunity, identity, and censoring rules;
4. observed period and cumulative value ledger with revenue-to-contribution reconciliation;
5. selected method, assumptions, formulas, forecast horizon, tail, and scenario or interval sensitivity;
6. calibration, error, maturity, quality, segment, drift, privacy, and fairness analysis;
7. compatible LTV, CAC, payback, cash, capacity, cannibalization, and risk comparison;
8. decision gates, remediation, owners, re-read dates, specialist handoffs, pinned Playbook sources, and approval-ready external actions.

For China work, keep market, language, locale, legal entity, customer, beneficiary, payer, product, price, contract, payment, tax, invoice, currency, exchange rate, channel, attribution, identity, consent, data access, storage, transfer, service cost, support, retention, cohort maturity, model calibration, applicable review, and local owner separate. Do not transfer a US model through translation or currency conversion alone, and do not provide legal, tax, accounting, or provider conclusions.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not access product, analytics, warehouse, CRM, billing, payment, finance, support, identity, ad, MMP, data-science, cloud, or other systems; export or reidentify customer data; train, deploy, score, or route customers; change models, dashboards, prices, offers, lifecycle states, bids, budgets, or production data; contact customers or vendors; publish; spend; deploy; or claim LTV or business improvement without separate task-level authorization and required controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, customer and payer entity, cohort, original denominator, eligibility, opportunity, product, market, currency, value basis, revenue, costs, contribution, retention states, maturity, censoring, observed horizon, forecast horizon, tail, terminal value, discounting, cash, model version, assumptions, uncertainty, calibration, error, privacy, fairness, LTV:CAC compatibility, attribution, incrementality, owners, handoffs, pinned sources, and action boundaries are explicit; incompatible entities and horizons were not combined; actual and forecast value were not conflated; revenue was not called contribution; no universal ratio, churn, plateau, tail, provider condition, forecast, approval, or result was invented; and no external action occurred.
