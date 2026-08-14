# Growth Data Quality Audit Output Contract

## Required Order

Return:

1. mode, audit ID and version, state, decision and intended uses, owners, reviewers, approvers, scope, products, customers, markets, entities, periods, cutoff, maturity, systems, access, privacy, review, expiry, and external-action boundary;
2. source, table, field, event, metric, model, report, sample, query, log, reconciliation, schema, code, transformation, consumer, and evidence manifest;
3. expected-population, partition, source, product, market, version, period, sample, observed, missing, late, duplicate, invalid, excluded, suppressed, failed-join, and untested coverage reconciliation;
4. identity, eligibility, uniqueness, idempotency, event, field, structural, semantic, sequence, cardinality, timeliness, maturity, outlier, exclusion, and derived-value tests;
5. source authority and reconciliation bridges with currencies, accounting, timing, refunds, adjustments, known components, unknown residuals, and materiality;
6. end-to-end lineage, schema and metric versions, backfills, overrides, corrections, incidents, historical revisions, downstream consumers, and decision effects;
7. findings, severity, evidence, uncertainty, counterevidence, customer and decision impact, preventive, detective, reconciliation, monitoring, incident, correction, and review controls;
8. governance, market and privacy boundaries, specialist handoffs, pinned sources, approval-ready external actions, and completion record.

Include certification, scores, control values, severity, owners, dates, or phased remediation only when the quality-commitment readiness gate passes. Otherwise preserve supplied numbers as bounded evidence and return unvalued test, control, incident, and remediation contracts with readiness conditions.

## Data Quality Contract

| Audit / version / state | Decision / uses / exclusions | Owners / reviewers / approvers | Products / customers / markets / entities | Period / cutoff / watermark / maturity | Sources / systems / versions / access | Privacy / review / expiry / action boundary |
| --- | --- | --- | --- | --- | --- | --- |

## Evidence And Lineage Manifest

| Artifact / source / owner | Entity / population / fields | Period / as-of / extraction / sample | Schema / code / transformation / metric / model version | Upstream / downstream / consumers | Evidence / freshness / limitation / contradiction | Access / retention / correction / audit |
| --- | --- | --- | --- | --- | --- | --- |

Public artifacts and samples do not prove unobserved private systems or populations.

## Coverage Reconciliation

| Expected population / partition | Source / product / market / version / period | Expected / observed | Missing / late / duplicate / invalid | Excluded / suppressed / failed join | Untested / sample bias / maturity | Residual / owner / next evidence |
| --- | --- | ---: | ---: | ---: | --- | --- |

Every rate includes an absolute count and denominator. Missing and unavailable are not zero.

## Test Register

| Test / dimension / version | Requirement / population / fields / period | Procedure / denominator / tolerance | Observed evidence / state / coverage | Exceptions / uncertainty / counterevidence | Decision and customer effect | Owner / control / review / expiry |
| --- | --- | --- | --- | --- | --- | --- |

Cover identity, eligibility, uniqueness, validity, sequence, cardinality, completeness, timeliness, maturity, consistency, derived values, and governance as applicable.

## Source Reconciliation

| Source A / contract | Source B / contract | Compatible basis | Explainable additions / exclusions / timing / currency / accounting / adjustments | Expected result | Unknown residual / materiality | Owner / decision / next evidence |
| --- | --- | --- | --- | ---: | ---: | --- |

Do not select favorable sources or use unexplained plugs.

## Change And Incident Register

| Change or incident / version | Trigger / detection / prior state | Scope / periods / populations / fields / value | Evidence / validity / consumer and decision effect | Backfill / correction / containment / recovery proposal | Approval / effective / rollback / audit | Residual / review / expiry |
| --- | --- | --- | --- | --- | --- | --- |

Preserve prior as-of data and decisions. Do not imply correction or resolution.

## Findings And Controls

| Finding / dimension / severity | Evidence / count / rate / denominator | Population / period / customer and decision effect | Uncertainty / counterevidence / cause status | Prevent / detect / reconcile / monitor / incident / correct / review control | Owner / prerequisite / proof | Residual / handoff / review / expiry |
| --- | --- | --- | --- | --- | --- | --- |

Do not average blockers into a composite score.

## Completion Gate

Confirm audit, version, mode, state, decision, uses, owner, reviewers, approvers, scope, exclusions, products, business models, customers, roles, markets, locales, entities, identity, eligibility, populations, partitions, sources, tables, fields, events, metrics, models, reports, periods, cutoffs, watermarks, maturity, samples, evidence, access, schemas, code, transformations, lineage, versions, coverage, completeness, uniqueness, idempotency, validity, sequence, cardinality, timeliness, consistency, observed and non-observed value states, outliers, exclusions, source authority, currencies, accounting, reconciliation, residuals, backfills, overrides, corrections, incidents, historical revisions, findings, severity, customer and decision effects, controls, monitoring, SLOs, owners, privacy, market transfer, retention, review, expiry, handoffs, pinned sources, and external actions are explicit; public and sample evidence was not generalized; missing did not become zero; entities and value were not duplicated; definitions and maturity were not mixed; modeled values remained labeled; records were not removed for favorable results; sources were not forced to reconcile; history was not rewritten; uptime did not become quality; recommendations did not become remediation; and no external action occurred.

When readiness did not pass, also confirm that no score, certification, traffic light, tolerance, target, threshold, SLO, severity, response time, error budget, schedule, review date, expiry, owner, approver, deadline, phase, or remediation plan was invented; unsupported fields remain unavailable; and no control or correction was represented as operating.
