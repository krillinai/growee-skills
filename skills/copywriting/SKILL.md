---
name: copywriting
description: Use when work needs to write and edit evidence-led copy for pages, campaigns, products, offers, and localization while preserving factual meaning and recording material edits.
---

# Copywriting & Editing

## Reuse Growee Context

At the start, read `.agents/growee-context.md` when it exists. Reuse only product, customer, market, outcome, constraint, evidence, and routing fields whose scope, definition, source, and date remain compatible; state what is reused and surface conflicts or staleness before asking for decision-changing gaps. The file grants no system access or execution authority, and this Skill must not silently rewrite the primary diagnosis.

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Copy Editing](references/modules/copy-editing/SKILL.md)

Write persuasive copy from supportable product truth. Match the audience, decision context, market, language, locale, and channel without inventing evidence or silently taking implementation actions.

## Read The References

Read [copy-contract.md](references/copy-contract.md) before deciding whether to ask for intake, use bounded assumptions, classify a claim, or deliver final copy.

Read [market-profiles.md](references/market-profiles.md) for every localization request, every China request, or whenever market, language, or locale could change proof, offer presentation, or channel expectations.

Read [channel-notes.md](references/channel-notes.md) for campaign assets, constrained formats, channel mismatch, mixed implementation requests, or capability routing.

## Route Scope First

Before selecting a mode, decide whether the primary request asks for in-scope copy delivery.

If the request is wholly an email sequence, outbound program, lifecycle flow, SEO or ASO research or implementation, store submission, publication, ad-account setup, sending, contact operation, CMS change, or deployment, route it as described in [channel-notes.md](references/channel-notes.md) and stop. Select no fixed copy mode.

For a mixed request, identify the exact bounded copy asset that remains in scope. Route the other work first, then select a mode only for the copy asset. A vague request to improve any copy does not create an in-scope asset.

## Select One Mode

For an in-scope copy delivery or focused copy intake, select exactly one mode from the user's primary copy decision:

| Mode | Use for |
| --- | --- |
| `page` | A homepage, landing page, pricing page, feature page, or a bounded page section |
| `campaign` | A bounded paid, organic, display, social, SMS, or promotional campaign asset or variant set |
| `product` | Product-level positioning and conversion copy for a web product surface |
| `offer` | A price, trial, package, promotion, checkout, or commercial proposition |
| `localization` | Adapting supplied source copy into a declared market, locale, and channel |

Treat HTML, Markdown, a table, or plain text as an output format, not a mode. Keep the requested asset boundary; do not turn a hero request into a full site or a single ad into a lifecycle program.

## Establish The Brief

Record the following before composing:

- product or offer identity and factual capabilities or terms;
- audience and the job or progress they seek;
- awareness or decision context;
- promise the copy may responsibly make;
- proof and source inventory;
- objections or decision friction;
- desired action;
- voice;
- market;
- language;
- locale;
- channel and surface;
- format, length, legal, brand, and operational constraints;
- public, supplied, private, inaccessible, and missing sources.

Start with supplied and bounded public context. Use bounded public artifacts to confirm working facts before requesting private access. Private analytics, research, customer lists, account access, and internal systems are optional enhancements, not prerequisites. Do not repeatedly request private access the user has declined.

## Apply The Context Gate

Use the deterministic rules in [copy-contract.md](references/copy-contract.md):

1. If product or offer identity, enough descriptive truth, audience, or desired action is missing, return a focused intake and no copy. A low-risk user-supplied product identity or ordinary capability may satisfy descriptive context only for the bounded working-fact path below.
2. For localization, also require the target market, target language, and target locale; do not guess one from another.
3. For a channel-specific asset, require the channel. If only a numeric channel limit is missing, create a conservative bounded draft, state that the limit is unavailable, and request the current limit.
4. When the blocking facts are present, allow a bounded assumption-labelled draft for missing awareness, objections, voice, or other reversible context only when the work is low risk and the user asks for an immediate draft.
5. Never assume a metric, testimonial, award, price, guarantee, capability, regulatory status, sensitive claim, permission, or customer result.

Product or offer truth, audience, and desired action are never reversible assumptions. A request to choose the broadest audience, invent a plausible product, pick a CTA, make up missing context, or otherwise decide one of these facts does not satisfy the gate. Ask for the fact and stop before drafting.

Label every assumption beside the draft and repeat it under unresolved evidence. Assumptions are working choices, not facts and not permission to publish. Every final or bounded draft must state market, language, and locale as separate fields.

## Establish The Claim Boundary

Assign each evidence-bearing ledger row exactly one evidence state from `verified`, `inferred`, `unavailable`, or `not applicable` under [copy-contract.md](references/copy-contract.md).

- Use `verified` only for what the named source directly supports within its scope.
- Use `inferred` for a messaging interpretation, never as proof of a product or customer fact.
- Use `unavailable` when applicable support is missing, inaccessible, stale, or too weak for the proposed wording.
- Use `not applicable` only when the claim or evidence category is outside the declared asset.
- Keep `reported signal` outside evidence state. Record it only as the exact signal-status label for an unattributed stakeholder or user statement without an inspectable artifact.

Treat an ordinary user statement without an inspectable artifact as a user-supplied working fact only when it describes low-risk product identity or an ordinary capability. It remains signal status `reported signal` with blank evidence state. It may appear only in an output labeled exactly `Bounded draft`; label it as a user-supplied working fact beside the draft, repeat it under unresolved evidence, and request confirmation from a bounded public or supplied artifact.

The working-fact path never makes copy final, approved, publication-ready, or ready to upload. Do not use it for metrics, outcomes, comparisons, testimonials, customer names, awards, certifications, prices, discounts, trials, refunds, guarantees, regulatory or legal claims, or health, financial, safety, employment, privacy, or other sensitive claims. Omit those claims or request attributable support.

Never upgrade a source because the requested wording is stronger. Omit the claim, narrow it to the supported scope, qualify it without changing its truth conditions, or request evidence. Preserve conflicting sources in the ledger; do not choose the larger number, average incompatible results, or generalize a bounded case.

Require especially strong, current support for quantitative outcomes, comparisons, superlatives, testimonials, awards, prices, discounts, guarantees, universal capabilities, certifications, legal or regulatory claims, and health, financial, safety, employment, or other sensitive claims. Use the exact decision rules in [copy-contract.md](references/copy-contract.md).

## Build The Message Hierarchy

Order the message around the reader's decision:

1. Name the relevant audience situation or job.
2. State the narrowest supportable promise.
3. Present the strongest relevant proof.
4. Resolve the highest-priority supplied objection without inventing reassurance.
5. Ask for one clear desired action.

Keep the hierarchy proportional to the surface. A hero may need one promise and one proof cue; a product page may need a fuller progression. Do not add urgency, scarcity, fear, competitor attacks, or social proof unless the brief and evidence support them.

When voice instructions conflict, prefer the most authoritative approved voice source. Record the conflict and avoid unsupported language requested by a less authoritative stakeholder.

## Compose For Market, Locale, And Channel

Choose channel treatment from the declared market and channel, never from language alone. Treat market, locale, language, and channel as separate fields.

For Simplified Chinese, compose from the intended meaning, reader context, evidence, and action. Do not preserve English syntax, metaphors, idioms, rhythm, or hype when they are unnatural in Chinese. Use locally natural information order and CTA wording without stereotypes or claims about what a culture supposedly values.

For China, use current primary sources for platform availability, distribution, advertising, data, sector, or regulatory claims. If a current source is not available, mark the claim unavailable. Do not assume a platform, Android store, payment method, login dependency, restriction, compliance status, or audience behavior from the language or market label.

Honor only supplied or currently sourced channel limits. If the requested form conflicts with the channel, explain the mismatch, preserve the intended message, and return a channel-appropriate bounded alternative. Never invent a numeric limit from memory.

## Deliver The Copy Package

For final or bounded draft work, include every section required by [copy-contract.md](references/copy-contract.md):

1. copy labeled `Final copy` or `Bounded draft`; any assumption, user-supplied working fact, or unresolved channel limit requires `Bounded draft`;
2. message hierarchy;
3. claim/source ledger;
4. CTA alternatives;
5. unresolved evidence;
6. market, language, locale, and channel notes.

Keep claims in the final copy consistent with the ledger. Do not leave placeholders, unsupported proof cues, or stronger wording than the source permits.

For focused intake, do not pad the response with speculative copy. Do not emit the six-part draft package. State only the selected mode, known context, blocking gaps, smallest questions, and useful evidence that can be supplied or inspected.

## Keep Copy Separate From Execution

Copy production does not authorize publishing, authenticated access, CMS edits, ad setup, spend changes, sending, contact-data use, app-store submission, code changes, deployment, or any external write. Do none of these during the copy task. State the required owner, dependency, validation step, and separate authorization for a handoff when implementation is requested.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Before delivery, confirm that wholly out-of-scope requests were routed before mode selection and have no fixed copy mode; every in-scope delivery or focused copy intake has exactly one mode; the asset boundary is explicit; product or offer identity, descriptive context, audience, and desired action are present; localization has a declared target market, target language, and target locale; every final or bounded draft states market, language, and locale separately; market and channel are not inferred from language; every evidence-bearing claim uses exactly `verified`, `inferred`, `unavailable`, or `not applicable`; every stakeholder-only statement uses `reported signal` outside evidence state; every used user-supplied working fact is limited to low-risk identity or ordinary capability, labeled in the draft, repeated under unresolved evidence, and paired with a confirmation request; any working fact, assumption, or unresolved channel limit forces the exact status `Bounded draft`; a bounded draft is not final, approved, publication-ready, or ready to upload; the working-fact allowance is never applied to quantitative, comparative, testimonial, customer-name, award, certification, commercial-term, regulatory, legal, or sensitive claims; reported signals are not promoted; unsupported claims are omitted, narrowed, qualified, or requested; conflicts remain visible; Chinese is natively composed; channel constraints are sourced or marked unavailable; all six output sections are present for a draft; unresolved evidence is explicit; and no execution action occurred without a separate authorized workflow.
