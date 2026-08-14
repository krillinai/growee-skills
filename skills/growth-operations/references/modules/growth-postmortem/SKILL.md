---
name: growth-postmortem
description: Use when a growth initiative, experiment, campaign, launch, pricing change, market move, system change, incident, or planning period needs a decision-ready postmortem; when an existing retrospective may contain hindsight, blame, selective evidence, duplicate impact, weak causal claims, or unactionable lessons; or when mature evidence requires a versioned refresh and operating handoff.
---

# Growth Postmortem

Turn a bounded body of growth work into an evidence-bounded record of what was known, decided, executed, observed, learned, and changed. Preserve history, separate outcome from decision and execution quality, and make learning reusable without manufacturing causality, blaming people, or executing follow-up work.

Read [postmortem-contract.md](references/postmortem-contract.md) before accepting the reviewed unit, source artifacts, evidence cutoff, state, authority, or outcome. Read [timeline-outcomes-and-evidence.md](references/timeline-outcomes-and-evidence.md) before reconstructing events, comparing plans and actuals, combining evidence, assigning impact, or naming causes. Read [decisions-learning-and-actions.md](references/decisions-learning-and-actions.md) before rating quality, retaining lessons, creating follow-up records, transferring learning, or closing the record. Read [governance-market-transfer-and-actions.md](references/governance-market-transfer-and-actions.md) before reviewing a portfolio, people, harm, incidents, markets, private data, or external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `build` | Create a postmortem for one bounded unit from supplied versioned decisions, plans, evidence, events, and outcomes |
| `audit` | Inspect an existing postmortem for hindsight, evidence selection, causal overreach, duplicate impact, blame, weak actions, and missing governance |
| `refresh` | Version a postmortem after evidence matures, a correction arrives, an action changes state, or a transfer claim is tested |

Use one state: `draft`, `evidence-pending`, `review-ready`, `accepted`, `actions-open`, `closed`, `superseded`, or `expired`. State is not root-cause proof, approval, authorization, publication, adoption, correction, action effectiveness, system improvement, or business impact.

Use `growth-operations` for recurring current decisions and open commitments; `growth-diagnosis` for an unresolved unexpected metric change; `growth-measurement` for causal design and readout integrity; `growth-measurement` for journey credit; `growth-measurement` for forecast error and vintages; and the source initiative, campaign, launch, infrastructure, or specialist Skill for its own detailed analysis. This Skill owns retrospective reconciliation, learning, and governed handoff. It does not recreate every specialist analysis or operate a response.

## Freeze The Postmortem Contract

Record the postmortem ID and version, mode and state, reviewed unit and eligibility rule, source decision and artifact versions, accountable review owner, facilitator, contributors, decision owner and required approver, product and business model, customer and participant roles, market and locale, planned and actual periods, evidence cutoff, maturity and correction dates, scope and exclusions, evidence access, privacy boundary, intended decisions, prior and superseded postmortems, and external-action boundary.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Preserve an attributable participant account as a `reported signal`. Keep actual, baseline, target, forecast, scenario, opportunity, plan, budget, attributed value, causal estimate, recommendation, decision, approval, authorization, action, completion, adoption, and business result separate.

Do not invent source artifacts, metrics, denominators, events, effects, costs, causes, confidence, severity, approvals, assignments, dates, corrections, adoption, or results. Missing material evidence creates an `evidence-pending` record, blocked conclusion, named request, or specialist handoff; it does not become a convenient assumption.

## Reconstruct The Ex-Ante Record

Freeze what was knowable at each decision: customer problem, strategy and constraint, alternatives, assumptions, thesis and mechanism, metric contracts, baseline, target, forecast vintage, opportunity, expected range, plan, budget, capacity, dependencies, risks, guardrails, approvals, stop and rollback rules, and intended decision. Preserve rejected options, amendments, missed milestones, unknowns, contradictions, and superseded versions.

Do not replace an original baseline, forecast, plan, or rationale with final data. Create an explicit version bridge for later definitions, source revisions, corrections, assumptions, decisions, and evidence. Evaluate a decision against information, authority, alternatives, reversibility, and constraints available at the time, not only against its eventual result.

## Reconstruct The Timeline

Order attributable decisions, approvals, implementation, eligibility, assignment, exposure, adoption, customer events, metric and data changes, concurrent work, incidents, stops, rollbacks, recovery, outcome maturity, corrections, and review. Preserve event time, ingestion time, availability time, decision time, and revision time when they differ.

A launch date is not universal exposure; a rollback request is not verified rollback; a dashboard recovery is not a proven mechanism. Keep unresolved gaps and conflicting accounts visible. Do not call an initiative complete while material exposure, maturity, harm, correction, decommissioning, or residual obligations remain unresolved.

## Reconcile Plan And Actual Without Duplicate Impact

Compare compatible entities, eligibility, identities, products, markets, segments, channels, cohorts, periods, windows, maturity, currencies, conversion dates, accounting bases, sources, definitions, and versions. Use bridges or separate views when comparability fails. Immature or absent evidence is `unavailable`, not zero.

Reconstruct the chain from input and activity through implementation, eligible exposure, customer value, retained or protected value, business outcome, economics, cash, quality, trust, harm, capacity, opportunity cost, and residual obligation. Shipping, task closure, spend, traffic, utilization, or a presentation can verify activity; they cannot verify impact.

Deduplicate shared customers and value. Do not add attributed revenue, experiment lift, opportunity headroom, forecast upside, scenario value, portfolio halo, planned impact, and realized outcomes. Preserve overlap, interaction, cannibalization, residual, unresolved reconciliation, refunds, incentives, ongoing costs, displaced work, and customer harm.

## Bound Causal And Root-Cause Claims

Separate observation, temporal sequence, association, attribution, contribution, candidate mechanism, causal estimate, root-cause conclusion, and business result. Preserve the identification method, assumptions, uncertainty, tested population, interference, contamination, missingness, guardrails, and counterevidence. A before-after change, executive belief, dashboard attribution, rollback recovery, or favorable point estimate does not establish cause.

Classify each cause claim as `supported`, `plausible`, `contradicted`, `unresolved`, or `not tested`. Distinguish symptom, trigger, contributing condition, mechanism, control failure, root cause, and corrective action. Route unresolved anomalies, experiments, attribution, forecasts, metrics, economics, or incidents to their owning Skill. Never force one root cause when evidence supports several candidates or none.

## Separate Quality Dimensions

Assess outcome, customer protection, decision, evidence, execution, coordination, system, and learning quality separately. Do not create a composite score that hides tradeoffs. A good outcome can follow a weak decision; a bad outcome can follow a sound reversible decision; a negative or flat result can still produce decision-changing evidence.

Use accountable roles, decisions, interfaces, commitments, and controls. Do not rank, shame, diagnose, or assign personal fault. Employment, compensation, promotion, termination, legal, and other consequential individual judgments remain outside the postmortem.

## Convert Findings Into Durable Learning

For every retained learning, state the observation, interpretation, evidence and counterevidence, decision implication, valid scope, transfer boundary, owner, affected artifact or operating state, adoption evidence, effectiveness test, review trigger, and expiry. A lesson count, document, presentation, archive, or publication is not learning adoption.

Classify follow-up as `preserve`, `correct`, `prevent`, `detect`, `mitigate`, `investigate`, `experiment`, `reuse`, `standardize`, `retire`, or `route`. Record the proposed owner or owner role, decision and artifact, prerequisites, capacity, approval, due or maturity date, evidence gate, completion proof, guardrails, stop, rollback, escalation, expiry, and residual obligations. Generic advice such as "communicate better" or "move faster" is not an action contract.

Hand open decisions, commitments, and verification to `growth-operations`; route specialist changes to their owning Skills. A handoff record does not assign work, approve a change, or prove adoption.

## Audit Or Refresh Without Rewriting History

In `audit`, test eligibility and selection, version integrity, evidence completeness, comparison compatibility, maturity, causal claims, planned-versus-actual reconciliation, guardrails, decision and execution quality, learning contracts, action ownership, privacy, transfer, and external actions. Preserve wins, losses, flat, harmful, invalid, inconclusive, cancelled, expired, and never-launched work under one declared inclusion rule.

In `refresh`, preserve the prior postmortem and add the trigger, new evidence cutoff, matured outcomes, corrections, changed evidence states, revised conclusions, affected decisions, action-state evidence, and superseded artifacts. Never backdate knowledge, erase misses, relabel an old decision, or claim adoption from a new document.

## Handle Markets, People, Harm, And Incidents

Treat every market as a new evidence and operating boundary. Revalidate customers, product, channels, platforms, app distribution, metrics, prices, costs, payments, invoices, data, consent, advertising, calendars, support, owners, causes, remedies, approvals, and transfer tests. Translation and currency conversion do not validate transfer.

For China, distinguish market, legal entity, language, locale, product, platform, app distribution, identity, payment, invoice, data, consent, content, advertising, holidays, support, staffing, lead times, evidence, and locally accountable review. Use current direct sources and local expertise. Do not make legal, tax, regulatory, provider-availability, accounting, causal, approval, or performance conclusions.

Use aggregate, redacted, pseudonymous, minimum-necessary evidence and suppress small groups. Do not expose credentials, private messages, payment details, health or financial data, protected traits, precise locations, employee reviews, compensation, ratings, or full histories. Do not rank individuals for consequential decisions.

When active harm or an incident is reported, preserve the signal and supplied response evidence, but do not declare severity, containment, rollback, recovery, or closure without attributable proof. Route authorized response and specialist review outside the postmortem.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the contract and source manifest; ex-ante record and version bridges; timeline; planned-versus-actual outcome and economics reconciliation; causal and cause register; separate quality findings; learning and action registers; portfolio, market, privacy, incident, transfer, and governance limits; specialist handoffs; pinned sources; external-action record; and completion gate.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated analytics, data, experiment, project, CRM, billing, advertising, product, cloud, support, HR, finance, procurement, or communication systems; export or join personal data; correct records; assign work; change metrics, targets, plans, prices, budgets, permissions, or systems; pause, launch, roll back, contact, publish, send, spend, procure, deploy, or claim correction, adoption, completion, system improvement, or business impact without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md); the reviewed unit and inclusion rule are explicit; original artifacts and evidence cutoffs remain frozen; versions and timelines are traceable; comparisons are compatible; activity, outcome, attribution, causality, quality, and completion remain separate; customers and value are not duplicated; costs, harms, maturity, counterevidence, and unknowns remain visible; root causes do not exceed evidence; learning changes a bounded decision or system; actions have gates without implied authorization; market, privacy, people, and incident boundaries hold; and no external action occurred.
