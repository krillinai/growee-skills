---
name: b2b-outbound-messaging
description: Use when drafting or localizing evidence-based one-to-one B2B outreach, a bounded message sequence, or a follow-up for a user-supplied recipient through market-appropriate business email, LinkedIn, WeCom, or WeChat business-contact contexts.
---

# B2B Outbound Messaging

Draft relevant one-to-one B2B outreach from attributable evidence and a resolved permission context. Public evidence is sufficient to begin; private CRM or contact artifacts are optional and stay within their supplied scope. Missing private data is `unavailable`, not failure.

Read [message-contract.md](references/message-contract.md) for intake, draft packages, ledgers, stop states, localization, and measurement. Read [evidence-and-safety.md](references/evidence-and-safety.md) for evidence states, permission, privacy, prohibited conduct, and external-action boundaries. Read [market-channels.md](references/market-channels.md) whenever market, language, locale, business email, LinkedIn, WeCom, WeChat, current platform behavior, or regulatory text affects the request.

## Select One Mode

| Mode | Use | Required boundary |
| --- | --- | --- |
| `single-message` | One initial message to one bounded recipient | One selected channel and no implied later touch |
| `sequence` | A bounded set of messages to one recipient/context | Owner-approved message limit, timing, and stop logic |
| `follow-up` | A response or scheduled next message in a captured conversation | Inspect reply, permission, bounce, suppression, and sequence state first |
| `localization` | Native adaptation of a supplied or approved message | Preserve facts and permission while adapting to declared market, language, locale, and channel |

If a request mixes modes, name one primary mode and keep secondary work explicit. This Skill does not discover recipients or authorize bulk outreach.

## Freeze The Context

Record ICP; recipient role/company or bounded identity supplied by the user; sender's real identity and organization; relationship/contact source; verifiable personalization evidence; problem hypothesis; offer; proof; CTA; market; language; locale; channel; sequence limits; permission/consent/legal/policy constraints; stop and suppression state; and available source artifacts.

Keep `market`, `language`, `locale`, and `channel` separate. Chinese language does not imply China as the market, and a China market does not imply business email, WeCom, or WeChat availability or permission. Channel availability never implies permission or compliance.

Before treating copy as final or sendable, resolve the permission record described in `evidence-and-safety.md`. Permission is contextual to recipient, source, relationship, sender, purpose, market, channel, owner/legal review, platform/account policy, and opt-out/do-not-contact state. Pending legal or platform review may permit a local review draft when the owner has supplied a bounded permission basis, account-policy status, and clear stop state; it blocks final/sendable status and every external action. Such a draft must carry both exact literals `local review only` and `not final or sendable`. Both labels are required and not paraphrasable. Never claim legal compliance. State that this Skill is not legal advice and owner/legal review remains responsible.

If the bounded recipient, real sender, selected channel, evidence, actual permission basis, account-policy status, or stop state is missing, stop at focused intake. An active stop blocks copy entirely. Return known context, blocking gaps, the smallest questions, useful public or supplied evidence, and a handoff. Do not fabricate a message. Do not repeatedly request private access the user declined.

## Build From Evidence

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` as evidence states. A stakeholder-only statement uses signal status `reported signal` with a blank evidence state. Every personalization statement must trace to captured public evidence or an attributable supplied artifact.

Phrase a problem hypothesis as a possibility or question and label it `inferred`; never assert it as a recipient fact. Do not invent recipient events, interests, relationships, referrals, sender identity, metrics, customers, testimonials, prices, scarcity, guarantees, awards, certifications, regulatory status, capabilities, results, or legal conclusions.

Never scrape or bulk-collect contacts, discover personal contact details, enrich profiles, infer sensitive/personal traits, expose unnecessary personal data, leak private URLs, impersonate, spoof, use deceptive `Re:`/`Fwd:`, hide opt-out, or use misleading urgency.

## Apply Stops Before Copy

Do not continue after a reply, opt-out/do-not-contact, complaint or objection, hard bounce/invalid contact, permission withdrawal, material context change, sequence end, or owner-defined suppression. A reply stops the scheduled sequence even when a direct response may later be appropriate. Record the stop and provide an owner handoff; do not draft the next scheduled touch.

Cadence must be owner-approved and specific to this recipient, purpose, market, and channel. For draft-only sequencing, an owner-approved count and bounded window are sufficient; mark exact send dates/times unresolved unless the owner supplied them. Do not introduce a universal touch count, delay, send window, reply-rate target, or benchmark.

## Deliver Or Handoff

When drafting is allowed, return in this order:

1. mode and boundary record;
2. permission record;
3. message draft or bounded sequence;
4. personalization/source ledger;
5. owner-approved cadence;
6. stop conditions and current stop state;
7. channel and market notes;
8. measurement events and availability;
9. unresolved permission and evidence;
10. local review and external-action handoff.

For China work requested in Simplified Chinese, write native Simplified Chinese rather than literal English syntax. Use current direct official sources for platform or regulatory claims and record title, URL, publisher/product, exposed date, retrieval date, exact supported claim, and limitation/access state. If direct current text is unavailable, mark the claim `unavailable`; never transfer rules across markets or platforms.

Drafting permits local text only. It never authorizes sending, connection requests, contact import, account access, CRM reads/writes, automation, list upload, bulk collection, attachments, campaign launch, or monitoring. Sending, enrichment, and contact discovery remain out of scope even if requested. Provide a separate handoff requiring task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the recipient and sender are bounded; actual permission basis, account-policy status, and stop state are resolved or drafting stopped; every pending legal/platform review draft contains exact label `local review only`; every pending legal/platform review draft contains exact label `not final or sendable`; neither required label was paraphrased; every personalization claim has a source-ledger row; evidence states are canonical; reported signals have blank evidence states; hypotheses are not recipient facts; unsupported and sensitive claims are absent; sender and subject are honest; all stop states were enforced; cadence is owner-approved; measurement uses no invented capability or benchmark; market, language, locale, and channel remain distinct; current claims have direct official source records; unresolved items are visible; and no external action occurred.
