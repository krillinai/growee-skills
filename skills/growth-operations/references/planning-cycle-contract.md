# Planning Cycle Contract

## Choose The Cycle

| Cycle | Primary use | Typical horizon | Do not assume |
| --- | --- | --- | --- |
| Annual | Reconcile medium-term direction, outcomes, portfolio, capacity, budget, and governance | Usually 6-18 months | that fiscal year, calendar year, or strategy horizon are identical |
| Quarterly | Convert current strategy and evidence into bounded decisions, commitments, and initiative readiness | Usually 3-6 months including maturity and follow-up | that every outcome matures inside the quarter |
| Rolling | Refresh specified decisions as evidence and conditions change | Explicit lookback, committed period, and forward horizon | that continuous change removes approval or version control |

Record fiscal and calendar conventions, time zone, market holidays, decision and evidence periods, and any overlap between cycles. Cadence does not override evidence maturity.

## Freeze Required Fields

| Field | Requirement |
| --- | --- |
| Identity | Cycle ID, version, mode, state, cadence, title, and superseded version |
| Time | Horizon, periods, planning start, evidence cutoff, decision dates, effective period, review, refresh, and expiry |
| Scope | Company, portfolio, product, market, customer, business model, included decisions, exclusions, and non-goals |
| Accountability | Planning owner, artifact owners, decision owners, contributors, forums, approvers, escalation, and decision rights |
| Lineage | Strategy, metric, target, forecast, opportunity, investment, organization, portfolio, initiative, risk, and prior-review versions |
| Governance | Evidence states, approval states, privacy, market, communication, system, spend, and external-action boundaries |

Do not silently change the cycle unit, fiscal basis, metric definition, market, customer, scope, or evidence cutoff.

## Use Explicit Cycle States

| State | Meaning |
| --- | --- |
| `draft` | Scope or required inputs are incomplete |
| `reconciling` | Inputs exist but compatibility, tradeoffs, or decisions remain open |
| `decision-ready` | Material inputs, alternatives, consequences, owners, and requested decisions are explicit |
| `blocked` | A named evidence, decision, dependency, resource, risk, or approval prevents valid progression |
| `approved` | Attributable authorized approver evidence exists for the bounded version and effective period |
| `active` | Separately authorized commitments are operating under the approved record |
| `superseded` | A later version replaces this cycle while preserving its history |
| `cancelled` | An accountable decision ends the cycle and assigns residual obligations |
| `expired` | The decision, evidence, approval, or effective period lapsed without valid renewal |

A state is not proof of implementation, completion, outcome, or causal impact.

## Build The Artifact Manifest

For every input record:

- artifact type, stable ID, version, title, and owner;
- decision served, scope, customer, product, market, segment, entity, and period;
- source, as-of date, evidence cutoff, effective dates, maturity, and evidence state;
- approval state, approver, conditions, expiry, and superseded artifact;
- dependencies, downstream consumers, limitations, contradictions, and refresh trigger.

Use `required`, `conditional`, `optional`, `unavailable`, `superseded`, or `not applicable` for planning availability. Availability does not replace `verified`, `inferred`, `unavailable`, or `not applicable` evidence state.

## Keep Planning Layers Separate

```text
vision and context
-> strategy choices and exclusions
-> metrics and baseline
-> independent target and forecast
-> opportunity and alternatives
-> investment and portfolio decisions
-> organization, capacity, and budget boundaries
-> initiative plans
-> operating review and refresh
```

The cycle checks handoffs and ordering. It does not synthesize a missing layer from downstream tasks. A prior-year budget, roadmap, target, or task list cannot substitute for strategy.
