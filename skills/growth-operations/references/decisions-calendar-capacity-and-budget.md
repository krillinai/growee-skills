# Decisions, Calendar, Capacity, And Budget

## Build The Decision Register

For every material decision include:

| Field | Requirement |
| --- | --- |
| Decision | Bounded question, owner, contributors, forum, required approver, and decision rights |
| Alternatives | Current state plus credible choices, exclusions, and consequences |
| Inputs | Artifact IDs and versions, evidence, contradiction, maturity, and unavailable inputs |
| Dependencies | Predecessor decisions, external events, lead times, capacity, and failure paths |
| Timing | Earliest valid date, latest useful date, meeting or forum, expiry, and refresh trigger |
| Output | Selected state, rationale, conditions, downstream artifact, owner acceptance, and effective period |
| Control | Risk, guardrails, cap, stop, rollback, escalation, permission, and residual obligation |

Use `select`, `preserve`, `revise`, `defer`, `reject`, `stop`, or `route` only when the current evidence and authority support it.

## Sequence Decisions Before Dates

Use dependency types `hard`, `evidence`, `approval`, `capacity`, and `external`. Build the directed decision graph before assigning calendar dates. Common ordering includes:

```text
strategy and scope
-> metric and baseline compatibility
-> independent target, forecast, and opportunity views
-> alternatives, investment, and portfolio decisions
-> organization, capacity, and budget commitments
-> initiative readiness and authorization
-> mature operating review and refresh
```

Parallelize only compatible work. Record owner, lead-time range, calendar, evidence state, buffer, alternate, failure signal, escalation, and replan trigger. If durations are unavailable, return a provisional graph rather than a false critical path.

## Match The Calendar To Maturity

Schedule each gate by the evidence or operating state it requires. Distinguish:

- planning-start and submission dates;
- evidence cutoff and data availability;
- cohort, contract, revenue, refund, retention, LTV, and guardrail maturity;
- decision, approval, effective, initiative-readiness, and review dates;
- preliminary, mature, long-term, expiry, and refresh gates.

Meetings do not mature evidence. Use `unavailable`, `defer`, `investigate`, or a clearly provisional decision when the valid horizon exceeds the forum date.

## Reconcile The Initiative Portfolio

For each supplied portfolio commitment record class, outcome, evidence, capacity, budget boundary, opportunity cost, dependencies, interaction, customer protection, decision, approval, initiative-plan version, maturity, graduation, cap, stop, fallback, expiry, and review.

Do not create a portfolio choice when strategy or authority is missing. Do not make every item top priority, allocate a universal ratio, or preserve work only because it already exists. Show selected, preserved, deferred, rejected, stopped, and routed work plus the evidence that could reopen it.

## Freeze Capacity

| Field | Requirement |
| --- | --- |
| Unit | Role, skill, team, vendor, platform, inventory, budget, or leadership decision capacity |
| Availability | Amount or range, period, calendar, location or time-zone constraint, and evidence state |
| Ownership | Resource owner, allocation owner, and required approver |
| Commitments | Existing work, new work, shared dependencies, utilization, buffer, and contention |
| Reserve | Maintenance, incidents, support, trust, compliance, accessibility, and customer protection |
| Shortfall | Bottleneck, work displaced, substitute, scope reduction, defer, pause, stop, or escalation |

Use `available`, `committed`, `contingent`, `requested`, `unavailable`, or `displaced`. Hiring plans and vendor proposals are not available capacity. Do not allocate the same resource twice.

## Freeze Budget Boundaries

For every budget view record owner, currency, conversion basis, accounting and cost scope, cash timing, period, fixed and variable components, committed, approved, contingent, requested, unavailable, and shared amounts, uncertainty, and approval evidence.

Separate spend, cost, saving, revenue, gross profit, contribution, cash, and valuation. A cost cannot also be a saving without an explicit counterfactual and bridge. A budget does not prove opportunity, impact, staffing, procurement, or authorization outside its bounded approval.

## Include Operating Obligations

Preserve applicable capacity and budget for current customers, support, reliability, accessibility, privacy, security, fraud, compliance, data quality, localization, incidents, migrations, refunds, communication, maintenance, documentation, knowledge transfer, decommissioning, and vendor exit.

When the portfolio does not fit, reduce scope, sequence, defer, stop, or request a bounded resource decision. Do not remove controls or compress maturity to preserve a date.
