---
name: growth-accounting
description: Use when a team needs to reconcile, audit, compare, or diagnose period-to-period customer, account, activity, subscription, recurring-revenue, gross-profit, or contribution movements; distinguish retained, new, resurrected, churned, expanded, and contracted states; calculate logo or value retention; explain growth mix without confusing decomposition with attribution, causality, forecasts, or targets.
---

# Growth Accounting

Reconcile how a defined customer or value base moved from one period to the next. Freeze entity, eligibility, identity, period, maturity, and value basis before classifying movement; a balanced bridge describes what changed, not why it changed or who caused it.

Read [accounting-contract.md](references/accounting-contract.md) before accepting inputs. Read [classification-and-equations.md](references/classification-and-equations.md) before assigning movement classes or calculating a bridge. Read [diagnosis-and-interpretation.md](references/diagnosis-and-interpretation.md) before interpreting mix, quality, concentration, or possible constraints. Read [governance-and-boundaries.md](references/governance-and-boundaries.md) before using personal data, transferring a method across markets, routing specialist work, or preparing external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `reconcile` | Build a reproducible entity, activity, or recurring-value bridge from supplied compatible evidence |
| `diagnose` | Audit definitions, classifications, reconciliation, mix, and movement quality and identify the smallest unresolved evidence |
| `portfolio` | Compare and reconcile compatible bridges across products, cohorts, segments, markets, periods, or value bases |

Name one primary mode, decision, owner, entity and level, active or value state, opening and closing periods, observation and maturity windows, product, segment, cohort, market, value basis, currency, as-of date, source versions, review date, and external-action boundary. Public sources can verify visible products, prices, releases, and historical public events. They cannot establish private active populations, movement classes, retention, revenue, contribution, cash, attribution, or causes.

## Freeze The Accounting Contract

Record person, user, seat, workspace, account, payer, legal customer, contract, subscription, order, transaction, and marketplace-participant hierarchy; eligibility and active or recurring-value state; identity, duplicate, merge, split, transfer, guest, deletion, and unknown rules; entry, lapse, grace, dormancy, reactivation, resurrection, cancellation, churn, refund, reversal, and finalization; period, frequency, timezone, cutoff, observation opportunity, lookback, maturity, censoring, and late data; product, plan, price, segment, cohort, market, channel, platform, version, acquisition, and migration; activity, logo, booking, billing, cash, recognized revenue, gross profit, contribution, and recurring-value bases; currency, exchange-rate policy, tax, discount, credit, refund, FX, acquisition, reclassification, and other adjustments; sources, lineage, evidence states, reconciliation, privacy, owners, and requested actions.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. An attributable unsupported statement is a `reported signal`, not a fifth evidence state. Keep zero, missing, late, immature, censored, suppressed, deleted, corrected, and not-applicable states distinct.

## Classify Mutually Exclusive Movement

Apply a declared precedence so one entity has one movement class for one bridge:

| Class | Required meaning |
| --- | --- |
| `retained` | Eligible and active on compatible opening and closing states |
| `new` | First-ever qualified entry during the closing period with sufficient prior history |
| `resurrected` | Qualified return after the declared inactive or churned interval |
| `churned` | Eligible opening entity that crosses the declared mature inactive or terminated state |
| `unresolved` | Prior history, identity, maturity, or observation is insufficient for a valid class |

Use `reactivated` separately when the product distinguishes a short lapse from resurrection. A first observed record is not necessarily new. Do not classify an immature or late outcome as churned, assign the same entity to new and resurrected, or hide transfers and migrations inside behavioral movement.

For recurring value, classify `new`, `resurrection`, `expansion`, `contraction`, and `churn` against one opening value and accounting basis. Keep retained opening value, current retained value, one-time value, usage value, recurring value, bookings, invoices, cash, recognized revenue, gross profit, and contribution separate.

## Build And Reconcile The Bridge

For a compatible active-entity bridge, verify:

```text
opening active = retained + churned + declared opening adjustments
closing active = retained + new + resurrected + declared closing adjustments
net change = new + resurrected - churned + net declared adjustments
```

For a compatible recurring-value bridge, verify:

```text
closing recurring value
= opening recurring value
+ new value + resurrection value + expansion value
- contraction value - churned value
+ FX + acquisitions + migrations + reclassifications + other declared adjustments
```

Show residuals. Do not force equality, rewrite history, double-count ending retained value, average percentages across different denominators, or combine currencies and accounting bases without an explicit conversion and reconciliation layer.

Calculate rates only when their population, numerator, denominator, value basis, window, maturity, and exclusions are explicit. Keep logo retention, gross value retention, net value retention, churn, resurrection, quick-ratio-style summaries, net growth, and contribution movement separate. Do not select denominators to improve presentation or invent universal healthy thresholds.

## Diagnose Without Overclaiming

Begin with absolute movements and reconciliation, then compare rates. Separate:

- base-size effect from rate change;
- acquisition or entry mix from within-cohort movement;
- product, price, plan, segment, market, and channel mix from local behavior;
- broad movement from concentration in a few accounts or events;
- operational movement from FX, acquisitions, migrations, reclassifications, and accounting timing;
- observed decomposition from attribution, incrementality, intervention effect, and cause.

Rank possible constraints only when compatible evidence distinguishes them. Otherwise preserve alternatives and request the smallest evidence that would change a decision. A release preceding expansion, a campaign preceding lower churn, or a last touch attached to a new customer is not causal proof.

## Compare Portfolios Carefully

Build local bridges before portfolio totals. Align entity, eligibility, active state, identity, period, observation opportunity, maturity, product and price version, cohort, segment, market, currency, value basis, source, and adjustment policy. Show component weights, absolute movements, rates, mix contribution, concentration, residuals, and segment reversals.

Use reported- and constant-currency views when FX matters. Separate organic movement from acquired populations, customer migration from new or resurrected behavior, and chart or definition changes from operational growth. Do not rank unlike businesses by one net-growth percentage.

## Route Specialist Work

This Skill owns movement definitions, mutual exclusivity, opening-to-closing bridges, numerator and denominator contracts, reconciliation, mix decomposition, concentration, compatible comparison, and refresh governance. Route metric-system design to `growth-measurement`; cohort construction and age comparisons to `retention`; recurring-value, churn, and resurrection mechanisms to `retention`; full business stocks, flows, loops, and constraints to `growth-model-design`; acquisition credit to `growth-measurement`; channel portfolios and budget allocation to `acquisition-strategy`; causal intervention validation to `growth-measurement`; future movement outlooks to `growth-measurement`; LTV to `monetization`; and pipeline, booking, invoice, revenue, and cash reconciliation to `growth-operations`.

Specialist outputs become accounting inputs only when entity, version, period, maturity, market, value basis, evidence state, and owner remain compatible.

## Deliver In Order

Return:

1. mode, decision, owner, scope, periods, as-of, source versions, review date, and action boundary;
2. entity, identity, state, period, maturity, value, adjustment, source, and evidence contracts;
3. mutually exclusive classification table with unresolved states and QA;
4. opening-to-closing entity and value bridges with formulas, absolute movements, rates, and residuals;
5. cohort, segment, product, market, channel, version, mix, concentration, and portfolio views where compatible;
6. observed findings, counterevidence, alternative explanations, and the smallest discriminating next evidence;
7. governance, refresh, revision, privacy, market-transfer, and specialist handoffs;
8. pinned Playbook sources, approval-ready external actions, and completion record.

For China work, keep market, language, customer and payer entities, product, contract, plan, price, payment, invoice, tax, refund, currency, channel, platform, attribution, identity, data, consent, storage, transfer, source access, dormancy, accounting, review, and local owner separate. Translation and currency conversion do not validate a transferred accounting model. Use current direct sources and locally accountable review for time-sensitive conditions; do not provide legal, tax, accounting, regulatory, or provider conclusions.

## External-Action Boundary

Create and read local artifacts only. Do not access analytics, warehouse, CRM, billing, payment, finance, product, ad, support, BI, or cloud systems; export, merge, or reidentify people; rewrite historical states; change identity, lifecycle labels, customer records, dashboards, forecasts, targets, budgets, routing, campaigns, prices, or products; contact anyone; publish; send; spend; deploy; or claim growth improvement without separate task-level authorization and required controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, owner, entity, eligibility, active and value states, identity, periods, frequency, timezone, observation, lookback, maturity, censoring, late data, product, version, cohort, segment, market, currency, accounting basis, sources, evidence, retained, new, resurrected, churned, expansion, contraction, adjustments, formulas, numerators, denominators, opening, closing, residuals, mix, concentration, revisions, privacy, market transfer, handoffs, pinned sources, and external actions are explicit; movement classes are mutually exclusive; incomplete history did not become new; missing or immature did not become zero or churn; incompatible populations and values were not combined; accounting did not become attribution or causality; unsupported targets, benchmarks, scores, and precision were not invented; and no external action occurred.
