# Tracking Contract

## Intake

Capture independently:

- decision, owner, consumers, review cadence, launch window, and failure cost;
- product, surface, environment, version, market, language, locale, and business model;
- customer value states, business states, metric contracts, funnel, cohort, experiment, attribution, lifecycle, and operational use;
- actor, affected entity, eligible population, exclusions, prerequisites, re-entry, and unknown handling;
- event name, version, trigger, collection point, authoritative source, timestamp, ordering, and latency;
- property name, meaning, type, allowed values, required status, source, sensitivity, and null behavior;
- anonymous, user, account, workspace, order, subscription, billing, assignment, and messaging identities as applicable;
- merge, split, cross-device, logout, deletion, deduplication, idempotency, late-arrival, and restatement rules;
- consent purpose, state, source, version, timestamp, withdrawal, suppression, retention, access, and downstream enforcement;
- destination systems, transformations, lineage, consumers, service levels, incidents, and repair rights;
- implementation, QA, release, dual-run, reconciliation, monitoring, rollback, backfill, and deprecation owners.

## Event Dictionary Row

Use one row per event version:

| Field | Required detail |
| --- | --- |
| ID | Stable event ID, canonical name, semantic version, status |
| Meaning | Observable state change and what it does not establish |
| Trigger | Exact condition, layer, source, actor, entity, and prerequisites |
| Time | Event time, receipt time, timezone, ordering, and late-arrival rule |
| Properties | Schema, types, enums, nullability, sources, sensitivity, and examples |
| Identity | Keys, scope, joins, merge, split, logout, deletion, and re-entry |
| Quality | Deduplication, idempotency, validation, invariants, reconciliation, and SLA |
| Governance | Purpose, consent, retention, access, owner, consumers, and prohibited uses |
| Lifecycle | Effective date, compatibility, migration, rollback, and deprecation |

## Property Controls

Prefer stable enums and pseudonymous IDs. Do not place email, phone, name, address, raw query text, message body, document content, credentials, secrets, payment credentials, exact location, or sensitive traits into event properties unless the declared decision requires the field and appropriate authorization and governance are explicit.

Record unknown, not applicable, refused, not collected, and system error separately where meaning differs. Do not overload null.

## Evidence States

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may use signal status `reported signal` and no evidence state. A desired schema is a specification, not verified implementation.
