# Implementation And QA

## Source Selection

Choose the layer that owns the fact:

| Fact | Preferred evidence |
| --- | --- |
| View, focus, click, or client rendering | Client or browser, qualified by visibility and environment |
| Accepted command or durable state change | Application server or authoritative service |
| Payment, refund, invoice, or chargeback | Payment and billing systems reconciled to order and customer |
| Fulfillment, delivery, or service completion | Operational source that owns completion and reversal |
| Experiment assignment | Deterministic assignment service |
| Treatment exposure | Surface that confirms rendered or delivered treatment |
| Message send and delivery | Orchestrator plus provider receipt, kept separate from customer value |
| Ad attribution | Platform-reported evidence, kept separate from incrementality and business truth |

Do not use a downstream warehouse row as the only definition without tracing its inputs and transformations.

## QA Matrix

Test at least:

- valid happy path and each terminal result;
- ineligible, duplicate, retry, refresh, multi-tab, offline, out-of-order, and late-arrival cases;
- cancellation, refund, reversal, deletion, merge, split, logout, and re-entry;
- missing, invalid, unknown, oversized, unexpected enum, and sensitive-property cases;
- anonymous-to-known and account or workspace transitions;
- consent granted, denied, withdrawn, changed-purpose, and suppression paths;
- assignment without exposure, exposure without treatment, and concurrent experiment cases;
- market, language, locale, product version, app version, web, and device cases that are actually in scope.

For every case state fixture, steps, expected event count, order, actor, entity, properties, prohibited fields, source receipt, downstream row, latency, and cleanup.

## Reconciliation

Define compatible time windows and join keys, then reconcile expected relationships such as:

```text
payment_succeeded <= payment_submitted
order_refunded <= order_fulfilled or payment_succeeded under declared policy
experiment_exposed <= eligible assignments
message_delivered <= provider-accepted sends
accepted_outputs <= generated_outputs
```

These are examples, not universal invariants. State product-specific exceptions, late data, replay, and reversal behavior. Compare counts, missing joins, duplicates, latency, and monetary totals against authoritative sources.

## Release Gates

Require schema review, privacy and security review where applicable, owner acceptance, test evidence, lineage, dashboards or queries for quality only when authorized, alerts, on-call or incident owner, rollback, data repair decision, and consumer communication. Use dual logging when a semantic change needs direct comparison.

## Migration And Backfill

Map old to new events and properties as exact, transformable, incomparable, or retired. Do not rewrite history across changed meaning. Backfill only when authoritative historical facts, transformations, authorization, lineage, validation, and rollback are available. Otherwise show a visible version break.

## Quality Operations

Monitor completeness, freshness, validity, uniqueness, consistency, lineage, and reconciliation. Tie alerts to decision and customer impact, not generic volume alone. Record incident severity, detection, owner, affected versions and consumers, decision freeze, repair or replay, communication, recovery proof, and retrospective.
