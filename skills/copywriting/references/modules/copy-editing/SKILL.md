---
name: copy-editing
description: Use when existing marketing, product, campaign, or localized copy needs editing for clarity, voice, factual support, risk, channel fit, or native market adaptation without creating a new strategy.
---

# Copy Editing

Review existing copy without silently changing factual meaning. Preserve the submitted text, return revised copy, and account for every material edit with exact spans.

## Read The References

Read [review-contract.md](references/review-contract.md) for every request.

Read [claims-and-evidence.md](references/claims-and-evidence.md) whenever copy contains factual claims, proof, prices, metrics, outcomes, comparisons, testimonials, certifications, guarantees, regulated statements, or user-supplied facts.

Read [localization-review.md](references/localization-review.md) for every localization request, every China request, every Simplified Chinese asset, or any review where market, language, locale, or channel fit matters.

## Confirm Review Scope

Review requires existing copy or clearly identified copy fields. Preserve the original verbatim before making any recommendation.

Do not turn editing into new positioning, audience research, competitor research, campaign strategy, or an invented offer. If those decisions are missing and would determine the copy, identify the required upstream work and return a bounded intake. Do not pretend it is a completed copy review.

Review authorization covers local analysis and artifacts only. CMS access, account access, live editing, publishing, deployment, sending, and contacting people are separate actions that require explicit authorization. Never imply that an external action occurred.

## Record Context Separately

Record the audience, desired action, market, language, locale, channel or surface, constraints, approved voice, and supplied sources. Never infer market or channel from language. Missing evidence is `unavailable`, not a review failure.

Ask only for missing inputs that could materially change the edit. When a useful bounded review is possible, state assumptions and continue instead of requiring private data.

## Select One Mode

Use the user's explicit mode when supplied. Otherwise select the narrowest mode that covers the request.

| Mode | Use for |
| --- | --- |
| `quick` | High-impact corrections with a compact findings set |
| `full` | Complete review across message, proof, action, consistency, accessibility, and market fit |
| `claims` | Factual support, proof scope, conflicts, and risky or regulated statements |
| `voice` | Approved voice, tone, terminology, readability, and voice-source conflicts |
| `localization` | Native adaptation for the declared market, language, locale, and channel |

Do not broaden a narrow mode silently. A `voice` review may still remove or flag a dangerous unsupported claim, but should not redesign unrelated message strategy.

## Review Then Revise

1. Copy the original exactly, including numbers, qualifiers, negation, plan limits, dates, units, names, and CTA.
2. Separate supported facts, reported signals, inferred editorial judgments, unavailable support, and non-applicable material.
3. Review the dimensions required by the mode. A `full` review covers clarity, audience fit, message hierarchy, proof, specificity, CTA alignment, factual support, consistency, accessibility, market and locale fit, channel fit, and risky or regulatory claims.
4. Make the smallest edit that solves each issue. Keep supported facts within their exact scope. Never strengthen an unverifiable claim; flag it, remove it, or replace it with wording that no longer asserts the unsupported fact.
5. Check the revision against the original fact map and channel constraints before delivery.

Do not invent sources, metrics, testimonials, customer identities, prices, discounts, guarantees, certifications, legal or regulatory status, capabilities, compatibility, urgency, scarcity, or outcomes.

## Deliver The Review

Use this order:

1. **Review context** - mode, audience, desired action, market, language, locale, channel, constraints, and source boundary.
2. **Original copy** - the complete submitted copy, verbatim. Keep variants or fields separately identifiable.
3. **Findings** - prioritized observations with location, issue, reason, classification, and recommended disposition. For `full`, cover every review dimension even when no change is needed.
4. **Revised copy** - a usable revision that preserves supported meaning and the requested action.
5. **Exact change ledger** - one row per material edit with `Original span`, `Revised span`, `Reason`, `Evidence state`, `Signal status`, and `Meaning / risk effect`. Use `[removed]` or `[none]` when a span is deleted or added. For a stakeholder-only statement, leave `Evidence state` blank and use signal status `reported signal`. For a purely editorial edit that evaluates no factual evidence, leave both `Evidence state` and `Signal status` blank.
6. **Unresolved inputs** - only gaps that affect confidence, approval, or a material claim; request the smallest useful source.

Do not summarize several distinct changes into one approximate ledger row. Grammar and punctuation edits may be grouped only when the exact spans and meaning effect remain unambiguous.

## Finish Locally

Return the review in the conversation or a local artifact. Label any unresolved legal, regulatory, brand, or factual approval boundary. Do not call copy final, approved, compliant, publish-ready, or deployed unless the supplied evidence and explicit task scope support that status.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.
