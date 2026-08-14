---
name: growth-data-quality-audit
description: Use when a team needs to audit supplied growth data, events, tables, metrics, identities, cohorts, models, dashboards, source reconciliations, pipeline logs, quality incidents, backfills, or historical revisions; investigate data completeness, validity, uniqueness, timeliness, consistency, lineage, and decision impact; or design preventive, detective, reconciliation, monitoring, correction, and governance controls for a bounded data product.
---

# Growth Data Quality Audit

Turn a vague trust concern into a bounded, reproducible quality decision. Define the expected population and semantics, test supplied evidence, preserve missing and incompatible states, reconcile sources without plugs, trace versions and revisions, and connect defects to actual decisions and controls. Data volume, uptime, a favorable sample, or one composite score cannot certify quality.

Read [data-quality-contract.md](references/data-quality-contract.md) before accepting the decision, data product, entities, population, sources, fields, systems, versions, evidence, or access state. Read [coverage-identity-and-validity.md](references/coverage-identity-and-validity.md) before testing coverage, completeness, identity, uniqueness, event semantics, validity, timeliness, maturity, models, or exclusions. Read [lineage-reconciliation-and-change.md](references/lineage-reconciliation-and-change.md) before assigning source authority, reconciling systems, tracing lineage, comparing versions, auditing backfills, or preserving historical revisions. Read [controls-governance-market-and-actions.md](references/controls-governance-market-and-actions.md) before rating findings, designing controls, handling incidents, transferring across markets, using personal data, or proposing external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Inspect supplied datasets, aggregates, dictionaries, samples, logs, queries, exports, or reconciliations for decision-relevant quality defects and unknowns |
| `control-design` | Specify preventive, detective, reconciliation, monitoring, incident, correction, and review controls for one bounded data product or decision |
| `refresh` | Version a prior audit after sources, definitions, schemas, pipelines, backfills, incidents, controls, evidence, or downstream uses change |

Name one primary mode and state `draft`, `evidence-pending`, `review-ready`, `accepted-record`, `controls-pending`, `superseded`, or `expired`. State does not prove access, correctness, certification, remediation, control deployment, or improved decisions.

Route event and property schema design or migration to `growth-measurement`; metric semantics and registries to `growth-measurement`; unexpected business movement and mechanisms to `growth-diagnosis`; customer movement equations to `retention`; detailed attribution, cohort, experiment, LTV, or economics logic to the corresponding analytical Skill; and platform capability or sourcing to `growth-operations`. This Skill owns quality evidence, defects, reconciliation, controls, and approval-ready remediation, not the specialist model or implementation.

## Freeze The Data Quality Contract

Record audit ID and version, mode and state, decision and intended uses, accountable data-product owner, decision owner, source and field owners, reviewers and approvers, scope and exclusions, products and business models, customers and participant roles, markets and locales, entities and identity, expected populations and partitions, sources and authority, tables, fields, events, metrics, models, reports, periods, cutoffs, time zones, watermarks, maturity, source, schema, code and metric versions, evidence access, privacy boundary, review and expiry, prior audit, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Keep reported signal, observed value, derived value, imputation, prediction, attribution, adjustment, finding, recommendation, decision, approval, authorization, correction, deployment, verification, and result separate. Do not invent data, tests, coverage, quality, owners, causes, corrections, approvals, or outcomes.

## Gate Certification, Scores, Controls, And Remediation

Issue a certification, score, traffic light, tolerance, SLO, threshold, severity level, response time, error budget, control schedule, review or expiry date, owner assignment, deadline, or phased remediation commitment only when a bounded decision and population, reproducible source and test evidence, baseline and variation, failure cost and materiality, current controls and incident history, operating calendar, system constraints, accountable owner, and approval authority support it. A screenshot, uptime claim, row count, favorable sample, generic benchmark, executive request, or desire for a complete plan does not pass this gate.

If any decision-critical input is unavailable, keep the audit `draft` or `evidence-pending`. Preserve supplied numbers as bounded reported or diagnostic facts, but do not replace missing evidence with a readiness score, provisional SLO, severity taxonomy, role assignment, or 30/60/90-day plan. Return test, finding, control, incident, and remediation contracts with unsupported values marked `unavailable`, the first limiting evidence gate, and conditions for a later control or commitment version. Required role types may be named; assignments and authority remain unavailable.

## Inventory Sources, Fields, And Evidence

Create a complete supplied-evidence manifest with stable IDs, owners, source type, extraction method, as-of time, expected and observed periods, row or aggregate counts, entities, keys, fields, semantics, versions, transformations, access state, sample design, limitations, contradictions, and downstream consumers.

Public pages, screenshots, stakeholder statements, samples, and exports verify only what they contain. They do not establish private warehouses, CRM, billing, finance, identity, experiment, or historical pipeline quality. Preserve untested products, markets, periods, fields, rows, transformations, and systems.

## Test Coverage And Completeness

Define the expected eligible population before measuring observed coverage. Reconcile entities, partitions, source systems, products, markets, app or schema versions, periods, loads, fields, and downstream outputs. Report expected, observed, missing, late, duplicate, invalid, suppressed, excluded, and untested counts with denominators.

Do not treat row volume or a favorable sample as completeness. Record sampling frame, method, selection, coverage, bias, and inference limits. Keep missing, late, unknown, censored, suppressed, redacted, immature, failed-join, unavailable, not-applicable, valid-zero, and default states distinct. Absent events are not confirmed non-events unless eligibility, instrumentation, delivery, and maturity support that interpretation.

## Audit Identity, Uniqueness, And Eligibility

Freeze person, device, cookie, household, account, workspace, company, order, invoice, subscription, event, and other domain entities separately. Record natural, surrogate, source, idempotency, retry, replay, and version keys; deterministic and probabilistic match rules; precedence; confidence; exclusions; consent; purpose; and market boundaries.

Measure duplicate, false-merge, false-split, conflict, unresolved, and coverage states. Distinguish legitimate repeated behavior from replay or ingestion duplication. Reconcile lifecycle, transaction, billing, refund, and revenue records without counting the same entity or value more than once. Do not choose identity or deduplication rules by which produces the most growth.

## Test Semantic And Structural Validity

For each field and event define actor, object, trigger or state, eligibility, source, type, units, allowed values, null rules, cardinality, sequence, timestamp, time zone, expected frequency, invariants, and version. Test impossible states, invalid transitions, property mismatches, duplicate firing, missing eligible events, ordering, drift, and cross-platform divergence.

An event name and arriving rows do not prove semantic validity. Reconcile behavioral events with authoritative product, order, payment, billing, support, or operational states where applicable. Separate legitimate extremes, rare populations, abuse, errors, retries, adjustments, and unresolved cases. Never delete inconvenient records or set post-outcome rules to smooth metrics.

## Test Timeliness, Maturity, And Derived Values

Separate event time, processing time, reporting time, correction time, as-of time, watermark, latency, and expected lateness. Measure completeness by cohort age and outcome horizon. Missing, late, immature, censored, and suppressed are not zero. Compare equal-age cohorts or route censoring-aware analysis to the owning Skill.

Classify fields as `observed`, `derived`, `imputed`, `predicted`, `attributed`, `inferred`, `synthetic`, or `manually adjusted`. Record source, transformation, features, training cutoff, model or rule version, population, horizon, calibration, uncertainty, drift, overrides, actual-versus-predicted residual, and approved uses. Do not present modeled values as observations.

## Reconcile Sources Without Hiding Residuals

Assign field-level source authority by entity, use, period, and accounting or operational purpose. Reconcile scope, identity, lifecycle, timing, currencies, exchange rates, refunds, chargebacks, taxes, recognition, adjustments, late data, and versions. Show explainable bridges and preserve unknown residuals and materiality.

Do not select the most favorable dashboard or add unexplained plugs. Analytics activity, CRM state, billing transactions, cash, and finance recognition may be valid for different uses. Keep incompatible views separate and route accounting or specialist conclusions.

## Preserve Lineage, Versions, And History

Trace source, ingestion, transformation, join, model, metric, aggregate, report, export, and decision versions. Record code or query, effective time, dependencies, owner, tests, backfills, overrides, corrections, and consumers. Do not silently mix definitions, schemas, calendar and fiscal periods, currencies, cash and accrual views, or mature and immature records.

In `refresh`, preserve original as-of data, audit, dashboards, exports, evidence, and decisions. Create a versioned old-to-new bridge for schema, metric, pipeline, backfill, and correction changes. Record affected populations, periods, fields, metrics, decisions, consumers, validation, dual run, approval, effective date, rollback, and expiry. Never rewrite prior decision owners as knowing corrected data.

## Rate Findings And Design Controls

For each finding record requirement, observed evidence, affected population and period, dimension, defect, count and rate, materiality, decision and customer effect, supporting and contradictory evidence, uncertainty, cause status, current control, recommendation, owner, prerequisites, verification, residual risk, review, and expiry. Do not average blockers into a universal score.

Do not label severity or assign priority, owner, deadline, review, or expiry when the affected population, failure cost, decision effect, policy, baseline, authority, or operating evidence is unavailable. Preserve the finding and required fields without invented values.

In `control-design`, connect each preventive, detective, reconciliation, monitoring, incident, correction, or review control to a decision, field or population, failure mode, test, denominator, threshold, baseline, schedule, watermark, owner, severity, routing, runbook, escalation, suppression, stop, rollback, correction, audit, and SLO. Pipeline uptime does not prove semantic validity, completeness, reconciliation, or decision readiness.

Treat threshold, baseline, schedule, owner, severity, response, escalation, and SLO as required contract fields, not values to fill from convention. Leave them unavailable until the certification and control gate passes.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the contract; source and field inventory; coverage and evidence map; identity and duplicate analysis; semantic, structural, timeliness, maturity, and derived-value tests; reconciliation, lineage, versions, backfills and incidents; findings and decision effects; control and remediation design; governance, market and privacy boundaries; handoffs, pinned sources, approval-ready external actions, and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated warehouse, analytics, CDP, CRM, billing, finance, experiment, identity, product, cloud, support, HR, or communication systems; run production queries; export or join personal data; delete, merge, rewrite, backfill, correct, upload, or change data, identities, schemas, events, metrics, models, pipelines, dashboards, alerts, permissions, or records; contact; publish; send; spend; procure; deploy; or claim correction, incident resolution, control deployment, certification, or improved quality without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md); the decision and expected population are frozen; coverage and tests have denominators; missing states remain distinct; identity and duplicates are bounded; events and fields are semantically valid or flagged; maturity precedes comparison; modeled values remain labeled; exclusions are not outcome-driven; sources reconcile without invented plugs; versions and revisions preserve history; findings connect to decisions; controls have owners and actions; public and sample evidence stays bounded; market and privacy boundaries hold; specialist work is routed; and no external action occurred.
