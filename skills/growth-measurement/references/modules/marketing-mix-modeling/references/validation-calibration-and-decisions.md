# Validation, Calibration, And Decisions

## Three Validation Verdicts

Return separate verdicts:

| Verdict | Question |
| --- | --- |
| Predictive | Does the model outperform a relevant baseline on unseen compatible outcomes? |
| Structural | Are transformations, parameters, contributions, residuals, and market differences plausible and stable? |
| Decision | Do uncertainty and supported response ranges distinguish the alternatives under consideration? |

`decision-ready` requires all three for the declared decision. A model can predict well yet remain causally unidentified or unable to distinguish allocation options.

## Validation Suite

Use applicable checks:

- naive and seasonal baseline comparison;
- rolling-origin, out-of-time, withheld-period, withheld-market, or geographic holdout;
- residual mean, autocorrelation, heteroskedasticity, distribution, outlier, and structural-break review;
- posterior predictive or simulation-based checks where applicable;
- convergence, effective-sample, chain, optimization, and numerical diagnostics;
- coefficient, sign, lag, decay, saturation, contribution, and response plausibility;
- source, missingness, taxonomy, currency, and revision sensitivity;
- prior, constraint, variable, transformation, window, market, and hierarchy sensitivity;
- baseline, contribution, interaction, residual, and observed-outcome reconciliation;
- decision stability under uncertainty, covariance, and alternative defensible specifications.

Training R-squared, MAPE, adjusted fit, information criteria, posterior intervals, large row counts, or visual similarity cannot certify causal or decision quality alone.

## Experiment Calibration Bridge

For every experiment record intervention, channel and tactic, assignment and exposure unit, eligible population, market, period, outcome, estimand, maturity, randomization, power, SRM, contamination, interference, spillover, carryover, concurrent change, effect, uncertainty, source, version, and limitations.

Confirm compatibility before use. A geo test of one creative, spend band, market set, and short-term sales outcome may not directly calibrate total channel effect across all markets and long-term customer value.

Use compatible experimental evidence through a declared:

- prior or prior-predictive constraint;
- likelihood or joint-estimation component;
- calibration target with uncertainty;
- model-selection or specification check;
- withheld validation comparison;
- response-curve anchor or bound.

Do not force MMM and experiment point estimates to agree. Investigate differences in scope, exposure, estimand, time, outcome, maturity, interference, model controls, priors, and data quality. Preserve unresolved contradiction and route experiment design and readout to `growth-measurement`.

## Contribution And Economics

Report baseline, context, input, interaction, joint or unresolved, and residual components by compatible market and period with uncertainty. Keep modeled incremental customer outcomes separate from attributed conversions and platform credit.

Join revenue, refunds, discounts, incentives, cost of goods, service cost, media cost, production cost, fees, gross profit, contribution, and cash only through compatible cohort, lag, currency, accounting, and maturity bridges. Route detailed economics to `monetization`.

Define:

```text
modeled average return
= modeled incremental outcome over the supported historical band
/ compatible input cost over that band

modeled marginal return
= change in modeled outcome for a bounded next input change
/ compatible incremental cost of that change
```

Both remain conditional on model assumptions, support, and uncertainty. Historical average return is not next-dollar return.

## Scenario Register

| Scenario | Input change and support | Outcome and economic basis | Uncertainty and covariance | Constraints and obligations | Trigger / stop / review | Owner / decision handoff |
| --- | --- | --- | --- | --- | --- | --- |

Include cash, commitments, minimums, capacity, inventory, distribution, creative supply, audience reach, frequency, availability, channel restrictions, concentration, interaction, learning, risk, customer protection, and reversibility where relevant. Build only scenarios that can change the decision. Do not invent an optimum, probability, budget, owner, or approval.

Route channel choice and scale gates to `acquisition-strategy`; cross-functional resources to `growth-operations`; forecasts to `growth-measurement`; targets to `growth-measurement`; and planning to `growth-operations`.

## Long-Term And Non-Paid Effects

Preserve paid, owned, earned, referral, partner, sales, product-led, retail, distribution, pricing, promotion, and word-of-mouth mechanisms separately where measurable. Short histories and short-term sales outcomes may not identify long-term brand, habit, retention, network, or product effects. Use longer horizons, intermediate and mature outcomes, experiments, surveys, search or demand signals, and triangulation only with explicit roles and causal limits.

## Versioning And Refresh

Version dataset, vintages, sources, outcome, market hierarchy, transformations, priors, constraints, model code, fit, validation, calibration, contribution, response, scenario, recommendation, and decision. Preserve candidate, failed, selected, calibrated, deployed-record, superseded, and retired states.

Refresh after material channel, platform, product, price, promotion, distribution, market, privacy, source, taxonomy, measurement, structural, experiment, or decision change. Record the trigger and bridge. Do not overwrite misses, unfavorable versions, assumptions, or decisions.

## Governance And External Actions

Treat every market as a new evidence and operating boundary. Revalidate product, outcome, media, platforms, costs, currency, calendars, competition, data, transformations, response, experiments, privacy, and ownership. Hierarchical pooling requires an exchangeability argument; translation or currency conversion is insufficient.

Use aggregate minimum-necessary data. Define purpose, authority, access, aggregation, minimum cells, retention, deletion, correction, audit, fairness, customer protection, and review. Do not create individual channel-influence scores or automated targeting, pricing, denial, employment, credit, insurance, health, housing, or other consequential decisions.

The default deliverable is a local specification, audit, model artifact, scenario, or approval-ready handoff. Do not access systems, export data, deploy models, alter budgets or campaigns, publish dashboards, or claim incremental growth.
