---
name: go-to-market-strategy
description: Use when work needs to design and govern go-to-market systems and product launches across audience, offer, motion, readiness, exposure, value, measurement, and scale gates.
---

# Go-to-Market & Launch

## Reuse Growee Context

At the start, read `.agents/growee-context.md` when it exists. Reuse only product, customer, market, outcome, constraint, evidence, and routing fields whose scope, definition, source, and date remain compatible; state what is reused and surface conflicts or staleness before asking for decision-changing gaps. The file grants no system access or execution authority, and this Skill must not silently rewrite the primary diagnosis.

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Product Launch Strategy](references/modules/product-launch-strategy/SKILL.md)

Turn one defined product-market unit into a repeatable system connecting customer value, buying roles, positioning, proof, offer, motion, routes, first and repeated value, delivery, measurement, retained economics, and an evidence-gated expansion decision. GTM is not a campaign calendar, launch announcement, sales target, channel list, or theoretical market share.

Read [gtm-contract.md](references/gtm-contract.md) before accepting products, customers, markets, motions, routes, or outcomes. Read [readiness-and-motion.md](references/readiness-and-motion.md) before assigning readiness or choosing self-serve, product-led, sales-assisted, sales-led, partner, marketplace, community, or hybrid motions. Read [routes-and-sequencing.md](references/routes-and-sequencing.md) before selecting a beachhead, channel portfolio, sales path, pilot, initiative order, or expansion. Read [measurement-economics-and-governance.md](references/measurement-economics-and-governance.md) before defining funnels, cohorts, economics, causal evidence, targets, governance, privacy, market transfer, or actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Diagnose an existing GTM motion, plan, readiness claim, route, funnel, handoff, economics, or outcome |
| `design` | Build one evidence-bounded GTM system for a defined product-market unit and decision |
| `portfolio` | Compare and sequence segments, markets, offers, motions, routes, or GTM initiatives under one capacity boundary |

Name one primary mode, decision, owner, product and offer version, customer and buying unit, initial segment, market, buying situation, motion, horizon, evidence cutoff, review date, and external-action boundary. Public pages and announcements can verify visible products, offers, prices, claims, channels, releases, and historical public events. They cannot establish private customers, demand, pipeline, conversion, retention, economics, capacity, incrementality, readiness, or Product-Market Fit.

## Freeze The GTM Contract

Record product, workflow, API, service, offer, package, price, contract, and version; customer job, trigger, segment, exclusions, alternatives, switching cost, proof, and unmet risk; beneficiary, user, champion, administrator, buyer, approver, procurement, legal, security, finance, payer, partner, implementer, support, and success roles; market, language, locale, legal entity, channel, platform, route, motion, partner, campaign, sales path, and handoffs; eligibility, intent, source, identity, permission, access, exposure, activation, first value, repeated value, retention, purchase, renewal, expansion, contraction, churn, referral, and support states; product, positioning, commercial, distribution, delivery, data, measurement, economics, capacity, trust, safety, privacy, governance, evidence, owners, approvals, and requested actions.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. An attributable unsupported statement may be a `reported signal` without an evidence state. Keep public signal, supplied fact, observation, attribution, causal estimate, forecast, scenario, target, plan, benchmark, approval, zero, missing, immature, censored, and suppressed states separate.

## Define One Product-Market Unit

Use the smallest unit whose customer, value, offer, buying process, motion, delivery, economics, and decision can be described coherently:

```text
product and offer version
+ customer and buying unit
+ job, trigger, alternatives, and value
+ segment and market
+ motion and routes
+ delivery and retained outcome
= GTM unit
```

Split units when products, APIs, services, migrations, customer roles, prices, markets, routes, sales cycles, implementation, risk, or economics differ materially. A portfolio may coordinate units, but each keeps its own evidence, readiness, capacity, measurement, owner, stop, rollback, and retirement.

Route customer discovery to `customer-research`, ICP and positioning work to `positioning`, market estimates to `market-sizing`, entry into new regions or verticals to `growth-strategy`, Product-Market Fit to `product-market-fit-assessment`, and pricing to `monetization`.

## Audit Readiness In Dependency Order

Evaluate six independent gates:

1. `customer and problem`: bounded customer and buying unit, trigger, job, alternatives, urgency, evidence, exclusions, and willingness to change;
2. `position and offer`: differentiated value, proof, category and language, participant-specific narrative, offer, package, price, terms, trust, and objection handling;
3. `product and value`: availability, prerequisites, reliability, security, privacy, accessibility, onboarding, first and repeated value, retention, limitations, and failure recovery;
4. `motion and routes`: buying complexity, self-serve or sales path, channel-model fit, intent, destination, partner role, creative, sales stages, overlap, dependency, and saturation;
5. `delivery and operations`: implementation, provisioning, billing, payment, contracts, support, success, inventory, fulfillment, moderation, incidents, capacity, rollback, and ownership;
6. `measurement and economics`: entities, events, identity, cohorts, maturity, attribution, incrementality, revenue, contribution, cash, CAC, LTV, payback, uncertainty, guardrails, and decision rules.

Use `verified ready`, `bounded pilot only`, `specified not verified`, `verified blocker`, `unavailable`, or `not applicable` for each gate. Unavailable is not failed. Do not average away a blocker or create an opaque readiness score.

## Select A Motion From Fit

Compare self-serve, product-led, sales-assisted, sales-led, partner-led, marketplace, community-led, developer-led, and hybrid motions through customer intent, time to value, product complexity, trialability, collaboration, buyer and payer roles, procurement, security, integration, implementation, contract value, frequency, service, support, capacity, economics, and feedback speed.

One company can use several motions only with explicit segment, offer, ownership, handoff, conflict, attribution, customer, and economic boundaries. Do not choose product-led growth because it appears cheap, add sales because deal size is high, or add partners to replace missing direct customer value. Define the smallest motion that can prove the next decision.

## Build The Full Value And Buying Path

Preserve states:

```text
qualified problem or demand signal
-> reachable eligible customer and buying group
-> coherent positioning, proof, and offer exposure
-> qualified response, self-serve entry, or buying milestone
-> product access and first customer value
-> repeated value at the natural interval
-> purchase, renewal, retained contribution, and advocacy or expansion
-> next segment, route, offer, or scale decision
```

Attention is not reachability. A lead, demo, signup, feature enablement, purchase, or contract is not customer value. First value is not retention. Bookings are not cash. Attributed revenue is not incrementality. One channel, partner, sales rep, or large account is not repeatability.

Map buying roles and milestones, qualification and disqualification, proof, security and procurement, commercial negotiation, implementation, promise handoff, adoption, success, renewal, and expansion. Route seller and buyer assets to `sales-enablement`, pipeline and commercial controls to `growth-operations`, first value to `activation`, and recurring value to `retention`.

## Sequence A Bounded GTM Pilot

Choose the narrowest product, customer, offer, route, market, and operating unit that can distinguish the current hypothesis. Define prerequisites, non-goals, initial cohort, access, route, positioning and proof, offer, delivery, measurement, economics, capacity, owner, decision horizon, positive, negative, harmful, and inconclusive outcomes, stop, rollback, and expiry.

Sequence upstream uncertainty before downstream scale:

```text
customer and alternative evidence
-> positioning, proof, and offer comprehension
-> product access and first value
-> repeated value and delivery reliability
-> route repeatability and buying progression
-> retained contribution and operating stability
-> adjacent segment, route, market, or offer
```

Do not launch all channels, markets, or motions at once. Every expansion spends customer attention and operating capacity. Scale only when the next step adds a declared learning or viable repeatable path.

## Measure Compatible Outcomes

Freeze entity, eligibility, identity, source, product and offer version, market, route, assignment or access, exposure, cohort, window, maturity, cutoff, currency, value basis, and exclusions. Report counts beside rates. Keep attention, qualified demand, access, exposure, response, buying milestone, first value, repeated value, retention, purchase, revenue, contribution, cash, support, trust, and harm separate.

Use actuals, forecasts, targets, plans, and benchmarks separately. Never backsolve leads, conversion, price, retention, spend, or capacity to reach a target. Route metric design to `growth-measurement`, instrumentation to `growth-measurement`, funnel analysis to `growth-diagnosis`, cohorts to `retention`, attribution to `growth-measurement`, economics to `monetization`, and outlooks to `growth-measurement`.

Observed before-after movement can nominate a mechanism, not prove it. Preserve product, offer, price, message, channel, partner, sales, market, seasonality, mix, selection, attribution, and concurrent changes. Route causal validation to `growth-measurement`.

## Coordinate, Do Not Absorb, Specialist Work

This Skill owns the GTM unit, readiness gates, motion choice, route and buying-path orchestration, dependency sequence, pilot, cross-functional handoffs, portfolio comparison, and expansion or stop decision. It consumes specialist outputs only when their customer, segment, product, market, version, period, evidence state, uncertainty, and owner remain compatible.

Route launch units and audience ladders to `go-to-market-strategy`; channel portfolio, budget decisions, and campaigns to `acquisition-strategy`; partners and communities to `partnership-marketing`; customer proof to `content-strategy`; seller workflows to `sales-enablement`; sales systems and infrastructure to `growth-operations`; and decision rights and capacity portfolios to `growth-operations`.

## Deliver In Order

Return:

1. mode, decision, owner, GTM unit, segment, market, motion, horizon, cutoff, review date, and action boundary;
2. product, customer, buying group, problem, alternative, value, position, proof, offer, route, delivery, evidence, and owner contract;
3. six-gate readiness matrix with first blocking dependency, counterevidence, and unavailable inputs;
4. motion comparison and selected bounded path with explicit rejected alternatives, conflicts, dependencies, and handoffs;
5. end-to-end customer, buying, product-value, delivery, measurement, and economic state map;
6. beachhead and pilot sequence with prerequisites, caps, cohorts, owners, positive, negative, harmful, inconclusive, stop, rollback, and expiry;
7. measurement, retained economics, uncertainty, target and forecast separation, portfolio, and next-scale decision;
8. specialist handoffs, privacy, market transfer, governance, pinned Playbook sources, approval-ready actions, and completion record.

For China work, keep market, language, locale, legal entity, customer and payer, product and offer, position, price, motion, channel, platform, app distribution, payment, invoice, tax, contract, identity, consent, data, storage, transfer, support, content review, advertising, measurement, economics, source access, review, and local owner separate. Translation and currency conversion do not validate transferred GTM. Use current direct sources and locally accountable review; do not provide legal, tax, accounting, regulatory, or provider conclusions.

## External-Action Boundary

Create and read local artifacts only. Do not access product, analytics, warehouse, CRM, billing, payment, finance, ad, social, app-store, support, sales, partner, experiment, identity, BI, or cloud systems; export, join, or reidentify people; change product access, pages, offers, prices, packages, contracts, tracking, routing, budgets, forecasts, targets, customer records, or systems; contact anyone; launch campaigns or pilots; publish; send; spend; deploy; or claim GTM or business improvement without separate task-level authorization and required controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, owner, product and offer version, customer and buying unit, job, trigger, alternatives, segment, market, participant roles, positioning, proof, package, price, motion, routes, buying milestones, access, exposure, first and repeated value, delivery, support, capacity, readiness gates, entities, identity, cohorts, maturity, attribution, incrementality, economics, uncertainty, pilot, owners, dependencies, positive, negative, harmful, inconclusive, stop, rollback, expansion, privacy, market transfer, handoffs, pinned sources, and external actions are explicit; TAM is not reachability; attention is not value; leads are not customers; bookings are not cash; first value is not retention; attribution is not causality; launch is not GTM repeatability; targets are not evidence; unavailable is not failure; unsupported precision, readiness, Product-Market Fit, approvals, and results were not invented; and no external action occurred.
