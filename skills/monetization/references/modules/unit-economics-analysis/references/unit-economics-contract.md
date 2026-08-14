# Unit Economics Contract

Freeze this contract before calculating, comparing, forecasting, or acting on customer economics. Split the model whenever one row cannot describe every entity, cohort, product, market, channel, cost, value, or period being combined.

## Decision Header

| Field | Required definition |
| --- | --- |
| Mode and decision | `audit`, `model`, or `portfolio`; owner, deadline, threshold, and actions not authorized |
| Customer unit | Beneficiary, user, seat, workspace, account, legal customer, payer, contract, order, transaction, or marketplace side |
| Acquisition cohort | Eligibility, entry event, new or returning rule, original denominator, start period, source, market, exclusions, and maturity |
| Product and market | Product, offer, package, price, version, segment, geography, language, locale, and availability |
| Acquisition | Channel, campaign, motion, spend period, conversion lag, attribution rule, counterfactual, and acquisition-cost basis |
| Value | Customer value, revenue, gross profit, contribution before or after acquisition, cash, LTV method, and horizon |
| Time | Source cutoff, observed period, forecast period, refund and cancellation maturity, censoring, and review date |
| Finance | Currency, FX, tax, invoice, revenue recognition, allocation, capitalization, accrual, and cash policies |
| Model | Equations, assumptions, version, uncertainty, calibration, owner, allowed use, and prohibited use |
| Action | Local analysis allowed now and separately authorized operating action |

## Entity And Identity Hierarchy

Keep lead, signup, activated user, beneficiary, user, seat, device, workspace, account, buyer, payer, legal customer, subscription, contract, order, item, transaction, seller, supplier, and marketplace participant distinct. Define acquisition, value, retention, churn, revenue, cost, and cash ownership for each level.

Record anonymous-to-known stitching, duplicates, shared accounts, multiple payers, multiple products, merge, split, transfer, guest, employee, fraud, deletion, and unresolved identity. One acquisition interaction can create several users or one account; one account can generate several orders; buyer and seller acquisition cannot be added as one customer count.

## Cohort And Timing Contract

Define:

- eligible population and acquisition event;
- original denominator and whether it is a lead, signup, activated user, payer, account, or another entity;
- channel, campaign, partner, sales motion, product, offer, price, segment, and market version;
- spend, touchpoint, lead, signup, activation, sale, implementation, invoice, collection, refund, retention, and churn dates;
- conversion lag and attribution lookback distributions;
- observed horizon, forecast horizon, cohort age, censoring, reporting lag, refund maturity, and finalization;
- timezone, calendar or fiscal period, currency date, and source cutoff.

Do not use same-period cost and customer totals merely because they share a reporting month. Bridge cost to the cohort it could produce. Keep first observed, first acquired, reactivated, resurrected, cross-sold, transferred, and returning entities separate.

## Evidence Ledger

| ID | Claim or value | Entity and cohort | Period and market | Source and lineage | State | Coverage, limitation, next check |
| --- | --- | --- | --- | --- | --- | --- |

Use only `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A `reported signal` is attributable but unsupported and has no evidence state. Preserve zero, missing, late, immature, censored, corrected, disputed, estimated, forecast, target, benchmark, suppressed, and not-applicable states separately.

## Compatibility Gate

Before combining or dividing, align:

- customer and payer entity, hierarchy, identity, and original denominator;
- acquisition event, cohort, source, conversion lag, attribution or incrementality basis, and maturity;
- product, offer, package, price, segment, market, language, locale, and version;
- cost scope, allocation, expense and cash timing, currency, FX, tax, and accounting basis;
- value basis, retention states, observed and forecast horizons, LTV version, uncertainty, and cutoff.

If a bridge changes meaning, keep separate views. Do not normalize every quantity into a customer, use unknown as zero, choose a denominator to improve a ratio, or silently change definitions between numerator and denominator.

## Version And Review

Version the contract, source snapshot, transformations, allocation rules, cohort mapping, equations, scenarios, overrides, outputs, decisions, and actualization. Preserve historical versions and explain revisions. Trigger review when identity, channel, product, offer, price, cost, attribution, customer mix, market, currency, accounting, retention, model calibration, capacity, or decision changes.
