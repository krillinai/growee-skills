# Calibration And Uncertainty

## Separate Maturity From Performance

Compare cohorts at the same observed landmark or through a model that was validated for the relevant horizon. Record cohort age, cutoff, refund maturity, reporting lag, product and price version, market, source, and acquisition mix. Right-censored customers remain at risk; they are not observed churn or zero future value.

Use a maturity table:

| Cohort | Original size | Observed horizon | Actual-to-date value | Forecast remainder | Interval or scenarios | Mature for decision? |
| --- | ---: | ---: | ---: | ---: | --- | --- |

Do not let a mature cohort automatically defeat a younger cohort, or let a model forecast erase actual-to-date differences.

## Back-Test Design

Freeze model version, prediction time, eligible population, feature cutoff, value basis, forecast horizon, training cohorts, validation cohorts, market, and decision before evaluation. Use out-of-time and out-of-cohort holdouts that resemble the intended decision population. Keep post-outcome features out of the model.

For every holdout report:

- predicted and observed mean and total value;
- absolute and signed error;
- calibration by prediction band, cohort, horizon, product, market, source, and relevant customer segment;
- error distribution and concentration, not only an average;
- ranking or discrimination only if the decision uses ordering;
- interval coverage or scenario capture;
- drift in inputs, state transitions, value, costs, and residuals;
- decision impact, including false-scale and false-stop cases.

## Calibration Calculations

For a group with predicted value `P` and observed mature value `O`:

```text
Signed error = P - O
Relative overprediction = (P - O) / O, when O is nonzero and this denominator is declared
Calibration ratio = O / P, when P is nonzero
```

Do not hide denominator choice. Avoid percentage error where observed value is zero or near zero; use absolute error and grouped value-weighted measures. Positive rank correlation can coexist with severe overprediction and unsafe thresholds.

## Forecast Uncertainty

Propagate uncertainty from cohort size, retention or opportunity, value conditional on activity, price, expansion, contraction, refunds, costs, foreign exchange, seasonality, model parameters, tail, and structural change. Distinguish sampling uncertainty, model uncertainty, scenario uncertainty, and unavailable evidence.

Return an interval when the method supports one; otherwise return named downside, base, and upside scenarios. Show the smallest assumption changes that reverse the decision. Never present extra decimal precision as confidence.

## Segment And Fairness Review

Check performance across decision-relevant product, market, tenure, acquisition state, customer topology, and service-cost segments. Use protected traits only when necessary, authorized, minimized, and governed for fairness review; do not use them to reduce service or opportunity. Small groups require suppression and cautious interpretation.

## Monitoring And Retirement

Define owner, refresh cadence, maturity calendar, calibration thresholds, drift triggers, abstention, override, fallback, incident response, rollback, and retirement. Stop or downgrade model use when identity, outcome, cost, product, market, price, tracking, or calibration changes invalidate the contract.
