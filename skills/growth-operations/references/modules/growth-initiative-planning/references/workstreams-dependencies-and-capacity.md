# Workstreams, Dependencies, And Capacity

## Design The Minimum Workstream Set

Create a workstream only when it produces required evidence, an operating capability, customer value, business value, or a governing control. Possible classes include research, measurement, experiment, product, acquisition, activation, retention, monetization, referral, sales, content, launch, infrastructure, operations, support, localization, trust, risk, governance, maintenance, and decommissioning.

Classify each workstream:

- `required`: necessary for the selected outcome, prerequisite, or protection;
- `optional`: useful only after a named gate or if capacity remains;
- `deferred`: explicitly outside the current horizon, with a reopen rule;
- `routed`: owned by a specialist workflow, with an input and output contract.

For every workstream record ID, class, outcome contribution, artifact or evidence, owner, collaborators, inputs, dependencies, capacity, budget boundary, earliest start, due or maturity date, metric, guardrail, completion proof, risk, escalation, and permission boundary.

## Model Dependencies Explicitly

Use these dependency types:

| Type | Meaning | Example |
| --- | --- | --- |
| `hard` | Successor cannot validly start or complete first | Usage metering before usage-based billing |
| `soft` | Parallel work is possible but increases rework or risk | Positioning evidence before broad creative production |
| `evidence` | A result or maturity gate changes whether work should continue | Retention maturity before distribution scale |
| `approval` | Accountable review or authorization is required | Privacy review before new data use |
| `capacity` | Scarce people, system, vendor, budget, or attention constrains work | One data team shared by two launches |
| `external` | A third party, market event, platform, contract, or delivery lead time controls timing | Vendor integration or app review |

Record predecessor, successor, owner, dependency type, lead-time range, calendar, evidence state, confidence boundary, failure signal, buffer, alternate path, escalation, and replan trigger. Do not treat an assumption as a completed dependency.

## Derive Sequence And Critical Path

1. Draw the dependency graph from required work and gates.
2. Remove optional work that does not change the outcome or decision in the horizon.
3. Apply supported duration ranges, calendars, capacity, approval lead times, evidence maturity, and buffers.
4. Find paths that control the earliest valid outcome or next irreversible commitment.
5. Mark the supported critical path, near-critical paths, unresolved durations, and external concentration.
6. Define alternate, cap, pause, stop, rollback, and replan rules before dependent exposure.

When durations or calendars are unavailable, do not invent dates or calculate false precision. Return the dependency order, provisional critical path, unresolved inputs, and decision date for obtaining them. A target date is a constraint, not proof that the sequence fits.

## Freeze Capacity Units

For each capacity source record:

| Field | Requirement |
| --- | --- |
| Unit | Named role, skill, team, vendor, system, budget, or leadership decision capacity |
| Availability | Period, calendar, amount or range, location or time-zone constraint, and evidence state |
| Ownership | Resource owner, initiative allocation owner, and required approver |
| Allocation | Existing commitments, new commitment, utilization, buffer, and contention |
| Cost | Currency, accounting basis, cash timing, fixed and variable components, and approval state |
| Operating reserve | Maintenance, incidents, support, reliability, accessibility, trust, compliance, and customer protection |
| Failure path | Shortfall signal, substitute, scope reduction, defer, pause, stop, or escalation |

Use compatible capacity units. Do not add engineering weeks, media spend, vendor lead time, and leadership attention into one score. Do not allocate the same person, budget, inventory, or system capacity more than once.

## Distinguish Capacity States

- `available`: directly evidenced and not otherwise committed;
- `committed`: accepted by the accountable owner for the period and scope;
- `contingent`: depends on a named decision or event;
- `requested`: proposed but not approved or accepted;
- `unavailable`: known not to exist in the required period;
- `displaced`: removed from another obligation with explicit opportunity cost.

A staffing plan, hiring request, vendor proposal, or budget line is not committed capacity. Keep headcount, contractor, media, infrastructure, incentive, support, and risk budgets separate.

## Protect Operations And Existing Customers

Include applicable work for:

- reliability, incidents, observability, accessibility, security, privacy, fraud, compliance, and data quality;
- current customer support, customer communication, migration, refunds, reversibility, and service continuity;
- localization, platform operations, payments, invoices, fulfillment, sales enablement, and partner readiness;
- maintenance, technical and process debt, documentation, knowledge transfer, decommissioning, and residual obligations.

These are not optional merely because they do not create new signups. Growth cannot compensate for noncompensable customer or system harm.

## Resolve Infeasibility Honestly

When required work exceeds capacity or the horizon:

1. preserve the outcome and protection constraints;
2. identify the controlling bottleneck and work displaced;
3. reduce scope, sequence a smaller eligible population, or choose a reversible stage;
4. defer optional work and expose the opportunity cost;
5. request a bounded capacity, budget, scope, or date decision;
6. pause or stop if no feasible protected path remains.

Do not compress review, maturity, support, rollback, security, privacy, or other controls to maintain a promise. Do not call a knowingly infeasible plan ambitious.
