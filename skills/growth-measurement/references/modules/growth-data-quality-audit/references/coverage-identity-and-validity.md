# Coverage, Identity, And Validity

## Reconcile Expected And Observed Population

Start with an expected-population ledger:

| Population layer | Required evidence |
| --- | --- |
| Entity | Person, device, account, workspace, company, order, subscription, transaction, event, or domain unit |
| Eligibility | Inclusion time, state, product, market, channel, consent, role, and exclusions |
| Source | Authoritative creator, expected delivery, partition, schema or app version, and owner |
| Time | Event period, load period, watermark, maturity, late-arrival window, and audit cutoff |
| Observed | Present, missing, late, duplicate, invalid, suppressed, excluded, failed-join, and untested counts |

Report absolute counts and rates with denominators. Reconcile partitions and source totals rather than using raw row volume. Check missing loads, silent partitions, schema versions, market and product exclusions, failed joins, and downstream drops.

For samples, record population, frame, selection method, stratification, sample size, response or availability, fields tested, periods, bias, and inference boundary. Never generalize a convenient or favorable sample to untested scope.

## Preserve Missing States

Keep these distinct: valid zero, null, absent record, missing required field, late, unknown, censored, suppressed, redacted, immature, failed join, invalid, unavailable, not applicable, system default, imputed, and excluded.

Define source, eligibility, expected arrival, watermark, maturity, and field semantics before interpreting absence. Report missingness by product, market, source, version, period, cohort age, and relevant segment. Do not impute without an explicit decision use, method, assumptions, uncertainty, sensitivity, and label.

## Audit Identity And Eligibility

Separate person, device, cookie, household, account, workspace, company, payer, beneficiary, order, subscription, and transaction. Record identity keys, source, namespace, deterministic and probabilistic rules, precedence, confidence, consent, purpose, market, effective period, and version.

Test shared devices, recycled identifiers, aliases, account transfers, bots, guests, anonymous-to-known transitions, cross-device and cross-product joins, household assumptions, participant roles, and eligibility changes. Measure:

- match and coverage rate;
- false merge and false split evidence;
- one-to-many and many-to-one conflicts;
- unresolved and source-disagreement populations;
- downstream denominator, cohort, attribution, experiment, billing, and customer-risk effect.

Do not merge from similarity alone, infer a person behind every device, or reidentify pseudonymous data.

## Audit Uniqueness And Idempotency

Define natural, surrogate, source, event, transaction, idempotency, retry, replay, correction, and version keys. Distinguish legitimate repeated customer behavior from duplicate production or ingestion.

Test exact and near duplicates, retries, replay, out-of-order records, updates represented as inserts, slowly changing dimensions, refund and reversal pairs, order and invoice relationships, subscription periods, and aggregation duplication. Report duplicate entities and economic value before and after each rule, false-positive risk, unresolved matches, and sensitivity.

Do not select a deduplication rule by favorable growth, revenue, conversion, or retention output.

## Audit Event And Field Validity

For events define actor, object, trigger, state transition, eligibility, source, properties, order, timestamp, expected frequency, cardinality, invariants, and version. Test:

- missing eligible events and events before the triggering action;
- duplicate firing, retries, replays, and impossible frequency;
- invalid types, units, ranges, values, nulls, arrays, encodings, and cardinality;
- impossible state transitions and broken event order;
- time zone, clock skew, future and pre-account timestamps;
- differences across web, app, server, product, market, and version;
- reconciliation to product, order, payment, billing, support, or operational truth.

An event name, a nonzero row count, or schema conformance alone does not establish semantic validity.

## Handle Outliers And Exclusions

Separate legitimate high-value customers, rare markets, refunds, chargebacks, failed payments, fraud, bots, abuse, tests, employees, data errors, and unresolved extremes. Define exclusion purpose, rule, threshold, evidence, scope, owner, effective date, version, and downstream use before viewing outcomes where possible.

Preserve immutable raw inputs and traceable transformations. Report included and excluded counts and values. Specify sensitivity across defensible rules. Never delete records or choose exclusions to smooth metrics or improve a result.

## Audit Timeliness And Maturity

Separate event, ingestion, processing, reporting, correction, and as-of times. Define watermark, expected lateness, service objective, cohort horizon, censoring, and maturity date. Report completeness by age and source.

Do not compare a new cohort with a mature cohort as final or treat delayed conversions, renewals, churn, refunds, support, and revenue as complete at ingestion. Route censoring-aware estimation to the relevant analysis Skill and preserve its assumptions.
