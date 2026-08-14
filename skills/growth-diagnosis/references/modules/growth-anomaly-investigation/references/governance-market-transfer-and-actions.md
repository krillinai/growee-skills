# Governance, Market Transfer, And Actions

## Govern The Incident

Record incident owner, metric and source owners, analyst, data or engineering contacts, product and operating owners, privacy, security, legal or regulatory reviewers where needed, decision owner, approvers, status, severity basis, review cadence, evidence cutoff, resolution state, correction status, next check, and closure criteria.

Do not use an opaque severity score. Base priority on bounded customer and business impact, duration, spread, reversibility, trust, risk, decision deadline, and evidence uncertainty. Distinguish impact estimate from confirmed loss.

## Resolution And Closure

For a resolution state record:

- the material observed change and compatible baseline;
- measurement, mix, behavioral, expected-variation, and unknown contributions;
- supporting, contradictory, unavailable, and stale evidence;
- candidate mechanisms and causal status;
- affected and unaffected populations;
- remaining customer, financial, data, trust, regulatory, and operating risk;
- correction, containment, monitoring, or specialist recommendation and its authorization state;
- owner, maturity or review date, expiry, reopen triggers, and completion proof.

Close only when the decision is made, the evidence needed for that decision is mature, source reconciliation is bounded, material residuals are visible, and authorized follow-up has an owner. Closure does not mean every causal detail is known.

## Transfer Across Markets

Treat each market as a new anomaly boundary. Re-establish metric definition, customer and account hierarchy, product and app version, channel and platform, identity and consent, payment and invoice, source and data latency, timezone, weekday and holiday calendar, promotion, release schedule, currency, benchmark, bot and fraud rules, regulation, support, owner, and expected-variation baseline.

Translation, currency conversion, or a shared dashboard does not validate transfer. For China, distinguish market, legal entity, language, locale, timezone, product, channel, platform, app distribution, identity, payment, invoice, data source, storage, transfer, content, advertising, holidays, release, support, and local accountable review. Use current direct sources and local expertise. Do not make legal, regulatory, provider-availability, causal, or performance conclusions.

## Protect People And Data

Use aggregate, redacted, pseudonymous, minimum-necessary evidence by default. Define purpose, authority, consent where required, access, retention, deletion, audit, lineage, and small-cell suppression. Do not request credentials, private messages, health or financial details, protected traits, precise locations, employee records, raw identity, or complete histories when aggregate evidence is sufficient.

Do not identify, blame, or rank individuals for an anomaly. Do not infer sensitive traits, reidentify people, join data beyond the declared purpose, expose small groups, or use post-hoc segments for consequential acquisition, pricing, service, employment, credit, insurance, health, housing, or similar decisions.

## External-Action Boundary

Create and read local artifacts only. Do not access analytics, warehouse, CRM, billing, payment, finance, advertising, experiment, product, cloud, support, sales, partner, HR, identity, or BI systems; export, join, or reidentify people; change tracking, schemas, queries, data, backfills, attribution, dashboards, product, prices, campaigns, budgets, flags, experiments, releases, permissions, or records; pause, roll back, contact, publish, send, spend, deploy, or claim resolution or business impact without separate task-level authorization and required controls.

For every proposed external action record owner, system, exact mutation or communication, affected population, evidence, approver, privacy and security review, dry run, customer and operating guardrails, monitoring, stop, rollback, correction, audit, and completion proof. Recommendation, approval, authorization, execution, verification, and result are separate states.

## Specialist Handoffs

| Need | Route |
| --- | --- |
| Metric contract and hierarchy | `growth-metrics-design` |
| Event, identity, and source implementation | `tracking-plan` |
| Funnel transitions and losses | `growth-diagnosis` |
| Cohort and maturity behavior | `retention` |
| Customer and recurring-value state reconciliation | `retention` |
| Touchpoint and channel credit | `attribution-analysis` |
| Experiment integrity and causality | `experiment-design` |
| Primary current growth constraint | `growth-diagnosis` |
| Time-series forecast and calibration | `growth-forecasting` |
| Data and decision capability remediation | `growth-infrastructure-assessment` |

For each handoff preserve the frozen metric and incident contract, source and evidence cutoff, required fields, decision, owner, maturity date, expected artifact, and permission boundary. A handoff does not imply access, execution, or result.
