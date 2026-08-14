# Evidence Gates And Replanning

## Distinguish Work Types

| Work type | Primary purpose | Required boundary |
| --- | --- | --- |
| Research | Reduce a decision-relevant unknown | Question, sample or source, limits, owner, and decision |
| Evidence repair | Make a metric or source usable | Definition, quality rule, reconciliation, owner, and verification |
| Experiment | Estimate a causal effect under valid assignment or a stated alternative design | Hypothesis, eligibility, assignment, sample, maturity, guardrails, and readout |
| Pilot | Test value and operating readiness in a bounded real context | Population, scope, capacity, support, evidence, cap, and rollback |
| Staged rollout | Expand exposure through governed steps | Entry and exit gates, monitoring, support, stop, and rollback |
| Full rollout | Operate at intended scope after required evidence and authorization | Readiness, ownership, capacity, customer protection, and residual monitoring |
| System work | Build or change a shared capability | Consumers, reliability, adoption, migration, maintenance, and retirement |
| Maintenance | Preserve value, safety, quality, or continuity | Service state, owner, capacity, evidence, and escalation |

Do not relabel a rollout as an experiment to avoid evidence, exposure, approval, support, or rollback requirements.

## Define A Verifiable Gate

For each evidence or operating gate record:

| Field | Requirement |
| --- | --- |
| Decision | Continue, revise, cap, pause, stop, rollback, escalate, route, or authorize a separately controlled action |
| Scope | Eligible unit, product, market, segment, exposure, and exclusions |
| Required state | Artifact, operating capability, customer state, metric, or evidence |
| Metric contract | Entity, eligibility, numerator, denominator, event or state, identity, segment, window, cohort, maturity, source, and owner |
| Evidence rule | Threshold or bounded state, uncertainty, data quality, comparison, and contradictory evidence |
| Guardrails | Customer, quality, trust, economics, capacity, privacy, security, fairness, reliability, and compliance conditions |
| Timing | Earliest valid maturity, due date, expiry, review date, and lag |
| Accountability | Evidence owner, decision owner, required approver, and completion proof |

Dates organize review but do not establish passage. A gate is incomplete when evidence is immature, unavailable, incompatible, contradicted, or missing required controls.

## Predeclare Outcomes And Responses

Where evidence is tested, define:

- `positive`: evidence supports the bounded continuation decision and guardrails hold;
- `negative`: evidence does not support the mechanism or expected value;
- `harmful`: a noncompensable guardrail or customer protection is breached;
- `inconclusive`: validity, power, maturity, quality, interference, or mixed evidence prevents the decision.

Map each to a response. Do not automatically continue from one positive metric, average harm into upside, ignore negative or inconclusive evidence, or reuse a causal estimate outside its tested unit without transfer evidence.

## Govern Commitments

For each commitment record owner, artifact or outcome, acceptance criteria, dependency, due or maturity date, evidence, completion proof, state, permission boundary, escalation, expiry, and superseding commitment. Use `proposed`, `ready`, `active`, `blocked`, `paused`, `complete`, `cancelled`, or `expired` consistently with the plan.

Evidence of completion must be attributable:

- versioned artifact and acceptance evidence;
- verified operating state and eligible exposure;
- mature metric or customer outcome under its contract;
- reconciled business outcome under a compatible accounting basis;
- decision record with owner, rationale, conditions, and expiry.

`On track`, green status, percent complete, meetings, utilization, ticket closure, deployment, or campaign launch are not sufficient by themselves.

## Separate Completion Layers

Keep these distinct:

1. `plan complete`: required planning records and decisions exist;
2. `workstream complete`: accepted artifact or operating state is verified;
3. `implementation verified`: authorized change reached the intended eligible scope;
4. `customer outcome mature`: value metric reached its declared maturity;
5. `business outcome mature`: economics or business state reconciled at the required period;
6. `causal impact supported`: a valid design supports an effect estimate in the tested boundary.

An initiative may complete its work while impact remains unavailable or negative. Preserve that result.

## Maintain Risk And Assumption Registers

For each assumption record statement, type, evidence state, source, owner, consequence if false, earliest signal, decision affected, test or observation, maturity, expiry, and response. For each risk record cause, event, consequence, customer and business exposure, likelihood evidence or `unavailable`, severity basis, detectability, owner, prevention, monitoring, cap, stop, rollback, escalation, residual obligation, and review.

Do not multiply invented likelihood and impact scores into false precision. Prioritize with bounded evidence, irreversibility, customer harm, concentration, dependency, and decision urgency.

## Control Changes And Replanning

Preserve the prior plan and create a new version when a material change affects outcome, scope, non-goals, customer, market, mechanism, metric, baseline, target, evidence, dependency, critical path, capacity, budget, milestone, guardrail, owner, authority, risk, date, or commitment.

For each change record:

| Field | Requirement |
| --- | --- |
| Trigger | New evidence, miss, dependency failure, capacity change, guardrail breach, scope request, external event, or source-decision revision |
| Prior state | Version, assumption, commitment, date, evidence, decision, and owner at the time |
| New state | Updated evidence and proposed contract without backdating |
| Effect | Outcome, scope, sequence, critical path, capacity, cost, risk, customer, and downstream handoffs |
| Decision | Revise, reduce, resequence, defer, pause, stop, cancel, escalate, or preserve |
| Governance | Owner, approver, effective date, expiry, communication boundary, and next review |

Do not silently change a baseline, target, denominator, scope, date, or definition. Do not mark a missed commitment as always known. Do not preserve the original date by removing evidence or customer-protection work.

## Audit The Plan

Audit lineage, unit coherence, evidence state, outcome chain, duplicate value, scope, readiness, workstreams, dependencies, critical path, capacity, maintenance, gates, commitments, risks, changes, privacy, market transfer, and external actions. Classify findings by the decision they block or change, not by cosmetic severity.

Expire stale commitments and gates. Route unresolved specialist work. A clean task tracker cannot compensate for an incoherent outcome, invalid evidence, impossible sequence, unavailable capacity, or missing authority.
