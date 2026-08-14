# Timeline, Mechanisms, And Evidence

## Build A Versioned Timeline

Record exact effective time, timezone, scope, eligibility, access, exposure, owner, source, and rollback or end time for:

- product, feature, onboarding, pricing, package, paywall, recommendation, notification, and infrastructure releases;
- tracking, identity, consent, schema, pipeline, query, attribution, currency, and reporting changes;
- experiments, holdouts, flags, ramp, mutual-exclusion, and interference states;
- campaigns, creative, offers, media budgets, auctions, channels, partners, sales routing, and lifecycle messages;
- incidents, outages, latency, inventory, fulfillment, support, fraud controls, moderation, and policy changes;
- holidays, promotions, paydays, billing, renewals, weather, competitor, platform, regulation, and market events.

Use exposure and affected-unit evidence, not release date alone. Separate announcement, availability, eligibility, access, exposure, adoption, outcome, rollback, and recovery.

## Build Candidate Mechanisms

For each candidate record:

| Field | Requirement |
| --- | --- |
| Mechanism | How the event could change the frozen metric through named states |
| Population | Eligible, exposed, affected, and unaffected units |
| Timing | Expected onset, lag, duration, maturity, carryover, and recovery |
| Supporting evidence | Attributable observations compatible with the mechanism |
| Contradiction | Evidence that limits or opposes it |
| Alternatives | Measurement, mix, seasonality, product, channel, market, and concurrent explanations |
| Causal status | Observation, association, attribution, quasi-experimental estimate, randomized estimate, or unavailable |
| Discriminating check | Smallest lawful read-only evidence that changes the ranking |

Keep symptom, contributor, mechanism, and root cause separate. A segment contribution says where the change appears, not why. A preceding release or campaign is associated in time, not automatically causal.

## Investigate In Evidence Order

1. Verify metric contract, source continuity, freshness, and maturity.
2. Quantify change versus a predeclared compatible baseline and expected variation.
3. Reconcile parent totals and locate material descriptive contributions.
4. Build the change timeline before reading motives into correlations.
5. Compare candidate mechanisms with supporting, contradictory, and missing evidence.
6. Use valid exposure, unaffected units, natural experiments, or randomized evidence where available.
7. Define the next evidence task, monitoring condition, or controlled action request.

Do not begin with stakeholder explanations and retrofit data. Preserve hypotheses proposed by users or leaders as reported signals until evidence supports them.

## Handle Experiments

Preserve eligible, assigned, accessed, exposed, noncompliant, contaminated, and outcome populations; randomization unit; identity; mutual exclusion; overlapping experiments; interference; carryover; novelty; sample-ratio mismatch; metric contract; horizon; and maturity.

Do not assign effects by the last experiment seen, compare raw exposed users as if randomized, or add overlapping experiment estimates. Route integrity, power, estimand, multiple testing, and causal readout to `growth-measurement`.

## Handle Attribution And Channels

Version touchpoint rules, lookback windows, view-through and click treatment, UTMs, platform models, identity coverage, consent, unknown source, organic, direct, overlap, and unattributed states. Keep total observed outcomes, attributed outcomes, incremental outcomes, retained value, contribution, and cash distinct.

An attribution-model change can move channel credit without changing demand. Route detailed source and touchpoint reconciliation to `growth-measurement`, and channel economics and action decisions to `acquisition-strategy`.

## Handle Quality, Fraud, And Abuse

For volume spikes, inspect bot and crawler traffic, internal tests, QA, retries, duplicate identities, device farms, spam, referral rings, incentive abuse, payment fraud, synthetic activity, moderation, and policy changes. Preserve legitimate high-frequency behavior and false-positive risk.

Separate raw events, identities, valid participants, qualified actions, customer value, retained behavior, incentives, refunds, fraud loss, contribution, and trust. Route incentive and referral system changes to `growth-loop-design`; do not change controls during read-only investigation.

## Choose The Next Evidence

Prioritize evidence by its ability to distinguish resolution states or material mechanisms, not by ease of query. For every task define question, required fields or artifact, entity, segment, source, owner, access boundary, method, maturity date, expected outcomes, decision rule, privacy limit, and stopping condition.

If evidence cannot distinguish causes, state `unresolved`. Recommend monitoring only when a future maturity or trigger can change the decision. Recommend containment only as an approval-ready action with customer, trust, data, economic, and operational tradeoffs visible.
