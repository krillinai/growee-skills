# Core Read-Only Tools

Use this contract only when the user explicitly authorizes a named system and scope and a capable connector or API path is already available. A request for diagnosis does not itself authorize authenticated access. If any gate fails, request a bounded export or mark the source unavailable.

## Access Gate

Before every query, record the decision, system, property/project/portal/account ID, owner, approved time window, segments, fields or metrics, minimum permission, data sensitivity, and query limit. Preview the query when practical. Use the narrowest aggregate read that can change the diagnosis.

Allowed core sources:

| Source | Minimum access | Useful diagnostic evidence | Never do |
| --- | --- | --- | --- |
| GA4 | `analytics.readonly`; named property | bounded aggregate acquisition, activation, and retention reports plus metadata | admin, event, key-event, audience, import, deletion, or raw-user operations |
| PostHog | named project; view-only role or read-restricted key | bounded trends, funnels, retention, and existing insight results | ingest events, change persons, flags, experiments, dashboards, or export replays |
| Search Console | `webmasters.readonly`; named property | bounded query, page, country, device, date, sitemap, and inspection evidence | submit or delete sitemaps, request indexing, or change users/settings |
| HubSpot | named portal; required `crm.objects.*.read` only; property allowlist | bounded lifecycle, company, deal, owner, pipeline, and reconciliation evidence | mutate records, enroll lists/workflows, send messages, or export unrestricted personal data |
| Google Ads | named customer; platform Read only role | bounded GAQL delivery, configuration, conversion, change, query, and product evidence | any mutate operation, recommendation application, spend change, upload, or customer-data export |
| Meta Ads | named account; `ads_read`; no `ads_management` | bounded Insights and configuration evidence | mutate ads, budgets, audiences, tracking, leads, or use `ads_management` |

## Evidence Record

For every result preserve source, property/project/portal/account ID, query timestamp, requested and returned windows, timezone, currency, entity, dimensions, metrics, filters, attribution setting, row or aggregation limits, sampling or thresholding indicators, and known limitations. Label connector output `verified` only for what the response directly establishes; it does not establish causality, incrementality, customer intent, or cross-system identity.

Do not write credentials, tokens, cookies, raw personal data, lead records, audience lists, or unrestricted result sets into `.agents/growee-context.md`. Store only privacy-safe aggregates, source identifiers, definitions, dates, and limitations needed for later Skills.
