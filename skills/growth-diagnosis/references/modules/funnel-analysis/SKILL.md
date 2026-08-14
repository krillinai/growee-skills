---
name: funnel-analysis
description: Use when a product, marketing, sales, commerce, marketplace, or lifecycle workflow needs a funnel definition, conversion calculation, cohort or segment comparison, drop-off analysis, constraint diagnosis, state-model design, instrumentation specification, or evidence-bounded funnel improvement plan.
---

# Funnel Analysis

Define how eligible customers move through observable value states, calculate loss without changing denominators, identify the most decision-relevant constraint, and design the next evidence or intervention. Work from supplied data or attributable public context. Private analytics, warehouse, CRM, product, billing, support, or research data is optional; mark missing or declined inputs `unavailable`, never fabricate funnel counts, rates, causes, or results.

Read [funnel-contract.md](references/funnel-contract.md) for state definitions, evidence rules, metric contracts, identity, privacy, and reconciliation requirements. Read [analysis-methods.md](references/analysis-methods.md) before calculating conversion, loss, time, cohort maturity, segment effects, or uncertainty. Read [diagnosis-and-design.md](references/diagnosis-and-design.md) before naming a constraint or proposing changes. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `analysis` | Define or calculate a funnel or state model, reconcile counts, and compare mature cohorts or decision-relevant segments |
| `diagnosis` | Separate an observed drop-off from candidate demand, qualification, value, friction, capacity, trust, retention, economics, or measurement mechanisms |
| `design` | Design a funnel or state model, instrumentation contract, intervention portfolio, or validation plan for a supported constraint |

Name one primary mode. A request may include secondary work, but keep observed calculations, causal hypotheses, and proposed interventions visibly separate.

## Freeze The Funnel Contract

Record the decision and owner; final customer and business outcome; entity and level; canonical eligible starting population; ordered states or permitted state transitions; entry and success events for every state; numerator and denominator; observation and maturation windows; identity and deduplication; re-entry, skipping, reversal, and repeat rules; exclusions; timezone; market, language, locale, product surface, source, and segment boundaries; data version and capture date; guardrails; and known limitations.

Do not model a page, click, form field, or internal status as a funnel state merely because it is measurable. A state must represent a meaningful customer or operating transition and have an observable rule. Use a state model when customers can skip, repeat, return, branch, or move backward.

## Validate Before Calculating

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder-only statement without inspectable support may use signal status `reported signal` with a blank evidence state.

Calculate only from attributable counts or records whose entity, eligibility, events, windows, identity, exclusions, and maturity are compatible. Reconcile step counts with canonical cohort membership and end-to-end totals. Preserve zeroes, missingness, late arrival, duplicate identities, partial exposure, and right-censored units. If definitions conflict or required data is absent, return a measurement and instrumentation specification instead of a number.

Never silently change a denominator, exclude users because they encountered friction, combine users with accounts, compare immature with mature cohorts, multiply averages from incompatible populations, or infer causality from transition rates.

## Measure Movement And Contribution

Report step conversion, end-to-end conversion, absolute loss, time in state or time to transition, maturity, and downstream retained or economic quality where available. Show numerators and denominators beside rates. Keep one canonical total view alongside any segments.

Rank opportunities by plausible absolute downstream movement, not by the lowest rate or largest percentage-point gap alone. Consider eligible volume, achievable transition lift, downstream survival, evidence confidence, implementation delay, operating capacity, retained value, economics, reversibility, and risk. Treat opportunity estimates as scenarios, not forecasts.

## Diagnose Without Overclaiming

A funnel shows where observed loss occurs; it does not establish why. Test alternative explanations across demand, promise and qualification, product value, friction, capacity, trust and risk, retention, economics, customer mix, and measurement quality. Preserve intentional qualification, safety, compliance, and trust gates when they protect downstream value.

Name a primary constraint only when the evidence distinguishes it and it plausibly limits the final outcome within the decision horizon. Otherwise rank alternatives and make the discriminating evidence the next action. Use customer research, process observation, instrumentation, operational evidence, and experiments as appropriate.

## Design And Route Work

Tie every proposed change to a named mechanism, eligible population, target transition, downstream outcome, guardrails, owner, maturity window, evidence plan, and decision rule. Preserve the original cohort and denominator through downstream validation.

Route first-value definition or onboarding mechanisms to `activation`, recurring-value and churn mechanisms to `retention`, offer, pricing, payment, revenue, or unit-economics mechanisms to `monetization`, causal validation to `experiment-design`, broader system constraint selection to `growth-diagnosis`, and customer-mechanism research to `customer-research`. Funnel Analysis may specify required messages, campaigns, or copy, but does not draft, launch, send, or publish them.

## Deliver In Order

Return:

1. mode, decision, owner, and analysis boundary;
2. funnel contract and state dictionary;
3. evidence, data-quality, and reconciliation ledger;
4. calculation table or measurement specification;
5. canonical, cohort, and segment findings with maturity;
6. observed loss, candidate mechanisms, counterevidence, and alternatives;
7. primary constraint or unresolved constraint ranking;
8. intervention, instrumentation, validation, owner, and handoffs;
9. Playbook references and external-action boundary.

For China work, keep market, language, locale, product surface, identity, app distribution, payment, channel, platform, consent, and data availability separate. Do not infer WeChat, Mini Program, WeCom, Alipay, app-store, SMS, CRM, analytics, or payment conditions from the market or language.

Analysis, diagnosis, and design authorize local artifacts only. Do not access accounts, query production systems, read or write CRM, warehouse, CDP, analytics, billing, ad, or messaging data, change events or dashboards, launch experiments, alter product flows, publish, send messages, change spend, or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, outcome, entity, eligibility, states, events, denominators, windows, maturity, identity, exclusions, sources, segments, and guardrails are explicit; counts reconcile or discrepancies remain visible; rates include absolute volume; censoring and incompatible cohorts are not hidden; observed drop-off is separate from causal explanation; the primary constraint reflects downstream contribution rather than the lowest rate alone; recommendations do not exceed evidence; Playbook sources are pinned; and no external action occurred.
