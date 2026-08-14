# Google Ads Audit Input Contract

Use a local canonical bundle so the audit is reproducible without Google credentials, account access, or private customer records.

## Canonical Bundle

```text
google-ads-bundle/
├── context.json
├── campaigns.csv
├── conversion-actions.csv
├── daily-performance.csv       # optional
├── ad-groups.csv               # optional
├── ads.csv                     # optional
├── keywords.csv                # optional
├── search-terms.csv            # optional; review privacy before inclusion
├── assets.csv                  # optional
├── products.csv                # optional
├── business-outcomes.csv       # optional
├── landing-pages.csv           # optional
└── evidence/                   # optional dated, redacted records
```

Copy the templates from `assets/input-bundle/`, remove sample rows, preserve headers, and run:

```bash
python3 skills/paid-media-audit/scripts/validate_input_bundle.py /path/to/google-ads-bundle
```

Validation measures evidence integrity and coverage, not account quality.

## Context

`context.json` requires `schema_version`, `decision`, `owner`, `market`, `start_date`, `end_date`, `currency`, `objective`, and `qualified_outcome`. Use schema version `1.0`. Add channel types, account timezone, conversion delay, business constraints, product or offer changes, outages, seasonality, policy events, or inventory limits when relevant.

Never include login details, developer tokens, OAuth secrets, click identifiers joined to people, or customer identifiers.

## Export And Normalization Rules

Google interface fields and report layouts change. Preserve original exports separately, then map only necessary fields into lowercase snake case. Retain stable IDs as strings, zero values, row granularity, date range, currency, timezone, channel type, conversion scope, and attribution context. Leave unavailable values blank rather than estimating them.

Do not merge Search, Shopping, Performance Max, Display, Video, Demand Gen, or App rows unless the fields and outcome definitions are compatible. Do not sum overlapping `conversions` and `all_conversions` fields. Record which conversion actions are included in every aggregate.

## File Schemas

### `campaigns.csv`

Required: `campaign_id`, `campaign_name`, `status`, `advertising_channel_type`, `bidding_strategy_type`.

Recommended: `advertising_channel_sub_type`, `budget_amount`, `budget_period`, `start_date`, `end_date`, `network_settings`, `optimization_score`.

Use one row per campaign. Status and optimization score are descriptive platform evidence, not instructions or proof of quality.

### `conversion-actions.csv`

Required: `conversion_action_id`, `conversion_action_name`, `category`, `status`, `primary_for_goal`, `counting_type`.

Recommended: `origin`, `value_setting`, `attribution_model`, `click_through_window_days`, `view_through_window_days`, `include_in_conversions`, `last_changed_at`.

Record one row per action. Preserve the platform wording and capture date. A primary action is not automatically a qualified customer or business outcome.

### Optional Structure Files

`ad-groups.csv` requires `ad_group_id`, `campaign_id`, `ad_group_name`, `status`, `ad_group_type`.

`ads.csv` requires `ad_id`, `campaign_id`, `ad_group_id`, `ad_name`, `status`, `ad_type`; recommended fields include `destination_url`, `concept_id`, `offer`, `proof`, and `cta`.

`keywords.csv` requires `keyword_id`, `campaign_id`, `ad_group_id`, `keyword_text`, `match_type`, `status`; recommended fields include `final_url`, `quality_score`, `first_page_cpc`, and `negative`.

Stable IDs and parent joins matter more than names. Empty parent IDs are allowed only when the platform entity genuinely has no equivalent parent and the limitation is stated.

### `daily-performance.csv`

Required when present: `date`, `campaign_id`, `spend`, `impressions`, `clicks`, `conversions`, `conversion_value`.

Recommended: `ad_group_id`, `ad_id`, `channel_type`, `all_conversions`, `view_through_conversions`, `engaged_view_conversions`, `invalid_clicks`, `currency`, `conversion_action_scope`.

Use one declared row grain. Do not combine currencies, attribution definitions, or conversion-action scopes silently.

### `search-terms.csv`

Required when present: `date`, `campaign_id`, `ad_group_id`, `search_term`, `impressions`, `clicks`, `spend`, `conversions`.

Recommended: `keyword_text`, `match_type`, `conversion_value`, `currency`, `search_term_status`.

Search terms are platform-reported queries, not verified customer intent. Review for names, contact details, health, finance, location, or other sensitive text before processing. Redact or aggregate where necessary; do not try to re-identify a searcher.

### `assets.csv`

Required when present: `asset_id`, `campaign_id`, `asset_type`, `concept_id`, `status`.

Recommended: `ad_group_id`, `asset_group_id`, `asset_name`, `persona`, `pillar`, `angle`, `offer`, `proof`, `format`, `rights_status`, `performance_label`.

A platform label is not a causal verdict. Separate customer hypotheses from crops, lengths, aspect ratios, and other execution variants.

### `products.csv`

Required when present: `date`, `campaign_id`, `product_id`, `product_title`, `product_category`, `status`.

Recommended: `merchant_center_id`, `feed_label`, `availability`, `price`, `spend`, `clicks`, `conversions`, `conversion_value`, `gross_margin`, `currency`.

Product IDs are business entities, not customer identifiers. Feed or policy status establishes the recorded state only; diagnose causes from dated evidence.

### `business-outcomes.csv`

Required when present: `date`, `aggregation_level`, `entity_id`, `gross_revenue`, `new_customers`.

Recommended: `orders`, `qualified_leads`, `refunds`, `cost_of_goods`, `variable_costs`, `contribution_margin`, `currency`, `maturation_window`.

Use aggregated privacy-safe outcomes. State whether `entity_id` refers to account, campaign, market, product, or cohort. Disagreement with Google attribution is evidence to reconcile, not an error to hide.

### `landing-pages.csv`

Required when present: `landing_page_id`, `campaign_id`, `url`, `captured_at`.

Recommended: `ad_group_id`, `ad_id`, `market`, `language`, `offer`, `primary_message`, `proof`, `cta`, `status`.

Capture the destination state that applied during the audit window. Do not crawl, edit, or deploy a page without separate authorization.

## Dated Evidence

Add redacted captures for conversion settings, tag diagnostics, enhanced-conversion status, consent configuration, offline import definitions, experiment readouts, Merchant Center or feed diagnostics, policy states, asset previews and rights, landing pages, business definitions, and incident timelines when available. A screenshot verifies only its visible scope and capture time.

## Privacy

Exclude names, email addresses, phone numbers, postal addresses, customer or user IDs, Customer Match lists, raw offline-conversion identifiers, GCLID or similar identifiers joined to people, payment records, credentials, access tokens, developer tokens, API keys, client secrets, and passwords. Aggregate outcomes before export and redact query or screenshot content that can expose a person.
