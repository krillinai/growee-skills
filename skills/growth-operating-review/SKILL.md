---
name: growth-operating-review
description: Use when a team needs to build, run, audit, or refresh a weekly, monthly, or quarterly growth operating review; reconcile customer value, lifecycle, acquisition, growth accounting, revenue, economics, forecasts, anomalies, experiments, initiatives, capacity, risks, commitments, and prior decisions; or replace status reporting and dashboard recitals with a versioned, evidence-bounded decision forum.
---

# Growth Operating Review

Turn a recurring growth meeting into a versioned decision system. Focus on material changes, constraints, customer and business outcomes, assumptions, risks, and commitments rather than exhaustive metrics or activity. A review compares evidence with prior expectations and decisions; it does not manufacture causality, rewrite history, or authorize execution.

Read [review-contract.md](references/review-contract.md) before accepting cadence, period, as-of date, audience, metrics, comparisons, or evidence. Read [evidence-and-reconciliation.md](references/evidence-and-reconciliation.md) before interpreting movement, targets, forecasts, growth accounting, experiments, or anomalies. Read [operating-review-views.md](references/operating-review-views.md) before constructing customer, lifecycle, acquisition, economic, portfolio, capacity, or risk views. Read [decisions-cadence-and-governance.md](references/decisions-cadence-and-governance.md) before assigning decisions, commitments, cadence, market transfer, privacy, or external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `build` | Create a review from bounded supplied evidence and prior decision records |
| `audit` | Inspect whether an existing review is reproducible, comparable, decision-focused, and governed |
| `refresh` | Update a prior review with new mature evidence while preserving its version and history |

Name one cadence: `weekly`, `monthly`, or `quarterly`. A weekly review handles fresh operating signals, incidents, commitments, and near-term gates. A monthly review reconciles mature lifecycle, economic, forecast, experiment, and portfolio evidence. A quarterly review tests strategic assumptions, capacity, and portfolio direction. Cadence does not override metric maturity.

Route each follow-up to the smallest specialist artifact that can resolve it:

| Follow-up need | Route |
| --- | --- |
| Current primary constraint and 30-day plan | `growth-diagnosis` |
| Unexpected metric movement or decision-critical cross-source data defects | `growth-anomaly-investigation`, `growth-data-quality-audit` |
| Metric contract, instrumentation, projection, or one causal test | `growth-metrics-design`, `tracking-plan`, `growth-forecasting`, `experiment-design` |
| Cross-team experiment portfolio, capacity, quality, and learning governance | `experiment-program-management` |
| Material strategic choice or annual, quarterly, or rolling integrated plan | `growth-strategy`, `growth-planning-cycle` |
| One investment case, shared budget allocation, or one selected initiative plan | `growth-investment-case`, `growth-budget-allocation`, `growth-initiative-planning` |
| One canonical decision, a cross-initiative risk portfolio, or reusable cross-source learning | `growth-decision-record`, `growth-risk-management`, `growth-learning-system` |
| Adoption and legacy retirement for an authorized change, or one completed-work retrospective | `growth-change-management`, `growth-postmortem` |

The review records decisions and reconciles returned evidence; it does not recreate specialist analysis or imply execution.

## Freeze The Review Contract

Record review ID and version, cadence, period, as-of and evidence cutoff, accountable review owner, decision owners, audience and required approvers, scope and exclusions, product and business model, customers and participant roles, market and locale, stage, prior review and strategy versions, target decisions, metric maturity, source availability, meeting date, next review, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Keep actual, reported signal, estimate, benchmark, target, forecast, scenario, causal estimate, plan, approval, action, completion, and result separate. Preserve source, date, version, entity, definition, segment, market, period, currency, accounting basis, freshness, lag, maturity, limitations, contradictions, revisions, and lineage.

Do not invent metric values, targets, benchmarks, causes, forecasts, experiment results, economics, capacity, confidence, approvals, completion, or impact. Do not blend incompatible entities, cohorts, denominators, windows, markets, currencies, accounting bases, or evidence maturities.

## Validate Before Interpreting

For every decision-relevant metric confirm entity, eligibility, numerator, denominator, event or state, identity, segment, market, window, cohort, maturity, source of truth, freshness, lag, version, quality, and owner. An incomplete period or immature cohort is `unavailable`, not zero.

Check instrumentation and definition changes, delayed data, backfills, duplicates, identity breaks, attribution changes, currency and accounting revisions, missing segments, and source reconciliation before explaining movement. Separate measurement change, mix shift, temporary variance, execution miss, structural change, and unknown.

## Compare Against The Right Reference

Choose comparison by decision: compatible prior period or cohort, seasonality-adjusted history, target, as-of forecast, valid control, operational boundary, or strategy assumption. State why it is compatible. A target miss is not a cause. A benchmark is not an attainable counterfactual. A forecast is not a target or strategy.

Show absolute and relative change, numerator and denominator movement, maturity, segment or mix contribution, uncertainty, and revision. Preserve positive, negative, flat, harmful, delayed, contradictory, and unavailable evidence.

## Reconcile The Operating System

Build only the views material to the review:

1. **Customer value:** first, repeated, expanded, restored, or protected value and guardrails.
2. **Lifecycle and acquisition:** qualified source through activation, retention, monetization, referral, and expansion using compatible cohorts.
3. **Growth accounting:** opening, retained, new, resurrected, expanded, contracted, churned, and closing stocks or values.
4. **Economics and cash:** revenue, gross profit, contribution, cash, marginal economics, capacity, and customer protection.
5. **Forecast and scenarios:** prior as-of forecast, mature actual, error, bias, revisions, and decision implications.
6. **Experiments and learning:** validity, maturity, guardrails, outcomes, cumulative evidence, and next decision.
7. **Portfolio and capacity:** strategic link, evidence gate, dependencies, opportunity cost, concentration, and retain, revise, accelerate, cap, pause, graduate, or retire decision.
8. **Risks and systems:** reliability, quality, privacy, trust, security, regulatory review, incidents, and critical capability health.

Do not count the same customer or value at multiple lifecycle stages. Do not add attributed channel outcomes, experiment uplifts, opportunity ranges, or initiative claims as independent impact. Activity, launches, assets, meetings, and completed tasks are not customer or business outcomes by themselves.

## Investigate Material Change Without Causal Leaps

For a material change, state observation, expected range or comparator, affected scope, customer and business effect, data-quality state, candidate mechanisms, supporting and contradictory evidence, decision urgency, owner, and next evidence. Route a detailed incident or unexpected movement to `growth-anomaly-investigation`.

Do not declare a crisis, root cause, or remedy from one aggregate chart. Correlation, sequence, attribution, and stakeholder belief do not establish causality. Proposed rollback, budget, price, product, or operational changes require separate authorization and controls.

## Turn Evidence Into Decisions

For each decision record context, alternatives, evidence, contradiction, customer and economic effect, risk, owner, required approver, decision state, rationale, conditions, expiry, and review trigger. Use `decide`, `continue`, `investigate`, `escalate`, `defer`, `stop`, or `route` only when evidence distinguishes them.

For every commitment record owner, artifact or outcome, due or decision date, dependency, evidence of completion, permission boundary, and status: `open`, `blocked`, `complete`, `revised`, `cancelled`, or `expired`. `In progress` is not completion proof. Do not carry actions indefinitely or rewrite prior decisions after seeing outcomes.

## Handle Cadence And Escalation

Carry forward stable contracts, definitions, assumptions, and prior decisions by version. Do not recalculate LTV, market size, pricing, organization, strategy, or every experiment at every weekly review. Escalate only material decisions that exceed the forum's authority, evidence, time, risk, or scope.

Keep attendance tied to decision rights. A review is not successful because every leader attended or every topic was discussed. Completion means decisions and unresolved evidence are explicit, owners accepted responsibility, and the record is versioned.

## Handle Markets, People, And Data

Treat every market as a new evidence boundary. Revalidate definitions, baselines, cohorts, targets, forecasts, channels, prices, economics, source access, operating capacity, risks, and owners. Translation and currency conversion do not validate transfer.

For China, distinguish market, legal entity, language, locale, product, platform, app distribution, identity, payment, invoice, data, content, advertising, support, and locally accountable review. Use current direct sources and local expertise. Do not make legal, tax, regulatory, provider-availability, accounting, or performance conclusions.

Use aggregate, redacted, pseudonymous, minimum-necessary evidence by default. Do not expose credentials, payment details, private messages, health data, protected traits, precise locations, raw identities, employee records, or full histories when bounded aggregates suffice. Do not rank individuals for consequential pricing, employment, credit, insurance, health, housing, or similar decisions.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the review contract; evidence and metric health; executive decision view; customer, lifecycle, accounting, economic, forecast, experiment, portfolio, system, and risk views as applicable; decisions and commitments; escalations and handoffs; pinned sources; external actions; and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated analytics, CRM, advertising, billing, finance, product, cloud, experiment, sales, support, HR, research, or data systems; export or join personal data; change metrics, targets, forecasts, budgets, prices, products, experiments, roadmaps, permissions, contracts, or records; send decisions; contact people; publish; spend; deploy; or claim implementation or business results without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md), all material evidence is versioned and comparable, immature data is not zero, targets and forecasts did not become causes, customer and economic outcomes reconcile without duplication, decisions and commitments have owners and rules, specialist work is routed, privacy and market boundaries hold, and no external action occurred.
