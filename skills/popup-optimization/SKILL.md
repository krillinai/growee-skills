---
name: popup-optimization
description: Use when a team needs to design, audit, prioritize, localize, specify, or experiment on marketing popups, modals, banners, bars, slide-ins, interstitials, overlays, exit-intent prompts, lead-capture forms, announcements, upgrade prompts, or in-product promotional messages; define audience eligibility, page context, trigger, timing, frequency, suppression, offer, copy, form, consent, dismissal, accessibility, mobile behavior, performance, measurement, downstream quality, guardrails, and rollout without changing a live site.
---

# Popup Optimization

Use interruptive UI only when it helps a qualified person make a relevant decision without blocking their current job. Optimize incremental qualified value with trust and accessibility, not popup views, email capture, click-through, immediate conversion, or attributed revenue alone.

Read [popup-contract.md](references/popup-contract.md) before accepting page, audience, trigger, permission, offer, or performance evidence. Read [experience-and-accessibility.md](references/experience-and-accessibility.md) before selecting a surface, interaction, form, dismissal, mobile, or localization pattern. Read [measurement-and-experiments.md](references/measurement-and-experiments.md) before defining events, diagnosing results, testing, or rolling out. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `audit` | Diagnose an existing popup's relevance, friction, accessibility, permission, performance, and downstream evidence |
| `design` | Specify a bounded popup hypothesis, experience, content, states, controls, measurement, and handoff |
| `experiment` | Define eligibility, assignment, exposure, outcomes, guardrails, maturity, and decision rules |

Name one primary mode, decision, owner, page or product surface, audience state, objective, market, horizon, and external-action boundary.

## Freeze The Popup Contract

Record source and page or product job; visitor, user, account, lifecycle, intent, device, market, language, locale, eligibility, exclusions, permission and suppression state; popup type, objective, value, offer, claim, proof, CTA, destination, form, fields, message classification, consent, trigger, timing, scroll or behavior condition, frequency, cooldown, session and cross-device identity, priority, collision, dismissal, close, escape, focus, background behavior, return focus, accessibility, mobile viewport, orientation, keyboard, screen reader, reduced motion, performance, SEO or platform dependency, events, outcomes, guardrails, owner, approval, and requested external action.

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder or platform statement without inspectable support may be a `reported signal` with no evidence state. Public page behavior can verify a dated rendered experience; it cannot verify internal targeting, consent, frequency, identity, experiments, downstream outcomes, or causality.

## Protect The Current Job

Classify the surface before designing:

- marketing offer or lead capture;
- announcement or product education;
- in-product upgrade or expansion;
- transactional, safety, service, legal, or consent notice;
- age, region, authentication, or access gate;
- another bounded purpose.

Do not use a marketing optimization pattern for a required safety, legal, service, privacy, or consent interaction. Do not condition access on unrelated marketing consent, preselect optional choices, hide rejection, make the close target difficult, add false urgency, disguise ads as controls, shame users, trap focus, reopen immediately, or show several competing overlays.

Trigger only after sufficient page or product context supports relevance. Preserve the primary task, back navigation, scroll position, media, form state, and error recovery. Define invalid, ineligible, already-converted, subscribed, customer, suppressed, opted-out, dismissed, completed, expired, unsupported, offline, and failed states.

## Design The Smallest Useful Surface

Prefer a non-modal banner, inline component, contextual prompt, or product-native message when interruption is not necessary. Use a modal or interstitial only when importance and timing justify focus capture. Define one primary message and action, one honest alternative or dismissal, supportable claims, sufficient proof, minimal fields, transparent value exchange, and destination continuity.

All dialogs need a programmatic name, logical focus entry, focus containment where appropriate, keyboard operation, visible focus, Escape behavior unless a valid critical reason is documented, clear close control, return focus, screen-reader state, sufficient contrast, readable text, zoom and reflow, touch targets, reduced motion, and mobile safe-area behavior. Avoid layout shift, delayed interaction, blocked content rendering, and heavy third-party scripts.

Route final copy to `copywriting`, edits to `copy-editing`, page diagnosis to `landing-page-audit`, forms and conversion paths to `funnel-analysis`, offers to `monetization`, lifecycle messages and permission to `lifecycle-marketing`, and event implementation to `tracking-plan`.

## Measure The Whole Effect

Keep eligible, assigned, rendered, viewable, exposed, interacted, dismissed, completed, qualified, consented, delivered, activated, retained, monetized, complained, opted out, errored, slowed, and harmed states separate. A render is not exposure; email capture is not permission, deliverability, customer value, or incrementality.

Measure the popup and the underlying page or product task together. Include primary task completion, abandonment, back behavior, errors, performance, accessibility, support, complaints, opt-outs, first value, retention, refunds, contribution, and repeated exposure. Preserve absolute counts and compatible entity, eligibility, identity, source, page, device, market, popup version, cohort, window, maturity, and consent definitions.

Do not use universal timing, scroll depth, exit-intent, frequency, form-field, conversion, or uplift benchmarks. Diagnose audience, offer, context, trigger, message, interaction, form, destination, product value, and measurement as separate possible mechanisms.

## Experiment Safely

Define decision, hypothesis, eligible population, randomization unit, assignment, exposure, control, treatment, primary outcome, diagnostics, guardrails, minimum meaningful effect, power or feasibility, observation and maturation windows, interference, SRM, novelty, decision rules, stop, rollback, and follow-up.

Use persistent suppression and assignment where repeated exposure matters. Check contamination across sessions, devices, pages, campaigns, and concurrent overlays. A short-term form lift cannot justify rollout when page completion, first value, retention, trust, or accessibility risk matures later.

## Deliver In Order

Return:

1. mode, decision, owner, surface, page job, audience state, objective, market, and boundary;
2. evidence, permission, offer, claim, trigger, state, and limitation ledger;
3. current experience audit or popup hypothesis;
4. surface, content, form, interaction, accessibility, mobile, performance, and destination specification;
5. eligibility, priority, collision, frequency, suppression, persistence, and failure-state rules;
6. event, identity, experiment, downstream, guardrail, and causal measurement plan;
7. dependency-ordered implementation and QA handoff with owners, approvals, stop, rollback, and completion proof;
8. Playbook sources and unresolved evidence.

For China work, keep China, language, locale, product surface, page, platform, account, message classification, phone or email collection, consent, SMS, WeChat or WeCom, Mini Program, identity, data, hosting, transfer, content review, advertising, and applicable rules separate. Do not infer a channel, account, contact permission, consent, data use, or legal condition from China or Simplified Chinese.

This Skill creates and reads local artifacts only. Do not access CMS, product, tag manager, experimentation, consent, analytics, CRM, email, SMS, messaging, account, or customer systems; collect or upload contacts; change pages, components, styles, scripts, forms, events, consent, cookies, identity, targeting, frequency, suppression, experiments, feature flags, or customer state; send messages; publish; launch; deploy; monitor live users; or claim implementation or results.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that current job, audience, eligibility, exclusions, permission, purpose, offer, claims, surface, trigger, frequency, suppression, priority, collisions, dismissal, focus, accessibility, mobile, performance, form, destination, events, identity, experiment, downstream value, guardrails, owners, approvals, stop, rollback, and action boundaries are explicit; render is not exposure; capture is not consent; local conversion is not customer value; unavailable is not failure; and no external action occurred.
