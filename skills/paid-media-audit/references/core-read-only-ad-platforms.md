# Core Read-Only Ad Platform Access

Use direct Google Ads or Meta Ads reads only when the user explicitly authorizes a named account and decision and a capable connector or API path is already configured. Otherwise use the canonical local export bundle. A login credential or broad token is not sufficient authorization.

## Google Ads

Require a named customer, platform **Read only** account role, approved developer token and OAuth path when API access is used, dates, timezone, currency, channel types, conversion scope, fields, filters, and row limit. Use bounded GAQL reads for reporting, configuration, conversion actions, change history, search terms, or products.

The OAuth scope used by Google Ads is not itself read-only. Enforce safety through the account's Read only role and by permitting query operations only. Never issue a mutate request, apply a recommendation, upload conversions or audiences, or change bids, budgets, campaigns, assets, goals, feeds, exclusions, or settings.

## Meta Ads

Require a named ad account, `ads_read`, no `ads_management`, dates, timezone, currency, attribution settings, entity level, breakdowns, fields, filters, and result limit. Use bounded Insights and configuration reads only.

Never retrieve leads or personal audience members; create or mutate campaigns, ad sets, ads, creatives, audiences, pixels, or Conversions API settings; or change bids, budgets, placements, delivery, or publication state.

## Evidence Record

Preserve the account identifier, query timestamp, request and returned windows, timezone, currency, entity level, fields, breakdowns, filters, attribution settings, pagination or row limits, privacy suppression, and response errors. Platform results are verified only as platform reporting or configuration. They do not prove qualified customers, retained value, business economics, or incrementality without compatible external evidence.
