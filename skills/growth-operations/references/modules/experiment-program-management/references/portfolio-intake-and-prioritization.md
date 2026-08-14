# Portfolio Intake And Prioritization

## Require Decision-Centered Intake

| Field | Required decision evidence |
| --- | --- |
| Decision | Bounded choice, accountable owner, decision date, alternatives, reversibility, and action states |
| Uncertainty | Important unknown, current belief, evidence and counterevidence, and why new evidence can change the decision |
| Customer | Eligible population, problem, value, potential harm, market, product, and exclusions |
| Mechanism | Intervention or evidence source, expected causal or descriptive path, failure signal, and interference risk |
| Outcomes | OEC or primary outcome, practical threshold, guardrails, maturity, long-term outcome, and proxy boundary |
| Feasibility | Traffic, sensitivity, assignment, exposure, identity, engineering, analysis, review, and operating capacity |
| Governance | Ethics, privacy, security, domain review, approvers, stop, rollback, expiry, and action boundary |
| Follow-through | Possible result states, decisions, owner, implementation dependency, verification, and reopen rule |

A feature, tactic, stakeholder request, solution, idea count, or desired result is not a complete experiment candidate. Return exact missing fields and route detailed design to `growth-measurement`.

Do not rank or schedule an incomplete population. If decision importance, traffic, capacity, maturity, interference, risk, or opportunity cost cannot be compared, preserve separate views and mark ordering unresolved. Do not fill gaps with a score, executive priority, request age, equal quota, universal portfolio ratio, or invented reserve.

## Choose The Evidence Design Family

The program records the design family and why it can inform the decision; `growth-measurement` owns the detailed specification.

| Family | Program gate |
| --- | --- |
| Randomized experiment | Ethical and reversible intervention, controllable assignment and exposure, sufficient sensitivity, mature outcome, and manageable interference |
| Switchback or cluster design | Shared environment or interference requires time or cluster assignment and carryover controls |
| Quasi-experimental design | Assignment mechanism and identifying assumptions are explicit and reviewable |
| Bounded pilot | Operational feasibility or harm must be learned before broad exposure; causal limits remain explicit |
| Offline evaluation or simulation | The decision can be narrowed without customer exposure and model-to-live transfer is bounded |
| Qualitative or descriptive evidence | Mechanism, language, problem, or implementation uncertainty precedes causal testing |
| No experiment | Severe defects, unethical exposure, irreversible action, unavailable sensitivity, or a decision already resolved by stronger evidence |

Do not default to A/B testing or relabel nonrandomized evidence as an experiment.

## Classify The Portfolio

| Class | Purpose | Main protection |
| --- | --- | --- |
| `core optimization` | Improve a validated value path or named current constraint | Prevent local metric wins from degrading retained value |
| `adjacency` | Test transfer to a bounded segment, surface, product, or market | Revalidate transfer assumptions and local capacity |
| `exploration` | Resolve a different mechanism, model, or strategic uncertainty | Keep commitment reversible and learning decision-specific |
| `system quality` | Improve assignment, exposure, metrics, diagnostics, methods, or evidence operations | Do not starve foundations to maximize visible product tests |
| `long-term validation` | Revalidate proxies, delayed value, guardrails, and shipped decisions | Preserve cohorts, holdouts, follow-up, and reopen rules |

Do not impose a universal allocation ratio or relabel routine work as exploration.

## Compare Without False Precision

Compare candidates through separate views:

- importance of the decision and customer consequence;
- strategic relevance and current constraint as supplied;
- uncertainty and current evidence quality;
- whether causal evidence is necessary;
- eligible traffic, minimum sensitivity, and maturity;
- engineering, product, data, analysis, review, and decision capacity;
- dependencies, concurrency, interference, shared surfaces, and opportunity cost;
- reversibility, customer harm, trust, privacy, security, legal or regulatory review, and residual obligations;
- time to decision-changing evidence and next action.

Scoring can organize discussion but cannot create reach, impact, confidence, effort, or comparability. Keep units, evidence states, ranges, and conflicts visible. Executive sponsorship and equal team quotas are governance inputs, not decision value.

Use `accept`, `request evidence`, `route`, `stage`, `queue`, `defer`, `reject`, `reserve capacity`, or `unresolved`. Record rationale, first limiting gate, owner, prerequisites, expiry, and reopen evidence.

## Reconcile Scarce Capacity

Time-phase:

- eligible users, accounts, clusters, networks, markets, surfaces, and holdout inventory;
- engineering, design, product, data, platform, analysis, statistics, domain review, support, and decision-owner attention;
- metric, logging, assignment, exposure, and repository services;
- maintenance, incident response, long-term follow-up, and capacity reserve.

Do not double-book populations, people, systems, or decision attention. Show committed, requested, available, protected, reserved, contingent, and unavailable capacity. Route cross-functional budget changes to `growth-operations`.

## Sequence The Portfolio

Fix ethics, identity, assignment, exposure, metric, and quality foundations before dependent scale. Resolve high-value upstream uncertainties before downstream variants. Sequence colliding interventions and maturity windows. Prefer the smallest reversible design that can change the decision. Preserve system-quality and long-term-validation work even when short-term product tests look more visible.
