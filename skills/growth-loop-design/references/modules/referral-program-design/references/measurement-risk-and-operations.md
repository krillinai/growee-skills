# Referral Measurement, Risk, And Operations

## State And Event Chain

Keep these states distinct:

```text
sender eligible -> prompt assigned -> prompt exposed -> sender participates
-> referral attempted -> delivered -> unique qualified recipient arrives
-> recipient reaches first value -> recipient retained
-> reward qualifies -> pending -> settled or reversed
-> later referral opportunity
```

For each state define actor, affected entity, event, source, timestamp, properties, identity, deduplication, program version, cohort, window, maturity, owner, and reconciliation. A generated code, send attempt, click, signup, or pending reward is not delivery, recipient value, settlement, or retained growth.

## Metric Contract

Report counts beside rates. Keep compatible entity, eligibility, version, market, source, cohort, age, and maturity.

| Measure | Definition boundary |
| --- | --- |
| Sender eligibility | Eligible senders / declared active value-qualified population |
| Participation | Unique participating senders / exposed eligible senders |
| Qualified reach | Unique relevant reachable recipients / delivered referrals |
| Recipient first value | Qualified recipients reaching the declared value event within W |
| Retained recipient quality | Mature first-value recipients repeating value at natural horizon R |
| Retention-adjusted propagation | Compatible participation x recipients x value conversion x retained quality |
| Attributed referral outcome | Qualified outcome assigned by the declared precedence rule |
| Incremental referral outcome | Outcome caused by program eligibility or exposure versus a credible counterfactual |
| Net incremental contribution | Retained incremental contribution minus full incremental program cost |

When a denominator is zero, return `unavailable`. Do not require a universal participation rate, K-factor, cycle time, reward, CAC, retention, payback, fraud, or complaint threshold.

## Identity And Attribution

Define sender and recipient entities; existing-account, household, company, team, device, payment, and cross-market rules; referral windows; first, last, shared, or precedence credit; duplicate codes; multiple senders; organic visits; prior awareness; paid-media overlap; and offline or partner claims.

Attribution supports operations and fulfillment. It does not establish causality. Preserve unassigned and disputed outcomes rather than forcing credit.

## Incrementality And Interference

Prefer a design compatible with the social mechanism: sender-level prompt holdout, sender-level reward holdout, recipient-level treatment where ethical and isolated, account or cluster assignment, market rollout, switchback, threshold, or a bounded observational alternative. Route detailed design to `experiment-design`.

Preserve assignment through recipient value, retention, contribution, complaints, and fraud readout. Check spillovers, multiple senders, recipient overlap, social exposure, network interference, noncompliance, novelty, and cross-channel displacement. Do not compare referred users only with unrelated paid or organic cohorts and call the difference causal.

## Full Economics

Include marginal:

```text
reward and discount value
+ payment, fulfillment, settlement, and liability
+ partner, affiliate, creator, media, and platform fees
+ engineering, operations, support, dispute, and recovery
+ fraud and abuse loss
+ cannibalized organic or portfolio contribution
+ tax, compliance, privacy, and risk operations
+ capacity and opportunity cost
= full incremental program cost
```

Use retained incremental contribution at a mature compatible horizon. Avoid double counting. State cash timing, currency, refunds, variable cost, serving cost, uncertainty, concentration, payback, and forecast assumptions.

## Layered Risk Controls

| Stage | Controls to consider |
| --- | --- |
| Eligibility | Value prerequisite, relationship, market, account age, limits, exclusions, disclosed rules |
| Referral | Rate and frequency limits, recipient relevance, sender control, link safety, delivery and consent checks |
| Qualification | Identity and existing-user rules, event quality, cancellation, return, duplicate and graph review |
| Settlement | Delay, cap, reserve, manual review, reason code, reversible fulfillment, ledger reconciliation |
| Post-settlement | Behavior and cluster monitoring, complaint review, recovery, appeal, model and rule audit |

Treat device, IP, address, payment, velocity, graph, or behavior matches as signals. Combine proportional evidence, preserve legitimate shared contexts, measure false positives by segment, and provide review and appeal. Do not reveal exploitable thresholds in participant-facing materials.

## Operations And Incident Plan

Assign owners for product, growth, finance, risk, support, privacy, legal or policy, analytics, engineering, and market operations where applicable. Define:

- program and terms versioning;
- eligibility and exposure release checks;
- delivery, landing, event, reward, and ledger reconciliation;
- budget, liability, settlement, capacity, and support monitoring;
- complaint, fraud, fairness, privacy, and trust review;
- exceptions, manual review, appeals, corrections, and incident severity;
- pause, rollback, reward protection, communication, and audit trail;
- taper, stop, archive, and post-program observation.

Completion proof is an inspectable artifact, query result, reconciliation, approval, or test result. A task marked complete or a dashboard screenshot alone is insufficient.
