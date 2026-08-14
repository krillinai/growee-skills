# Traffic, Quality, And Evidence Operations

## Build Traffic And Concurrency Ledgers

For every proposed or active-record item capture eligible population, identity, randomization unit, required sample or sensitivity input, assignment share, exposure rule, product surface, market, period, ramp, maturation window, long-term holdout, exclusions, shared metrics, and concurrent interventions.

Map:

- namespaces, layers, mutual-exclusion groups, and permitted combinations;
- factorial or interaction designs and the decisions they serve;
- contamination across devices, accounts, products, channels, and markets;
- network, marketplace, geographic, creator, household, or organizational spillovers;
- carryover, washout, novelty, learning, seasonality, and persistent treatment;
- simultaneous product, price, lifecycle, acquisition, policy, and platform changes.

Do not assume independent samples or effects. Record expected interaction, detection limits, unresolved residual, sequencing, and specialist review. A technically available slot is not available if maturity, decision attention, support, or risk capacity is unavailable.

## Gate Schedules And Traffic Plans

Specify dates, phases, traffic percentages, sample sizes, sensitivity, power, duration, randomization units, namespaces, holdouts, readout windows, reserves, or owners only from attributable experiment specifications and reconciled program capacity. Do not manufacture a safe-looking calendar from category labels or requested experiment count.

When the current inventory, exposure, traffic, capacity, maturity, or authorization state is unavailable, mark the schedule and new exposure decision unresolved. State that no new exposure is supported or authorized by the program record; do not label an unknown live system `0%`, imply existing tests stopped, or create placeholder dates and allocations.

## Apply Risk-Tiered Preflight Gates

Use `verified ready`, `bounded pilot only`, `specified not verified`, `verified blocker`, `unavailable`, or `not applicable` for each gate:

1. decision and owner;
2. ethics, customer value, reversibility, and harm;
3. eligibility, unit, assignment, exposure, identity, variants, and implementation;
4. OEC or primary metric, practical threshold, guardrails, invariants, and long-term outcome;
5. baseline, variance, sample, power inputs, duration, maturity, exclusions, multiplicity, and sequential rules;
6. interference, concurrency, contamination, carryover, and external change;
7. logging, lineage, data quality, SRM, monitoring, analysis population, and corrections;
8. privacy, security, market, domain, approval, authorization, stop, rollback, expiry, and audit.

Preflight occurs before exposure. Low-risk reversible work may use contracted self-service and automated checks. Shared surfaces, irreversible exposure, safety, sensitive data, pricing, financial, network, regulated, or high-scale decisions require stronger specialist and accountable review. A gate does not launch an experiment.

## Maintain A Quality Incident Ledger

| Field | Requirement |
| --- | --- |
| Incident | Stable ID, type, detection time, source, affected experiments, populations, metrics, decisions, and period |
| Failure | Eligibility, assignment, exposure, identity, logging, metric, guardrail, SRM, peeking, multiplicity, interference, implementation, analysis, or platform state |
| Impact | Evidence integrity, customer harm, decision risk, downstream artifacts, and unknown residual |
| Response | Hold interpretation, request stop, invalidate, correct, reanalyze, rerun, recover, communicate, or unresolved |
| Governance | Owner, reviewers, authorization, correction version, audit, recurrence, review, expiry, and residual risk |

Do not suppress incidents, overwrite affected results, or keep a test valid to improve program metrics. More detection may initially raise the reported rate. Measure coverage, time to detection, containment, recovery, repeated failure, affected decisions, and correction adoption separately.

## Govern Maturity And Readout

For every metric preserve definition, entity, denominator, source, window, cutoff, expected delay, censoring, maturity date, missingness, and quality state. Missing, delayed, immature, censored, and suppressed are not zero.

Keep preregistered, amended, and exploratory analysis separate. Track sample counts, assignment, exposure, treatment and control values, absolute and relative effects, uncertainty, quality checks, guardrails, practical threshold, population, maturity, and assumptions. A positive point estimate, significance label, or dashboard winner does not establish practical value or validity.

Use result states from the owning `growth-measurement` record: meaningful benefit with guardrails passing; harm or guardrail breach; directionally useful but below threshold; practically flat under a valid boundary; inconclusive; or invalid. The program cannot upgrade a weak result to fill a portfolio narrative.

## Trace Decision And Follow-Through

Maintain this chain by stable IDs and versions:

```text
specification -> approval -> authorization -> assignment -> exposure
-> implementation -> mature readout -> recommendation -> accountable decision
-> follow-through -> completion proof -> mature downstream outcome -> reopen status
```

Record deviation, override, rationale, owner, date, dependency, and expiry. Shipping, stopping, or publishing is follow-through evidence, not customer or business impact. Reconcile retained value, contribution, cash, quality, trust, and harm only when compatible mature evidence exists. Do not attribute all company movement to the experiment.

## Operate Long-Term Validation

For each proxy or shipped decision record intended long-term outcome, causal rationale, population, metric versions, horizon, novelty and decay expectations, holdout or alternative follow-up, maturity, calibration, drift, guardrails, delayed harm, owner, expiry, and reopen rule.

Maintain long-term validation as a protected portfolio class. Do not remove holdouts solely to maximize exposure. Use them only when ethical, feasible, and decision-relevant. If a holdout is not valid, define the strongest bounded alternative and its causal limits.
