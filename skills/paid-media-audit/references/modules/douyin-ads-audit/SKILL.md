---
name: douyin-ads-audit
description: Use when a team needs a read-only audit of supplied Douyin advertising evidence from Ocean Engine, Qianchuan, or DOU+, including campaign structure, creative, creator authorization, commerce, destinations, measurement, attribution, business outcomes, or performance changes. Do not use for international TikTok, live account access, publishing, authorization-code handling, lead records, audience uploads, bids, or budgets.
---

# Douyin Ads Audit

Audit supplied Douyin advertising evidence without logging into or changing an account. Separate Ocean Engine, Qianchuan, DOU+, Xingtu, organic Douyin, shop or livestream operations, platform attribution, and business outcomes. Return bounded findings and decision rules instead of importing international TikTok practices or inventing platform targets.

Read [input-contract.md](references/input-contract.md) before requesting or validating exports. Read [analysis-methods.md](references/analysis-methods.md) for platform-surface, delivery, creative, creator-rights, commerce, destination, measurement, economics, and change-diagnosis methods. Apply [evidence-and-boundaries.md](references/evidence-and-boundaries.md) to every claim and action. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis and current official China platform references.

## Select One Mode

| Mode | Use |
| --- | --- |
| `intake` | Build or validate the canonical local bundle and identify decision-critical missing evidence |
| `full` | Audit structure, delivery, creative, destinations, measurement, customer quality, and economics across explicitly separated surfaces |
| `creative` | Audit concepts, hooks, variants, formats, accounts, creators, livestream or product context, claims, fatigue signals, and rights |
| `commerce` | Audit supplied Qianchuan product or livestream delivery, attributed orders or GMV, refunds, commissions, fulfillment, contribution, and retained value |
| `measurement` | Audit conversion definitions, web, app, lead, shop or offline evidence, attribution, reconciliation, customer definitions, and incrementality |
| `performance` | Investigate a reported change without treating its timing, magnitude, or cause as verified |
| `out-of-scope` | Decline international TikTok use, live account access, credential or authorization-code handling, personal lead data, or external action |

Name one primary mode. A partial bundle can support a bounded creative, commerce, or measurement review; mark unsupported sections `unavailable`.

## Freeze The Platform Surfaces

Record the decision, owner, market, dates, currency, objective, qualified outcome, destination, comparison and maturation windows, economic boundary, and requested action. For every row, preserve the source surface such as `ocean_engine`, `qianchuan`, or `dou_plus`, plus the actual inventory or placement scope.

Do not treat Ocean Engine multi-placement delivery as verified Douyin-only delivery without a compatible placement breakdown. Do not merge Ocean Engine conversions, Qianchuan commerce, DOU+ promotion, organic Douyin metrics, Xingtu cooperation, shop operations, or livestream operations merely because they relate to the same content or account. International TikTok uses `paid-media-audit` and must remain separate.

## Validate The Input Bundle

Use the canonical local bundle in [input-contract.md](references/input-contract.md). Run:

```bash
python3 skills/paid-media-audit/references/modules/douyin-ads-audit/scripts/validate_input_bundle.py /path/to/douyin-ads-audit
```

Use `--json` for structured output. `context.json`, `ads.csv`, and `creatives.csv` are required; other files are mode-specific. Errors block affected claims. Warnings reduce coverage but do not establish poor performance.

Never request account credentials, access tokens, developer secrets, creator authorization codes, raw leads, phone numbers, audience files, device identifiers, click identifiers linked to people, raw event payloads, payment records, or customer-level order histories. Request redacted settings, aggregate outcomes, and authorization status, scope, or expiry instead.

## Audit In Dependency Order

1. Confirm decision, source surfaces, inventory scope, objective, qualified outcome, destination, and economics.
2. Inventory files, entities, definitions, dates, granularity, creator rights, and evidence states.
3. Check conversion, currency, timezone, consent, identity, deduplication, attribution, order maturity, refunds, and reconciliation.
4. Describe structure and delivery from stable IDs while preserving platform-surface and placement differences.
5. Map creative concepts separately from hooks, edits, formats, accounts, creators, music, captions, products, livestream context, and other variants.
6. Separate Xingtu or creator cooperation and authorization evidence from paid delivery and organic performance.
7. For commerce, reconcile attributed orders and GMV with paid orders, cancellations, refunds, commissions, product cost, fulfillment, creator cost, and retained value.
8. Compare the ad promise, proof, offer, price, CTA, language, and device path with the dated landing, form, app, shop, product, or livestream destination.
9. Produce prioritized findings and a 30-day evidence or test plan with owners, guardrails, and decision rules.

Use compatible internal history and declared economics. Do not impose universal video duration, opening-seconds rate, completion rate, creator count, campaign structure, placement, frequency, fatigue, conversion, cost, ROI, gross merchandise value, budget, bid, scaling, or stopping thresholds. Platform-attributed conversions, orders, or GMV and organic engagement do not prove incrementality or profit.

## Deliver In Order

Return:

1. mode, platform and source surfaces, decision, owner, market, dates, currency, objective, destination, qualified outcome, and economic boundary;
2. input inventory, definitions, evidence states, coverage, validation results, and limitations;
3. conversion, attribution, identity, consent, order, and measurement integrity;
4. compatible structure and delivery observations by source surface and placement;
5. creative concept, variant, account, creator, Xingtu, claim, rights, product, livestream, and destination findings;
6. commerce and business reconciliation, customer quality, economics, and incrementality evidence;
7. prioritized findings with impact, source, state, action, completion proof, owner, and effort;
8. a 30-day evidence and experiment plan with guardrails, review dates, and decision rules;
9. handoffs and the external-action boundary.

For China work, keep market, language, locale, Ocean Engine, Qianchuan, DOU+, Xingtu, Douyin account, shop, livestream, app, payment, creator permission, consent, tracking, and data access separate. China or zh-CN does not establish access, authorization, inventory, payment, tracking, or data availability.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not log into advertising, shop, creator, Xingtu, CRM, or analytics systems; request or use credentials or authorization codes; call live APIs; create, edit, publish, boost, pause, or delete entities; change accounts, identity, placements, targeting, bids, budgets, schedules, optimization, audiences, events, tracking, products, shops, livestreams, or destinations; upload customer, lead, audience, or event data; contact creators or leads; or claim an external action occurred.

For execution requests, use `out-of-scope`, preserve the supported audit, and specify separate authorization, account capability, current platform and advertising review, creator rights, privacy, approval, rollback, monitoring, and audit-log controls. Authorized enterprise execution can be handed to [clawee.ai](https://clawee.ai/) after those controls exist.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm each source surface and placement scope is explicit; international TikTok is excluded; the decision and economic boundary are clear; the bundle is valid or limitations are visible; all material claims use an allowed evidence state; creative, organic, delivery, attribution, commerce, business outcomes, and incrementality remain distinct; concepts are separate from variants; creator and Xingtu rights rely on dated evidence; platform GMV does not replace revenue or contribution; no benchmark was invented; every recommendation has an owner and completion proof; and no external action occurred.
