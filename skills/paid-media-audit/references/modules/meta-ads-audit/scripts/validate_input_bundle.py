#!/usr/bin/env python3
"""Validate a canonical local input bundle for the Meta Ads Audit skill."""

import argparse
import csv
import json
import re
import sys
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path


CONTEXT_REQUIRED = {
    "schema_version",
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
        "required": {"ad_id", "campaign_id", "ad_set_id", "ad_name", "status"},
        "recommended": {
            "campaign_name",
            "ad_set_name",
            "objective",
            "destination_url",
        },
        "unique": "ad_id",
    },
    "creatives.csv": {
        "required": {"creative_id", "ad_id", "asset_type", "concept_id"},
        "recommended": {
            "persona",
            "pillar",
            "angle",
            "offer",
            "proof",
            "format",
            "hook",
            "creator",
            "rights_status",
        },
        "unique": "creative_id",
    },
    "daily-performance.csv": {
        "required": {"date", "ad_id", "spend", "impressions", "clicks", "results"},
        "recommended": {
            "reach",
            "landing_page_views",
            "result_type",
            "attributed_revenue",
            "currency",
            "attribution_setting",
        },
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
            "refunds",
            "cost_of_goods",
            "variable_costs",
            "contribution_margin",
            "currency",
        },
    },
    "landing-pages.csv": {
        "required": {"landing_page_id", "ad_id", "url", "captured_at"},
        "recommended": {
            "market",
            "language",
            "offer",
            "primary_message",
            "proof",
            "cta",
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
    re.compile(r"(^|_)(address|street|postal_code|zip_code|date_of_birth|dob|ssn)($|_)"),
    re.compile(r"(^|_)(access_token|refresh_token|api_key|client_secret|password)($|_)"),
)

DATE_COLUMNS = {"date", "captured_at"}
NUMERIC_COLUMNS = {
    "spend",
    "impressions",
    "reach",
    "clicks",
    "landing_page_views",
    "results",
    "attributed_revenue",
    "orders",
    "new_customers",
    "gross_revenue",
    "refunds",
    "cost_of_goods",
    "variable_costs",
    "contribution_margin",
}
NONNEGATIVE_COLUMNS = NUMERIC_COLUMNS - {"contribution_margin"}


def parse_iso_date(value):
    return date.fromisoformat(value)


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
            headers = reader.fieldnames
            if not headers:
                errors.append(f"{filename}: missing header row")
                return [], []
            headers = [header.strip() for header in headers]
            if len(headers) != len(set(headers)):
                errors.append(f"{filename}: duplicate headers are not allowed")
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{filename}: cannot read CSV: {exc}")
        return [], []

    schema = CSV_SCHEMAS[filename]
    missing = sorted(schema["required"] - set(headers))
    if missing:
        errors.append(f"{filename}: missing required header(s): {', '.join(missing)}")

    recommended_missing = sorted(schema.get("recommended", set()) - set(headers))
    if recommended_missing:
        warnings.append(
            f"{filename}: missing recommended header(s): {', '.join(recommended_missing)}"
        )

    forbidden = sorted(header for header in headers if is_forbidden_header(header))
    if forbidden:
        errors.append(
            f"{filename}: forbidden direct-identifier or credential header(s): "
            f"{', '.join(forbidden)}"
        )

    if not rows:
        warnings.append(f"{filename}: contains no data rows")

    unique_column = schema.get("unique")
    unique_values = set()
    for row_number, row in enumerate(rows, start=2):
        for required_header in schema["required"] & set(headers):
            if not (row.get(required_header) or "").strip():
                errors.append(
                    f"{filename}:{row_number}: required value {required_header} is blank"
                )

        if unique_column and unique_column in headers:
            unique_value = (row.get(unique_column) or "").strip()
            if unique_value and unique_value in unique_values:
                errors.append(
                    f"{filename}:{row_number}: duplicate {unique_column} {unique_value!r}"
                )
            unique_values.add(unique_value)

        for column in DATE_COLUMNS & set(headers):
            raw_value = (row.get(column) or "").strip()
            if raw_value:
                try:
                    parse_iso_date(raw_value)
                except ValueError:
                    errors.append(
                        f"{filename}:{row_number}: {column} must use YYYY-MM-DD"
                    )

        for column in NUMERIC_COLUMNS & set(headers):
            raw_value = (row.get(column) or "").strip()
            if not raw_value:
                continue
            try:
                numeric_value = Decimal(raw_value)
                if not numeric_value.is_finite():
                    raise InvalidOperation
            except InvalidOperation:
                errors.append(f"{filename}:{row_number}: {column} must be numeric")
                continue
            if column in NONNEGATIVE_COLUMNS and numeric_value < 0:
                errors.append(f"{filename}:{row_number}: {column} cannot be negative")

    return headers, rows


def validate_context(path, errors):
    try:
        context = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"context.json: cannot read valid JSON: {exc}")
        return {}

    if not isinstance(context, dict):
        errors.append("context.json: root value must be an object")
        return {}

    missing = sorted(
        key for key in CONTEXT_REQUIRED if not str(context.get(key, "")).strip()
    )
    if missing:
        errors.append(f"context.json: missing required field(s): {', '.join(missing)}")

    for forbidden_path in find_forbidden_keys(context):
        errors.append(
            f"context.json: forbidden direct-identifier or credential field: {forbidden_path}"
        )

    start_date = None
    end_date = None
    for field in ("start_date", "end_date"):
        raw_value = context.get(field)
        if raw_value:
            try:
                parsed = parse_iso_date(str(raw_value))
                if field == "start_date":
                    start_date = parsed
                else:
                    end_date = parsed
            except ValueError:
                errors.append(f"context.json: {field} must use YYYY-MM-DD")
    if start_date and end_date and start_date > end_date:
        errors.append("context.json: start_date must be on or before end_date")

    currency = str(context.get("currency", ""))
    if currency and not re.fullmatch(r"[A-Z]{3}", currency):
        errors.append("context.json: currency must be a three-letter uppercase ISO code")

    if context.get("schema_version") not in (None, "1.0"):
        errors.append("context.json: unsupported schema_version; expected 1.0")

    return context


def validate_references(rows_by_file, errors):
    ad_ids = {
        (row.get("ad_id") or "").strip()
        for row in rows_by_file.get("ads.csv", [])
        if (row.get("ad_id") or "").strip()
    }
    for filename in ("creatives.csv", "daily-performance.csv", "landing-pages.csv"):
        for row_number, row in enumerate(rows_by_file.get(filename, []), start=2):
            ad_id = (row.get("ad_id") or "").strip()
            if ad_id and ad_id not in ad_ids:
                errors.append(
                    f"{filename}:{row_number}: ad_id {ad_id!r} is absent from ads.csv"
                )


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
            warnings.append(
                f"Missing optional evidence file: {filename}; related analysis will be unavailable"
            )

    if (bundle / "context.json").is_file():
        validate_context(bundle / "context.json", errors)

    for filename in CSV_SCHEMAS:
        path = bundle / filename
        if not path.is_file():
            continue
        _, rows = read_csv(path, filename, errors, warnings)
        rows_by_file[filename] = rows

    validate_references(rows_by_file, errors)

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "present_files": present_files,
            "row_counts": {
                filename: len(rows) for filename, rows in sorted(rows_by_file.items())
            },
        },
    }


def print_text_result(result):
    status = "VALID" if result["valid"] else "INVALID"
    print(f"Meta Ads audit input bundle: {status}")
    for error in result["errors"]:
        print(f"ERROR: {error}")
    for warning in result["warnings"]:
        print(f"WARNING: {warning}")
    row_counts = result["summary"].get("row_counts", {})
    if row_counts:
        counts = ", ".join(f"{name}={count}" for name, count in row_counts.items())
        print(f"Rows: {counts}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate a canonical local Meta Ads audit input bundle."
    )
    parser.add_argument("bundle", help="Path to the input-bundle directory")
    parser.add_argument(
        "--json", action="store_true", dest="as_json", help="Emit JSON output"
    )
    args = parser.parse_args(argv)

    result = validate_bundle(args.bundle)
    if args.as_json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_text_result(result)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
