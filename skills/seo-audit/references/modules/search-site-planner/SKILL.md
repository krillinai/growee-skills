---
name: search-site-planner
description: Use when planning or reviewing a website or section hierarchy, navigation, URL structure, breadcrumbs, internal links, restructuring decisions, or old-to-new migration mappings from a declared page or URL inventory across markets and locales.
---

# Search Site Planner

Turn a declared, bounded inventory into an implementable site-structure plan. Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` as evidence states. Keep an attributable but uninspected owner statement separate as signal status `reported signal` with a blank evidence state; it is not evidence. A partial crawl supports conclusions about its inspected scope only.

## Route The Work

Choose one primary mode:

| Mode | Boundary | Required decision |
| --- | --- | --- |
| `new-site` | Supplied or approved page candidates | Place each candidate or mark its placement unresolved |
| `restructure` | Scoped current URLs | Give every URL one of `keep`, `move`, `merge`, `retire`, or `needs-evidence` |
| `migration` | Scoped old URLs and proposed target inventory | Give every old URL exactly one explicit migration disposition |
| `focused` | Named page or section set | Review only that set; do not widen into a site redesign |

If a request mixes modes, name the primary mode and bound any secondary work. Read [planning-contract.md](references/planning-contract.md) for the inventory, evidence, hierarchy, navigation, URL, breadcrumb, internal-link, and output contracts. For `migration`, or when redirects or release validation are involved, also read [migration-and-validation.md](references/migration-and-validation.md). For market, language, locale, domain, provider, indexing, or China questions, read [market-search-notes.md](references/market-search-notes.md).

## Freeze The Evidence Boundary

Before planning, record:

- inventory source, capture time, and capture state or version;
- included scope, total known count, inspected count, and exclusions;
- market, language, and locale as separate fields;
- capture limitations, implementation constraints, and unavailable evidence.

Use a supplied inventory or the smallest approved captured sample. Do not begin a broad crawl, access private analytics or webmaster tools, or expand the inventory without separate explicit authorization. Never infer site-wide behavior from one page, a capped crawl, or a section sample.

Public evidence is sufficient to begin. Attributable private exports may refine decisions when supplied, but they are optional enhancements. Missing analytics, demand, rankings, conversion, backlinks, logs, or console evidence is `unavailable`, not a failure and not a negative score. Never invent demand, traffic, rankings, conversions, link value, page importance, URLs, competitors, or benchmarks.

## Plan From Relationships

Use user tasks, product or content relationships, the bounded inventory, captured navigation and link behavior, and implementation constraints. Do not impose universal click-depth, page-count, word-count, URL-length, navigation-link-count, internal-link-count, or industry-benchmark rules.

Apply the mode contract:

- `new-site`: plan only supplied or approved candidates; list discovery gaps without creating a fictional business or page inventory.
- `restructure`: reconcile every scoped current URL, preserve source uniqueness, and require unique destinations for distinct retained pages unless an explicit evidence-backed merge explains a shared target.
- `migration`: preserve a URL when the supplied relationship and implementation evidence support preservation. For every redirect, give the exact source, exact target, and rationale. Never default unmatched URLs to the homepage.
- `focused`: keep all findings and recommendations inside the named set. Describe external dependencies without redesigning them.

For China work requested in Simplified Chinese, write user-facing output in native Simplified Chinese. Do not infer market from language or locale, and do not treat a country domain, subdomain, subdirectory, or separate international domain as universally correct.

## Deliver In Order

1. mode and boundary record;
2. inventory coverage, evidence-state register, and signal-status register;
3. readable ASCII hierarchy;
4. URL map with identity and collision checks;
5. navigation specification;
6. breadcrumb behavior;
7. internal-link rules;
8. migration mapping and reconciliation report when applicable;
9. missing evidence and unresolved decisions;
10. local implementation checks and validation checks;
11. authorization boundary, owner handoffs, and source notes.

Default to local deliverables. Broad crawling, authenticated analytics or webmaster access, Search Console actions, CMS, router, navigation or template edits, redirect deployment, canonical, robots or sitemap changes, DNS work, publishing, and production validation each require separate explicit authorization. Never bypass authentication, CAPTCHA, robots controls, or rate limits.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the boundary is reproducible; evidence states use only the canonical four values; every reported signal has a blank evidence state; no signal was promoted to evidence; every inference names its basis and confirmation step; coverage arithmetic reconciles; no partial capture became a site-wide conclusion; every scoped item has the mode-required decision; distinct pages do not silently collide on one URL; the ASCII tree, URL map, navigation, breadcrumbs, and link rules agree; raw migration URLs and request-source server mappings both reconcile; release readiness is blocked by any hold; redirects have exact targets and rationale; loops, chains, ambiguous targets, missing rows, query and fragment behavior, locale or market loss, orphan targets, parity, rollback, and validation were checked where applicable; unavailable private evidence was not penalized; provider claims remain provider-specific; and no external action occurred without explicit authorization.
