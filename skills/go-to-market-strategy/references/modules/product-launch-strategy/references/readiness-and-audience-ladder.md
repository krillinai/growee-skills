# Readiness And Audience Ladder

## Readiness Matrix

Record every gate as `verified ready`, `verified blocked`, `inferred`, `unavailable`, or `not applicable` with source, owner, affected audience, decision impact, remediation, and completion proof.

| Gate | Required questions |
| --- | --- |
| Customer and value | Is the audience explicit, the problem real, the product suitable, and first plus repeated value observable? |
| Product | Are quality, reliability, performance, accessibility, compatibility, safety, data, and failure states acceptable for this stage? |
| Security and privacy | Are identity, permissions, data use, access, retention, transfer, incident, and required reviews owned? |
| Experience | Do access, onboarding, documentation, migration, errors, fallback, support, and destination continuity work? |
| Measurement | Are eligibility, assignment, exposure, value, cohorts, maturity, lineage, reconciliation, and guardrails trustworthy? |
| Operations | Can infrastructure, support, success, implementation, moderation, billing, finance, sales, and partners serve the stage? |
| Distribution | Are positioning, proof, claims, assets, demonstrations, channels, communications, and handoffs approved and accurate? |
| Decision and recovery | Are advance, hold, repair, pause, rollback, incident, retirement, and postmortem owners and proof explicit? |

Marketing readiness cannot override a verified customer, product, security, privacy, accessibility, reliability, support, financial, or rollback blocker.

## Audience Ladder Record

For each stage capture:

```text
stage and audience entity
learning decision and reason this audience is next
eligibility, exclusions, source, permission, and suppression
access mechanism, capacity, timing, expiry, and identity
first and repeated value, qualitative evidence, and maturity
product, experience, support, economic, trust, and risk guardrails
advance, hold, repair, pause, rollback, and retirement rules
owner, approver, communication, evidence, and completion proof
```

Possible labels include internal, employee, design partner, trusted customer, waitlist, private beta, early access, limited availability, segment, existing customer, partner, region, and general availability. Labels do not imply a universal order or quality level.

## Waitlist Gate

Treat a waitlist as a source and intent registry, not verified demand. Reconcile date, source, promise, market, language, identity, duplicate, bot, employee, existing customer, role, permission, suppression, intent, freshness, eligibility, capacity, access offered, accepted, expired, declined, and no-response states.

Measure access acceptance, first value, repeated value, support, and mature customer outcomes. Open and click rates describe communication behavior, not product value.

## Existing-Customer Gate

Separate account enablement, administrator authorization, user eligibility, user exposure, migration, adoption, contract, billing, renewal, and support. Require data and feature parity, permissions, training, documentation, success capacity, dual-run or fallback where applicable, and rollback.

Do not force a migration or expansion to hide weak new-scope value. Route detailed expansion inside an existing relationship to `customer-expansion-strategy`.

## Advance And Stop Rules

Advance only when current-stage value and critical guardrails are sufficiently mature for the next decision. Hold when evidence is unavailable or immature. Repair the earliest verified dependency. Pause or roll back when customer harm, safety, security, privacy, reliability, financial, support, trust, or operating thresholds are exceeded.

Record containment, evidence preservation, affected audience, product state, communication owner, customer help path, rollback, restart criteria, and review date. This Skill specifies these actions but does not execute them.
