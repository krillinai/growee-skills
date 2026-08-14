# Output Contract

Return Markdown unless the user requests another local format. Preserve actuals, forecasts, scenarios, targets, plans, evidence states, uncertainty, overrides, approvals, and causal claims separately.

## 1. Decision And Forecast Header

State mode, decision, owner, outcome, entity and level, segment, product, market, frequency, timezone, as-of, evidence cutoff, actual period, forecast origin, horizon, model and forecast versions, review date, and external-action boundary.

## 2. Contract And Vintage Ledger

| Input or series | Entity, definition, unit | Scope and period | Source and version | Event and availability times | State | Quality, maturity, revision | Owner and next check |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include identity, currency, accounting basis, cohorts, exclusions, late and censored data, reconciliation, access limits, and unavailable inputs.

## 3. Series Reconciliation

Show finalized actual, preliminary actual, estimate, nowcast, forecast, scenario, stress case, target, plan, budget, and benchmark as separate versioned series. Include a revision bridge from the prior forecast and preserve unexplained residuals.

## 4. Method And Assumptions

Document topology, naive or incumbent baseline, selected method, equations, driver and lag table, constraints, seasonality, interventions, structural breaks, cohort and maturity treatment, portfolio hierarchy, reconciliation, and assumption register. Label each input observed, externally forecast, inferred, assumed, targeted, planned, or scenario-only.

## 5. Forecast Outputs

| Outcome | Origin and horizon | Point or range | Interval or quantiles | Scenario | Segment or component | Constraint and residual | Decision threshold |
| --- | --- | --- | --- | --- | --- | --- | --- |

State units, rounding, uncertainty method, intended coverage, and conditions. Do not fabricate probabilities or precision.

## 6. Back-Test And Calibration

Show holdout design, information-vintage controls, naive and incumbent baselines, signed error, absolute and appropriate relative or scaled errors, interval coverage and width, turning points, bias, revisions, overrides, and decision impact by horizon and decision-relevant segment.

## 7. Decisions And Governance

Return target and plan gap, sensitivity, break-even conditions, thresholds, risk of over- and underprediction, fallback, recalibration and retirement gates, refresh cadence, owners, approvals, privacy, fairness, market transfer, and specialist handoffs.

## 8. Completion Record

List pinned Playbook sources, unavailable evidence, unresolved assumptions, next evidence, review dates, approval-ready external actions, and completion proof. Confirm no future leakage, overwritten actual, incompatible aggregation, hidden target manipulation, unsupported accuracy, causal claim, legal conclusion, system change, deployment, or result claim occurred.
