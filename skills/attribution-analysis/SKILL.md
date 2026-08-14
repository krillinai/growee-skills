---
name: attribution-analysis
description: Use when work needs to audit attribution and marketing mix models across journeys, media, identity, outcomes, reconciliation, incrementality, calibration, and uncertainty.
---

# Attribution & Marketing Mix

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Marketing Mix Modeling](references/modules/marketing-mix-modeling/SKILL.md)

Assign operational credit under explicit rules, reconcile it to observed customer and business outcomes, and expose how identity, windows, sources, models, and missing evidence change the result. Attribution describes a journey or allocates credit; it does not prove what caused growth or what would disappear if a channel stopped.

Read [attribution-contract.md](references/attribution-contract.md) before accepting source, touchpoint, identity, conversion, customer, revenue, or attribution evidence. Read [models-and-journeys.md](references/models-and-journeys.md) before choosing or comparing first-touch, last-touch, multi-touch, platform, partner, MMP, B2B, account, app, or cross-device views. Read [reconciliation-and-quality.md](references/reconciliation-and-quality.md) before combining platforms, product analytics, CRM, billing, finance, refunds, costs, or downstream value. Read [causal-boundaries-and-governance.md](references/causal-boundaries-and-governance.md) before making incrementality, predictive-model, privacy, automation, or market-transfer claims. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Diagnose an existing attribution report, model, journey, source rule, platform claim, quality problem, or decision |
| `design` | Define a decision-specific attribution contract, journey views, model rules, validation, governance, and implementation handoff |
| `reconcile` | Resolve incompatible counts, entities, windows, systems, revenue states, overlap, unknowns, and downstream outcomes |

Name one primary mode, operational decision, owner, customer or business outcome, entity, product, market, horizon, model or rule version, and external-action boundary. Public information may verify visible channels, offers, pages, partner links, ads, app listings, and dated activity; it cannot establish private journeys, identity, attribution, customers, costs, revenue, retention, model quality, or incrementality.

## Freeze The Attribution Contract

Record customer, person, device, browser, cookie, app instance, email, user, household, contact, account, workspace, buying group, opportunity, subscription, payer, order, and business hierarchy; product, offer, market, language, locale, channel, platform, partner, campaign, content, creative, placement, keyword, referrer, destination, app, store, and offline source versions; eligible audience, touchpoint, impression, view, click, visit, session, response, lead, signup, install, restore, activation, first value, repeated value, retained value, opportunity, contract, order, payment, refund, revenue, contribution, and churn states; source taxonomy, identity, deduplication, touchpoint eligibility, precedence, lookback, conversion, reattribution, direct-return, cross-device, cross-domain, and unknown rules; attribution, prediction, reconciliation, incrementality, cost, quality, privacy, owners, evidence, assumptions, limitations, and requested external actions.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder or platform statement without inspectable support may be a `reported signal` with no evidence state. Keep observed event, attributed credit, reconciled outcome, predicted outcome, causal effect, target, benchmark, and scenario separate.

## Define The Outcome Before Credit

Name the event or value state being attributed and why it supports the decision. Signup, lead, install, opportunity, booking, payment, first value, retained value, revenue, and contribution are not interchangeable. Define entity, eligibility, event and source truth, exclusions, window, natural frequency, maturity, currency, cost scope, market, and product version.

Preserve a state chain compatible with the business:

```text
eligible customer or account
-> eligible touchpoint and observable journey
-> qualified entry or commercial progress
-> first and repeated product value
-> mature customer and business outcome
-> operational attribution view
-> separately supported causal or allocation decision
```

Do not let a locally convenient conversion event replace downstream customer value. Route metric definition and role to `growth-metrics-design` and event implementation to `tracking-plan`.

## Resolve Identity Without Inventing It

Map assignment, touchpoint, conversion, customer, billing, and analysis entities separately. Define deterministic, declared, probabilistic, unavailable, ambiguous, merged, split, disputed, consent-denied, deleted, and unmatched identity states. Never infer a person, household, or company join from similarity alone.

Preserve device, cookie, anonymous session, email, user, workspace, account, buying group, payer, order, and customer as different units. Document join keys, hierarchy, confidence, precedence, collision handling, reidentification risk, consent or authority, retention, correction, and deletion. Report matched, unmatched, duplicate, ambiguous, and unknown coverage against a declared eligible denominator.

## Keep Sources And Journeys Auditable

Define source taxonomy and precedence before comparison. Keep paid, organic, direct, referral, owned, partner, affiliate, sales, product-led, app-store, offline, unknown, and internal traffic distinct where they change a decision. Separate branded and nonbranded intent, new and returning state, acquisition and reactivation, campaign and channel, and initial source and later engagement.

For every eligible touchpoint, define event, viewability or interaction rule, actor, entity, timestamp, timezone, source, campaign and content version, destination, identity state, channel permission, lookback, conversion eligibility, and late-arrival handling. Do not overwrite a known prior source with a direct return by default or convert unknown outcomes into known channels to force 100% coverage.

## Compare Models As Decision Views

First-touch, last-touch, linear, position-based, time-decay, algorithmic, platform, partner-code, MMP, opportunity-source, and custom rules answer different operational questions. State the rule exactly. Do not adopt universal weights or declare one model objectively correct because it assigns the preferred winner.

Compare candidate views by decision use, eligible touchpoints, entity, outcome, identity coverage, lookback, precedence, reconciliation, downstream value, stability over time, segment sensitivity, interpretability, gaming, privacy, and causal validation. Return a sensitivity table showing what credit changes and what does not. Version every rule and revalidate when product, channel, platform, identity, consent, market, or customer behavior changes.

## Reconcile Before Comparing

Do not sum self-attributed platform, partner, MMP, analytics, CRM, billing, or finance counts. Build a waterfall from eligible company outcomes through identity, deduplication, matching, attribution, payment, refund, recognition, retained value, and unknown states. Freeze snapshot, timezone, currency, exchange rate, tax, refund, cancellation, late-arrival, and product versions.

Preserve:

- claimed, observed, matched, attributed, unattributed, unknown, duplicated, excluded, reversed, and disputed outcomes;
- platform, product, CRM, commercial, billing, finance, and customer-value source truths;
- new, returning, reactivated, existing-customer, expansion, and unknown customer states;
- revenue, gross profit, contribution, CAC, payback, and retained economics as separate calculations.

A discrepancy narrows investigation; it does not establish bad attribution or one root cause. Route revenue lifecycle, CRM ownership, routing, stage, forecast, and finance integrity to `growth-infrastructure-assessment`.

## Join Attribution To Mature Value

Compare compatible cohorts by source, intent, market, product, entry state, customer entity, exposure, cohort start, cutoff, maturity, and cost scope. Report absolute outcomes and rates. Preserve activation, retention, contribution, refunds, support, trust, capacity, and quality even when a local conversion metric looks strong.

Do not compare immature weekly signups with mature quarterly customers, users with accounts, or gross bookings with retained contribution. Attribution may operate a channel before long-term value matures, but the decision must label the proxy, later outcome, uncertainty, and re-read date.

## Separate Attribution From Incrementality

Attribution distributes observed credit under a declared rule. Incrementality estimates what happened because an intervention existed. Attributed conversions are not causal lift; a shutdown does not necessarily remove all credited outcomes. Preserve prior intent, organic demand, cross-channel overlap, returning demand, spillovers, selection, seasonality, saturation, and concurrent changes.

For causal allocation, define the intervention, counterfactual, assignment and exposure unit, interference, outcome, maturity, assumptions, guardrails, and decision rule, then route power, holdout, geo, switchback, shutdown, matched, time-series, and readout details to `experiment-design`. Route channel scaling, caps, diversification, and budget scenarios to `acquisition-strategy`.

## Govern Algorithmic Attribution

Freeze prediction time, eligible population, eligible pre-outcome touchpoints, features, label, window, model version, training cutoff, and allowed decision. Exclude future conversion, revenue, renewal, churn, later support, later campaign labels, protected attributes, and unnecessary raw communications from pre-outcome features.

Require lineage, reproducibility, reason codes, out-of-time validation, calibration where relevant, stability, segment error, fairness, drift, abstention, override, audit, fallback, and retraining triggers. Predictive accuracy, fit, or feature importance does not establish causality. Do not auto-route budgets, bids, customers, or actions.

## Route Specialist Work

Route event schemas, identity instrumentation, and lineage to `tracking-plan`; metric roles and contracts to `growth-metrics-design`; funnel and cohort analysis to `growth-diagnosis` and `retention`; causal tests to `experiment-design`; channel quality, saturation, marginal economics, allocation, and campaign setup to `acquisition-strategy`; commercial entities, finance reconciliation, and shared data or decision capability gaps to `growth-infrastructure-assessment`; pricing and contribution design to `monetization`; and platform-specific evidence to the relevant ads audit.

This Skill owns attribution decision framing, identity and source contracts, touchpoint and journey rules, model comparison and sensitivity, overlap and unknown handling, outcome reconciliation, downstream joins, and attribution-versus-incrementality boundaries. It does not implement tracking, operate platforms, approve budgets, or claim causality.

## Deliver In Order

Return:

1. mode, decision, owner, outcome, entity, product, market, horizon, model version, and action boundary;
2. attribution contract and evidence ledger with unknowns, contradictions, and privacy limits;
3. identity hierarchy, match and deduplication states, coverage, joins, and deletion rules;
4. source taxonomy, eligible touchpoints, journeys, lookbacks, precedence, direct and unknown treatment;
5. current model audit or candidate model sensitivity table with decision uses and limitations;
6. platform-to-product-to-commercial-to-finance-to-retained-value reconciliation waterfall;
7. compatible cohort, downstream quality, economics, model quality, and causal-boundary analysis;
8. remediation, validation, governance, specialist handoffs, pinned Playbook sources, and approval-ready external actions.

For China work, keep market, language, locale, legal entity, customer, product, platform, channel, device, app distribution, identifier, consent, purpose, data access, storage, transfer, provider, ad account, CRM, payment, invoice, currency, journey, window, model, applicable review, and local owner separate. Do not infer any provider, platform, legal, identity, consent, commercial, data, or customer condition from translation or geography alone.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not access ad platforms, MMPs, analytics, warehouse, CRM, billing, finance, product, support, identity, clean-room, cloud, or other systems; export user or customer journeys; enrich or reidentify people; change tags, events, identity rules, source fields, windows, models, dashboards, budgets, bids, routing, or production data; contact customers, partners, vendors, or platforms; publish; deploy; spend; or claim attribution, causal, or business results without separate task-level authorization and required controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, outcome, entity, eligibility, source taxonomy, touchpoints, journeys, identity, joins, deduplication, new and returning states, direct and unknown handling, lookbacks, precedence, model rules, windows, versions, market, cohorts, maturity, platform overlap, product outcome, commercial and finance reconciliation, refunds, costs, downstream value, attribution, prediction, incrementality, quality, privacy, governance, handoffs, pinned sources, and external-action boundary are explicit; incompatible counts and entities were not summed; unknowns were not reassigned; signup, install, lead, booking, revenue, and contribution were not conflated; attribution was not called causality; no score, weight, forecast, provider capability, approval, or result was invented; and no external action occurred.
