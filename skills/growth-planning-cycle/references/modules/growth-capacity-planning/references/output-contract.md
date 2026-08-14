# Growth Capacity Planning Output Contract

## Required Order

Return:

1. mode, plan ID and version, state, decision, service or workload, demand and supply units, boundary, period, calendar, market, owners, approvers, cutoff, review, expiry, privacy, and external actions;
2. evidence manifest with verified, inferred, unavailable, and not-applicable states, sources, versions, limitations, contradictions, corrections, and decision-critical requests;
3. demand, commitment, forecast, target, plan, scenario, stress, workload, and conversion records without duplication;
4. resource and capacity ledgers with skills, calendars, restrictions, obligations, lead time, ramp, reliability, states, reserves, allocation, consumption, and verification;
5. flow, queue, WIP, throughput, lead and cycle time, aging, variability, service class, constraint, dependency, contention, utilization, and reserve records;
6. base, upside, downside, surge, stress, recovery, and other conditional cases, plus gap or surplus, sensitivity, triggers, decision dates, stop, and recovery;
7. gap options, monitoring, market and privacy controls, specialist and approval-ready handoffs, pinned sources, version history, residual obligations, and completion record.

## Capacity Contract And Evidence

| Decision / service / boundary | Demand unit / supply unit / conversion | Period / calendar / market | Owner / approver / state | Source / as-of / version | Evidence / limitation / contradiction | Review / expiry / external action |
| --- | --- | --- | --- | --- | --- | --- |

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable`. Request only evidence that can change the model or decision.

## Demand And Workload Ledger

| Series / version | Work item / class / market | Observed / committed / forecast / target / scenario | Arrival / backlog / mix / distribution | Workload conversion and native units | Evidence / uncertainty / overlap | Horizon / trigger / owner |
| --- | --- | --- | --- | --- | --- | --- |

Do not add alternative representations of the same demand.

## Resource And Capacity Ledger

| Resource / owner | Unit / skill / eligibility | Calendar / restriction / obligation | Lead time / ramp / reliability | Requested through verified states | Theoretical / rated / demonstrated / effective | Reserve / allocatable / allocated / consumed / residual |
| --- | --- | --- | --- | --- | --- | --- |

Do not blend native units or treat approval, access, roster, contract, budget, seat, or quota as effective capacity.

## Flow, Service, And Constraint Register

| Service / class | Queue / WIP / arrival | Throughput / acceptance | Lead / cycle / aging / variability | Dependency / shared resource / contention | Candidate constraint / counterevidence | Reserve / breach / escalation / recovery |
| --- | --- | --- | --- | --- | --- | --- |

State whether Little's Law conditions hold before using it. Highest utilization or largest queue is not proof of a constraint.

## Scenario And Gap Register

| Case / version / trigger | Load / mix / assumptions | Effective / reserved / surge / recovery capacity | Constraint / gap / surplus / sensitivity | Reversible option / irreversible commitment | Decision date / stop / recovery | Evidence / uncertainty / residual risk |
| --- | --- | --- | --- | --- | --- | --- |

Do not invent probabilities, targets, demand, headcount, budget, costs, dates, owners, or approvals.

## Option And Handoff Register

| Gap / decision | Eliminate / reduce / shape / improve / add / change / accept option | Lead time / ramp / reversibility / reliability | Cost basis / dependency / customer and employee risk | Trigger / evidence gate / acceptance | Owning Skill / approver / external action | Residual capacity / risk / obligation |
| --- | --- | --- | --- | --- | --- | --- |

Keep option, recommendation, decision, approval, authorization, execution, verification, and result separate.

## Completion Gate

Confirm that decision, boundary, service, work item, customer or participant, product, market, locale, period, calendar, unit, conversion, source, cutoff, version, maturity, evidence state, demand series, workload, supply, skill, eligibility, restrictions, obligations, lead time, ramp, reliability, capacity layer and state, queue, WIP, throughput, lead and cycle time, aging, variability, utilization, service class, dependency, contention, reserve, scenario, trigger, gap, option, uncertainty, privacy, corrections, expiry, handoffs, external actions, and residual obligations are explicit; incompatible quantities were not combined; missing values were not set to zero; demand was not duplicated; theoretical access did not become effective capacity; resources were not double-booked; utilization did not become productivity; Little's Law was gated; protected work was not starved; targets and scenarios did not become forecasts or facts; employment and market-transfer boundaries held; specialist work was routed; actions and outcomes were not invented; and no external action occurred.
