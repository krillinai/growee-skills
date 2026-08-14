# Controls, Governance, Market, And Actions

## Rate Findings Without A Composite Score

For each finding record requirement, observed and expected state, evidence, population, period, count, rate and denominator, affected fields and consumers, quality dimension, materiality, customer and decision effect, supporting and contradictory evidence, cause status, current control, uncertainty, priority rationale, recommendation, owner, prerequisites, verification, residual risk, review, and expiry.

Keep these separate:

- `quality failure`: evidence violates a defined contract;
- `coverage gap`: required scope was not observed or tested;
- `control gap`: no adequate prevention, detection, reconciliation, response, or audit exists;
- `decision blocker`: the failure prevents a named valid decision;
- `risk`: a possible customer, business, privacy, security, financial, or operating effect;
- `root cause`: supported mechanism, not merely the visible defect.

Use `verified blocker`, `material defect`, `bounded defect`, `monitor`, `unavailable`, or `not applicable` only with decision-specific rationale. Do not average blockers with passing dimensions.

When affected population, count, denominator, failure cost, materiality, decision effect, baseline, policy, or authority is unavailable, do not infer `material defect`, incident severity, priority, or remediation deadline. Use `unavailable` or a bounded blocker statement and name the evidence that could support classification.

## Design Controls In Layers

| Control type | Purpose | Required fields |
| --- | --- | --- |
| Preventive | Stop invalid data or changes before production use | contract, schema, validation, approval, test, version, and rejection path |
| Detective | Identify a defect after creation or arrival | test, population, denominator, threshold, baseline, schedule, watermark, and coverage |
| Reconciliation | Compare sources or layers on compatible bases | authority, bridge, tolerance, residual, owner, and review |
| Monitoring | Observe reliability, completeness, timeliness, validity, drift, and incidents | SLI, SLO, window, segmentation, alert, suppression, and trend |
| Incident | Contain, investigate, correct, recover, and learn | severity, owner, runbook, escalation, stop, rollback, correction, and audit |
| Correction | Version a valid repair without rewriting history | scope, evidence, approval, validation, backfill, communication, rollback, and expiry |
| Review | Revalidate decisions, definitions, tolerances, sources, and controls | cadence, trigger, owner, consumers, artifacts, and action states |

Connect every control to a decision, data product, entity, field or event, population, failure mode, materiality, owner, recipient, action, and proof. Avoid alerts without action, duplicate alerts, universal thresholds, and paging every owner.

## Define Monitoring And SLOs

Keep availability, reliability, coverage, completeness, freshness, validity, uniqueness, consistency, reconciliation, model calibration, decision readiness, and customer impact separate. Pipeline uptime proves only the bounded availability measure it actually observes.

Before setting a control value, define entity, eligible population, numerator, denominator, source, baseline distribution, tolerance basis, failure cost, materiality, decision use, operating calendar, watermark, owner, authority, response capability, review trigger, and expiry. If these are unavailable, describe the SLI, test, control, routing, and evidence fields without a numeric SLO, threshold, severity, response time, schedule, or owner assignment.

For alerts define baseline, threshold or change rule, schedule, evaluation window, watermark, minimum population, severity, routing, deduplication, suppression, maintenance window, escalation, runbook, auto-action prohibition or authority, and close evidence. Measure alert precision, known coverage limits, time to detect, acknowledge, contain, recover and verify, recurrence, false positives, missed incidents, and fatigue.

Do not import generic reliability targets or create a provisional severity taxonomy to make an incomplete audit actionable. Control recommendations are not approved policies, deployed alerts, assigned incidents, or operating commitments.

## Transfer Across Markets

Treat every market as a new product, entity, identity, eligibility, consent, source, event, metric, currency, accounting, payment, invoice, tax, data-flow, storage, transfer, retention, platform, vendor, calendar, latency, control, incident, owner, and approval boundary.

Translation and currency conversion do not validate transfer. For China, distinguish market, legal entity, language, locale, product, channel, platform, app distribution, identity, payment, invoice, data, content, advertising, support, sources, storage, transfer, vendors, calendars, costs, and locally accountable review. Use current direct sources and local expertise. Do not provide legal, tax, accounting, regulatory, provider-availability, approval, or quality conclusions.

## Protect People And Data

Use aggregate, redacted, pseudonymous, minimum-necessary evidence and small-cell suppression. Define purpose, authority, consent where required, access, retention, deletion, correction, audit, lineage, and reidentification controls.

Do not request or expose credentials, payment details, private messages, health or financial information, protected traits, precise locations, raw identities, complete histories, employee reviews, compensation, or ratings. Do not reidentify people or rank individuals for targeting, pricing, service, employment, credit, insurance, health, housing, or similar decisions. Review fairness, accessibility, retaliation, and misuse risk.

## Prepare Approval-Ready Actions

For each proposed query, test, schema change, data correction, identity change, backfill, dashboard change, alert, access request, communication, or deployment record owner, system, exact action, affected population, prerequisites, evidence, privacy, security and domain review, approvers, authorization, dry run, backup, sample and full validation, monitoring, cap, stop, rollback, correction, communication, audit, completion proof, and residual obligations.

Create local specifications only. Do not access systems, run production queries, export data, mutate records, deploy controls, contact people, or claim quality improved.

## Route Specialist Work

| Need | Route |
| --- | --- |
| Event and property schema, instrumentation, migration, and implementation QA | `growth-measurement` |
| Metric definitions, registry, hierarchy, and governance | `growth-measurement` |
| Unexpected business metric movement and candidate mechanisms | `growth-diagnosis` |
| Customer and recurring-value movement equations | `retention` |
| Attribution, cohorts, experiments, forecasts, LTV, or unit economics | the corresponding analytical Skill |
| Platform architecture, reliability service, sourcing, or roadmap | `growth-operations` |

Every handoff records input contract, decision, expected artifact, owner, due or maturity date, dependency, and permission boundary. A handoff does not imply access, correction, or execution.
