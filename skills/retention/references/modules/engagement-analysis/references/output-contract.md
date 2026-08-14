# Engagement Analysis Output Contract

## Delivery Order

Return these sections in order:

1. **Mode and boundary:** decision, owner, product, customer job, entity, market, window, cutoff, version, and external-action limit.
2. **Verdict:** exactly one of `decision-ready`, `descriptive-only`, `partially specified`, or `not decision-useful`, plus the limiting gate.
3. **Engagement contract:** eligibility, zero state, value event, quality, natural opportunity, dimensions, identity, time, source, and privacy.
4. **Evidence and reconciliation:** source ledger, evidence states, freshness, maturity, contradictions, missing fields, and population equation.
5. **Canonical distribution or specification:** counts, shares, bucket boundaries, supported bounds, and active-only secondary view where useful.
6. **Dimension views:** frequency, depth, breadth, quality, concentration, burden, and guardrails only where supported.
7. **Comparisons:** compatible periods, segments, cohorts, products, versions, roles, workflows, or marketplace sides with canonical totals.
8. **Interpretation:** findings, supporting and contradictory evidence, alternatives, uncertainty, causal status, and downstream-value boundary.
9. **Next evidence and handoffs:** exact artifact, input, owner, decision use, dependency, guardrail, authority state, and date where supplied.
10. **Sources, external actions, and completion:** pinned conceptual sources, approval-ready actions, actions not performed, and unresolved evidence.

## Canonical Tables

### Contract

| Field | Definition | Evidence state | Source or limitation |
| --- | --- | --- | --- |
| Decision and owner | Decision this analysis supports |  |  |
| Entity and eligibility | Primary unit, denominator, exclusions, zero state |  |  |
| Value event and quality | Qualifying success and failure or reversal |  |  |
| Opportunity and time | Natural cadence, window, cutoff, timezone, maturity |  |  |
| Identity and source | Deduplication, joins, versions, freshness, latency |  |  |
| Privacy and action boundary | Minimum data and prohibited actions |  |  |

Do not fill unavailable fields with invented values. Omit an empty template only when the same fields are present in an equally explicit readable structure.

### Distribution

| Frequency or opportunity bucket | Eligible N | Share of eligible | Value or quality boundary | Maturity | Evidence |
| --- | ---: | ---: | --- | --- | --- |

Include the zero bucket and reconcile counts to the eligible population. Add bounds when aggregate ranges prevent exact statistics. Keep user, account, workspace, product, marketplace side, revenue, and cost in separate views.

### Findings And Handoffs

| Finding or unresolved question | Evidence and alternatives | Decision implication | Owner or route | Guardrail and authority |
| --- | --- | --- | --- | --- |

Do not assign an owner who has not accepted responsibility. Use an owner role or mark ownership unavailable. Routing does not imply acknowledgement, execution, completion, adoption, or impact.

## Verdict Rules

- `decision-ready`: the declared decision can use the supplied mature and reconciled distribution under explicit limitations.
- `descriptive-only`: the distribution is reproducible, but its mechanism, prediction, downstream value, or intervention effect is not established.
- `partially specified`: useful inputs exist, but a material contract or compatibility field prevents a complete analysis.
- `not decision-useful`: the supplied metric or requested score cannot represent the declared customer value or decision.

Do not average verdicts or create a numeric confidence, health, maturity, or engagement score.

## External Actions

For every requested external action record the exact object, version, eligible population, owner, authority, access, approval, dependency, privacy and security controls, monitoring, stop, rollback, and independent verification required. Mark it `not performed` unless separately authorized and executed by a capable path.

## Completion Record

State what the analysis completed, what evidence remains unavailable, what was routed, and which actions did not occur. Never claim data access, calculation, event change, customer ranking, message delivery, product change, experiment launch, publication, adoption, engagement improvement, retention, PMF, revenue, or causal impact without attributable mature evidence.
