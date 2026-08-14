# Frequency, Depth, Breadth, And Concentration

## Calculation Gate

Before arithmetic, verify one compatible entity, eligibility rule, zero state, value event, natural opportunity, identity, source, event version, window, cutoff, timezone, latency, maturity, quality rule, and privacy threshold. If a gate fails, preserve supplied values separately and return a specification or `partially specified` verdict.

Do not divide devices by accounts, users by companies, sessions by contracts, or activity from one event version by another. Do not compare incomplete future exposure with a mature window or fill late and censored observations with zero.

## Build The Canonical Distribution

Assign every eligible entity to one mutually exclusive frequency value or exact bucket under the frozen rule. Include a zero-use bucket. Reconcile:

```text
eligible N
= verified zero N
 + sum(observed mutually exclusive bucket N)
 + unresolved missing, immature, censored, unknown, suppressed, or deleted N
```

Report counts and shares together:

```text
bucket share = bucket N / eligible N
```

Do not remove zeroes, failed attempts, churned entities, deleted records, or unknown identities solely to improve the distribution. If privacy or source rules prevent inclusion, expose the state and reconciliation residual. Label an active-only distribution `conditional on at least one qualifying event`.

## Power User Curves And Active-Day Distributions

A Power User Curve requires a fixed observation window and exact qualifying active-day or opportunity count for every eligible entity, or exact mutually exclusive counts for every possible value including zero. Plot count or share by exact frequency without smoothing.

DAU, WAU, and MAU aggregates cannot reconstruct an entity-level curve. Calculate ratios only when numerator and denominator share entity, active-event, identity, source, timezone, product, market, and compatible nested windows:

```text
DAU / MAU = compatible daily active entities / compatible monthly active entities
WAU / MAU = compatible weekly active entities / compatible monthly active entities
```

These are aggregate stickiness ratios, not exact average active days, retention, or a distribution. Keep total eligible population, active population, commercial penetration, frequency, and scale separate.

Use L7, L30, active days, or similar labels only with an exact definition: entity, qualifying event, lookback or fixed window, cutoff, timezone, eligibility, and whether zeroes are included. Never transfer a universal healthy daily threshold from another product.

## Work With Exact Buckets

Preserve supplied bucket boundaries. For bucket `[lower_i, upper_i]` with count `n_i`, supported total-frequency bounds are:

```text
lower total = sum(n_i * lower_i)
upper total = sum(n_i * upper_i)
lower mean  = lower total / reconciled eligible N
upper mean  = upper total / reconciled eligible N
```

Include a verified zero bucket in the eligible denominator. Report an exact mean only when exact within-bucket values are supplied. A median or percentile may be located within a bucket when cumulative counts support it, but its exact value remains unavailable. Exact Gini, variance, tail concentration, day-level curve, and smooth shape require sufficient entity-level or exact-frequency data.

Do not choose convenient within-bucket values, interpolate observations, assume uniformity, or draw a smooth curve. Request exact entity frequencies or finer exact buckets when the decision needs unavailable statistics.

## Opportunity-Adjusted Frequency

For need-based or episodic work, preserve opportunity:

```text
opportunity-adjusted engagement
= eligible opportunities with qualifying value
 / verified eligible opportunities
```

Also show entities and opportunity-count distributions so frequent opportunity does not masquerade as better customer behavior. Record how an opportunity is detected and what remains unobserved. A person with no tax filing, trip, order need, shift, or project opportunity is not a failed daily user.

## Measure Depth And Quality

Define the successful unit before measuring depth: completed jobs, accepted outputs, fulfilled orders, resolved cases, useful collaborations, or another evidenced outcome. Report distribution, not only average volume. Keep attempts, retries, errors, abandoned tasks, reversals, rework, time, cost, latency, and support burden visible.

More prompts, tokens, model calls, generated outputs, files, clicks, time, or sessions can indicate complexity, failure, cost, or idle use. For AI, require eligible task, accepted or successful result, quality, correction, human review, hallucination or error, latency, cost, reliability, trust, abandonment, and repeated workflow evidence. Retain raw volume as diagnostics only.

## Measure Breadth And Adoption States

For every feature, workflow, role, team, or product, distinguish:

`eligible -> available -> exposed -> attempted -> successful first value -> repeated value -> retained value`

Visibility, enablement, click, accidental open, and access do not establish adoption. Useful breadth depends on customer job, role, product scope, and value; requiring every customer to use the same feature count creates shelfware and burden.

Keep breadth separate from frequency, depth, quality, and retained value. Preserve plan, tenure, role, account size, customer fit, selection, and reverse causality when breadth is associated with later outcomes. Route customer-scope expansion to `customer-expansion-strategy`.

## Measure Concentration

State the population and contribution basis: entities, successful jobs, value units, revenue, cost, or another declared measure. Report zeroes and negative or failed contribution where applicable. A small heavy-use tail can coexist with weak broad value, concentration risk, mandatory use, abuse, or cost concentration.

Do not infer product health from a Gini coefficient, top-decile share, or power-user band alone. Require compatible counts, quality, downstream outcomes, and guardrails. Do not calculate exact concentration from coarse buckets unless only defensible bounds are reported.

## Compare Compatible Distributions

Freeze entity, eligibility, zero state, event, opportunity, bucket rules, identity, source, window length, cutoff, timezone, latency, maturity, product, market, and version. Keep a canonical total beside predeclared segment, cohort, role, or product cuts and preserve unknown groups.

When definitions change, create an overlap bridge, dual-run, restatement, or separate series. Decompose observed movement into population mix and within-group change when supported. Do not call an incompatible or immature difference a trend or attribute it to a release; route unexpected changes to `growth-diagnosis`, source defects to `tracking-plan`, and causal questions to `experiment-design`.
