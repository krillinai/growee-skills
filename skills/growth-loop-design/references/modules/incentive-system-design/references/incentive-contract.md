# Incentive System Contract

## Decision And Mechanism

Capture independently:

- decision, owner, decision date, horizon, review cadence, and allowed action;
- product, business model, market, language, locale, lifecycle role, and program version;
- customer or participant sides, entity, identity, segment, role, payer, recipient, and credible opportunity;
- customer or network value, natural frequency, target behavior, quality, and durable outcome;
- observed barrier, incentive mechanism, non-incentive alternatives, and counterfactual behavior;
- eligible and excluded populations, reason for difference, data inputs, exceptions, and audit trail;
- reward type, amount, currency, face value, realized value, payer, recipient, timing, visibility, terms, expiration, withdrawal, settlement, liability, reversal, tax, and dispute rules;
- assignment or eligibility, exposure, action, product value, fulfillment, repeat behavior, taper, and stop events;
- identity, deduplication, cohort start, observation and maturation windows, cutoff, timezone, source latency, and version;
- organic baseline, holdout or alternative design, interference, attribution, and incrementality assumptions;
- contribution basis, full cost, payback, budget, exposure cap, cash timing, operational capacity, and uncertainty;
- fraud, abuse, cannibalization, quality, trust, fairness, accessibility, privacy, policy, compliance, support, and incident controls;
- source artifact, owner, extraction or field date, evidence state, freshness, and limitation;
- requested production action and separate authorization state.

Version the contract when eligibility, target action, reward, value, terms, market, cost basis, risk rules, experiment, or taper changes materially. Do not combine incompatible versions into one program result.

## Evidence States

Use:

- `verified`: directly supported by an attributable inspectable artifact;
- `inferred`: reasoned from named evidence with the inference explicit;
- `unavailable`: needed but not supplied or observable;
- `not applicable`: outside the declared mechanism and decision;
- `reported signal`: attributable stakeholder statement without inspectable support; leave evidence state blank.

Public evidence may verify visible reward terms, product mechanics, eligibility language, expiry, and dated program claims. It cannot verify private exposure, organic behavior, incremental lift, post-incentive retention, contribution, cost, fraud, cannibalization, complaints, fairness outcomes, or causal impact.

## Event And State Chain

Keep these distinct where applicable:

    eligible
    -> assigned or offered
    -> actually exposed
    -> target action attempted
    -> target action qualified
    -> product or network value attained
    -> reward pending
    -> reward settled or reversed
    -> incentive tapered or removed
    -> post-incentive value repeated

Define source, actor, affected entity, timestamp, identity, deduplication, required properties, version, owner, and reconciliation for every decision-critical state. A code, click, send, generated reward, or payment request is not a qualified action, settled reward, or retained value.

## Privacy Boundary

Prefer aggregate cohorts or pseudonymous eligibility, assignment, exposure, action, outcome, cost, and risk records. Exclude names, raw emails, phone numbers, credentials, payment credentials, bank details, tax IDs, raw messages, exact locations, protected attributes, complete device or social graphs, and unrelated history unless the authorized decision cannot be supported without them.

Document purpose, consent or permissible use, joins, access, retention, minimum cell size, appeal access, output aggregation, and deletion or withdrawal handling.
