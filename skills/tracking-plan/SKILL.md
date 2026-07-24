---
name: tracking-plan
description: Use when a team needs to design, audit, migrate, or govern a product, website, app, lifecycle, commerce, sales, or marketing tracking plan; define event and property taxonomies; separate intent, action, result, quality, refund, and reversal states; specify entities, identity, consent, sources, schema versions, and data retention; map metrics and experiments to instrumentation; or create implementation, QA, reconciliation, release, monitoring, rollback, and deprecation requirements.
---

# Tracking Plan

Translate decisions and value states into an implementation-ready instrumentation contract. Track the smallest set of observable facts that can support the declared metric, funnel, cohort, experiment, attribution, lifecycle, or operational decision. Do not treat a tracking plan as a list of clicks or assume an SDK event is true because it fires.

Read [tracking-contract.md](references/tracking-contract.md) before defining events, properties, identity, consent, or sources. Read [implementation-and-qa.md](references/implementation-and-qa.md) before selecting collection points, versioning schemas, releasing instrumentation, reconciling systems, or deprecating events. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `design` | Build a new tracking specification from decisions, value states, metrics, and source-of-truth requirements |
| `audit` | Test existing events, properties, identity, consent, lineage, and data quality for declared decisions |
| `migration` | Version, map, dual-run, reconcile, cut over, and deprecate instrumentation without silently breaking comparability |

Name one primary mode. Keep desired business meaning, implemented collection, observed data, and validated truth visibly separate.

## Freeze Decision And Data Boundary

Record decision, owner, consumers, product, surface, market, language, locale, business model, entity, actor, eligible population, value states, metric definitions, experiment or campaign context, collection systems, sources of truth, identity rules, consent and purpose, data classes, retention, access, required history, release window, and prohibited data.

If metric meaning is unresolved, preserve candidate definitions and route the decision to `growth-metrics-design`. A tracking plan implements a declared semantic contract; it should not silently choose the company's North Star, activation, retention, conversion, or revenue definition.

## Model States Before Events

Map intent, attempt, accepted action, processing, result, quality, failure, cancellation, refund, reversal, and deletion where applicable. Track meaningful state changes at the authoritative layer. Examples:

```text
checkout_started -> payment_submitted -> payment_succeeded -> order_fulfilled -> order_refunded
invite_created -> invite_delivered -> invite_accepted -> collaborator_reached_value
task_requested -> output_generated -> output_accepted -> task_completed -> result_reversed
```

Do not substitute page views, button clicks, client callbacks, ad-platform conversions, or generated outputs for server-confirmed or operational outcomes. Retain both when they answer different questions and label the relationship.

## Specify Every Event

For every event define canonical name and version; business meaning; actor and affected entity; trigger and authoritative source; eligibility and prerequisites; timestamp and timezone; required and optional properties with type, allowed values, nullability, source, and sensitivity; identity keys and join rules; consent and purpose; deduplication and idempotency; late arrival and ordering; retries, offline behavior, and failure handling; owners; downstream metrics and consumers; QA; effective date; change log; and deprecation.

Use stable snake_case names and past-tense state changes when that matches the repository or implementation convention. Do not encode dynamic values into event names. Avoid free text and direct identifiers when enums, pseudonymous keys, or aggregates are sufficient.

## Keep Identity And Eligibility Explicit

Separate anonymous device, person, user, account, workspace, household, buyer, payer, order, subscription, listing, creator, supplier, market, experiment assignment, billing identity, and messaging eligibility. Specify create, merge, split, logout, cross-device, deletion, re-entry, and historical restatement rules.

Consent is not a boolean inferred from market. Record purpose, collection and use basis, state source, timestamp, version, withdrawal, suppression, retention, regional or product scope, and downstream enforcement. Do not collect a property merely because it may be useful later.

## Design For Reconciliation

Assign an authoritative source to each fact. Reconcile client and server events; order and payment states; product and billing identities; campaign and destination parameters; assignment, exposure, and treatment delivery; lifecycle eligibility and send or delivery receipts; and warehouse transformations where relevant.

For each critical event define completeness, freshness, validity, uniqueness, consistency, lineage, expected relationship or invariant, alert owner, incident severity, replay or repair boundary, and customer or decision impact. Volume alone is not a quality check.

## Release Without Breaking Meaning

Use schema and semantic versions. A new optional property may be backward compatible; changing an event trigger, entity, eligibility, source, consent purpose, or required property usually needs a new version or visible series break.

Plan implementation owners, dependency order, test environments, synthetic fixtures, end-to-end QA, privacy and security review, analytics validation, dual logging, reconciliation, backfill policy, cutover, monitoring, rollback, communication, and deprecation. Never claim tracking is deployed or historical data was backfilled unless the authorized systems confirm it.

## Deliver In Order

Return:

1. mode, decision, owner, consumers, scope, and external-action boundary;
2. value-state and source-of-truth map;
3. entity, identity, eligibility, consent, privacy, and retention contract;
4. event dictionary and property schemas;
5. metric, funnel, cohort, experiment, attribution, and lifecycle lineage matrix;
6. implementation dependencies and ownership plan;
7. QA fixtures, assertions, reconciliation, monitoring, and incident rules;
8. version, migration, dual-run, cutover, rollback, backfill, and deprecation plan;
9. unresolved semantics, evidence gaps, handoffs, and pinned Playbook sources.

Route metric definition to `growth-metrics-design`, funnel semantics to `funnel-analysis`, cohort requirements to `cohort-analysis`, experiments to `experiment-design`, lifecycle classification to `lifecycle-marketing`, ad-platform-specific evidence to the relevant ads audit, and production implementation to an authorized engineering workflow.

For China work, keep market, language, locale, product surface, device, app distribution, identity, payment, invoice, consent, collection purpose, storage, transfer, analytics provider, platform, channel, and applicable review separate. Do not infer any platform, provider, payment, consent, or data condition from market or language.

This Skill creates and reads local artifacts only. Do not install SDKs, change application code, tags, consent managers, schemas, pipelines, warehouse models, identity graphs, dashboards, alerts, ad pixels, product analytics, or production data; do not backfill, delete, publish, or deploy; and do not claim those actions occurred without separate task-level authorization.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decisions, states, events, properties, entities, actors, sources, identity, eligibility, consent, purpose, sensitivity, retention, ordering, deduplication, lineage, metrics, experiments, QA, reconciliation, versions, migration, backfill, monitoring, incident, rollback, deprecation, owners, and unresolved semantics are explicit; state results are not replaced by clicks; versions preserve comparability; unnecessary personal data is absent; and no external action occurred.
