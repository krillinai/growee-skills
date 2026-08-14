# Normalization, Uncertainty, And Interpretation

## Compatibility Gate

Compare only after aligning:

- customer value and business outcome meaning;
- entity, hierarchy, identity, eligibility, exclusions, numerator, denominator, formula, aggregation, and unit;
- event, source type, source version, product, offer, plan, segment, cohort, channel, market, and platform;
- observation, attribution, and maturity windows; cutoff, timezone, seasonality, latency, censoring, and finalization;
- currency, exchange, inflation, tax, refunds, discounts, recognition, gross or net, costs, and accounting;
- reference-class membership, sample, weighting, distribution, missingness, privacy, and uncertainty.

Use one verdict per focal metric and reference class. If a material field fails, do not force a normalized number. Show each original view, incompatibility, and evidence required for a bridge.

## Preserve Original And Normalized Views

Never overwrite the source value. Record original metric, unit, currency, basis, period, source, version, and evidence state beside every normalized view. Give the normalized view its own ID, formula, assumptions, author, reviewer, effective date, sensitivity, and expiry.

Use normalization only when it answers the declared decision. Possible adjustments include:

- equal periods, cohort ages, maturity, cutoffs, and seasonal windows;
- common entities, customer units, plan or product scopes, and denominators;
- currency conversion under a named source and date;
- nominal-to-real conversion under a named price index and base period;
- tax, refund, discount, revenue-recognition, gross-versus-net, and cost-scope reconciliation;
- per-customer, per-account, per-opportunity, per-employee, or per-capacity views under aligned definitions;
- restatement, dual run, overlap bridge, or separate series after definition changes.

Do not normalize ARR, GMV, bookings, recognized revenue, contribution, and cash into one value merely through currency conversion. Do not divide by employee counts from different dates or scopes. Report scenarios when a defensible choice remains unresolved.

## Historical, Cohort, And Mix Controls

Use compatible as-of dates and preserve preliminary, revised, restated, and final actuals. Future or late data is missing or immature, not zero. Compare cohorts at equal age under compatible eligibility, start, outcome, window, and maturity.

Keep free, paid, enterprise, consumer, market, channel, plan, product, tenure, and customer segments visible. Show the canonical total with predeclared cuts. Decompose aggregate movement into composition and within-group change when supplied data support it. Do not label an incompatible gap a trend or product-quality deficit.

## Currency, Accounting, And Economic Units

Record currency, exchange-rate source and date, spot or period average, nominal or real basis, inflation index, purchasing-power use, tax, invoice, discounts, refunds, returns, recognized or booked value, gross or net presentation, revenue share, pass-through, variable costs, contribution scope, cash timing, and accounting standard when material.

For workforce or capacity ratios, align employee, full-time equivalent, contractor, role, geography, average or endpoint headcount, and measurement date. For marketplace metrics, keep GMV, bookings, revenue, take rate, refunds, incentives, contribution, and participant economics separate.

Do not make legal, tax, or accounting conclusions. Route interpretation to accountable finance, tax, legal, and economics owners.

## Statistical And Practical Uncertainty

Report focal and reference counts, denominators, estimates, distributions, intervals or another justified uncertainty representation, sampling and weighting basis, missingness, and limitations. Preserve source model uncertainty, revision uncertainty, measurement error, peer-class sensitivity, normalization sensitivity, and structural transfer risk separately.

Do not call a small point difference statistically or practically superior. A percentile requires the full eligible distribution or an attributable quantile method. Address sparse focal samples, small reference cells, multiple metrics, peer sets, periods, subgroup searches, and repeated looks through predeclaration, adjustment, validation, or explicit exploratory labels.

Two decimal places do not create precision. Non-significance does not prove equivalence, and significance does not prove importance or causality. Report the decision threshold and downside separately from statistical evidence.

## Source-Type And Model Boundaries

Keep these distinct:

| State | Required detail |
| --- | --- |
| Observed actual | Scope, source, period, finalization, revisions, and accounting |
| Preliminary actual | Expected late data, revision policy, and final date |
| Modeled estimate | Model, inputs, assumptions, training or calibration basis, uncertainty, and version |
| Survey response | Construct, frame, sample, fielding, weighting, and stated-versus-observed limit |
| Forecast | Origin, horizon, method, uncertainty, back-test, calibration, and revisions |
| Target | Owner, decision, ambition, basis, capacity, approval, and review |
| Case outcome | Selection, context, attribution, measurement, conditions, and transfer limit |

Do not interpolate missing historical years and label them actuals. Preserve revisions and return source-type-specific views when sources cannot be combined.

## Product Topology

Build topology-specific comparisons:

- consumer and habit: value-bearing activity, natural cadence, zeroes, mature retention, quality, and fatigue;
- low-frequency and episodic: value per verified opportunity, readiness, and later return;
- B2B and collaborative: user, role, seat, workspace, account, contract, renewal, and revenue separately;
- marketplace and network: participant sides, local networks, supply, demand, match, fulfillment, quality, incentives, concentration, multi-homing, and economics;
- AI: task success, accepted output, correction, latency, reliability, human effort, cost, and retained workflow, not tokens or prompts alone.

Do not rank unlike topologies on one daily, engagement, adoption, efficiency, or growth score. Route engagement analysis to `retention` and topology economics to their owning Skills.

## Benchmark, Target, Practice, And Cause

Keep:

`benchmark -> local interpretation -> strategy or mechanism hypothesis -> forecast or scenario -> target or decision -> plan -> authorized action -> observed outcome -> causal estimate`

as separate records. A benchmark does not set a target, rewrite a forecast, allocate a budget, approve a plan, assign a quota, classify failure, or establish what would happen under intervention.

Peer practices are descriptive. Preserve implementation quality, customer, stage, scale, capacity, business model, selection, omitted variables, reverse causality, and downside. Require local research, pilot, or a credible causal design before copying onboarding, notifications, experiments, staffing, advertising, price, or another practice. Preserve quality, cost, fatigue, customer, trust, fairness, and capacity guardrails.

## Market Transfer And China

Treat each market as a new reference class and evidence boundary. Separate market, language, locale, currency, timezone, legal entity, product, platform, app distribution, identity, payment, invoice, tax and accounting basis, channel, data, sample, privacy, support, and owner.

For China, do not copy US SaaS metrics, Google or Meta channel definitions, app-store data, workweeks, sources, samples, benchmarks, consent, accounting, or targets. Revalidate local customer value, entities, platforms, source availability, periods, maturity, privacy, and review through current direct evidence and locally accountable expertise. Translation and currency conversion do not establish comparability. Avoid legal, tax, regulatory, provider, approval, accounting, and performance conclusions.

## Privacy, Fairness, And Peer Protection

Use aggregate, redacted, pseudonymous, minimum-necessary evidence and suppress unsafe small cells. Prevent reidentification through narrow peer groups, differencing, joins, repeated releases, and outliers. Record purpose, authority, consent or accountable basis, access, retention, deletion, correction, audit, fairness, accessibility, dissent, appeal, and independent review.

Do not collect or expose private contracts, named customer or employee histories, health, financial, protected-trait, precise-location, private-message, salary, or performance data merely for comparison. Do not score named people or companies for consequential pricing, service, employment, layoffs, credit, insurance, or another high-impact decision. Require accountable privacy, security, legal, finance, and competition review without claiming compliance.
