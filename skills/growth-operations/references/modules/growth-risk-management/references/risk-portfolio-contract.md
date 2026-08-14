# Growth Risk Portfolio Contract

## Freeze Identity And Use

| Field | Required record |
| --- | --- |
| Identity | Portfolio ID, immutable version, mode, state, title, prior version, canonical fields, and non-goals |
| Decision use | Exact decision, audience, owner, earliest useful date, materiality, intended and prohibited uses |
| Scope | Products, business models, customers, participant roles, markets, channels, initiatives, systems, vendors, teams, resources, and exclusions |
| Time | Evidence period, cutoff, horizon, maturity, effective period, review, trigger, expiry, close, and supersession |
| Accountability | Portfolio, risk, control, decision, evidence, acceptance, execution, verification, stop, escalation, and residual-obligation owners |
| Lineage | Strategy, metric, target, forecast, experiment, budget, initiative, system, contract, policy, incident, and prior-risk versions |
| Governance | Source, access, privacy, market, specialist, approval, authorization, communication, and external-action boundaries |

One portfolio can contain many risks but must share a coherent decision use, scope, cutoff, governance boundary, and aggregation basis. Split incompatible legal entities, markets, evidence cutoffs, objectives, risk authorities, or decision horizons; link them with dependencies.

## Keep States Separate

| State | Meaning |
| --- | --- |
| Concern or reported signal | Attributable statement without sufficient independent support |
| Uncertainty | Material information or future state is not known |
| Assumption | Explicit proposition used despite incomplete evidence |
| Dependency | Required person, artifact, resource, system, provider, or condition |
| Vulnerability | Susceptibility that may enable an adverse event |
| Risk | Uncertain event or condition that could affect an objective or population |
| Event | Occurrence that may or may not create harm or breach |
| Issue | Current condition requiring a decision or correction |
| Incident | Governed event meeting a supplied response definition |
| Loss or harm | Observed adverse customer, business, financial, operational, or trust result |
| Outcome | Mature observed result, with causality separately bounded |

Record transition source, owner, date, definition, evidence, affected population, and version. A missed target is not automatically a risk event, incident, loss, or cause.

## Apply The Readiness Gate

| Portfolio field or transition | Minimum attributable basis |
| --- | --- |
| Assessed risk or rating | Complete risk statement, bounded population and horizon, compatible evidence, method, uncertainty, source, owner, and version |
| Appetite, tolerance, limit, or trigger | Objective, risk class, metric contract, baseline, current exposure, authority, rationale, period, breach response, review, and expiry |
| Owner, assignment, or deadline | Exact accountability, authority, explicit acceptance, capacity, scope, dependency, calendar basis, and effective period |
| Current control or effectiveness | Risk and population, approved design, implementation evidence, observed operation, coverage, test method, exceptions, failures, verifier, and period |
| Treatment plan or expected effect | Supported mechanism, affected exposure, alternatives, capacity, cost, dependencies, approver, owner acceptance, verification, and lifecycle |
| Residual-risk acceptance | Exact residual exposure and version, alternatives, controls, evidence, authority, conditions, monitoring, effective period, and expiry |
| Closure or propagation | Accountable closure or consumer evidence, exact version and scope, retained obligations, acknowledgement, independent verification, date, and reopen rule |

If the minimum basis is absent, keep the field `unavailable`. Put user-specified values in a separate request ledger without calculating dates, creating 30/60/90 plans, proposing assignments, or promoting candidate controls and treatments into portfolio commitments. Urgency, seniority, completeness, a favorable label, and a user-requested value do not satisfy this gate.

## Form A Complete Risk Statement

Use:

```text
Because [cause, dependency, or condition],
[uncertain event] may affect [objective, customer, or operation]
for [population, product, market, and horizon],
leading to [bounded consequence], subject to [evidence and uncertainty].
```

Record risk ID and version, objective, source, cause and mechanism, uncertain event, consequence, affected population, scope, horizon, evidence and counterevidence, assumptions, dependencies, current controls, inherent and residual exposure states, owner, decision required, treatment, indicators, review, expiry, and related risks. Do not use a category label as the statement.

## Use A Discovery Taxonomy

Review as applicable:

- customer value, harm, trust, accessibility, fairness, support, and reputation;
- strategy, market, competition, concentration, policy, and external change;
- product, activation, retention, monetization, expansion, and lifecycle;
- acquisition, channel, partner, platform, content, creative, and brand;
- pricing, incentives, refunds, fraud, economics, cash, and working capital;
- data, identity, metrics, attribution, experiments, forecasts, models, and automation;
- privacy, security, access, reliability, resilience, vendors, and contracts;
- operations, capacity, dependencies, maintenance, people, incentives, and key-person exposure.

Taxonomy is a prompt for discovery, not evidence that a risk exists or has a particular severity.

## Preserve Evidence And Metrics

Use only `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Record source ID, owner or author, date, version, scope, population, market, period, method, definition, maturity, access, evidence state, claim supported, contradiction, limitation, correction, and next evidence.

For every indicator record entity, eligible population, numerator, denominator, formula, unit, window, time zone, maturity, source, owner, version, baseline, current value, expected range if supplied, missing-state treatment, trigger, and review. Keep missing, late, immature, censored, suppressed, unavailable, and valid zero distinct.

## Separate Appetite Terms

| Term | Meaning |
| --- | --- |
| Capacity | Maximum exposure the organization can absorb before viability or hard obligations fail |
| Appetite | Attributable amount and type of exposure an accountable authority is willing to pursue or retain for an objective |
| Tolerance | Bounded acceptable variation around an objective or appetite for a defined period |
| Limit | Operating boundary requiring a defined response when reached or breached |
| Guardrail | Customer, quality, economic, trust, or system condition that constrains a decision |
| Trigger | Evidence condition that starts review, escalation, containment, or another action request |
| Stop rule | Predefined condition requiring exposure to pause or stop under named authority |
| Target | Desired outcome; not a risk boundary unless separately governed as one |

For each boundary record risk class, objective, population, product, market, metric and version, unit, baseline, current exposure, source, authority, rationale, hard or soft status, exception process, breach state, response, effective period, review, and expiry. Leave unavailable boundaries unavailable. Do not backsolve them from current exposure.

## Assign Distinct Owners

Separate portfolio owner, risk owner, source owner, metric owner, control owner, treatment owner, decision owner, specialist reviewer, acceptance authority, executor, independent verifier, stop authority, escalation recipient, and residual-obligation owner. Attendance, consultation, seniority, or silence does not assign any role.

## Version Canonical Fields

Preserve every source register and authority. Reconcile conflicts by exact field, decision class, scope, population, period, definition, source, owner, and authority. Use one stable portfolio ID and immutable versions; record amendment, correction, effective date, consumer acknowledgement, exception, divergence, supersession, archive, and reopen rules. Do not let consumers select the lowest rating or silently overwrite a conflict.
