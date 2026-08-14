# Benchmark Contract And Reference Classes

## Benchmark Question

Start with a decision that a comparison could inform. Record:

| Field | Required boundary |
| --- | --- |
| Decision | Choice, owner, alternatives, date, consequence, and evidence threshold |
| Focal unit | Organization, product, market, segment, cohort, channel, team, or another explicit unit |
| Focal metric | Exact version, customer or business meaning, entity, population, formula, source, period, and maturity |
| Comparison use | Context, gap, range, risk, planning input, diagnostic input, or monitoring |
| Excluded uses | Target, forecast, causal proof, ranking, compensation, or another unsupported use |

One benchmark question must state `compared with whom, on what, as of when, and for which decision`. If any element is missing, return `specification` mode rather than searching for a convenient number.

## Metric And Evidence Contract

Record benchmark ID; focal and reference metric IDs and versions; entity and level; eligibility and exclusions; numerator, denominator, formula, aggregation, rounding, and unit; value or outcome meaning; start, exposure, qualifying, reversal, and censoring states; identity and joins; source type and owner; product, offer, plan, segment, cohort, market, channel, and platform; observation and maturity windows; cutoff, timezone, calendar, latency, and revisions; currency, tax, accounting, refund, and cost basis; distribution, sample, weighting, uncertainty, and privacy; effective date, review, expiry, corrections, and consumers.

Use exactly:

- `verified`: inspectable evidence supports the claim in the declared scope;
- `inferred`: a bounded interpretation follows from named evidence but remains unverified;
- `unavailable`: necessary evidence is absent, inaccessible, stale, or incompatible;
- `not applicable`: the field does not apply and the reason is explicit.

An attributable claim without inspectable support may be a `reported signal` with no evidence state. Do not silently upgrade it because a publisher is familiar or many articles repeat it.

## Reference-Class Contract

Define membership before examining the outcome:

| Dimension | Examples to declare |
| --- | --- |
| Customer and job | Consumer, SMB, enterprise, buyer, user, payer, participant side, use case, natural opportunity |
| Product topology | Habit, episodic, B2B, collaborative, marketplace, network, transaction, subscription, AI, portfolio |
| Business system | Revenue model, price level, gross or net basis, sales motion, channel, service intensity, unit economics |
| Stage and scale | Launch stage, age, customers, revenue, employees, geography, maturity, capacity |
| Market and period | Country, locale, legal entity, currency, calendar, structural regime, contemporaneous membership |
| Metric readiness | Compatible definitions, sources, cohort age, finalization, quality, distribution, uncertainty |

State inclusion, exclusion, unknown, and missing rules. Freeze class version, selector, selection date, rationale, affected decision, and sensitivity alternatives. Preserve companies or units that failed, closed, were acquired, became inactive, remain private, do not disclose, or cannot be classified.

Do not select famous winners, current survivors, vendor customers, favorable cases, or outcome-disclosing units and call them peers. For historical questions, use class membership knowable at that historical point or label survivor-conditioned views explicitly.

## Reference-Class Types

| Type | Defensible use | Main boundary |
| --- | --- | --- |
| Internal historical | Variation, seasonality, and structural change in the focal system | Definitions, mix, product, maturity, and source must bridge |
| Internal cross-unit | Comparable products, markets, segments, cohorts, or teams | Shared systems do not guarantee compatible customers or opportunities |
| Direct peer | Similar customer, product, model, stage, market, and metric | Private performance and complete coverage are usually unavailable |
| Broader industry | Directional context and distribution shape | Heterogeneous models and selection limit rank and targets |
| Vendor-customer | Performance inside a provider's selected customer base | Commercial, customer-only, response, and survivorship bias |
| Survey or panel | Estimates for a declared frame and response process | Nonresponse, weighting, attrition, and stated-versus-observed limits |
| Modeled or analyst | Scenario or estimate under published assumptions | Not observed actual; model and revision uncertainty remain |
| Case or example | Mechanism hypothesis and contextual learning | Selected narrative is not a distribution or prevalence estimate |
| Public filing or registry | Attributable reported metrics for covered entities | Accounting, disclosure, period, and business-scope differences |
| Aspirational | Directional ambition | Not evidence of feasibility, probability, or required target |

Never pool types without preserving source type and showing why the combination is decision-compatible.

## Product Topology And Opportunity

Use topology-specific value bases:

- consumer or habit: value-bearing activity at a natural cadence, with legitimate low-frequency states;
- episodic: completed value per verified opportunity, not daily use;
- B2B and collaborative: user, role, seat, workspace, account, contract, and revenue states separately;
- marketplace and network: participant sides, local network, opportunity, match, fulfillment, quality, multi-homing, and economics;
- AI: task, accepted output, successful workflow, quality, correction, latency, cost, and retained outcome rather than tokens or prompts alone.

Do not rank unlike topologies with DAU, seats, GMV, messages, tokens, or one engagement score.

## Historical And Cohort Comparison

Align entity, eligibility, event, identity, product, plan, segment, market, channel, cohort start, age, window, maturity, cutoff, timezone, latency, and finalization. Preserve preliminary, revised, restated, and final values. Missing future or late outcomes are not zero.

When definitions change, use an overlap bridge, dual run, restatement, or separate series. Keep canonical totals beside predeclared cuts and preserve mix. Do not compare day-7 with month-12, users with accounts, or calendar aggregates containing different cohort ages.

## Boundary With Adjacent Skills

Growth Benchmark Analysis evaluates comparison evidence. It does not define the canonical metric, instrument events, build cohorts, set targets, forecast performance, size opportunity, select competitors, diagnose cause, allocate resources, or approve action. Route those outputs and record the exact returned artifact and version needed.
