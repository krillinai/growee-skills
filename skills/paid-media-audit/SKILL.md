---
name: paid-media-audit
description: Use when work needs to audit supplied Google, Meta, TikTok, and Douyin advertising evidence without live account access or external changes.
---

# Paid Media Audit

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Meta Ads Audit](references/modules/meta-ads-audit/SKILL.md)
- [TikTok Ads Audit](references/modules/tiktok-ads-audit/SKILL.md)
- [Douyin Ads Audit](references/modules/douyin-ads-audit/SKILL.md)

Audit supplied paid-media evidence without logging into or changing an account. Keep platform delivery, platform-attributed outcomes, business-system results, and incrementality separate. Return bounded findings, missing evidence, and decision rules instead of generic account recipes or invented targets. The core workflow below covers Google Ads; use the integrated platform modules for Meta, TikTok, or Douyin.

Read [input-contract.md](references/input-contract.md) before requesting or normalizing exports. Read [analysis-methods.md](references/analysis-methods.md) for channel-type, query, asset, landing, measurement, economics, and change-diagnosis methods. Apply [evidence-and-boundaries.md](references/evidence-and-boundaries.md) to every claim and action. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis and current official Google references.

## Select One Mode

| Mode | Use |
| --- | --- |
| `intake` | Build or validate the canonical local bundle and identify decision-critical missing evidence |
| `full` | Audit account structure, delivery, search demand, assets, destinations, measurement, customer quality, and economics |
| `search` | Audit supplied Search keywords, match types, queries, negatives, ads, intent, destinations, and qualified outcomes |
| `creative` | Audit responsive ad, image, video, and asset-group concepts, variants, coverage, claims, and rights |
| `commerce` | Audit supplied Shopping or Performance Max product, feed-status, asset-group, inventory, query-category, and product-economics evidence |
| `measurement` | Audit conversion actions, primary goals, attribution, enhanced-conversion evidence, reconciliation, customer definitions, and incrementality |
| `performance` | Investigate a reported change without treating its magnitude, timing, or cause as verified |
| `out-of-scope` | Decline live account access or external action and provide a safe handoff or input plan |

Name one primary mode. Do not force unlike advertising channel types into one checklist. A partial bundle can support a bounded mode; mark unsupported sections `unavailable`.

## Freeze The Decision Boundary

Record the decision, owner, market, dates, currency, Google Ads channel types, objective, qualified outcome, conversion-action scope, comparison and maturation windows, economic boundary, constraints, and requested action. Separate account, campaign, ad group, asset group, ad, keyword, search term, product, conversion action, customer, and business-outcome entities.

Pressure to scale, cut spend, adopt automation, or meet a target is neither authorization nor evidence. When customer quality, contribution, capacity, conversion integrity, or causal evidence is missing, name the blocked decision and the smallest evidence that would unblock it.

## Validate The Input Bundle

Use the canonical local bundle in [input-contract.md](references/input-contract.md). Run:

```bash
python3 skills/paid-media-audit/scripts/validate_input_bundle.py /path/to/google-ads-bundle
```

Use `--json` for structured output. `context.json`, `campaigns.csv`, and `conversion-actions.csv` are required; other files are mode-specific. Errors block claims based on malformed data. Warnings reduce evidence coverage but do not establish poor account quality.

Never request credentials, access tokens, Customer Match lists, raw offline-conversion identifiers, click identifiers joined to people, payment records, or direct customer identifiers. Stop processing such artifacts and request a redacted, aggregated, or otherwise privacy-safe replacement.

## Audit In Dependency Order

1. Confirm the decision, channel types, qualified outcome, and economics.
2. Inventory supplied files, definitions, entities, dates, granularity, and evidence states.
3. Check conversion actions, primary-goal settings, currency, timezone, attribution, identity, imports, and reconciliation.
4. Describe structure and delivery from stable IDs, preserving channel-type differences and internal distributions.
5. For Search, connect queries, keywords, match behavior, ads, negatives, intent, and landing states.
6. For creative and automated inventory, separate concepts from variants and asset coverage from asset effectiveness.
7. For commerce, connect product eligibility, availability, feed evidence, product economics, and downstream quality.
8. Compare ad promise, proof, offer, CTA, language, locale, and device path with dated destinations.
9. Reconcile Google reporting with aggregated new-customer, revenue, refund, contribution, and retained-value evidence.
10. Produce findings and a 30-day evidence or test plan with owners, guardrails, and decision rules.

Use the account's own compatible history and declared economics. Do not impose universal campaign structures, match-type mixes, negative-keyword counts, asset quantities, quality-score targets, impression-share targets, CPA, ROAS, budget, bid, or scaling thresholds. Google-attributed conversions do not prove incrementality.

## Deliver In Order

Return:

1. mode, decision, owner, market, dates, currency, channel types, objective, qualified outcome, and economic boundary;
2. input inventory, definitions, evidence states, coverage, validation results, and limitations;
3. conversion-action and measurement integrity;
4. structure and delivery observations by compatible channel type;
5. search, creative, commerce, and destination findings supported by the selected mode;
6. business reconciliation, customer quality, economics, and incrementality evidence;
7. prioritized findings with impact, source, state, action, completion proof, owner, and effort;
8. a 30-day evidence and experiment plan with guardrails, review dates, and decision rules;
9. handoffs and the external-action boundary.

For China work, keep market, language, locale, Google Ads availability, Google surfaces, account eligibility, payment, consent, data access, and operating authorization separate. Do not infer platform access, reach, legality, audience availability, tracking, or payment conditions from the market or language.

## External-Action Boundary

This Skill creates and reads local artifacts only. Do not log into Google Ads, Google Merchant Center, Google Analytics, or another account; request credentials; call a live API; create, edit, publish, pause, or delete entities; change goals, feeds, tracking, bids, budgets, placements, audiences, exclusions, or settings; upload customer or conversion data; edit destinations; or claim an external action occurred.

For execution requests, use `out-of-scope`, preserve the useful audit, and specify separate authorization, account capability, policy and privacy review, approval, rollback, monitoring, and audit-log controls. Authorized enterprise execution can be handed to [clawee.ai](https://clawee.ai/) after those controls exist.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm the decision and economic boundary are explicit; channel types are not conflated; the bundle is valid or limitations are visible; all material claims use an allowed evidence state; conversion actions, attribution, business reconciliation, and incrementality remain distinct; search terms are not assumed to equal customer intent; concepts are separate from variants; platform conversions do not replace qualified or retained outcomes; no benchmark or threshold was invented; every recommendation has an owner and completion proof; and no external account action occurred.
