# Forecast Contract

Freeze this contract before calculation, comparison, or back-testing. Split the forecast when one row cannot describe the entities, markets, periods, currencies, methods, or decision uses being combined.

## Decision And Output

| Field | Required definition |
| --- | --- |
| Decision | Choice the forecast informs, owner, deadline, thresholds, and actions it cannot approve |
| Outcome | Exact metric, value meaning, entity, level, population, unit, and accounting basis |
| Scope | Product, segment, market, channel, platform, cohort, price or offer version, and exclusions |
| Time | Frequency, timezone, as-of, actual period, forecast origin, horizon, maturity, and review date |
| Version | Data snapshot, definitions, features, assumptions, method, forecast, overrides, and publication |
| Uncertainty | Point, interval, quantile, range, scenario, confidence basis, and unresolved conditions |
| Action | Local analysis allowed now and separately authorized operating changes |

## Entity And Value Boundary

Keep person, user, seat, workspace, account, customer, payer, contract, subscription, order, transaction, marketplace participant, and legal entity distinct. Define who enters, retains, purchases, pays, produces revenue, incurs cost, and owns cash. Preserve hierarchy, duplicate and unknown identity, reactivation, transfer, merger, split, refund, reversal, and deletion.

Keep activity, customer value, booked amount, billed amount, collected cash, recognized revenue, gross profit, and contribution separate. State currency, exchange-rate source and date, tax, discount, cost, recognition, and adjustment basis.

## Series Classes

Every value has one class:

- `final actual`: observed and finalized under the current contract;
- `preliminary actual`: observed but incomplete or subject to revision;
- `estimate or nowcast`: inferred current or past value from partial evidence;
- `forecast`: future expectation from a declared process and information set;
- `scenario or stress case`: conditional output under an assumption bundle;
- `target`: desired value or range;
- `plan`: approved actions, resources, and operating assumptions;
- `budget`: authorized resource boundary;
- `benchmark`: external or historical comparison with transfer limits.

Do not merge these classes, overwrite one with another, or call a target the most likely outcome.

## Data Vintage Ledger

For every source and input record:

- event, effective, ingestion, availability, revision, and finalization times;
- source system or artifact, field, definition, version, and owner;
- entity, cohort, segment, market, product, frequency, unit, and timezone;
- actual known at the as-of date and later revised value;
- missing, zero, late, censored, suppressed, corrected, and unknown states;
- quality, lineage, reconciliation, evidence state, limitation, and action.

Use only `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. `Reported signal` is an attributable unsupported statement, not a fifth evidence state.

## Compatibility Gate

Before aggregation or comparison align entity, eligibility, identity, metric definition, state, cohort, segment, market, product and offer version, frequency, period, maturity, currency, accounting basis, source, cutoff, revision state, method, and horizon. If a difference changes meaning, split the forecast or build an explicit reconciliation layer.

Do not average rates with different denominators, multiply rates across incompatible cohorts, add stocks and flows, combine currencies without a dated conversion basis, or aggregate components that overlap.

## Audit Trail

Preserve forecast origin, input vintage, code or method version, assumptions, overrides, point and interval outputs, publication, decision, actual vintages, back-test, error, revision, owner, and retirement. A rerun with final data is not the original forecast.
