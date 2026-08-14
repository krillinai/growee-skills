#!/usr/bin/env python3
"""Tests for the Google Ads Audit input-bundle validator."""

import csv
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("validate_input_bundle.py")
SPEC = importlib.util.spec_from_file_location("google_ads_validator", SCRIPT_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.bundle = Path(self.tempdir.name)

    def tearDown(self):
        self.tempdir.cleanup()

    def write_context(self, **overrides):
        value = {
            "schema_version": "1.0",
            "decision": "Review evidence",
            "owner": "Growth",
            "market": "US",
            "start_date": "2026-06-01",
            "end_date": "2026-06-30",
            "currency": "USD",
            "objective": "Qualified acquisition",
            "qualified_outcome": "Matured new customer",
        }
        value.update(overrides)
        (self.bundle / "context.json").write_text(json.dumps(value), encoding="utf-8")

    def write_csv(self, filename, headers, rows):
        with (self.bundle / filename).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    def write_required(self):
        self.write_context()
        self.write_csv(
            "campaigns.csv",
            ["campaign_id", "campaign_name", "status", "advertising_channel_type", "bidding_strategy_type"],
            [{
                "campaign_id": "campaign-1",
                "campaign_name": "Search",
                "status": "ENABLED",
                "advertising_channel_type": "SEARCH",
                "bidding_strategy_type": "MAXIMIZE_CONVERSIONS",
            }],
        )
        self.write_csv(
            "conversion-actions.csv",
            ["conversion_action_id", "conversion_action_name", "category", "status", "primary_for_goal", "counting_type"],
            [{
                "conversion_action_id": "conversion-1",
                "conversion_action_name": "Purchase",
                "category": "PURCHASE",
                "status": "ENABLED",
                "primary_for_goal": "true",
                "counting_type": "EVERY",
            }],
        )

    def test_minimal_bundle_is_valid_with_coverage_warnings(self):
        self.write_required()
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertTrue(result["valid"])
        self.assertTrue(any("optional evidence" in warning for warning in result["warnings"]))

    def test_missing_required_file_is_invalid(self):
        self.write_context()
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("campaigns.csv" in error for error in result["errors"]))

    def test_forbidden_identifier_header_is_invalid(self):
        self.write_required()
        self.write_csv(
            "daily-performance.csv",
            ["date", "campaign_id", "spend", "impressions", "clicks", "conversions", "conversion_value", "email"],
            [{
                "date": "2026-06-01",
                "campaign_id": "campaign-1",
                "spend": "1",
                "impressions": "10",
                "clicks": "2",
                "conversions": "1",
                "conversion_value": "5",
                "email": "redacted@example.com",
            }],
        )
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("forbidden" in error for error in result["errors"]))

    def test_unknown_campaign_reference_is_invalid(self):
        self.write_required()
        self.write_csv(
            "assets.csv",
            ["asset_id", "campaign_id", "asset_type", "concept_id", "status"],
            [{
                "asset_id": "asset-1",
                "campaign_id": "missing",
                "asset_type": "IMAGE",
                "concept_id": "concept-1",
                "status": "ENABLED",
            }],
        )
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("absent from campaigns.csv" in error for error in result["errors"]))

    def test_invalid_date_and_negative_spend_are_rejected(self):
        self.write_required()
        self.write_csv(
            "daily-performance.csv",
            ["date", "campaign_id", "spend", "impressions", "clicks", "conversions", "conversion_value"],
            [{
                "date": "06/01/2026",
                "campaign_id": "campaign-1",
                "spend": "-2",
                "impressions": "10",
                "clicks": "2",
                "conversions": "1",
                "conversion_value": "5",
            }],
        )
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("YYYY-MM-DD" in error for error in result["errors"]))
        self.assertTrue(any("cannot be negative" in error for error in result["errors"]))

    def test_shipped_template_bundle_is_valid(self):
        source = SCRIPT_PATH.parent.parent / "assets" / "input-bundle"
        for template in source.glob("*.template.*"):
            target_name = template.name.replace(".template", "")
            shutil.copyfile(template, self.bundle / target_name)
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertTrue(result["valid"], result["errors"])


if __name__ == "__main__":
    unittest.main()
