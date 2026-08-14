# Capacity Contract And Units

## Contract

Record:

| Field | Required content |
| --- | --- |
| Identity | Plan ID, version, mode, state, prior version, owner, contributors, approvers |
| Decision | Decision served, alternatives affected, horizon, review, expiry |
| Boundary | Service or workload, entry, completion, customer or participant, product, market, exclusions |
| Demand | Work item, arrival, backlog, service class, period, mix, complexity, due condition, source |
| Workload | Resource requirement by compatible unit, skill, stage, service, and time |
| Supply | Resource, unit, skill, eligibility, calendar, restrictions, obligations, reserve, reliability |
| Evidence | `verified`, `inferred`, `unavailable`, or `not applicable`; source, as-of, window, version, limitation |
| Governance | Privacy, correction, approval, external actions, review, refresh, supersession |

Keep actual, commitment, forecast, scenario, target, plan, request, recommendation, approval, authorization, allocation, consumption, delivery, verification, effect, and outcome separate.

## Demand Ledger

| Series | Meaning | Never assume |
| --- | --- | --- |
| Observed load | Measured eligible arrivals or workload in a defined past/current window | Complete future demand |
| Accepted commitment | Work the accountable service has admitted under a defined promise | All requests are commitments |
| Forecast | Time-indexed estimate with assumptions and uncertainty | Target, plan, or certainty |
| Scenario | Conditional load used to test a decision | Probability or expected value |
| Target | Desired outcome | Demand evidence or forecast |
| Stress load | Deliberately adverse test condition | Normal operating plan |

For every series record origin, owner, definition, entity, market, service class, horizon, time grain, as-of and cutoff, version, maturity, uncertainty, and overlap with other series. Add series only when they represent mutually exclusive demand or a documented bridge. Never sum the same future load because it appears in sales, marketing, finance, and product plans.

Translate demand into workload with an attributable conversion such as verified handling-time distribution by request class or tested resource consumption by workload shape. When the production relationship is unavailable, retain the demand and resource units separately and request the minimum measurement needed.

## Supply And Capacity States

| State | Meaning |
| --- | --- |
| Requested | Proposed but not approved |
| Approved | Decision permission exists, but resource may not be authorized or usable |
| Authorized | Accountable authority permits commitment |
| Committed | Contractual or internal obligation exists |
| Provisioned | Access, seat, quota, roster, or equipment exists |
| Available | Eligible resource can be used in the period after restrictions and obligations |
| Allocated | Available resource is reserved for named work |
| Consumed | Resource was used |
| Verified | Accepted service or work was delivered and reconciled to the capacity record |

Report capacity layers separately:

1. `theoretical`: physical, payroll, license, quota, or design maximum;
2. `rated`: supplier, design, or policy rating under stated conditions;
3. `demonstrated`: observed or tested output under a compatible workload;
4. `effective`: demonstrated ability after eligibility, calendar, reliability, loss, and obligations;
5. `reserved`: protected capacity unavailable to ordinary allocation;
6. `allocatable`: effective capacity remaining after reserve and fixed obligations;
7. `allocated`: allocatable capacity assigned in the supplied approved record;
8. `consumed`: resource usage observed in the period;
9. `verified`: accepted, quality-passing completion attributable to the period and service.

Do not mechanically multiply unverified percentages. A useful reconciliation is:

```text
allocatable capacity
= demonstrated compatible capacity
- calendar and eligibility losses
- fixed operating obligations
- reliability and variability allowance
- protected reserve
```

Use ranges when inputs are ranges. Preserve every term, unit, period, evidence state, source, and reason. Never infer effective capacity from headcount, contracted hours, unspent budget, cloud quota, seats, or access alone.

## Resource Ledger

| Resource | Unit and period | Skill / eligibility | Calendar / location | Restrictions / obligations | Lead time / ramp / reliability | State / evidence | Owner / expiry |
| --- | --- | --- | --- | --- | --- | --- | --- |

Keep money, people, skill-hours, decision attention, traffic, customer exposure, creative assets, inventory, vendor service, storage, compute, requests, and completed work in their native units. Convert only when a verified relationship exists. A composite capacity score hides the active constraint and is not an acceptable substitute.

## People Capacity

Start with role-, skill-, seniority-, work-type-, location-, timezone-, and period-compatible calendars. Account for holidays, leave, part-time schedules, meetings, support, maintenance, incidents, training, management, handoffs, coordination, context switching, ramp, rework, healthy workload, and reserve. Report rostered, scheduled, eligible, effective, allocatable, allocated, delivered, and verified hours or service units separately.

Do not infer that ten 40-hour employees provide 400 project hours. Do not rank individuals or use private messages, keystrokes, health, protected traits, reviews, salary, precise location, or full history to estimate capacity.

## Numerical Gate

Calculate only when entity, unit, service class, market, calendar, period, source, evidence state, and conversion are compatible. Label rounding, missingness, uncertainty, sensitivity, and residual. If the gate fails, return a measurement specification rather than a number.
