# Marketplace Contract And Evidence

## Decision Contract

| Group | Required fields |
| --- | --- |
| Decision | decision, owner, permitted action, horizon, consequence, review cadence |
| Customer and participants | customer, user, provider, supplier, buyer, requester, payer, beneficiary, operator, nonparticipant |
| Atomic market | geography, time, category, use case, service promise, product version, language, legal entity |
| Core interaction | request, candidate, match, commitment, payment, fulfillment, value, quality, repeat |
| Marketplace need | side-specific problem, natural frequency, current alternative, hard-side hypothesis, constraint |
| Economics | participant value, acquisition, onboarding, utilization, revenue, contribution, incentives, full cost |
| Governance | identity, permission, access, trust, safety, accessibility, privacy, security, support, appeals, incidents |
| Boundary | scope, exclusions, dependencies, specialist review, external actions, expiry, residual obligations |

The atomic market is the smallest unit where relevant supply and demand can complete the promised interaction. It may be geographic, temporal, categorical, workflow-based, account-based, or a combination. Never call the whole marketplace liquid when evidence applies to one unit.

## Entities And State Paths

Keep these entities separate even when one person fills several roles:

- participant identity and role;
- supplier or provider account;
- inventory, listing, capacity, or available service unit;
- buyer, requester, or demand account;
- query, request, intent, or job;
- candidate set, offer, match, or allocation;
- transaction, booking, contract, or commitment;
- payment, settlement, refund, fee, subsidy, and dispute;
- fulfillment, delivery, service completion, quality, and incident;
- review, reputation, support case, repeat interaction, retention, and exit.

Supply states:

```text
eligible -> started -> verified or qualified -> onboarded -> listed or scheduled
-> available -> discoverable -> responsive -> accepted -> fulfilled -> retained
```

Demand states:

```text
eligible -> discovered marketplace -> searched or requested -> saw candidates
-> received response or offer -> accepted -> paid or committed -> fulfilled -> repeated
```

Define unknown, ineligible, duplicate, unavailable, hidden, no-result, abandoned, nonresponsive, rejected, expired, cancelled, failed, refunded, disputed, incident, off-platform, churned, resurrected, and exited states.

## Evidence States

Use exactly:

- `verified`: attributable, inspectable, compatible evidence;
- `inferred`: explicit reasoning from named evidence with uncertainty;
- `unavailable`: required but not supplied, current, mature, or compatible;
- `not applicable`: outside the declared market and decision;
- `reported signal`: attributable statement without inspectable support; leave evidence state blank.

Do not fill unavailable data with zero or penalize inaccessible private evidence. Public cases can verify dated public claims, not current local liquidity, private economics, quality, controls, incidents, or causality.

## Evidence Manifest

For every artifact, record type, owner, source, as-of, period, entity, side, atomic market, definition, version, incentive state, cohort maturity, evidence state, compatibility, limitation, contradiction, decision use, and expiry.

Keep actuals, forecasts, plans, surveys, vendor claims, participant reports, experiment results, benchmarks, and company cases separate. Do not combine cities, categories, time windows, sides, cohorts, currencies, product versions, or rewarded and organic activity without compatibility proof.

## Minimum Evidence

Prefer aggregate, redacted, pseudonymous, or small-cell-suppressed evidence:

- participant and market-unit definitions;
- aggregate side-specific state counts including zero and failure states;
- availability, search, request, candidate, response, match, completion, quality, time, and repeat distributions;
- mature cohorts for side retention, utilization, economics, incentives, and post-incentive behavior;
- aggregate fraud, incident, complaint, dispute, refund, support, appeal, and recovery evidence;
- metric contracts, lineage, reconciliation, change logs, decision records, and experiment summaries;
- local operating capacity, queues, manual work, costs, owners, gates, and retrospectives.

Do not request names, raw contact details, precise individual locations, private messages, payment credentials, identity documents, biometrics, health or disability data, protected traits, background checks, access tokens, employee records, or unrelated full histories. Route consequential participant, worker, privacy, security, employment, and legal decisions to accountable specialists.
