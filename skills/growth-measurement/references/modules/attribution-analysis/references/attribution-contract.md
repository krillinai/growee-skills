# Attribution Contract

Complete this contract before interpreting a channel report, comparing models, reconciling systems, or specifying implementation.

## Decision Header

| Field | Requirement |
| --- | --- |
| Mode | `audit`, `design`, or `reconcile` |
| Decision | The operational decision attribution supports; causal or budget decisions require additional evidence |
| Owner | Accountable human role; do not infer approval |
| Outcome | One declared conversion, value, commercial, or customer state |
| Entity | Person, user, account, workspace, opportunity, order, subscription, payer, customer, or another explicit unit |
| Product and market | Product, offer, package, market, language, locale, platform, and relevant versions |
| Horizon | Touchpoint, conversion, cohort, maturity, refund, and re-read windows |
| Model version | Exact rule, configuration, effective dates, and owner |
| Action boundary | Local analysis, implementation specification, or separately authorized action |

## Evidence States

Use only:

- `verified`: inspectable evidence establishes the scoped statement;
- `inferred`: bounded reasoning from identified evidence, with alternatives;
- `unavailable`: evidence needed for the claim was not supplied or inspectable;
- `not applicable`: the field does not apply to the frozen contract.

Keep a `reported signal` separate when a stakeholder, partner, or platform statement has no inspectable support. Record source, entity, market, versions, time, scope, limitation, and counterevidence.

## Entity And Identity Map

Record applicable layers:

```text
device or browser -> anonymous identifier -> email or login -> user
-> household, workspace, team, account, buying group, or marketplace side
-> opportunity, contract, subscription, order, payer, customer, and revenue entity
```

For each join, state key, source, authority or consent, deterministic or probabilistic method, timestamp, version, conflict handling, merge and split logic, expiry, correction, deletion, and audit path. Never infer joins merely to increase match rate.

## Outcome Contract

Define name, decision use, entity, eligibility, numerator or event, source truth, exclusions, start, end, natural frequency, maturity, market, product version, currency, cost scope, reversal treatment, and owner. Keep lead, signup, install, first value, opportunity, booking, payment, revenue, retained value, and contribution separate.

## Source And Touchpoint Contract

For every source family and touchpoint, state taxonomy, channel, platform or partner, campaign and content version, actor, event, eligibility, view or interaction rule, timestamp and timezone, destination, identity state, market, permission, late-arrival rule, lookback eligibility, and source precedence.

Preserve direct, unknown, unattributed, consent-denied, unmatched, blocked, deleted, internal, test, bot, fraud, duplicate, and unclassified states. Never reallocate them silently.

## Attribution Rule

Record:

- eligible conversion and touchpoint entities;
- first, last, multi-touch, platform, MMP, code, opportunity, or custom logic;
- click, view, session, or other lookback windows;
- conversion time and late touchpoint treatment;
- source precedence, direct-return, self-referral, branded, reattribution, and reactivation rules;
- cross-device, cross-domain, app, offline, and account logic;
- unknown and disputed treatment;
- rule version, effective dates, owner, audit, fallback, and retirement.

## Privacy Boundary

Request only fields necessary for the decision. Prefer aggregate, redacted, or pseudonymous tables. Record purpose, authority, consent, joins, access, retention, minimum cells, suppression, correction, deletion, and reidentification risk. Exclude protected traits, raw communications, credentials, exact location, payment secrets, unrelated histories, and named journeys unless separately necessary, authorized, and governed.
