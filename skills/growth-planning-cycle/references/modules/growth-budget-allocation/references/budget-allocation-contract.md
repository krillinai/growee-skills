# Growth Budget Allocation Contract

## Freeze Identity And Authority

| Field | Required record |
| --- | --- |
| Decision | Allocation ID, version, mode, state, decision question, current version, superseded version, and non-goals |
| Accountability | Accountable owner, contributors, finance owner, allocation-unit owners, specialist reviewers, approvers, escalation, and segregation of duties |
| Scope | Company or portfolio, products, business models, customers, participant roles, markets, locales, lifecycle and channel boundaries, and exclusions |
| Time | Fiscal and calendar bases, horizon, allocation and benefit periods, evidence cutoff, decision date, effective date, maturity, review, and expiry |
| Value basis | Entities, identity, eligibility, units, currencies, exchange-rate sources and dates, accounting basis, cash basis, and valuation exclusions |
| Lineage | Strategy, planning cycle, target, forecast, opportunity, investment case, initiative, metric, experiment, and current-budget versions |
| Governance | Evidence, privacy, market, approval, transfer, spend, communication, system, and external-action boundaries |

Do not silently change the envelope, market, period, customer, unit, currency, accounting basis, cash basis, evidence cutoff, or authority. A pie chart or percentage without this contract is not decision-ready.

## Use Explicit States

For evidence-bearing claims use only `verified`, `inferred`, `unavailable`, or `not applicable`. Preserve source, owner, date, version, definition, population, market, period, maturity, limitations, contradictions, and corrections.

For a resource use the first applicable state and preserve transitions:

| Resource state | Meaning |
| --- | --- |
| `requested` | A party asks for resources; no decision is implied |
| `recommended` | An analysis proposes resources; no approval is implied |
| `approved` | An attributable approver accepted a bounded version and period |
| `authorized` | The required authority permits the named commitment or action |
| `committed` | A binding internal or external obligation exists |
| `encumbered` | The resource is reserved against a known obligation |
| `spent` | Cash left or the resource was consumed under the relevant basis |
| `accrued` | An accounting obligation exists although cash timing may differ |
| `prepaid` | Cash left before the service or value period |
| `recoverable` | Evidence supports a bounded amount and recovery path |
| `available` | Verified, unencumbered, transferable resource exists in the required period |
| `protected` | A governed floor or obligation cannot enter discretionary comparison |
| `discretionary` | Verified available resource remains after restrictions and protections |
| `contingent` | Resource becomes available only after a named trigger and approval |
| `reserved` | Capacity is intentionally held for uncertainty or a governed purpose |
| `unavailable` | Required evidence or resource does not exist for the decision |

Keep recommendation, decision, approval, authorization, allocation, commitment, transfer, spend, verification, and result separate.

## Reconcile The Envelope

Build a resource bridge for cash, headcount, specialist time, engineering or data capacity, creative supply, partner bandwidth, inventory, customer exposure, and operating risk:

```text
declared envelope
- restrictions and nontransferable amounts
- committed and encumbered resources
- consumed resources not recoverable in-period
- protected obligations and reserves
+ verified recoveries available in-period
= discretionary envelope
+ separately governed contingent resources
= maximum conditional envelope
```

Show unresolved residuals. Do not treat a budget request, target, prior-year amount, accounting allocation, open role, shared team, executive preference, or forecast as availability.

Do not subtract reported spend from a reported envelope until the record establishes whether the envelope includes that spend, the fiscal and cash period, destination, accounting basis, commitment state, recoverability, and source. Arithmetic validity does not establish resource availability.

## Require A Numeric Readiness Gate

Recommended numbers require all of the following:

- a verified envelope with period, currency, accounting and cash bases, restrictions, and treatment of prior spend;
- reconciled approved, authorized, committed, encumbered, spent, accrued, prepaid, recoverable, available, protected, discretionary, contingent, and reserved states;
- attributable protection standards, owners, floors, exceptions, and residual obligations rather than an arbitrary reserve;
- compatible allocation units or explicit separate views with source-backed minimum, staged, and maximum resource ranges;
- feasible capacity, dependencies, lead times, transferability, and no double booking;
- named accountable decision owner, required approvers, effective window, review, expiry, and external-action boundary.

When any material condition is unavailable, use `draft` or `reconciling` and omit recommended amounts, percentages, weights, ceilings, floors, reserves, deltas, dates, phases, return thresholds, and release bands. Provide the unresolved ledger and the conditions under which a numeric version could be built. Do not normalize incomplete requests to 100 percent or invent a balancing reserve.

## Classify Costs And Capacity

| Class | Decision question |
| --- | --- |
| Sunk | Has the past resource already become irrecoverable? It cannot justify future allocation. |
| Fixed | Does cost stay unchanged inside the decision band? Fixed does not mean avoidable or cash-available. |
| Variable | Does cost change with a defined unit and range? |
| Step | Which threshold adds another block of cost or capacity? |
| Allocated or shared | Is it an accounting assignment, a real constrained resource, or both? |
| Committed | Which contract, promise, role, or service obligation exists and until when? |
| Avoidable | Which future cost can stop, when, with what impact and proof? |
| Recoverable | Which resource can return, in which amount and period, through what action? |
| Salvage | Which artifact, right, asset, learning, or capacity remains useful after change? |
| Exit or decommissioning | What cancellation, migration, customer continuity, data, vendor, and system work remains? |
| Opportunity | Which compatible alternative or protected work is displaced? |
| Residual | Which obligation remains after funding ends or the program stops? |

For people and shared capacity record role, owner, period, current commitment, transferable fraction, notice, hiring or release lead time, onboarding, ramp, utilization, dependencies, and opportunity cost. Requested headcount is not hired productive capacity.

## Check Compatibility

Before comparing, align entity, identity, eligibility, lifecycle state, customer, product, market, channel, source, metric definition, numerator, denominator, cohort, window, maturity, period, currency, exchange rate, accounting basis, cash basis, cost boundary, and evidence version.

Create a traceable bridge only when the underlying records support it. Keep incompatible markets, business models, currencies, horizons, accounting views, and maturity states separate. Missing, immature, censored, suppressed, and unavailable are not zero.
