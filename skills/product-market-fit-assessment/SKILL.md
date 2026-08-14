---
name: product-market-fit-assessment
description: Use when work needs to assess product-market fit and customer journeys across problem, first and repeated value, path friction, service dependencies, and evidence boundaries.
---

# Product-Market Fit & Journey

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Customer Journey Analysis](references/modules/customer-journey-analysis/SKILL.md)

Assess whether a defined market repeatedly receives meaningful value from a product and whether the surrounding channel and business system can support the intended decision. Treat PMF as a bounded, revisable judgment supported by an evidence stack, not a company badge, survey threshold, retention curve, revenue milestone, or synthetic score.

Read [fit-contract.md](references/fit-contract.md) before collecting or interpreting evidence. Read [assessment-methods.md](references/assessment-methods.md) before assigning maturity, evaluating a must-have survey, reconciling Four Fits, or recommending expansion. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `assessment` | Evaluate a current fit claim from supplied compatible evidence |
| `measurement` | Define a decision-ready evidence plan when usable product or private evidence is missing |
| `revalidation` | Reassess fit after a segment, market, product, promise, model, channel, price, cost, competition, regulation, or expectation changes |

Name one primary mode and the decision it serves. Public evidence may support a draft fit unit and measurement plan, but cannot establish private customer behavior, survey results, economics, or distribution quality.

## Freeze The Fit Contract

Record the decision and owner; product and version; customer or participant; segment, role, account type, use case, problem, and alternative; beneficiary, buyer, payer, and decision maker; geography, market, language, locale, and period; natural frequency; first-value and repeated-value events; entity, eligibility, identity, cohort, window, maturity, and denominator; price, contribution, cost to serve, payback, and reachable market; channel and acquisition quality; trust, safety, quality, capacity, and regulatory guardrails; sources, evidence states, counterevidence, and requested external action.

Use the smallest coherent unit. Separate users, workspaces, accounts, buyers, payers, marketplace sides, atomic markets, products, tasks, and revenue where the value mechanism differs. Fit in one unit is a prior for an adjacent unit, not proof.

## Reconcile The Evidence Stack

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may be a `reported signal` with no evidence state.

Assess problem importance, first value, repeated value, declared dependence, segment concentration, organic pull, economics, distribution, and guardrails independently. Preserve dates, definitions, populations, sample selection, numerators, denominators, cohort ages, confidence or uncertainty, sources, and contradictions. Do not average unlike signals into one PMF score.

A Sean Ellis result is one declared-dependence signal. Check respondent eligibility, exposure to core value, tenure, segment, source, response rate, field dates, sample size, uncertainty, open-text reasons, survivorship, and nonresponse before interpretation. The often-cited 40 percent result is a heuristic, not certification.

Retention is repeated-value evidence only when the entity, value-bearing behavior, natural interval, cohort, denominator, and maturity are valid. A flattening curve can support a retained group; it does not prove market size, causality, margin, scalable distribution, or permanent fit.

## Evaluate The Fit System

Keep four hypotheses distinct:

| Fit | Decision question |
| --- | --- |
| Market-Product | Does the product repeatedly solve an important problem for this defined market? |
| Product-Channel | Does the product fit how this channel reaches and converts qualified demand? |
| Channel-Model | Can marginal channel economics support the business model? |
| Model-Market | Can reachable demand, price, cost, retention, and attainable share support the intended scale? |

Assign one evidence maturity: `interest`, `initial value`, `retained segment`, `viable fit system`, or `adaptive fit`. Maturity describes the strongest defensible evidence state, not company quality or a pass/fail grade. State the strongest counterevidence and what would move the claim up or down.

Use model-market arithmetic only as an explicit assumption set:

    annual revenue per customer
    x reachable customers in the defined market
    x realistically attainable share
    = potential annual revenue

Label the result a hypothesis, not a forecast. Preserve uncertainty in market definition, willingness to pay, reachability, competition, churn, contribution, share, and timing.

## Decide And Route

Choose one primary decision: `deepen`, `measure`, `scale one mechanism`, `test one adjacent unit`, `adapt`, `narrow`, or `stop`. Scaling is defensible only when repeated value, the named segment, marginal economics, channel quality, and guardrails support that bounded move. Revalidate after any material change to the fit contract.

Route interview design and synthesis to `customer-research`; durable segment, ICP, and market framing work to `positioning`; first value to `activation`; cohort construction and recurring-value mechanisms to `retention`; pricing and unit economics to `monetization`; channel planning to `acquisition-strategy`; referral or compounding mechanics to `growth-loop-design`; causal tests to `growth-measurement`; and company-wide constraint triage to `growth-diagnosis`.

## Deliver In Order

Return:

1. mode, decision, owner, and assessment boundary;
2. bounded fit claim and current evidence maturity;
3. fit unit, definitions, versions, and observation period;
4. source, evidence-quality, privacy, and contradiction ledger;
5. problem, first-value, repeated-value, dependence, segment, pull, economics, distribution, and guardrail assessment;
6. Four Fits and model-market assumptions where relevant;
7. strongest supporting evidence, strongest counterevidence, missing evidence, and confidence rationale;
8. one decision with a bounded evidence or 30-day validation plan;
9. adjacent-Skill handoffs, Playbook references, and external-action boundary.

For China work, keep market, language, locale, product surface, identity, app distribution, payment, invoice, channel, consent, regulation, and data availability separate. Do not infer WeChat, Mini Program, WeCom, Douyin, Xiaohongshu, Alipay, app-store, CRM, survey, or analytics conditions from market or language.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not access analytics, warehouse, CRM, survey, support, billing, payment, ad, product, or messaging systems; export customer data; change instrumentation, identity, onboarding, product, price, packaging, entitlements, channel, budget, or customer state; recruit or contact customers; launch experiments; publish; send; spend; or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, product, customer, segment, use case, payer, geography, frequency, period, value events, entities, cohorts, definitions, evidence states, economics, distribution, guardrails, contradictions, maturity, owner, and next decision are explicit; surveys and retention are qualified; fit units are not blended; Four Fits remain distinct; arithmetic is not promoted to forecast; no score, benchmark, causal claim, permanence, or scale recommendation was invented; adjacent Skills remain bounded; Playbook sources are pinned; and no external action occurred.
