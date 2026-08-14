# Customer Health Contract And Labels

## Decision Contract

| Field | Required content |
| --- | --- |
| Identity | Model ID, version, mode, state, prior version, owner, reviewers, approvers |
| Decision | Question, alternatives, receiving role, permissible use, action capacity, horizon, review and expiry |
| Customer | Modeled entity, hierarchy, products, contracts, roles, market, eligibility and exclusions |
| Outcome | Observable state, start, end, due condition, finalization, maturity, competing states and censoring |
| Snapshot | Prediction or assessment time, feature cutoff, source availability, data vintage and timezone |
| Evidence | `verified`, `inferred`, `unavailable`, or `not applicable`; source, version, limitation |
| Governance | Privacy, suppressions, override, correction, appeal, audit, external actions and supersession |

Keep current customer state, descriptive health dimension, risk prediction, causal explanation, treatment response, target, recommendation, decision, approval, action, verification, and result separate.

## Customer Hierarchy

Record beneficiary, user, guest, practitioner, admin, champion, buyer, payer, approver, sponsor, account owner, workspace, team, subsidiary, parent, legal customer, product, module, contract, subscription, invoice, opportunity, and renewal relationships as applicable.

Freeze the modeled entity and one row-generation rule. Define:

- parent-child and shared-contract relationships;
- account merge, split, migration, acquisition, and legal-entity changes;
- role, seat, workflow, product, contract, and market coverage;
- aggregation, weighting, unknown, residual, and cross-product rules;
- repeated observations and train-validation grouping;
- re-entry, deletion, correction, and historical restatement.

One active user cannot establish account health. One contract outcome cannot label all products or subsidiaries. Split models when entity, value path, product, contract, lifecycle, outcome, horizon, or action differs.

## Customer State Ledger

Preserve separately:

| Dimension | Example states |
| --- | --- |
| Access | Contracted, provisioned, entitled, authorized, suspended, unavailable |
| Lifecycle | Implementing, first value, repeated value, mature, migrated, paused, ended |
| Product value | Opportunity, attempt, success, quality, repeat, retained, lapsed, unknown |
| Reliability and service | Normal, degraded, incident, recovery, unresolved support, escalated |
| Relationship | Observed customer evidence, reported internal signal, disagreement, unknown |
| Commercial | Quote, contract, invoice, paid, delinquent, renewal due, renewed, contracted, churned |
| Decision | Eligible, suppressed, review, abstain, approved, acted, verified, expired |

Do not collapse these into one customer truth. A commercial state can disagree with product value; high usage can coexist with failure or support burden; low use can be normal for a low-frequency job.

## Outcome And Label Contract

Choose one observable outcome per model. Define entity, eligibility, prediction time, horizon, event or state, due condition, grace period, observation end, finalization, source, version, exclusions, competing events, missing outcome, label delay, correction, and expiry.

Possible outcomes include successful implementation, first or repeated value, support escalation, product retention, renewal, contraction, partial churn, full churn, or expansion readiness. These are not interchangeable.

For renewal and churn, preserve fixed-term, auto-renewal, month-to-month, usage, transaction, marketplace, pause, migration, delinquency, negotiation, contraction, partial churn, and complete churn states. A not-yet-due or unobserved renewal is not churn.

For time-to-event models, define time origin, event, competing events, censoring, left truncation, time-varying features, observation cutoff, and risk-set eligibility. For fixed-window models, define the exact window and how customers without mature follow-up are excluded or labeled unavailable.

## Lifecycle And Opportunity Compatibility

Define natural customer-value opportunity, lifecycle stage, tenure, implementation status, product availability, contract timing, support or incident state, seasonality, and outcome maturity. Separate new, implementing, immature, mature, low-frequency, not due, suspended, incident-affected, migrated, and censored populations.

Use stage-specific baselines, stratification, hierarchy, or separate models when appropriate. Do not score an implementation customer from production usage, an annual workflow from weekly activity, or an incident customer from support volume without the relevant state.

## Evidence And Vintages

Record event time, ingestion time, availability time, revision time, finalization time, extraction cutoff, source version, definition version, and value known at every model snapshot. Preserve backfills, source incidents, missingness, identity changes, label revisions, contract changes, and outcome delays. Never backfill past prediction snapshots with knowledge that arrived later.
