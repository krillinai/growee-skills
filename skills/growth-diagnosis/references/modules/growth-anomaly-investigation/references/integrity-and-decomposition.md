# Integrity And Decomposition

## Reconcile Sources Before Causes

For every source or dashboard record:

- metric and event definition, entity, eligibility, identity, deduplication, filters, exclusions, and aggregation;
- event and processing time, timezone, refresh, cutoff, lateness, backfill, correction, and retention;
- source tables, joins, query, semantic layer, report, model, attribution, currency, and version;
- product, app, SDK, server, consent, platform, market, and release coverage;
- owner, quality checks, known incidents, and reconciliation to a source of record.

Common discontinuities include renamed or split events, trigger changes, client-to-server migration, duplicate suppression, missing backfill, identity merges or splits, consent changes, bot filters, attribution windows, currency treatment, account hierarchy changes, late data, retry storms, and report-query edits.

Do not average disagreeing sources. Build compatible views, quantify coverage and residual differences, and leave unresolved discrepancies visible. Route schema and implementation repair to `tracking-plan`; do not modify production during investigation.

## Quantify The Observed Change

Report:

- prior and current counts, denominators, rates or values;
- absolute delta, relative delta, and contribution to the parent outcome;
- entity, segment, market, product, source, window, timezone, and maturity;
- missing, late, unknown, suppressed, duplicate, invalid, and excluded units;
- expected baseline, variation or interval, method, assumptions, and limitation.

A rate can rise while successful counts fall. Revenue can rise while retained customers, contribution, or cash deteriorate. A large relative change in a tiny cell can have negligible aggregate impact. Always pair rate and relative movement with counts and absolute effect.

Do not invent statistical significance. If event-level or sufficient aggregate data is supplied, select a method appropriate to distribution, dependence, repeated measures, seasonality, and sampling. Otherwise state that uncertainty is unavailable and request the minimum sufficient fields.

## Separate Expected Variation

Account for weekday and hour patterns, month and quarter boundaries, holidays, payday, billing and renewal cycles, campaigns and promotions, seasonality, weather, inventory, outages, release cadence, market events, and known structural trends where relevant.

Use matched historical periods or a supplied calibrated forecast. Record the training or comparison window, exclusions, structural breaks, and interval behavior. A forecast miss can identify an anomaly; it does not identify the mechanism. Do not fit a baseline after seeing the desired conclusion.

## Decompose Without Losing The Total

Start with the fewest decision-relevant dimensions that can explain a material share of the parent delta. Typical order:

1. source, definition, product or app version, platform, and maturity;
2. lifecycle or value state and growth-accounting movement;
3. major market, customer, plan, product, and channel mix;
4. new versus existing cohorts, eligibility, access, exposure, and behavior;
5. deeper hypothesis-specific segments only after a parent contribution appears.

For every split show parent total, child totals, coverage, unknown residual, and reconciliation. Use compatible mutually exclusive groups or state overlap explicitly.

For an aggregate rate `R = sum(w_i * r_i)`, separate:

- **mix effect:** change caused by segment weights `w_i` at held-compatible rates;
- **within-segment effect:** change caused by segment rates `r_i` at held-compatible weights;
- **interaction or residual:** difference from the chosen decomposition convention, rounding, missing cells, or overlap.

State the weighting convention. Do not present decomposition as causality. Use it to locate material descriptive contributions and Simpson's-paradox patterns.

For additive values such as customers or recurring revenue, reconcile opening state plus new, resurrected, expanded, contracted, churned, corrected, currency, and other movements to closing state as applicable. Route detailed state reconciliation to `retention`.

## Control Segment Search

Pre-specify high-value dimensions from the incident and business model. Track every comparison. Mark post-hoc findings exploratory. Check denominator, effect size, absolute contribution, uncertainty, missingness, maturity, and stability over adjacent windows. Require replication or confirmatory evidence before action.

Do not search hundreds of cells until one looks extreme, rank small groups, expose suppressed populations, or use sensitive traits without a necessary, authorized, fair, and privacy-reviewed purpose. Route deeper compatible cohort work to `retention` and transition analysis to `growth-diagnosis`.

## Stop Decomposition At The Decision Boundary

Stop when:

- a measurement defect accounts for the material delta and the remaining behavior is bounded;
- one or more stable descriptive contributors explain the parent change enough to choose the next evidence task;
- remaining cells are too small, immature, overlapping, or privacy-sensitive;
- further slicing cannot change the stated decision;
- a specialist analysis is required.

Preserve the unexplained residual. Do not force contributions to 100% by assigning unknowns to a preferred mechanism.
