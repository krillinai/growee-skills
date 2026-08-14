# Shared Growth Service Contract

## Required Fields

| Area | Contract |
| --- | --- |
| Purpose | repeated decision, customer outcome, business outcome, guardrails, and exclusions |
| Consumers | named teams, roles, frequency, volume, context, current workaround, and migration commitment |
| Inputs | entities, semantics, sources, versions, identity, consent, quality, latency, and missing-data behavior |
| Outputs | decisions, recommendations, assignments, deliveries, assets, records, confidence, and allowed uses |
| Interface | API, UI, table, configuration, review queue, schema, compatibility, quotas, and deprecation |
| Reliability | availability, freshness, latency, throughput, accuracy or reconciliation, recovery, and support expectation |
| Controls | access, approvals, audit, override, fallback, stop, suppression, frequency, privacy, security, and policy |
| Operations | product owner, technical owner, data owner, risk owner, support, on-call, incident, recovery, and retrospective |
| Economics | build or vendor cost, run cost, support cost, usage unit, budget owner, and cost per useful decision or outcome |
| Health | reliability, adoption, decision, customer, risk, incident, and retirement metrics |
| Lifecycle | pilot, validation, migration, rollback, change, versioning, communication, consolidation, and retirement |

## Self-Service Gate

Allow standard self-service only when eligibility, inputs, outputs, quality, guardrails, review exceptions, logs, support, and stop controls are reliable and understandable. Unusual randomization units, sensitive audiences, high-risk actions, new markets, model changes, large budget moves, or long-maturing outcomes require stronger review.

Self-service removes avoidable queues; it does not remove accountable owners, statistical standards, privacy, market judgment, or incident duties.

## Automation Gate

Before a service acts automatically, require:

- stable objective and action boundary;
- approved inputs and prohibited features;
- attributable training, calibration, or rule evidence;
- uncertainty and abstention behavior;
- eligibility, consent, suppression, frequency, budget, and capacity constraints;
- quality, economics, trust, safety, fairness, and regulatory guardrails;
- human override, fallback, stop loss, kill switch, and degraded mode;
- versioned logs that reconstruct inputs, decision, output, and action;
- drift, incident, customer-harm, retraining, rollback, and retirement triggers.

Do not expand automation because recommendation or delivery volume is high. Expand only when downstream decision and customer outcomes remain trustworthy under the declared controls.

## Incident Contract

Define severity, detection source, triage owner, authorized containment and stop path, customer and business impact, internal and external communication, evidence preservation, recovery, validation, follow-up monitoring, root-cause review, corrective actions, and retrospective owner.

An assessment can specify these controls but cannot operate a live stop control, revoke access, change traffic, or declare recovery without separate authorized system evidence.
