# Funnel Diagnosis And Design

## Separate Three Layers

Keep these layers visibly distinct:

| Layer | Question | Evidence |
| --- | --- | --- |
| Observation | Where, for whom, and when did measured movement change? | Reconciled counts, rates, time, maturity, segments, and guardrails |
| Mechanism | What could explain the observed pattern? | Process, customer, operational, technical, market, and comparative evidence |
| Intervention | What change should test or address the mechanism? | Explicit hypothesis, owner, exposure, outcome, guardrails, and decision rule |

A low transition rate is an observation. Friction, weak intent, missing value, limited capacity, distrust, price, or measurement error are mechanisms. A shorter form, assisted setup, different qualification, or product change is an intervention.

## Constraint Taxonomy

| Constraint | Typical signal | Discriminating evidence |
| --- | --- | --- |
| Demand | Too few qualified units enter | Reach, intent, addressable demand, channel incrementality |
| Promise and qualification | Entry is high but downstream quality is weak | Source, message, job, ICP, retained and economic quality |
| Product value | Steps complete without meaningful first or recurring value | Value events, task outcomes, alternatives, customer evidence |
| Friction | Qualified units fail at a preventable transition | Errors, time, abandonment, usability, permissions, support |
| Capacity | Demand exceeds people, inventory, supply, or systems | Queue time, availability, utilization, fulfillment, service levels |
| Trust and risk | Uncertainty or consequences delay movement | Objections, consent, security, policy, reversals, complaints |
| Retention | Entry outpaces recurring value | Mature cohorts, churn, resurrection, natural frequency |
| Economics | Conversion cannot be sustained profitably | Marginal CAC, margin, payback, service cost, incentive dependence |
| Learning | The team cannot distinguish causes | Instrumentation, definition drift, ownership, cycle time |

Preserve credible alternatives. The smallest rate is not automatically the primary constraint, and a large absolute loss is not automatically removable.

## Rank A Primary Constraint

For the current decision horizon, compare candidates on:

- absolute downstream movement if the mechanism is changed;
- retained customer and business value;
- evidence strength and unresolved alternatives;
- team control, implementation time, and operational capacity;
- cost, margin, trust, privacy, fairness, accessibility, compliance, and reversibility;
- speed and value of learning.

Record one primary constraint only when it plausibly limits the final outcome and the evidence distinguishes it. Otherwise return a ranked constraint ledger and the cheapest decisive evidence step.

## Preserve Useful Gates

Do not remove steps solely to raise local conversion. Qualification, identity, consent, safety, fraud, security, compliance, payment, or implementation gates may protect downstream value. Evaluate whether the gate is necessary, correctly placed, clearly explained, reliable, and proportionate.

Read local movement together with downstream activation, retention, revenue, margin, support burden, complaints, errors, trust, and risk. A high step rate can pass low-quality units downstream; a low rate can be healthy qualification.

## Design An Intervention

Specify:

- supported mechanism and counterhypothesis;
- eligible entity, entry state, and target transition;
- proposed change and unchanged control or comparison;
- expected local and downstream effects;
- instrumentation and data-quality checks;
- observation and maturation windows;
- retained-value, economic, quality, trust, risk, and capacity guardrails;
- owner, dependencies, approval, rollback, and review date;
- ship, iterate, stop, or gather-more-evidence rule.

Do not claim launch readiness when instrumentation, operational capacity, legal or policy review, consent, or ownership is unresolved.

## Routing

- Route first-value definitions, onboarding paths, and retained activation to `activation`.
- Route recurring value, churn, resurrection, and cohort retention to `retention`.
- Route offers, plans, pricing, payment, retained revenue, contribution, and unit economics to `monetization`.
- Route causal tests and alternative evaluation designs to `experiment-design`.
- Route system-wide primary constraint selection to `growth-diagnosis`.
- Route interviews, observation, and mechanism research to `customer-research`.

Funnel Analysis retains ownership of the canonical state model, metric definitions, reconciliation, observed transition analysis, and cross-domain handoff ledger.
