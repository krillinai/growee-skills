---
name: marketplace-growth-strategy
description: Use when a team needs to diagnose, cold-start, optimize, replicate, govern, or stop growth in a two-sided or multi-sided marketplace; define atomic market units, participant sides, hard-side constraints, supply availability, demand, discovery, matching, fulfillment, quality, cross-side retention, incentives, participant and platform economics, trust, disintermediation, or local expansion without treating aggregate scale as liquidity or network-effect proof.
---

# Marketplace Growth Strategy

Design marketplace growth around complete, valuable cross-side interactions inside a declared atomic market. Optimize reliable local liquidity, participant value, quality, trust, and contribution rather than users, listings, requests, transactions, GMV, subsidies, or geographic coverage alone.

Read [marketplace-contract-and-evidence.md](references/marketplace-contract-and-evidence.md) before accepting participant, market, supply, demand, interaction, or evidence claims. Read [liquidity-matching-and-quality.md](references/liquidity-matching-and-quality.md) before measuring liquidity, diagnosing the hard side, or changing discovery and matching. Read [cold-start-economics-and-expansion.md](references/cold-start-economics-and-expansion.md) before seeding, subsidizing, monetizing, or replicating a market. Read [governance-experiments-and-output.md](references/governance-experiments-and-output.md) before proposing ranking, experiments, trust controls, AI, or delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Private operating evidence or a stable market contract is absent |
| `audit` | Diagnose an existing liquidity, quality, retention, economic, or scale claim |
| `cold-start` | Select an atomic market, hard-side hypothesis, seeding path, and graduation gates |
| `optimization` | Improve one constrained transition in a functioning market without damaging another side |
| `replication` | Decide whether a working local market can expand, bridge, or transfer |

Name one primary mode, decision, owner, customer, participant sides, payer, product, atomic market, core interaction, horizon, and external-action boundary. If decision-critical evidence is missing, return an evidence-pending specification rather than inventing a score, threshold, forecast, or roadmap.

## Freeze The Marketplace Contract

Record:

- customers, users, providers, suppliers, buyers, requesters, payers, beneficiaries, operators, and affected nonparticipants;
- atomic market boundary across geography, time, category, use case, service promise, product version, language, and legal entity;
- supply, inventory, availability, demand, request, candidate, offer, match, transaction, payment, fulfillment, quality, review, dispute, repeat, and exit entities;
- participant value before and after the core interaction, natural frequency, eligibility, identity, deduplication, state, window, and maturity;
- discovery, ranking, response, match, acceptance, completion, cancellation, failure, refund, dispute, off-platform, and recovery rules;
- side-specific acquisition, onboarding, utilization, retention, economics, incentives, concentration, multi-homing, and disintermediation;
- trust, safety, accessibility, privacy, security, moderation, payment, insurance, support, incident, appeal, and stop controls;
- source, owner, version, as-of, period, evidence state, contradiction, limitation, expiry, and requested external action.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. Keep an attributable statement without inspectable support as a `reported signal` with no evidence state. Request only the smallest aggregate, redacted, or pseudonymous evidence that can change a verdict, dependency, gate, or handoff.

## Audit Atomic Market Health

Do not aggregate across units until participant, state, metric, cohort, incentive, market, and maturity definitions are compatible.

```text
qualified supply -> available relevant supply -> discovery and response
qualified demand -> request with intent --------> candidate and match
match -> acceptance -> payment or commitment -> fulfillment -> quality value
-> side-specific repeat and retention -> sustainable participant and platform economics
```

Track both paths and their join. Include eligible zero-activity units, no-result searches, abandoned requests, unavailable supply, nonresponse, rejection, expiration, cancellation, failed fulfillment, refund, dispute, incident, and off-platform completion.

Use one bounded verdict per atomic market and horizon:

| Verdict | Meaning |
| --- | --- |
| `working` | Complete interactions reliably meet participant value, quality, retention, trust, capacity, and marginal economic gates |
| `constrained` | One named side or transition prevents sufficient interaction completion |
| `fragile` | Activity depends on subsidy, concentration, manual intervention, temporary capacity, or weak controls |
| `congested or harmful` | More activity reduces relevance, quality, safety, economics, trust, or participant value |
| `not assessable` | Unit, entities, definitions, maturity, or compatible evidence are incomplete |
| `not applicable` | The proposed market or mechanism is outside the decision scope |

Do not create one marketplace score or infer local liquidity from global users, inventory, bookings, or GMV.

## Diagnose The Binding Constraint

Treat the hard side as a local, stage-specific hypothesis. Separate registered supply from eligible, onboarded, qualified, listed, available, discoverable, responsive, accepted, fulfilled, retained supply. Separate audience volume from eligible demand, intent, request quality, willingness to pay, timing, relevance, trust, and repeat demand.

Test geography, time, category, price, service promise, capacity, relevance, response, trust, quality, payment, fulfillment, and participant economics before buying either side. More supply can worsen utilization; more demand can worsen wait, price, quality, safety, or provider experience.

For cold start, prefer the narrowest complete market where urgent demand and adequate supply can meet. Preserve manual, managed, curated, scheduled, waitlist, single-player, concierge, guaranteed-demand, and seeded-inventory options when they create real value without fabricating activity. Graduate only after local interaction, repeat, contribution, trust, and operating gates pass.

## Protect Quality And Economics

Measure supply availability, demand, density, discovery, response, match, acceptance, fulfillment, time to value, quality, repeat behavior, side-specific retention, utilization, participant earnings or margin, contribution, incentives, concentration, support, incidents, multi-homing, and disintermediation as distributions by compatible local unit and cohort.

Reconcile transaction value, recognized revenue, variable costs, incentives, guarantees, refunds, payment losses, fraud, insurance, trust and safety, support, local operations, working capital, taxes, and other applicable costs without double counting. Use marginal post-incentive participant and platform economics for scale decisions.

Do not treat rewarded activity as incremental or permanent liquidity. Define barrier, eligibility, exposure, counterfactual, full cost, post-incentive durability, quality floor, cap, taper, pause, and stop rule; route detailed mechanism work to `growth-loop-design`.

## Distinguish Adjacent Mechanisms

Marketplace health asks whether relevant sides complete valuable interactions. It does not by itself prove:

- propagation or referral;
- a closed growth loop;
- a positive network effect from added participation;
- scale economies;
- switching costs or defensibility;
- Product-Market Fit in every market or side.

Route marginal participant value and defense to `growth-loop-design`; loop closure to `growth-loop-design`; referral mechanics to `growth-loop-design`; side acquisition to `acquisition-strategy`; activation and recurring value to `activation` and `retention`; commercial architecture to `monetization`; metrics and instrumentation to `growth-metrics-design` and `tracking-plan`; unit economics to `monetization`; causal design to `experiment-design`; trust and risk to accountable specialists; and broader constraint triage to `growth-diagnosis`.

## Govern Matching, Expansion, And Learning

Rank and match for complete participant value under explicit constraints, not predicted GMV or fee alone. Require eligible candidate definitions, objective, relevance, availability, quality, fairness, trust, concentration, exploration, reason codes, correction, appeal, human review, override, audit, stop, rollback, incident, and recovery. Keep recommendation, approval, authorization, execution, verification, and result separate.

Treat a working market and every company case as a prior, not proof. Revalidate customer need, supply shape, demand frequency, geography, time, category, price, competition, regulation, trust, economics, and operating capacity. Require each new market to pass independent readiness, launch, graduation, pause, stop, rollback, and learning gates before bridging hides weak local liquidity.

## Deliver In Order

Return:

1. mode, decision, owner, scope, horizon, atomic market, participants, payer, core interaction, and boundary;
2. one bounded local verdict with evidence coverage and limiting dependency;
3. side-specific state maps joined through discovery, match, fulfillment, quality, repeat, and exit;
4. hard-side and transition diagnosis with competing explanations;
5. liquidity, quality, retention, participant economics, platform economics, incentives, trust, and risk ledger;
6. cold-start, optimization, or replication sequence with evidence, capacity, graduation, pause, and stop gates;
7. causal measurement, governance, specialist handoffs, Playbook references, and approval-ready requests;
8. local artifacts created, external actions not taken, expiry, residual obligations, and completion status.

For China work, answer in Simplified Chinese when requested and keep market, language, locale, currency, timezone, legal entity, participant roles, geography, category, platform, app distribution, maps, identity, payment, invoice, messaging, review, moderation, data, privacy, support, vendor, staffing, labor, tax, and decision rights separate. Translation and currency conversion do not transfer a marketplace playbook.

## External-Action Boundary

Create and read local artifacts only. Do not access product, marketplace, analytics, warehouse, CRM, payment, identity, ad, support, moderation, finance, HR, procurement, or communication systems; export private or production data; recruit participants; buy demand; issue incentives; change prices, fees, eligibility, ranking, matching, payments, reviews, permissions, or policy; message participants; launch markets or experiments; spend; publish; deploy; or claim liquidity, network effects, Product-Market Fit, GMV, participant value, or business improvement without separate authorization and attributable outcomes.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm decision, participants, payer, atomic units, core interaction, hard side, supply, demand, availability, discovery, matching, fulfillment, quality, repeat, retention, incentives, participant and platform economics, trust, safety, multi-homing, disintermediation, evidence states, causal limits, dependencies, gates, owners, specialist boundaries, expiry, residual obligations, and external actions. Aggregate scale is not local liquidity; a match is not fulfillment; GMV is not contribution; subsidy is not durable value; marketplace growth is not automatically a network effect; one market is not proof of transfer; and no external action occurred.
