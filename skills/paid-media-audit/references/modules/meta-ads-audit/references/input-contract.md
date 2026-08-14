# Input Contract

Use a local canonical bundle so an audit can be repeated without Meta credentials, live account access, or private customer records.

## Canonical Bundle

```text
meta-ads-audit/
├── context.json
├── ads.csv
├── creatives.csv
├── daily-performance.csv        # optional
├── business-outcomes.csv        # optional
├── landing-pages.csv            # optional
└── evidence/                    # optional screenshots or dated records
```

Copy the templates from `assets/input-bundle/`, remove the sample rows, and preserve the canonical headers. Run:

```bash
python3 skills/paid-media-audit/references/modules/meta-ads-audit/scripts/validate_input_bundle.py /path/to/meta-ads-audit
```

Use `--json` when another tool needs machine-readable results. Validation measures evidence completeness, not account quality.

## Required Context

`context.json` must contain:

| Field | Meaning |
| --- | --- |
| `schema_version` | Use `1.0` for this contract |
| `decision` | The decision this audit should inform |
| `owner` | Role or team accountable for the decision |
| `market` | Bounded country, region, or operating market |
| `start_date`, `end_date` | Inclusive audit window in `YYYY-MM-DD` |
| `currency` | Three-letter uppercase ISO currency code |
| `objective` | Declared advertising objective |
| `qualified_outcome` | Downstream customer or business result that defines useful growth |

Record material constraints, attribution context, offer changes, launch dates, outages, inventory limits, or policy events as additional fields. Do not put credentials or direct customer identifiers in the context file.

## Build The Exports

Meta interface labels and export options can change. In Ads Manager, create a dated report at ad level, select the relevant identifiers and delivery fields, add the measures needed for the decision, use a daily time breakdown for trend analysis, and export CSV. Keep the original export outside the canonical bundle if it contains extra fields; map only necessary columns into the templates.

Use two logical extracts:

1. Populate `ads.csv` with stable campaign, ad set, and ad identifiers plus names, delivery status, objective, and destination.
2. Populate `daily-performance.csv` with one row per date and ad. Keep reported results, result type, attribution setting, currency, and attributed revenue visible instead of silently reconciling unlike definitions.

The export may use localized, title-cased, or spaced labels. Normalize them to lowercase snake case. Example mappings include `Ad ID` to `ad_id`, `Campaign ID` to `campaign_id`, `Ad set ID` to `ad_set_id`, `Amount spent` to `spend`, `Landing page views` to `landing_page_views`, and the chosen result column to `results`. Verify the mapping against the export's own definitions; do not infer a result type from the number alone.

## File Schemas

### `ads.csv`

Required: `ad_id`, `campaign_id`, `ad_set_id`, `ad_name`, `status`.

Recommended: `campaign_name`, `ad_set_name`, `objective`, `destination_url`.

Use one row per ad. Preserve stable IDs as strings. Status is descriptive evidence from the export, not authorization to change delivery.

### `creatives.csv`

Required: `creative_id`, `ad_id`, `asset_type`, `concept_id`.

Recommended: `persona`, `pillar`, `angle`, `offer`, `proof`, `format`, `hook`, `creator`, `rights_status`.

Build this inventory from creative files, thumbnails, briefs, copy records, or dated screenshots. `concept_id` represents a customer or value hypothesis. A crop, opening frame, caption length, or aspect-ratio change remains an execution variant unless the underlying hypothesis changes.

### `daily-performance.csv`

Required when present: `date`, `ad_id`, `spend`, `impressions`, `clicks`, `results`.

Recommended: `reach`, `landing_page_views`, `result_type`, `attributed_revenue`, `currency`, `attribution_setting`.

Do not mix currencies or result definitions without explicit segmentation. Retain zeroes. Leave genuinely unavailable measures blank rather than estimating them.

### `business-outcomes.csv`

Required when present: `date`, `aggregation_level`, `entity_id`, `gross_revenue`, `new_customers`.

Recommended: `orders`, `refunds`, `cost_of_goods`, `variable_costs`, `contribution_margin`, `currency`.

Use aggregated, privacy-safe outcomes by date and permitted entity level. State whether `entity_id` refers to account, campaign, ad set, ad, market, or cohort. Use matured finance or commerce definitions where possible. A row need not reconcile to Meta attribution; discrepancies are audit evidence.

### `landing-pages.csv`

Required when present: `landing_page_id`, `ad_id`, `url`, `captured_at`.

Recommended: `market`, `language`, `offer`, `primary_message`, `proof`, `cta`, `status`.

Record the dated page state that the ad actually reached. Use screenshots in `evidence/` when a page changes during the audit window. Do not crawl, edit, or deploy the page unless separately authorized.

## Measurement Evidence

Add dated, redacted records in `evidence/` when available:

- Events Manager diagnostics, event definitions, event-match or deduplication evidence;
- attribution settings and reporting-window definitions;
- commerce, CRM, finance, refund, retained-value, or new-customer definitions;
- experiment design and mature incrementality readouts;
- creative thumbnails, briefs, usage rights, and landing-page captures;
- relevant incident, offer, pricing, inventory, tracking, or release timelines.

Screenshots establish only what is visible at capture time. Record the capture date, source surface, market, account scope, and any redaction.

## Privacy And Security

Exclude raw names, email addresses, phone numbers, postal addresses, customer or user IDs, lead lists, custom-audience files, payment records, credentials, access tokens, API keys, client secrets, and passwords. Aggregate customer outcomes before export. Redact screenshots. Prefer the smallest evidence that can change the decision.

Do not request or use Meta login credentials for this Skill. Marketing API integrations, access review, data retention, and live account operations require a separate authorized implementation.
