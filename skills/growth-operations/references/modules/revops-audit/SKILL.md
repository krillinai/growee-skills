---
name: revops-audit
description: Use when a team needs to audit, map, reconcile, or improve revenue operations across marketing, sales, partnerships, implementation, customer success, support, finance, and product; assess lifecycle stages, lead and account routing, qualification, opportunity and pipeline hygiene, handoffs, territories, capacity, forecasting, bookings, contracts, subscriptions, invoices, recognized revenue, cash, renewals, expansion, attribution, CRM data, integrations, automation, access, governance, or a dependency-ordered RevOps roadmap without accessing or changing live systems.
---

# RevOps Audit

Audit whether the revenue operating system turns qualified demand into realized and retained customer value, economically reconciled revenue, and accountable decisions. Optimize trustworthy progression and cross-functional execution, not lead volume, CRM completeness, tool count, pipeline coverage, forecast confidence, bookings, or automation alone.

Read [revenue-contract.md](references/revenue-contract.md) before accepting lifecycle, entity, ownership, source, pipeline, customer, contract, or revenue evidence. Read [audit-methods.md](references/audit-methods.md) before mapping workflows, handoffs, controls, systems, or capability states. Read [forecasting-and-reconciliation.md](references/forecasting-and-reconciliation.md) before comparing funnel, pipeline, forecast, bookings, ARR, recognized revenue, contribution, invoice, or cash evidence. Read [governance-and-roadmap.md](references/governance-and-roadmap.md) before proposing automation, access, change control, service levels, or remediation. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `system` | Audit the end-to-end revenue operating model, definitions, workflows, systems, controls, and governance |
| `motion` | Audit one bounded lead, account, opportunity, partner, implementation, renewal, or expansion workflow |
| `reconciliation` | Resolve definitions, lineage, snapshots, attribution, forecast, commercial, finance, or customer-value discrepancies |

Name one primary mode, decision, owner, revenue motion, entity boundary, market, horizon, and external-action boundary. Public artifacts and supplied process documentation are sufficient to start; CRM, warehouse, call, contract, finance, customer, and employee data are optional.

## Freeze The Revenue Contract

Record product, offer, package, price and contract version; customer, buying, service, payer, and revenue units; person, contact, lead, account, workspace, opportunity, partner, quote, contract, order, subscription, invoice, payment, cash, revenue, implementation, renewal, and expansion entities; lifecycle and stage definitions; eligibility, entry, exit, re-entry, reversal, loss, disqualification, and unknown states; source, identity, deduplication, hierarchy, ownership, routing, handoffs, service expectations, territories, capacity, approvals, systems, integrations, fields, versions, access, lineage, quality, snapshots, currency, time, attribution, economics, privacy, incidents, and requested external action.

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may be a `reported signal` with no evidence state. Do not repeatedly request declined private access or penalize unavailable evidence.

## Assign Control States, Not False Certainty

For each scoped control assign one state:

| Control state | Requirement |
| --- | --- |
| `operating and reconciled` | Attributable evidence verifies the control operates and its important outputs reconcile within a declared tolerance and period |
| `operating not reconciled` | Operation is verified but outcome, source, or downstream reconciliation is absent, incompatible, or unresolved |
| `specified not implemented` | An approved definition or process exists but implementation evidence is absent or verifies it is not operating |
| `verified gap` | Attributable evidence verifies absence, failure, bypass, contradiction, or unacceptable variance |
| `unavailable` | Evidence needed to assess the control is not supplied or observable |
| `not applicable` | The control does not apply to the declared motion and reason |

Do not produce an overall score by default. If a score is explicitly requested, calculate only eligible verified checks, show weights and deductions tied to findings, and display evidence coverage separately. Missing private evidence does not reduce the score.

## Map Value, Buyer, Commercial, And Revenue States

Keep these layers linked but distinct:

```text
qualified demand and buying progress
-> accountable opportunity and commercial decision
-> contract, order, or subscription state
-> implementation and first customer value
-> invoice, payment, cash, and recognized revenue
-> recurring value, renewal, expansion, contraction, or churn
```

Seller activity is not buyer progress. A lead is not a person, account, opportunity, order, customer, or revenue unit without explicit identity and transition rules. A signed contract is not implementation, customer value, recognized revenue, cash, renewal, or retained contribution. Preserve branches, assisted and self-serve paths, partners, multiple products, account hierarchies, split ownership, reactivation, reversal, refund, and churn.

Use existing lifecycle and stage names when their definitions are observable and decision-useful. Do not impose a universal funnel, MQL or SQL definition, SLA, territory, pipeline coverage multiple, forecast accuracy target, sales methodology, or tech stack.

## Audit In Dependency Order

1. `decision and value`: customer value, business outcome, motion, scope, owner, review cadence, and guardrails;
2. `entities and definitions`: identity, hierarchy, lifecycle, stage, source, qualification, attribution, contract, revenue, and customer-state contracts;
3. `workflow and ownership`: routing, queues, acceptance, rejection, recycling, handoffs, exceptions, service expectations, capacity, territories, and decision rights;
4. `systems and data`: sources of truth, fields, versions, interfaces, integrations, permissions, quality, lineage, snapshots, reconciliation, observability, and incidents;
5. `pipeline and forecast`: stage evidence, amount, probability basis, timing, changes, age, slippage, loss, category, snapshots, calibration, bias, and capacity;
6. `commercial and finance`: offer, price, discount, approval, quote, contract, order, subscription, invoice, payment, refund, cash, recognized revenue, contribution, currency, tax, and accounting boundaries;
7. `delivery and durability`: implementation, first value, support, recurring value, renewal, expansion, contraction, churn, promise alignment, and customer health;
8. `governance and improvement`: access, privacy, change, exception, audit, incident, rollback, feedback, automation, retirement, and roadmap.

Trace symptoms to the first broken dependency. Do not repair inconsistent entities or stage definitions with required fields, dashboards, scoring, AI forecasting, or more automation.

## Diagnose Without Inventing Cause

For every finding state observed condition, affected entities and period, source, control state, decision impact, customer and financial risk, plausible mechanisms, counterevidence, confidence, owner, dependency, and completion proof. Name a root cause only when evidence distinguishes it from alternatives.

Keep operational attribution, financial reconciliation, association, prediction, and causal effect separate. A dashboard discrepancy, slow response, aged pipeline, forecast miss, no-decision, churn, or data gap narrows investigation but does not identify one cause by itself.

## Deliver In Order

Return:

1. mode, decision, owner, motion, scope, horizon, and external-action boundary;
2. one system verdict: `decision-ready`, `partially controlled`, `reported only`, or `not assessable`, with the limiting dependency;
3. entity, lifecycle, buyer, customer-value, commercial, and revenue state map;
4. workflow, ownership, handoff, system, source-of-truth, and integration map;
5. control matrix with evidence state, coverage, findings, risks, and reconciliations;
6. pipeline, forecast, capacity, commercial, finance, renewal, and expansion analysis;
7. prioritized dependency-ordered remediation with owner, decision rule, guardrail, stop rule, and completion proof;
8. 30-, 60-, and 90-day roadmap, governance cadence, specialist handoffs, Playbook sources, and unresolved evidence.

Route event implementation to `growth-measurement`; metric definitions to `growth-measurement`; transition calculations to `growth-diagnosis`; mature segments to `retention`; causal tests to `growth-measurement`; offers, pricing, and unit economics to `monetization`; customer and ICP rules to `customer-research` and `positioning`; buying assets to `sales-enablement`; organization structure to `growth-operations`; and shared platform or sourcing decisions to `growth-operations`.

For China work, keep market, language, locale, legal entity, customer and payer unit, route to market, partner, platform, CRM, identity, hosting, data, consent, contract, seal or signature, order, payment, tax, invoice, revenue recognition, currency, bank, procurement, security, access, retention, transfer, and applicable rules separate. Do not infer a platform, legal entity, invoice, payment, contract, data, accounting, or procurement condition from China or Simplified Chinese.

This Skill creates and reads local artifacts only. Do not access CRM, marketing automation, sales engagement, call, support, customer success, product, analytics, warehouse, billing, payment, contract, finance, HR, compensation, partner, or identity systems; export production or employee data; create or change records, entities, identities, stages, sources, fields, routing, ownership, territories, quotas, compensation, forecasts, prices, discounts, quotes, contracts, invoices, revenue, permissions, integrations, automations, dashboards, alerts, or customer state; contact anyone; procure software; deploy; or claim changes or results.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, motion, entities, identity, lifecycle, buyer progress, stages, sources, ownership, routing, handoffs, service expectations, capacity, systems, fields, lineage, snapshots, quality, forecast, commercial terms, contracts, revenue, cash, customer value, renewal, expansion, privacy, controls, incidents, evidence coverage, owners, dependencies, roadmap, and action boundaries are explicit; unavailable is not a gap; activity is not buyer progress; pipeline is not revenue; bookings are not cash; attribution is not causality; automation follows trustworthy foundations; and no external action occurred.
