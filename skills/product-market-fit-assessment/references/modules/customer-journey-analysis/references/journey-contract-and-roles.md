# Journey Contract And Roles

## Contents

1. Journey contract
2. Evidence and source coverage
3. Participant roles and relationships
4. Identity and account boundaries
5. Current and target versions

## Journey Contract

Create one contract for one decision-coherent journey.

| Field | Minimum contract |
| --- | --- |
| Identity | Journey ID and version, mode, record state, current or target designation, prior version |
| Decision | Decision question, decision owner, intended customer and business outcome, review and expiry |
| Product | Product, service, offer, package, entitlement and relevant version |
| Customer | Customer entity, account boundary, participant roles, job, trigger, alternatives and exclusions |
| Context | Market, legal or operating context, language, locale, channel, device and service model |
| Path | Entry and exit conditions, included paths, start and end states, period, horizon and maturity |
| Evidence | Sources, cutoff, access, methods, coverage, evidence states, contradictions and limitations |
| Measurement | Metric IDs and versions, entities, identity, cohorts, windows, source truth and owners |
| Governance | Journey owner, reviewers, privacy, rights, retention, correction and external-action boundary |

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. An attributable stakeholder or participant statement without inspectable support may remain a `reported signal`; do not label it verified or inferred automatically. `Unavailable` is applicable missing evidence, not zero or failure.

Keep these distinct:

```text
source -> observation or report -> interpretation -> hypothesis
-> recommendation -> decision -> approval -> authorization -> action
-> verification -> customer outcome -> business outcome -> causal estimate
```

An existing journey map is a source artifact, not proof that its personas, sequence, systems, causes, metrics, or target states are current or true.

## Evidence And Source Coverage

Inventory each source with owner, author, date, version, original or derivative status, method, participant or population, product, market, channel, period, exact claim, metric definition, access, rights, evidence state, limitation, contradiction, and journey fields used.

Potential sources include supplied interviews, surveys, reviews, support cases, calls, field notes, product events, web and channel evidence, search or referral evidence, CRM stages, contracts, billing, implementation records, service logs, incident records, experiments, and prior journey maps. Do not imply any source exists or was accessed.

Build a coverage matrix:

| Role / state or transition | Direct observation | Reported experience | Behavioral or operating evidence | Measurement coverage | Contradiction / limitation / missing evidence |
| --- | --- | --- | --- | --- | --- |

Observed instrumentation covers only its defined systems, identities, events, permissions, periods, and populations. It cannot prove the complete journey, internal state, untracked behavior, or causality. Preserve dark, peer, offline, partner, sales, procurement, security, implementation, workaround, and exit paths as unavailable unless attributable evidence supports them.

Record eligible sources, supplied sources, used sources, excluded sources, unavailable sources, and suppressed sources. A small or biased set of interviews, reviews, support tickets, tracked users, or successful customers cannot silently represent the whole population.

## Participant Roles And Relationships

Map roles because different people can discover, evaluate, use, authorize, pay for, support, benefit from, or leave the product.

| Role / entity | Job / trigger / alternatives | Value / burden / risk | Authority / access / permission | States / paths / handoffs | Evidence / exclusion / exit |
| --- | --- | --- | --- | --- | --- |

Consider beneficiary, end user, administrator, creator, collaborator, champion, recommender, buyer, approver, procurement, security, legal, finance, payer, implementer, operator, partner, support contact, customer-success contact, former customer, and affected nonparticipant only when applicable.

Record relationships between roles: same person, distinct person, unknown, delegated, shared, proxy, household, team, workspace, account, buying group, legal entity, or partner. Preserve changes over time. A user may become a champion; a buyer may never use; a payer may not benefit; an administrator may impose or remove access.

Do not infer one role's job, value, authority, consent, use, purchase, satisfaction, or advocacy from another role. Do not use department labels or one persona as complete role definitions. Include people who cannot access, do not progress, decline, fail, cancel, churn, or are affected without participating.

## Identity And Account Boundaries

Separate identities by decision:

- anonymous visit, browser, device, cookie, ad identifier, referral code, email, phone and channel profile;
- known person, registered user, administrator, member, seat and invitee;
- household, team, workspace, account, parent account, buying group and legal entity;
- opportunity, contract, subscription, entitlement, transaction, invoice, payment, refund and dispute;
- support case, incident, experiment assignment, product event and revenue record.

For each source record key, namespace, entity, version, creation and change rules, permission, collision, duplicate, shared use, merge, split, deletion, retention, correction, and owner. Preserve unknown, unresolved, unassigned, anonymous, duplicated, merged, split, changed, shared, and suppressed states.

Do not build a device graph or perfect customer profile. Cross-channel analytical reconciliation requires minimum-necessary purpose, authority, privacy, security, data-quality, and identity controls. Customer-visible continuity can often be assessed without personal record joins: repeated explanation, context loss, conflicting status, duplicate requests, broken links, missing handoffs, or inconsistent promises.

## Current And Target Versions

Keep `current-state record` and `target-state proposal` separate. The current version describes attributable evidence and unknowns. The target version describes a proposed state, reason, dependencies, assumptions, customer and operating effects, risks, evidence plan, decision, authorization, implementation owner, stop and rollback conditions.

| Dimension | Current evidence | Target proposal | Gap / burden / risk | Dependency / handoff | Verification / expiry |
| --- | --- | --- | --- | --- | --- |
| Roles and value | | | | | |
| States and transitions | | | | | |
| Touchpoints and continuity | | | | | |
| Frontstage and backstage work | | | | | |
| Systems, data and policy | | | | | |
| Failure, recovery and exit | | | | | |
| Measurement and governance | | | | | |

Do not overwrite current evidence after a redesign or rewrite prior uncertainty after outcomes are known. Version corrections, decisions, implementation evidence, results, and supersession explicitly.
