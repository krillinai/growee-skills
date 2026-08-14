---
name: customer-health-modeling
description: Use when a team needs to specify, build, audit, validate, calibrate, compare, monitor, or refresh a customer or account health model, scorecard, renewal-risk model, churn-risk model, value-realization signal, or decision threshold; reconcile customer hierarchies, prediction times, labels, features, censoring, leakage, calibration, capacity, reason codes, drift, privacy, and safe action boundaries without scoring or routing named customers in live systems.
---

# Customer Health Modeling

Build a versioned, decision-specific view of current customer value or a calibrated prediction of a defined future customer outcome. Health is not customer truth, one universal score, usage volume, renewal status, sentiment, or expansion propensity alone. Separate observed state, prediction, causal mechanism, treatment response, recommendation, action, and outcome.

Read [customer-health-contract-and-labels.md](references/customer-health-contract-and-labels.md) before accepting the customer entity, hierarchy, decision, outcome, prediction time, horizon, label, cohort, maturity, or evidence. Read [features-models-and-validation.md](references/features-models-and-validation.md) before using product, support, relationship, commercial, or human signals; designing features; selecting a rule, scorecard, survival, or predictive model; or validating leakage, discrimination, calibration, and thresholds. Read [decisions-monitoring-and-governance.md](references/decisions-monitoring-and-governance.md) before creating action bands, reason codes, suppressions, overrides, monitoring, market transfer, privacy, or external handoffs. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Define a calculation-ready customer, outcome, feature, label, validation, and decision contract when compatible evidence is unavailable |
| `build` | Build a bounded rule, dimensional view, scorecard, survival model, or prediction specification from supplied compatible evidence |
| `audit` | Inspect an existing model, score, dashboard, band, route, or claimed outcome for validity, leakage, calibration, safety, and governance |
| `validate` | Evaluate a supplied model or ruleset on mature out-of-time outcomes and the intended decision population |
| `monitor` | Review population, features, labels, calibration, performance, actions, and outcomes for drift or feedback |
| `refresh` | Preserve the prior version and update affected data, labels, features, model, thresholds, actions, or governance after material change |

Name one primary mode. Use `evidence-pending`, `infeasible`, `partially specified`, `descriptive-only`, `validation-pending`, `decision-ready`, `blocked`, `superseded`, or `retired` for the record state. A state or color does not prove customer value, contract outcome, causal mechanism, approval, action, or improvement.

## Own A Narrow Modeling Boundary

This Skill owns the health-model decision contract, customer hierarchy for modeling, prediction-time snapshot, outcome and label contract, feature availability and leakage audit, dimensional or model specification, mature validation, calibration, action-capacity threshold evidence, reason and suppression interface, drift monitoring, versioning, and approval-ready handoffs.

Route recurring-value and churn mechanisms to `retention`; engagement distributions to `retention`; cohorts and maturity tables to `retention`; product-qualified expansion signals and expansion strategy to `customer-expansion-strategy`; lifecycle, account, contract, renewal, and revenue-system reconciliation to `growth-operations`; customer segments and ICPs to `positioning`; causal treatment effects to `growth-measurement`; lifecycle messages to `lifecycle-marketing`; prices and packages to `monetization`; source implementation to `growth-measurement`; data defects to `growth-measurement`; forecasts to `growth-measurement`; and LTV or unit economics to their owning Skills.

A health model may consume compatible specialist outputs or create a bounded signal contract for an accountable workflow. It does not diagnose the full customer mechanism, choose an expansion strategy, renew a contract, route an account, contact a customer, or change service.

## Freeze The Customer And Decision Contract

Record model ID and version, mode and state, decision and alternatives, accountable owner and reviewers, modeled entity, customer and commercial hierarchy, eligible population and exclusions, product and value scope, market and locale, prediction or assessment time, feature cutoff, outcome, horizon, observation and label-finalization windows, natural opportunity, model and threshold versions, action capacity, review, expiry, privacy boundary, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Preserve source, owner, event time, availability time, as-of cutoff, population, entity, definition, version, maturity, missingness, limitation, contradiction, correction, and lineage. Do not invent customers, features, labels, scores, probabilities, thresholds, benchmarks, reasons, owners, actions, dates, approvals, or effects. Missing values remain distinct from zero.

Keep current observed state, reported signal, descriptive health dimension, model prediction, confidence or uncertainty, causal explanation, treatment response, target, recommendation, review, approval, authorization, action, verification, and customer or business result separate.

## Resolve Customer Hierarchy And Scope

Define beneficiary, user, guest, admin, champion, buyer, payer, approver, executive sponsor, account owner, workspace, team, subsidiary, parent, legal customer, contract, subscription, product, module, invoice, opportunity, and renewal relationships as applicable. Freeze the modeled unit. Do not let one power user, product, contract, or seller opinion silently define whole-account health.

Preserve user, workflow, team, product, account, contract, relationship, service, and commercial outcomes separately. Define aggregation, role, weighting, coverage, shared use, missing participants, cross-product, cross-contract, and parent-child rules. Split models or views when customer value, product, contract, lifecycle, outcome, horizon, or action differs materially.

## Define One Observable Outcome And Horizon

Choose one outcome per model: value realization, repeated value, product retention, renewal, contraction, partial churn, full churn, support escalation, successful implementation, expansion readiness, or another explicit state. Do not combine them into a universal health label.

Define eligibility, prediction time, outcome start and end, due condition, grace, finalization, competing events, censoring, re-entry, missing outcome, and revision. Separate fixed-term, auto-renewal, month-to-month, usage, transactional, marketplace, and other commercial models. A missing renewal is not churn; a contract is not customer value; NRR is not sufficient customer health.

Use lifecycle- and opportunity-compatible windows. Preserve new, implementing, first-value, recurring-value, mature, suspended, incident, security-review, renewal, migrated, paused, not-due, unknown, and censored states. Do not compare immature or low-frequency customers with mature high-opportunity customers as equivalent.

## Build Leakage-Safe Features

For each feature record entity, value meaning, source, event time, ingestion and availability time, window, aggregation, population coverage, direction, transformation, missingness, version, evidence, reason, and exclusion. Use only information available at the prediction time and through the approved operating process.

Keep product value, access, adoption, engagement, reliability, implementation, support, success, survey, relationship, contract, billing, price, renewal, expansion, and churn evidence separate. Audit future outcomes, post-outcome notes, later invoices, post-treatment behavior, final reasons, outcome-driven overrides, human workflow stages, proxies, identity joins, and repeated customer rows for leakage.

Missing telemetry is not zero use; no support ticket is not satisfaction; no survey response is not a detractor; no note is not no relationship; and no invoice is not nonpayment. Preserve missing, zero, unavailable, not applicable, not due, late, suppressed, disconnected, and source-incident states. Model informative missingness only with an explicit interpretation and sensitivity.

Treat human judgments as attributable, versioned signals. Record observer, role, time, rubric, evidence, uncertainty, disagreement, coverage, and correction. Do not infer emotion, authority, intent, or customer truth from sentiment, attendance, title, or internal optimism.

## Choose A Model That Matches The Decision

Prefer a disaggregated dimensional view when the decision needs several noncompensable conditions. Use a transparent ruleset or scorecard only when dimensions, weights, blocker rules, missingness, evidence coverage, threshold rationale, and sensitivity are declared. Never invent a universal 0-100 score.

Use binary, multiclass, time-to-event, competing-risk, ordinal, hierarchical, or other predictive models only when the entity, outcome, horizon, censoring, prevalence, features, sample, and decision fit. Begin with prevalence, naive, prior-model, and simple rules-based baselines. Complexity, AI, feature importance, high accuracy, or a large training table does not establish usefulness.

Train and validate with customer- and hierarchy-safe splits, prediction-time snapshots, and out-of-time mature outcomes. Prevent the same account family or future period from leaking across sets. Preserve feature, label, dataset, model, calibration, threshold, and validation versions.

## Validate For The Intended Action

Report calibration at the decision horizon; discrimination; precision, recall, specificity, false-positive and false-negative consequences; lift and gains; uncertainty; threshold sensitivity; group error; abstention; and evidence coverage as applicable. Accuracy on a rare outcome is insufficient. A top decile is not a red state by default.

Define thresholds or bands from the action, service capacity, cost, customer impact, risk, review, and uncertainty. Show counts and base rates beside scores or probabilities. Use reason codes grounded in observable pre-cutoff evidence; do not expose sensitive attributes, internal labels, or unverifiable narratives.

Prediction does not establish cause or which treatment helps. Define a separate action-specific counterfactual, eligibility, exposure, outcome, horizon, guardrails, and decision rule when intervention evidence is needed. High churn risk can coexist with low preventability; high expansion propensity can coexist with weak customer value or unsafe timing.

## Govern Decisions, Suppressions, And Monitoring

For every proposed use define eligible model population, receiving role, permissible decision, capacity, threshold or band, reason codes, evidence, review, override, abstain, suppression, expiry, feedback, later outcome, correction, appeal, and audit. Suppress or require review for incidents, unresolved complaints, implementation, security review, missing authority, prior decline, do-not-contact, ineligible roles, immature evidence, and capacity overflow as appropriate.

Monitor population, feature, source, missingness, label, prevalence, calibration, discrimination, threshold, action mix, overrides, suppressions, customer impact, outcome delay, intervention contamination, and feedback drift. Define refresh, recalibration, fallback, repair, and retirement triggers. Preserve old predictions, outcomes, thresholds, overrides, actions, and models; build a revision bridge rather than rewriting history.

## Handle Markets, Privacy, And Actions

Treat every market as a new customer hierarchy, product, value, identity, telemetry, CRM, support, contract, payment, invoice, renewal, label, model, threshold, service, source, privacy, and ownership boundary. For China, distinguish market, legal entity, language, locale, currency, timezone, product, platform, identity, payment, invoice, data, consent, privacy, sources, and locally accountable review. Translation and currency conversion do not validate transfer. Avoid legal, tax, regulatory, provider, accounting, approval, causal, or performance conclusions.

Use aggregate, redacted, pseudonymous, minimum-necessary, and small-cell-suppressed evidence. Do not ingest direct identifiers, private messages, call recordings, keystrokes, precise locations, health, protected traits, compensation, employee reviews, payment details, private customer content, or full histories when bounded evidence suffices. Do not rank named people, infer vulnerability, deny service, personalize price, pressure sales, set employee workloads, or make employment or other consequential decisions.

## Deliver And Stop At The Boundary

Follow [output-contract.md](references/output-contract.md). Deliver the model and decision contract; customer hierarchy; outcome and label contract; source and prediction-time manifest; feature, missingness, leakage, maturity, and censoring audits; baseline and model specification; validation, calibration, threshold, capacity, reasons, suppressions, monitoring, drift, versions, market, privacy, handoff, pinned-source, external-action, and completion records.

Create and read local artifacts only. Do not access authenticated product, analytics, warehouse, CRM, billing, finance, support, success, sales, HR, experiment, messaging, or cloud systems; export customer data; train or deploy production models; score, rank, route, or enrich named customers or people; contact anyone; change contracts, renewals, prices, discounts, service, support, permissions, ownership, lifecycle state, dashboards, alerts, forecasts, or records; publish; send; spend; or claim retention, renewal, expansion, customer, or business improvement without separate task-level authorization and verification.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, entity, hierarchy, outcome, prediction time, cutoff, horizon, eligibility, lifecycle, natural opportunity, maturity, censoring, source availability, label, feature, missingness, leakage, baseline, model, validation, calibration, threshold, capacity, reasons, suppressions, uncertainty, group error, drift, privacy, market, versions, and handoffs are explicit; unlike states are not one score; missing is not zero; future information does not leak; accuracy does not replace calibration; risk is not cause; prediction is not treatment effect; score is not authorization; specialist work is routed; and no external action occurred.
