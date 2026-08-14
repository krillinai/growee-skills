# Anomaly Contract

## Freeze The Incident

Record this contract before interpreting a chart or querying more segments.

| Field | Required definition |
| --- | --- |
| Mode | `triage`, `investigate`, or `review` |
| Incident | Stable ID, reported time, reporter, symptom, and current status |
| Decision | The decision this investigation must inform and its owner and deadline |
| Metric | Exact entity, state or event, numerator, denominator, eligibility, identity, unit, aggregation, and exclusions |
| Scope | Product, version, customer, segment, market, locale, platform, channel, and explicit exclusions |
| Source | System, dataset, table or artifact, query or report version, owner, lineage, and refresh behavior |
| Time | Event time, processing time, timezone, observation window, outcome window, cutoff, lateness, and correction rules |
| Baseline | Expected comparison selected before mechanism testing |
| Maturity | When denominator and outcome are complete enough for the decision |
| External boundary | Local artifacts allowed; systems, data mutation, contact, publication, rollback, and deployment excluded unless separately authorized |

Split the incident when metrics, entities, sources, products, markets, periods, or possible decisions cannot be reconciled. A chart label is not a metric contract. A dashboard percentage is not interpretable without counts and denominators.

## Evidence States

Use exactly:

- `verified`: attributable and inspectable within the declared source, version, and cutoff;
- `inferred`: reasoned from named evidence with assumptions and alternatives visible;
- `unavailable`: required but not supplied, accessible, mature, compatible, or measurable;
- `not applicable`: excluded by the incident contract with a reason.

Use `reported signal` for an attributable but unverified incident claim. Keep observation, derived value, attribution, association, causal estimate, forecast, target, benchmark, correction, approval, zero, missing, late, immature, censored, and suppressed states separate.

For each evidence item preserve source, owner, captured or observed time, entity, population, segment, market, product and metric version, window, value, state, quality, limitation, contradiction, and next check.

## Define A Valid Baseline

Choose the baseline for the decision, not for the most dramatic delta. Candidate comparisons include:

- immediately preceding compatible periods;
- matched weekday, season, holiday class, campaign state, market, and maturity;
- a stable historical distribution or forecast with calibrated uncertainty;
- eligible unexposed or unaffected units under a valid design;
- prior product, metric, identity, channel, or source version;
- a structurally comparable cohort, segment, or market.

Record why the baseline is comparable and what differs. Do not use an industry benchmark as the anomaly baseline unless its entity, definition, population, product, market, mix, period, maturity, and source are compatible. External benchmarks are usually context, not evidence of an internal incident.

## Establish Maturity

Record observation age and expected completion for every denominator and outcome. Check:

- partial day, week, month, billing, renewal, and cohort windows;
- event-time versus processing-time lag;
- delayed ingestion, identity resolution, refunds, chargebacks, cancellations, corrections, backfills, and late conversions;
- censoring, survival horizon, trial, contract, and natural-use frequency;
- timezone and daylight-saving boundaries;
- data freshness service levels and known incident windows.

Missing or immature is not observed zero. Compare like-for-like maturity or wait. When the decision cannot wait, show provisional ranges and the risk of acting early.

## Resolution States

Use one primary state only when evidence distinguishes it:

| State | Meaning |
| --- | --- |
| `measurement issue` | Definition, identity, collection, processing, source, query, quality, or maturity explains the material observed change |
| `behavioral change` | Compatible evidence supports a real customer, participant, market, product, or operating change |
| `mixed` | Both measurement and behavioral contributions are material or unresolved within one aggregate |
| `expected variation` | The observed change is compatible with the declared baseline and uncertainty after quality checks |
| `unresolved` | Available evidence cannot distinguish states or material contributors |

Do not force a root cause. State confidence as a bounded qualitative conclusion supported by named evidence and limitations; do not manufacture a numeric score. A resolution can be descriptive without being causal.
