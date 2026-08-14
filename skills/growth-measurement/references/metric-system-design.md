# Metric System Design

Build the smallest system that can support the declared decision. Start from customer value and a durable outcome, not the metrics already available in a dashboard.

## Metric Roles

Assign one primary role per metric for the declared objective:

| Role | Purpose | Common failure |
| --- | --- | --- |
| `outcome` | Judge whether a durable customer or business result occurred | Replacing the result with activity or exposure |
| `north-star-candidate` | Candidate shared measure of delivered customer value with a sustainable business connection | Treating one familiar company-wide KPI as mandatory |
| `input` | Behavior or operating condition a team can plausibly influence in the decision horizon | Calling a correlated input causal |
| `guardrail` | Protect quality, trust, fairness, safety, risk, cost, capacity, or downstream value | Hiding harm behind aggregate success |
| `diagnostic` | Explain, segment, locate, or monitor movement | Treating the diagnostic as success itself |
| `business-health` | Protect revenue quality, contribution, cash, payback, capacity, or sustainability | Treating gross revenue as customer value or profit |

A metric may serve another role under another objective. State the objective and do not assign several primary roles to avoid making a choice.

## North Star Candidate Gate

A North Star Metric is optional. A candidate must pass all of these tests:

1. **Value:** represents a meaningful outcome received by a qualified customer, not mere activity or platform exposure.
2. **Durability:** connects to recurring or retained value at an appropriate natural interval.
3. **Business connection:** has a plausible and bounded relationship to sustainable economics.
4. **Controllability:** decomposes into inputs teams can influence without gaming the outcome.
5. **Coverage:** applies to the declared product, customer, market, and maturity scope without erasing critical sides or segments.
6. **Quality resistance:** cannot improve simply through spam, low-quality volume, coercion, subsidy, fraud, overuse, or cost transfer.
7. **Measurability:** has a reproducible contract, stable identity, observable maturity, and inspectable lineage.

Reject the candidate when a material test fails. Recommend an outcome plus inputs, guardrails, diagnostics, and business-health system instead. Do not force one metric across products, markets, lifecycle stages, or business units with materially different value mechanics.

Revenue, GMV, DAU, MAU, traffic, signups, messages, seats, content volume, prompts, tokens, generated outputs, and transactions may be useful metrics. None is automatically a North Star.

## Metric Constellation

Start with:

```text
durable outcome
|-- north-star candidate, only if it passes the gate
|-- controllable input hypotheses
|-- guardrails and business health
`-- diagnostic cuts and quality checks
```

Keep the constellation small enough to assign owners and decision rules. Retain metrics only when they change diagnosis, prioritization, validation, or governance. Preserve opposing dimensions separately rather than averaging away a tradeoff.

Examples of necessary balance include conversion with refunds and retained value; engagement with quality, safety, and fatigue; marketplace demand with local liquidity and side-specific retention; revenue with contribution, cash, and capacity; model usage with accepted outcomes, error, safety, latency, and cost.

## Metric Tree Relationships

Label every edge exactly once:

| Relationship | Use |
| --- | --- |
| `arithmetic identity` | Mutually exclusive and exhaustive components reproduce the parent by definition |
| `hypothesized driver` | A named mechanism is plausible, but causal evidence is unavailable |
| `observed association` | Compatible evidence shows co-movement without a credible counterfactual |
| `causal evidence` | A credible counterfactual supports an effect in the declared population, exposure, and horizon |
| `tradeoff` | Movement may harm another outcome, risk, cost, trust, fairness, or capacity dimension |

Rules:

- Arithmetic decomposition never proves what to change.
- An input remains a hypothesis until evidence supports its relationship to the outcome.
- Causal evidence must name assignment or identification, exposure, population, estimate, uncertainty, maturity, interference, and limitations.
- Association must preserve alternatives such as selection, mix, seasonality, instrumentation, concurrent changes, and reverse causality.
- Tradeoffs remain visible beside the optimized metric.
- Do not connect every available metric. An unlabeled or non-decision-useful edge should be removed.

## Context-Specific Tests

### B2B And Multi-User Products

Separate user, team, workspace, account, buyer, payer, contract, and revenue. Define whether value is individual, collaborative, administrative, or organizational. Preserve adoption depth, account coverage, buying committee, renewal horizon, and revenue maturity. Do not use active users to claim account retention or expansion.

### Marketplaces And Networks

Name the local or functional network unit. Separate supply, available supply, demand, requests, matches, completions, quality, repeat use, contribution, congestion, and multi-homing. Global users can hide weak local liquidity. Aggregate scale does not prove a network effect.

### AI Products

Prompts, tokens, sessions, generated outputs, and model calls measure activity or cost unless qualified value is established. Prefer accepted or completed customer outcomes with quality, correction, safety, latency, cost, retention, and human-override guardrails. Keep offline model metrics separate from online customer value.

### Low-Frequency And Assisted Products

Use natural opportunity windows and eligible opportunities rather than forcing daily activity. Separate product, sales, service, partner, and customer contributions. Do not penalize successful low-frequency value or credit a channel for outcomes it did not cause.

## Targets And Benchmarks

A target requires a metric version, owner, baseline, population, segment, market, date, business rationale, capacity, downside, guardrails, and review rule. A target does not prove the underlying relationship.

An external benchmark requires comparable entity, formula, denominator, product topology, market, stage, channel, maturity, economics, and source. If those fields are unavailable, label the benchmark contextual or reject it. Never invent a North Star target, conversion rate, retention rate, CAC, ROAS, LTV/CAC, payback, K-factor, marketplace density, or experiment threshold.

## Observation, Prediction, Attribution, And Causality

Keep these separate:

- **Observed outcome:** matured event or value under a reproducible contract.
- **Prediction:** model estimate with training population, features, target, horizon, calibration, uncertainty, segment error, and drift.
- **Attribution credit:** result assigned under a declared identity, overlap, and credit rule.
- **Association:** compatible co-movement without a counterfactual.
- **Causal effect:** estimate supported by a credible counterfactual in a bounded scope.

A model score does not replace the observed outcome used to validate it. Platform attribution does not establish incrementality. A statistically significant result does not eliminate practical, guardrail, maturity, or external-validity review.
