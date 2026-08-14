# Uncertainty And Calibration

Forecast quality is conditional on the decision, origin, horizon, entity, segment, market, data vintage, and outcome maturity. One aggregate accuracy number is insufficient.

## Forecast Output

Return the least precise output supported by the evidence:

- point plus interval or quantiles for a probabilistic forecast;
- bounded range when probability calibration is unavailable;
- conditional scenarios for coherent assumption bundles;
- unresolved specification when inputs cannot support calculation.

State the interval or range method and interpretation. A 95% prediction interval targets long-run coverage under its assumptions; it does not mean the point forecast is 95% accurate or that a single outcome has been certified.

## Time-Valid Back-Testing

Use rolling-origin or blocked holdouts that reproduce:

- information available at each origin;
- historical feature, definition, and source versions;
- late-arriving and revised actual states;
- forecast horizon and decision cadence;
- product, price, market, channel, and policy conditions;
- overrides and method changes actually used.

Compare with the naive and incumbent baselines. A random train-test split can leak future regime and seasonality information.

## Error And Calibration

Report a decision-relevant set:

| Measure | Use | Limitation |
| --- | --- | --- |
| Signed error or mean error | Direction and systematic bias | Positive and negative errors can cancel |
| MAE | Typical absolute error in original units | Depends on scale |
| RMSE | Penalizes larger misses | Sensitive to outliers |
| MAPE | Relative error for positive outcomes away from zero | Unstable at or near zero and asymmetric |
| WAPE | Aggregate absolute error relative to aggregate actual | Can hide segment bias and depends on volume |
| MASE or scaled error | Comparison against a baseline across scales | Requires a valid scaling baseline |
| Interval coverage and width | Calibration and usefulness of uncertainty | Wide intervals can cover without helping decisions |
| Pinball or quantile loss | Quality of quantile forecasts | Needs consistent quantile interpretation |

Also inspect turning points, peak and trough periods, revision size, rank or threshold decisions where relevant, and the cost of over- versus underprediction.

## Segment And Horizon Calibration

Report error and coverage by forecast horizon, origin, market, product, segment, cohort age, source, growth regime, season, and decision threshold where sample size permits. Use aggregation and small-cell protection when detail would be unstable or unsafe.

Annual reconciliation can hide systematic weekly or market error. Average calibration can hide new-market overprediction, peak underprediction, or a protected and underserved group. Do not call unavailable segment evidence good performance.

## Revision Bridge

For every new forecast version reconcile changes due to:

```text
prior forecast
+ actual data revisions
+ newly observed periods
+ definition or source changes
+ driver forecast changes
+ assumption changes
+ method or parameter changes
+ approved overrides
+ previously unknown events
= current forecast
```

Preserve residual unexplained change. Do not rewrite history to make old forecasts appear more accurate.

## Bias, Overrides, And Governance

Distinguish statistical error from optimism, conservatism, target pressure, stale assumptions, missing constraints, structural break, data defects, and operational overrides. Record who overrode what, when, why, expected effect, and later outcome.

Define thresholds for recalibrate, repair data, shorten horizon, widen interval, use baseline fallback, split model, suspend use, or retire. A complex model does not earn continued use through prestige or sunk cost.

## Scenarios And Sensitivity

Scenarios are conditional cases, not probability forecasts by default. Define coherent driver bundles, triggers, counterconditions, outcomes, constraints, and decisions. Do not assign probabilities unless an attributable method supports them.

Use one-way, multi-way, break-even, or simulation sensitivity as evidence permits. Show which assumptions change the decision, where ranks reverse, and where uncertainty makes alternatives indistinguishable.
