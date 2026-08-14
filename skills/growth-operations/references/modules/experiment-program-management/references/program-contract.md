# Experiment Program Contract

## Freeze Program Identity

| Field | Required record |
| --- | --- |
| Program | ID, version, mode, state, purpose, current version, superseded version, and non-goals |
| Accountability | Program owner, decision owners, portfolio owner, platform and data owners, contributors, specialist reviewers, approvers, escalation, and segregation of duties |
| Scope | Company, portfolio, products, business models, customers, participant roles, markets, locales, teams, decision classes, and exclusions |
| Time | Fiscal and calendar periods, planning horizon, evidence cutoff, exposure periods, maturity horizon, review, and expiry |
| Lineage | Strategy, metric registry, experiment-platform, budget, organization, operating-review, and prior-program versions |
| Systems | Supplied artifacts, source systems, access state, identity, assignment, exposure, metric, repository, decision, and follow-through records |
| Governance | Evidence, ethics, privacy, security, market, approval, authorization, exposure, communication, publication, and external-action boundaries |

Do not silently change the program population, market, metric version, decision horizon, evidence cutoff, risk tier, or authority. Public information cannot establish a private program inventory, traffic, capacity, platform health, incidents, results, decisions, or impact.

## Use Explicit Evidence And Action States

Use only `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Preserve source, owner, date, version, population, market, definition, window, maturity, limitations, contradictions, corrections, and lineage. An attributable unsupported statement may remain a `reported signal` without an evidence state.

Keep these concepts separate:

```text
request -> recommendation -> decision -> approval -> authorization
-> assignment -> eligibility -> exposure -> implementation
-> analysis -> readout -> follow-through -> verification -> outcome
```

No earlier state proves a later state.

## Require Program Readiness Before Precision

Numeric targets and operating commitments require:

- a complete eligible inventory and stable denominator, including unfavorable and incomplete states;
- current baselines with compatible definitions, sources, windows, maturity, segmentation, and corrections;
- a time-phased traffic, identity, surface, sensitivity, holdout, engineering, analysis, review, support, and decision-owner capacity model;
- explicit decision portfolio, dependencies, interference, opportunity cost, incident history, long-term obligations, and risk policy;
- attributable owners, reviewers, approvers, authorization boundaries, effective periods, review triggers, and expiry.

When any material condition is unavailable, use `draft` or `reconciling`. Do not invent target percentages, score weights, quotas, portfolio ratios, deadlines, service levels, retention periods, traffic ceilings, schedule phases, risk-tier thresholds, cadences, owners, approvers, or approval matrices. Keep supplied goals as requests or scenarios and return metric definitions, nonnumeric workflow, unresolved evidence, and readiness conditions.

## Maintain A Complete Inventory

Use states only when attributable records support them:

| State | Meaning |
| --- | --- |
| `proposed` | An uncertainty or solution was submitted |
| `incomplete` | Required decision or evidence fields are missing |
| `rejected` | The program declined the item with rationale and reopen evidence |
| `queued` | Accepted but not yet through quality, traffic, capacity, or authority gates |
| `gated` | A named prerequisite blocks valid progression |
| `approved-record` | An approver accepted the bounded design or program position |
| `authorized-record` | Separate evidence permits the named exposure or action |
| `exposed-record` | Supplied records verify eligible exposure occurred |
| `stopped` | Exposure or work ended under an attributable decision |
| `cancelled` | Work ended before decision evidence was produced |
| `expired` | Evidence, approval, queue position, or decision window lapsed |
| `maturing` | Required outcome windows are not complete |
| `readout-ready` | Required quality and maturity gates support interpretation |
| `decided` | An accountable owner recorded the bounded decision |
| `follow-through-pending` | The decision has no verified implementation or closure record |
| `verified` | Bounded follow-through proof exists; impact remains separate |
| `invalid` | Quality or design failure prevents the intended inference |
| `superseded` | A later version replaces the record without erasing history |

Preserve flat, negative, harmful, underpowered, invalid, cancelled, expired, and inconclusive items. Define one consistent eligibility and retention rule; do not curate the denominator to improve win, velocity, or conclusiveness rates.

## Check Compatibility

Before aggregating, align decision type, customer, product, market, randomization unit, identity, eligibility, intervention, metric definition, baseline, threshold, assignment, exposure, analysis population, time window, maturity, evidence design, result state, currency, and cost boundary.

Keep incompatible experiments and alternative evidence designs separate. Counts across different decision importance, sensitivity, maturity, risk, and design classes do not become a quality score.

## Protect Version History

For `refresh`, preserve prior intake, priority, specification, traffic plan, capacity, concurrency, quality gates, incidents, amendments, results, decisions, follow-through, learning, health claims, and rationale. Add corrections and mature evidence by version. Record who changed what, why, which prior statement remains valid, and which downstream decision must reopen.
