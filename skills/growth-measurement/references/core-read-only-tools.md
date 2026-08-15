# Core Read-Only Measurement Tools

Use GA4, PostHog, Google Search Console, HubSpot, Google Ads, or Meta Ads only through an already capable connector or API path and only after explicit task-level authorization names the system, property/project/portal/account, owner, decision, time window, fields, and guardrails. If authorization, capability, or minimum read access is missing, produce a query specification or request a bounded export.

## Minimum Read Contracts

| Source | Minimum access | Bounded reads |
| --- | --- | --- |
| GA4 | `analytics.readonly`; named property | metadata and aggregate reports for declared dimensions, metrics, filters, segments, and windows |
| PostHog | named project; view-only role or read-restricted key | event definitions, trends, funnels, retention, and existing insights |
| Search Console | `webmasters.readonly`; named property | aggregate Search Analytics, property, sitemap, and supported inspection evidence |
| HubSpot | named portal; only required `crm.objects.*.read`; property allowlist | schemas and selected lifecycle, company, deal, owner, and pipeline fields |
| Google Ads | named customer; platform Read only role | bounded GAQL configuration and performance reporting; no mutate operations |
| Meta Ads | named account; `ads_read`; no `ads_management` | bounded Insights and configuration reads |

## Query And Evidence Discipline

1. Freeze the metric contract before querying: entity, population, event, formula, identity, timezone, currency, windows, attribution, maturity, filters, and decision use.
2. Request the smallest aggregate result that can answer the question. Avoid raw user, contact, lead, audience, session-replay, click-identifier, or customer payload exports.
3. Preserve source ID, query timestamp, request parameters, returned window, row limits, sampling, thresholding, privacy suppression, pagination, attribution settings, and errors.
4. Reconcile only compatible entities and definitions. Do not join identities across systems unless a separately authorized, privacy-reviewed path already exists.
5. Treat platform-attributed outcomes, CRM stages, product behavior, billing outcomes, forecasts, and causal effects as distinct evidence layers.

Never create or mutate events, records, audiences, dashboards, reports, alerts, flags, experiments, campaigns, budgets, bids, conversions, sitemaps, settings, permissions, or customer state. Never store credentials or unrestricted personal data in local reports or `.agents/growee-context.md`.
