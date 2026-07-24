---
name: acquisition-strategy
description: Use when a team needs to audit, design, compare, sequence, diversify, scale, cap, or stop acquisition channels or a channel portfolio; evaluate channel-model fit, source quality, attribution versus incrementality, full or marginal CAC, payback, retained contribution, saturation, creative or audience decay, platform and partner dependency, product-led distribution, market entry, or acquisition budget scenarios across paid, organic, earned, owned, sales, partner, app-store, search, content, social, and portfolio mechanisms.
---

# Acquisition Strategy

Design a portfolio that connects a defined customer problem and reachable intent to incremental customers who activate, retain, and create acceptable contribution. Reach, traffic, leads, signups, rankings, followers, attributed conversions, low historical CAC, and channel count are operating signals; none proves acquisition quality, incrementality, economics, or diversification.

Read [acquisition-contract.md](references/acquisition-contract.md) before accepting audience, source, attribution, cohort, cost, retention, contribution, saturation, or dependency evidence. Read [channel-and-portfolio-methods.md](references/channel-and-portfolio-methods.md) before selecting, sequencing, scaling, diversifying, or stopping channels. Read [measurement-and-economics.md](references/measurement-and-economics.md) before calculating CAC, payback, contribution, incrementality, or allocation. Read [market-entry-and-risk.md](references/market-entry-and-risk.md) for international, platform, partner, concentration, privacy, and operating boundaries. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Diagnose an existing source, channel, campaign family, acquisition result, market, economics claim, quality problem, saturation pattern, or dependency |
| `design` | Define one bounded channel hypothesis, source-to-value path, market-entry sequence, validation plan, or second distribution mechanism |
| `portfolio` | Compare channels, spend bands, markets, or mechanisms and create evidence-gated allocation, cap, reallocation, or retirement scenarios |

Name one primary mode, acquisition decision, owner, customer and problem, qualified entry state, market, product and business model, horizon, budget or capacity boundary, and external-action limit. Public information may verify visible channels, pages, offers, partners, terms, rankings, ads, and dated claims; it cannot establish private spend, exposure, identity, attribution quality, incrementality, CAC, retention, contribution, saturation, contracts, or operational risk.

## Keep One Output Language

Choose the report language from the request. When no language is explicit, match the user's dominant language. Market, locale, platform, and source language do not override the requested output language.

Use one language consistently across titles, headings, prose, tables, labels, recommendations, owners, stages, gates, and handoffs. Do not make a report appear technical by mixing ordinary English business terms into Chinese prose or adding unnecessary Chinese glosses to English prose.

For a Simplified Chinese deliverable:

- write natural Simplified Chinese throughout;
- translate ordinary operating terms such as `owner`, `listing`, `best-fit`, `proof`, `offer`, `qualified entry`, `retained value`, `taxonomy`, `lineage`, `source-to-value`, `cohort`, `guardrail`, `contribution`, `consent`, `hook`, `cluster`, `gate`, `pilot`, `dry run`, `stop rule`, and `recovery`;
- use Chinese labels for the visible mode and evidence state, while retaining required machine tokens or IDs only in code formatting when traceability requires them;
- introduce a standard acronym with its Chinese name on first use, such as “客户获取成本（CAC）”, then use the acronym consistently only when it improves readability;
- retain proper product, company, platform, protocol, file, code, formula, URL, and quoted source names where translation would be inaccurate.

For an English deliverable, write complete idiomatic English and do not add Chinese translations except for proper nouns or quoted source text that must remain in the original language. If a source term needs explanation, translate it once in prose rather than alternating languages throughout the report. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables.

## Freeze The Acquisition Contract

Record customer and account unit, ICP or best-fit hypothesis, problem, intent, trigger, alternatives, promise, proof, offer, channel family and mechanism, source taxonomy, market, language, locale, device, platform, campaign or partner version, entry surface and state; eligible audience, qualified exposure or response, arrival, identity, deduplication, new-versus-returning status, activation, retained value, revenue and contribution; attribution rule, counterfactual, interference, cohort start, windows, cutoff, maturity, source latency, and product version; media, creative, agency, incentive, tool, sales, partner, implementation, support, fraud, refund, discount, and operating costs; capacity, cash, payback, saturation, fatigue, dependency, cannibalization, trust, policy, privacy, risk, owners, sources, evidence states, and requested external actions.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may be a `reported signal` with no evidence state. Keep visibility, attribution, prediction, reconciliation, incrementality, and scenario assumptions separate.

## Diagnose The Source-To-Value Path

Use this chain:

```text
customer problem and intent
-> qualified reachable demand
-> promise, proof, and offer
-> distribution mechanism
-> entry surface and qualified arrival
-> first value and retained value
-> incremental contribution and reinvestment
```

Find the first decision-relevant break without assigning cause from a funnel drop alone. Preserve alternatives such as wrong audience, weak intent, poor positioning, misleading proof, offer friction, source overlap, broken destination state, product-value failure, immature cohorts, fraud, attribution error, cost omission, capacity, saturation, or market mismatch. Product behavior is acquisition-quality evidence even when another team owns the surface.

## Select Channels From Mechanism And Model Fit

Classify the actual mechanism and external dependency, not just its label. Compare organic discovery, earned, owned, paid, product-led, partner, sales-led, and portfolio distribution on:

- objective and decision horizon;
- customer access, intent, and credible reach;
- format, promise, proof, offer, and product-path fit;
- retained contribution, acceptable acquisition cost, payback, cash, and service load;
- time to start and time to mature evidence;
- control, auditability, capacity, saturation, decay, and reversibility;
- data, platform, partner, policy, rights, bargaining, switching, and recovery risk;
- internal capability, maintenance, support, and local-market ownership.

When evidence is weak, select one or two hypotheses that can be tested deeply through retained value rather than spreading shallow activity across many channels. A high-ACV channel can still fail when contribution, churn, sales time, implementation, support, cash, or capacity cannot fund it. Route pricing and packaging changes to `monetization`.

## Separate Attribution From Incrementality

Use platform, first-touch, last-touch, multi-touch, partner-code, and journey models as operational views within their declared rules. Reconcile identities, eligible population, new and returning state, duplicated contacts, view-throughs, organic demand, source changes, and company totals before comparing them.

Incrementality governs causal allocation. Prefer a mechanism-compatible randomized, geographic, switchback, phased, shutdown, threshold, matched, or time-series design with explicit assumptions, contamination, interference, power, maturity, guardrails, and decision rules. Do not sum channel-reported conversions or label attributed revenue incremental. Route statistical design and readout to `experiment-design`.

## Use Full, Marginal, Retained Economics

Keep these calculations distinct:

```text
full acquisition cost = media + creative + agency + incentive + tools
                      + variable sales + partner + onboarding + support
                      + fraud + other decision-relevant operating cost

incremental CAC = incremental acquisition cost / incremental customers

net retained incremental contribution
  = retained contribution caused by acquisition - full incremental acquisition cost
```

State currency, tax treatment, time basis, entity, cost scope, contribution definition, source, maturity, and exclusions. Do not call cost per click, attributed signup, platform conversion, or reconciled new customer incremental CAC. Prevent double counting when contribution already includes refunds, discounts, cost of goods, service, or other deductions.

Use marginal evidence for the next allocation. Historical average CAC or ROAS cannot justify scaling when the next spend band has worse quality, payback, contribution, reach, fatigue, or risk. Cap, redesign, test, reallocate, or stop when marginal retained incremental contribution fails the declared boundary.

## Build A Portfolio Whose Mechanisms Fail Differently

For each channel or spend band, compare eligible remaining demand, marginal retained incremental contribution, full cost, evidence, maturity, capacity, dependencies, concentration, interaction, reversibility, risk, uncertainty, learning value, and strategic control. Return allocation scenarios and gates, not false precision or live budget changes.

Channel count is not diversification. Several placements, agencies, creators, or tactics can share one identity, auction, platform, content format, partner, measurement layer, or policy failure. Map the underlying mechanism and external owner. A second mechanism reduces risk only when it reaches qualified demand with materially different dependencies and can be operated economically.

## Treat Scale As A Gate, Not A Cure

Use narrow manual or low-cost “kindle” work to identify a retained best-fit segment and understand the distribution mechanism. Move to repeatable “fire” only after customer fit, first value, retention, contribution, channel behavior, capacity, quality, and controls are credible. A launch, broad access, automation, or publicity cannot create Product-Market Fit.

For every scale, market, or channel expansion, define eligible audience, exposure cap, evidence horizon, activation and retention maturity, economics, capacity, guardrails, decision rule, stop rule, recovery, maintenance, and next expansion layer. Do not extrapolate early response as a constant.

## Route Specialist Work

Route primary constraint selection to `growth-diagnosis`; customer and segment evidence to `customer-research` and `icp-segmentation`; positioning to `positioning`; campaign briefs and asset plans to `campaign-planning`; creative systems to `ad-creative`; pages to `landing-page-audit`; paid account diagnosis to the relevant ad-audit Skill; search, GEO, app-store, programmatic page, structured-data, site, and content execution to their specialist Skills; source instrumentation to `tracking-plan`; cohort construction to `cohort-analysis`; activation and retention work to `activation` and `retention`; referral and product-loop mechanics to `referral-program-design` and `growth-loop-design`; metrics to `growth-metrics-design`; experiments to `experiment-design`; economics, pricing, and packaging to `monetization`; and shared acquisition infrastructure to `growth-infrastructure-assessment`.

This Skill owns the acquisition contract, source-to-value diagnosis, channel hypothesis and model fit, portfolio and concentration analysis, attribution-versus-incrementality boundary, full and marginal economics, saturation and dependency decisions, market-entry sequence, and evidence-gated scale or stop plan. It does not create specialist deliverables or operate channels.

## Deliver In Order

Return:

1. mode, decision, owner, customer, problem, qualified entry, market, horizon, budget or capacity, and action boundary;
2. acquisition contract, evidence ledger, and source taxonomy;
3. source-to-value path and first constrained transition with alternatives;
4. channel-mechanism and channel-model-fit comparison;
5. attribution, identity, cohort, incrementality, and quality ledger;
6. full and marginal economics with formulas, assumptions, and uncertainty;
7. portfolio, concentration, dependency, market, and capacity scenarios;
8. staged validation, allocation gates, stop and recovery rules, handoffs, and pinned Playbook sources.

For China work, keep market, language, locale, customer, product, channel, platform, device, app distribution, search, social, creator, partner, content supply, identity, consent, attribution, payment, invoice, currency, data, policy, applicable review, and operating ownership separate. Do not infer any platform, provider, payment, consent, regulatory, access, or customer condition from translation or geography alone.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not access ad, analytics, warehouse, CRM, billing, app-store, search, social, email, partner, finance, product, identity, experimentation, or cloud systems; export production or customer data; enrich or upload audiences; contact prospects, creators, partners, customers, or vendors; change bids, budgets, targeting, offers, prices, pages, campaigns, permissions, tracking, contracts, or product state; launch a test or market; publish; send; spend; procure; deploy; or claim the strategy is live without separate task-level authorization and required controls.

## Completion Gate

Confirm that the decision, customer, intent, mechanism, source taxonomy, qualified entry, promise, proof, offer, destination, identity, new-versus-returning state, activation, retention, contribution, attribution, counterfactual, cohort, maturity, full cost, marginal economics, payback, capacity, saturation, fatigue, dependency, concentration, cannibalization, risk, market context, evidence states, scale and stop gates, specialist handoffs, pinned sources, privacy boundary, and external-action limit are explicit; incompatible sources and cohorts were not combined; activity was not called value; attribution was not called incrementality; channel count was not called diversification; no universal ranking, budget, or benchmark was invented; and no external action occurred.
