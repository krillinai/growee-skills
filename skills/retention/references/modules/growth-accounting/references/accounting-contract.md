# Accounting Contract

Freeze one contract before classification or calculation. Split the bridge when one row cannot describe the entities, periods, values, or markets being combined.

## Decision And Scope

| Field | Required definition |
| --- | --- |
| Decision | Choice, owner, deadline, review cadence, and actions this analysis cannot approve |
| Entity | Accounting unit, hierarchy, eligibility, identity, and exclusions |
| State | Active, inactive, retained, new, resurrected, churned, unresolved, and value states |
| Time | Opening and closing periods, frequency, timezone, cutoff, observation, lookback, maturity, and finalization |
| Scope | Product, plan, price, cohort, segment, market, channel, platform, source, and versions |
| Value | Activity, logo, recurring value, revenue, profit, contribution, cash, currency, and accounting basis |
| Action | Local analysis allowed now and separately authorized data or operating work |

## Entity And Identity

Keep person, user, device, seat, workspace, account, payer, legal customer, contract, subscription, order, transaction, and marketplace participant distinct. Define which entity enters, activates, retains, lapses, returns, pays, expands, contracts, churns, and owns value.

Record identity source, stable key, validity period, duplicate rule, anonymous-to-known transition, household or shared access, guest, merge, split, transfer, acquisition, migration, deletion, and unknown state. A row count is not a customer count unless the entity and deduplication rule make it so.

## State And Time

Define eligible population, qualifying activity or value, entry, first-ever history requirement, retained window, lapse, grace, dormancy, reactivation, resurrection, cancellation, churn, renewal, refund, reversal, and finalization. State precedence when more than one rule might match.

Record event, effective, ingestion, availability, revision, and finalization times. Preserve period length, observation opportunity, seasonality, business calendar, timezone, and fiscal calendar. Recent unresolved outcomes remain preliminary, immature, censored, late, or unavailable rather than zero.

## Value Boundary

Keep bookings, contracted value, billings, invoices, collected cash, recognized revenue, gross profit, contribution, marketplace GMV, one-time services, usage value, and recurring value separate. State currency, exchange-rate source and date, constant- or reported-currency policy, tax, discounts, credits, refunds, reversals, recognition, and cost basis.

Separate operational movements from FX, acquisitions, disposals, migrations, chart changes, product reclassifications, accounting-policy changes, and data corrections.

## Evidence Ledger

For each source record artifact, field, owner, definition, version, entity, state, period, market, value basis, lineage, quality, reconciliation, limitation, and evidence state. Use only `verified`, `inferred`, `unavailable`, or `not applicable`. Keep attributable unsupported statements as `reported signal` without an evidence state.

## Compatibility Gate

Before aggregation or comparison align entity, eligibility, identity, state, precedence, period, observation opportunity, lookback, maturity, cohort, product, price, segment, market, currency, value and accounting basis, source version, adjustment policy, and cutoff. If a mismatch changes meaning, split the bridge or add a visible reconciliation layer.
