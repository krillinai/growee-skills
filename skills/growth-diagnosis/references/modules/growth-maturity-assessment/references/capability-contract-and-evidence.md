# Capability Contract And Evidence

## Assessment Contract

Freeze these fields before evaluating any capability:

| Group | Required fields |
| --- | --- |
| Decision | decision, consumer, accountable owner, permitted action, consequence, horizon, review cadence |
| Assessed unit | company, business unit, product, market, segment, team, workflow, version, period |
| Customer | customer entity, role, problem, value state, eligibility, exclusion, protection |
| Context | product, business model, stage, market, language, locale, currency, timezone, legal entity |
| Growth need | current constraint, recurring decision, frequency, customer outcome, business outcome, guardrails |
| Capability | service, inputs, outputs, interfaces, owner, operator, dependencies, controls, acceptance |
| Boundary | included domains, exclusions, external actions, specialist review, expiry, residual obligations |

Do not call a whole company mature when the evidence applies to one product, market, team, workflow, or period.

## Evidence States

Use these labels exactly:

- `verified`: directly supported by an attributable, inspectable, compatible artifact;
- `inferred`: reasoned from named evidence with the inference and uncertainty explicit;
- `unavailable`: required but not supplied, observable, current, or compatible;
- `not applicable`: outside the declared capability and decision;
- `reported signal`: attributable statement without inspectable support; leave evidence state blank.

Confidence is not an evidence state. Missing evidence is not zero performance. Public information can verify public artifacts and claims, but not private operation, adoption, reliability, incidents, cost, controls, or outcomes.

## Evidence Manifest

Record every artifact separately:

| Field | Purpose |
| --- | --- |
| Artifact ID and type | Distinguish actual, plan, roadmap, policy, survey, benchmark, vendor claim, case, experiment result, or reported signal |
| Owner and source | Preserve accountability and access path |
| As-of and period | Separate current state from historical or future intent |
| Entity and scope | Preserve product, market, segment, team, workflow, and population boundaries |
| Definition and version | Prevent same-name/different-meaning aggregation |
| Evidence state | Show support without converting uncertainty to a score |
| Compatibility | Record whether entity, definition, period, and maturity permit comparison |
| Limitation and contradiction | Preserve exclusions, disagreement, negative evidence, and counterclaims |
| Decision use and expiry | Show which finding it can change and when it must be refreshed |

Never combine a strategy deck, live dashboard, old survey, vendor claim, cross-product experiment, customer metric, and future roadmap into one current view without compatibility evidence.

## Minimum Evidence By State

| State | Minimum inspectable evidence |
| --- | --- |
| Need | repeated decision inventory, consumers, consequence, customer-value link, current workaround |
| Defined | versioned contract, semantics, owner, interfaces, controls, acceptance criteria |
| Approved or provisioned | approval, access, resource, license, integration, and readiness states kept separate |
| Implemented | working artifact or service in the declared environment and scope |
| Operated | case records, quality, cycle time, failure, exception, maintenance, support, and cost |
| Adopted | eligible denominator, repeat use, non-use, abandonment, queue, bypass, and workaround |
| Reliable | service levels, incidents, degradation, fallback, recovery, and reconciliation |
| Decision-integrated | attributable decisions, options, reason codes, rejection, reversal, escalation, and stop |
| Outcome-verified | customer and economic outcomes with maturity, guardrails, attribution, and causal limits |
| Learning | reusable records, corrections, transfer boundaries, expiry, review, and retirement |

Documents, policies, training, licenses, named owners, and configured tools can support early states only. They cannot prove operation, adoption, reliability, decision use, or results.

## Evidence Collection

Prefer aggregate, redacted, pseudonymous, or small-cell-suppressed evidence:

- decision inventories and redacted decision records;
- capability and service catalogs, interfaces, owners, versions, and dependency maps;
- aggregate usage, non-use, queue, cycle-time, workaround, support, and cost measures;
- quality, incident, exception, recovery, maintenance, and change records;
- compatible customer, lifecycle, economic, experiment, and guardrail summaries;
- access, audit, override, stop, rollback, retention, deletion, and review evidence.

Request evidence only if it can change a finding, dependency, priority, or handoff. Do not collect employee names, private messages, keystrokes, health or disability data, protected traits, immigration status, precise location, payment credentials, access tokens, or unrelated complete histories. Never score named people or use a capability assessment for compensation, leave, workload, or employment decisions.

## Self-Assessment And Interviews

Treat ratings as reported signals. Record respondent role, question, construct, instrument, sample, response, time, access to evidence, uncertainty, and limitation. Preserve disagreement rather than averaging it away.

Triangulate owners with capability consumers, frontline operators, non-users, affected customers, artifacts, logs, incidents, exceptions, failed work, decision records, and outcomes. A strong opinion can identify a question; it cannot answer it by itself.
