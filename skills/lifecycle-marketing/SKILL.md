---
name: lifecycle-marketing
description: Use when planning, drafting, reviewing, or localizing welcome, activation, transactional, retention, win-back, or campaign messaging across email, SMS, WeChat Official Accounts, Mini Program subscription messages, WeCom, or WhatsApp.
---

# Lifecycle Marketing

Plan lifecycle programs from bounded evidence and current channel permission. Public product information is enough to begin a useful blueprint. Private CRM, CDP, event, consent, account, and analytics artifacts are optional; record missing or declined private data as `unavailable`, never as failure, and do not request declined access again.

Read [program-contract.md](references/program-contract.md) for intake, classification, draft gates, suppression, evidence, cadence, measurement, privacy, outputs, and handoffs. Read [channel-gates.md](references/channel-gates.md) whenever channel choice, fallback, market, language, locale, or localization affects the task. Read [source-records.md](references/source-records.md) before making a current platform, provider, regulatory, or capability claim.

## Select One Mode

| Mode | Primary job |
| --- | --- |
| `welcome` | Establish the first expected relationship after a valid entry state |
| `activation` | Support a verified next-use milestone |
| `transactional` | Communicate a necessary service, account, or transaction state |
| `retention` | Support continued use or value realization |
| `win-back` | Invite an eligible former or inactive customer to return |
| `campaign` | Deliver a bounded non-sequence announcement or promotion |

Name one primary mode. Keep adjacent purposes separate rather than hiding promotion inside service content.

## Freeze The Context

Record these as separate fields: market; language; locale; channel; mode; message classification; bounded audience and recipient eligibility; trigger/event semantics, source, and freshness; real sender; purpose; attributable claim evidence; channel-specific permission basis; platform and account-policy status; sender, account, or template registration status where applicable; current opt-out, do-not-contact, complaint, invalid-destination, consent-withdrawal, quiet-hour, frequency-cap, and suppression state; owner/legal/platform review state; cadence; collision policy; measurement capabilities; and source artifacts.

Never infer one field from another. Chinese language does not establish China as the market. A market does not establish a channel. Account capability does not establish recipient permission. Keep WeChat Official Accounts, Mini Program subscriptions, and WeCom independent.

## Classify Before Copy

Use exactly one classification:

- `transactional/service`: necessary information tied to a verified account action, service duty, or transaction, without promotion;
- `marketing`: promotion, reactivation, upsell, campaign, or optional engagement content;
- `mixed/uncertain`: purposes are combined or the accountable owner has not resolved the classification.

Keep `mixed/uncertain` visible and route it to owner/legal/platform review. Do not draft the combined message. Remove promotional content from a transactional/service duty or handle it as a separately eligible marketing message. Never claim compliance.

## Apply Stops Before Copy

Apply current stop and suppression state before selecting content or fallback. Stop on opt-out or do-not-contact, complaint, hard bounce or invalid destination, consent withdrawal, sequence completion, material context change, stale trigger, quiet-hour or frequency-cap conflict, owner suppression, or expired/consumed subscription state.

A transactional duty can require an owner handoff. It does not authorize promotion, reuse of an exhausted permission, or automatic channel switching.

## Gate The Artifact

Produce no message copy when any final-copy field in `program-contract.md` is unresolved. Return a focused intake, program blueprint, evidence record, or owner handoff instead. Missing evidence is not a negative finding.

A tightly bounded local-review draft is allowed only when classification and every audience, sender, evidence, event, permission, account, template, suppression, cadence, and channel gate are resolved, and the sole remaining state is explicitly pending owner/legal/platform final review. The owner must explicitly authorize that review draft. Do not infer pending review, owner authorization, or completed review. If review state is absent, return no copy. Label an authorized review draft with both exact, non-paraphrasable literals:

- `restricted local review`
- `not approved for sending`

Those labels do not cure a missing permission or active stop. Keep the non-sendable boundary explicit and never claim legal or platform compliance.

## Build From Evidence

Use only attributable public artifacts or supplied records. Never invent customer state, events, consent, identities, metrics, claims, capabilities, sender/template approval, benchmarks, delivery/read/open data, or legal conclusions. Preserve source scope and separate observed facts from hypotheses.

For China work requested in Simplified Chinese, write native Simplified Chinese. Avoid imported English lifecycle idioms, fake urgency, artificial familiarity, and unnatural opt-out language. Preserve classification, facts, permission, stop logic, and unresolved review state during localization.

## Deliver In Order

Return:

1. mode, market, language, locale, channel, and artifact boundary;
2. classification record;
3. audience, sender, purpose, trigger, permission, account/template, and current stop-state record;
4. program blueprint, focused intake, handoff, or permitted local copy;
5. claim/source ledger;
6. owner-approved cadence, frequency, quiet hours, and deterministic collision result;
7. measurement-event availability;
8. unresolved evidence and accountable handoff;
9. source records for current claims and the external-action boundary.

Drafting and planning authorize local artifacts only. Do not send, publish, schedule, submit templates, access accounts, read or write CRM/CDP data, import contacts, upload lists, activate automation, monitor, or deploy. Any such action needs a separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that classification preceded copy; final-copy fields are resolved or copy is absent; active stops were applied; fallback has independent permission; promotion is absent from service content; claims are attributable; private data is minimized; future actions are not described as complete; cadence and collision rules are owner-supplied; measurement matches supplied capabilities; Simplified Chinese is native when requested; current claims have direct official source records; required review labels are exact; no compliance conclusion was made; and no external action occurred.
