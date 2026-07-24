---
name: growth-metrics-design
description: Use when a team needs to audit KPIs, dashboards, targets, metric definitions, North Star Metrics, metric trees, guardrails, business-health measures, or reporting governance; design a decision-useful growth metric system; or specify reproducible metric contracts across product, marketing, sales, marketplace, AI, subscription, commerce, or B2B work.
---

# Growth Metrics Design

Audit, design, or specify a growth metric system that connects delivered customer value to sustainable business outcomes. Keep activity, attribution, prediction, association, and causality distinct. Missing evidence produces a bounded specification, never invented values.

Read [metric-contract.md](references/metric-contract.md) before accepting, comparing, or calculating a metric. Read [metric-system-design.md](references/metric-system-design.md) before selecting roles, a North Star candidate, or tree relationships. Read [measurement-and-governance.md](references/measurement-and-governance.md) before proposing instrumentation, reconciliation, targets, or operating cadence. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Review existing KPIs, definitions, dashboards, targets, trees, and reporting practices |
| `design` | Define a bounded outcome, metric constellation, tree, guardrails, and decision rules |
| `measurement` | Freeze reproducible contracts, sources, identity, windows, lineage, quality, and governance |

Name one primary mode. Preserve useful secondary work without blending an audit finding, design hypothesis, measured result, and operating decision.

## Return One Verdict

| Verdict | Gate |
| --- | --- |
| `decision-ready` | Core contracts are compatible, evidence is attributable, limitations are visible, and the declared decision rule can be applied |
| `partially specified` | Useful definitions or evidence exist, but material contract, comparability, quality, or governance fields remain unresolved |
| `hypothesis` | Customer value, metric role, relationship, target, or operating mechanism is plausible but not supported for the declared scope |
| `not decision-useful` | The proposed measure cannot support the decision because it represents the wrong value, entity, population, denominator, horizon, or evidence type |

Choose exactly one verdict for the metric system in scope. A dashboard, familiar KPI, target, executive preference, or large sample does not make a system decision-ready.

## Freeze The Decision And Contracts

Record the decision, owner, decision date and window, product and business context, customer value, qualified customer outcome, durable business outcome, entity and level, population, events, formula, identity, windows, maturity, cohorts, segments, sources, lineage, quality, guardrails, target basis, limitations, and external-action boundary.

Use exactly `verified`, `reported signal`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing fields. Do not calculate or compare incompatible definitions. When private data is unavailable, create a metric and instrumentation specification with unknowns made explicit.

## Build From Value, Not Availability

Assign each core metric one primary role for the declared objective:

- `outcome`
- `north-star-candidate`
- `input`
- `guardrail`
- `diagnostic`
- `business-health`

A North Star Metric is optional. Reject every candidate when none represents delivered customer value, connects credibly to sustainable business value, decomposes into controllable inputs, and resists low-quality optimization. Revenue, GMV, DAU, MAU, traffic, signups, messages, seats, prompts, tokens, generated outputs, and transactions are not automatically customer value.

Label every metric-tree edge as exactly one of:

- `arithmetic identity`
- `hypothesized driver`
- `observed association`
- `causal evidence`
- `tradeoff`

Arithmetic decomposition does not establish causality. Correlation does not become a driver because it is actionable. A target is a strategic choice, not evidence; an external benchmark is context, not an operating rule.

## Execute In Dependency Order

1. Freeze the decision, owner, customer value, business outcome, and measurement boundary.
2. Validate entities, eligibility, events, formulas, identity, sources, windows, maturity, cohorts, and versions.
3. Assign metric roles and reject vanity or role-confused metrics without discarding useful diagnostics.
4. Build the smallest decision-useful constellation and label every tree edge with its evidence relationship.
5. Separate observed outcomes, predictions, attribution credit, associations, causal effects, targets, and benchmarks.
6. Audit quality, reconciliation, lineage, segment behavior, guardrails, business health, and counterevidence.
7. Specify the next measurement, validation, governance, and specialist handoffs.

## Transfer Across Markets

Treat every market as a new metric evidence boundary. Revalidate customer and payer value, entities, eligibility, events, formulas, identity, windows, cohorts, maturity, segments, sources, lineage, quality, targets, benchmarks, guardrails, business health, owners, and decision rules. Translation, a copied dashboard, or a familiar metric name does not validate transfer.

For China, distinguish market, legal entity, language, locale, product, channel, platform, app distribution, identity, payment, invoice, data source, consent, storage and transfer, content, advertising, support, and locally accountable review. When Simplified Chinese is requested, respond in native Simplified Chinese. Use current direct sources and local expertise; do not infer provider availability or make legal, tax, regulatory, accounting, causal, or performance conclusions. Keep the system `partially specified` or `hypothesis` until compatible local contracts and evidence support another verdict.

## Route Specialist Work

This Skill owns metric roles, contracts, constellation and tree design, relationship labels, guardrails, and measurement governance. Route adjacent artifacts without recreating them:

| Need | Route |
| --- | --- |
| Primary-constraint selection | `growth-diagnosis` |
| Value-state transitions or equal-maturity comparisons | `funnel-analysis`, `cohort-analysis` |
| Decision-critical identity, completeness, validity, lineage, or reconciliation defects | `growth-data-quality-audit` |
| Organization target commitments or time-indexed projections | `growth-target-setting`, `growth-forecasting` |
| One causal test or a cross-team experiment portfolio | `experiment-design`, `experiment-program-management` |
| Recurring weekly, monthly, or quarterly decision review | `growth-operating-review` |
| First value, recurring value, monetization, or returned-input mechanisms | `activation`, `retention`, `monetization`, `growth-loop-design` |

## Deliver In Order

Return:

1. mode, decision, owner, context, and measurement boundary;
2. one metric-system verdict and its limiting gate;
3. customer value, qualified outcome, and North Star recommendation or rejection;
4. metric constellation with one primary role per core metric;
5. metric tree with labeled relationships and evidence states;
6. versioned Metric Contracts;
7. evidence, compatibility, quality, lineage, target, benchmark, and limitation ledger;
8. instrumentation, reconciliation, governance, and 30-day validation plan;
9. Playbook sources, capability handoffs, and external-action boundary.

## External-Action Boundary

This Skill produces local analysis and specifications. Do not access analytics, warehouses, CRM, billing, advertising, or product systems; query production data; export customer data; alter events, identity, definitions, targets, dashboards, alerts, reports, experiments, or customer state; publish results; or claim those actions occurred without separate task-level authorization and a capable execution path.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision and owner are explicit; every core metric has one role and a reproducible or visibly incomplete contract; entities, denominators, windows, maturity, cohorts, sources, and versions are compatible; North Star candidacy is tested rather than assumed; every tree edge names its relationship and evidence; quality, trust, risk, cost, and business guardrails remain visible; targets and benchmarks have attributable bases or stay unavailable; predictions, attribution, association, and causality remain separate; missing evidence yields useful next work; specialist handoffs do not duplicate adjacent Skills; sources are pinned; and no external action occurred.
