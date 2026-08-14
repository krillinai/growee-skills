---
name: engagement-analysis
description: Use when a team needs to define, calculate, audit, compare, or diagnose product engagement distributions; analyze value-bearing activity frequency, depth, breadth, concentration, active-day distributions, Power User Curves, L7 or L30, DAU, WAU, MAU, stickiness, feature or workflow adoption, opportunity-adjusted usage, or engagement-to-outcome associations across consumer, B2B, collaborative, marketplace, AI, or low-frequency products without accessing live systems.
---

# Engagement Analysis

Analyze how a declared eligible population performs value-bearing activity inside a compatible opportunity and observation window. Preserve the full distribution, including zero use, instead of turning volume, averages, or a small power-user group into customer value, retention, Product-Market Fit, causality, or business impact.

## Read The Contract

Read [engagement-contract.md](references/engagement-contract.md) before accepting an active event, entity, eligible population, opportunity, window, identity, source, or evidence state. Read [frequency-depth-and-breadth.md](references/frequency-depth-and-breadth.md) before calculating Power User Curves, L7 or L30, stickiness, bucket bounds, depth, breadth, concentration, or comparisons. Read [interpretation-and-diagnosis.md](references/interpretation-and-diagnosis.md) before interpreting product topology, later outcomes, mechanisms, predictions, PMF, or interventions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Define a calculation-ready engagement, event, query, or aggregate-table contract when compatible data is unavailable |
| `analysis` | Build and interpret one canonical engagement distribution from supplied compatible data |
| `comparison` | Compare compatible periods, segments, cohorts, products, versions, roles, workflows, or marketplace sides |
| `audit` | Inspect an existing engagement definition, dashboard, distribution, comparison, score, or decision for validity and missing evidence |

Name one primary mode. Keep metric specification, observed distribution, comparison, candidate mechanism, prediction, intervention, and causal effect visibly separate.

## Return One Verdict

| Verdict | Gate |
| --- | --- |
| `decision-ready` | Contract, sources, maturity, reconciliation, quality, privacy, and decision rule are compatible |
| `descriptive-only` | The observed distribution is usable, but its mechanism or downstream value remains unresolved |
| `partially specified` | Material entity, eligibility, event, opportunity, identity, quality, maturity, source, or comparison fields are unresolved |
| `not decision-useful` | The measure represents incompatible entities, access, volume, burden, or activity rather than the declared value |

Choose exactly one verdict for the analysis in scope. A familiar metric, complete-looking dashboard, large sample, executive request, or high-activity band does not make an analysis decision-ready.

## Freeze The Engagement Contract

Freeze every field required by [engagement-contract.md](references/engagement-contract.md), including decision, entity, eligibility, zero state, value and quality, opportunity, dimensions, source, identity, time, maturity, market, privacy, and action boundary. Use only its evidence states and preserve missing, zero, late, immature, censored, suppressed, deleted, unknown, failed, and not applicable separately. If the calculation gate fails, return `specification` rather than synthetic behavior.

Respond in the user's requested language; use Simplified Chinese when requested.

## Build A Zero-Inclusive Distribution

Reconcile the full eligible population into zero-use and mutually exclusive observed buckets. Use successful value, show counts and shares, label active-only views, preserve aggregate bounds, and calculate DAU, WAU, MAU, ratios, or Power User Curves only from compatible contracts. Follow [frequency-depth-and-breadth.md](references/frequency-depth-and-breadth.md); never replace the distribution with a score or universal daily threshold.

## Separate Engagement Dimensions

Keep frequency, depth, breadth, intensity, duration, quality, reliability, burden, commercial state, and downstream outcomes separate. Volume can coexist with failure, rework, mandatory use, fatigue, shelfware, or declining value. Preserve eligibility through retained-value states and never infer health from a heavy-use tail.

## Compare And Interpret Conservatively

Compare only compatible contracts, keep canonical totals beside predeclared cuts, and separate mix from within-group change. Use [interpretation-and-diagnosis.md](references/interpretation-and-diagnosis.md) for topology, alternatives, downstream outcomes, prediction, and causal limits. Engagement records behavior inside a boundary; it does not establish mechanism, benefit, retention, PMF, or intervention effect.

## Route Specialist Work

This Skill owns the engagement contract, zero-inclusive distribution, supported engagement dimensions, compatible comparisons, bounded interpretation, and next-evidence plan. Route adjacent artifacts without recreating them:

| Need | Route |
| --- | --- |
| Metric system, event implementation, or decision-critical source defects | `growth-measurement` |
| Time-, exposure-, behavior-, or state-based cohort construction | `retention` |
| First value, recurring value, churn, resurrection, or customer expansion | `activation`, `retention`, `customer-expansion-strategy` |
| B2B access, lifecycle, account, commercial, or renewal reconciliation | `growth-operations` |
| Journey transitions, funnel constraints, or company-wide primary constraint | `product-market-fit-assessment`, `growth-diagnosis` |
| Causal effect, forecast, Product-Market Fit, plan, unit economics, network liquidity, or lifecycle message | `growth-measurement`, `product-market-fit-assessment`, `growth-operations`, `monetization`, `growth-loop-design`, `lifecycle-marketing` |

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Include one verdict, the contract and ledgers, zero-inclusive distribution or specification, supported dimensions and comparisons, interpretation and causal boundary, handoffs, pinned sources, external actions, and completion. Treat every market as a new evidence boundary; for China, separate market, language, locale, timezone, entities, product, platforms, identity, payments, data, consent, support, and local ownership.

Do not copy US event definitions, Google or Meta identities, app-store sources, workweeks, cadence, benchmarks, account hierarchies, consent, or targets into China. Revalidate local product value, participant roles, opportunities, sources, events, maturity, privacy, and review with current direct evidence and accountable local owners; translation and currency conversion do not establish measurement equivalence.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated systems, export or join customer data, mutate events or operations, rank or contact people or accounts, send, launch, publish, spend, deploy, or claim improvement without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the full output contract; zeroes and buckets reconcile; definitions and comparisons are compatible; aggregate limits remain visible; activity does not become value, retention, PMF, causality, or impact; no benchmark, score, target, holdout, duration, authorization, or result is invented; and no external action occurred.
