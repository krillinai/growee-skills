# Learning, Governance, Market, And Actions

## Make Learning Reuse Verifiable

Each reusable record includes experiment and decision IDs, versions, customers, product, market, period, evidence design, hypothesis, mechanism, metrics, result state, quality, incidents, counterevidence, limitations, decision, follow-through, long-term status, applicability, exclusions, transfer conditions, expiry, corrections, superseded artifacts, and owner.

Classify a later use as:

- `cited`: the record was referenced;
- `considered`: an owner reviewed applicability;
- `applied`: a later design, metric, decision, guardrail, model, stop rule, or standard changed or was explicitly preserved;
- `validated`: later attributable evidence supports the intended reuse;
- `contradicted`: later evidence limits or reverses the learning;
- `expired`: the transfer or freshness boundary lapsed.

Only `applied` with an attributable artifact change demonstrates use; `validated` adds later evidence. Repository size, searches, citations, publication, or training attendance do not prove reuse. Preserve negative, flat, harmful, invalid, and inconclusive learning when it changes a bounded later decision.

## Measure Program Health In Separate Layers

| Layer | Useful evidence | Main misuse |
| --- | --- | --- |
| Reliability | assignment, exposure, metric, SRM, incident detection, recovery, and recurrence | hiding incidents to improve the rate |
| Adoption and efficiency | eligible teams, appropriate self-service, queue, setup, analysis, review, and decision cycle | calling speed or usage value |
| Question and design quality | decision importance, complete intake, suitable evidence design, power, maturity, and guardrails | testing easy questions to inflate conclusiveness |
| Decision | decisions changed, preserved, stopped, reopened, or unresolved with rationale | counting positive results or shipping |
| Follow-through | authorized actions, completion proof, deviations, and residual obligations | treating implementation as impact |
| Learning | applied, validated, contradicted, expired, and repeated-mistake evidence | counting documents and citations |
| Customer and business | mature retained value, contribution, cash, quality, and trust with attribution limits | assigning total movement to experiments |
| Risk and sustainability | customer harm, privacy, fairness, long-term effects, workload, key-person and platform risk | hiding cost or harm behind velocity |

Do not collapse the layers into one score or universal maturity target. Experiment count and win rate can diagnose workload or selection but should not drive performance incentives.

Before setting any health target, define the entity, eligible population, numerator, denominator, source, baseline, window, maturity, segmentation, owner, decision use, gaming risk, and review trigger. A desirable property such as full registration, complete retention, fast review, or zero invalid use is a control objective, not automatically a numeric target or service level. When baseline, capacity, risk, and authority are unavailable, leave the target and deadline unavailable.

## Assign Risk-Tiered Decision Rights

For each tier define who proposes, reviews, decides, approves, authorizes, executes, can stop, verifies, and receives escalation. Centralize stable contracts, automated checks, shared-surface controls, complex methods, incidents, and high-risk review when evidence supports it. Keep contextual product and customer judgment with accountable teams under common semantics and guardrails.

Avoid both central approval of every reversible low-risk decision and uncontrolled self-service for pricing, safety, privacy, financial, network, persistent, shared-surface, regulated, or high-exposure decisions. Define service levels, queue limits, exceptions, override, audit, correction, and expiry.

Define risk dimensions and required governance questions before naming tiers, thresholds, approvers, or service levels. When the organization, workload, policy, authority, and incident evidence are unavailable, return a candidate governance structure without tier numbers, approval assignments, cadence, or deadlines.

## Transfer Across Markets

Treat each market as a new program and evidence boundary. Revalidate customer, product, surface, channel, app distribution, identity, eligibility, assignment, exposure, traffic, sensitivity, metrics, maturity, interference, holdouts, outcomes, guardrails, data, consent, storage, transfer, platform, vendor, staffing, support, calendars, sources, decision rights, approvals, and incident response.

Translation or shared tooling does not validate transfer. For China, distinguish market, legal entity, language, locale, product, channel, platform, app distribution, identity, payment, invoice, data, content, advertising, support, traffic, capacity, source access, and locally accountable review. Use current direct sources and local expertise. Do not provide legal, regulatory, provider-availability, permissibility, approval, causal, or performance conclusions.

## Protect People And Data

Use aggregate, redacted, pseudonymous, minimum-necessary evidence and small-cell suppression. Define purpose, authority, consent where required, access, retention, deletion, correction, audit, and reidentification controls.

Do not expose credentials, payment details, private messages, health or financial information, protected traits, precise locations, raw identities, full histories, employee reviews, compensation, or ratings. Do not rank experimenters by wins or individuals for employment, pricing, targeting, service, credit, insurance, health, housing, or similar decisions. Protect honest negative results and incident reporting from retaliation and gaming.

## Prepare External Actions

Create local artifacts and approval-ready requests only. For each requested action record owner, system, exact mutation, eligible population, market, timing, prerequisite evidence, maturity, decision, approvers, authorization, privacy, security and domain review, dry run, monitoring, cap, stop, rollback, correction, audit, completion proof, residual obligations, and result boundary.

Do not access authenticated experiment, feature-flag, product, analytics, warehouse, identity, CRM, billing, finance, HR, project, support, cloud, or communication systems; export or join personal data; create experiments; assign users; change traffic, flags, variants, metrics, data, permissions, or records; launch; stop; roll back; contact; publish; send; spend; procure; or deploy.

## Route Specialist Work

| Need | Route |
| --- | --- |
| One experiment, alternative evidence design, power, analysis, or readout | `experiment-design` |
| Company strategy, portfolio thesis, or exclusions | `growth-strategy` |
| Cross-functional resources and budget | `growth-planning-cycle` |
| Platform capability, service contract, sourcing, or roadmap | `growth-infrastructure-assessment` |
| Team structure, staffing, or organization decision rights | `growth-organization-design` |
| Metric contract, event schema, attribution, anomaly, or data issue | the relevant data and measurement Skill |
| Broad recurring business evidence and decision forum | `growth-operating-review` |
| Domain intervention | the relevant lifecycle, channel, pricing, market, launch, or product Skill |

Each handoff records input contract, decision, expected artifact, owner, maturity or due date, dependency, and permission boundary. A handoff does not imply access or execution.
