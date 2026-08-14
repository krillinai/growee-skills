#!/usr/bin/env python3
"""Tests for the TikTok Ads Audit input-bundle validator."""

import csv
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("validate_input_bundle.py")
SPEC = importlib.util.spec_from_file_location("tiktok_ads_validator", SCRIPT_PATH)
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
            "platform_scope": "TikTok Ads Manager (international)",
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
            "ads.csv",
            ["ad_id", "campaign_id", "adgroup_id", "ad_name", "status", "objective", "destination_type"],
            [{
                "ad_id": "ad-1",
                "campaign_id": "campaign-1",
                "adgroup_id": "adgroup-1",
                "ad_name": "Proof video",
                "status": "active",
                "objective": "conversion",
                "destination_type": "website",
            }],
        )
        self.write_csv(
            "creatives.csv",
            ["creative_id", "ad_id", "creative_type", "concept_id", "identity_type"],
            [{
                "creative_id": "creative-1",
                "ad_id": "ad-1",
                "creative_type": "video",
                "concept_id": "concept-1",
                "identity_type": "custom_identity",
            }],
        )

    def test_minimal_bundle_is_valid_with_coverage_warnings(self):
        self.write_required()
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertTrue(result["valid"])
        self.assertTrue(any("optional evidence" in warning for warning in result["warnings"]))

    def test_douyin_scope_is_rejected(self):
        self.write_required()
        self.write_context(platform_scope="Douyin Ocean Engine")
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("separate audit" in error for error in result["errors"]))

    def test_authorization_code_header_is_rejected(self):
        self.write_required()
        self.write_csv(
            "creatives.csv",
            ["creative_id", "ad_id", "creative_type", "concept_id", "identity_type", "authorization_code"],
            [{
                "creative_id": "creative-1",
                "ad_id": "ad-1",
                "creative_type": "video",
                "concept_id": "concept-1",
                "identity_type": "spark",
                "authorization_code": "secret",
            }],
        )
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("authorization" in error for error in result["errors"]))

    def test_unknown_ad_reference_is_invalid(self):
        self.write_required()
        self.write_csv(
            "daily-performance.csv",
            ["date", "ad_id", "spend", "impressions", "clicks", "conversions"],
            [{
                "date": "2026-06-01",
                "ad_id": "missing",
                "spend": "1",
                "impressions": "10",
                "clicks": "2",
                "conversions": "1",
            }],
        )
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("absent from ads.csv" in error for error in result["errors"]))

    def test_invalid_date_and_negative_spend_are_rejected(self):
        self.write_required()
        self.write_csv(
            "daily-performance.csv",
            ["date", "ad_id", "spend", "impressions", "clicks", "conversions"],
            [{
                "date": "06/01/2026",
                "ad_id": "ad-1",
                "spend": "-2",
                "impressions": "10",
                "clicks": "2",
                "conversions": "1",
            }],
        )
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertFalse(result["valid"])
        self.assertTrue(any("YYYY-MM-DD" in error for error in result["errors"]))
        self.assertTrue(any("cannot be negative" in error for error in result["errors"]))

    def test_shipped_template_bundle_is_valid(self):
        source = SCRIPT_PATH.parent.parent / "assets" / "input-bundle"
        for template in source.glob("*.template.*"):
            shutil.copyfile(template, self.bundle / template.name.replace(".template", ""))
        result = VALIDATOR.validate_bundle(self.bundle)
        self.assertTrue(result["valid"], result["errors"])


if __name__ == "__main__":
    unittest.main()
