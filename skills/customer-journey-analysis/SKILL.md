---
name: customer-journey-analysis
description: Use when a team needs to map, audit, compare, or redesign a customer journey, lifecycle path, buying journey, omnichannel experience, service blueprint, moment of truth, touchpoint system, handoff, friction, failure and recovery path, cancellation or exit path, or role-specific route from problem trigger through first and repeated value.
---

# Customer Journey Analysis

Build an evidence-bounded graph of how distinct participants move through customer-visible and backstage states to value, failure, recovery, pause, or exit. A journey map is a versioned decision model, not a decorative linear funnel, fictional persona story, complete behavioral record, implementation claim, or causal proof.

Read [journey-contract-and-roles.md](references/journey-contract-and-roles.md) before accepting customers, roles, jobs, triggers, paths, identities, sources, states, or scope. Read [paths-blueprint-friction-and-measurement.md](references/paths-blueprint-friction-and-measurement.md) before mapping transitions, touchpoints, frontstage and backstage work, dependencies, friction, failure, recovery, accessibility, metrics, or opportunities. Read [governance-market-and-actions.md](references/governance-market-and-actions.md) before handling versions, personal data, fairness, market transfer, specialist handoffs, or external actions. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `map` | Construct a current-state journey and service blueprint from supplied evidence |
| `audit` | Inspect an existing journey for missing roles, states, paths, evidence, continuity, recovery, measurement, or governance |
| `redesign` | Specify a target journey and evidence plan without claiming implementation |

Name one mode and state `draft`, `evidence-pending`, `review-ready`, `current-state-record`, `target-state-proposal`, `decision-ready`, `approved-record`, `implementation-pending`, `verification-pending`, `review-required`, `superseded`, or `expired`. State does not prove approval, authorization, implementation, exposure, adoption, customer value, business outcome, or causal impact.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. An attributable statement without inspectable support may remain a `reported signal` with no evidence state. Keep source, observation, report, interpretation, hypothesis, recommendation, decision, approval, authorization, action, verification, customer outcome, business outcome, and causal estimate separate. Do not invent personas, jobs, motives, emotions, quotes, roles, paths, touchpoints, systems, rates, causes, scores, owners, approvals, execution, or results.

## Freeze The Journey Contract

Record journey ID and version, mode and state, decision, current or target designation, product and offer version, customer and account boundary, participant roles, job and trigger, market and locale, entry and exit conditions, included and excluded paths, period and evidence cutoff, source access, journey owner, decision owner, reviewers, metric versions, review and expiry, privacy, and external-action boundary.

Use the smallest journey unit whose customer, role, job, product, market, path, owner, and outcome can be described coherently. Split journeys when participant role, product or offer, buying path, service model, market, identity, channel availability, policy, failure mode, metric, or intended outcome differs materially. A portfolio may link variants without blending their evidence or rates.

An instrumented path is not the complete journey. Record coverage and unknowns across discovery, evaluation, buying, access, product use, service, support, failure, recovery, cancellation, and exit. Treat dark, peer, offline, partner, procurement, security, workaround, and untracked paths as bounded evidence gaps unless attributable evidence supports them.

## Separate Participants And Identities

Map beneficiary, end user, administrator, champion, buyer, approver, procurement, security, payer, implementer, partner, support contact, former customer, and affected nonparticipant separately where applicable. For each role record entity, job, trigger, value, burden, authority, access, evidence, states, relationships, handoffs, failure, recovery, and exit.

Separate visitor, device, person, user, account, workspace, household, buying group, contract, transaction, invoice, support case, and revenue identities. Preserve unknown, duplicate, shared, merged, split, changed, and unresolved states. Cross-channel analytical linkage and customer-visible continuity are different problems; do not join or reidentify personal records inside a journey analysis.

Do not replace role evidence with polished fictional personas. Beliefs, motives, emotions, objections, and quotes require attributable research and explicit limitations. Route new interviews, surveys, review synthesis, and behavioral research to `customer-research`.

## Build A State Graph, Not A Universal Funnel

Define every state by eligible entity, entry rule, exit rule, observable evidence, owner, time boundary, failure state, and next possible transitions. Include only applicable states. Preserve branches, loops, skips, pauses, retries, assisted paths, reversals, nonprogression, failures, cancellations, churn, exit, and re-entry.

Separate discovery and evaluation, buying and approval, access and setup, first and repeated value, purchase and payment, support and recovery, expansion and contraction, cancellation and service end. Do not imply that every participant reaches purchase, retention, expansion, or advocacy.

Map customer action, visible interaction, employee or partner action, backstage process, system and data dependency, policy or permission, evidence, metric, failure, fallback, recovery, owner, and handoff for each material transition. A customer-facing diagram without delivery dependencies is not a complete service blueprint.

## Audit Touchpoints And Continuity

For each touchpoint record the role served, originating and destination states, customer job, channel, owner, source and content version, permission, eligibility, timing, frequency, accessibility, localization, expected response, delivery evidence, correction, expiry, and fallback. Distinguish created, delivered, viewable, exposed, interacted, comprehended, completed, and value-bearing states.

More touchpoints are not a better journey. Identify duplicated, contradictory, unnecessary, inaccessible, expired, mistimed, coercive, and missing interactions. Preserve channel switching, repeated explanation, identity loss, context loss, handoff delay, promise mismatch, status uncertainty, and customer work transferred between teams or systems.

Views, clicks, sends, calls, meetings, logins, tickets, and closures are activity signals. They do not establish comprehension, task completion, product value, problem resolution, retention, or impact.

## Diagnose Friction Without Inventing Causes

Classify friction as `value-enabling`, `necessary`, `protective`, `avoidable`, `transferred`, `deceptive`, or `unknown`. Assess effort, delay, repetition, interruption, uncertainty, cognitive load, coordination, access, risk, and trust by role and context. Security, consent, eligibility, safety, legal, financial, and customer-protection controls are not automatically waste.

Keep observed loss, reported difficulty, interpretation, candidate mechanism, root cause, and causal effect separate. A drop-off, complaint, long duration, or extra step can nominate a problem but cannot prove cause. Do not invent impact, confidence, effort, emotion, or priority scores. Compare removal, simplification, resequencing, explanation, assistance, automation, fallback, and deliberate retention only against supplied evidence and guardrails.

## Map Failure, Recovery, Accessibility, And Exit

Treat error, decline, outage, missing permission, stockout, failed verification, bad import, dispute, support, refund, workaround, retry, containment, recovery, abandonment, and residual harm as journey states when applicable. Separate ticket creation, response, closure, problem resolution, service recovery, trust recovery, and retained value.

Test paths across role, ability, accessibility need, language, literacy, device, connectivity, identity, authority, time, and assistance conditions using supplied evidence without stereotyping. Include alternate formats, proxy or assisted use, safe feedback, correction, and appeal. Accessibility is an entry, acceptance, guardrail, failure, and recovery condition, not a post-launch decoration.

Treat pause, downgrade, cancellation intent, cancellation, export, refund, deletion request, service end, residual obligation, and re-entry as first-class states. Reject hidden, confusing, forced, repetitive, or retaliatory exit friction. Prevented cancellation caused by obstruction is not retained customer value.

## Measure Transitions And Outcomes

For each metric define ID and version, entity, eligibility, numerator, denominator, identity, event or state, source, market, channel, cohort, period, window, maturity, exclusions, late data, suppression, revision, valid zero, owner, and limitation. Report counts beside rates and time or distribution where the decision requires it.

Keep supply, reach, viewability, exposure, interaction, task completion, first value, repeated value, purchase, support resolution, retention, customer outcome, business outcome, and causal effect separate. Preserve missing, unavailable, late, immature, censored, suppressed, revised, disputed, valid zero, and not applicable states. Never average incompatible entities and signals into one journey score.

Route metric contracts to `growth-metrics-design`, event and identity implementation to `tracking-plan`, quantitative transition and loss analysis to `funnel-analysis`, cohort maturity to `cohort-analysis`, attributed source credit to `attribution-analysis`, and causal validation to `experiment-design`. A journey redesign followed by improvement does not prove causality.

## Coordinate Specialist Work

Route strategy and motion to `growth-strategy` and `go-to-market-strategy`; segment evidence to `icp-segmentation`; activation, retention, monetization, expansion, referrals, and lifecycle interventions to their owning Skills; commercial lifecycle and system handoffs to `revops-audit`; product launch to `product-launch-strategy`; infrastructure and organization changes to `growth-infrastructure-assessment` and `growth-organization-design`; messages to `lifecycle-marketing`, `copywriting`, or `sales-enablement`; and implementation to separately authorized owners.

This Skill owns the journey contract, role paths, state graph, touchpoint inventory, service blueprint, continuity, friction evidence, failure and recovery map, accessibility and exit paths, transition measurement specification, journey variants, and target-state handoffs. Routing does not mean research, design, approval, execution, or verification occurred.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Deliver the journey contract and source ledger; participant, identity, job and relationship map; state graph and evidence coverage; touchpoints, continuity and service blueprint; friction, failure, recovery, accessibility and exit analysis; metric and causal boundaries; current-to-target gaps and specialist handoffs; version, market, privacy and fairness governance; pinned sources, approval-ready external actions, and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not scrape sources; conduct research without task-level authority; access authenticated analytics, CRM, billing, product, support, sales, research, identity, communication, experiment, HR, or cloud systems; export, join, or reidentify people; assign owners; contact participants; send messages; change journeys, pages, product, price, entitlement, tracking, routing, data, permissions, support, dashboards, or systems; launch tests; publish; spend; deploy; or claim research, implementation, adoption, improvement, completion, or impact without separate authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the output passes [output-contract.md](references/output-contract.md); decision, version, current or target state, customers, roles, jobs, triggers, market, boundaries, sources, evidence states, coverage, identities, states, branches, touchpoints, continuity, frontstage, backstage, dependencies, failures, recovery, accessibility, exit, friction, metrics, maturity, causal limits, privacy, fairness, specialist handoffs, and action boundary are explicit; a linear or instrumented path did not become the whole journey; fictional personas and composite scores were not invented; activity did not become value; friction did not become cause; obstruction did not become retention; specialist work was not absorbed; and no external action occurred.
