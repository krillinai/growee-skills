---
name: growth-benchmark-analysis
description: Use when a growth, product, finance, or operating decision needs internal historical, peer, industry, vendor, survey, case, percentile, best-in-class, reference-class, or market benchmark evidence sourced, audited, normalized, compared, monitored, or interpreted; when metric definitions, populations, maturity, currencies, accounting, selection, survivorship, uncertainty, or transferability may make a benchmark misleading; or when a benchmark risks becoming a target, forecast, causal proof, ranking, or operating standard without support.
---

# Growth Benchmark Analysis

Turn comparison points into a versioned evidence system with explicit reference classes, compatible metric contracts, source lineage, uncertainty, and transfer limits. A benchmark describes attributable observations or estimates inside a bounded comparison set; it is not automatically a baseline, target, forecast, counterfactual, best practice, or attainable standard.

Read [benchmark-contract-and-reference-classes.md](references/benchmark-contract-and-reference-classes.md) before accepting a metric, focal unit, peer group, distribution, period, or comparison purpose. Read [sources-lineage-and-bias.md](references/sources-lineage-and-bias.md) before collecting, deduplicating, verifying, refreshing, or citing benchmark evidence. Read [normalization-uncertainty-and-interpretation.md](references/normalization-uncertainty-and-interpretation.md) before normalizing units, currencies, accounting, maturity, product topologies, distributions, uncertainty, ranks, targets, or causal claims. Follow [output-contract.md](references/output-contract.md) for delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Define a benchmark question, metric contract, reference-class criteria, source plan, and acceptance gate when evidence is missing |
| `audit` | Inspect an existing benchmark, league table, report, peer set, historical series, claim, or decision use |
| `comparison` | Normalize and compare supplied compatible focal and reference evidence |
| `monitor` | Version and refresh benchmark sources, distributions, comparability, corrections, expiry, and decision implications |

Name one primary mode. For every focal-metric and reference-class pair return exactly one verdict:

| Verdict | Meaning |
| --- | --- |
| `comparable` | Metric, class, source, period, maturity, normalization, coverage, and uncertainty support the declared comparison |
| `conditionally comparable` | A bounded comparison is usable only under explicit adjustments, subsets, sensitivity, or assumptions |
| `context-only` | Evidence supplies directional or descriptive context but cannot support rank, gap, threshold, or operating decision |
| `not comparable` | Material definition, population, topology, source, maturity, unit, bias, privacy, or evidence gaps invalidate the comparison |

Do not average verdicts into a benchmark score. A familiar publisher, large sample, repeated citation, executive request, or polished percentile does not establish comparability.

## Freeze The Benchmark Contract

Record benchmark ID and version, mode, decision and owner, focal organization or product, customer and business model, focal metric and version, entity, eligibility, numerator, denominator, unit, value or outcome meaning, source, identity, product and offer version, segment, cohort, market, period, window, maturity, currency and accounting basis, reference-class criteria and exclusions, source cutoff, evidence states, normalization, uncertainty, privacy, review, expiry, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. An attributable statement without inspectable support may remain a `reported signal` with no evidence state. Keep actual, preliminary actual, estimate, modeled estimate, survey response, forecast, scenario, benchmark, baseline, target, plan, budget, quota, approval, action, outcome, and causal effect separate.

Never invent peer values, private performance, sources, definitions, samples, population weights, distributions, percentiles, ranks, normalization, currencies, uncertainty, causes, targets, approvals, actions, or results. Public pages can establish visible claims and product facts only, not private retention, conversion, engagement, economics, or growth.

## Define Reference Classes Before Outcomes

Define reference-class eligibility from the decision: product topology, customer, job, business model, stage, scale, geography, channel, price, sales motion, natural opportunity, metric maturity, period, and evidence availability. Preserve included, excluded, failed, acquired, inactive, private, unknown, and unavailable members with reasons.

Do not choose famous winners, current survivors, vendor customers, favorable cases, or companies with disclosed metrics after seeing the desired outcome. Use contemporaneous membership for historical questions. Report multiple classes and sensitivity when no single peer group is coherent.

Separate internal historical, internal cross-segment, direct peer, broader industry, vendor-customer, survey, modeled, case, regulatory or public filing, and aspirational reference classes. They answer different questions and cannot be silently pooled.

## Protect Source And Distribution Meaning

Trace every benchmark to its earliest inspectable source and underlying dataset. Record publisher, sponsor, collector, methodology, collection and publication periods, sample and response process, definitions, transformations, revisions, commercial incentives, license, access, freshness, and limitations. Repeated articles quoting one dataset are one evidence lineage, not independent confirmation.

Preserve selection, nonresponse, coverage, survivorship, look-ahead, publication, disclosure, attrition, customer-only, active-user, and winner-only bias. A percentile requires a defined reference distribution, not a labeled example. Report counts, denominators, distributions, uncertainty, missingness, and effective coverage rather than point estimates alone.

## Normalize Only Compatible Evidence

Run the compatibility gate before arithmetic: value meaning, entity, eligibility, formula, identity, source type, product, topology, segment, cohort, market, period, maturity, currency, inflation, tax, accounting, refund, recognition, scale, and source quality. If a gate fails, show separate views or return `not comparable`.

Preserve exact original values and create versioned normalized views. Align observation periods, as-of dates, cohort ages, seasonality, late data, and preliminary-versus-final states. For currency and economics, state exchange-rate source and date, nominal or real basis, tax, refunds, discounts, gross or net, revenue recognition, cost scope, and purchasing-power assumptions as relevant.

Do not combine DAU, seats, GMV, messages, tokens, retention, NPS, CAC, NRR, margin, and revenue growth into one score. Adapt reference classes to consumer, low-frequency, B2B, collaborative, marketplace, and AI value topologies.

## Interpret Without Turning Context Into Policy

Report observed focal value, reference distribution, compatible gap, sensitivity, uncertainty, coverage, transfer limits, counterevidence, and decision relevance. Below median does not mean failure; top quartile does not mean healthy; a benchmark is not an attainable counterfactual.

Keep peer practice, implementation, context, outcome, association, candidate mechanism, and causal effect separate. Higher-performing peers using a practice does not prove the practice caused performance or will transfer. Require local customer evidence, operating fit, pilot, or causal validation proportionate to consequence.

Benchmark Analysis does not set targets, rewrite forecasts, allocate budget, approve plans, assign quotas, diagnose root causes, or rank people. Route those artifacts to their owners.

## Route Specialist Work

| Need | Route |
| --- | --- |
| Metric definitions, events, source quality, or cohorts | `growth-metrics-design`, `tracking-plan`, `growth-data-quality-audit`, `cohort-analysis` |
| Targets, forecasts, opportunity, budgets, investments, or plans | `growth-target-setting`, `growth-forecasting`, `growth-opportunity-sizing`, `growth-budget-allocation`, `growth-investment-case`, `growth-planning-cycle` |
| Competitor alternatives, market size, or market entry | `competitive-intelligence`, `market-sizing`, `market-entry-strategy` |
| Engagement, retention, economics, or commercial accounting | `engagement-analysis`, `retention`, `unit-economics-analysis`, `monetization`, `revops-audit` |
| Organization, acquisition, lifecycle, or product mechanism | `growth-organization-design`, `acquisition-strategy`, `lifecycle-marketing`, and the owning lifecycle Skill |
| Unexpected gap, primary constraint, prediction, or causal effect | `growth-anomaly-investigation`, `growth-diagnosis`, `growth-forecasting`, `experiment-design` |

This Skill owns the benchmark question, reference classes, source and lineage ledger, compatibility verdicts, normalization record, distribution and uncertainty view, transfer limits, monitoring, and decision handoff. Routing does not imply analysis, approval, execution, or impact occurred.

## Deliver And Govern

Follow [output-contract.md](references/output-contract.md). Respond in the user's requested language; use Simplified Chinese when requested. Treat every market as a new evidence boundary. For China, separate market, language, locale, currency, timezone, legal entity, product, platforms, app distribution, identity, payment, invoice, tax and accounting basis, source, sample, consent, privacy, support, and local ownership. Translation and currency conversion do not validate transfer.

Use aggregate, redacted, pseudonymous, minimum-necessary evidence and suppress unsafe small cells. Do not collect private contracts, raw customer or employee histories, health, financial, protected-trait, precise-location, private-message, or named performance data merely to enrich a peer set. Do not score or rank named people or companies for consequential pricing, service, employment, credit, insurance, or similar decisions.

## External-Action Boundary

Create and read local artifacts only. Do not bypass authentication, paywalls, robots controls, CAPTCHAs, licenses, or access restrictions; create accounts; accept terms; purchase reports; contact sources; access analytics, finance, benchmark, CRM, billing, HR, or other authenticated systems; export or join private data; change metrics, targets, forecasts, budgets, plans, quotas, dashboards, or decisions; rank or notify people; publish; send; spend; deploy; or claim improvement without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm benchmark ID, version, mode, decision, focal unit, metric, entity, eligibility, formula, value meaning, reference class, membership timing, sources, lineage, source type, evidence states, coverage, selection, nonresponse, survivorship, publication, definitions, periods, maturity, normalization, currency, accounting, distribution, uncertainty, privacy, market transfer, verdicts, sensitivity, counterevidence, causal boundary, handoffs, expiry, corrections, and external actions are explicit; citations did not become independent evidence; missing did not become zero; estimates did not become actuals; incompatible evidence was not averaged; context did not become target, forecast, failure, cause, plan, or result; and no external action occurred.
