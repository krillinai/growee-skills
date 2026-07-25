# Metric Contract

Use this contract before calculating, comparing, targeting, or governing a core metric. A readable name is not a definition. Preserve disputed definitions as separate versions until reconciled.

## Intake Ledger

Record:

| Field | Required detail |
| --- | --- |
| Decision | Exact choice, owner, decision date, operating cadence, and decision window |
| Context | Product, customer, business model, stage, market, language, locale, and product surface |
| Value | Customer problem, value-producing behavior, qualified customer outcome, and durable business outcome |
| Current system | Metrics, reports, dashboards, targets, owners, consumers, decisions, and disputed definitions |
| Entity | Person, device, account, team, workspace, buyer, payer, order, transaction, subscription, listing, content unit, market, cohort, revenue, or another explicit entity |
| Population | Eligibility, exclusions, start state, exposure, re-entry, censoring, and unknown bucket |
| Events | Start, exposure, qualifying, outcome, cancellation, refund, and reversal events with versions |
| Calculation | Numerator, denominator, formula, aggregation, unit, currency, and rounding |
| Time | Observation, attribution, and maturation windows; cutoff, timezone, and calendar rules |
| Identity | Keys, joins, deduplication, merges, splits, cross-device rules, deletions, and late data |
| Comparison | Cohorts, segments, markets, channels, experiments, product versions, and maturity |
| Evidence | Source system, table or event, field, extraction date, freshness, lineage, owner, and counterevidence |
| Quality | Missingness, invalid events, bots, fraud, refunds, reconciliation, incidents, model error, and drift |
| Governance | Version, effective date, approval owner, review rule, access, privacy, and retirement rule |
| Decision rule | Baseline, threshold or target basis, guardrails, stop rule, downside, capacity, and follow-up |
| Boundary | Requested external actions, available capability, permissions, and prohibited actions |

Use exactly these evidence states:

- `verified`: inspectable supplied evidence supports the field in the declared scope;
- `reported signal`: an attributable stakeholder or platform statement exists but inspectable support is absent;
- `inferred`: a bounded interpretation follows from named evidence but remains unverified;
- `unavailable`: required evidence was not supplied or is incompatible;
- `not applicable`: the field does not apply and the reason is explicit.

Do not silently upgrade `reported signal` or `inferred` to `verified`.

## Core Metric Contract

Specify every core metric in this order:

```text
Metric ID, canonical name, version, and primary role
Purpose, decision, decision owner, and metric owner
Customer value or business outcome represented
Entity, level, unit, and currency
Eligible population and exclusions
Start, exposure, qualifying, outcome, reversal, and censoring events
Numerator, denominator, formula, aggregation, and rounding
Observation, attribution, maturation, and decision windows
Cutoff, timezone, calendar, and late-arrival allowance
Identity, joins, deduplication, re-entry, deletion, and unknown treatment
Segments, cohorts, markets, surfaces, channels, and experiment cuts
Source systems, fields, extraction date, freshness, and lineage
Reconciliation and data-quality checks
Guardrails, diagnostics, and related business-health metrics
Target or threshold basis and review rule
Known limitations, uncertainty, and counterevidence
Effective date, approval owner, change log, and retirement rule
```

Mark a contract `incomplete` when a field needed for the declared decision is unavailable. A specification can still be useful; it cannot support calculation or an operating decision until the missing gate is closed.

## Compatibility Gate

Before arithmetic or comparison, verify compatibility across:

- entity and level;
- eligibility, exclusions, and denominator;
- start, exposure, qualifying, outcome, and reversal events;
- identity, joins, deduplication, and re-entry;
- formula, aggregation, unit, currency, and version;
- observation, attribution, maturation, cutoff, and timezone;
- cohort age, segment rules, market, surface, channel, and exposure;
- source freshness, lineage, late data, incidents, and quality;
- prediction, attribution, observation, or causal-estimate type.

If a gate fails, do not force a blended result. Show each compatible slice, the incompatibility, and the specification needed to reconcile it. A zero denominator returns `unavailable`, not zero percent.

## Entity And Level Controls

Keep different entities distinct unless explicit joins and decision logic support a linked view:

- user, seat, team, workspace, account, buyer, and payer;
- lead, opportunity, contract, account, and recognized revenue;
- listing, supplier, buyer, request, match, order, market, and network unit;
- prompt, session, task, output, accepted output, retained user, account, and cost;
- order, customer, subscription, invoice, refund, contribution, and cash.

For B2B products, name the buying committee and the unit receiving value. User activity cannot automatically represent account value, buyer intent, renewal, or revenue. In Simplified Chinese output, use `企业客户` for this B2B entity by default, use `客户账户层级` only when the analytical level must be explicit, and reserve `用户账号` for a person's login identity; do not use standalone `账户` when the entity could be misunderstood. For marketplaces, preserve local network units and side-specific entities. For AI products, distinguish generated activity from accepted, useful, safe, and retained outcomes.

## Rate, Value, And Composite Controls

Every rate shows numerator, denominator, period, maturity, and source. Every value metric names currency, recognition rule, refunds, discounts, taxes, costs, and horizon as applicable.

Do not create a composite score merely to obtain one number. If a score is necessary, document component definitions, weights, normalization, missingness, monotonicity, sensitivity, version, validation, and how users can inspect the underlying dimensions. Never let a score hide a harmed guardrail.
