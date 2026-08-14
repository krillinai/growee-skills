# Growth Infrastructure Capability Contract

## Decision Context

Capture independently:

- decision, decision date, owner, permitted action, horizon, and review cadence;
- customer outcome, business outcome, constrained growth decision, and guardrails;
- repeated workflow, frequency, volume, variability, internal consumers, and local context;
- current steps, systems, data, manual work, handoffs, queues, workarounds, cycle time, and failure modes;
- failure probability, customer impact, decision impact, financial cost, compliance risk, and recovery cost;
- capability layer, upstream dependencies, downstream consumers, interfaces, versions, and service expectations;
- product, market, language, locale, business model, entity, identity, consent, currency, and time basis;
- service, platform, team, vendor, data, security, privacy, risk, finance, and operational owners;
- access, approvals, logs, overrides, fallback, stop, incident, recovery, retrospective, and exception rules;
- reliability, adoption, efficiency, decision-quality, customer, risk, and cost evidence;
- source artifacts, owners, dates, versions, freshness, uncertainty, and limitations;
- external action requested and separate authorization state.

## Capability Layers

| Layer | Contract to verify | Dependency warning |
| --- | --- | --- |
| Data foundation | meaningful states, sources, identity, consent, quality, lineage, reconciliation, incidents | every downstream service can scale data error |
| Metric system | semantic definitions, registry, approved uses, versioning, guardrails | shared names without shared meaning create false comparability |
| Experiment services | eligibility, assignment, exposure, identity, diagnostics, metrics, decision record | self-service can scale invalid causal claims |
| Decision services | objective, inputs, model, calibration, uncertainty, action rights, fallback | accurate prediction can still optimize the wrong outcome |
| Execution systems | eligibility, suppression, frequency, delivery, retries, receipts, cost, outcome feedback | delivery success can coexist with customer harm |
| Creative systems | concept and asset lineage, tags, claims, rights, review, exposure, outcome feedback | variant volume can replace meaningful learning |
| Governance and operations | ownership, access, audit, override, stop, incident, privacy, risk separation | governance added after automation may not be enforceable |

## Evidence States

Use:

- `verified`: directly supported by an attributable inspectable artifact;
- `inferred`: reasoned from named evidence with the inference explicit;
- `unavailable`: required but not supplied or observable;
- `not applicable`: outside the scoped capability and decision;
- `reported signal`: attributable stakeholder statement without inspectable support; leave evidence state blank.

Public artifacts can verify visible products, vendors, policies, job descriptions, documentation, and dated company statements. They cannot verify private architecture, event quality, identity accuracy, platform adoption, experiment validity, model calibration, incidents, access, cost, customer effects, or internal control operation.

## Minimum Evidence

Prefer aggregate, pseudonymous, or redacted evidence:

- architecture and data-flow diagrams with versions and owners;
- service catalogs, interfaces, SLAs or SLOs, dependency maps, and consumer inventories;
- metric registry samples, lineage, reconciliation, quality, and incident summaries;
- aggregate assignment, exposure, SRM, delivery, latency, retry, failure, and recovery measures;
- redacted decision logs, overrides, model cards, calibration, drift, and fallback summaries;
- concept and asset registry samples, review states, exposure, fatigue, and outcome summaries;
- request queues, cycle-time decomposition, adoption, workarounds, support demand, and training evidence;
- vendor contracts, cost categories, staffing, maintenance, migration, lock-in, and exit assumptions;
- access matrices, audit coverage, exception, stop-control, incident, recovery, and retrospective evidence.

Do not request names, raw emails, phone numbers, credentials, tokens, payment credentials, private messages, exact locations, protected attributes, private recordings, complete production logs, or unrelated histories when redacted contracts and aggregates are sufficient.
