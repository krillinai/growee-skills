---
name: positioning
description: Use when work needs to define evidence-backed ICPs, segments, positioning, exclusions, category choices, messages, and validation plans.
---

# ICP & Positioning

## Reuse Growee Context

At the start, read `.agents/growee-context.md` when it exists. Reuse only product, customer, market, outcome, constraint, evidence, and routing fields whose scope, definition, source, and date remain compatible; state what is reused and surface conflicts or staleness before asking for decision-changing gaps. The file grants no system access or execution authority, and this Skill must not silently rewrite the primary diagnosis.

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [ICP Segmentation](references/modules/icp-segmentation/SKILL.md)

Turn product, customer, competitive, and market evidence into a scoped reason why a specific customer should choose this product in a specific situation. Treat positioning as a versioned market hypothesis, not a slogan. Public artifacts are sufficient to begin; private research, analytics, CRM, win/loss, retention, or revenue data are optional and must be marked `unavailable` when absent.

Read [positioning-contract.md](references/positioning-contract.md) before setting scope, evidence, claims, or outputs. Read [analysis-and-validation.md](references/analysis-and-validation.md) before mapping alternatives, building value chains, choosing a category, translating the position, or proposing tests. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `build` | Create a positioning hypothesis and downstream message architecture from attributable evidence |
| `audit` | Test an existing position for scope, alternatives, differentiated value, proof, coherence, and downstream fit |
| `reposition` | Compare current and proposed positions, migration costs, evidence gaps, and validation gates |

Name one primary mode. Keep observed facts, stakeholder reports, interpretations, hypotheses, choices, and final wording visibly separate.

## Freeze The Positioning Unit

Record the decision and owner; product, edition, module, service, or bundle; customer and buying units; user, buyer, payer, and approver; trigger, job, current alternative, urgency, and decision criteria; market, language, locale, route to market, lifecycle stage, price or package context, time horizon, version, source dates, exclusions, and review date.

Split the scope when products, situations, alternatives, value priorities, proof, buying processes, or markets are incompatible. Do not force one umbrella statement across distinct positions.

## Protect Evidence And Claims

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may use signal status `reported signal` with a blank evidence state.

Public artifacts can verify visible product capabilities, current wording, price displays, public proof, and competitor claims at a dated capture. They cannot establish what customers truly compare, why they buy, realized value, prevalence, win rate, willingness to pay, retention, economics, or causality.

Never invent customer quotes, motives, alternatives, urgency, differentiation, proof, category comprehension, market size, conversion, or outcomes. Record each claim's wording, source, scope, market, date, limitation, counterevidence, owner, and approval status.

## Build The Choice Logic

Start with what the customer would do if the product did not exist: inaction, current behavior, manual work, service, general tool, adjacent product, or direct competitor. Map alternatives by buying situation, not by a generic competitor list.

For every proposed advantage, build this chain:

```text
available capability -> operational consequence -> differentiated customer value -> proof -> conditions and limits
```

Reject roadmap-only advantages and generic claims such as easy, modern, powerful, or AI-powered unless attributable evidence makes the difference, consequence, and boundary concrete. Define best-fit customers through value conditions, readiness, behavior, alternative, buying path, retention, and economics, not firmographics alone.

Choose an existing category, qualified subcategory, reframe, or new category according to buyer comprehension, useful inherited criteria, differentiation, education burden, proof, time, capital, and ecosystem support. A new label is not category creation.

## Translate Without Dilution

Produce one scoped positioning thesis, then translate it into problem and category frame, value pillars, capabilities, proof, objections, qualification, audience and stage messages, and channel requirements. Messaging may vary while the underlying position remains coherent.

Route final page or campaign copy and revisions to `copywriting`, customer evidence acquisition to `customer-research`, segment design to `positioning` when available, offers to `monetization`, campaigns to `acquisition-strategy`, sales assets to `sales-enablement` when available, and causal tests to `growth-measurement`.

## Validate The Whole Chain

Test alternatives, comprehension, value priority, proof credibility, qualification, buying behavior, promised-use-case activation, retained value, price acceptance, service burden, and economics. A headline test or click lift supports message performance only; it does not verify the full position.

When evidence is incomplete, return hypotheses and the smallest discriminating evidence plan with population, method, owner, decision date, success and contradiction signals, and downstream guardrails. Preserve evidence that weakens the preferred position.

## Deliver In Order

Return:

1. mode, decision, owner, scope, version, and review date;
2. evidence and claim ledger with counterevidence;
3. buying situations and competitive-alternative map;
4. capability, consequence, value, proof, condition, and limitation chains;
5. best-fit, prerequisite, exclusion, and disqualification conditions;
6. category decision and education burden;
7. positioning thesis and message hierarchy;
8. downstream product, acquisition, sales, activation, retention, pricing, and service implications;
9. validation plan, decision rules, owners, and handoffs;
10. Playbook references and external-action boundary.

For China work, keep market, language, locale, customer unit, product surface, category, terminology, alternatives, route to market, channel, platform, app distribution, payment, consent, claims, data access, and applicable review separate. Do not infer local platform availability, customer behavior, competitive conditions, or permission from market or language.

This Skill authorizes local analysis and artifacts only. Do not contact customers or competitors, conduct interviews, access private systems, change product or pricing, alter websites, publish messaging, launch campaigns or tests, or claim that positioning was approved or deployed without separate task-level authorization.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that scope, customer, situation, alternatives, capabilities, differentiated value, proof, best-fit and exclusion conditions, category, claims, message hierarchy, counterevidence, downstream implications, validation, owners, version, and review date are explicit; wording does not exceed evidence; public facts are not treated as customer truth; localization does not assume market equivalence; and no external action occurred.
