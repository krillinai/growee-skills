# Features, Models, And Validation

## Feature Contract

| Feature | Entity / meaning | Source / event / availability | Window / aggregation | Missing / zero / not applicable | Transformation / direction | Version / evidence / leakage risk |
| --- | --- | --- | --- | --- | --- | --- |

Feature families can include:

- product access, eligible opportunity, first and repeated value, frequency, depth, breadth, quality, reliability, errors, cost and burden;
- implementation, readiness, migration, training, permissions, integration, support, incident, recovery and customer-success state;
- survey and qualitative customer evidence with response, construct, instrument, sampling and maturity limits;
- relationship signals with observer, rubric, evidence, disagreement and correction;
- contract, entitlement, price, discount, invoice, payment, renewal, expansion and contraction state;
- market, product, plan, tenure, seasonality and other predeclared context.

Keep each family separate in the output. Do not treat logins, NPS, tickets, CSM sentiment, contract value, renewal, and churn as one numeric construct by default.

## Prediction-Time Integrity

Use only evidence available through the feature cutoff. Audit:

1. direct target fields and outcome statuses;
2. later events, invoices, support outcomes, notes, reasons and final classifications;
3. post-offer, post-contact, post-treatment and post-renewal behavior;
4. human workflow stages or overrides caused by advance knowledge;
5. future aggregate windows and final data vintages;
6. repeated customer, hierarchy and time leakage across train, validation and test;
7. proxies that reveal outcome processing rather than customer state;
8. features available in research but absent at operating prediction time.

Freeze event, ingestion, availability, revision and finalization timestamps. Use customer-, account-family- and time-safe validation splits that mirror the intended use.

## Missingness

Preserve zero, missing, unavailable, not applicable, not due, late, suppressed, deleted, disconnected, below threshold and source-incident states. No telemetry is not zero use; no ticket is not satisfaction; no survey is not a negative response; no note is not no relationship; no invoice is not nonpayment.

Document imputation, missing indicators, exclusions, fallback, sensitivity and affected populations. Missingness can be informative because operational processes differ, but using it may encode access, team, geography, contract or intervention bias. Audit that path explicitly.

## Model Choice

| Model | Appropriate use | Required caution |
| --- | --- | --- |
| Dimensional ledger | Several value, service, commercial or risk dimensions should not compensate for one another | Do not hide a decision behind colors |
| Rules or scorecard | Transparent predeclared conditions are sufficient and reviewable | Expose weights, blockers, missingness and sensitivity |
| Binary or multiclass | One fixed-horizon outcome with mature labels | Preserve prevalence, misclassification costs and calibration |
| Survival or hazard | Time to renewal, churn or another event with censoring | Define origin, risk set, competing events and time variation |
| Hierarchical model | Products, contracts, markets or segments share partial information | Validate exchangeability and local calibration |
| Treatment-effect model | Decision asks who benefits from a specific action | Requires causal identification, not risk labels alone |

Begin with prevalence, naive, prior-model and simple rules-based baselines. Record algorithm, objective, training population, features, labels, class treatment, hyperparameters, random seed where relevant, software, code, dataset and model version. Complexity or feature importance is not validity.

## Validation Contract

Validate on mature, out-of-time outcomes and the intended operating population. Report applicable measures:

- base rate and baseline performance;
- calibration curve, intercept, slope, Brier or log score;
- ROC and precision-recall behavior with class prevalence;
- precision, recall, specificity, false-positive and false-negative counts and consequences;
- lift, gains and capture at realistic review capacity;
- survival discrimination and calibration at declared horizons;
- uncertainty, bootstrap or repeated-sample stability;
- product, market, lifecycle, contract and relevant-group errors;
- threshold, missingness, label, feature and specification sensitivity;
- abstention and unresolved cases.

Accuracy on a rare outcome is insufficient. A high rank correlation does not prove calibration. A top decile, 0.5 probability or score of 75 is not a decision threshold without capacity, consequence and customer-impact evidence.

## Human Signals And Fairness

For CSM, seller, support or executive signals, record observer, role, time, rubric, underlying evidence, uncertainty, disagreement, inter-rater reliability, coverage, override and correction. Preserve customer statements and observed behavior separately from internal opinion. Do not infer emotion, authority, vulnerability or intent from notes or titles.

Evaluate performance, calibration, missingness, thresholds, actions, overrides and outcomes across relevant lawful groups and customer contexts. Protect accessibility and customers with lower telemetry access, different roles, lower natural frequency or different service models. Do not use protected traits or close proxies for consequential individual decisions.

## Prediction Is Not Treatment

A risk model estimates a defined outcome under historical conditions. It does not prove a cause, preventability, incremental treatment response or customer value. Define intervention, eligible population, assignment or identification, exposure, outcome, horizon, guardrails, interference and decision rule separately. Route causal design to `experiment-design`.
