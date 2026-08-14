# Output Contract

Use this order. Keep verified evidence, reported signals, inference, unavailable inputs, observed values, forecasts, scenarios, targets, approvals, and causal claims visibly distinct.

## 1. Decision Header

State mode, decision, owner, customer and payer entity, cohort, product, market and locale, value basis, currency, observed cutoff, forecast horizon, model version, and external-action boundary.

## 2. Executive Finding

State what current evidence can support and the primary entity, denominator, value-basis, maturity, censoring, model, calibration, uncertainty, or comparability constraint. Do not return an unexplained LTV number, score, ratio, or winner.

## 3. LTV Contract And Evidence Ledger

Include customer hierarchy, cohort entry, original denominator, states, opportunity, identity, value waterfall, horizons, model, evidence state, source, contradictions, unavailable inputs, and privacy boundary.

## 4. Observed Value Ledger

Show period and cumulative actual-to-date customer value, revenue, refunds, costs, gross profit, and contribution as applicable. State cutoff, maturity, original denominator, coverage, late events, reversals, and source reconciliation.

## 5. Forecast And Sensitivity

Show selected topology and method, observed-to-forecast boundary, survival or opportunity, conditional value, expansion, contraction, costs, discounting, tail, terminal, scenarios or interval, and assumptions that can reverse the decision.

## 6. Calibration And Quality

Report holdout design, maturity, predicted versus observed value, signed and absolute error, grouped calibration, segment error, interval coverage, stability, drift, fairness, abstention, and model limitations.

## 7. Compatible Decision View

Match LTV with CAC, payback, cash, attribution or incrementality, marginal economics, saturation, capacity, customer value, overlap, cannibalization, concentration, and risk. Mark incompatible comparisons rather than forcing a ranking.

## 8. Actions And Governance

Return dependency-ordered evidence, calculation, model, and operating fixes with owner, decision rule, guardrail, stop rule, completion proof, re-read date, specialist handoff, and pinned Playbook source. Keep external changes approval-ready and unexecuted.

## Mode-Specific Requirements

| Mode | Required addition |
| --- | --- |
| `audit` | Current calculation lineage, error ledger, unsupported assumptions, decision impact, and remediation |
| `estimate` | Reproducible observed calculation plus bounded forecast or explicit reason not to forecast |
| `portfolio` | Compatibility matrix, scenario comparison, overlap, uncertainty, tradeoffs, gates, and rejected comparisons |

## Final Checks

- Customer, payer, retention, revenue, and cost entities are compatible.
- Original cohort denominator, cutoff, maturity, and censoring remain visible.
- Observed actual-to-date value is separate from forecast remainder.
- Revenue, gross profit, contribution, CAC, and payback are not conflated or double counted.
- No universal churn, plateau, horizon, terminal value, LTV:CAC threshold, model accuracy, market transfer, or causal claim is invented.
- No sensitive record, named customer score, live access, model deployment, routing, pricing, budget, publishing, customer contact, or result claim appears.
