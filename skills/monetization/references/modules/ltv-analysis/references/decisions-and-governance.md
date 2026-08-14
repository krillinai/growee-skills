# Decisions And Governance

## LTV Is Decision Support

LTV can compare bounded customer economics, set evidence priorities, inform scenario planning, and identify where calibration matters. It does not prove why customers retained, which channel caused value, what price is fair, or which budget should move.

Keep these claims distinct:

| Claim | Required support |
| --- | --- |
| Actual-to-date value | Reconciled cohort, original denominator, observed horizon, and value ledger |
| Forecast LTV | Frozen model, assumptions, horizon, uncertainty, and holdout calibration |
| Attributed LTV | Compatible source-credit contract and customer-value join |
| Incremental value | Credible counterfactual and mature outcome evidence |
| Allocation decision | Incrementality, marginal economics, cash, capacity, risk, guardrails, and authority |

## LTV:CAC Compatibility

Match customer entity, cohort, product, market, currency, horizon, value basis, maturity, attribution or incrementality basis, and cost scope. Separate average from marginal LTV and CAC. Show payback and cash timing. Prevent acquisition cost from appearing inside LTV and again in CAC.

Do not enforce a universal ratio. A decision threshold depends on forecast error, capital, payback, margin, retention risk, saturation, capacity, concentration, customer harm, and strategic constraints. Route channel scaling and stopping to `acquisition-strategy` and causal evidence to `experiment-design`.

## Portfolio Decisions

For each scenario show observed value, forecast remainder, interval, calibration, acquisition or service cost, payback, cash, capacity, customer value, concentration, cannibalization, overlap, market risk, and reversibility. Compare only compatible units or normalize through an explicit common decision basis.

Return `investigate`, `hold`, `bounded test`, `eligible for specialist allocation review`, or `not comparable` as decision states unless the user supplies a different approved governance vocabulary. Do not move budgets or rank customers from LTV alone.

## Predictive Model Governance

Freeze prediction time, population, label, features, training and validation cutoff, version, allowed use, and prohibited use. Require lineage, reason codes, reproducibility, calibration, segment error, fairness, drift, abstention, override, audit, fallback, incident, rollback, and retirement.

Do not use future outcomes, post-decision labels, protected traits, raw messages, exact location, employee notes, or unrelated histories as convenience features. Do not deny service, suppress customers, personalize prices, reduce support, auto-bid, or route accounts from predicted value without separate authorization, fairness review, and appropriate controls.

## Market Transfer

Freeze legal entity, customer and payer, product, contract, price, currency, exchange rate, payment, invoice, tax, revenue recognition, costs, usage, support, retention, channel, attribution, identity, consent, data, model, calibration, and owner for each market.

Metric principles may transfer; coefficients, hazards, opportunities, costs, platform data, provider behavior, customer behavior, and calibration require local evidence. Translation and currency conversion do not validate model transfer. Preserve unavailable legal, tax, accounting, platform, and provider conditions without supplying professional advice.

## External Actions

LTV analysis may produce local contracts, formulas, cohort calculations, model specifications, scenarios, calibration plans, QA checks, dashboards specifications, and approval-ready handoffs. It must not access systems, export customer data, train or deploy models, score or route users, publish rankings, change price or service, move budgets, contact customers, or claim improvement without explicit task-level authorization and required privacy, security, finance, model, deployment, monitoring, incident, and rollback controls.
