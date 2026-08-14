# Review Contract

## Freeze The Forum

Record this contract before interpreting movement or preparing decisions.

| Field | Required definition |
| --- | --- |
| Review identity | ID, version, `build`, `audit`, or `refresh` mode, and `weekly`, `monthly`, or `quarterly` cadence |
| Time | Review period, as-of time, evidence cutoff, meeting date, and next review |
| Ownership | Accountable review owner, decision owners, contributors, approvers, and escalation forum |
| Scope | Product, model, customer, lifecycle, market, portfolio, systems, risks, and explicit exclusions |
| Decisions | Questions the forum can decide and authority limits |
| Context | Stage, strategy and forecast versions, prior review, targets, assumptions, and material changes |
| Evidence | Authorized sources, freshness, lag, maturity, quality, and unavailable inputs |
| External boundary | Local artifacts allowed; system access, data export, mutation, contact, publication, spend, and deployment excluded unless separately authorized |

The meeting date is not the evidence cutoff. Late data or revisions after cutoff belong to a later version. Do not silently change entity, segment, market, metric, period, currency, accounting basis, or decision authority.

## Evidence States

Use exactly:

- `verified`: attributable and inspectable within the declared source, version, and cutoff;
- `inferred`: reasoned from named evidence with the inference and alternatives visible;
- `unavailable`: required but not supplied, accessible, mature, compatible, or reconciled;
- `not applicable`: excluded by the frozen review contract with a reason.

An attributable statement may remain a `reported signal`. Keep actual, estimate, benchmark, target, forecast, scenario, causal estimate, plan, approval, action, completion, and result separate. Preserve source, owner, date, version, entity, population, definition, market, segment, period, currency, accounting basis, maturity, freshness, limitation, contradiction, and revision.

## Define Metric Contracts

For each decision-relevant metric record:

| Element | Definition |
| --- | --- |
| Customer or business meaning | Value state, process, stock, flow, quality, economics, or guardrail represented |
| Entity and eligibility | User, account, payer, order, revenue, or other unit and who enters the denominator |
| Numerator and denominator | Exact counts, values, exclusions, and original cohort where applicable |
| Event or state | Observable start, outcome, deduplication, and identity rules |
| Window and maturity | Observation period, allowed outcome window, censoring, and mature date |
| Segment and market | Decision-relevant slice, mix, locale, and excluded populations |
| Source and quality | System of record, transformation, freshness, lag, missingness, revisions, reconciliation, and owner |

An incomplete period or immature cohort is unavailable, not zero. Do not put incompatible metrics into one traffic-light score or percentage-change column.

## Choose A Comparison Contract

Use a reference that answers the decision:

- compatible prior period or cohort;
- seasonality-aware historical range;
- target, kept separate from actual and cause;
- forecast frozen at its original as-of date;
- valid control or causal estimate;
- operational or risk boundary;
- versioned strategic assumption.

Record absolute and relative difference, numerator and denominator change, maturity, mix, uncertainty, source revisions, and why the comparison is valid. If it is not compatible, show separate views.
