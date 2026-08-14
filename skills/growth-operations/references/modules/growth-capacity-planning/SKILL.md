---
name: growth-capacity-planning
description: Use when a team needs to build, audit, or refresh a growth capacity plan; reconcile demand, workload, people, skills, systems, vendors, inventory, customer or experiment exposure, queues, throughput, lead time, utilization, reserves, shared constraints, service classes, and capacity scenarios; or prepare evidence-bounded capacity-gap options without assigning work, hiring, buying, or scaling systems.
---

# Growth Capacity Planning

Turn growth demand and operating obligations into a versioned capacity record that exposes feasible service, constraints, contention, reserves, and conditional response options. Capacity is a unit-, time-, skill-, service-, and evidence-specific ability to complete accepted work reliably; it is not headcount, budget, access, quota, utilization, or theoretical maximum alone.

Read [capacity-contract-and-units.md](references/capacity-contract-and-units.md) before accepting demand, workload, resource, calendar, state, unit, conversion, or numerical capacity. Read [flow-constraints-and-service.md](references/flow-constraints-and-service.md) before using queues, WIP, throughput, lead time, Little's Law, utilization, bottlenecks, shared resources, service classes, or reserves. Read [scenarios-governance-and-actions.md](references/scenarios-governance-and-actions.md) before building scenarios, transferring a plan across markets, using workforce data, selecting a gap response, or preparing an external handoff. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Define the capacity system and evidence requests before compatible demand or supply observations exist |
| `build` | Reconcile supplied demand, workload, resources, flow, obligations, scenarios, and decisions into one capacity plan |
| `audit` | Inspect an existing plan for false availability, incompatible units, double booking, hidden queues, unsafe utilization, weak evidence, or governance failure |
| `refresh` | Preserve the prior version and update affected capacity after material demand, supply, service, dependency, market, or operating change |

Name one primary mode. Use `evidence-pending`, `reconciling`, `scenario-ready`, `decision-ready`, `blocked`, `approved-record`, `superseded`, or `expired` as the record state. A state does not prove approval, availability, allocation, execution, delivery, customer outcome, or business impact.

Route annual or quarterly orchestration to `growth-operations`; time-indexed demand outlooks to `growth-measurement`; target contracts to `growth-measurement`; budget and cross-functional resource decisions to `growth-operations`; investment cases to `growth-operations`; selected initiative planning and scheduling to `growth-operations`; organization, staffing, and hiring design to `growth-operations`; experiment design to `growth-measurement`; experimentation portfolios to `growth-operations`; revenue operations to `growth-operations`; causal diagnosis to `growth-diagnosis`; and infrastructure implementation to the accountable technical owner. This Skill owns the compatible capacity ledger, flow and constraint view, conditional load cases, gap options, triggers, and approval-ready handoffs.

## Freeze The Capacity Contract

Record capacity-plan ID and version, mode and state, decision served, service or workload, demand unit, supply unit, entry and completion, period and calendar, product, customer or participant, market and locale, owner, contributors, required approvers, evidence cutoff, review and expiry, scope and exclusions, privacy boundary, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Preserve source, owner, as-of date, collection window, entity, definition, segment, market, maturity, version, limitations, contradiction, correction, and lineage. Do not invent demand, capacity, productivity, conversion, utilization, service levels, headcount, budget, costs, dates, owners, approvals, effects, or outcomes. Missing values remain unavailable; they do not become zero.

Keep observed load, committed demand, forecast, scenario, target, plan, request, recommendation, approval, authorization, resource access, allocation, consumption, completed work, verified service, causal effect, and business result separate. Request, approval, contract, roster, seat, quota, or budget is not productive capacity.

## Reconcile Demand, Workload, And Supply

Define arrivals and backlog by eligible work item, service class, market, period, priority, effort or resource demand, due condition, abandonment, rework, and evidence state. Keep observed demand, accepted commitments, forecasts, targets, scenarios, and stress loads as separate versioned series. Do not add multiple representations of the same future demand.

Translate demand into workload only through attributable production relationships. Preserve distributions, peaks, seasonality, bursts, mix, complexity, uncertainty, and censored or incomplete work. Do not average away service classes or convert leads, revenue, users, requests, hours, impressions, inventory, and money into one capacity score.

For every supply record define resource, unit, skill or eligibility, owner, location and timezone, calendar, restrictions, lead time, notice, ramp, reliability, transferability, concurrency, expiry, obligations, reserve, and evidence. Reconcile `requested`, `approved`, `authorized`, `committed`, `provisioned`, `available`, `allocated`, `consumed`, and `verified` states. Separately report theoretical, rated, demonstrated, effective, reserved, allocatable, allocated, consumed, and verified capacity.

## Model Flow And The Active Constraint

Define arrival, admission, entry, queue boundary, WIP, blocked work, exit, acceptance, throughput, lead time, cycle time, aging, rework, abandonment, and time window before calculation. Report distributions and ranges, not averages alone. Use Little's Law only for compatible observations from an approximately stable, bounded system; it does not prove stability or predict exact completion dates.

Map dependencies, handoffs, starvation, blocking, batching, quality loss, rework, downstream acceptance, and customer-value completion. Distinguish a capacity constraint from a policy constraint, quality constraint, dependency, temporary incident, symptom, and causal root. Highest utilization or largest queue alone does not identify the bottleneck. Test candidate constraints against counterevidence and sensitivity; route causal diagnosis when evidence cannot distinguish them.

Define service classes with eligibility, admission, priority, preemption, acceptance, target or objective, aging, breach, escalation, stop, recovery, and review rules. Protect maintenance, support, reliability, accessibility, privacy, security, localization, incident response, customer recovery, and residual obligations. Do not mark every executive request urgent or let growth upside silently starve protected work.

## Reconcile Contention, Utilization, And Reserve

Map people and skills, systems, vendors, audiences, customers, inventory, leadership attention, and shared dependencies separately. Record calendar overlap, exclusivity, concurrency, contention, interference, displaced work, opportunity cost, and residual capacity. A resource cannot be allocated at 100 percent to multiple commitments.

Model utilization with arrival and service variability, failures, rework, queue growth, waiting time, switching, recovery, and consequence. Do not optimize every resource to 100 percent or promise that higher local output improves end-to-end throughput. Define operating, surge, contingency, and recovery capacity, plus protected reserve grounded in variability, lead time, service risk, and failure consequence.

## Build Conditional Capacity Cases

Create base, upside, downside, surge, stress, recovery, and other decision-relevant cases only from supplied demand series and assumptions. For each case preserve horizon, trigger, evidence, uncertainty, demand mix, required service, capacity by resource, constraint, reserve, gap or surplus, lead time, reversible option, irreversible commitment, decision date, stop condition, and residual risk. Do not invent probabilities or call a target or upside case certain.

When a gap remains, compare `eliminate`, `reduce`, `smooth`, `defer`, `sequence`, `cross-train`, `standardize`, `automate`, `buy`, `build`, `outsource`, `hire`, `change service`, or `accept` only as bounded options. Compare lead time, ramp, reversibility, reliability, cost basis, dependency, customer and employee risk, evidence gate, trigger, and residual capacity. Do not choose vendors, headcount, budgets, organization changes, dates, owners, schedules, or implementation without supplied evidence and separate authorization.

## Adapt Without Collapsing Units

For people, account for calendars, leave, meetings, support, maintenance, incidents, training, management, skill compatibility, handoffs, switching, ramp, and healthy workload. For experimentation, separate eligible experimental units, assignment, exposure, traffic, duration, maturation, platform throughput, analyst review, engineering work, interference, and customer attention. For B2B, preserve stage-, account-, role-, skill-, territory-, service-, and handoff-specific demand. For systems, use peak workload, concurrency, latency distributions, dependencies, saturation, failures, load tests, cost, failover, and recovery evidence. For marketplaces, model local side-specific availability, matching, fulfillment, quality, cancellations, liquidity, incentives, multi-homing, support, and operational capacity.

Do not use invasive employee surveillance or consequential individual productivity scoring. Use aggregate, redacted, pseudonymous, minimum-necessary, and small-cell-suppressed evidence with purpose, accountable basis, access, retention, deletion, correction, audit, fairness, accessibility, employee-health, dissent, appeal, and independent-review controls.

Treat every market as a new evidence and operating boundary. For China, distinguish market, legal entity, language, locale, currency, timezone, product, platform, app distribution, identity, payment, invoice, data, consent, privacy, staffing, vendors, holidays, support, and locally accountable review. Translation, ratio reuse, or currency conversion does not validate transfer. Avoid legal, labor, tax, regulatory, provider, accounting, approval, or performance conclusions.

## Deliver And Stop At The Boundary

Follow [output-contract.md](references/output-contract.md). Deliver the contract and evidence manifest; demand, workload, and supply ledgers; flow, service, constraint, contention, utilization, and reserve views; scenarios and gap options; monitoring and triggers; market, privacy, uncertainty, versions, handoffs, pinned sources, external actions, and completion record.

Create and read local artifacts only. Do not access authenticated planning, HR, finance, cloud, analytics, CRM, support, experiment, procurement, project, or communication systems; export private data; assign work; change priorities, quotas, schedules, staffing, compensation, leave, budgets, contracts, systems, or infrastructure; hire, procure, deploy, publish, or contact people; or claim capacity, delivery, customer, or business improvement without separate task-level authorization and verification.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that units and boundaries are compatible; evidence states are explicit; demand representations are not duplicated; resource states are reconciled; theoretical access is not effective capacity; calendars, skills, obligations, variability, queues, dependencies, service classes, reserves, and shared resources are preserved; utilization is not treated as productivity; scenarios are conditional; gap responses remain options; markets and privacy boundaries hold; specialist work is routed; approval and execution are not invented; and no external action occurred.
