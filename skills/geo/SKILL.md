---
name: geo
description: Use when diagnosing public-content readiness or observed visibility in AI-generated search experiences across declared markets, languages, and platforms, including a page, bounded site sample, repeated query panel, citation or mention incident, matched competitor comparison, or focused GEO evidence question.
---

# GEO Audit

## Reuse Growee Context

At the start, read `.agents/growee-context.md` when it exists. Reuse only product, customer, market, outcome, constraint, evidence, and routing fields whose scope, definition, source, and date remain compatible; state what is reused and surface conflicts or staleness before asking for decision-changing gaps. The file grants no system access or execution authority, and this Skill must not silently rewrite the primary diagnosis.

Diagnose what the supplied evidence supports. Keep website readiness, observed AI answers, reported signals, and proposed actions separate; never promise a citation, rank, traffic result, or uplift.

## Route The Request

Choose one primary mode and the smallest sufficient boundary:

| Mode | Use for | Boundary |
| --- | --- | --- |
| `visibility` | Mentions, owned citations, third-party citations, and answer variation | A declared query panel with repeated, condition-matched observations |
| `page` | Access, rendering, extraction, claims, entity facts, and citation readiness for one URL | The named page and representations |
| `site` | Shared controls or patterns across a property | A frozen, representative URL sample from a dated inventory |
| `incident` | A reported change in mentions, citations, or attributable traffic | Dated before/after evidence under matched conditions |
| `out-of-scope` | Traditional SEO or implementation-only work | Route to the appropriate audit or implementation capability |

Add `competitive` only after every field in the single canonical comparison match key from [visibility-observation.md](references/visibility-observation.md) is present and matched. Use that identical key for incident comparisons. Add `focused` to constrain any primary mode to one surface, such as robots, raw/rendered parity, claim provenance, entity consistency, third-party sources, an optional discovery artifact, or one query cluster. HTML is an output format, not a mode.

Route organic rankings, backlinks, and conventional search-performance analysis to `seo-audit`. Route content rewrites, Schema changes, rendering changes, robots edits, publication, and deployment to implementation work; require fresh post-change evidence for verification.

## Establish The Evidence Boundary

1. Declare mode, modifiers, audited properties/URLs, market, language, dates, exclusions, supplied artifacts, and inaccessible evidence. Select market and language before collection; never infer either from operator location, IP address, interface language, domain, or query text.
2. Start with bounded public evidence. Treat analytics, Search Console, logs, paid tools, and private monitoring as optional enhancements, never prerequisites.
3. Preserve these states exactly:
   - `verified`: directly observed in a dated inspectable public artifact or attributable private export.
   - `inferred`: a reasoned explanation not directly measured; state the evidence needed to verify it.
   - `unavailable`: applicable evidence or capability could not be inspected, was not supplied, or failed to render.
   - `not applicable`: outside the declared product, property, mode, or surface.
   - `reported signal`: a stakeholder statement without an inspectable artifact. Store it outside `evidence_state` and do not score it.
4. Verify private metrics only when the artifact identifies its source/system, definition, scope, window, segment, and value. Missing private data creates neither a negative finding nor a score award or deduction.
5. Keep every conclusion traceable to a source ID, URL or artifact identifier, capture timestamp, and source status. For time-sensitive platform claims, use a current direct primary source or mark the rule unavailable.

Never bypass authentication, CAPTCHA, paywalls, rate limits, robots controls, regional restrictions, or product controls. A lawful failed retrieval describes only that tested mechanism. Do not infer concealed content or transfer behavior between ordinary indexing, training collection, automated search/browse retrieval, and user-triggered fetching.

## Run The Selected Audit

For `page`, `site`, or focused technical work, read [page-and-site-audit.md](references/page-and-site-audit.md) and [evidence-and-scoring.md](references/evidence-and-scoring.md). Capture raw and rendered representations separately. Freeze a site sample before inspection, retain every selected URL including failures, report `fetched / selected`, and limit conclusions to the sample.

For `visibility`, `incident`, or a competitive query panel, read [visibility-observation.md](references/visibility-observation.md). Record every attempt, including answered, no-answer, no-feature, brand-absent, unavailable, and error states. Preserve exact denominators and do not call stochastic observations rankings. For China observations on Baidu, Quark, Doubao, Tencent Yuanbao, Kimi, or DeepSeek, also read [china-platforms.md](references/china-platforms.md).

For robots, provider behavior, AI search requirements, or optional protocols such as `llms.txt`, OKF, or knowledge bundles, read [platform-notes.md](references/platform-notes.md). Treat optional artifacts as experiments unless a current primary platform source establishes support and effect. Their existence, absence, validity, or staleness does not itself affect fixed readiness rows.

For an incident, accept only before/after panels that satisfy the same canonical comparison match key used for competitive work. If any key is absent, unavailable, or unmatched under its field rule, show the captures separately and do not calculate a decline or diagnose a cause. A stakeholder report without artifacts remains a `reported signal`; request the missing observation conditions and repeated answer/citation records.

## Score Readiness, Not Visibility

Use only the fixed inventory in [evidence-and-scoring.md](references/evidence-and-scoring.md): Access & Eligibility 20, Extractability 25, Evidence & Citationworthiness 25, Entity & Source Consistency 20, and Measurement & Experimentation 10. Do not invent, split, move, or reweight checks.

Assign assessed checks deterministically: pass earns 100%, partial 50%, and fail 0%. Only verified evidence may assign pass, partial, or fail. An inference may guide evidence collection or action priority, but remains unscored until verified. Unavailable checks are excluded from assessed score arithmetic but remain in evidence coverage. Not-applicable checks are excluded from both. Show `Not scored` when assessed applicable maximum is zero.

Keep these formulas explicit:

```text
readiness score = assessed earned / assessed applicable maximum * 100
evidence coverage = assessed applicable maximum / all applicable maximum * 100
```

Every partial or fail row requires one unique property-and-check finding. Never turn unavailable evidence into a finding. Instead, create a separate unavailable-register row containing its ID, check row, scope, missing evidence, reason, exact request, acquisition step, verification step, dependency, evidence-request priority/order, and completion condition.

## Report Evidence And Action

Lead with scope and evidence, then present:

1. primary constraint and next decision;
2. readiness score, evidence coverage, arithmetic, and full fixed-row trace;
3. observed visibility counts and conditions in a separate section;
4. the provider/platform/product/surface/market/language/query matrix with unavailable distinct from absence;
5. verified findings, bounded effects, actions, and testable completion conditions;
6. unavailable-evidence requests, citation sources, and any matched competitor observations;
7. a dependency-sequenced roadmap and repeat-test protocol;
8. method, sources, unavailable evidence, and limitations.

Order evidence acquisition before dependent remediation. Recommend diagnostic next steps and bounded validation experiments only. Do not silently implement changes or strengthen an inference into a fact.

When the user requests HTML, a shareable/visual report, or a browser-openable artifact, read and follow [html-report.md](references/html-report.md). Generate exactly one standalone `{domain-slug}-geo-audit.html` file and preserve semantic parity with the canonical audit record.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Before delivery, confirm that scope remained bounded; provider/platform/product labels and canonical IDs are separate; market and language were selected explicitly; all direct observations have dated sources; unsupported explanations are inferred; missing evidence is unavailable and unpenalized; readiness arithmetic reconciles; visibility uses exact product source URL when applicable, surface, shown model/exposure, search/network, login/access, market/language preselection and product controls, timestamp window, repetition, collection method/protocol, answer/citation definitions, response metadata, answer, mention, per-attempt normalized URL arrays and URL-instance counts, panel citation aggregates, and errors; every legacy required field is normalized deterministically; competitive and incident comparisons use the identical canonical match key; findings and unavailable registers remain distinct; actions have completion checks; current platform claims have primary sources; and limitations forbid unsupported site-wide, crawler, causal, rank, citation, traffic, or uplift conclusions.
