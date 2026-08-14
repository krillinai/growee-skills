---
name: growth-initiative-planning
description: Use when a team needs to build, audit, or replan one 30-90 day growth initiative after a strategy, diagnosis, target, opportunity, or investment decision; translate a bounded outcome into feasible workstreams, dependencies, capacity, evidence gates, milestones, commitments, risks, and change rules; or replace generic roadmaps, all-priority task lists, fictional schedules, and status reporting with a decision-linked execution plan.
---

# Growth Initiative Planning

Turn one selected growth direction into a feasible, versioned execution plan. Connect work to a bounded customer and business outcome through explicit mechanisms, dependencies, capacity, evidence gates, commitments, and change rules. A plan coordinates authorized work; it does not choose company strategy, manufacture approval, guarantee a target, operate systems, or prove impact.

Read [initiative-contract.md](references/initiative-contract.md) before accepting the source decision, outcome, customer, market, scope, owner, authority, evidence, or plan state. Read [workstreams-dependencies-and-capacity.md](references/workstreams-dependencies-and-capacity.md) before sequencing work, assigning dates, declaring a critical path, or allocating people and budget. Read [evidence-gates-and-replanning.md](references/evidence-gates-and-replanning.md) before defining milestones, experiments, commitments, completion, audit, or replanning. Read [governance-market-transfer-and-actions.md](references/governance-market-transfer-and-actions.md) before routing specialist work, transferring a plan across markets, using personal data, or proposing external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `build` | Create one bounded initiative plan from a declared source decision, outcome, evidence, capacity, and horizon |
| `audit` | Inspect an existing plan for lineage, coherence, feasibility, evidence gates, ownership, completion proof, and execution boundaries |
| `replan` | Version a plan after material evidence, dependency, capacity, scope, risk, or decision change without rewriting history |

Name one mode. Use exactly one plan state: `proposed`, `ready`, `active`, `blocked`, `paused`, `complete`, `cancelled`, or `expired`. State is not approval, authorization, action, verification, or business impact.

Route company or portfolio choices to `growth-strategy`, current constraint selection to `growth-diagnosis`, target contracts to `growth-measurement`, opportunity bounds to `growth-model-design`, resource-commitment decisions to `growth-operations`, organization and portfolio design to `growth-operations`, and recurring reconciliation to `growth-operations`. This Skill owns the execution contract for one selected initiative, not those upstream or downstream decisions.

## Freeze The Initiative Contract

Record initiative ID and version, mode and state, source decision ID and version, rationale and conditions, accountable outcome owner, workstream owners, required approver, authority and external-action boundaries, customer and participant roles, product and business model, market and locale, baseline, target or desired state, opportunity basis, horizon, scope, non-goals, strategy and metric versions, evidence cutoff, plan date, review date, expiry, and superseded plan.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Keep actual, baseline, reported signal, estimate, benchmark, target, opportunity, forecast, scenario, plan, recommendation, approval, authorization, action, completion, verification, causal estimate, and business result separate. Preserve source, owner, date, version, entity, definition, segment, market, period, currency, accounting basis, maturity, limitations, contradictions, and lineage.

Do not invent customers, baselines, targets, uplift, causal effects, opportunity, forecasts, capacity, costs, dates, confidence, approvals, authorization, implementation, or results. Missing upstream decisions create prerequisite gates; they do not become plan assumptions.

## Bound One Coherent Initiative

Define one customer or participant unit, problem or opportunity, first and repeated value, sustainable business outcome, mechanism, outcome owner, time horizon, and decision boundary. Name non-goals, excluded markets and populations, deferred work, and evidence that could reopen them.

Split work into separate initiatives when customer value, product, market, motion, economic unit, metric, owner, dependency graph, approval, or decision differs materially. Coordinate shared dependencies without blending evidence or results. If several independent initiatives remain, route the portfolio choice rather than calling all of them one priority.

Map the outcome chain:

```text
inputs -> activities -> outputs -> eligible exposure -> first value -> repeated or protected value -> retained customer outcome -> sustainable business outcome
```

Label each relationship `arithmetic`, `hypothesized`, `associated`, `causal`, or `tradeoff`. Delivery volume and utilization are diagnostic signals, not customer or business impact. Reconcile overlap across lifecycle stages and workstreams; do not add attributed, forecast, opportunity, or experimental effects as independent outcomes.

## Establish Readiness Before Scheduling

Mark a plan `ready` only when the source decision, bounded outcome, owner, authority, metric definitions, baseline evidence, required capacity, hard prerequisites, customer protections, decision gates, stop and rollback rules, and review path are explicit. Keep it `proposed` or `blocked` when a missing input can invalidate execution.

Separate research, evidence repair, experiment, pilot, staged rollout, full rollout, system work, operating readiness, and maintenance. A full-market or irreversible release is not an experiment. Require stronger evidence, review, controls, and authorization as spend, exposure, irreversibility, uncertainty, or potential harm rises.

## Build Workstreams And The Dependency Graph

Create only workstreams required by the outcome mechanism or a governing constraint. Classify each `required`, `optional`, `deferred`, or `routed`. For each record its outcome contribution, deliverable or decision-changing evidence, owner, inputs, dependencies, capacity, budget boundary, earliest start, maturity or due date, guardrails, completion proof, and permission boundary.

Model `hard`, `soft`, `evidence`, `approval`, `capacity`, and `external` dependencies. Record owner, predecessor and successor, lead time or range, evidence state, failure signal, alternate path, buffer, escalation, and replan trigger. Sequence prerequisites before dependent launch or scale. Expose the critical path and near-critical dependencies only from supported durations and calendars; otherwise return a provisional dependency order and missing evidence.

Do not start every workstream on day one. Do not compress work, remove controls, or parallelize incompatible dependencies to preserve a date.

## Prove Capacity And Economic Feasibility

Define capacity units, roles and skills, accountable owners, availability period, calendars, allocation, contention, external lead times, budget owner, approved or contingent amount, currency, accounting basis, and uncertainty. Separate available, committed, contingent, requested, unavailable, and displaced capacity.

Reserve explicit capacity for existing-customer support, reliability, accessibility, privacy, security, compliance, fraud controls, localization, data quality, incidents, maintenance, communication, decommissioning, and leadership review where applicable. Show utilization, bottlenecks, opportunity cost, and work displaced.

When capacity is insufficient, reduce scope, resequence, defer, pause, stop, or request a decision. Do not double-book people, assume unlimited budget or attention, infer hiring approval, or promise dates from fictional capacity.

## Define Evidence And Operating Gates

A milestone is a verifiable decision or operating state, not a date, meeting, deck, feature, campaign, dashboard, or closed ticket by itself. For each gate record the decision enabled, eligible population and exposure, required artifact or operating state, metric contract, evidence threshold or bounded state, maturity, guardrails, owner, due or maturity date, completion proof, and response.

Where evidence is tested, predeclare `positive`, `negative`, `harmful`, and `inconclusive` outcomes with `continue`, `revise`, `cap`, `pause`, `stop`, `rollback`, `escalate`, or `route` decisions. Route causal assignment, power, analysis, and readout to `growth-measurement`; do not claim that routing completed the work.

For each commitment record owner, artifact or outcome, date, dependency, evidence, completion proof, state, expiry, escalation, and permission boundary. Self-reported percentages, traffic-light status, activity, or ticket closure are not completion proof. Separate plan completion, implementation verification, mature customer outcome, business impact, and causal impact.

## Audit Or Replan Without Rewriting History

In `audit`, compare every contract, workstream, dependency, capacity assumption, gate, commitment, risk, and claimed completion with attributable evidence. Surface ownerless, overdue, stale, blocked, contradicted, revised, cancelled, and expired items. Do not accept `on track`, `green`, or percent-complete assertions without proof.

In `replan`, preserve the original version, assumptions, commitments, dates, evidence, misses, and decisions. Record the trigger and new evidence, recompute affected dependencies, critical path, capacity, opportunity cost, scope, gates, dates, risks, owners, and handoffs, then choose `revise`, `reduce`, `resequence`, `defer`, `pause`, `stop`, `cancel`, or `escalate`. State what remains unchanged and why.

Trigger replanning when a source decision changes; a prerequisite fails; evidence contradicts the mechanism; a guardrail breaches; capacity, budget, scope, market, platform, risk, or approval changes materially; a milestone expires; or an external event invalidates the plan. Do not hide missed commitments or backdate assumptions.

## Govern Markets, People, And Actions

Treat every market as a new evidence and operating boundary. Revalidate customers, value, product, channels, platforms, metrics, baselines, economics, capacity, dependencies, calendars, support, risks, owners, approvals, and rollback. Translation and currency conversion do not validate transfer.

For China, distinguish market, legal entity, language, locale, product, platform, app distribution, identity, payment, invoice, data, consent, content, advertising, holidays, support, staffing, lead times, and locally accountable review. Use current direct sources and local expertise. Do not make legal, tax, regulatory, provider-availability, accounting, approval, or performance conclusions.

Use aggregate, redacted, pseudonymous, minimum-necessary evidence. Do not expose credentials, private messages, payment details, health or financial data, protected traits, precise locations, raw identities, employee reviews, or full histories when bounded evidence suffices. Do not rank individuals for consequential pricing, service, employment, credit, insurance, health, housing, or similar decisions.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the initiative and decision contract; evidence and outcome chain; scope and non-goals; workstreams and specialist handoffs; dependencies and critical path; capacity, budget boundary, maintenance, and opportunity cost; evidence and operating gates; commitments and schedule; risks and change control; market, privacy, and external-action governance; pinned sources; and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated project, analytics, data, CRM, billing, advertising, experiment, product, cloud, support, HR, finance, procurement, or communication systems; export or join personal data; assign tasks; approve budgets; hire; change prices, products, permissions, contracts, records, or traffic; launch tests or campaigns; contact people; publish; send; spend; deploy; or claim implementation or business results without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md); the source decision and authority are explicit; one bounded outcome links to feasible work; incompatible units remain separate; definitions and evidence are versioned; dependencies, capacity, maintenance, gates, commitments, risks, and change rules are complete; dates do not replace proof; activity and status do not become impact; effects are not double counted; specialist work is routed; market and privacy boundaries hold; and no external action occurred.
