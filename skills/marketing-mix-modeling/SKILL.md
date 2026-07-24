---
name: marketing-mix-modeling
description: Use when a team needs to specify, build, audit, calibrate, compare, or refresh a Marketing Mix Model or Media Mix Model; estimate aggregate channel contribution, carryover, saturation, response curves, marginal returns, or budget scenarios from time-series or market-level outcomes and media; reconcile experiments, attribution, forecasts, economics, and allocation decisions without accessing live systems or changing spend.
---

# Marketing Mix Modeling

Build a versioned aggregate model of how media and other growth inputs relate to a reconciled customer or business outcome across time and markets. Preserve identification assumptions, baseline, carryover, saturation, experiments, uncertainty, and supported response ranges so an MMM informs decisions without turning fit, platform credit, or modeled contribution into causal certainty.

Read [model-and-data-contract.md](references/model-and-data-contract.md) before accepting the decision, outcome, entity, market, time grain, sources, media, controls, vintages, or feasibility. Read [transformations-identification-and-estimation.md](references/transformations-identification-and-estimation.md) before choosing adstock, lag, saturation, priors, constraints, controls, pooling, interactions, or an estimation method. Read [validation-calibration-and-decisions.md](references/validation-calibration-and-decisions.md) before validating, calibrating with experiments, reporting contribution, building response curves, comparing models, or creating budget scenarios. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Define a calculation-ready model and measurement contract when compatible aggregate evidence is unavailable |
| `feasibility` | Decide whether history, variation, sources, outcomes, dimensions, and calibration can support the intended decision |
| `build` | Estimate and validate a bounded model from supplied compatible data |
| `audit` | Inspect an existing model, contribution report, response curve, scenario, or decision for data, identification, validation, and governance failure |
| `calibrate` | Reconcile an existing MMM with compatible experiment or other causal evidence without forcing agreement |
| `refresh` | Preserve the prior version and update affected data, transformations, assumptions, model, calibration, or decisions after material change |

Name one primary mode. Use `evidence-pending`, `infeasible`, `partially specified`, `estimable`, `descriptive-only`, `calibration-pending`, `decision-ready`, `blocked`, `superseded`, or `retired` for the record state. A state does not prove causality, approval, deployment, allocation, spend, or incremental growth.

## Own One Aggregate Decision Boundary

This Skill owns the aggregate model contract, model-ready outcome and input panel, feasibility and identification audit, media transformations, estimation specification, model comparison, experiment calibration bridge, contribution reconciliation, supported response curves, uncertainty, model versions, and decision-bounded scenarios.

Route person-, account-, device-, touchpoint-, lookback-, and journey-credit rules to `attribution-analysis`; one causal test or quasi-experimental readout to `experiment-design`; future outcome projections to `growth-forecasting`; customer-level acquisition and channel strategy to `acquisition-strategy`; CAC, contribution, payback, and LTV to `unit-economics-analysis`; shared resource allocation to `growth-budget-allocation`; metric contracts to `growth-metrics-design`; event and source implementation to `tracking-plan`; source defects to `growth-data-quality-audit`; revenue-system reconciliation to `revops-audit`; and campaign operations to the applicable planning or advertising Skill.

MMM may consume compatible outputs from those Skills or provide bounded response evidence to them. It does not replace their decisions, approve spend, or operate channels.

## Freeze The Model Contract

Record model ID and version, mode and state, decision and alternatives, accountable owner and reviewers, outcome and value meaning, entity or aggregate unit, market hierarchy, product and business model, time grain, history, as-of cutoff, outcome maturation, scenario horizon, currencies and accounting basis, media and contextual-input scope, experiment and calibration scope, evidence state, privacy boundary, review, expiry, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Preserve source, owner, extraction and availability time, collection window, definition, market, unit, version, revision, maturity, missingness, transformation, limitation, contradiction, and lineage. Do not invent outcomes, spend, exposure, controls, coefficients, priors, decay, saturation, experiments, contribution, returns, budgets, targets, owners, dates, approvals, or impact. Missing values remain unavailable until a documented treatment is justified.

Keep observed outcome, platform-reported credit, attributed credit, descriptive association, modeled contribution, calibrated incremental estimate, forecast, scenario, target, plan, budget, recommendation, approval, authorization, spend, verification, and business result separate.

## Reconcile The Outcome Before Modeling

Define one decision-relevant company outcome by entity, eligibility, state, event, unit, time, market, currency, tax and accounting basis, refund and reversal treatment, source, cutoff, maturity, and revisions. Reconcile product, analytics, CRM, billing, finance, and other authoritative sources with unknown and residual states. Never sum self-attributed platform conversions or revenue as the outcome.

Preserve impressions, reach, clicks, leads, acquisitions, activation, retention, transactions, revenue, GMV, gross profit, contribution, cash, and guardrails as distinct measures. Use an upstream proxy only with a named downstream bridge, lag, maturation plan, and limitation. A revenue model does not establish retained or profitable growth.

## Build A Model-Ready Panel

For every media series record channel, platform, tactic, market, product, audience, unit, spend and exposure basis, currency, cost treatment, availability time, source, coverage, zeros, missingness, revisions, and known measurement changes. Keep spend, impressions, reach, GRPs, clicks, platform conversions, incentives, owned activity, and earned activity separate.

For contextual variables define price, promotion, inventory, distribution, product releases, owned and earned mechanisms, sales capacity, competitor activity, auction conditions, macroeconomics, weather, holidays, seasonality, trend, incidents, and other decision-relevant shocks. Record expected causal role and timing; do not add every available variable or treat mediators and colliders as harmless controls.

Assess history length, time grain, effective observations, variation, channel flighting, dimensionality, sparsity, lags, seasonality, missingness, revisions, structural breaks, outcome maturity, and geographic support. If the panel cannot identify the requested decision, return `infeasible`, `partially specified`, aggregation options, measurement requirements, or alternative evidence instead of a model.

## Transform And Identify Before Estimating

Specify channel- and context-relevant lag, carryover or adstock, saturation, threshold, diminishing-return, interaction, and hierarchical assumptions. Compare defensible geometric, Weibull, distributed-lag, Hill, spline, or other forms only when their support and constraints fit. Do not impose one industry decay, positivity rule, or response form on every channel.

Build an identification register for collinearity, weak variation, budgets responding to demand, reverse causality, search harvesting demand, simultaneous media and promotions, targeting, auction dynamics, omitted variables, seasonality, trend, competitor reaction, spillovers, interference, and measurement error. Priors, sign constraints, fixed effects, instruments, natural variation, experiments, or model structure can constrain an estimate; none silently turns association into truth.

Group or leave channel contribution unresolved when the data cannot separate co-moving channels. Use separate, partially pooled, or hierarchical market effects only with exchangeability assumptions and diagnostics. For marketplaces, preserve participant sides, local networks, media, incentives, supply, liquidity, fulfillment, cross-side effects, congestion, multi-homing, and equilibrium rather than forcing one global outcome.

## Validate Prediction, Structure, And Decisions Separately

Compare against naive and seasonal baselines. Use compatible holdouts, rolling-origin or out-of-time checks, geographic validation, residual diagnostics, posterior predictive checks, contribution reconciliation, parameter and response stability, sensitivity, and decision robustness. In-sample fit, R-squared, MAPE, sample size, Bayesian machinery, or a narrow interval does not prove causal or decision validity.

Audit experiments for compatible intervention, scope, market, population, outcome, time, exposure, maturity, estimand, power, interference, and quality. Use compatible evidence through a documented prior, likelihood, calibration target, holdout, or validation bridge. Preserve both uncertainties and investigate disagreement; do not force estimates to match or discard unfavorable experiments.

Reconcile baseline, modeled inputs, interactions, residual, and observed outcome. Do not call the intercept organic demand or assign every unexplained movement to paid media. Report joint, unresolved, prior-sensitive, or ranged contribution when required.

## Bound Response And Scenario Use

For every response curve state channel, market, period, spend or exposure unit, transformation, observed support, average and marginal estimand, uncertainty, covariance, saturation, sensitivity, and exclusions. Interpolate within credible support; label or refuse extrapolation. Do not guarantee next-dollar return or a global optimum.

Create allocation scenarios only when they can change a decision and include cash, commitments, creative and audience capacity, inventory, availability, channel and market restrictions, concentration, learning, risk, uncertainty, interactions, protected obligations, reversibility, trigger, stop, and review. Keep model output, scenario, recommendation, budget decision, authorization, spend, and verified result separate. Route allocation and channel selection to their owning Skills.

Preserve model, dataset, outcome, source, transformation, prior, calibration, response, scenario, decision, and code versions. Refresh after material product, price, channel, platform, measurement, privacy, market, structural, or experiment change. Never overwrite prior data vintages, models, actuals, decisions, or failed specifications.

## Handle Markets, Privacy, And Actions

Treat every market as a new product, channel, platform, outcome, currency, calendar, cost, source, structural, calibration, and governance boundary. For China, distinguish market, legal entity, language, locale, currency, timezone, product, platform, app distribution, payment, invoice, data, consent, privacy, media sources, holidays, and locally accountable review. Translation and currency conversion do not validate model transfer. Avoid legal, tax, regulatory, provider, accounting, approval, causal, or performance conclusions.

Use aggregate, redacted, minimum-necessary, and small-cell-suppressed data. MMM normally does not require names, direct identifiers, messages, precise locations, protected traits, health, compensation, payment details, private content, or full histories. Do not score people, target vulnerable groups, deny offers, set individual prices, or export person-level data.

## Deliver And Stop At The Boundary

Follow [output-contract.md](references/output-contract.md). Deliver the model contract and verdicts; outcome reconciliation; source and vintage manifest; media and context panel; feasibility, transformation, identification, estimation, validation, calibration, contribution, response, uncertainty, scenario, version, market, privacy, handoff, pinned-source, external-action, and completion records.

Create and read local artifacts only. Do not access authenticated advertising, analytics, warehouse, CRM, MMP, billing, finance, planning, product, experiment, campaign, or cloud systems; export data; train or deploy production models; change events, sources, dashboards, forecasts, targets, plans, budgets, bids, campaigns, audiences, prices, or customer states; contact people; publish; send; spend; procure; or claim incremental growth or business improvement without separate task-level authorization and verification.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the outcome reconciles; units, markets, periods, vintages, currencies, and definitions are compatible; missing data is not zero; history and variation support the decision or infeasibility is explicit; transformations and priors are versioned; collinearity and endogeneity remain visible; validation exceeds in-sample fit; experiments are reconciled without forced agreement; contribution includes baseline and residual; response stays within support; uncertainty changes scenarios; forecasts, targets, allocations, actions, and results remain separate; market and privacy boundaries hold; specialist work is routed; and no external action occurred.
