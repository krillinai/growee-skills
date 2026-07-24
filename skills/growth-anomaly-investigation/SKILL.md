---
name: growth-anomaly-investigation
description: Use when a growth, product, customer, channel, lifecycle, revenue, experiment, or operating metric unexpectedly rises, falls, spikes, drops, diverges from a baseline, disagrees across dashboards, or appears structurally different and a team needs read-only triage, decomposition, evidence, or root-cause review before acting.
---

# Growth Anomaly Investigation

Determine whether an observed metric change is a measurement issue, behavioral change, mixed effect, expected variation, or unresolved. Freeze comparability first, quantify and reconcile the change, locate contribution without losing the parent total, and test candidate mechanisms without converting timing, attribution, or segment correlation into causality.

Read [anomaly-contract.md](references/anomaly-contract.md) before accepting a chart, metric, source, baseline, comparison, maturity, or resolution. Read [integrity-and-decomposition.md](references/integrity-and-decomposition.md) before reconciling dashboards, testing data continuity, quantifying a change, estimating expected variation, decomposing segments, or searching cohorts. Read [timeline-mechanisms-and-evidence.md](references/timeline-mechanisms-and-evidence.md) before building a change timeline, ranking mechanisms, interpreting releases, experiments, attribution, fraud, or defining next evidence. Read [governance-market-transfer-and-actions.md](references/governance-market-transfer-and-actions.md) before closure, monitoring, market transfer, personal data, specialist handoffs, or external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `triage` | Decide whether a reported change is measurable, mature, material, and more consistent with data, behavior, expected variation, or unresolved evidence |
| `investigate` | Reconcile sources, quantify and decompose the change, build a timeline, and compare candidate mechanisms |
| `review` | Audit an existing analysis for contract, denominator, maturity, baseline, decomposition, multiplicity, evidence, and causal errors |

Name one primary mode, incident, decision, owner, and deadline. A request to redefine the metric belongs to `growth-metrics-design`; implement event or identity changes through `tracking-plan`; analyze a frozen funnel through `funnel-analysis`; analyze cohorts through `cohort-analysis`; reconcile customer or recurring-value states through `growth-accounting`; reconcile channel credit through `attribution-analysis`; test causality through `experiment-design`; and select the primary growth constraint through `growth-diagnosis`.

## Freeze The Anomaly Contract

Record incident ID and reported time, symptom, decision, owner, metric entity and state or event, numerator, denominator, eligibility, identity, unit, aggregation and exclusions, source and lineage, query or report version, product and app version, customer and segment, market and locale, channel and platform, event and processing time, timezone, observation and outcome windows, cutoff, lateness and correction rules, baseline, expected-variation method, maturity, evidence access, status, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. An attributable unverified incident claim may remain a `reported signal`. Keep observation, derived value, attribution, association, causal estimate, forecast, target, benchmark, correction, approval, zero, missing, late, immature, censored, and suppressed separate.

Do not invent metric definitions, counts, denominators, baselines, distributions, uncertainty, causes, revenue effects, confidence scores, approvals, corrections, or results. A screenshot verifies only visible labels and values at capture; it does not establish source integrity, maturity, impact, or cause.

## Verify Integrity And Maturity

Reconcile metric and event definitions, entities, eligibility, identity, deduplication, filters, aggregation, source tables, joins, semantic layers, queries, timezones, freshness, lateness, backfills, corrections, consent, bot rules, attribution, currency, product and SDK coverage, and owners across every source. Do not average disagreeing dashboards. Quantify compatible coverage, differences, and residuals.

Check for renamed or split events, trigger changes, client or server migration, missing backfill, duplicate suppression, retry storms, identity merges or splits, account hierarchy changes, consent loss, bot filters, attribution windows, report edits, partial periods, delayed outcomes, refunds, and cohort censoring.

Missing, late, immature, and suppressed are not zero. Compare like-for-like observation and outcome maturity. If the decision precedes maturity, label provisional ranges and the cost of acting early.

## Quantify Against A Valid Baseline

Report prior and current counts, denominators, rates or values, absolute and relative deltas, parent contribution, missing and unknown states, window, timezone, and maturity. A rising rate can hide falling successful counts; a large relative change can have negligible aggregate impact.

Select a predeclared compatible baseline using matched historical periods, weekdays, seasons, holidays, promotion states, markets, cohorts, versions, or valid unaffected units. Account for known structural trends, calendar, billing, renewals, weather, campaigns, outages, and external changes. A benchmark is context unless definitions and populations are truly compatible.

Do not invent significance or expected intervals. Use a suitable method only when sufficient event-level or aggregate inputs are supplied; otherwise request the smallest required fields and preserve uncertainty as unavailable.

## Decompose Without Fishing

Start with source and version, lifecycle or value state, major customer and market mix, product, plan, platform, channel, cohort, eligibility, access, and exposure. Use the fewest decision-relevant dimensions that explain a material parent contribution.

For every split show parent and child totals, counts, denominators, rates or values, coverage, overlap, unknown residual, and reconciliation. Separate aggregate-rate mix effects from within-segment effects and state the weighting convention. Separate additive opening, inflow, outflow, adjustment, and closing states where relevant. Descriptive contribution identifies where change appears, not why.

Track comparisons, mark post-hoc cells exploratory, protect small groups, and require stability or confirmatory evidence. Do not slice until a tiny group looks extreme, use sensitive traits without necessary review, or force unknown residual to a preferred mechanism.

## Build The Timeline And Mechanism Ledger

Version product, price, tracking, identity, attribution, experiment, campaign, budget, channel, partner, incident, outage, fraud control, holiday, promotion, billing, competitor, platform, regulation, weather, and market events. Record announcement, availability, eligibility, access, exposure, adoption, outcome, rollback, and recovery separately.

For each candidate mechanism state affected population, expected onset, lag, duration, maturity, supporting and contradictory evidence, alternatives, causal status, and the smallest discriminating read-only check. Keep symptom, contributor, mechanism, and root cause distinct. Temporal order is not causality.

Preserve experiment assignment, exposure, overlap, interference, carryover, novelty, SRM, randomization unit, and maturity. Version attribution models, lookbacks, touchpoints, identity coverage, unknown and organic states. For spikes, inspect bots, duplicates, tests, retries, spam, fraud, abuse, and valid high-frequency behavior before calling growth.

## Resolve Or Remain Unresolved

Use one primary state only when evidence distinguishes it:

- `measurement issue` for a material definition, identity, collection, processing, source, query, quality, or maturity effect;
- `behavioral change` for a compatible real customer, participant, market, product, or operating effect;
- `mixed` when both are material or aggregated together;
- `expected variation` when the change fits the declared baseline after integrity checks;
- `unresolved` when evidence cannot distinguish states or contributors.

State material evidence, measurement and behavioral contributions, expected variation, unknown residual, affected populations, confidence boundary, impact, remaining risk, next evidence, monitoring or containment recommendation, owner, review or maturity date, and closure criteria. Do not force a root cause or numeric confidence score.

## Route Specialist Work

| Need | Route |
| --- | --- |
| Metric contract | `growth-metrics-design` |
| Event, identity, source, or schema implementation | `tracking-plan` |
| Transition and drop-off analysis | `funnel-analysis` |
| Cohort, retention, or maturity analysis | `cohort-analysis` |
| Customer or recurring-value movement | `growth-accounting` |
| Touchpoint and source credit | `attribution-analysis` |
| Experiment integrity and causal effect | `experiment-design` |
| Forecast baseline and calibration | `growth-forecasting` |
| Primary growth constraint | `growth-diagnosis` |
| Data and decision capability remediation | `growth-infrastructure-assessment` |

Preserve the frozen contract, required inputs, decision, owner, maturity, expected artifact, and permission boundary. A handoff does not imply the analysis or action ran.

## Handle Markets, Privacy, And Actions

Treat each market as a new metric, source, calendar, product, platform, identity, payment, release, data-latency, fraud, benchmark, and expected-variation boundary. Translation does not validate transfer.

For China, distinguish market, legal entity, language, locale, timezone, product, channel, platform, app distribution, identity, payment, invoice, data, content, advertising, holidays, release, support, and locally accountable review. Use current direct sources and local expertise. Do not make legal, regulatory, provider, causal, or performance conclusions.

Use aggregate, redacted, pseudonymous, minimum-necessary data. Do not request sensitive data, identify or blame people, expose small groups, or rank individuals for consequential decisions.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the incident and metric contract; integrity and maturity; observed change; source reconciliation; decomposition; timeline and candidates; resolution and impact; evidence, monitoring or containment plan; governance, handoffs, pinned sources, external actions, and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated systems; export or join personal data; change tracking, data, backfills, dashboards, product, prices, campaigns, budgets, experiments, flags, releases, or records; pause; roll back; contact; publish; send; spend; deploy; or claim resolution or business impact without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md), sources are reconciled before causes, counts and denominators accompany rates, comparisons are mature and compatible, parent totals reconcile, mix and within effects remain descriptive, candidate mechanisms preserve alternatives and causal status, resolution follows evidence, specialist work is routed rather than invented, and no external action occurred.
