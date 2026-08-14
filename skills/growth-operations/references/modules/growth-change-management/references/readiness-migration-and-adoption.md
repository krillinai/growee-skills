# Readiness, Migration, And Adoption

## Contents

1. Readiness gates and decisions
2. Communications and enablement
3. Migration, cutover, rollback, and recovery
4. Rollout and adoption states
5. Support, benefits, and decommissioning

## Readiness Gates And Decisions

Readiness is a set of evidence-backed gates, not a composite score.

| Gate | Questions |
| --- | --- |
| Decision | Is the exact change decided, approved where required, authorized, versioned, and still valid? |
| Product | Does the target state work for eligible roles, versions, environments, accessibility needs, and exceptions? |
| Data | Are identities, schemas, definitions, quality, consent, lineage, reconciliation, retention, and correction ready? |
| System | Are dependencies, access, reliability, observability, security, load, backup, fallback, and recovery ready? |
| People | Do affected roles have capacity, access, understanding, practice, support, and safe feedback paths? |
| Operations | Are procedures, owners, schedules, vendors, incidents, exceptions, manual paths, and residual duties ready? |
| Support | Are volume assumptions, staffing, knowledge, routing, escalation, accessibility, and service recovery ready? |
| Market | Are local customers, product, platforms, vendors, timing, language, policy, data, payments, and support revalidated? |
| Governance | Are authority, privacy, security, fairness, legal review, audit, stop, rollback, correction, and expiry explicit? |

For each gate record requirement, applicable change unit, evidence, evidence state, source and version, owner, dependency, state, limitation, exception, condition, review, expiry, and accountable decision authority. Use `pass`, `partial`, `fail`, `unavailable`, or `not applicable` only against explicit criteria.

Do not assign decimal readiness or confidence from adjectives. If supplied inputs support a calculation, show formula, units, scale, weights, source, range, missing fields, and limitation; never let an average offset a hard blocker. Return an evidence coverage view separately from readiness.

Possible decisions are `go`, `go with conditions`, `stage`, `hold`, `pause`, `stop`, `rollback`, or `escalate`. Record owner, authority, evidence, dissent, residual risk, conditions, expiry, review, and what would reverse the decision. The Skill may recommend or draft a decision record; it does not authorize.

When authority, accepted ownership, capacity, dependencies, criteria, or calendar basis is unavailable, keep decision, owner, date, target, communication, enablement, migration, rollout, adoption, and closure fields unavailable. Record requested values only in the request ledger. Do not convert relative dates into calendar dates, create suggested 30/60/90 commitments, reserve unnamed roles, or label a candidate design as an accepted plan.

## Communications And Enablement

### Communication contract

| Audience / role | Need and impact | Claim / source / version | Sender / authority | Permitted channel / timing | Action / acknowledgement | Feedback / correction / expiry |
| --- | --- | --- | --- | --- | --- | --- |

Track states separately:

```text
created -> reviewed -> approved -> scheduled -> sent -> delivered
-> viewable -> viewed -> aware -> comprehending -> responding -> acting
```

Delivery and opens are transport or attention evidence. They do not prove comprehension, agreement, consent, authorization, action, compliance, or adoption. Silence can mean absence, accessibility failure, channel failure, lack of authority, lack of value, fear, confusion, or deliberate rejection.

Use minimum-necessary information by audience. Define confidentiality, localization, accessibility, frequency, quiet periods, suppression, questions, dissent, escalation, correction, withdrawal, expiry, and retirement. Do not repeat communications until compliance or disclose private project details indiscriminately.

### Enablement contract

| Role / target task | Prerequisite / environment | Asset / source version | Practice / assessment | Competence evidence | Support / remediation / refresh | Privacy / accessibility / expiry |
| --- | --- | --- | --- | --- | --- | --- |

Track `available`, `assigned`, `enrolled`, `attended`, `completed`, `comprehended`, `practiced`, `demonstrated competence`, `performed in context`, `repeated correctly`, and `adopted` separately. Define representative tasks, quality criteria, assessor, independence, observation window, exceptions, appeal, and revalidation.

Attendance or a quiz may show participation or bounded recall. It cannot prove role competence, correct production behavior, customer value, durable adoption, or business impact. Never publish employee rankings or use enablement evidence for consequential decisions without a separately authorized, fair, appealable process and accountable expertise.

## Migration, Cutover, Rollback, And Recovery

Create an object-level migration map:

| Source object / version | Target object / version | Identity and field mapping | Eligible / excluded / unsupported | Transform / validation | History / permission / retention | Owner / acceptance / exception |
| --- | --- | --- | --- | --- | --- | --- |

Map customers, accounts, users, identities, permissions, entitlements, prices, contracts, events, metrics, content, workflows, integrations, history, and unsupported states separately as applicable. Define source freeze, target write, mapping, default, null, duplicate, conflict, precision, currency, time zone, language, consent, lineage, backfill, and correction rules.

Use a bounded sequence:

1. Freeze versions, population, eligibility, exclusions, authority, backup, and acceptance criteria.
2. Validate mappings and dependencies with representative test cases and unsupported states.
3. Run a dry run or trial migration against a bounded cohort where authorized.
4. Reconcile counts, identities, states, values, history, permissions, failures, and sampling evidence.
5. Use dual run or shadow comparison when consequences and feasibility require it.
6. Admit the next cohort only after entry, exit, support, guardrail, and independent verification gates pass.
7. Hold, stop, rollback, fall back, or recover when predeclared triggers occur.
8. Retain the prior state until residual obligations and decommissioning gates pass.

Define idempotency, retries, partial failure, failed-record queues, manual review, audit, privacy, support, incident ownership, communication correction, recovery time and recovery point where relevant. A green smoke test proves only its bounded checks. Verify representative workflows, reconciled data, permissions, performance, security, support, customer safety, and downstream consumers separately.

Do not recommend an irreversible global cutover merely because a date was announced. Account for time zones, peak periods, blackout windows, support coverage, vendor dependencies, customer promises, and local authority.

## Rollout And Adoption States

Use an explicit state model:

```text
eligible -> assigned -> access granted -> enabled -> rendered
-> viewable -> exposed -> interacted -> first useful task
-> competent use -> repeated useful workflow -> adopted workflow
-> retained value -> customer outcome -> business outcome
```

Account, workspace, administrator, buyer, payer, user, and nonparticipant are different entities. A feature flag at account level does not prove user access, render, exposure, use, competence, adoption, or value.

For every rate specify metric ID and version, entity, eligible population, numerator, denominator, identity, event or state, source, cohort, assignment, exposure, segment, market, period, window, maturity, exclusions, late-arriving data, suppression, revision, valid zero, owner, and limitation.

Separate communication reach, enablement, technical rollout, workflow adoption, operational compliance, customer outcome, business outcome, and causal effect. Track invited and uninvited, eligible and ineligible, exposed and unexposed, adopting and nonadopting, exception and workaround, support-assisted and unassisted, retained and reversed states.

## Support, Benefits, And Decommissioning

Support is part of change readiness and customer protection. Define eligible users, channels, hours, languages, accessibility, expected volume, staffing and capacity, knowledge version, escalation, incident class, workaround, response and resolution boundaries, correction, feedback, privacy, and sunset. Ticket closure is not problem resolution or adoption.

Measure adoption quality with workflow completion, task quality, time to competence, repeated value, breadth and depth where relevant, workaround and exception use, errors, reversals, support burden, trust, accessibility, customer retention, economics, and harm. Preserve nonuse caused by exclusion, lack of access, low relevance, low authority, low capacity, low trust, poor support, or deliberate rejection.

For benefits, record hypothesis, intended mechanism, source decision, outcome metric and version, baseline, eligible, assigned, exposed, adopting, nonadopting and unaffected populations, start, maturity, comparator, guardrails, alternative explanations, concurrent changes, disconfirming evidence, causal design, attribution limit, review, and owner. Communications, training, rollout, adoption, or temporal sequence alone cannot establish incremental benefit.

Decommission only after source freeze, migration acceptance, downstream acknowledgement, support and incident review, retention and archive, access revocation, contract and vendor obligations, privacy and deletion rules, audit evidence, rollback horizon, residual users and data, correction path, owner, and independent verification pass. Record what remains, why, who owns it, review, and expiry. Never claim deletion or retirement from a plan.
