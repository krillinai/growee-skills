---
name: growth-decision-record
description: Use when a team needs to build, audit, or refresh a durable record for one growth decision; preserve the decision question, scope, owner, alternatives, evidence, assumptions, uncertainty, tradeoffs, recommendation, decision, dissent, approval, authorization, conditions, dependencies, effective period, expiry, downstream consumers, follow-through, outcomes, corrections, and supersession without rewriting history or implying execution.
---

# Growth Decision Record

Turn one bounded growth choice into a canonical, versioned decision object. Preserve what was known, considered, recommended, decided, approved, and authorized at each cutoff; keep alternatives and dissent visible; and make conditions, dependencies, expiry, downstream consumers, follow-through, and later outcomes traceable. A meeting, message, recommendation, silence, or favorable result is not a complete decision record.

Read [decision-record-contract.md](references/decision-record-contract.md) before accepting the decision, owner, scope, authority, state, sources, or versions. Read [alternatives-evidence-and-decision-quality.md](references/alternatives-evidence-and-decision-quality.md) before recording options, evidence, assumptions, causality, scoring, uncertainty, risks, tradeoffs, or decision quality. Read [versioning-dependencies-and-follow-through.md](references/versioning-dependencies-and-follow-through.md) before assigning canonical status, effective dates, dependencies, downstream consumers, refresh triggers, corrections, follow-through, or outcomes. Read [governance-market-privacy-and-actions.md](references/governance-market-privacy-and-actions.md) before assigning decision rights, transferring across markets, using personal data, or proposing external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `build` | Create one record from supplied question, alternatives, evidence, recommendation, accountable decision, authority, and conditions |
| `audit` | Inspect an existing record for ambiguous scope, missing alternatives, evidence overreach, weak authority, stale assumptions, version conflict, or false execution claims |
| `refresh` | Add new evidence, correction, decision, approval, outcome, expiry, or supersession by version without rewriting earlier records |

Name one mode and state `draft`, `evidence-pending`, `decision-ready`, `decided-record`, `approval-pending`, `approved-record`, `authorized-record`, `active-record`, `review-required`, `paused-record`, `closed-record`, `superseded`, or `expired`. A record state does not prove an external action, implementation, completion, adoption, causal impact, or success.

Route the substantive analysis to the relevant strategy, metrics, experiment, lifecycle, channel, market, pricing, budget, organization, or infrastructure Skill. Route recurring multi-decision review to `growth-operating-review`, planning-artifact reconciliation to `growth-planning-cycle`, and after-action quality, causality, and learning to `growth-learning-system`. This Skill owns one decision's canonical record and state transitions, not the specialist analysis or execution.

## Bound One Decision

Record decision ID and version, mode and state, exact question, decision type, accountable decision owner, proposer and recommender, reviewers and approvers, stop authority, scope and exclusions, products and business models, customers and participant roles, markets and locales, metric and outcome, decision and evidence periods, cutoff, effective date, review and expiry, source access, privacy boundary, external-action boundary, current canonical version, and superseded versions.

One record contains one choice that shares an owner, authority, alternatives, effective period, reversibility, and outcome. Decompose unrelated market, pricing, budget, organization, experiment, contract, and launch choices into linked records. A parent dependency map does not replace bounded child decisions.

## Preserve Evidence And Action States

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. An attributable statement can remain a `reported signal`. Preserve exact source, owner, date, version, scope, definition, population, period, market, maturity, limitation, contradiction, and correction.

Keep proposal, signal, analysis, recommendation, decision, approval, authorization, funding, assignment, implementation, verification, outcome, causal estimate, and success separate. A Slack message, executive belief, repetition, attendance, vote, recommendation, or lack of objection does not establish all later states. Do not invent consensus, authority, evidence, confidence, approval, or execution.

## Gate Governing Fields

Populate `decided-record`, `approved-record`, `authorized-record`, `active-record`, canonical status, accountable ownership, confidence, effective date, review, expiry, acknowledgement, or propagation only from attributable evidence for that exact state, bounded scope, authority, conditions, and version. Record local authorship separately from organization-specific decision authority and system-of-record canonical status.

When readiness is missing, keep the record `draft` or `evidence-pending` and leave unsupported governing fields `unavailable`. Preserve user-requested owners, scores, confidence, relative dates, durations, deadlines, states, and actions only as exact reported requests with source and unsupported status. Do not convert `tomorrow`, `90 days`, `six months`, or similar requests into calendar dates; derive a review date; label them as proposed commitments; or assign roles merely to complete the template. State the minimum attributable evidence needed for each promotion without inventing an owner, deadline, acceptance, approval, acknowledgement, or action.

## Establish Baseline And Credible Alternatives

Record current-state and do-nothing baselines without assuming failure. Include credible smaller, staged, reversible, preserve, defer, partner, build, buy, compose, pause, stop, salvage, and exit alternatives as applicable. Do not use strawmen.

Compare alternatives on common customer, product, market, period, resource, economic, cash, capacity, evidence, risk, and maturity bases. Record value, evidence, counterevidence, assumptions, dependencies, costs, opportunity cost, reversibility, downside, residual obligations, decision gates, and reopen conditions. Keep incompatible views separate.

## Distinguish Decision Inputs

Keep baseline, target, opportunity, forecast, scenario, estimate, benchmark, plan, budget request, approval, actual, attribution, association, causal estimate, recommendation, and decision separate. Do not backsolve evidence or convert an aspiration into an actual.

Leadership judgment can make a decision under uncertainty when the accountable owner and authority are explicit. Record that judgment as judgment, not verified evidence. Preserve dissent and why the decision proceeds despite unavailable or contradictory evidence.

Do not call temporal order, correlation, dashboard attribution, analogy, popularity, or senior belief causal proof. State the mechanism and causal status supported by the owning analysis, alternatives, confounding, tested population, maturity, and next discriminating evidence.

## Record Tradeoffs Without False Precision

Keep customer value and harm, strategy, evidence, economics, cash, capacity, timing, dependency, concentration, privacy, security, accessibility, reliability, support, employee burden, reversibility, opportunity cost, and residual obligations separate. Noncompensable harm and verified blockers do not disappear inside ROI or a weighted score.

Use calculations only from supplied compatible inputs and show formulas, units, sources, ranges, rounding, limitations, and sensitivity. Do not invent scores, probabilities, weights, confidence, or decimal precision. A scoring aid cannot replace accountable rationale.

## Record The Decision And Authority

State recommendation, chosen alternative, accountable decision, rationale, evidence and counterevidence, assumptions, dissent, unresolved issues, tradeoffs accepted, conditions, resource boundary, risk acceptance, approvers, authorization requirements, effective period, review, expiry, scale, cap, stop, rollback, correction, and reopen rules.

Map who proposes, recommends, decides, reviews, approves, authorizes, executes, verifies, can stop, and receives escalation. Consultation is not consensus; attendance is not acceptance; consensus is not authority; decision is not approval; approval is not authorization; authorization is not execution.

## Version Dependencies And Downstream Consumers

Use one stable ID and immutable versions. Record upstream strategy, metric, forecast, experiment, budget, policy, contract, and evidence versions; downstream plan, initiative, experiment, budget, product, system, communication, and report consumers; dependencies; required updates; acknowledgement state; divergence; effective date; expiry; and supersession.

When records conflict, preserve each source and authority, reconcile decision classes and fields, and identify the canonical bounded version. Do not let downstream teams choose the most favorable record or silently overwrite conflicts.

## Refresh Without Hindsight

In `refresh`, preserve the complete ex-ante layer: evidence, assumptions, alternatives, dissent, uncertainty, recommendation, decision, approval, rationale, conditions, and cutoff. Add an ex-post layer with new evidence, outcomes, corrections, changed assumptions, follow-through, and reopen status. Record who changed what, why, from which source, and which downstream consumers reopen.

Do not backdate a mechanism, remove missed conditions, claim participants predicted outcomes, or equate good outcomes with good decisions and bad outcomes with incompetence. Link later results without rewriting the earlier decision. Route full after-action review to `growth-learning-system`.

## Govern Effective Period And Expiry

Define applicability by customer, product, market, metric, version, resource, evidence cutoff, condition, effective period, and authority. Set scheduled review and event-driven triggers for strategy, customer, product, market, price, channel, platform, metric, evidence, regulation, cost, cash, capacity, risk, incident, or dependency changes.

An expired or materially invalidated record cannot remain active by inertia. Preserve customer, contractual, system, data, financial, and decommissioning obligations when a decision pauses, stops, expires, or is superseded.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the contract; source and evidence ledger; baseline, credible alternatives, assumptions, uncertainty, tradeoffs, and recommendation; accountable decision, dissent, approval and authorization states; conditions, risks, effective period, review and expiry; dependencies and downstream consumers; version, correction, follow-through and outcome record; governance, market and privacy boundaries; handoffs, pinned sources, approval-ready external actions, and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated planning, project, finance, procurement, HR, analytics, CRM, billing, product, experiment, cloud, support, contract, or communication systems; export or join personal data; decide without authority; approve; authorize; assign work; change budgets, targets, forecasts, roadmaps, experiments, flags, products, prices, contracts, permissions, data, systems, or records; notify; contact; publish; sign; spend; hire; fire; launch; deploy; or claim propagation, execution, completion, adoption, or results without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md); one decision and owner are explicit or unavailable with the missing authority recorded; sources and evidence states remain bounded; alternatives are credible; decision inputs are not conflated; causality does not exceed evidence; false scoring does not replace rationale; unsupported governing, numeric, time, ownership, acknowledgement, and propagation fields remain unavailable; downside and dissent remain visible; recommendation, decision, approval, authorization, execution, and result are separate; applicability and expiry are explicit only when supported; canonical versions and downstream consumers reconcile; history is not rewritten; outcome quality does not become decision quality; market and privacy boundaries hold; specialist work is routed; and no external action occurred.
