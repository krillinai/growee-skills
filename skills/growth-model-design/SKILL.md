---
name: growth-model-design
description: Use when work needs to design growth models and size opportunities across lifecycle behavior, economics, reach, capacity, overlap, scenarios, and risk.
---

# Growth Model & Opportunity

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Growth Opportunity Sizing](references/modules/growth-opportunity-sizing/SKILL.md)

Build an explicit, falsifiable explanation of how a defined customer reaches value, retains, creates a durable business outcome, and replenishes future growth inputs. Use equations and diagrams to expose assumptions, not to manufacture causality, certainty, or exponential forecasts.

Read [model-contract.md](references/model-contract.md) before mapping entities, states, edges, time, evidence, economics, capacity, or model versions. Read [modeling-methods.md](references/modeling-methods.md) before reconciling equations, running scenarios, testing sensitivity, or selecting a model constraint. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `map` | Create a bounded current-state model and measurement contract |
| `audit` | Test an existing diagram, spreadsheet, equation, dashboard, or narrative for decision usefulness |
| `scenario` | Reconcile supplied compatible inputs and compare explicit assumption changes or ranges |

Name one primary mode, decision, owner, horizon, and permitted action. If private evidence is unavailable, complete a public-evidence-bounded hypothesis and calculation-ready specification rather than inventing coefficients.

## Freeze The Model Contract

Record the model version; decision and owner; product and business model; customer, participant, segment, role, use case, payer, market, and period; natural frequency; canonical entities and identity rules; value and durable-outcome definitions; opening stocks, inflows, transitions, outflows, ending stocks, and re-entry; currency and accounting basis; acquisition, activation, retention, monetization, propagation, expansion, and reinvestment mechanisms; operational and financial capacity; saturation, platform, trust, quality, safety, regulatory, and environmental constraints; sources, definitions, evidence states, causal status, uncertainty, and requested external action.

Version the model when the customer, product, promise, channel, price, cost, entity, event, attribution rule, market, technology, competition, regulation, capacity, or decision horizon changes materially. Do not overwrite history with incompatible definitions.

## Build A Business-Specific Topology

Map only mechanisms relevant to the declared business:

    defined customer and problem
    -> qualified acquisition input and promise
    -> first credible value
    -> repeated value and retention
    -> revenue or another durable outcome
    -> propagation, expansion, resource, or reinvestment output
    -> qualified next growth input

For every node, state entity, eligibility, state, value meaning, stock or flow, unit, and source. For every edge, state source and destination entities, event, numerator, denominator, window, lag, cohort, maturity, segment, cost, quality, owner, evidence state, causal status, and alternative explanations.

A lifecycle names customer stages. A funnel measures ordered transitions. A loop tests whether an output creates a later qualified input. A dashboard reports metrics. A forecast projects assumptions. A growth model connects selected mechanisms and their economics for a specific decision. Do not relabel one artifact as another.

## Validate Before Calculating

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder claim without inspectable support may be a `reported signal` with no evidence state. Keep descriptive association, mechanism evidence, causal identification, and scenario assumption distinct.

Calculate only when entity, segment, market, eligibility, identity, definition, source, currency, period, cohort, window, maturity, and model version are compatible. Preserve missing values, zeroes, unknown populations, late data, range assumptions, and definition breaks. Never multiply the best rates from different cohorts, markets, products, time periods, or entity levels.

Separate stocks from flows. Reconcile opening populations to retained and churned components before adding new or resurrected entities; do not subtract churn twice. Separate opening, new, expansion, contraction, churned, and ending revenue under one declared accounting policy. Show formulas, units, substituted values, results, and reconciliation differences.

## Test Scenarios And Constraints

Keep the baseline unchanged and label every scenario input as supplied, observed, inferred, or assumed. Change one decision-relevant assumption or a declared bundle, preserve ranges and lags, and show outcome sensitivity plus guardrail effects. A scenario is not a forecast; a fitted relationship is not automatically causal or incremental.

Test Market-Product, Product-Channel, Channel-Model, and Model-Market Fit as connected assumptions before treating the topology as coherent. A change to customer, product, channel, price, route, or target scale can invalidate several Fits at once; do not preserve old coefficients by changing one label.

Identify a primary model constraint only when compatible evidence shows it limits the declared retained customer, durable value, contribution, cash, or other outcome within the horizon. Compare impact, sensitivity, evidence strength, control, time to learn, economics, capacity, externalities, and risk. The lowest conversion rate, largest volume, longest delay, or first funnel stage is not automatically the constraint. Preserve credible alternatives when evidence cannot distinguish them.

## Route Specialist Work

Route customer evidence to `customer-research`; fit assessment to `product-market-fit-assessment`; segmentation and market framing to `positioning`; transition analysis and broad company constraint triage to `growth-diagnosis`; first value to `activation`; cohort construction and recurring-value work to `retention`; pricing and economics to `monetization`; metric systems to `growth-measurement`; individual loops to `growth-loop-design`; causal tests to `growth-measurement`; and channel plans to `acquisition-strategy`.

The model may specify what evidence these capabilities must return, but it does not duplicate their full workflows or execute their actions.

## Deliver In Order

Return:

1. mode, decision, owner, horizon, model version, and boundary;
2. business-specific node, edge, stock-flow, capacity, and guardrail map;
3. evidence, definition, compatibility, causal-status, and limitation ledger;
4. Four Fits and model-coherence register;
5. equation register with units, values, sources, maturity, and reconciliation;
6. baseline and scenario results with ranges, lags, sensitivity, and downside;
7. primary model constraint or discriminating evidence plan plus alternatives;
8. a bounded 30-day validation and model-update cadence;
9. adjacent-Skill handoffs, Playbook references, and external-action boundary.

For China work, keep market, language, locale, product surface, identity, app distribution, payment, invoice, channel, consent, regulation, and data availability separate. Do not infer platform, payment, advertising, CRM, survey, or analytics conditions from market or language.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not access analytics, warehouse, CRM, billing, payment, finance, ad, product, support, survey, or messaging systems; export production data; change events, identities, dashboards, forecasts, targets, product, onboarding, price, packaging, entitlements, budgets, staffing, or customer state; contact customers; launch experiments; publish; send; spend; or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, model version, customer, value, entities, periods, stocks, flows, edges, equations, sources, evidence states, causal status, economics, reinvestment, capacity, Four Fits, guardrails, uncertainty, scenarios, constraint, owner, and update trigger are explicit; definitions and cohorts are compatible; reconciliations close or differences remain visible; stocks and flows are not double counted; loops close before being named; scenarios are not forecasts; the constraint is not selected by rate alone; adjacent Skills remain bounded; Playbook sources are pinned; and no external action occurred.
