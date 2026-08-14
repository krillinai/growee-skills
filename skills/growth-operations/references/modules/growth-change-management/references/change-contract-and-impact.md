# Change Contract And Impact

## Contents

1. Change object and evidence states
2. Decomposition and source lineage
3. Current and target operating states
4. Participant, authority, and impact map
5. Dependencies, capacity, and sequencing

## Change Object And Evidence States

Create one record for one decision-bounded change.

| Field | Minimum contract |
| --- | --- |
| Identity | Change ID, version, parent and child IDs, mode, record state |
| Decision | Decision question, intended customer and business outcome, decision owner, state, date, review, expiry |
| Authority | Sponsor, approver, authorizer, change owner, operators, independent verifier, stop and rollback authority |
| Boundary | Product, customer, participant, market, locale, system, data, process, policy, period, cutoff, exclusions |
| Transition | Current state, target state, coexistence, sequence, migration, cutover, fallback, rollback, decommissioning |
| Evidence | Source, owner, version, date, exact claim, evidence state, applicability, limitation, contradiction |
| Outcomes | Adoption unit, intended mechanism, metric versions, maturity, guardrails, alternative explanations |
| Governance | Access, privacy, rights, retention, review, correction, external-action boundary |

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing fields. A reported statement without inspectable support may be kept as a `reported signal`, not silently upgraded. `Unavailable` is not zero, safe, passed, or not applicable.

Keep these states distinct:

```text
proposal -> recommendation -> decision -> approval -> authorization
-> assignment -> execution -> verification -> exposure -> adoption
-> customer outcome -> business outcome -> causal estimate
```

Do not infer any state from the next or prior state. An approval is not authorization; deployment is not exposure; exposure is not adoption; an outcome is not a causal estimate.

## Apply The Commitment Gate

| Field or transition | Minimum attributable basis |
| --- | --- |
| Owner, sponsor, champion, or assignment | Exact role, authority, accepted responsibility, capacity, scope, population, period, and escalation |
| Readiness, resistance, confidence, or score | Defined construct, observable inputs, source, method, compatible population, owner, version, uncertainty, and limitations |
| Date, deadline, phase, or target | Source decision, dependency and capacity basis, owner acceptance, calendar and timezone, conditions, approval state, and review rule |
| Communication or enablement commitment | Audience, purpose, content version, sender or trainer authority, channel or format, permission, capacity, accessibility, support, and evidence |
| Migration, rollout, cutover, or decommissioning | Exact objects and populations, mappings, authority, prerequisites, controls, capacity, dry run, verification, stop, rollback, and residual obligations |
| Adoption, stabilization, or benefit | Eligible denominator, correct repeated workflow, supported duration, exceptions, workarounds, outcome maturity, alternatives, and verifier or causal design |

If the minimum basis is absent, keep the field `unavailable`. Preserve user-specified values in a request ledger without calculating dates, creating 30/60/90 plans, naming executives, reserving champions, assigning owners, inventing targets, or promoting proposed actions into commitments. Urgency, seniority, attendance, completeness, and desired outcomes do not satisfy this gate.

## Decomposition And Source Lineage

Split changes when any of these differ materially:

- source decision or authority;
- product, offer, customer, market, legal entity, or participant population;
- process, system, schema, identity, permission, contract, price, or metric;
- owner, operating workflow, support path, or residual obligation;
- reversibility, migration method, cutover, rollback, risk, or intended outcome.

Classify relationships as `independent`, `prerequisite`, `coupled`, `conflicting`, `shared resource`, `shared audience`, `external`, or `residual`. A parent portfolio records shared assumptions, dependencies, change load, capacity, and sequencing. Every child retains its own source, authority, impact, readiness, migration, rollout, support, rollback, verification, and completion contract.

Maintain a source ledger:

| Source / owner / authority | Version / effective period | Exact decision or claim | Scope and exclusions | Evidence / limitation / conflict | Downstream change fields |
| --- | --- | --- | --- | --- | --- |

Preserve source artifacts by immutable reference. Never overwrite an original decision with a later plan or outcome. Version corrections and supersession explicitly.

## Current And Target Operating States

Describe the state transition as inspectable work, not aspiration.

| Dimension | Current state | Target state | Gap and burden | Coexistence or migration | Acceptance and verifier |
| --- | --- | --- | --- | --- | --- |
| Customer and participant value | | | | | |
| Workflow and process | | | | | |
| Product and entitlement | | | | | |
| Data, identity, and metric | | | | | |
| System and integration | | | | | |
| Policy, contract, and permission | | | | | |
| Operations, support, and incidents | | | | | |
| Market and local conditions | | | | | |

For each row record owner, evidence state, version, applicable population, exclusions, start and end conditions, unresolved conflicts, and residual obligations. Preserve the prior state while a blocking field is unavailable or a reversible path is required.

## Participant, Authority, And Impact Map

Do not use department names as complete participant definitions. Map roles according to the value, workflow, authority, and burden they experience.

| Role / entity | Current and target job | Value / burden / risk | Access / permission / authority | Direct / indirect / temporary / displaced impact | Communication / enablement / support | Adoption evidence / protection |
| --- | --- | --- | --- | --- | --- | --- |

Consider separately when applicable:

- customer, beneficiary, end user, administrator, buyer, payer, approver, champion, and nonuser;
- operator, support, customer success, seller, partner, vendor, and downstream consumer;
- sponsor, decision owner, approver, authorizer, change owner, manager, executor, and independent verifier;
- employee, contractor, applicant, former participant, nonparticipant, and affected third party.

Map impact across value gained, work removed, new work, learning burden, access, permissions, data use, monitoring, errors, workarounds, service continuity, customer promises, compensation or performance implications, accessibility, trust, and exit. Record who is excluded or unable to benefit.

Authority must come from an attributable mandate, not seniority, title, attendance, silence, or enthusiasm. Acceptance and consent cannot be inferred from use when access is mandatory, alternatives were removed, or power is unequal.

## Dependencies, Capacity, And Sequencing

For every dependency record predecessor, successor, type, owner, evidence, lead-time range, earliest usable state, failure signal, alternate path, buffer, escalation, and expiry.

For capacity record:

| Role or resource / owner | Unit / period | Available | Committed | Protected | Contingent | Unavailable | Contention / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include engineering, product, design, data, operations, support, legal, privacy, security, finance, procurement, training, communications, managers, vendors, local teams, and participant attention where relevant. Protect incident response, maintenance, customer support, contractual work, accessibility, compliance, rollback, recovery, and verification capacity.

Build a change-load view by audience and period. Include concurrent changes, context switching, repeated messages, training hours, peak customer periods, blackout windows, migration burden, support demand, leadership review, and recovery space. Do not convert subjective fatigue into a fabricated score. Use observable load, reported constraints, absence, queue time, errors, support demand, or unavailable capacity with limitations.

Sequence prerequisites and hard gates before exposure. Use cohorts, spacing, batching, holding points, alternate paths, and recovery windows. When conflict remains, propose `reduce`, `stage`, `resequence`, `defer`, `pause`, `stop`, or an accountable decision; do not compress controls or assume unlimited attention to preserve a date.
