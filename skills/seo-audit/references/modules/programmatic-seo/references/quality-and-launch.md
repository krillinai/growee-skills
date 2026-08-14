# Quality And Launch

## Quality Layers

1. **Source:** authority, license, identity, coverage, freshness, conflicts, and missingness.
2. **Schema:** types, enums, units, constraints, references, and versions.
3. **Transformation:** correct computation, selection, comparison, or workflow utility.
4. **Page:** required modules, distinct value, claims, readable hierarchy, accessibility, and states.
5. **Technical:** response, render, URL, canonical, locale, links, sitemap, performance, and mobile behavior.
6. **Journey:** promise, CTA, product continuation, first value, trust, and support.
7. **Outcome:** qualified discovery, activation, retention, contribution, maintenance cost, and risk.

Automate deterministic checks. Use human or expert review for intent satisfaction, usefulness, claim context, sensitive topics, localization, accessibility judgment, and edge cases.

## Sampling Matrix

Sample across page families; high, median, low, and zero supply; common and rare entities; short and long values; every locale and market actually in scope; newly added, updated, stale, expired, conflict, duplicate, merged, and removed states; top predicted demand and random tail candidates; product-action branches; desktop and mobile; raw and rendered output.

State the population, sampling method, sample count, selection date, reviewed fields, acceptance rule, owner, and limitations. Passing a sample supports only the sampled frame and confidence; it does not verify every page.

## Launch Gates

Require:

- frozen candidate inventory and versioned contracts;
- source, schema, transformation, page, and technical acceptance;
- a representative publishable batch and explicit held-back inventory;
- source-of-truth and product-path QA;
- crawl, render, status, robots, canonical, locale, sitemap, link, performance, and mobile verification;
- metric and tracking contracts for page cohort, qualified arrival, activation, retention, cost, and guardrails;
- owner approval, monitoring, incident, rollback, removal, and communication plans.

Expand by a predefined batch rule only after maturity. A page being crawlable or indexed does not prove usefulness or permission to expand.

## Measurement

Keep distinct:

```text
candidates -> valid pages -> published -> live -> crawlable -> canonical
-> discovered -> indexed when verified -> impressions -> qualified visits
-> qualified action -> first value -> retained value -> contribution
```

For every transition state entity, numerator, denominator, source, window, maturity, identity, market, page family, cohort, attribution, and limitation. Use page-cohort and source-cohort views. Preserve search attribution and causal incrementality as different evidence.

## Risk And Abuse

Check copied or licensed content, fabricated entities or locations, unsafe comparisons, private or personal data, biased or harmful categorizations, user-generated abuse, spam submissions, moderation, misinformation, expired facts, manipulated reviews, security, rendering cost, crawl traps, infinite combinations, and platform dependency.

## Retirement

For each retired page choose keep, update, merge, redirect to an equivalent target, gone, noindex where appropriate to the operating policy, or needs evidence. Never send unmatched pages to the homepage. Remove internal links and sitemap entries consistently, preserve required records, update structured data and caches, validate representative states, monitor customer and search effects, and keep rollback criteria.
