# Opportunity Contract

## Freeze The Decision

Record this contract before accepting an estimate or calculating a range.

| Field | Required definition |
| --- | --- |
| Mode | `size`, `compare`, `audit`, or `refresh` |
| Decision | The choice, evidence investment, resource commitment, or gate the estimate informs |
| Owner | One accountable decision owner plus contributors and approvers |
| As-of and horizon | Evidence available by the as-of time and the bounded outcome period |
| Scope | Product, segment, market, mechanism, lifecycle state, and explicit exclusions |
| Entities | User, account, buyer, payer, seller, order, subscription, or other unit and participant roles |
| Customer outcome | First, repeated, expanded, restored, or protected value with a measurable state |
| Business value | Revenue, gross profit, contribution, cash, capacity, risk, or another compatible unit |
| Baseline | Current state with source, definition, segment, period, maturity, and version |
| Eligible population | Who or what can enter the opportunity chain and why |
| External boundary | Local artifacts allowed; system access, data export, mutation, contact, publication, spend, and deployment excluded unless separately authorized |

Do not silently change entity, eligibility, denominator, event, state, window, cohort, maturity, segment, market, currency, accounting basis, or version. Use separate views for incompatible businesses or participant roles.

## Evidence States

Use exactly:

- `verified`: attributable and inspectable within the source and cutoff;
- `inferred`: reasoned from named evidence with the bridge and alternatives visible;
- `unavailable`: required but not supplied, accessible, mature, or compatible;
- `not applicable`: excluded by the frozen contract with a reason.

An attributable claim can remain a `reported signal`. Keep actual, benchmark, estimate, causal estimate, scenario, forecast, target, plan, approval, and realized result separate. Record source, owner, date, version, entity, definition, segment, market, period, value, currency, maturity, sample or coverage, limitations, and contradictions.

## Define Every Transition

For each rate or state change record:

| Element | Definition |
| --- | --- |
| Eligibility | Population allowed to enter the transition |
| Numerator | Qualified outcomes within the declared window |
| Denominator | Original eligible population unless a different contract is justified |
| Start and end states | Observable customer-value or business states, not page labels alone |
| Identity | How entities are deduplicated and joined across states |
| Window and maturity | Time allowed for the outcome and whether the cohort is complete |
| Segment and market | Decision-relevant slice and exclusions |
| Source and quality | System of record, version, missingness, lag, reconciliation, and known bias |

Do not apply a rate to a population outside its eligibility contract. A final immature cohort is unavailable for a mature comparison, not zero.

## Separate Opportunity Layers

| Layer | Meaning | What it does not prove |
| --- | --- | --- |
| Observed baseline or loss | Attributable current state under the frozen contract | Cause or preventability |
| Theoretical headroom | Mathematical difference from a boundary or comparator | Reachability or uplift |
| Reachable change | Eligible portion that a bounded mechanism could plausibly affect | Adoption or retained value |
| Retained opportunity | Customer value that persists through the required maturity | Revenue, contribution, or cash |
| Net decision value | Compatible value minus incremental, recurring, risk, and opportunity costs | Approval or realized result |

Missing evidence changes the commitment. It may justify research, instrumentation, a reversible test, preserving an option, deferral, or rejection rather than a point estimate.
