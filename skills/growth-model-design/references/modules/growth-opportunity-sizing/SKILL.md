---
name: growth-opportunity-sizing
description: Use when a team needs to size, audit, compare, or refresh growth opportunities across acquisition, activation, retention, monetization, referral, expansion, products, segments, markets, channels, or growth systems; translate baselines, eligible populations, transition gaps, reach, adoption, retained value, economics, overlap, capacity, risk, and uncertainty into decision-ready ranges; or distinguish opportunity headroom from market size, targets, forecasts, causal impact, plans, and realized growth.
---

# Growth Opportunity Sizing

Turn a growth idea or observed gap into a traceable range that a decision owner can accept, reject, preserve, or send for evidence. Size theoretical headroom, reachable change, retained customer value, and net economic value separately. Do not manufacture uplift, convert a target into evidence, or present a double-counted portfolio total.

Read [opportunity-contract.md](references/opportunity-contract.md) before accepting the decision, entity, outcome, baseline, population, period, market, or evidence. Read [sizing-methods.md](references/sizing-methods.md) before calculating lifecycle, demand, monetization, expansion, loop, or system opportunities. Read [overlap-and-portfolio.md](references/overlap-and-portfolio.md) before comparing or adding opportunities. Read [validation-and-governance.md](references/validation-and-governance.md) before defining validation, privacy, market transfer, ownership, review, or external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `size` | Build a new evidence-bounded range for one opportunity |
| `compare` | Compare multiple compatible opportunities and expose overlap, capacity, risk, and evidence needs |
| `audit` | Reproduce and challenge an existing estimate from its original evidence and as-of date |
| `refresh` | Version an estimate after material evidence, scope, market, cost, capacity, or mechanism change |

Name one primary mode. Route external market demand to `market-sizing`, current constraint selection to `growth-diagnosis`, mechanism equations to `growth-model-design`, time-indexed projections to `growth-measurement`, medium-term portfolio choices to `growth-strategy`, and the approval case for one bounded resource commitment to `growth-operations`. Opportunity sizing can supply an input range to those decisions; it does not replace them or constitute an investment case.

## Freeze The Opportunity Contract

Record the decision, accountable owner, as-of date, horizon, scope and exclusions, product and business model, market and locale, customer and participant entities, segments, current stage, customer outcome, business value unit, baseline, eligible population, evidence cutoff, source access, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Keep actual, reported signal, estimate, benchmark, causal estimate, scenario, forecast, target, plan, approval, and result distinct. Preserve source, date, version, entity, definition, segment, market, period, currency, accounting basis, maturity, limitations, contradictions, and lineage.

Do not invent baselines, rates, benchmarks, reach, adoption, uplift, elasticity, incrementality, retention, LTV, contribution, costs, overlap, capacity, probabilities, confidence scores, approvals, or results. Do not blend incompatible customers, participants, lifecycle states, denominators, markets, currencies, periods, accounting bases, or outcomes.

## Draw The Opportunity Chain

For each opportunity map:

```text
eligible population
  x current or missing value transition
  x bounded reachable change
  x adoption and delivery
  x repeated or retained value
  x compatible value per retained outcome
  - incremental and recurring cost
  = conditional net opportunity range
```

Use only factors supported by compatible evidence. Replace multiplication with a state model, cohort model, cash-flow model, or explicit handoff when the mechanism is not multiplicative. Never apply a percentage to a population that was not eligible for the source rate.

Keep four layers visible:

1. **Observed baseline or loss:** what happened under a frozen contract.
2. **Theoretical headroom:** the mathematical gap before reach, causality, or feasibility.
3. **Reachable retained opportunity:** the bounded change that could reach eligible customers and persist.
4. **Net decision value:** retained value minus incremental, recurring, risk, and opportunity costs on a compatible basis.

An observed gap is not a cause. A benchmark is not an attainable counterfactual. A market is not reachable demand. Attributed outcomes are not automatically incremental. Gross revenue is not contribution or cash.

## Build Conditional Ranges

Use low, central, and high cases only when their assumptions are explicit and internally coherent. Name conditions rather than implying calibrated probability. Show the calculation, source, uncertainty, sensitivity, failure signal, and next decision-changing evidence for every material factor.

Bound change using attributable internal variation, compatible cohorts, validated experiments, operational limits, credible external evidence, or a transparent assumption. If no defensible bound exists, return `unavailable` and size the evidence decision instead of inventing a number. Never backsolve assumptions to hit a target.

Include time to evidence, time to customer value, ramp, maturity, duration, decay, saturation, reversibility, and cash timing where they change the decision. Route detailed unit economics and LTV work to `monetization`.

## Reconcile Overlap And Interaction

Map shared customers, accounts, cohorts, transitions, channels, products, mechanisms, costs, capabilities, and outcome units before adding opportunities. Separate:

- mutually exclusive alternatives;
- upstream causes and downstream consequences;
- independent opportunities;
- overlapping populations or value;
- cannibalization and substitution;
- reinforcing or constraining interactions;
- shared capacity, cost, concentration, and risk.

Report gross opportunity, attributable overlap adjustment, adjusted portfolio range, and unresolved overlap separately. Do not apply an arbitrary discount or add every opportunity as independent. Sequence evidence where interaction prevents a credible portfolio estimate.

## Compare Without False Precision

Compare compatible opportunities on customer value, retained outcome, net economics, evidence coverage, sensitivity, time to evidence, time to value, capacity, dependencies, reversibility, downside, trust, and opportunity cost. Do not fabricate RICE, ICE, confidence, impact, or effort scores or collapse unlike outcomes into one unsupported number.

Classify each opportunity as `advance`, `validate`, `preserve`, `defer`, `reject`, or `route`. State the reason, owner, evidence gate, expiry, scale or stop condition, and what would change the class. The largest gross range is not automatically the best choice or the company strategy.

## Validate Before Commitment

Match evidence strength to cost, irreversibility, customer exposure, and downside. Use `growth-measurement` for causal tests, `growth-measurement` for instrumentation, `retention` for maturity-aware groups, and relevant lifecycle or channel Skills for specialist diagnosis and design.

Define the smallest evidence that distinguishes material alternatives. Preserve negative, flat, harmful, contradictory, and delayed results. Version the original estimate and as-of evidence; do not rewrite assumptions with hindsight. Sunk cost is not future opportunity value.

## Handle Markets, People, And Data

Treat every market as a new evidence boundary. Revalidate customers, eligibility, baseline, alternatives, reach, product and channel availability, value, pricing, payments, invoices, costs, capacity, trust, data, regulation, and local ownership. Translation and currency conversion do not validate transfer.

For China, distinguish market, legal entity, language, locale, product, platform, app distribution, identity, payment, invoice, data, content, advertising, support, and locally accountable review. Use current direct sources and local expertise. Do not make legal, tax, regulatory, provider-availability, accounting, or performance conclusions.

Use aggregate, redacted, pseudonymous, minimum-necessary evidence by default. Do not request credentials, private messages, payment details, health data, protected traits, precise locations, raw identity, or full histories when bounded aggregates suffice. Do not rank or target individuals for consequential pricing, employment, credit, insurance, health, housing, or similar decisions.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the decision contract; evidence and source ledger; opportunity chains; traceable calculations and conditional ranges; economics and sensitivity; overlap-aware portfolio view; classification and evidence plan; specialist handoffs; pinned sources; external actions; and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated analytics, CRM, advertising, billing, finance, product, cloud, sales, support, research, experiment, or data systems; export or join personal data; change budgets, prices, products, infrastructure, permissions, contracts, or records; launch tests; contact people; publish; spend; deploy; or claim implementation or realized growth without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the output passes [output-contract.md](references/output-contract.md), every material input has an evidence state and compatible contract, gross headroom remains separate from reachable retained and net value, uncertainty and sensitivity are visible, portfolio overlap is reconciled or unresolved, specialist work is routed, market and privacy boundaries hold, and no external action occurred.
