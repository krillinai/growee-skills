# Initiative Contract

## Establish Decision Lineage

A plan must descend from a named decision, not a vague ambition. Record:

| Field | Requirement |
| --- | --- |
| Initiative | Stable ID, version, title, mode, state, plan date, evidence cutoff, horizon, review, and expiry |
| Source decision | Decision ID and version, owner, rationale, selected option, rejected alternatives, conditions, evidence, approval state, and effective period |
| Authority | Outcome owner, workstream owners, required approver, budget owner, decision rights, escalation path, and external-action boundary |
| Unit | Customer and participant roles, product, business model, market, locale, motion, channel, and economic unit |
| Outcome | Baseline, desired customer and business state, metric contract, maturity, horizon, guardrails, and evidence state |
| Scope | Included work, non-goals, exclusions, deferred work, constraints, dependencies, and evidence that can reopen scope |

If strategy, diagnosis, target, opportunity, or investment evidence is missing, preserve the gap and create a prerequisite gate. Do not manufacture a source decision or mark the plan ready.

## Separate Decision And Execution States

Keep these distinct:

```text
reported signal -> evidence -> recommendation -> decision -> approval -> authorization -> action -> verification -> mature outcome -> causal result
```

A target is desired performance, not a forecast or baseline. An opportunity is a bounded decision range, not committed impact. An approved investment is not authorization for every downstream mutation. A plan is not implementation. A closed task is not customer value.

Use `verified`, `inferred`, `unavailable`, or `not applicable` for claims. Preserve reported statements as reported signals rather than upgrading them to verified evidence.

## Bound The Initiative Unit

Define one coherent combination of:

- customer, user, buyer, seller, account, beneficiary, approver, and payer roles;
- problem, buying situation, first value, repeated or protected value, and retained outcome;
- product, offer, market, locale, motion, route, price model, and economic unit;
- baseline, metric definition, maturity, source, owner, and decision horizon.

Split initiatives when materially different units need independent outcomes, owners, decisions, dependencies, evidence, economics, or approval. A shared platform or team creates a coordinated dependency, not permission to average the units.

## Build The Outcome And Mechanism Contract

Trace only supported transitions:

| Layer | Question | Evidence requirement |
| --- | --- | --- |
| Input | What scarce capacity, budget, data, or asset is committed? | Availability, owner, period, approval state, and opportunity cost |
| Activity | What work is performed? | Workstream, owner, dependency, and completion proof |
| Output | What artifact or operating capability exists? | Versioned artifact or verified operating state |
| Exposure | Which eligible unit can encounter the change? | Eligibility, assignment or access, date, and population |
| Customer outcome | What first, repeated, retained, expanded, restored, or protected value changes? | Metric contract, baseline, maturity, evidence, and guardrails |
| Business outcome | What sustainable contribution, cash, capacity, quality, trust, or strategic option changes? | Compatible economics, period, maturity, and accounting basis |

Label relationships `arithmetic`, `hypothesized`, `associated`, `causal`, or `tradeoff`. Do not describe a hypothesis as a guaranteed mechanism. Preserve alternatives and contradictory evidence.

## Prevent Duplicate Outcomes

Define eligible, exposed, acquired, activated, retained, monetized, referred, expanded, resurrected, protected, and churned states only where applicable. Record identity and deduplication rules, overlap, interaction, residual, and reconciliation.

Assign one accountable owner to the initiative outcome and distinct owners to workstream artifacts. Contribution ownership does not create separate copies of the same customers, revenue, or impact. Keep attribution, contribution, forecast, opportunity, and causal estimates separate.

## Determine Plan Readiness

Use these plan states:

| State | Meaning |
| --- | --- |
| `proposed` | Contract or feasibility is incomplete; no execution claim |
| `ready` | Required decisions, capacity, prerequisites, gates, controls, owners, and authorization path are explicit |
| `active` | Separately authorized work has begun; evidence must be supplied |
| `blocked` | A named dependency, evidence gap, capacity constraint, risk, or approval prevents progress |
| `paused` | An accountable decision temporarily stops work while preserving obligations |
| `complete` | Plan obligations have attributable completion proof; impact remains separately assessed |
| `cancelled` | An accountable decision ends the initiative and assigns residual obligations |
| `expired` | A decision, gate, evidence window, or commitment lapsed without valid renewal |

Never infer `ready`, `active`, or `complete` from a date, task list, budget mention, meeting, dashboard, or self-report.
