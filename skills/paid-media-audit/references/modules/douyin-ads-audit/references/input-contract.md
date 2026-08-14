# Douyin Ads Audit Input Contract

Use a local bundle so an audit can be repeated without credentials, live account access, creator authorization codes, raw lead data, audience files, or customer records.

## Canonical Bundle

```text
douyin-ads-audit/
├── context.json
├── ads.csv
├── creatives.csv
├── campaigns.csv                 # optional
├── ad-groups.csv                 # optional
├── daily-performance.csv         # optional
├── conversion-definitions.csv    # optional
├── commerce-outcomes.csv         # optional
├── business-outcomes.csv         # optional
├── destinations.csv              # optional
└── evidence/                     # optional dated, redacted records
```

Copy templates from `assets/input-bundle/`, remove sample rows, preserve headers, and run:

```bash
python3 skills/paid-media-audit/references/modules/douyin-ads-audit/scripts/validate_input_bundle.py /path/to/douyin-ads-audit
```

Validation measures evidence integrity and coverage, not advertising quality.

## Context

`context.json` requires `schema_version`, `platform_scope`, `decision`, `owner`, `market`, `start_date`, `end_date`, `currency`, `objective`, and `qualified_outcome`. Use schema version `1.0` and platform scope `Douyin advertising`. Add declared source surfaces, inventory, destination type, account timezone, attribution context, order delay, offer or price changes, product availability, creator events, livestream schedule, policy events, and incidents where relevant.

International TikTok must not be normalized into this bundle.

## Export And Normalization Rules

Platform labels and exports change. Preserve original files separately, then map necessary fields into lowercase snake case. Keep stable IDs as strings, zeroes, source surface, placement, row grain, dates, currency, result type, attribution setting, destination, and market visible. Leave unavailable values blank.

Do not silently combine Ocean Engine, Qianchuan, DOU+, organic, Xingtu, shop, product, livestream, app, lead, or offline data. Do not add overlapping conversions, attributed orders, paid orders, or GMV fields.

## File Schemas

### `ads.csv`

Required: `ad_id`, `campaign_id`, `ad_group_id`, `ad_name`, `status`, `source_surface`, `inventory_scope`, `objective`, `destination_type`.

Recommended: `campaign_name`, `ad_group_name`, `placement`, `optimization_goal`, `identity_type`, `douyin_account`, `destination_ref`.

Use one row per ad. `source_surface` should identify `ocean_engine`, `qianchuan`, `dou_plus`, or another directly verified surface. A multi-placement row without a breakdown cannot support a Douyin-only conclusion.

### `creatives.csv`

Required: `creative_id`, `ad_id`, `creative_type`, `concept_id`, `identity_type`.

Recommended: `content_id`, `douyin_account`, `persona`, `pillar`, `angle`, `offer`, `proof`, `format`, `duration_seconds`, `hook`, `caption`, `music`, `creator`, `xingtu_status`, `rights_status`, `rights_scope`, `rights_expires_at`, `product_id`, `livestream_id`.

A content ID or visible account does not establish ownership, endorsement, cooperation, or paid rights. Never include an authorization code or token.

### `campaigns.csv`

Required when present: `campaign_id`, `campaign_name`, `status`, `source_surface`, `objective`, `budget_mode`.

Recommended: `inventory_scope`, `budget_amount`, `start_date`, `end_date`, `campaign_type`.

### `ad-groups.csv`

Required when present: `ad_group_id`, `campaign_id`, `ad_group_name`, `status`, `source_surface`, `placement`, `optimization_goal`.

Recommended: `bid_strategy`, `budget_amount`, `schedule_start`, `schedule_end`, `audience_summary`, `destination_type`.

Use aggregate configuration descriptions. Do not include audience member or lead records.

### `daily-performance.csv`

Required when present: `date`, `ad_id`, `source_surface`, `spend`, `impressions`, `clicks`, `conversions`.

Recommended: `reach`, `video_play_2s`, `video_play_5s`, `video_views_25`, `video_views_50`, `video_views_75`, `video_views_100`, `result_type`, `attributed_orders`, `attributed_gmv`, `currency`, `attribution_setting`.

Preserve exported definitions. Do not compare view measures across incompatible formats, products, placements, or reporting definitions.

### `conversion-definitions.csv`

Required when present: `conversion_id`, `conversion_name`, `source_surface`, `source`, `status`, `optimization_event`, `qualified_outcome`.

Recommended: `counting_rule`, `value_rule`, `deduplication_rule`, `attribution_setting`, `consent_status`, `captured_at`.

Describe event contracts and settings only. Do not include raw lead, event, cookie, device, IP, or click-level payloads.

### `commerce-outcomes.csv`

Required when present: `date`, `source_surface`, `aggregation_level`, `entity_id`, `paid_orders`, `gross_merchandise_value`.

Recommended: `product_id`, `livestream_id`, `cancellations`, `refunds`, `gross_revenue`, `platform_fees`, `creator_commission`, `product_cost`, `fulfillment_cost`, `variable_costs`, `contribution_margin`, `currency`, `maturation_window`.

Use matured, aggregate, privacy-safe commerce evidence. GMV is transaction value, not revenue or profit. Preserve cancellations, refunds, fees, commission, fulfillment, and order maturity.

### `business-outcomes.csv`

Required when present: `date`, `aggregation_level`, `entity_id`, `gross_revenue`, `new_customers`.

Recommended: `orders`, `qualified_leads`, `refunds`, `cost_of_goods`, `creator_costs`, `variable_costs`, `contribution_margin`, `currency`, `maturation_window`.

Use aggregate outcomes and state the entity scope. Platform and business totals may disagree; preserve the residual for reconciliation.

### `destinations.csv`

Required when present: `destination_id`, `ad_id`, `destination_type`, `destination_ref`, `captured_at`.

Recommended: `market`, `language`, `offer`, `price`, `primary_message`, `proof`, `cta`, `product_or_livestream_state`, `status`.

Capture the landing page, app, native form, shop, product, or livestream state that applied during the audit window. Do not access private systems or edit a destination.

## Dated Evidence

Add redacted captures for conversion and attribution settings, event diagnostics, consent, experiment readouts, creator or Xingtu cooperation and rights, ad previews, organic and paid metrics, product and shop status, livestream schedule, destination state, policy records, finance definitions, and incident timelines when available.

A screenshot establishes only its visible scope and capture time. An account name, content ID, creator label, cooperation status, or platform badge does not establish authorization, authenticity, endorsement, ownership, or effectiveness.

## Privacy And Credentials

Exclude names, phone numbers, email addresses, postal addresses, raw leads, customer or user IDs, device and advertising IDs, IP addresses, click IDs linked to people, audience lists, raw event payloads, payment records, credentials, access tokens, developer secrets, and creator authorization codes. Aggregate customer, lead, order, and commerce outcomes before use.
