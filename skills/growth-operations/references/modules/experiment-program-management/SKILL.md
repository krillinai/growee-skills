---
name: experiment-program-management
description: Use when a team needs to audit, design, or refresh an experimentation program, experiment portfolio, intake process, shared traffic and capacity plan, concurrency policy, pre-exposure quality gate, incident system, maturity queue, decision follow-through ledger, long-term validation portfolio, evidence repository, or program health and governance model across multiple experiments and teams.
---

# Experiment Program Management

Turn many experiments and alternative evidence designs into a trustworthy decision system. Govern which uncertainties enter, how scarce traffic and capacity are allocated, where concurrent interventions collide, when evidence is ready, how incidents and inconclusive results remain visible, and whether learning changes later decisions. Experiment volume and win rate are activities, not program outcomes.

Read [program-contract.md](references/program-contract.md) before accepting program scope, experiment inventory, states, owners, systems, periods, evidence, or health claims. Read [portfolio-intake-and-prioritization.md](references/portfolio-intake-and-prioritization.md) before accepting ideas, classifying work, comparing decision value, or allocating traffic and capacity. Read [traffic-quality-and-evidence-operations.md](references/traffic-quality-and-evidence-operations.md) before defining concurrency, preflight gates, incidents, maturity, readouts, follow-through, or long-term checks. Read [learning-governance-market-and-actions.md](references/learning-governance-market-and-actions.md) before governing reuse, program health, decision rights, market transfer, personal data, or external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Inspect a current experimentation program for selection, contract, quality, traffic, capacity, interference, maturity, learning, follow-through, or governance failures |
| `design` | Build an evidence-bounded program contract, portfolio, operating gates, cadence, repository, and health system |
| `refresh` | Version the program after strategy, traffic, capacity, evidence maturity, incidents, proxy validity, long-term outcomes, platform, or governance changes |

Name one primary mode and state `draft`, `reconciling`, `decision-ready`, `approved-record`, `active-record`, `superseded`, or `expired`. A record state does not prove approval, assignment, exposure, completion, adoption, or impact.

Route one experiment or alternative evidence design, including assignment, power, analysis, and readout, to `growth-measurement`; company strategy to `growth-strategy`; cross-functional resources to `growth-operations`; platform capability and sourcing to `growth-operations`; team structure to `growth-operations`; and broad recurring business review to `growth-operations`. This Skill owns the multi-experiment portfolio and operating system, not each specialist analysis or external execution.

## Freeze The Program Contract

Record program ID and version, mode and state, decision purpose, accountable program owner, portfolio and decision owners, contributors, platform and data owners, required specialist reviewers and approvers, company or product scope, business models, customers and participant roles, markets and locales, fiscal and calendar periods, evidence cutoff, planning and maturity horizons, strategy and metric versions, systems and access boundary, prior program version, review and expiry, privacy boundary, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Keep request, recommendation, decision, approval, authorization, assignment, eligibility, exposure, implementation, result, follow-through, verification, and customer or business outcome separate. Do not invent experiments, traffic, capacity, assignment, results, power, validity, causal effects, decisions, approvals, adoption, or impact.

## Gate Program Targets And Operating Commitments

Set numeric targets, percentages, ratios, score weights, deadlines, service levels, retention periods, throughput ceilings, traffic allocations, reserves, schedule phases, meeting cadences, risk-tier thresholds, or approval matrices only when a complete inventory and denominator, current baselines, compatible definitions, traffic and capacity model, maturity and incident evidence, decision needs, risk policy, accountable owners, and approval authority support them. An executive goal, desired experiment count, win rate, generic best practice, or need to start immediately does not pass this gate.

If any decision-critical input is unavailable, keep the state `draft` or `reconciling`. Preserve user-supplied numbers as requests or diagnostic scenarios, but do not replace them with invented precision. Return disaggregated metric contracts with current values and targets marked unavailable, a nonnumeric operating structure, the first limiting gate, evidence requests, and conditions for a later target or operating version. Do not express unavailable authorization or traffic as `0%`; say that new exposure is not supported or authorized while preserving the unknown current state.

## Build Complete Intake And Inventory

Require each item to name a bounded decision, owner, important uncertainty, customer and business relevance, current evidence, mechanism, credible alternative, eligible population, controllable intervention or evidence source, intended outcome, meaningful threshold, guardrails, maturity, risk, required resources, dependencies, decision states, follow-through, expiry, and external-action boundary. A solution, feature, button color, stakeholder request, or hypothesis count is not sufficient intake.

Maintain proposed, incomplete, rejected, queued, gated, approved-record, authorized-record, exposed-record, stopped, cancelled, expired, maturing, readout-ready, decided, follow-through-pending, verified, invalid, and superseded states as applicable. Preserve negative, flat, harmful, invalid, underpowered, cancelled, and inconclusive work. Do not optimize the repository or program by deleting unfavorable evidence.

## Construct The Decision Portfolio

Classify work as `core optimization`, `adjacency`, `exploration`, `system quality`, or `long-term validation` only when the decision purpose fits. Do not impose universal ratios, equal team quotas, executive-first ordering, or one opaque score.

Compare decision importance, customer value, strategic relevance, uncertainty reduction, current evidence, causal need, traffic, sensitivity, maturity, engineering and analysis capacity, decision-owner attention, dependencies, interference, reversibility, risk, opportunity cost, and expected next decision on compatible bases. Preserve system quality, guardrail, proxy-validation, and delayed-outcome work that prevents attractive short-term tests from consuming the program.

When the operating gate does not pass, do not invent queue order, portfolio ratios, quotas, score weights, reserves, dates, or owners. Define the comparison dimensions and unresolved conflicts only.

## Reconcile Traffic, Capacity, And Concurrency

Time-phase eligible populations, identities, randomization units, product surfaces, markets, traffic, minimum sensitivity, maturation windows, holdouts, engineering, data, platform, analysis, specialist review, support, and decision-owner capacity. Do not double-book users, samples, people, systems, or review attention or treat overlapping populations as independent capacity.

Do not publish a calendar, traffic percentage, sample plan, duration, wave, sequence, randomization unit, power threshold, or readout date until the owning experiment specifications and program capacity records support it. A recommendation to withhold new exposure is not a verified `0%` system state and does not stop existing exposure.

Map namespaces, layers, mutual exclusion, interaction designs, sequencing, carryover, washout, novelty, contamination, spillovers, cross-device and cross-product identity, network interference, shared metrics, and concurrent product, price, channel, or market changes. Sequence or explicitly model collisions; never assume simultaneous interventions are independent.

## Gate Evidence Before Exposure

Use risk-tiered gates for decision, ethics and reversibility, eligibility, assignment, exposure, identity, variants, metric versions, minimum meaningful effect, power inputs, maturity, SRM and invariants, interference, privacy, security, customer protections, analysis rules, stop, rollback, correction, owner, approvers, expiry, and audit. Reversible low-risk work can use governed self-service; shared-surface, irreversible, sensitive, financial, safety, network, or high-exposure work requires stronger review.

Do not default every question to a 50/50 user-level A/B test. When randomization is infeasible, unethical, underpowered, too slow, or dominated by spillovers, route the decision to the strongest bounded qualitative, offline, simulation, switchback, time-series, threshold, matched, pilot, or other evidence design. Do not relabel observational evidence as randomized evidence.

## Govern Quality Incidents

Track SRM, eligibility, assignment, exposure, identity, missing or delayed events, metric drift, invariant, guardrail, peeking, multiplicity, interference, implementation, analysis, correction, and platform incidents. Record detection, time, affected units and decisions, severity, evidence, containment, validity effect, owner, correction, recovery, recurrence, residual risk, and review.

Do not hide incidents to improve a rate. More detection can initially increase reported incidents. Use `continue interpretation`, `hold interpretation`, `stop exposure request`, `invalidate`, `correct and reanalyze`, `rerun`, or `unresolved` only when supported. Route platform remediation to `growth-operations` and individual validity to `growth-measurement`.

## Manage Maturity, Decisions, And Follow-Through

Maintain metric-specific maturity dates and frozen preregistered, amended, and exploratory layers. A positive point estimate, statistical significance, dashboard label, or stakeholder preference is not a conclusive result. Preserve power, uncertainty, practical threshold, SRM, guardrails, interference, tested population, and result state.

Trace specification, authorization, assignment, exposure, implementation, readout, recommendation, decision, follow-through, verification, mature customer value, business outcome, economics, guardrails, reversal, and reopen status separately. Shipping is not realized value. Do not attribute total company movement to one experiment.

## Build Long-Term Validation And Reusable Learning

Record every proxy's intended long-term outcome, mechanism, population, horizon, calibration, limitations, drift, novelty, decay, and revalidation trigger. Maintain bounded holdouts or alternative follow-up when ethical and feasible. Include retention, quality, trust, support, ecosystem effects, and delayed harm. Define reopen, constrain, rollback, or retire rules.

A document, repository row, search, citation, or training session is not learning reuse. Verify reuse only when prior evidence changes or preserves a later decision, design, metric, model, guardrail, stop rule, standard, or retired practice. Preserve applicability, counterevidence, transfer limits, corrections, superseded versions, expiry, and repeated mistakes.

## Measure Program Health Without Gaming

Keep reliability, adoption, efficiency, question quality, validity, conclusiveness, decision cycle, follow-through, learning reuse, long-term calibration, mature customer and business outcomes, incidents, and risk separate. Experiment count, win rate, setup speed, platform uptime, self-service adoption, publication volume, and citations cannot prove better decisions or growth.

Define each health measure's entity, eligible population, numerator, denominator, source, window, maturity, segmentation, baseline, owner, decision use, gaming risk, and review trigger before setting a target. When those fields are unavailable, provide the metric contract without a target, deadline, service level, or maturity stage.

Do not rank people by wins or use program measures for consequential employment, pricing, targeting, or service decisions. Protect negative results and honest incident reporting from performance incentives.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the contract; complete inventory and evidence states; portfolio decisions; traffic, capacity, concurrency, and opportunity cost; preflight gates and quality incidents; maturity, readout, decision, and follow-through ledgers; long-term validation and learning reuse; health, governance, market and privacy boundaries; handoffs, pinned sources, approval-ready external actions, and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated experiment, feature-flag, product, analytics, warehouse, identity, CRM, billing, finance, HR, project, support, cloud, or communication systems; export or join personal data; create experiments; assign users; change eligibility, traffic, flags, variants, metrics, data, permissions, or records; launch; stop; roll back; contact; publish; send; spend; procure; deploy; or claim execution, adoption, decision follow-through, or impact without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md); the inventory is complete; decisions precede designs; traffic and capacity are not double-booked; concurrency and interference are controlled; quality gates precede exposure; incidents and unfavorable results remain visible; maturity precedes interpretation; follow-through is not called impact; proxy and long-term outcomes are revalidated; learning reuse changes a bounded artifact; program health is disaggregated; governance is risk-tiered; market and privacy boundaries hold; specialist work is routed; and no external action occurred.
