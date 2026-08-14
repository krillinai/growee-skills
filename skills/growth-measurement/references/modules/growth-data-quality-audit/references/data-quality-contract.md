# Growth Data Quality Contract

## Freeze The Decision And Data Product

| Field | Required record |
| --- | --- |
| Audit | ID, version, mode, state, decision, intended and prohibited uses, prior version, and non-goals |
| Accountability | Data-product owner, decision owner, source, field, metric, model, pipeline and report owners, reviewers, approvers, and escalation |
| Scope | Products, business models, customers, participant roles, markets, locales, entities, populations, partitions, sources, fields, periods, and exclusions |
| Semantics | Keys, eligibility, events, states, metrics, units, time zones, currencies, accounting and cash bases, watermarks, maturity, and tolerances |
| Lineage | Source, extraction, schema, code, transformation, join, model, metric, aggregate, report, export, and decision versions |
| Evidence | Supplied artifacts, samples, queries, logs, dictionaries, reconciliations, screenshots, source access, as-of time, limitations, and contradictions |
| Governance | Privacy, security, market, retention, correction, approval, system, communication, publication, and external-action boundaries |

Do not silently change the decision, expected population, field meaning, authority, period, version, cutoff, or tolerance during an audit.

## Use Explicit Evidence And Value States

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. A stakeholder statement without inspectable evidence may remain a `reported signal` with no evidence state.

Classify values independently:

| State | Meaning |
| --- | --- |
| `observed` | Directly recorded under the defined source and collection contract |
| `derived` | Deterministic transformation of versioned inputs |
| `imputed` | Filled from an explicit rule or model because the intended value was missing |
| `predicted` | Model estimate of a future or unobserved outcome |
| `attributed` | Credit assigned by an explicit attribution rule or model |
| `inferred` | Non-observed classification or relation from bounded evidence |
| `synthetic` | Generated or simulated value, label, or record |
| `manually adjusted` | Human-entered correction or override with attributable authority |

Never relabel a non-observed state as observed. Preserve model, rule, features, training cutoff, owner, population, horizon, calibration, uncertainty, override, and actual reconciliation.

## Inventory Supplied Evidence

For every artifact record stable ID, title, source, owner, extraction or capture method, as-of and received time, periods, populations, rows or aggregates, fields, versions, transformations, access state, sample design, freshness, limitations, contradictions, and consumers.

Keep public pages, screenshots, stakeholder accounts, small samples, exports, query results, logs, schemas, and authoritative records separate. A screenshot verifies only visible pixels and labels at capture time. A sample verifies only sampled fields and records under its selection method. Neither proves private system-wide quality.

## Define Quality Dimensions By Use

| Dimension | Decision question |
| --- | --- |
| Coverage | Does observed scope represent the expected eligible population, sources, partitions, products, markets, and periods? |
| Completeness | Are required records and fields present after their valid arrival and maturity windows? |
| Uniqueness | Are entities and events represented once under the relevant key and idempotency contract? |
| Identity and eligibility | Are records joined to the correct entity, role, consent, lifecycle state, and population? |
| Validity | Do values, events, types, ranges, sequences, states, and relationships satisfy the semantic contract? |
| Timeliness | Are event, processing, reporting, correction, and watermark times fit for the decision? |
| Consistency | Do compatible sources, platforms, versions, aggregates, and reports agree within explainable tolerances? |
| Lineage and reproducibility | Can every decision value be reproduced from attributable versioned sources and transformations? |
| Integrity and governance | Are access, privacy, security, retention, change, correction, incident, and audit controls appropriate? |

Tolerances depend on the decision and failure cost. Do not average dimensions into a universal score or let a strong dimension cancel a blocker.

## Define Test Evidence

Every test records test ID and version, requirement, dimension, source, population, fields, period, denominator, query or deterministic procedure, expected result, tolerance, observed result, evidence state, coverage, exceptions, owner, execution time, limitations, and downstream decision effect.

If the supplied artifacts cannot run or reproduce the test, provide the exact test specification and mark the result unavailable. Do not claim a test ran or passed.

## Require Readiness Before Quality Commitments

Certification, scores, tolerances, SLOs, severity, response targets, control schedules, owners, and remediation commitments require:

- a bounded decision, intended and prohibited uses, eligible population, products, markets, periods, sources, fields, versions, and consumers;
- reproducible tests with denominators, observed baselines, variation, sample limits, maturity, and source lineage;
- decision-specific failure costs, materiality, customer effects, risk policy, current controls, and incident history;
- operating calendars, watermarks, system constraints, maintenance windows, action authority, accountable owners, approvers, and review triggers.

When any material condition is unavailable, use `draft` or `evidence-pending`. Do not invent a readiness score, certification, traffic light, target, threshold, tolerance, SLO, severity tier, response time, error budget, cadence, review date, expiry, owner, approver, deadline, phase, or 30/60/90-day plan. Return unvalued test and control contracts plus evidence required to set them.
