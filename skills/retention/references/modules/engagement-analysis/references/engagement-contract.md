# Engagement Contract

## Freeze The Decision

Start with the decision, not DAU, MAU, a dashboard, or a preferred target. Record:

| Field | Required boundary |
| --- | --- |
| Decision | Exact choice, owner, alternatives, date, consequence, and evidence threshold |
| Customer value | Job, successful outcome, beneficiary, quality, failure, burden, and guardrails |
| Engagement use | Description, comparison, diagnosis input, prediction input, intervention measurement, or governance |
| Evidence | Supplied source, version, cutoff, evidence state, access, contradiction, and limitation |

Keep metric specification, observed activity, inferred value, association, prediction, intervention, causal effect, target, forecast, plan, decision, action, and outcome separate. Do not make one Engagement Score or arbitrary health threshold from incompatible dimensions.

## Entity And Hierarchy

Name one canonical analysis entity. Preserve device, visitor, person, user, role, seat, team, workspace, account, parent account, company, contract, subscription, transaction, market, and revenue as distinct entities. Define keys, joins, cardinality, precedence, shared identity, anonymous-to-known mapping, merges, splits, re-entry, deletion, bots, service accounts, test traffic, and unknown joins.

For linked B2B views, define each transition separately:

`purchased -> provisioned -> invited -> accessed -> attempted -> successful first value -> repeated value -> retained value -> commercial outcome`

Do not add states with different denominators into one adoption rate. A provisioned seat, invitation, login, contract, or invoice is access or commercial state, not value by default. Return user, workspace, and account views only when each reconciles under explicit joins.

For marketplaces, preserve participant side, role, listing or supply unit, request, match, transaction, fulfillment, cancellation, local network, and participant economics. For AI products, preserve user, workspace, session, prompt, model call, task, output, accepted result, successful workflow, cost, and commercial entity.

## Eligibility, Zero, And Opportunity

Define the eligible population and why every included entity had a relevant chance to receive value. Record entry, exit, exclusions, churn, deletion, suppression, unknown identity, product access, role, market, plan, lifecycle, and observation eligibility.

The canonical denominator includes every eligible entity, including zero qualifying activity. Preserve:

- verified zero after complete observation;
- no verified opportunity;
- missing or late data;
- immature or censored observation;
- unknown identity or eligibility;
- suppressed or deleted data;
- failed attempt;
- not applicable.

These states are not interchangeable. Do not turn missing, future, late, unavailable, no-opportunity, deleted, or suppressed data into zero. An active-only view is a secondary conditional distribution and cannot replace the eligible denominator.

Define the natural opportunity from the customer job: day, week, billing cycle, trip, filing event, project, order, shift, workflow, renewal, or another evidenced occasion. For episodic products, measure qualifying actions per verified opportunity and distinguish absence of opportunity from failure to act. Do not impose daily use on annual, seasonal, low-frequency, or need-based products.

## Value Event And Dimensions

Specify the active value event with event ID and version, entity, eligibility, prerequisite, successful outcome, quality rule, reversal, deduplication, failure, and guardrails. A login, open, click, session, prompt, token, output, status refresh, support ticket, invitation, seat, contract, or revenue is not value unless supplied evidence validates that relationship.

Define dimensions independently:

| Dimension | Meaning |
| --- | --- |
| Frequency | Number of distinct opportunities or intervals with qualifying value |
| Depth | Successful value volume or complexity inside an opportunity |
| Breadth | Distinct eligible workflows, roles, teams, or products reaching defined value states |
| Intensity | Event or resource volume, retained only as a diagnostic unless tied to value |
| Duration | Time observed, not value by itself |
| Quality | Success, accuracy, reliability, completion, acceptance, or customer outcome |
| Concentration | How entities or value contribution are distributed across the eligible population |

Keep retries, errors, rework, mandatory use, idle time, accidental opens, failure loops, and support activity separate from successful value.

## Source, Identity, And Time Contract

Record source system, table or event, owner, fields, extraction version, cutoff, freshness, lineage, event version, identity version, product version, market, timezone, calendar, observation window, opportunity window, maturation rule, late-arrival allowance, censoring, deletion, and known incidents.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. An attributable stakeholder statement without inspectable support may remain a `reported signal` with no evidence state. Public pages, pricing, app-store listings, customer logos, social activity, traffic estimates, screenshots, and jobs cannot establish private engagement.

## Accepted Input Shapes

| Input | Supported output |
| --- | --- |
| Entity-level opportunity or event rows | Reconciled distributions and supported dimensions after contract and quality checks |
| Exact active-day or opportunity count per entity | Exact frequency distribution and Power User Curve |
| Exact mutually exclusive buckets including zero | Bucket counts, shares, and mathematically valid bounds |
| DAU, WAU, or MAU aggregates | Compatible scale and ratio summaries only; no entity-level curve or exact active days |
| Incompatible or incomplete aggregates | Specification, reconciliation gap, and bounded unavailable results |

For a calculation-ready aggregate request, specify dimensions such as:

```text
entity_id or privacy-safe group
eligibility_state and eligible_opportunities
qualifying_value_count and distinct_qualifying_intervals
depth, breadth, success, failure, retry, burden, and guardrail fields
market, product, version, role, cohort, window, cutoff, timezone, and maturity
source, event version, identity version, quality state, and suppression
```

Request only fields that can change the decision or validity. Prefer approved aggregate tables when row-level personal data is unnecessary.

## Privacy And Governance

Use aggregate, redacted, pseudonymous, minimum-necessary evidence and suppress unsafe small cells. Record purpose, authority, consent or accountable basis, access, retention, deletion, correction, audit, downstream use, fairness, accessibility, dissent, appeal, and independent review.

Do not ingest private messages, support transcripts, precise location, health, financial, protected-trait, employee-note, or full-history data merely to enrich engagement. Do not score or rank named people for engagement, addiction, churn, value, compliance, pricing, service, employment, or another consequential decision.
