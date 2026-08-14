# Growth Infrastructure Assessment Methods

## Dependency Audit

For each capability, test:

1. Does it serve a named repeated decision and customer outcome?
2. Are inputs, outputs, entities, identity, semantics, and versions stable enough to contract?
3. Are upstream sources and quality trustworthy for the downstream action?
4. Are real consumers, usage frequency, local context, and workarounds known?
5. Are reliability, support, cost, and incident ownership explicit?
6. Are downstream outcomes, guardrails, feedback, and retirement triggers measurable?
7. Can an operator override or stop the system safely?

Do not repair a dependent layer with a more polished interface. Trace symptoms upstream and verify the contract at the first broken dependency.

## Centralization Test

Score no number. Record evidence for each condition:

- multiple teams repeatedly solve the same problem;
- inputs, outputs, and service expectations are stable;
- shared quality, reliability, or compliance exceeds local alternatives;
- platform coordination and support cost is lower than duplication and queues;
- local product and market context can enter through configuration or interfaces;
- an accountable owner can operate, support, evolve, and retire the service;
- consumers accept migration and the service can demonstrate downstream value.

If most conditions are unsupported, keep the work local or standardize only the contract. If context changes the answer, centralize computation and controls rather than the accountable decision. Make overrides visible, time-bounded, attributable, and reviewable.

## Scoped Maturity

| Maturity | Evidence | Next question |
| --- | --- | --- |
| `fragmented` | manual exports, inconsistent contracts, local dashboards, campaign-specific logic | which critical fact, owner, or reconciliation must be fixed first? |
| `standardized` | shared taxonomy and definitions plus basic repeatable services | are reliability, discoverability, adoption, and ownership sufficient? |
| `self-service` | standard decisions run without central queues under guardrails | do diagnostics, training, exceptions, lineage, and support preserve trust? |
| `automated` | repeated allocation or delivery acts with feedback and controls | are objective drift, model risk, overrides, stop, and customer harm controlled? |
| `adaptive platform` | multiple products or markets reuse capabilities while preserving local control | can complexity, lock-in, portfolio conflict, and accountability remain bounded? |

Assign maturity per capability and scope. A focused team can be effective at standardized or self-service. Do not build toward a stage unless a current constraint, repeated demand, risk, or economics justifies it.

## Build, Buy, Compose, Consolidate, Or Retire

Compare the same service contract and horizon:

| Dimension | Questions |
| --- | --- |
| Functional fit | Does the option support the required workflow, entities, markets, quality, and controls? |
| Data and privacy | What data is collected, stored, transferred, retained, trained on, or exposed? |
| Reliability and latency | What are availability, throughput, recovery, degradation, and support commitments? |
| Extensibility | Which local logic is configuration, integration, fork, or impossible? |
| Ownership | Who operates, supports, reviews, migrates, and responds to incidents? |
| Economics | License, usage, implementation, integration, people, maintenance, support, opportunity, migration, lock-in, and exit cost |
| Observability and control | Logs, versions, overrides, fallback, stop, audit, exports, and portability |
| Evolution | Roadmap dependence, model or policy change, vendor viability, and retirement path |

Three-year direct-cost examples use only supplied assumptions:

    buy TCO = recurring fees + implementation + integration + migration + exit + internal operation
    build TCO = initial build + ongoing people + infrastructure + maintenance + support + migration + opportunity cost
    compose TCO = vendor core + internal differentiated logic + integration + operation + migration + exit

State whether each component is one-time or recurring. Do not choose from sticker price when material criteria or costs are unavailable.

## Health Scorecard

Measure together:

- `reliability`: freshness, completeness, reconciliation error, incidents, assignment and exposure integrity, delivery latency, retry, recovery, calibration, drift, and fallback;
- `adoption and efficiency`: active consumers, repeat use, time to trustworthy decision, self-service completion, support queue, duplicate pipelines, workarounds, and cost per useful decision;
- `decision quality`: predefined outcomes and guardrails, evidence that changes decisions, reused learning, prediction-to-observed calibration, override quality, and post-decision review;
- `customer and risk`: activation, retention, contribution, complaints, opt-outs, fraud, policy violations, cannibalization, privacy, access, audit, safety, and harm.

Show numerator, denominator, window, source, version, target basis, and owner. Internal queries, dashboard views, experiment count, sends, assets, and automated decisions are activity measures unless tied to trustworthy decisions and downstream outcomes.

## Roadmap Sequence

1. Name the decision and customer outcome being constrained.
2. Map the current workflow, systems, consumers, owners, manual work, and failures.
3. Repair critical event, identity, metric, permission, and control foundations.
4. Choose one repeated high-value workflow with real consumers.
5. Freeze the service contract, interface, quality, logs, override, stop, support, and incident path.
6. Pilot end to end and measure reliability, cycle time, adoption, decision quality, customer effect, risk, and cost.
7. Document local-versus-platform ownership and migration.
8. Add self-service or automation only after trust and demand are demonstrated.
9. Review workarounds, incidents, unused services, platform economics, consolidation, and retirement.

Each step needs an owner, due date, dependency, decision rule, stop condition, and completion proof. Do not call procurement, implementation, migration, or deployment complete without authorized system evidence.
