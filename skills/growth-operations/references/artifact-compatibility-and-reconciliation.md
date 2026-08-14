# Artifact Compatibility And Reconciliation

## Check Compatibility Keys

Before comparing or aggregating artifacts, reconcile:

1. customer, user, account, buyer, seller, payer, beneficiary, approver, and employee roles;
2. entity, eligibility, identity, deduplication, numerator, denominator, event or state, and source of truth;
3. product, offer, business model, market, locale, segment, motion, route, channel, and platform;
4. actual, baseline, benchmark, target, opportunity, forecast, scenario, plan, budget, causal estimate, and result roles;
5. period, as-of, cutoff, calendar, time zone, window, cohort, maturity, lag, revision, and version;
6. currency, conversion date and source, revenue recognition, contribution, cash timing, cost scope, and accounting basis;
7. owner, approver, effective state, scope, limitation, contradiction, and downstream decision.

If a material key differs, use separate views or an explicit reconciliation bridge. Do not average incompatible units.

## Preserve Version Lineage

For each decision, identify the artifact versions available at that decision's original cutoff. Never replace an old forecast, target, baseline, strategy, budget, or plan with the newest value when evaluating the old decision.

Record:

```text
prior version + attributable data revision + definition change + method change + assumption change + decision change = current version
```

Keep unknown residuals visible. A latest artifact can supersede future use without erasing prior evidence or approval.

## Separate Planning Quantities

| Quantity | Meaning | Must not become |
| --- | --- | --- |
| Actual | Observed mature state under a declared contract | target or causal effect |
| Baseline | Compatible reference state for a decision | desired future or forecast by default |
| Target | Accountable desired state or threshold | forecast, evidence, or cause |
| Opportunity | Bounded headroom, reachable change, or decision value | committed result |
| Forecast | Time-indexed conditional projection as of a cutoff | target or promise |
| Scenario | Coherent conditional assumptions and effects | probability-weighted truth without support |
| Plan | Intended decisions, commitments, and actions | authorization or implementation |
| Budget | Resource boundary or approved financial allocation | proof of impact or capacity by itself |
| Causal estimate | Effect supported in a tested population and design | transferable portfolio value without evidence |
| Result | Mature customer or business outcome | attribution to every contributor |

Show target-to-forecast, baseline-to-target, forecast-to-budget, and portfolio-to-capacity gaps without forcing one quantity to equal another.

## Reconcile Hierarchies And Outcomes

Create child totals only when units form a mutually exclusive, collectively exhaustive partition on compatible periods and definitions. Otherwise preserve separate views, shared outcomes, overlap, residual, and reconciliation method.

Do not give marketing, sales, product, customer success, pricing, referral, and partnerships separate copies of the same customer, contract, revenue, contribution, or cash. Map lifecycle states without counting one entity independently at acquisition, activation, retention, monetization, referral, and expansion.

Separate:

- accountable outcome ownership from contributor work;
- attribution from incrementality and causality;
- gross opportunity from reachable retained and net value;
- experiment estimates from transferred and realized effects;
- local initiative results from portfolio effects and cannibalization.

## Reconcile Scenarios

Use scenarios only for uncertainties that change a planning decision. For each scenario record compatible assumptions, evidence and contradiction, sensitivity, strategy and portfolio effect, resource and economic effect, observable trigger, response, owner, and review.

Identify commitments that are robust, contingent, reversible options, hedges, or irreversible. Do not invent probabilities, use only an upside case, average incompatible scenarios, or hide the factor that controls the decision.

## Handle Contradictions

Record both sides, sources, versions, definitions, maturity, and decision effect. Resolve through a definition bridge, source reconciliation, updated evidence, specialist refresh, separate views, or an accountable decision. Do not choose the favorable claim or conceal an incompatible input to make the package decision-ready.
