# Growth Maturity Assessment Output Contract

## 1. Assessment Header

Return mode, decision, assessed unit, product, customer, value, business model, stage, market, current constraint, recurring decisions, consumers, owner, horizon, review cadence, scope, exclusions, hard constraints, and external-action boundary.

If evidence is absent, label the output `evidence-pending specification`. Never imply that planned review, requested access, or stakeholder confidence establishes current capability.

## 2. Capability Ledger

Use one row per capability and keep domains separate.

| Field | Required content |
| --- | --- |
| Domain and capability | Bounded capability name, not a broad company grade |
| Decision and consumer | Recurring decision served and intended user |
| Required state | Smallest sufficient state for the decision and horizon |
| State evidence | Need, definition, provisioning, implementation, operation, adoption, reliability, decision use, outcome, and learning kept separate |
| Evidence coverage | Verified, inferred, unavailable, not applicable, plus reported signals |
| Finding | Sufficient, conditional, insufficient, blocked, not assessable, or not applicable |
| Limitation | Contradiction, incompatible artifact, non-use, failure, incident, hard constraint, or causal limit |
| Dependency | Prerequisite, consumer, propagation risk, and evidence gate |
| Disposition | Maintain, improve, standardize, keep local, pilot, compose, consolidate, retire, defer, route, or not applicable |
| Review | Owner, expiry, trigger, residual obligation, and specialist handoff |

Do not add a composite score, universal stage, people ranking, invented weight, or unsupported benchmark.

## 3. Evidence Manifest And Compatibility

List artifact ID, type, owner, source, as-of, period, entity, product, market, definition, version, evidence state, compatibility, limitation, contradiction, decision use, and expiry. Keep actuals, plans, roadmaps, surveys, vendor claims, benchmarks, cases, and reported signals distinct.

Show evidence coverage separately from capability condition. Identify findings blocked by stale, incompatible, partial, contradictory, or unavailable evidence.

## 4. State And Operating Evidence

For every in-scope capability, show:

- eligible and actual consumers, repeat use, non-use, abandonment, queues, bypasses, and workarounds;
- quality, service level, cycle time, failure, incident, exception, recovery, support, maintenance, cost, and burden;
- decisions changed, rejected, reversed, escalated, or stopped with reason codes;
- customer first value, retained value, trust, complaints, opt-outs, accessibility, and protection;
- business economics, external conditions, attribution, uncertainty, durability, and causal limits;
- learning reused, corrected, expired, transferred, or retired.

Never use volume, access, documentation, tool ownership, task completion, automation, or revenue alone as maturity proof.

## 5. Dependency And Governance View

Map foundational dependencies, downstream uses, noncompensable constraints, accountable owners, controls, exceptions, incidents, residual exposure, acceptance authority, stop conditions, verification, and residual obligations.

For AI or automation, add source and prompt lineage, model and tool version, validation, calibration, drift, human review, authority, reason codes, abstention, override, audit, stop, rollback, incident, recovery, feedback-loop risk, and customer-harm review.

## 6. Priorities And Handoffs

Order only decision-relevant dispositions by customer value, current constraint, dependencies, risk, evidence, capacity, maintenance, management load, cost, adoption, and opportunity cost. State prerequisite and evidence gates.

Separate:

```text
finding -> capability need -> options -> recommendation -> decision
-> approval -> initiative -> action -> verification -> result
```

This Skill may produce local findings, evidence requests, decision briefs, and approval-ready handoffs. It must not invent or execute budget, procurement, staffing, reorganization, architecture, deployment, publication, or impact.

## 7. Completion

End with:

- decision-specific conclusions and explicitly unsupported claims;
- unresolved questions and smallest evidence requests;
- specialist boundaries and named handoffs;
- artifacts created or updated locally;
- external actions requested but not taken;
- expiry, review triggers, residual risks, and residual obligations;
- completion state for assessment work only.

Do not claim adoption, customer value, growth, business improvement, or completion of an external action without inspectable downstream evidence.
