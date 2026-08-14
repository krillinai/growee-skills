# Segment Contract

## Minimum Context

Capture independently:

- decision, owner, product, market, route to market, time horizon, decision date, and review date;
- market, account or household, user, role, job, use case, transaction, lifecycle state, cohort, and model units;
- need, trigger, urgency, current alternative, value mechanism, readiness, prerequisites, and failure conditions;
- buyer, payer, champion, user, admin, approver, blocker, supplier, beneficiary, and renewal relationships;
- segment eligibility, identification timing, observable rule, exclusions, unknowns, overlap, precedence, and fallback;
- path, offer, product, service, channel, sales, price, or support decision changed by the group;
- sources, populations, definitions, windows, maturity, counts, missingness, selection, counterevidence, and limitations;
- activation, retention, renewal, expansion, contribution, acquisition, service, failure, trust, and guardrail definitions;
- sensitive attributes and proxies, purpose, necessity, permission, retention, access, fairness, appeal, and incident controls;
- owner, version, effective date, change log, validation status, drift threshold, and retirement rule.

## Segment Specification

For each operating segment state its name, purpose, decision, unit, job, alternative, eligibility, identification rule, value mechanism, required conditions, role structure, route, economic assumptions, exclusions, edge cases, unknown rule, overlap rule, action, evidence, counterevidence, owner, version, and review date.

## ICP Contract

State the product and period, then record:

1. need: important job, trigger, urgency, and alternative;
2. fit: conditions required to receive differentiated value;
3. behavior: observable first and repeated value;
4. economics: acquisition, service, retention, contribution, and expansion conditions;
5. access: identifiable and reachable population under permitted routes;
6. readiness: authority, data, workflow, collaborators, urgency, and capacity;
7. exclusion: lookalike customers who fail, churn, remain unprofitable, or require exceptional service.

## Evidence And Privacy

Prefer aggregate or pseudonymous evidence. Do not reproduce direct identifiers or sensitive attributes in the deliverable. Missing private data produces `unavailable` fields and an evidence plan, not fabricated segment scores.
