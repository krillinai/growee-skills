# Decisions And Governance

A forecast informs a bounded decision owner. It does not approve a target, plan, budget, staffing level, price, campaign, product change, customer treatment, or external action.

## Decision Contract

For each use state:

- decision, owner, cadence, deadline, and reversibility;
- forecast outcome, origin, horizon, version, and uncertainty;
- threshold or range that changes action;
- cost and risk of over- and underprediction;
- guardrails, capacity, cash, trust, safety, and customer effects;
- fallback when data, model, or interval fails;
- approval and separately authorized action;
- actualization date, review, learning, and retirement.

Use `inform`, `review`, `validate`, `hold`, `fallback`, `suspend`, or `retire forecast use` as workflow states. They do not execute the operating decision.

## Forecast, Target, And Plan

Keep three views visible:

1. `unbiased or operating forecast`: the forecasting process's expected outcome and uncertainty;
2. `target`: the desired result and attributable basis;
3. `plan or scenario`: actions, resources, dependencies, and driver changes intended to alter the outcome.

Show target-to-forecast gap and the assumptions required to close it. Do not adjust a forecast silently until it reaches the target. Record challenge, approval, override, and revision without erasing the baseline.

## Specialist Ownership

| Forecast input or decision | Route |
| --- | --- |
| Full business topology, stocks, flows, loops, and scenario mechanisms | `growth-model-design` |
| Commercial pipeline, stages, bookings, contracts, revenue, invoice, and cash reconciliation | `growth-operations` |
| Customer lifetime value, survival, repeat purchase, and LTV:CAC | `monetization` |
| Metric definitions and lineage | `growth-measurement` |
| Cohort construction and maturity comparisons | `retention` |
| Activation, retention, monetization, or expansion mechanism | Relevant lifecycle Skill |
| Causal intervention effect | `growth-measurement` |
| Acquisition channel portfolio and budget allocation | `acquisition-strategy` |
| Targets, staffing, initiative portfolios, and decision rights | `growth-operations` |

Forecasting can consume a specialist output only with its entity, version, market, as-of date, horizon, uncertainty, limitations, and owner preserved.

## Privacy And Fairness

Use the minimum data required. Prefer aggregate, redacted, pseudonymous, consented, and small-cell-suppressed inputs. Define purpose, authority, access, retention, deletion, correction, audit, and incident ownership.

Do not request payment credentials, protected traits, health or financial details, private messages, exact locations, complete device graphs, personal notes, or raw identities when aggregate cohorts are enough. Do not reidentify people, create personal value or risk rankings, or route treatment without a separately justified and governed decision policy.

Audit calibration and error for decision-relevant groups without using protected traits as automatic treatment rules. Separate forecast quality from the fairness and legitimacy of the downstream decision.

## Market Transfer And China

Revalidate entity, customer, product, cohort, channel, platform, app distribution, calendar and seasonality, pricing, payment, tax, invoice, currency, exchange rate, attribution, identity, consent, data, storage, transfer, source access, model, assumptions, calibration, and ownership by market.

For China, use current direct sources and locally accountable review for time-sensitive product, platform, app-store, payment, data, advertising, and regulatory conditions. Translation and currency conversion do not validate a forecast. Require local holdouts, error analysis, fallback, and retirement rules. Do not provide legal, tax, accounting, or compliance conclusions.

## Operating Cadence

Define forecast production, review, publication, actualization, revision, calibration, override, archive, and retirement cadences. Preserve every vintage and decision record. Track timeliness, missing inputs, manual overrides, baseline skill, interval coverage, bias, decision errors, false precision, and use of stale forecasts.

Monitoring the forecast is not permission to alter dashboards, alerts, budgets, plans, or systems. Prepare approval-ready specifications and handoffs only.
