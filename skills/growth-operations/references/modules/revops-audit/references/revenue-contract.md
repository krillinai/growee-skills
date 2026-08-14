# Revenue Operations Contract

## Decision And Scope

Capture independently:

- decision, owner, approver, motion, product, market, horizon, cadence, and allowed action;
- customer value, qualified business outcome, revenue model, economic guardrails, and natural value or renewal frequency;
- self-serve, assisted, sales-led, partner-led, product-led, renewal, and expansion paths included or excluded;
- customer, user, buying group, account, service, payer, contracting, invoicing, and revenue-recognition units;
- person, contact, lead, account, parent, workspace, opportunity, quote, contract, order, subscription, invoice, payment, cash, implementation, renewal, and expansion entities;
- identity keys, joins, account hierarchy, merge, split, duplicate, existing-customer, re-entry, deletion, and unknown rules;
- lifecycle and stage name, entity, eligibility, entry, exit, required buyer or customer evidence, owner, time, reversal, loss, disqualification, and version;
- source, channel, campaign, partner, referral, original and current source, attribution, precedence, consent, and suppression;
- routing, queue, acceptance, rejection, recycle, handoff, service expectation, exception, escalation, capacity, territory, and ownership;
- system, object, field, source of truth, interface, integration, direction, frequency, latency, transformation, lineage, permission, and incident;
- pipeline, forecast, quote, pricing, discount, contract, order, subscription, billing, refund, cash, recognized revenue, contribution, renewal, expansion, contraction, and churn definitions;
- currency, exchange rate, timezone, calendar, fiscal period, snapshot, cutoff, late-arriving change, backfill, and restatement;
- source artifact, owner, extraction date, freshness, evidence state, counterevidence, limitation, and privacy boundary.

Split the audit when motions, products, entities, lifecycle definitions, currencies, markets, revenue policies, or customer-value paths are incompatible.

## Evidence States

Use:

- `verified`: directly supported by an attributable inspectable artifact;
- `inferred`: reasoned from named evidence, with the inference explicit;
- `unavailable`: decision-relevant but absent, inaccessible, declined, stale, or incompatible;
- `not applicable`: outside the declared scope, with reason;
- `reported signal`: attributable stakeholder statement without inspectable support; leave evidence state blank.

Public job descriptions, product pages, pricing pages, terms, help documentation, and vendor lists can support visible operating hypotheses. They cannot verify private entity definitions, routing, stage operation, data quality, forecasts, revenue, customer outcomes, access, incidents, costs, or compliance.

## Entity Registry

For every entity record canonical name, business meaning, grain, primary key, natural key, parent and child relationships, source of truth, creation, merge, split, deduplication, deletion, lifecycle, owner, consumers, version, and limitations.

Never silently use one entity as another. Common invalid substitutions include:

- contact or lead as unique person;
- person as account or buying group;
- account as opportunity;
- opportunity as contract or order;
- contract value as recognized revenue or cash;
- paid invoice as retained customer value;
- product user as buyer, payer, administrator, or renewal owner.

## Privacy Minimum

Prefer schemas, dictionaries, aggregate counts, pseudonymous samples, redacted records, reconciliation summaries, and access matrices. Exclude raw names, emails, phone numbers, credentials, tokens, message bodies, call audio, payment credentials, tax IDs, bank data, protected attributes, compensation details, and unrelated employee performance unless explicitly authorized and essential.

Document purpose, consent or permissible use, access, joins, field minimization, retention, deletion, transfer, aggregation, review, and incident handling. This Skill does not determine legal compliance.
