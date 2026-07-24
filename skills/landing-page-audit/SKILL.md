---
name: landing-page-audit
description: Use when a landing page, campaign destination, product page, signup page, lead form, pricing page, webinar or event page, ecommerce product or checkout page, app-install page, or market-specific entry page needs an evidence-backed conversion audit, fixed six-dimension score and evidence coverage, message-to-page continuity review, claims and proof review, CTA and friction diagnosis, form or checkout review, mobile and accessibility review, experiment roadmap, or brand-aware standalone HTML report.
---

# Landing Page Audit

Diagnose whether a bounded entry page helps the intended visitor understand the promise, trust the evidence, take a qualified next action, and continue toward first and retained value. Begin from public page evidence; analytics, session recordings, experiments, CRM, sales, or revenue data are optional. Missing private evidence is `unavailable`, never a deduction.

Read [audit-contract.md](references/audit-contract.md) before inspecting or scoring. Read [evidence-and-scoring.md](references/evidence-and-scoring.md) before assigning findings, points, coverage, priority, or tests. Read [html-report.md](references/html-report.md) only when HTML is requested. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `page` | Audit one page and its declared audience, source, intent, action, and downstream path |
| `journey` | Audit a bounded source-message-page-form-or-checkout-next-value sequence |
| `comparison` | Compare variants or competitor pages under the same audience, intent, market, device, date, and evidence card |
| `incident` | Diagnose a reported conversion decline or break with dated compatible evidence |

Name one primary mode. Treat a performance symptom stated in conversation as `reported signal` until attributable dated evidence verifies it.

## Freeze The Audit Contract

Record decision and owner; canonical URL; product and page type; audience, job, trigger, intent, lifecycle state, and exclusions; source, campaign, keyword, creative, or referrer when known; market, language, locale, device and viewport; promise, offer, proof, CTA, commitment, form or checkout, and downstream next value; capture and report date; capabilities; supplied evidence; private evidence; requested output; and external-action boundary.

Audit the actual entry page, not the homepage by default. Keep source-message continuity unavailable when the source artifact is not supplied or inspectable.

## Capture Evidence Safely

Inspect only through bounded read-only access. Record raw response, rendered page, viewport, interaction state, screenshot, performance measurement, form behavior, and downstream page separately according to capabilities actually used. Do not claim rendering, mobile inspection, submission, or measurement that did not occur.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing records. A stakeholder or platform statement without inspectable support may use `reported signal` with no evidence state.

Never fabricate conversion, bounce, scroll, attention, comprehension, rank, traffic quality, uplift, revenue, customer intent, or causality. Public page evidence can verify what was visible or operable in a dated capture; it cannot establish user behavior or business performance.

## Audit In Dependency Order

1. access, rendering, technical integrity, and interaction blockers;
2. audience, intent, source promise, product or category comprehension;
3. value, differentiation, claims, proof, trust, and objection handling;
4. information hierarchy, content sufficiency, mobile and accessibility;
5. CTA, commitment, form or checkout friction, error and success states;
6. downstream promise continuity, first value, measurement, and experiment readiness.

Aggressive gating can improve signup rate while reducing understanding, activation, retention, or trust. Optimize qualified progression and downstream value, not the page conversion rate in isolation.

## Score With Coverage

Use the fixed 100-point, six-dimension card in [evidence-and-scoring.md](references/evidence-and-scoring.md). Score only assessed applicable checks. Report:

```text
score = assessed earned / assessed applicable max * 100
evidence coverage = assessed applicable max / all applicable max * 100
```

Unavailable checks gain or lose no points but remain in the coverage denominator. Not-applicable checks are excluded from both. Every partial or fail deduction must map to one finding. Never create a numeric score from qualitative impressions or hide low coverage.

## Diagnose Before Prescribing

For each adverse result state the observation, affected scope, evidence, expected consequence as inference where not measured, alternative explanations, action, owner-ready completion condition, effort, and validation. Separate verified defects from plausible hypotheses and evidence requests.

Do not rewrite the entire page inside the audit. Provide a message architecture, wire-level content requirements, or bounded copy examples only when useful; route final copy to `copywriting`, revisions to `copy-editing`, positioning to `positioning`, and experiment design to `experiment-design`.

## Deliver In Order

Return:

1. mode, decision, scope, capture date, capabilities, and external-action boundary;
2. executive constraint and strongest verified opportunity;
3. score, evidence coverage, denominator math, and six-dimension trace;
4. source, page, interaction, downstream, and private-evidence inventory;
5. prioritized verified and inferred findings with completion conditions;
6. separate unavailable-evidence register;
7. source-message-page-action-next-value continuity map;
8. dependency-sequenced roadmap and bounded experiment backlog;
9. claim, proof, accessibility, privacy, and market limitations;
10. pinned Playbook sources and handoffs.

For China work, keep market, language, locale, audience, source, page, platform, app distribution, device, payment, invoice, identity, consent, form, messaging, data access, and applicable review separate. Do not infer WeChat, Douyin, Xiaohongshu, Baidu, an app store, a payment method, or data condition from market or language.

This Skill authorizes bounded read-only public inspection and local artifacts only. Do not submit forms, create accounts, place orders, enter personal or payment data, access private analytics or recordings, change pages or tags, deploy variants, launch tests, publish reports, or claim conversion improvements without separate task-level authorization.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that page, audience, source, intent, market, device, promise, proof, action, commitment, downstream value, capture, evidence states, scoring math, coverage, deductions, limitations, claims, privacy, accessibility, owners, completion conditions, tests, and action boundary are explicit; private missingness is not penalized; page behavior is not inferred from static source; conversion is not optimized without downstream quality; and no external action occurred.
