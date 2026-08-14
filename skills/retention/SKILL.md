---
name: retention
description: Use when work needs to analyze and improve retention through cohorts, growth accounting, engagement, recurring value, churn, resurrection, and customer health.
---

# Retention & Customer Health

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Cohort Analysis](references/modules/cohort-analysis/SKILL.md)
- [Growth Accounting](references/modules/growth-accounting/SKILL.md)
- [Engagement Analysis](references/modules/engagement-analysis/SKILL.md)
- [Customer Health Modeling](references/modules/customer-health-modeling/SKILL.md)

Determine whether a defined cohort continues receiving recurring value at the product's natural opportunity. Work from supplied data or attributable public context. Private product, billing, CRM, support, or analytics data is optional; mark missing or declined inputs `unavailable`, never as failure.

Read [retention-contract.md](references/retention-contract.md) for intake, evidence, metric contracts, privacy, and output requirements. Read [analysis-methods.md](references/analysis-methods.md) before calculating or comparing cohorts, growth accounting, resurrection, account retention, GRR, or NRR. Read [intervention-design.md](references/intervention-design.md) for recurring-value diagnosis, churn mechanisms, lifecycle states, and intervention design. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `analysis` | Define or calculate retention, cohorts, growth accounting, survival, resurrection, or commercial retention |
| `diagnosis` | Explain an observed retention symptom through bounded recurring-value, activation, reliability, need, commercial, or mix hypotheses |
| `design` | Design a retention intervention and validation plan for a supported mechanism and eligible cohort |

Name one primary mode. A request may include secondary work, but keep calculations, hypotheses, and interventions visibly separate.

## Freeze The Retention Contract

Record the entity; cohort eligibility and start event; recurring value event; natural interval or opportunity; retention definition; cohort-age and observation cutoff; market, language, locale, and timezone; user, account, product, or revenue level; segments; source artifacts; and decision the work must support.

Do not substitute login, app open, delivery, invoice status, or page view for recurring value unless supplied evidence establishes that relationship. Do not infer daily, weekly, or monthly cadence from dashboard defaults.

## Apply Evidence Before Calculation

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder-only statement may use signal status `reported signal` with a blank evidence state.

Calculate only from supplied attributable numerators, denominators, definitions, timestamps, cohort rules, and maturity status. Preserve incomplete or right-censored periods. If the data is missing or definitions conflict, produce a measurement specification and the smallest evidence request instead of a number.

Never invent retention rates, benchmarks, causal effects, cohort membership, churn reasons, event quality, revenue, expansion, or intervention results. A correlation can nominate a mechanism; it cannot establish causality.

## Diagnose Recurring Value

Separate the observed symptom from candidate mechanisms. Examine natural frequency, activation-to-retention bridge, recurring value pattern, cohort mix, product or reliability changes, customer need, competition, commercial state, seasonality, and measurement quality.

Name a primary mechanism only when evidence distinguishes it. Otherwise preserve alternatives and make the discriminating evidence or test the next action. Keep user, account, product, and revenue retention separate.

## Design Interventions

Tie every intervention to a named mechanism, eligible cohort, current lifecycle state, expected recurring value event, measurement window, guardrails, owner, and decision rule. Prefer fixing recurring value, activation, reliability, or workflow before adding reminders, discounts, or outreach.

This Skill may specify lifecycle-message eligibility and measurement, but it does not draft message copy. Route copy to `lifecycle-marketing`. Route causal validation to an experiment-design capability when needed.

## Deliver In Order

Return:

1. mode and decision boundary;
2. retention contract;
3. evidence and data-quality ledger;
4. calculations or measurement specification;
5. findings and bounded hypotheses;
6. intervention or analysis priorities;
7. validation and experiment handoff;
8. instrumentation, owner, and unresolved-evidence handoff;
9. Playbook references and external-action boundary.

For China work, keep market, language, locale, product surface, identity level, payment state, and channel separate. Do not infer WeChat, Mini Program, WeCom, app-store, payment, messaging, or data availability from the market or language.

Analysis and design authorize local artifacts only. Do not access accounts, query production systems, read or write CRM/CDP records, change lifecycle states, launch experiments, send messages, publish, schedule, modify billing, or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the entity, cohort, value event, interval, definition, maturity, cutoff, and level are explicit; calculations reconcile to supplied data; immature cohorts are not treated as mature; bounded, rolling, bracket, opportunity, and resurrection states are not mixed; user, account, and revenue views remain separate; causal language follows evidence; interventions target recurring value; missing data remains visible; Playbook sources are pinned; and no external action occurred.
