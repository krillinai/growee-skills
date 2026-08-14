# Expansion Measurement And Signals

## Cohort Contract

For each expansion type, freeze:

- customer or account entity and hierarchy;
- retained original-scope eligibility and value state;
- adjacent need and candidate scope;
- signal, assignment or exposure, acceptance, and expansion start;
- first-value, repeat-value, retention, renewal, contraction, and observation windows;
- cutoff, timezone, maturity, product, package, price, contract, and market versions;
- original-scope, new-scope, total-customer, commercial, support, quality, trust, and contribution outcomes;
- counterfactual, interference, selection, and missing-data rules.

Compare compatible and equally mature cohorts. Preserve accounts that decline, fail implementation, contract, churn, or never reach value. Report rates and absolute retained contribution.

## Commercial Decomposition

Use compatible supplied values:

```text
GRR = (starting recurring revenue - churn - contraction)
      / starting recurring revenue

NRR = (starting recurring revenue - churn - contraction
       + declared recurring expansion)
      / starting recurring revenue

adoption-led NRR = (starting recurring revenue - churn - contraction
                    + seat + usage + product expansion backed by declared adoption)
                   / starting recurring revenue
```

Show price changes, foreign exchange, one-time revenue, payment recovery, credits, and other effects separately. State currency, cohort, period, revenue and contribution basis, recognition rule, maturity, inclusions, exclusions, and source. Do not infer adoption quality from NRR.

## Causal Boundary

Expanded accounts differ through size, tenure, health, need, seller selection, success attention, contract timing, budget, and survivorship. Expansion can cause retention, retention can enable expansion, or both can share a third cause.

Define the estimand: value change for which eligible account or unit, caused by which product or commercial intervention, over which horizon. Account members share workflows, seats, pooled usage, admins, contracts, and outcomes, so individual randomization often contaminates treatment. Consider account, workspace, team, cluster, staged, threshold, encouragement, or other compatible designs and route statistical details to `growth-measurement`.

## Signal Contract

| Field | Requirement |
| --- | --- |
| Decision | exact eligible action, owner, capacity, expiry, and prohibited uses |
| Entity | account, workspace, team, product, user role, hierarchy, and identity |
| Value | retained original state, adjacent need, candidate new-scope outcome, and counterevidence |
| Rule or model | version, prediction time, pre-treatment inputs, unknown handling, and reason code |
| Quality | coverage, calibration, precision, recall, segment error, drift, and abstention |
| Governance | fairness, privacy, access, override, appeal, audit, and retirement |
| Feedback | exposed action, customer response, first and retained value, commercial result, harm, and maturity |

Product use indicates behavior, not need, authority, budget, security, procurement, or treatment benefit. Exclude future expansion, post-offer behavior, post-close notes, renewal, and later outcomes from features available at prediction time. Do not use protected attributes, executive relationships, private messages, or sensitive proxies by default.

## Suppression And Capacity

Define ineligible, declined, do-not-contact, incident, implementation, support escalation, renewal risk, security review, missing authority, recent exposure, frequency, incompatible offer, unresolved complaint, and capacity-overflow states. A score without a safe action and receiving owner should not create a route.

Measure signal-to-value, not signal-to-opportunity alone: eligible coverage, accepted handoff, first value, retained new-scope value, original-scope health, total-customer value, contribution, complaints, and false-positive burden.
