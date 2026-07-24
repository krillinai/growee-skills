---
name: activation
description: Use when a product needs an activation definition, first-value or time-to-value analysis, onboarding or funnel diagnosis, retained-activation validation, or evidence-bounded activation intervention design across consumer, B2B, marketplace, AI, low-frequency, or assisted products.
---

# Activation

Determine whether an eligible new user, account, or participant received meaningful first value and has a credible path to receive value again. Work from supplied data or attributable public context. Private product, analytics, CRM, implementation, support, or research data is optional; mark missing or declined inputs `unavailable`, never as failure.

Read [activation-contract.md](references/activation-contract.md) for intake, evidence, metric contracts, entry states, privacy, and output requirements. Read [analysis-methods.md](references/analysis-methods.md) before calculating or comparing activation, funnels, time to first value, quality, or retained activation. Read [diagnosis-and-design.md](references/diagnosis-and-design.md) for mechanism diagnosis, product topologies, intervention design, and handoffs. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `analysis` | Define or calculate activation, funnels, time to first value, first-value quality, or retained activation |
| `diagnosis` | Explain an observed activation symptom through bounded intent, eligibility, prerequisite, path, reliability, quality, trust, assistance, or measurement hypotheses |
| `design` | Design an activation path or intervention for a supported mechanism and eligible entry state |

Name one primary mode. A request may include secondary work, but keep calculations, hypotheses, and interventions visibly separate.

## Freeze The Activation Contract

Record the entity and level; user intent and customer job; entry state; eligible population; activation start event; first-value event and quality threshold; observation window; exclusions; value-reinforcement signal; retention-validation horizon; market, language, locale, timezone, product surface, and segments; source artifacts; owner; and decision the work must support.

Do not substitute signup, onboarding completion, clicks, screen views, invitations sent, prompts, generated output, imported data, or payment status for activation unless supplied evidence establishes that the event represents meaningful received value. Activation does not always start at signup.

## Apply Evidence Before Calculation

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder-only statement may use signal status `reported signal` with a blank evidence state.

Calculate only from supplied attributable eligibility rules, numerators, denominators, timestamps, event definitions, windows, exclusions, quality rules, and maturity status. Preserve incomplete and right-censored periods. If data is missing or definitions conflict, produce a measurement specification and the smallest evidence request instead of a number.

Never invent activation rates, benchmarks, event quality, time-to-value distributions, funnel membership, abandonment reasons, retained-activation effects, causal effects, or intervention results. An activation-retention association can validate a predictive candidate; it cannot establish causality.

## Diagnose The Path To First Value

Separate the observed symptom from candidate mechanisms. Examine acquisition promise and intent, entry-state eligibility, prerequisites, setup burden, time and waiting, errors, permissions, trust, first-value quality, collaboration or marketplace dependencies, assistance, cohort mix, measurement quality, and downstream repeated value.

Name a primary mechanism only when evidence distinguishes it. Otherwise preserve alternatives and make the discriminating evidence or test the next action. Keep user, workspace, account, participant-side, payer, and product activation separate.

## Design Interventions

Tie every intervention to a named mechanism, eligible entry state, customer job, first-value event, quality threshold, observation window, expected downstream value, guardrails, owner, and decision rule. Prefer the smallest change that removes a verified barrier while preserving necessary setup, trust, and result quality.

Do not optimize step completion in isolation. Read immediate path movement, first-value quantity and quality, retained activation, errors, support burden, trust, and economics together. Preserve original assignment and denominator through downstream validation.

This Skill may specify onboarding content requirements or lifecycle-message eligibility, but it does not draft copy or send messages. Route product or onboarding copy to `copywriting`, lifecycle-message copy to `lifecycle-marketing`, broader constraint selection to `growth-diagnosis`, downstream recurring-value analysis to `retention`, and causal validation to an experiment-design capability when needed.

## Deliver In Order

Return:

1. mode and decision boundary;
2. activation contract;
3. evidence and data-quality ledger;
4. calculations or measurement specification;
5. path and first-value findings;
6. bounded mechanisms and alternatives;
7. intervention or analysis priorities;
8. validation, instrumentation, owner, and handoffs;
9. Playbook references and external-action boundary.

For China work, keep market, language, locale, product surface, identity level, app distribution, payment state, channel, and data availability separate. Do not infer WeChat, Mini Program, WeCom, app-store, login, payment, messaging, or data conditions from the market or language.

Analysis and design authorize local artifacts only. Do not access accounts, query production systems, read or write CRM/CDP records, change onboarding or lifecycle states, launch experiments, send messages, publish, schedule, alter spend, modify product configuration, or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that customer job, entity, entry state, eligibility, start event, first-value event, quality, window, exclusions, maturity, and downstream validation are explicit; calculations preserve denominators and censoring; signup, onboarding, engagement, and activation are not conflated; entry states and product levels are not mixed; causal language follows evidence; interventions target a supported barrier and preserve value quality; missing data remains visible; Playbook sources are pinned; and no external action occurred.
