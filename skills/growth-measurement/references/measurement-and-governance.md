# Measurement And Governance

Turn the metric system into a reproducible operating contract. This file specifies work; it does not authorize production access or changes.

## Measurement Audit

Audit in dependency order:

1. decision, customer value, durable outcome, owner, and decision window;
2. metric roles and actual decisions made from each metric;
3. entities, eligibility, events, denominators, formulas, units, and versions;
4. identity, sources, lineage, freshness, permissions, and data quality;
5. observation, attribution, maturation, cutoff, cohorts, segments, and comparability;
6. tree relationships, evidence, alternatives, guardrails, and business health;
7. targets, benchmarks, thresholds, decision rules, cadence, and incidents;
8. gaps, next evidence, owners, handoffs, and retirement candidates.

Reject vanity use, not operational metrics themselves. Activity, exposure, or volume can remain a diagnostic or input when its role and limits are explicit.

## Instrumentation Specification

For each missing event or field, specify:

```text
Decision and Metric Contract served
Event or field name and version
Entity and identity key
Trigger and non-trigger examples
Required properties and allowed values
Eligibility and consent boundary
Client, server, warehouse, billing, or external source
Timestamp, timezone, ordering, retry, and deduplication behavior
Late arrival, deletion, correction, refund, and reversal behavior
Validation owner, environment, sample, and acceptance rule
Privacy classification, retention, access, and minimization
Backfill policy and comparability break
Rollout, monitoring, rollback, and incident plan
```

Do not claim an event, join, dashboard, or alert exists because it is specified.

## Data Quality And Reconciliation

Require controls appropriate to the decision:

- schema, allowed-value, null, range, uniqueness, and referential-integrity checks;
- event volume, lateness, duplication, ordering, identity, bot, fraud, and deletion checks;
- funnel, cohort, billing, finance, channel, and source-to-source reconciliation;
- currency, timezone, tax, refund, chargeback, discount, and revenue-recognition alignment;
- unknown, unmapped, suppressed, and privacy-threshold buckets;
- model calibration, segment error, drift, leakage, feedback, and override checks;
- incident owner, severity, affected versions and periods, correction, annotation, and reprocessing rule.

Do not erase a discrepancy to make totals agree. Show the canonical source for the declared decision, the variance, plausible explanations, and the owner and date for resolution.

## Versioning And Change Control

A definition change creates a new version when it alters entity, eligibility, event, identity, formula, aggregation, unit, window, maturity, source, or decision meaning. Record:

- old and new definitions;
- effective timestamp and affected history;
- owner, approver, rationale, and consumers;
- backfill or no-backfill decision;
- comparability break and dashboard annotation;
- migration, dual-run, reconciliation, and retirement date.

Do not overwrite history without a visible policy. Freeze metric versions for experiments, targets, board reporting, incentives, and longitudinal comparisons.

## Governance Cadence

Assign a decision owner, metric owner, source owner, quality owner, and approval owner. One person may hold several roles, but responsibility must be explicit.

Use a cadence tied to the decision horizon:

- operating review: current movement, maturity, guardrails, incidents, and decisions;
- contract review: disputed definitions, lineage, quality, access, and version changes;
- target review: baseline, assumptions, capacity, downside, and stop rules;
- portfolio review: unused, duplicative, gameable, or misleading metrics to retire;
- incident review: impact, correction, communication, prevention, and audit record.

Metric incentives require anti-gaming checks and harmed-group review. Access must follow data minimization, purpose limitation, consent, privacy, security, retention, and applicable policy. This Skill does not provide legal approval.

## Thirty-Day Validation Plan

When evidence is incomplete, return a bounded plan:

| Window | Work | Completion proof |
| --- | --- | --- |
| Days 1-5 | Freeze decision, value, entities, definitions, owners, and source inventory | Approved contract ledger and dispute log |
| Days 6-10 | Reconcile sources, inspect quality, preserve unknowns, and identify maturity limits | Reconciliation report and quality baseline |
| Days 11-20 | Build compatible historical views and test association, tradeoff, and segment hypotheses | Reproducible tables with evidence labels and counterevidence |
| Days 21-25 | Design causal or qualitative validation for the most important unknown | Approved test or research specification with stop rule |
| Days 26-30 | Review guardrails, business health, governance, and decision readiness | Verdict, owner decision, next review date, and change log |

Use a shorter or longer natural window when customer value matures differently. Do not fabricate a 30-day result for a 90-day outcome.

## Capability Handoffs

| Need | Route |
| --- | --- |
| Select the primary growth constraint | `growth-diagnosis` |
| Analyze value-state transitions | `growth-diagnosis` |
| Compare equal-maturity groups | `retention` |
| Design or interpret causal evidence | `growth-measurement` |
| Define first value | `activation` |
| Define recurring value, churn, or resurrection | `retention` |
| Define pricing, revenue, contribution, CAC, LTV, or payback | `monetization` |
| Audit returned inputs and loop closure | `growth-loop-design` |
| Gather customer-value evidence | `customer-research` |

The metric Skill owns the shared contract and governance. The specialist Skill owns domain diagnosis or intervention design.

## External Actions

Without separate task-level authorization and a capable tool path, do not:

- access analytics, warehouse, CRM, billing, advertising, survey, or product accounts;
- query production data or export customer-level records;
- create or alter events, identity rules, pipelines, tables, models, dashboards, alerts, targets, or reports;
- launch experiments, change spend, message customers, publish results, or modify customer state;
- claim that any access, change, publication, or execution succeeded.

Provide local contracts, queries as non-executed specifications when useful, quality tests, reconciliation plans, and approval gates. Keep direct identifiers out of examples and outputs unless strictly required and authorized.
