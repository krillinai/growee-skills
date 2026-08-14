# Aggregation, Scenarios, And Controls

## Map Interaction Before Aggregation

Create a dependency graph across customers, products, channels, platforms, identities, data, models, metrics, experiments, vendors, contracts, markets, currencies, cash, capacity, people, controls, and time.

| Relationship | Question |
| --- | --- |
| Common cause | Can one upstream condition create several recorded risks or losses? |
| Correlated | Can exposures move together because they share context or drivers? |
| Cascading | Can one event cross products, systems, markets, or customer roles? |
| Reinforcing | Can two mechanisms amplify frequency, consequence, or duration? |
| Offsetting | Does one supplied exposure genuinely reduce another without creating hidden harm? |
| Competing | Do treatments consume the same cash, traffic, capacity, attention, or control? |
| Duplicate | Are several records counting the same cause, event, control, population, or loss? |

Preserve every item record while creating a portfolio relationship view. Do not assume independence, correlation, diversification, or offset without evidence.

## Measure Concentration With Denominators

Define the exposure unit and total before reporting concentration. Use supplied compatible bases such as customer value, revenue or contribution, cash, users, traffic, transactions, data, models, channels, vendors, platforms, products, markets, people, capacity, controls, or recovery resources.

Record numerator, denominator, period, maturity, source, version, exclusions, unknown share, and stress condition. Do not mix counts with value, gross with net, contracted with available, or point-in-time with flow exposures. Preserve unknown and unmeasured concentration.

## Avoid Duplicate And False Aggregation

Keep risk count, exposure, expected loss, observed loss, control coverage, issue count, incident count, and customer or business outcome separate. Add only compatible quantitative values with shared units, populations, horizons, definitions, and dependence treatment.

Do not:

- add ordinal heatmap numbers as money or probability;
- count one shared dependency or realized loss in every child risk;
- subtract opportunity from customer harm;
- call many initiatives diversification;
- net hard constraints against upside;
- use average exposure to hide tail, local, or concentrated harm.

## Build Bounded Scenarios And Stress Tests

Use scenarios to explore mechanisms and decision thresholds, not to invent forecasts. Record scenario ID, decision, scope, horizon, changed assumptions, fixed assumptions, shared dependencies, customer and operational effects, capacity, cash, controls, recovery, indicators, stop conditions, evidence, uncertainty, and owner.

Include current-state, plausible adverse, severe-but-decision-relevant, control-failure, dependency-loss, concentration, delayed-effect, recovery, and combined scenarios as applicable. Do not assign probability without a supported method. Show formulas, units, substituted values, ranges, sensitivity, and limitations.

Stress tests are not proof that an event will occur or that recovery works. Record which assumptions, limits, controls, or resources fail first and what decision changes.

## Separate Control States

```text
control objective
-> approved design
-> implemented control
-> observed operation
-> tested effectiveness
-> risk and customer outcome
```

Never infer a later state from an earlier one.

| Control field | Required record |
| --- | --- |
| Purpose | Risk, mechanism, population, objective, and failure mode addressed |
| Design | Preventive, detective, corrective, recovery, directive, or compensating mechanism |
| Ownership | Design owner, approver, operator, tester, verifier, stop authority, and escalation |
| Operation | System, scope, eligibility, frequency, threshold, response window, access, and evidence |
| Coverage | Eligible, protected, unprotected, excluded, failed, overridden, unavailable, and untested populations |
| Quality | Timeliness, false positives, false negatives, exceptions, failures, drift, gaming, and burden |
| Lifecycle | Test, remediation, fallback, stop, rollback, correction, retest, review, expiry, and decommissioning |

A policy, meeting, task, dashboard, alert, vendor claim, or purchased tool proves only its attributable content. It does not prove implementation or effectiveness.

## Evaluate Design And Operating Effectiveness

Design adequacy asks whether the mechanism could address the risk for the defined population under stated assumptions. Operating effectiveness asks whether supplied evidence shows it operated as designed for the required period, coverage, frequency, and exceptions. Outcome evidence asks what happened afterward without exceeding causal support.

Record current inherent exposure, control contribution, residual exposure, uncertainty, counterevidence, and remaining gaps separately. Do not report percentage reduction unless compatible evidence and a defensible method support it.

## Design Monitoring

Separate:

- leading condition and mechanism signals;
- exposure and concentration measures;
- control operation and coverage indicators;
- limit and guardrail breaches;
- near misses and weak signals;
- incidents, losses, customer harm, and lagging outcomes;
- missing coverage, blind spots, and unavailable evidence.

For every indicator define metric contract, owner, population, baseline, threshold or unavailable threshold, maturity, frequency, latency, response window, materiality, alert route, tiered escalation, suppression, duplicate handling, false-positive and false-negative review, stop, correction, retention, audit, and expiry.

No alert does not mean no exposure. A green status does not certify safety. Control alert fatigue, alert flooding, gaming, stale acknowledgements, and automatic closure. Require independent closure proof.

## Govern Events And Refreshes

Maintain an immutable event timeline with source, time, detection, population, systems, customers, evidence, incident-definition status, controls expected and observed, containment evidence, loss and outcome maturity, causal status, correction, and portfolio effects.

In a refresh, bridge old to new sources, definitions, metrics, assumptions, risks, controls, exposure, decisions, and acceptance. Preserve failed controls, overrides, dissent, contradictions, and what was knowable. Route active response to accountable operations and retrospective analysis to `growth-operations`; do not claim containment, recovery, resolution, prevention, or reduced risk.
