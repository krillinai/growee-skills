# RevOps Governance And Roadmap

## Ownership And Decision Rights

Assign accountable owners for revenue strategy, marketing operations, sales operations, partner operations, implementation, customer success, support, product, data, finance, security, privacy, legal or policy, and systems where applicable.

For every shared definition and workflow name the decision owner, source owner, process owner, system owner, quality owner, approver, operator, receiver, exception owner, incident owner, and review cadence. One person may hold several roles; shared ownership without one accountable decision is unresolved.

## Change Contract

Before changing an entity, identity, lifecycle, stage, source, field, routing, territory, ownership, attribution, forecast, price, commercial, revenue, automation, or access rule, specify:

- decision, rationale, owner, approver, affected entities and consumers;
- old and new contract, effective time, version, migration, and comparability break;
- upstream and downstream dependencies, historical backfill or no-backfill, and dual-run;
- privacy, security, financial, customer, employee, and partner review;
- test environment, acceptance criteria, monitoring, fallback, rollback, and incident path;
- communication, training, exception, completion proof, and retirement.

A configuration ticket or announcement does not prove successful implementation.

## Automation Gate

Automate only when:

- the decision and customer outcome are explicit;
- entities, identity, eligibility, definitions, and ownership are stable;
- inputs, outputs, exceptions, and service expectations are contracted;
- source quality, lineage, reconciliation, and permissions are trustworthy;
- action rights, approvals, logs, idempotency, retries, fallback, stop, and recovery exist;
- customer, financial, fairness, privacy, and operational guardrails are monitored;
- manual judgment remains where context changes the decision;
- the automation can be versioned, audited, overridden, and retired.

Do not automate a disputed definition, broken handoff, unbounded exception, or unowned process.

## Roadmap Sequence

Prioritize in dependency order:

1. contain verified critical risk and preserve affected records;
2. freeze the decision, motion, entities, lifecycle, owners, and source-of-truth contracts;
3. repair identity, unknown handling, timestamps, snapshots, access, lineage, and critical quality;
4. reconcile pipeline, commercial, finance, and customer-value states;
5. repair routing, acceptance, handoffs, exceptions, service expectations, and capacity;
6. standardize metrics, reviews, decision logs, and change control;
7. pilot one bounded workflow improvement end to end;
8. add self-service, prediction, or automation only after foundations and operating demand are verified;
9. consolidate or retire duplicate fields, reports, integrations, processes, and tools.

Each item requires finding, decision, owner, dependency, due date, affected scope, change contract, guardrail, decision rule, stop rule, completion proof, and review date.

## Operating Cadence

Use a cadence matched to the motion:

- operational review: routing, queues, handoffs, capacity, exceptions, customer risk, and incidents;
- pipeline and forecast review: as-of snapshot, changes, slippage, concentration, calibration, and decisions;
- reconciliation review: source variances, unknowns, timing, finance, customer value, and closure;
- contract review: disputed definitions, fields, versions, owners, access, and changes;
- lifecycle review: implementation, first value, renewal, expansion, contraction, churn, and promise alignment;
- portfolio review: duplicate, unused, costly, risky, or misleading fields, reports, integrations, automations, and tools.

Reviews must produce a decision, owner, due date, evidence requirement, and follow-up. Meeting count and dashboard consumption are activity.

## Completion Proof

Accept an inspectable approved contract, versioned configuration export, test result, reconciled report, timestamped snapshot, lineage artifact, access review, run log, incident record, rollback test, customer-value cohort, or other source appropriate to the control.

Do not accept a task status, verbal confirmation, screenshot without definitions, dashboard tile, or policy document alone as proof that an operational control works.
