# TikTok Ads Audit Input Contract

Use a local bundle so the audit can be repeated without TikTok credentials, live account access, Spark authorization codes, audience files, or private customer records.

## Canonical Bundle

```text
tiktok-ads-audit/
├── context.json
├── ads.csv
├── creatives.csv
├── campaigns.csv              # optional
├── ad-groups.csv              # optional
├── daily-performance.csv      # optional
├── event-definitions.csv      # optional
├── business-outcomes.csv      # optional
├── landing-pages.csv          # optional
└── evidence/                  # optional dated, redacted records
```

Copy templates from `assets/input-bundle/`, remove sample rows, preserve headers, and run:

```bash
python3 skills/paid-media-audit/references/modules/tiktok-ads-audit/scripts/validate_input_bundle.py /path/to/tiktok-ads-audit
```

Validation measures evidence integrity and coverage, not account or creative quality.

## Context

`context.json` requires `schema_version`, `platform_scope`, `decision`, `owner`, `market`, `start_date`, `end_date`, `currency`, `objective`, and `qualified_outcome`. Use schema version `1.0` and platform scope `TikTok Ads Manager (international)`. Add destination type, account timezone, attribution context, conversion delay, offer changes, product releases, inventory, creator events, policy events, or outages where relevant.

If the supplied platform is Douyin or Ocean Engine, do not normalize it into this bundle. Use a future platform-specific audit.

## Export And Normalization Rules

TikTok interface fields and exports change. Preserve original files separately, then map necessary fields into lowercase snake case. Keep stable IDs as strings, zeroes, dates, row grain, currency, timezone, result type, attribution setting, placement, destination, and market visible. Leave unavailable values blank.

Do not combine web, app, lead, shop, or offline outcomes without compatible definitions. Do not combine organic post metrics with paid-ad delivery or add overlapping conversion fields.

## File Schemas

### `ads.csv`

Required: `ad_id`, `campaign_id`, `adgroup_id`, `ad_name`, `status`, `objective`, `destination_type`.

Recommended: `campaign_name`, `adgroup_name`, `placement_type`, `optimization_goal`, `identity_type`, `spark_ad`, `destination_url`.

Use one row per ad. Status describes the export state; it does not authorize changes.

### `creatives.csv`

Required: `creative_id`, `ad_id`, `creative_type`, `concept_id`, `identity_type`.

Recommended: `post_id`, `spark_ad`, `persona`, `pillar`, `angle`, `offer`, `proof`, `format`, `duration_seconds`, `hook`, `caption`, `sound`, `creator`, `rights_status`, `rights_scope`, `rights_expires_at`.

Record authorization status, scope, and expiry only from dated evidence. Never include a Spark authorization code. A post ID may identify public content; it does not establish ownership or permission.

### `campaigns.csv`

Required when present: `campaign_id`, `campaign_name`, `status`, `objective`, `budget_mode`.

Recommended: `budget_amount`, `start_date`, `end_date`, `campaign_type`.

### `ad-groups.csv`

Required when present: `adgroup_id`, `campaign_id`, `adgroup_name`, `status`, `placement_type`, `optimization_goal`.

Recommended: `bid_strategy`, `budget_amount`, `schedule_start`, `schedule_end`, `audience_summary`, `destination_type`.

Do not include audience member lists or direct identifiers. `audience_summary` should be a bounded configuration description, not a user-level export.

### `daily-performance.csv`

Required when present: `date`, `ad_id`, `spend`, `impressions`, `clicks`, `conversions`.

Recommended: `reach`, `video_play_2s`, `video_play_6s`, `video_views_25`, `video_views_50`, `video_views_75`, `video_views_100`, `result_type`, `attributed_revenue`, `currency`, `attribution_setting`.

Preserve each metric's exported definition. Do not compare view or engagement measures with incompatible creative formats or reporting definitions.

### `event-definitions.csv`

Required when present: `event_id`, `event_name`, `source`, `status`, `optimization_event`, `qualified_outcome`.

Recommended: `platform`, `counting_rule`, `value_rule`, `deduplication_rule`, `attribution_setting`, `consent_status`, `captured_at`.

The file describes event contracts and visible settings, not raw event payloads. Do not include cookies, device identifiers, IP addresses, click IDs, or customer identifiers.

### `business-outcomes.csv`

Required when present: `date`, `aggregation_level`, `entity_id`, `gross_revenue`, `new_customers`.

Recommended: `orders`, `qualified_leads`, `refunds`, `cost_of_goods`, `creator_costs`, `variable_costs`, `contribution_margin`, `currency`, `maturation_window`.

Use aggregated privacy-safe outcomes. State whether the entity is account, campaign, ad group, ad, creative concept, market, or cohort. Do not force business rows to equal TikTok attribution.

### `landing-pages.csv`

Required when present: `landing_page_id`, `ad_id`, `url`, `destination_type`, `captured_at`.

Recommended: `market`, `language`, `offer`, `primary_message`, `proof`, `cta`, `app_or_shop_state`, `status`.

Capture the state that applied during the audit window. Do not access a private shop, app account, edit, or deploy from this Skill.

## Dated Evidence

When available, add redacted captures for event and attribution settings, Pixel or Events API diagnostics, app or MMP definitions, consent, experiment readouts, Spark identity and rights status, creator agreements, ad previews, post and paid metrics, destination states, policy decisions, business definitions, and incident timelines.

A screenshot establishes only its visible scope and capture time. A creator name, identity label, post ID, or Spark label does not establish ownership, permission, authenticity, endorsement, or effectiveness.

## Privacy And Credentials

Exclude names, email addresses, phone numbers, postal addresses, customer or user IDs, device or advertising IDs, IP addresses, audience or customer lists, raw event payloads, payment records, access tokens, advertiser authorization tokens, API keys, client secrets, passwords, and Spark authorization codes. Aggregate business outcomes and redact screenshots before use.
