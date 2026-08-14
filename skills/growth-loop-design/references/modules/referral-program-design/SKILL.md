---
name: referral-program-design
description: Use when a team needs to design, audit, measure, localize, govern, taper, or stop a customer, user, employee, partner, member-get-member, refer-a-friend, invitation, advocate, or product-led referral program; define sender and recipient value, triggers, eligibility, payloads, links or codes, landing continuity, rewards, attribution, retained recipient quality, incrementality, full economics, fraud, privacy, trust, fulfillment, support, experiments, or operations without sending invitations or operating a live program.
---

# Referral Program Design

Turn delivered product value into a permission-aware path from a qualified sender to a relevant recipient, then retain only mechanisms that create incremental recipient value above full cost and harm. Optimize retained qualified recipients and participant trust, not links, invitations, signups, reward claims, attributed revenue, gross K, or referral volume alone.

Read [referral-contract.md](references/referral-contract.md) before accepting participant, eligibility, relationship, reward, identity, attribution, or performance evidence. Read [mechanism-and-experience.md](references/mechanism-and-experience.md) before selecting triggers, payloads, channels, landing states, prompts, codes, links, or rewards. Read [measurement-risk-and-operations.md](references/measurement-risk-and-operations.md) before calculating results, designing tests, defining fraud controls, or specifying operations. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `design` | Define a value-led program hypothesis, experience, controls, measurement, pilot, and operating handoff |
| `audit` | Diagnose an existing program's value exchange, path, quality, economics, trust, risk, and operations |
| `measurement` | Specify reproducible events, identity, cohorts, attribution, counterfactuals, economics, and decision rules |

Name one primary mode, decision, owner, program boundary, population, horizon, and allowed action. If evidence supports only part of the program, complete that work and mark the rest `unavailable`.

## Freeze The Referral Contract

Record product and delivered value; market, language, locale, channel, and product surface; sender, recipient, payer, administrator, platform, and business; relationship, relevance, permission, and exclusions; sender trigger, eligibility, motivation, cost, risk, and value; payload, context, message source, link or code, delivery, expiry, and recipient controls; destination, carried state, recipient job, first value, retained value, and later referral opportunity; organic, prompted, rewarded, employee, partner, affiliate, and paid paths; reward, terms, disclosure, fulfillment, reversal, liability, tax, and support; identity, deduplication, attribution, cohorts, windows, maturity, counterfactual, cost, contribution, fraud, cannibalization, fairness, privacy, complaints, capacity, owners, approvals, and requested external action.

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may be a `reported signal` with no evidence state. Public terms and visible flows do not verify private eligibility, exposure, consent, delivery, identity, reward settlement, retained quality, fraud, economics, or incrementality.

## Design From Value And Relevance

Require credible sender value before the prompt and credible recipient value after it. Define:

```text
delivered sender value -> eligible trigger -> voluntary referral action
-> relevant recipient with useful context -> qualified arrival
-> recipient first value -> retained recipient quality
-> optional later referral opportunity
```

Treat word of mouth, product invitation, customer referral, advocacy, affiliate promotion, employee referral, and paid creator distribution as different mechanisms. A shared workspace invitation can primarily enable collaboration; a referral code can primarily attribute or reward acquisition. Do not force either into the other's operating or measurement model.

Prefer a useful artifact, role, context, proof, or benefit over a generic promotional message. Preserve sender editing, channel choice, recipient controls, honest sponsorship or reward disclosure, accessibility, destination continuity, and easy recovery from invalid or expired states. Prompt timing and copy cannot repair weak value or irrelevant recipients.

## Separate Reward Design

Design the non-reward value exchange before adding incentives. If a reward is justified, state its barrier, payer, recipient, qualification event, amount, currency or unit, timing, visibility, terms, cap, expiration, settlement, reversal, tax, dispute, taper, and stop rules.

Route detailed reward incrementality, post-incentive durability, cost, cannibalization, fairness, and portfolio allocation to `growth-loop-design`. A non-cash credit still has liability, serving, support, opportunity, and trust costs. Never infer that a larger or two-sided reward improves qualified referral.

## Measure The Complete Path

Keep counts and rates for eligible senders, exposed senders, participating senders, attempts, deliveries, qualified unique recipients, relevant arrivals, recipient first value, retained recipients, reward qualification, settlement, reversal, complaints, invalid traffic, and later participation. Freeze entity, denominator, event, identity, relationship, deduplication, attribution, cohort, window, maturity, market, program version, and source.

Referral attribution assigns operational credit; incrementality asks what changed because the program, prompt, or reward existed. Preserve organic overlap, cross-channel claims, prior awareness, existing accounts, household or company identity, sender-recipient interference, and portfolio cannibalization. Do not call codes, signups, gross K, attributed revenue, or referred-user retention incremental without a credible counterfactual.

Use full marginal economics: retained incremental contribution minus rewards, fulfillment, payment, media or partner fees, discounts, support, engineering, operations, fraud loss, cannibalization, tax and compliance operations, and capacity or opportunity cost. Keep prediction and scenario assumptions separate from observed outcomes.

## Govern Risk Without Inventing Identity

Design layered controls before eligibility, during referral, before qualification, before settlement, and after fulfillment. Use the minimum data necessary for the declared risk. Preserve legitimate shared households, teams, devices, networks, payment methods, travel, and accessibility needs; a signal is not proof of abuse.

Define review, evidence, reason codes, delay, reversal, appeal, correction, support, audit log, retention, access, incident, rollback, and monitoring. Do not recommend hidden protected-trait proxies, contact-graph harvesting, dark patterns, forced sharing, preselected contacts, deceptive scarcity, undisclosed sponsorship, or punishment for declining.

## Deliver In Order

Return:

1. mode, decision, owner, scope, population, horizon, and external-action boundary;
2. participant, value, relationship, permission, evidence, and limitation ledger;
3. current-state audit or referral mechanism hypothesis;
4. trigger, eligibility, payload, channel, destination, first-value, reward, and disclosure specification;
5. event, identity, attribution, cohort, maturity, economics, and experiment plan;
6. fraud, abuse, cannibalization, fairness, privacy, trust, complaint, and support controls;
7. bounded pilot or remediation backlog with dependencies, owners, guardrails, stop rules, and completion proof;
8. operating handoffs, Playbook sources, and unresolved evidence.

Route loop closure to `growth-loop-design`; rewards to `growth-loop-design`; recipient activation to `activation`; retained recipient quality to `retention`; causal design to `growth-measurement`; events to `growth-measurement`; metrics to `growth-measurement`; customer mechanism research to `customer-research`; referral copy to `copywriting`; and broader acquisition planning to `acquisition-strategy`.

For China work, keep market, language, locale, product surface, referral mechanism, participant relationship, platform, channel, account access, message classification, consent, contact access, identity, payment, settlement, withdrawal, tax, invoice, terms, support, dispute, content review, privacy, data access, and applicable rules separate. Do not infer WeChat, WeCom, SMS, Douyin, Xiaohongshu, another platform, a payment method, contact-book permission, channel access, or program legality from China or Simplified Chinese.

This Skill creates and reads local artifacts only. Do not access product, referral, CRM, analytics, warehouse, billing, payment, messaging, contact, fraud, support, or experiment systems; upload contacts; generate live codes; expose or suppress users; send invitations; contact participants; issue, settle, reverse, or withdraw rewards; block accounts; launch, change, taper, or stop a live program; publish terms; or claim results.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that decision, participants, value, relationship, permission, trigger, eligibility, exclusions, payload, channel, destination, first value, retained quality, reward, terms, disclosure, identity, deduplication, attribution, incrementality, cohorts, maturity, full economics, fraud, cannibalization, fairness, privacy, trust, complaints, support, capacity, owners, approvals, taper, stop, and evidence states are explicit; invitations are not recipient value; attribution is not incrementality; risk signals are not proof; market conditions are not inferred from language; and no external action occurred.
