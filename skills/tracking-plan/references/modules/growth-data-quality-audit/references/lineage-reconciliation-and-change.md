# Lineage, Reconciliation, And Change

## Assign Source Authority By Field And Use

A system is not universally authoritative. Define authority for each entity, field, state, period, and use:

| Source type | Typical valid boundary | Common mismatch |
| --- | --- | --- |
| Product or operational system | Created state and customer action under the product contract | retries, eventual consistency, missing instrumentation, and state reconstruction |
| Analytics | Behavioral collection and analysis under event and identity rules | coverage, consent, client loss, ad blockers, schema drift, and attribution |
| CRM | Commercial contacts, accounts, stages, owners, and activities | duplicates, manual entry, stage semantics, and stale ownership |
| Billing or payment | Invoices, charges, collections, refunds, and payment state | authorization versus settlement, retries, currencies, taxes, and chargebacks |
| Finance | Governed accounting and reporting under a defined basis | recognition timing, adjustments, consolidation, and close status |
| Experiment platform | Assignment, exposure, variants, and analysis metadata | eligibility, implementation, SRM, identity, and interference |
| Model or decision service | Features, scores, recommendations, and allowed actions | calibration, drift, leakage, override, and observed-versus-predicted confusion |

Record source owner, extraction, cutoff, version, effective period, authority, limitations, and prohibited uses.

## Build Explainable Reconciliation Bridges

Align entity, identity, lifecycle state, product, market, period, cutoff, time zone, currency, exchange rate, accounting and cash basis, maturity, and version before reconciling.

For each source pair report:

```text
source A under its contract
+ attributable additions
- attributable exclusions
+/- timing and version effects
+/- currency, refund, tax, recognition, and adjustment effects
= expected comparable source B
+ unexplained residual
```

Every bridge component needs source, owner, definition, period, calculation, evidence state, and amount or count. Preserve material unknown residuals. Do not select a favorable source or force equality with a plug.

## Trace End-To-End Lineage

Maintain stable IDs and versions for:

```text
authoritative source
-> extraction or event collection
-> ingestion and partition
-> validation and quarantine
-> transformation and join
-> identity and eligibility
-> model or rule
-> metric and aggregate
-> dashboard, export, or API
-> analysis and decision artifact
```

Record owner, code or query reference, inputs, outputs, schema, effective time, run or build ID, dependencies, tests, quality state, backfills, overrides, consumers, and retention. If lineage is supplied only as a stakeholder diagram, label it as reported rather than verified.

## Control Metric And Schema Versions

Freeze entity, eligibility, numerator, denominator, event or state, window, cohort, exclusions, currency, accounting basis, source, code, and owner for each metric version. For schemas record field names, types, constraints, semantics, producers, consumers, compatibility, and effective dates.

When versions change, define overlap, dual run, translation or bridge, backfill policy, validation, deprecation, downstream migration, and expiry. Keep incompatible historical segments separate. Do not choose versions by favorable output or silently mix calendar and fiscal, cash and accrual, currency, market, or maturity views.

## Audit Backfills And Corrections

For every backfill, restatement, correction, or manual adjustment record:

- change ID, type, owner, approver, reason, evidence, source and code versions;
- affected entities, populations, fields, products, markets, periods, rows, counts, and value;
- old and new values, bridge, unexplained residual, and materiality;
- validation, test environment, sample and full-scope checks, dual run, and sign-off;
- dashboards, exports, models, experiments, targets, forecasts, reports, decisions, and consumers affected;
- effective date, communication, audit, rollback, retention, expiry, and residual obligations.

Preserve original as-of data and decision artifacts. A correction does not make earlier decision owners know the revised values. Do not run a backfill, overwrite history, or claim remediation.

## Maintain A Quality Incident Record

| Field | Requirement |
| --- | --- |
| Identity | Incident ID, version, detection source and time, owner, affected systems, products, markets, periods, and consumers |
| Failure | Dimension, violated contract, observed evidence, expected state, scope, count, value, and uncertainty |
| Impact | Customer, metric, model, experiment, financial, operational, decision, privacy, security, and unknown effects |
| Response | Containment, evidence preservation, correction request, backfill plan, communication, stop, rollback, and recovery proof |
| Review | Candidate causes, alternatives, recurrence, preventive and detective controls, residual risk, review, expiry, and closure authority |

Separate detection, containment, correction, backfill, recovery, validation, closure, and downstream decision review. Do not mark an incident resolved because a pipeline reran or a dashboard looks normal.
