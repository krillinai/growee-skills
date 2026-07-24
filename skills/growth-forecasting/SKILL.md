---
name: growth-forecasting
description: Use when a team needs to build, audit, compare, reconcile, back-test, calibrate, version, or govern forecasts for customers, demand, acquisition, activation, retention, usage, orders, revenue, contribution, cash, capacity, or other growth outcomes; distinguish actuals, estimates, forecasts, scenarios, targets, plans, and budgets; handle maturity, censoring, seasonality, structural breaks, uncertainty, revisions, or forecast bias without changing live systems.
---

# Growth Forecasting

Forecast a defined growth outcome from an explicit as-of snapshot, compatible observed evidence, versioned assumptions, and a method suited to the value and time topology. Keep actual, estimate, nowcast, forecast, scenario, stress case, target, plan, budget, benchmark, attribution, incrementality, and final outcome separate; a forecast is a calibrated decision input, not a promise.

Read [forecast-contract.md](references/forecast-contract.md) before accepting entities, outcomes, periods, actuals, assumptions, or forecast evidence. Read [methods-and-assumptions.md](references/methods-and-assumptions.md) before selecting a baseline, driver, cohort, time-series, stock-flow, or portfolio method. Read [uncertainty-and-calibration.md](references/uncertainty-and-calibration.md) before returning intervals, scenarios, back-tests, accuracy, bias, revisions, or comparisons. Read [decisions-and-governance.md](references/decisions-and-governance.md) before connecting a forecast to targets, plans, allocation, staffing, privacy, market transfer, or external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Inspect an existing forecast, model, assumptions, data vintage, accuracy claim, process, or decision use |
| `build` | Create a bounded forecast or calculation-ready specification from supplied compatible evidence |
| `portfolio` | Compare and reconcile forecasts across products, markets, segments, horizons, methods, or scenarios |

Name one primary mode, decision, owner, outcome, entity and level, segment, market, product, frequency, as-of date and time, actual period, forecast origin, horizon, evidence cutoff, model and forecast version, review date, and external-action boundary. Public pages and announcements can verify visible products, prices, releases, claims, and historical public events. They cannot establish private actuals, customers, cohorts, conversion, retention, revenue, contribution, cash, pipeline, capacity, assumptions, forecast performance, or causality.

## Freeze The Forecast Contract

Record beneficiary, user, seat, workspace, account, customer, payer, contract, subscription, order, transaction, marketplace participant, and legal-entity hierarchy; outcome and value meaning; eligibility, identity, source, event, state, formula, unit, denominator, frequency, timezone, currency, exchange-rate basis, tax and accounting basis; cohort, segment, product, offer, price, market, channel, platform, version, natural frequency, seasonality, lags, maturity, censoring, late data, revision, and finalization; actual, preliminary actual, estimate, nowcast, forecast, scenario, stress case, target, plan, budget, and benchmark series; drivers, constraints, capacity, interventions, assumptions, methods, uncertainty, calibration, bias, owners, approvals, and requested action.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder or provider statement without inspectable support may be a `reported signal` with no evidence state. Keep zero, missing, late, immature, censored, suppressed, inaccessible, corrected, and not-applicable states distinct.

## Freeze The As-Of Snapshot

For every input record event time, ingestion time, availability time, revision time, finalization time, source version, and value known at the forecast origin. Do not train, calculate, select, or back-test with future outcomes, later refunds, revised classifications, subsequent notes, post-decision features, or final actuals that were unavailable at prediction time.

Preserve forecast vintages. A retrospective explanation using final data is a backcast or analysis, not the original forecast. Never overwrite prior forecasts, actual vintages, or methods; create a revision bridge showing data revisions, assumption changes, model changes, overrides, and previously unknown events.

## Separate Forecast From Adjacent Artifacts

| Artifact | Meaning |
| --- | --- |
| `actual` | Observed value under a declared source, definition, maturity, and finalization state |
| `estimate or nowcast` | Incomplete current-period value inferred from available partial evidence |
| `forecast` | Expected future outcome under the forecasting process and information set |
| `scenario or stress case` | Conditional result if a declared assumption bundle occurs |
| `target` | Desired future outcome, not evidence of likelihood or health |
| `plan` | Approved actions and resources intended to reach an outcome |
| `budget` | Authorized resource or spend boundary |
| `benchmark` | Attributable comparison point with transfer limits |

Do not force a forecast to equal a target or plan. Show the gap and the driver changes required to close it. A target-reaching case remains a scenario until the forecast process supports it.

## Select A Method For The Topology

Begin with a reproducible naive or seasonal baseline. Classify the outcome as time series, cohort maturation, contractual renewal, repeat purchase, usage, stock and flow, marketplace supply and demand, commercial pipeline, capacity-constrained operation, hierarchical portfolio, or a combination.

Use a simple baseline when evidence is thin or behavior is stable; time-series methods for repeatable temporal structure; driver models when defensible inputs, relationships, lags, and constraints are available; cohort methods when entry and age determine outcomes; stock-flow models when opening state, inflows, transitions, outflows, re-entry, and ending state must reconcile; and hierarchical reconciliation when component and total forecasts must coexist. Compare more complex methods against the baseline out of sample.

Do not extrapolate short growth rates indefinitely, multiply best-case rates from incompatible cohorts, average percentages across different bases, treat missing outcomes as zero, or call an equation causal. Model saturation, capacity, cash, seasonality, interventions, structural breaks, product and price changes, market differences, reporting latency, censoring, refunds, reversals, and external dependencies where they change the decision.

## Expose Assumptions And Uncertainty

Separate observed drivers, externally supplied forecasts, inferred relationships, planning assumptions, and scenario assumptions. Record value, unit, source, as-of availability, range, relationship, lag, segment, owner, expiry, and update trigger. Preserve coherent assumption bundles; do not mix mutually inconsistent upside inputs.

Return a point forecast only with uncertainty appropriate to the evidence. Use intervals, quantiles, ranges, scenarios, or explicit unresolved bounds; state method and intended interpretation. Uncertainty can widen, narrow, or become asymmetric with horizon, maturity, constraints, and information. Do not invent probabilities or claim 95% accuracy from a 95% interval.

## Back-Test And Calibrate By Decision

Use rolling-origin or otherwise time-valid holdouts that reproduce the original information set and revision state. Compare against the naive or incumbent baseline. Report signed error and bias, absolute error, scale-appropriate relative or scaled error, interval coverage and width, turning-point performance, calibration, stability, revisions, and decision impact by horizon, market, product, segment, and maturity.

Aggregate accuracy can hide systematic harm. A model may reconcile annually while overpredicting new markets, underpredicting peak weeks, or failing at the horizon used for staffing. Define recalibration, override, fallback, repair, and retirement gates. Do not change metrics or methods after seeing misses without preserving the version history.

## Route Specialist Work

This Skill owns the forecast contract, as-of snapshot, actual and forecast periods, baselines, driver and method selection, assumptions, uncertainty, forecast vintages, back-testing, calibration, bias, revision bridge, comparison, and refresh governance. Route adjacent artifacts without treating the forecast as their approval:

| Need | Route |
| --- | --- |
| Full business topology and stock-flow mechanism design | `growth-model-design` |
| Commercial pipeline, stages, bookings, contracts, finance, and cash reconciliation | `revops-audit` |
| Customer lifetime value, metric contracts, cohort construction, or decision-critical input defects | `ltv-analysis`, `growth-metrics-design`, `cohort-analysis`, `growth-data-quality-audit` |
| Activation, retention, monetization, expansion, or causal mechanisms | `activation`, `retention`, `monetization`, `customer-expansion-strategy`, `experiment-design` |
| Acquisition spend bands and channel allocation | `acquisition-strategy` |
| Organization targets or annual, quarterly, and rolling integrated plans | `growth-target-setting`, `growth-planning-cycle` |
| One investment case or shared cross-functional budget and resource allocation | `growth-investment-case`, `growth-budget-allocation` |
| Recurring weekly, monthly, or quarterly decision review | `growth-operating-review` |
| Organization structure, decision rights, staffing, or one selected initiative plan | `growth-organization-design`, `growth-initiative-planning` |

A specialist output may become a forecast input only with compatible entity, market, version, as-of date, horizon, uncertainty, and owner. The forecast does not approve budgets, hiring, targets, prices, campaigns, product changes, or customer treatment.

## Deliver In Order

Return:

1. mode, decision, owner, outcome, entity, segment, market, frequency, as-of, actual period, origin, horizon, versions, review date, and action boundary;
2. forecast contract, data-vintage ledger, sources, evidence states, definitions, reconciliation, and unavailable inputs;
3. actual, preliminary, estimate, forecast, scenario, target, plan, budget, benchmark, and revision series kept separate;
4. selected baseline and method, topology, equations, drivers, lags, constraints, interventions, structural breaks, and assumptions;
5. point, interval or range, scenario, segment, and portfolio outputs with reconciliation and residuals;
6. rolling back-test, baseline skill, bias, error, coverage, stability, revisions, and decision impact;
7. target and plan gap, sensitivities, thresholds, fallbacks, update triggers, owners, and specialist handoffs;
8. privacy, market transfer, governance, pinned Playbook sources, approval-ready external actions, and completion record.

For China work, keep market, language, locale, customer and payer entities, product, cohort, channel, platform, app distribution, seasonality, holiday and event calendars, price, payment, tax, invoice, currency, exchange rate, attribution, data, identity, consent, storage, transfer, source access, model, calibration, review, and local owner separate. Do not transfer a US model through translation or currency conversion alone, and do not provide legal, tax, accounting, or provider conclusions.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not access analytics, warehouse, CRM, billing, payment, finance, product, ad, app-store, support, experiment, HR, planning, BI, or cloud systems; export or reidentify people; train, deploy, score, or operate models; rewrite actuals; change forecasts, targets, plans, budgets, staffing, dashboards, alerts, prices, campaigns, product, routing, or customer state; contact anyone; publish; send; spend; deploy; or claim forecast or business improvement without separate task-level authorization and required controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, owner, outcome, entity, segment, market, product, frequency, timezone, currency, accounting basis, as-of, event and availability times, actual period, origin, horizon, maturity, censoring, latency, revisions, versions, actual, estimate, nowcast, forecast, scenario, target, plan, budget, benchmark, baseline, method, drivers, lags, constraints, interventions, assumptions, uncertainty, back-test, calibration, bias, errors, coverage, fallback, update triggers, privacy, market transfer, handoffs, pinned sources, and external actions are explicit; future information did not leak; incompatible entities and periods were not combined; actuals were not overwritten; missing was not zero; scenarios were not called forecasts; targets did not determine forecasts; fit was not called causality; unsupported precision was not invented; and no external action occurred.
