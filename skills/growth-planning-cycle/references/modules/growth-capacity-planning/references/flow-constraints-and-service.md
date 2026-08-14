# Flow, Constraints, And Service

## Flow Contract

Define work item, eligibility, arrival, admission, entry, queue boundary, WIP, active work, blocked work, exit, acceptance, throughput, lead time, cycle time, aging, abandonment, rework, service class, and observation window. Preserve distributions, percentiles, tails, peaks, mix, and censored items.

| Measure | Definition |
| --- | --- |
| Arrival rate | Eligible items entering the defined boundary per compatible period |
| Queue | Admitted but not active items inside the boundary |
| WIP | All admitted, incomplete items inside the boundary, explicitly including or excluding blocked items |
| Throughput | Accepted completions per compatible period |
| Lead time | Entry-to-acceptance elapsed time distribution |
| Cycle time | Active-start-to-acceptance elapsed time distribution |
| Aging | Elapsed time of incomplete items as of the cutoff |
| Rework | Returned or repeated work under an explicit counting rule |

## Little's Law Gate

Use `L = lambda W` only when the queue or system boundary is bounded, definitions and windows are compatible, arrivals and departures are approximately stable over the relevant interval, the same item population is used, and long-run averages are meaningful. Record exclusions, abandonment, rework, blocked items, and censoring.

Little's Law is a consistency relationship. It does not prove stability, identify a cause, forecast exact dates, authorize a service promise, or justify doubling rates. If its conditions fail, request compatible observations or use a clearly specified simulation or scenario range.

## Constraint Map

Trace demand through dependencies, handoffs, skills, systems, batches, queues, blocking, starvation, rework, quality checks, downstream acceptance, and customer-value completion. Classify candidate constraints:

| Type | Evidence question |
| --- | --- |
| Capacity constraint | Does compatible demand exceed effective service capacity at this point? |
| Policy constraint | Does admission, priority, approval, batch, or decision policy create avoidable delay? |
| Skill constraint | Is eligible capability scarce even when generic hours are available? |
| Dependency constraint | Is work waiting for an upstream or shared prerequisite? |
| Quality constraint | Does failure or rework reduce accepted throughput? |
| Market or demand constraint | Is productive capacity idle because qualified demand or liquidity is absent? |
| Incident | Is the limitation temporary and outside steady-state assumptions? |
| Symptom | Is the queue, utilization, or delay downstream of another constraint? |

Highest utilization, largest queue, or lowest local output is a candidate signal, not proof. Seek counterevidence: downstream starvation, blocked time, rework, batch release, changing mix, acceptance failure, and end-to-end throughput response. Route causal diagnosis or process redesign when evidence cannot distinguish candidates.

## Shared Resources And Contention

For each shared resource record eligible users, calendar, capacity unit, exclusivity, concurrency, setup and switching, maintenance, incidents, existing obligations, dependency order, allocation state, contention, displaced work, opportunity cost, and residual capacity.

Treat customer and experiment exposure, control groups, leadership decisions, specialist reviewers, vendors, inventory, and shared systems as bounded resources where applicable. Preserve interference, mutually exclusive use, cross-market restrictions, and transfer limits. Never allocate one resource at 100 percent to several commitments.

## Service Classes

| Field | Required definition |
| --- | --- |
| Class | Standard, fixed-date, expedite, incident, regulatory, maintenance, or locally defined class |
| Eligibility | Observable admission conditions and accountable approver |
| Promise | Population, outcome, clock, exclusions, target or objective, and evidence source |
| Priority | Queue order, preemption, fairness, aging, and anti-starvation rule |
| Acceptance | Quality and completion conditions |
| Protection | Reserve, privacy, safety, accessibility, customer and employee guardrails |
| Control | Breach, escalation, stop, recovery, review, expiry, and correction |

Do not call every executive request urgent. Protect incident response, security, privacy, accessibility, localization, support, maintenance, customer recovery, and residual obligations. Do not promise the same service level to populations with different work, risk, or clocks.

## Utilization, Variability, And Reserve

Model arrival and service distributions, peaks, seasonality, bursts, mix shifts, failures, retries, rework, blocking, setup, switching, and recovery. High utilization can increase queueing and lead time when variability exists. Local output can worsen end-to-end flow if downstream acceptance is constrained.

Separate:

- `operating capacity`: repeatable service under defined normal conditions;
- `surge capacity`: time-bounded extra service with explicit cost and degradation;
- `contingency capacity`: protected response to defined failures or obligations;
- `recovery capacity`: ability to clear backlog and restore service after disruption.

Base reserve on variability, service consequence, dependency concentration, replenishment or hiring lead time, failure recovery, customer protection, and employee health. Return sensitivity ranges and triggers rather than a universal utilization target. Never assume 100 percent utilization is efficient or safe.
