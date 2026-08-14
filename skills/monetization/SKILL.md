---
name: monetization
description: Use when work needs to design and audit monetization across offers, pricing, packaging, LTV, CAC, unit economics, payback, migration, and customer protection.
---

# Monetization & Economics

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Pricing & Packaging Strategy](references/modules/pricing-and-packaging-strategy/SKILL.md)
- [LTV Analysis](references/modules/ltv-analysis/SKILL.md)
- [Unit Economics Analysis](references/modules/unit-economics-analysis/SKILL.md)

Connect delivered customer value to a buyer, payer, offer, package, price metric, revenue model, and sustainable economics. Work from supplied data or attributable public context. Private billing, product, CRM, finance, support, sales, research, or cost data is optional; mark missing or declined inputs `unavailable`, never as failure.

Read [monetization-contract.md](references/monetization-contract.md) for intake, participant roles, evidence, metric contracts, privacy, and output requirements. Read [economics-methods.md](references/economics-methods.md) before calculating or comparing conversion, realized price, margins, CAC, payback, LTV, GRR, NRR, or take rate. Read [diagnosis-and-design.md](references/diagnosis-and-design.md) for mechanism diagnosis, offers, packaging, price metrics, revenue models, experiments, migration, and handoffs. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `analysis` | Define or calculate monetization metrics, participant economics, paid conversion, retained revenue, or unit economics |
| `diagnosis` | Explain an observed monetization symptom through bounded value, participant, offer, package, price, payment, retention, cost, trust, or measurement hypotheses |
| `design` | Design an offer, package, price metric, revenue model, commercial rule, or validation plan for a supported mechanism and segment |

Name one primary mode. A request may include secondary work, but keep calculations, hypotheses, and commercial designs visibly separate.

## Freeze The Monetization Contract

Record the customer segment and job; user, beneficiary, champion, administrator, buyer, approver, and payer where relevant; delivered and perceived value; alternatives and purchase constraints; offer, package, entitlements, limits, price metric, price, currency, billing frequency, commitment, discounts, taxes, fees, payment method, refund and cancellation rules; qualified exposure, conversion event, cohort, window, cutoff, and maturity; revenue and cost basis; market, language, locale, and timezone; source artifacts; owner; and decision the work must support.

Do not substitute signup, feature use, checkout start, invoice creation, bookings, cash collection, list price, or contract status for healthy monetization unless the declared decision and evidence support that measure. Keep user value, payer value, product use, revenue, cash, and contribution separate.

## Apply Evidence Before Calculation

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder-only statement may use signal status `reported signal` with a blank evidence state.

Calculate only from supplied attributable populations, definitions, amounts, currencies, periods, cohorts, cost boundaries, contract rules, timestamps, and maturity status. Preserve refunds, credits, discounts, free periods, taxes, payment loss, implementation, support, and other declared adjustments. If data is missing or definitions conflict, produce a measurement specification and the smallest evidence request instead of a number.

Never invent willingness to pay, price elasticity, conversion, revenue, margin, CAC, payback, LTV, retention, expansion, costs, benchmarks, causal effects, or commercial results. Stated willingness, visible pricing, bookings, and observational conversion can nominate a mechanism; they cannot establish durable customer value or causal impact.

## Diagnose The Monetization System

Separate the observed symptom from candidate mechanisms. Examine customer outcome and alternatives, participant and payer alignment, segment needs, offer comprehension, package boundaries, price metric, price level and terms, free or trial design, procurement, payment, discounts and exceptions, activation, retained use, expansion and contraction, cost to serve, margin, trust, fairness, migration, and measurement quality.

Name a primary mechanism only when evidence distinguishes it. Otherwise preserve alternatives and make the discriminating evidence or test the next action. Keep user, account, product, payer, transaction, recurring revenue, cash, gross margin, and contribution views separate.

## Design Commercial Changes

Tie every design to a named mechanism, eligible segment, participant roles, customer value, offer and package, price metric and terms, exposure rule, measurement window, migration rule, guardrails, owner, and decision rule. Prefer the simplest commercial architecture that customers can understand and the business can bill, support, govern, and measure.

Do not optimize pricing-page or checkout conversion in isolation. Read activation, paid conversion, realized price, retained use, refunds, churn, contraction, expansion, support, trust, margin, payback, and renewal together. Preserve original exposure, eligibility, commercial terms, and cohort through downstream validation.

This Skill may specify offer claims, pricing-page content requirements, sales proof, or lifecycle-message eligibility, but it does not draft or send copy. Route page and offer copy to `copywriting`, lifecycle messages to `lifecycle-marketing`, one-to-one sales outreach to `sales-enablement`, broader constraint selection to `growth-diagnosis`, first-value analysis to `activation`, recurring-value and revenue-retention analysis to `retention`, and causal validation to an experiment-design capability when needed.

## Deliver In Order

Return:

1. mode and decision boundary;
2. monetization contract and participant map;
3. evidence and data-quality ledger;
4. calculations or measurement specification;
5. value, offer, conversion, retention, and economics findings;
6. bounded mechanisms and alternatives;
7. commercial design or analysis priorities;
8. validation, migration, governance, owner, and handoffs;
9. Playbook references and external-action boundary.

For China work, keep market, language, locale, product surface, currency, invoice and tax context, identity, app distribution, payment method, channel, contract, and data availability separate. Do not infer WeChat Pay, Alipay, app-store billing, invoicing, tax, messaging, procurement, compliance, or data conditions from the market or language.

Analysis and design authorize local artifacts only. Do not access accounts, query production systems, read or write billing, CRM, payment, finance, or customer records, change prices, packages, entitlements, metering, contracts, discounts, credits, taxes, invoices, payment routing, refunds, campaigns, or product configuration, launch experiments, publish, send messages, or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that segment, customer job, participant roles, value, offer, package, metric, price, currency, commercial terms, exposure, conversion event, cohort, window, revenue basis, cost basis, and maturity are explicit; calculations preserve adjustments and compatible denominators; list price, bookings, revenue, cash, and contribution are not conflated; user and payer value remain visible; causal language follows evidence; designs include migration, fairness, retention, and economic guardrails; missing data remains visible; Playbook sources are pinned; and no external action occurred.
