# Message Contract

## Intake Gate

Capture these fields without merging them:

- primary mode;
- ICP and a user-supplied bounded recipient identity;
- sender's real identity and organization;
- relationship and contact source;
- personalization evidence and capture details;
- problem hypothesis, offer, proof, and CTA;
- market, language, locale, and channel;
- sequence limit and owner-approved cadence;
- permission, consent, legal or policy review, opt-out, do-not-contact, and suppression state;
- available public or supplied artifacts and their scope.

A final or sendable draft requires a bounded recipient, real sender, selected channel, sufficient evidence for every factual statement, and a resolved permission record for the intended contact. A local review draft may retain pending legal or platform review only when the bounded permission basis, account-policy status, and stop state are supplied; pending review remains visible and blocks every external action. It must carry both exact literals `local review only` and `not final or sendable`; both labels are required and not paraphrasable. A sequence also requires an owner-approved limit and cadence. An approved count plus bounded window is sufficient for draft-only sequencing; do not invent exact dates or times. A follow-up requires the captured conversation state. When a blocker remains, return the known context, blocking gaps, smallest questions that can resolve them, useful public or supplied evidence, and a handoff. Do not fill gaps with invented copy.

## Draft Package

When the intake gate passes, deliver:

1. **Boundary record**: mode; recipient; sender; market; language; locale; channel; source scope; sequence limit; both exact labels when pending review restricts the output.
2. **Permission record**: relationship/contact source; intended recipient; market; channel; sender; purpose; owner or legal review; platform/account policy; opt-out and do-not-contact state; unresolved items.
3. **Message drafts**: subject where applicable, body, CTA, and visible refusal or opt-out path appropriate to the approved context.
4. **Personalization/source ledger**: one row per factual or personalized statement.
5. **Cadence**: owner-approved, context-specific timing only. For a single message, state that no further touch is planned.
6. **Stop register**: applicable stop events and current status.
7. **Channel/market notes**: only supported, current, provider-specific constraints.
8. **Measurement events**: event name, definition, source, availability, and owner. Never invent channel capabilities or a benchmark.
9. **Unresolved permission/evidence**: every open review, missing source, or unsupported claim.
10. **Handoff**: draft review and any separately authorized next task. Drafting is not approval to act.

## Personalization/Source Ledger

Use one row for each claim:

| Statement ID | Draft text or claim | Recipient relevance | Source title/ID | Public or supplied | Publisher/owner | URL or artifact locator | Capture/retrieval date | Evidence state | Signal status | Inference basis | Confirmation step | Allowed use | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rules:

- Every personalization statement needs a captured public source or attributable supplied artifact.
- A source must support the exact statement, not merely the topic.
- A working hypothesis uses `inferred`, names its basis, and is phrased as a possibility or question. Never state it as the recipient's fact.
- An owner-only assertion uses signal status `reported signal` and a blank evidence state. Keep it out of the draft until independently supported when it affects a factual claim.
- Do not place private URLs, raw contact details, or unnecessary personal data in the ledger or output.

## Message Decisions

Keep the message proportionate to the channel and relationship. Establish the legitimate context, use at most the supported personalization needed for relevance, distinguish the problem hypothesis from known facts, state only verified offer/proof, use one low-friction CTA, identify the sender honestly, and make refusal easy. Do not manufacture familiarity, urgency, scarcity, a prior thread, a referral, or a recipient event.

`localization` is message design for the declared market, language, locale, channel, and relationship, not sentence-by-sentence translation. Preserve factual meaning and permission boundaries while rewriting syntax, register, salutation, CTA, and opt-out language natively. For China in Simplified Chinese, use native Simplified Chinese; do not import English cold-email idioms.

## Stop Register

Stop the recipient immediately on any of these states:

- reply, including a question or objection;
- opt-out or do-not-contact request;
- complaint;
- hard bounce or invalid contact;
- permission withdrawal;
- material change in recipient, sender, purpose, offer, relationship, market, channel, or evidence;
- sequence end;
- owner-defined suppression.

Do not draft a scheduled follow-up after a stop. Record the reason and provide a local owner handoff. Do not write the stop state to an external system unless a separate task explicitly authorizes that write and the capability is reviewed.

## Measurement

Define only events supported by the declared channel and available tools. Candidate local events include `draft prepared`, `owner approved`, `message sent`, `delivery confirmed`, `hard bounce`, `reply received`, `opt-out received`, `complaint received`, `meeting outcome recorded`, and `sequence stopped`. Availability is contextual: omit or mark unavailable any event the platform or supplied artifacts cannot expose. Report counts or rates only from supplied attributable data. Do not use universal reply, meeting, cadence, or touch-count benchmarks.
