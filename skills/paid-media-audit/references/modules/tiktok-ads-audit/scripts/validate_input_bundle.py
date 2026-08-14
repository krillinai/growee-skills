#!/usr/bin/env python3
"""Validate a canonical local input bundle for TikTok Ads Audit."""

import argparse
import csv
import json
import re
import sys
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path


EXPECTED_PLATFORM = "TikTok Ads Manager (international)"
CONTEXT_REQUIRED = {
    "schema_version",
    "platform_scope",
    "decision",
    "owner",
    "market",
    "start_date",
    "end_date",
    "currency",
    "objective",
    "qualified_outcome",
}

CSV_SCHEMAS = {
    "ads.csv": {
        "required": {
            "ad_id",
            "campaign_id",
            "adgroup_id",
            "ad_name",
            "status",
            "objective",
            "destination_type",
        },
        "recommended": {
            "campaign_name",
            "adgroup_name",
            "placement_type",
            "optimization_goal",
            "identity_type",
            "spark_ad",
            "destination_url",
        },
        "unique": "ad_id",
    },
    "creatives.csv": {
        "required": {"creative_id", "ad_id", "creative_type", "concept_id", "identity_type"},
        "recommended": {
            "post_id",
            "spark_ad",
            "persona",
            "pillar",
            "angle",
            "offer",
            "proof",
            "format",
            "duration_seconds",
            "hook",
            "caption",
            "sound",
            "creator",
            "rights_status",
            "rights_scope",
            "rights_expires_at",
        },
        "unique": "creative_id",
    },
    "campaigns.csv": {
        "required": {"campaign_id", "campaign_name", "status", "objective", "budget_mode"},
        "recommended": {"budget_amount", "start_date", "end_date", "campaign_type"},
        "unique": "campaign_id",
    },
    "ad-groups.csv": {
        "required": {
            "adgroup_id",
            "campaign_id",
            "adgroup_name",
            "status",
            "placement_type",
            "optimization_goal",
        },
        "recommended": {
            "bid_strategy",
            "budget_amount",
            "schedule_start",
            "schedule_end",
            "audience_summary",
            "destination_type",
        },
        "unique": "adgroup_id",
    },
    "daily-performance.csv": {
        "required": {"date", "ad_id", "spend", "impressions", "clicks", "conversions"},
        "recommended": {
            "reach",
            "video_play_2s",
            "video_play_6s",
            "video_views_25",
            "video_views_50",
            "video_views_75",
            "video_views_100",
            "result_type",
            "attributed_revenue",
            "currency",
            "attribution_setting",
        },
    },
    "event-definitions.csv": {
        "required": {
            "event_id",
            "event_name",
            "source",
            "status",
            "optimization_event",
            "qualified_outcome",
        },
        "recommended": {
            "platform",
            "counting_rule",
            "value_rule",
            "deduplication_rule",
            "attribution_setting",
            "consent_status",
            "captured_at",
        },
        "unique": "event_id",
    },
    "business-outcomes.csv": {
        "required": {
            "date",
            "aggregation_level",
            "entity_id",
            "gross_revenue",
            "new_customers",
        },
        "recommended": {
            "orders",
            "qualified_leads",
            "refunds",
            "cost_of_goods",
            "creator_costs",
            "variable_costs",
            "contribution_margin",
            "currency",
            "maturation_window",
        },
    },
    "landing-pages.csv": {
        "required": {"landing_page_id", "ad_id", "url", "destination_type", "captured_at"},
        "recommended": {
            "market",
            "language",
            "offer",
            "primary_message",
            "proof",
            "cta",
            "app_or_shop_state",
            "status",
        },
        "unique": "landing_page_id",
    },
}

REQUIRED_FILES = {"context.json", "ads.csv", "creatives.csv"}
OPTIONAL_FILES = set(CSV_SCHEMAS) - {"ads.csv", "creatives.csv"}

FORBIDDEN_HEADER_PATTERNS = (
    re.compile(r"(^|_)(email|e_mail|phone|mobile|telephone)($|_)"),
    re.compile(r"(^|_)(first_name|last_name|full_name|customer_name|contact_name)($|_)"),
    re.compile(r"(^|_)(customer_id|user_id|external_id|subscriber_id|lead_id)($|_)"),
    re.compile(r"(^|_)(address|street|postal_code|zip_code|date_of_birth|dob|ssn|ip_address)($|_)"),
    re.compile(r"(^|_)(device_id|advertising_id|idfa|gaid)($|_)"),
    re.compile(r"(^|_)(access_token|refresh_token|authorization_token|authorization_code|api_key|client_secret|password)($|_)"),
)

DATE_COLUMNS = {"date", "captured_at", "start_date", "end_date", "schedule_start", "schedule_end", "rights_expires_at"}
NUMERIC_COLUMNS = {
    "budget_amount",
    "duration_seconds",
    "spend",
    "impressions",
    "reach",
    "clicks",
    "video_play_2s",
    "video_play_6s",
    "video_views_25",
    "video_views_50",
    "video_views_75",
    "video_views_100",
    "conversions",
    "attributed_revenue",
    "orders",
    "qualified_leads",
    "new_customers",
    "gross_revenue",
    "refunds",
    "cost_of_goods",
    "creator_costs",
    "variable_costs",
    "contribution_margin",
}
NONNEGATIVE_COLUMNS = NUMERIC_COLUMNS - {"contribution_margin"}
BOOLEAN_COLUMNS = {"spark_ad", "optimization_event", "qualified_outcome"}


def is_forbidden_header(header):
    normalized = header.strip().lower().replace("-", "_").replace(" ", "_")
    return any(pattern.search(normalized) for pattern in FORBIDDEN_HEADER_PATTERNS)


def find_forbidden_keys(value, path="context"):
    findings = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if is_forbidden_header(str(key)):
                findings.append(child_path)
            findings.extend(find_forbidden_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(find_forbidden_keys(child, f"{path}[{index}]"))
    return findings


def read_csv(path, filename, errors, warnings):
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames:
                errors.append(f"{filename}: missing header row")
                return [], []
            headers = [header.strip() for header in reader.fieldnames]
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{filename}: cannot read CSV: {exc}")
        return [], []

    if len(headers) != len(set(headers)):
        errors.append(f"{filename}: duplicate headers are not allowed")
    schema = CSV_SCHEMAS[filename]
    missing = sorted(schema["required"] - set(headers))
    if missing:
        errors.append(f"{filename}: missing required header(s): {', '.join(missing)}")
    recommended_missing = sorted(schema.get("recommended", set()) - set(headers))
    if recommended_missing:
        warnings.append(f"{filename}: missing recommended header(s): {', '.join(recommended_missing)}")
    forbidden = sorted(header for header in headers if is_forbidden_header(header))
    if forbidden:
        errors.append(f"{filename}: forbidden identifier, credential, or authorization header(s): {', '.join(forbidden)}")
    if not rows:
        warnings.append(f"{filename}: contains no data rows")

    unique_column = schema.get("unique")
    unique_values = set()
    for row_number, row in enumerate(rows, start=2):
        for required_header in schema["required"] & set(headers):
            if not (row.get(required_header) or "").strip():
                errors.append(f"{filename}:{row_number}: required value {required_header} is blank")
        if unique_column and unique_column in headers:
            value = (row.get(unique_column) or "").strip()
            if value and value in unique_values:
                errors.append(f"{filename}:{row_number}: duplicate {unique_column} {value!r}")
            unique_values.add(value)
        for column in DATE_COLUMNS & set(headers):
            value = (row.get(column) or "").strip()
            if value:
                try:
                    date.fromisoformat(value)
                except ValueError:
                    errors.append(f"{filename}:{row_number}: {column} must use YYYY-MM-DD")
        for column in NUMERIC_COLUMNS & set(headers):
            value = (row.get(column) or "").strip()
            if not value:
                continue
            try:
                number = Decimal(value)
                if not number.is_finite():
                    raise InvalidOperation
            except InvalidOperation:
                errors.append(f"{filename}:{row_number}: {column} must be numeric")
                continue
            if column in NONNEGATIVE_COLUMNS and number < 0:
                errors.append(f"{filename}:{row_number}: {column} cannot be negative")
        for column in BOOLEAN_COLUMNS & set(headers):
            value = (row.get(column) or "").strip().lower()
            if value and value not in {"true", "false"}:
                errors.append(f"{filename}:{row_number}: {column} must be true or false")
    return headers, rows


def validate_context(path, errors):
    try:
        context = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"context.json: cannot read valid JSON: {exc}")
        return
    if not isinstance(context, dict):
        errors.append("context.json: root value must be an object")
        return
    missing = sorted(key for key in CONTEXT_REQUIRED if not str(context.get(key, "")).strip())
    if missing:
        errors.append(f"context.json: missing required field(s): {', '.join(missing)}")
    for forbidden_path in find_forbidden_keys(context):
        errors.append(f"context.json: forbidden identifier, credential, or authorization field: {forbidden_path}")
    if context.get("platform_scope") and context["platform_scope"] != EXPECTED_PLATFORM:
        errors.append(f"context.json: platform_scope must be {EXPECTED_PLATFORM!r}; Douyin and Ocean Engine require a separate audit")

    parsed_dates = {}
    for field in ("start_date", "end_date"):
        if context.get(field):
            try:
                parsed_dates[field] = date.fromisoformat(str(context[field]))
            except ValueError:
                errors.append(f"context.json: {field} must use YYYY-MM-DD")
    if parsed_dates.get("start_date") and parsed_dates.get("end_date"):
        if parsed_dates["start_date"] > parsed_dates["end_date"]:
            errors.append("context.json: start_date must be on or before end_date")
    currency = str(context.get("currency", ""))
    if currency and not re.fullmatch(r"[A-Z]{3}", currency):
        errors.append("context.json: currency must be a three-letter uppercase ISO code")
    if context.get("schema_version") not in (None, "1.0"):
        errors.append("context.json: unsupported schema_version; expected 1.0")


def id_set(rows, field):
    return {(row.get(field) or "").strip() for row in rows if (row.get(field) or "").strip()}


def require_parent(rows_by_file, child_file, child_field, parent_file, parent_field, errors):
    if parent_file not in rows_by_file:
        return
    parents = id_set(rows_by_file[parent_file], parent_field)
    for row_number, row in enumerate(rows_by_file.get(child_file, []), start=2):
        value = (row.get(child_field) or "").strip()
        if value and value not in parents:
            errors.append(f"{child_file}:{row_number}: {child_field} {value!r} is absent from {parent_file}")


def validate_references(rows_by_file, errors):
    for child_file in ("creatives.csv", "daily-performance.csv", "landing-pages.csv"):
        require_parent(rows_by_file, child_file, "ad_id", "ads.csv", "ad_id", errors)
    for child_file in ("ads.csv", "ad-groups.csv"):
        require_parent(rows_by_file, child_file, "campaign_id", "campaigns.csv", "campaign_id", errors)
    require_parent(rows_by_file, "ads.csv", "adgroup_id", "ad-groups.csv", "adgroup_id", errors)


def validate_bundle(bundle_path):
    bundle = Path(bundle_path)
    errors = []
    warnings = []
    rows_by_file = {}
    if not bundle.is_dir():
        return {
            "valid": False,
            "errors": [f"Bundle path is not a directory: {bundle}"],
            "warnings": [],
            "summary": {"present_files": [], "row_counts": {}},
        }
    present_files = sorted(path.name for path in bundle.iterdir() if path.is_file())
    for filename in sorted(REQUIRED_FILES):
        if not (bundle / filename).is_file():
            errors.append(f"Missing required file: {filename}")
    for filename in sorted(OPTIONAL_FILES):
        if not (bundle / filename).is_file():
            warnings.append(f"Missing optional evidence file: {filename}; related analysis will be unavailable")
    if (bundle / "context.json").is_file():
        validate_context(bundle / "context.json", errors)
    for filename in CSV_SCHEMAS:
        path = bundle / filename
        if path.is_file():
            _, rows_by_file[filename] = read_csv(path, filename, errors, warnings)
    validate_references(rows_by_file, errors)
    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "present_files": present_files,
            "row_counts": {name: len(rows) for name, rows in sorted(rows_by_file.items())},
        },
    }


def print_text_result(result):
    print(f"TikTok Ads audit input bundle: {'VALID' if result['valid'] else 'INVALID'}")
    for error in result["errors"]:
        print(f"ERROR: {error}")
    for warning in result["warnings"]:
        print(f"WARNING: {warning}")
    if result["summary"].get("row_counts"):
        counts = ", ".join(f"{name}={count}" for name, count in result["summary"]["row_counts"].items())
        print(f"Rows: {counts}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate a canonical TikTok Ads audit input bundle.")
    parser.add_argument("bundle", help="Path to the input-bundle directory")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit JSON output")
    args = parser.parse_args(argv)
    result = validate_bundle(args.bundle)
    if args.as_json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_text_result(result)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
