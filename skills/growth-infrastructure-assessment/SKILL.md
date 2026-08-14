---
name: growth-infrastructure-assessment
description: Use when work needs to assess growth infrastructure and RevOps across data, metrics, experiments, revenue entities, systems, handoffs, governance, and remediation.
---

# Growth Infrastructure & RevOps

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [RevOps Audit](references/modules/revops-audit/SKILL.md)

Assess whether repeated measurement, decision, delivery, creative, and governance work should become a reusable capability, and what foundation must come first. Infrastructure exists to improve trustworthy decisions and retained customer value, not to maximize tools, events, dashboards, tests, sends, assets, automation, or maturity-stage labels.

Read [capability-contract.md](references/capability-contract.md) before accepting architecture, ownership, adoption, cost, reliability, or maturity claims. Read [assessment-methods.md](references/assessment-methods.md) before evaluating dependencies, centralization, maturity, sourcing, or health. Read [service-contract.md](references/service-contract.md) before proposing a shared service or automation. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `assessment` | Diagnose a scoped capability, architecture, operating model, incident pattern, or platform-health claim |
| `roadmap` | Prioritize a dependency-ordered sequence from foundation repair through shared service, self-service, automation, or retirement |
| `sourcing` | Compare build, buy, compose, consolidate, migrate, or retire options under one service contract and horizon |

Name one primary mode, decision, owner, customer outcome, repeated workflow, internal consumers, horizon, and external-action boundary. Public information may support visible vendor, product, policy, or organization hypotheses; it cannot establish private architecture, reliability, adoption, economics, controls, or incidents.

## Freeze The Capability Contract

Record product, market, business model, team, decision and customer outcome; current workflow, frequency, volume, consumers, local workarounds, failure modes, cycle time, and failure cost; data, identity, consent, metric, experiment, model, decision, delivery, creative, and governance dependencies; systems, vendors, interfaces, owners, access, versions, service expectations, observability, incidents, and support; reliability, adoption, decision, customer, risk, and cost evidence; local-versus-platform boundary; source, freshness, evidence state, limitations, and requested external action.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may be a `reported signal` with no evidence state. Do not score unavailable capabilities or convert a maturity stage into a universal quality grade.

## Audit In Dependency Order

Assess independently:

1. `data foundation`: meaningful state events, authoritative sources, identity, eligibility, consent, quality, lineage, reconciliation, and incidents;
2. `metric system`: versioned semantics, entities, denominators, windows, currency, guardrails, registry, lineage, and approved uses;
3. `experiment services`: eligibility, assignment, exposure, identity, concurrency, SRM, metrics, power, guardrails, maturity, and decision records;
4. `decision services`: objective, features, prediction or attribution boundary, calibration, drift, uncertainty, allowed actions, overrides, fallback, and retraining;
5. `execution systems`: eligibility, suppression, frequency, scheduling, localization, adapters, idempotency, retries, receipts, cost, outcomes, and stop controls;
6. `creative systems`: research, concept and asset lineage, tags, claims, rights, review, audience, placement, exposure, fatigue, cost, and downstream feedback;
7. `governance and operations`: ownership, access, logs, approvals, exceptions, override, stop, incident, recovery, retrospective, privacy, and risk separation.

Keep layers independently diagnosable. A polished interface, large warehouse, accurate model, or high delivery rate cannot compensate for a broken upstream contract or absent downstream guardrail.

## Decide What Becomes Infrastructure

Centralize or standardize when multiple consumers repeatedly solve the same stable problem, inputs and outputs can be contracted, shared quality exceeds local alternatives, coordination cost is justified, local context can enter through configuration, and an accountable owner can operate the service. Keep work local when context determines the decision, the workflow changes rapidly, reuse is low, or central ownership creates a queue.

Assign one scoped maturity only when evidence supports it: `fragmented`, `standardized`, `self-service`, `automated`, or `adaptive platform`. Higher maturity is not the goal. Choose one next disposition: `repair foundation`, `keep local`, `standardize contract`, `pilot shared service`, `scale self-service`, `automate with controls`, `compose`, `buy`, `build`, `consolidate`, or `retire`.

For sourcing, compare the same service contract, decision horizon, volumes, reliability, privacy, latency, data boundaries, extensibility, staffing, maintenance, support, observability, lock-in, migration, exit, and total cost. Calculate only from supplied compatible assumptions and expose excluded costs.

## Design One Trustworthy Service

Start with one repeated high-value workflow and real consumers. Define inputs, outputs, interfaces, configuration, service levels, quality, owners, support, adoption, cost, logs, overrides, fallback, stop, incident, migration, and retirement before adding self-service or automation.

Measure four health groups together: reliability; adoption and efficiency; decision quality; customer and risk outcomes. Internal usage is necessary but not sufficient. Optimize time to trustworthy decision and cost per useful decision or retained outcome, not raw queries, tests, sends, assets, or model actions.

## Route Specialist Work

Route event schemas and implementation QA to `tracking-plan`; metric semantics and North Star work to `growth-metrics-design`; experiment design and readout to `experiment-design`; customer and segment evidence to `customer-research` and `positioning`; causal model structure to `growth-model-design`; lifecycle messaging to `lifecycle-marketing`; ad-platform audits to the relevant ad Skill; creative or page content to the relevant content Skill; and primary growth-constraint triage and enterprise execution routing to `growth-diagnosis`.

This Skill owns capability assessment, service boundaries, sourcing, governance requirements, and roadmap sequencing. It does not implement the specialist artifacts or operate production infrastructure.

## Deliver In Order

Return:

1. mode, decision, owner, outcome, workflow, consumers, horizon, and boundary;
2. one scoped maturity and next disposition with limiting evidence;
3. capability and dependency map with current systems, owners, workarounds, and failures;
4. evidence, reliability, adoption, decision, customer, risk, incident, and cost ledger;
5. centralize-versus-local decision and service contract;
6. build, buy, compose, consolidate, migrate, or retire comparison where relevant;
7. dependency-ordered 30-, 60-, and 90-day roadmap with decision rules and stop conditions;
8. health scorecard, operating cadence, handoffs, Playbook references, and external-action boundary.

For China work, keep market, language, locale, product surface, identity, consent, purpose, storage, transfer, providers, app distribution, payments, invoices, advertising, lifecycle channels, creative review, attribution, vendors, and incident paths separate. Do not infer any platform, provider, payment, consent, regulatory, or data condition from translation or geography alone.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not access cloud, warehouse, CDP, analytics, experiment, feature-flag, CRM, billing, finance, identity, ad, lifecycle, creative, product, support, or observability systems; export production data; install or procure vendors; change schemas, permissions, identities, consent, metrics, models, dashboards, alerts, automation, traffic, budgets, or customer state; stop live systems; publish; send; spend; migrate; or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, outcome, repeated workflow, consumers, current process, dependencies, systems, owners, contracts, maturity, evidence, reliability, adoption, decision quality, customer outcomes, cost, incidents, risks, centralization boundary, service levels, overrides, stop controls, sourcing assumptions, roadmap, health metrics, and retirement triggers are explicit; upstream foundations precede dependent automation; activity is not called value; higher maturity is not assumed better; local judgment remains local where required; specialist handoffs stay bounded; Playbook sources are pinned; and no external action occurred.
