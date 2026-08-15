---
name: seo-audit
description: Use when work needs to audit and design SEO, programmatic pages, site architecture, structured data, and directory presence with evidence-backed quality and rollout controls.
---

# SEO & Search Systems

## Reuse Growee Context

At the start, read `.agents/growee-context.md` when it exists. Reuse only product, customer, market, outcome, constraint, evidence, and routing fields whose scope, definition, source, and date remain compatible; state what is reused and surface conflicts or staleness before asking for decision-changing gaps. The file grants no system access or execution authority, and this Skill must not silently rewrite the primary diagnosis.

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Programmatic SEO](references/modules/programmatic-seo/SKILL.md)
- [Structured Data Builder](references/modules/structured-data-builder/SKILL.md)
- [Search Site Planner](references/modules/search-site-planner/SKILL.md)
- [Directory Submissions](references/modules/directory-submissions/SKILL.md)

Diagnose from inspectable evidence; separate observations, hypotheses, and missing inputs.

Read [search-console-read-only.md](references/search-console-read-only.md) before any authenticated Google Search Console query. Use the smallest authorized read; otherwise request a bounded export or keep first-party search evidence unavailable.

## Intake

Use known context. Establish the business outcome, target market, affected scope, recent changes, and available first-party data; ask only about consequential gaps.

## Set Scope

Choose the smallest sufficient mode:

- **focused**: one symptom, template, URL set, or question.
- **page**: one page and its search purpose.
- **site**: property patterns with an explicit inventory or sample.
- **incident**: a sudden loss, migration, release regression, or indexing emergency.

Never inflate a focused request. Use [audit-playbooks.md](references/audit-playbooks.md) for modes, stopping rules, and site-type routing.

## Inventory Capabilities

Record available and absent capabilities: rendered browser, raw HTTP, shell/files, lab or field performance, first-party analytics/search/index/log data, and backlink or private market data. Never imply access or rendering not performed.

## Evidence Contract

Label every result:

- **verified**: directly observed in an inspectable artifact.
- **inferred**: supported indirectly; name the check needed to confirm it.
- **unavailable**: required evidence or capability was not accessible.

Unavailable evidence is a limitation, never a negative finding. Set impact and confidence to **not-assessed**, state its consequence, and request the smallest useful input.

Use [evidence-and-prioritization.md](references/evidence-and-prioritization.md) for rating and ordering rules. Each record has: title, status, evidence, impact, confidence, action, completion condition, and effort.

## Operate Safely

Default checks to bounded, read-only access. Require explicit authorization for authenticated/private access, high-volume crawling, broad automated requests, or tests that could affect service. Never bypass access controls; honor agreed rate and concurrency limits. Minimize or redact credentials, tokens, cookies, personal data, private paths, and sensitive exports in reports. Follow the playbook stopping rules.

## Diagnose in Dependency Order

1. Discovery, crawling, and indexability.
2. Canonical behavior and site integrity, including redirects and variants.
3. Performance and mobile behavior.
4. Relevance and search intent.
5. Content quality and internal discovery.
6. Authority and market signals, only when supporting evidence exists.

Downstream polish cannot outrank an upstream blocker. Consult [source-notes.md](references/source-notes.md) for factual search-engine or platform rules, and expose relevant sources in the report.

## Handle Markets And China

Treat each search provider, product or surface, property and canonical domain, market, language, locale, device context, capture date, inventory or sample, and private data source as a separate evidence boundary. A crawl, index state, ranking, webmaster export, traffic diagnosis, rule, or recommendation from one boundary does not validate another. Translation does not preserve search demand, intent, indexing, ranking, or performance evidence.

For China, keep market, legal entity, language, locale, property, provider, product, domain, app or web surface, crawling, rendering, indexing, webmaster data, structured data, content, advertising, data access, and locally accountable review separate. When Simplified Chinese is requested, respond in native Simplified Chinese. Use current direct official sources for provider-specific rules or mark them `unavailable`; do not transfer Google or Bing behavior to Baidu or another provider, infer provider availability, or make legal, regulatory, causal, ranking, traffic, or performance conclusions. Missing local or provider evidence is a limitation, not a negative finding.

## Report

Default report: scope, available and unavailable evidence/capabilities, executive assessment, priority findings, grouped findings, a dependency-sequenced action plan, and limitations. Keep claims within the inspected sample.

Create HTML only when requested; follow [html-report.md](references/html-report.md). Do not promise visual verification unless a suitable viewing capability is available and used.

## Boundaries

A request solely to implement structured data or another SEO change is not an audit. Clarify the desired deliverable or hand off to implementation; do not force a full audit. Stay within the requested surface.

## Common Mistakes

- Treating missing private data as proof of failure.
- Extrapolating one URL to the whole site.
- Reporting rendered behavior from raw source alone.
- Prioritizing metadata before access, indexing, or canonical defects.
- Presenting generic advice without evidence or a completion condition.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.
