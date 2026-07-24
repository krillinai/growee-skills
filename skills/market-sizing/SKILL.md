---
name: market-sizing
description: Use when a team needs to build, audit, compare, reconcile, refresh, or govern a market size, demand pool, value pool, TAM, SAM, SOM, serviceable market, reachable demand, qualified demand, attainable-share scenario, category estimate, or market portfolio; define customer, buyer, payer, usage, transaction, geographic, time, source, overlap, frequency, value, capacity, uncertainty, and market-transfer boundaries without changing live systems.
---

# Market Sizing

Estimate a bounded demand and economic opportunity from explicit customer, job, geography, time, eligibility, frequency, value, serviceability, reachability, overlap, and evidence contracts. Treat TAM, SAM, and SOM as labels only after their definitions are frozen; a market size is a versioned decision model, not a fact that exists independently of units and assumptions.

Read [market-contract.md](references/market-contract.md) before accepting population, customer, category, demand, price, spend, transaction, or share evidence. Read [methods-and-reconciliation.md](references/methods-and-reconciliation.md) before using top-down, bottom-up, supply, transaction, value-pool, or observed-demand methods. Read [uncertainty-and-scenarios.md](references/uncertainty-and-scenarios.md) before combining sources, returning ranges, estimating attainable share, comparing markets, or refreshing estimates. Read [decisions-and-governance.md](references/decisions-and-governance.md) before connecting size to segments, positioning, price, entry, acquisition, forecasts, privacy, or market transfer. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Inspect an existing market definition, source, model, TAM/SAM/SOM, share, growth, confidence, or decision claim |
| `build` | Create a bounded market estimate or calculation-ready specification from supplied compatible evidence |
| `portfolio` | Compare and reconcile market, segment, geography, category, product, or scenario estimates under one decision |

Name one primary mode, decision, owner, market unit, customer and economic units, customer job and trigger, product boundary, geography, time period, currency and value basis, source cutoff, model version, review date, and external-action boundary. Public sources can verify published population, company, category, product, price, transaction, and estimate claims within their stated method and date. They cannot establish complete demand, customer eligibility, willingness to change or pay, realized price, reachability, company share, private outcomes, incrementality, or causality.

## Freeze The Market Contract

Record market, category, job, problem, trigger, alternative, product, service, bundle, platform, version, geography, language, locale, industry, segment, channel, time, season, and exclusions; beneficiary, person, household, employee, user, seat, device, workspace, organization, account, buyer, payer, contract, subscription, order, transaction, seller, supplier, and legal-entity hierarchy; population, need, opportunity, use, purchase, payment, retention, frequency, quantity, value, list price, realized price, spend, GMV, revenue, contribution, cash, currency, tax, accounting, serviceability, reachability, qualification, adoption, share, capacity, overlap, source, method, uncertainty, owner, and requested action.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A publisher, analyst, customer, vendor, or stakeholder statement without inspectable support may be a `reported signal` with no evidence state. Preserve zero, missing, inaccessible, stale, derivative, disputed, suppressed, estimated, forecast, and not-applicable states separately.

## Define Market Layers Before Naming Them

Use descriptive layers, then map to organizational labels if needed:

```text
bounded universe
-> demand with the defined job, trigger, and opportunity
-> demand serviceable by the current product and operating system
-> demand reachable through available channels and permissions
-> qualified demand with fit, readiness, and viable economics
-> attainable scenario under explicit time, capacity, competition, and execution assumptions
```

`TAM`, `SAM`, and `SOM` have no universal formulas. Record exactly which layer, entity, value basis, geography, period, and assumptions each label represents. Keep current estimate, conditional scenario, target, company plan, company forecast, and observed actual separate.

## Keep Customer, Demand, And Money Units Compatible

Do not add people, households, employees, seats, devices, organizations, subscriptions, orders, and transactions as customers. Define beneficiary, user, buyer, payer, account, and billing hierarchy. One person can create several demand opportunities; one organization can include many users; one purchase can cover several seats; one transaction can include multiple items.

Define natural demand opportunity, use, purchase, payment, repeat, retention, quantity, price metric, value basis, and period. Keep list, quoted, negotiated, promotional, legacy, and realized price separate. Keep spend, bookings, GMV, gross revenue, net revenue, gross profit, contribution, and cash separate. Do not multiply a broad population by list price or add overlapping value layers.

## Build With Several Evidence Views

Use:

- `top-down`: published populations, categories, spend, production, or revenue narrowed by compatible filters;
- `bottom-up`: eligible entities multiplied by bounded opportunity frequency, quantity, and compatible value;
- `supply-side`: current providers, capacity, locations, inventory, labor, production, or fulfillment;
- `transaction-side`: orders, payments, units, contracts, renewals, or usage under explicit coverage;
- `value-pool`: economic cost, savings, risk, or value available to participants without assuming capture;
- `observed demand`: searches, requests, waitlists, pipeline, purchases, alternatives, or usage with source and selection limits.

Every method must expose source lineage, entity, scope, year, coverage, conversion bridge, exclusions, overlap, assumptions, and uncertainty. Triangulation is agreement among compatible independent views, not averaging every number. Repeated citations of one report are one lineage.

## Bound Serviceability And Reachability

Serviceable demand requires current product and operating support: capability, version, language, locale, device, integration, accessibility, trust, security, payment, contract, implementation, support, fulfillment, capacity, data, and accountable market review where relevant. A roadmap does not make demand currently serviceable.

Reachable demand requires an available mechanism and permission, not platform audience size. Map addressable or eligible audience, targetability, identity, available reach, exposure, response, qualified entry, customer value, saturation, overlap, dependency, and cost. Route channel evidence and economics to `acquisition-strategy`.

## Handle Overlap And Market Structure

Map mutually exclusive, nested, overlapping, substitute, complementary, multi-product, multi-market, and unknown demand. Preserve source coverage gaps, duplicates, inactive entities, multiple roles, cross-border activity, multi-homing, and internal versus external spend. Do not add software, services, internal labor, adjacent categories, and transaction value without an explicit nonoverlap or value-chain model.

For marketplaces and networks, separate sides, participant roles, atomic geography or category, availability, demand, matching, fulfillment, quality, multi-homing, transaction, take rate, incentives, refunds, cost, and contribution. GMV is not platform revenue; buyers plus sellers are not one customer count.

## Return Ranges And Attainable Scenarios

Use point estimates only with uncertainty and sensitivity appropriate to the evidence. Report ranges, method-specific views, and reconciled bounds. Expose which assumptions change the result and which source gaps dominate uncertainty. Do not assign a precise confidence percentage without a calibrated basis.

Attainable share is a conditional scenario, not a universal percentage. Define product fit, customer readiness, current alternatives, switching, distribution, price, capacity, capital, competition, regulation, trust, timing, retention, unit economics, and execution assumptions. State observable triggers and counterevidence. Do not choose the market definition or share required to satisfy a target.

## Route Specialist Work

This Skill owns the market contract, market layers, demand and economic units, universe and exclusions, source lineage, sizing methods, conversion bridges, overlap, serviceability, reachability, attainable scenarios, uncertainty, reconciliation, comparison, and refresh governance. Route segment and ICP definitions to `icp-segmentation`; prevalence and customer research to `customer-research`; competitors and alternatives to `competitive-intelligence`; category and positioning to `positioning`; pricing, willingness-to-pay, and economics to `monetization`; market readiness and entry to `market-entry-strategy`; channel reach and capture to `acquisition-strategy`; company forecasts to `growth-forecasting`; full business topology to `growth-model-design`; and causal effects to `experiment-design`.

Specialist evidence may enter the sizing model only with its entity, population, method, market, period, version, uncertainty, and limitations. Market size does not approve entry, product, price, budget, staffing, fundraising claims, or customer action.

## Deliver In Order

Return:

1. mode, decision, owner, market, customer and economic units, job, product, geography, period, currency, value basis, cutoff, version, review date, and action boundary;
2. market contract, source and lineage ledger, evidence states, definitions, coverage, contradictions, and unavailable inputs;
3. bounded universe, total demand, serviceable, reachable, qualified, and attainable layers with inclusion, exclusion, and overlap;
4. top-down, bottom-up, supply, transaction, value-pool, and observed-demand methods used, with equations and assumptions;
5. entity, frequency, quantity, price, spend, GMV, revenue, contribution, currency, and accounting reconciliation;
6. method-specific estimates, ranges, uncertainty, sensitivity, source dependence, and reconciliation residuals;
7. attainable scenarios, triggers, counterevidence, decision thresholds, owners, and specialist handoffs;
8. privacy, market transfer, refresh and expiry, pinned Playbook sources, approval-ready external actions, and completion record.

For China work, keep market, language, locale, customer, role, job, category, product and version, competitor and alternative, channel, platform, app distribution, price, payment, tax, invoice, currency, exchange rate, frequency, data, identity, consent, storage, transfer, source access, serviceability, reachability, model, review, and local owner separate. Do not transfer a US market model through translation or currency conversion alone, and do not provide legal, tax, accounting, or provider conclusions.

## External-Action Boundary

This Skill may read supplied artifacts and public or otherwise authorized sources when the task and tools allow it, and may create local artifacts. Do not access analytics, CRM, billing, payments, finance, product, app-store, ad, marketplace, government, partner, customer, competitor, paid research, or private systems; bypass controls or licenses; export or reidentify people; buy reports; contact customers, competitors, analysts, partners, or authorities; change market definitions, ICPs, prices, forecasts, targets, plans, budgets, staffing, dashboards, or production data; publish; send; spend; deploy; or claim market or business growth without separate task-level authorization and required controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, owner, market, category, job, product, geography, time, customer and payer entities, demand opportunity, eligibility, frequency, quantity, value, price, spend, GMV, revenue, contribution, currency, accounting, total, serviceable, reachable, qualified, attainable, sources, lineage, methods, conversion bridges, overlap, coverage, exclusions, uncertainty, scenarios, sensitivity, calibration, privacy, market transfer, handoffs, pinned sources, and external actions are explicit; entities were not added as customers; population was not multiplied by list price; derivative sources were not independent; platform audience was not reachable demand; roadmap was not availability; GMV was not revenue; scenario was not forecast; target did not determine size; market size was not called causal; unsupported precision was not invented; and no unauthorized action occurred.
