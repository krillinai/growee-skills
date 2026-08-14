#!/usr/bin/env python3
"""Tests for the Meta Ads audit input-bundle validator."""

import csv
import json
import tempfile
import unittest
from pathlib import Path

from validate_input_bundle import validate_bundle


CONTEXT = {
    "schema_version": "1.0",
    "decision": "Decide which evidence to collect before the next media review",
    "owner": "Growth team",
    "market": "US",
    "start_date": "2026-06-01",
    "end_date": "2026-06-30",
    "currency": "USD",
    "objective": "Qualified purchases",
    "qualified_outcome": "First orders from new customers after refund maturation",
}

ADS_HEADERS = [
    "ad_id",
    "campaign_id",
    "campaign_name",
    "ad_set_id",
    "ad_set_name",
    "ad_name",
    "status",
    "objective",
    "destination_url",
]

CREATIVE_HEADERS = [
    "creative_id",
    "ad_id",
    "asset_type",
    "concept_id",
    "persona",
    "pillar",
    "angle",
    "offer",
    "proof",
    "format",
    "hook",
    "creator",
    "rights_status",
]


def write_csv(path, headers, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


class ValidateInputBundleTests(unittest.TestCase):
    def make_bundle(self):
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        bundle = Path(temporary_directory.name)
        (bundle / "context.json").write_text(
            json.dumps(CONTEXT), encoding="utf-8"
        )
        write_csv(
            bundle / "ads.csv",
            ADS_HEADERS,
            [
                {
                    "ad_id": "ad-1",
                    "campaign_id": "campaign-1",
                    "campaign_name": "Prospecting",
                    "ad_set_id": "adset-1",
                    "ad_set_name": "Broad",
                    "ad_name": "Customer proof video",
                    "status": "active",
                    "objective": "purchase",
                    "destination_url": "https://example.com/product",
                }
            ],
        )
        write_csv(
            bundle / "creatives.csv",
            CREATIVE_HEADERS,
            [
                {
                    "creative_id": "creative-1",
                    "ad_id": "ad-1",
                    "asset_type": "video",
                    "concept_id": "concept-proof-1",
                    "persona": "operations lead",
                    "pillar": "time saved",
                    "angle": "customer proof",
                    "offer": "demo",
                    "proof": "attributable testimonial",
                    "format": "9:16",
                    "hook": "See the workflow before and after",
                    "creator": "brand",
                    "rights_status": "verified",
                }
            ],
        )
        return bundle

    def test_valid_minimal_bundle_returns_warnings_but_no_errors(self):
        bundle = self.make_bundle()

        result = validate_bundle(bundle)

        self.assertTrue(result["valid"])
        self.assertEqual([], result["errors"])
        self.assertTrue(
            any("daily-performance.csv" in warning for warning in result["warnings"])
        )

    def test_missing_required_header_is_an_error(self):
        bundle = self.make_bundle()
        write_csv(
            bundle / "ads.csv",
            [header for header in ADS_HEADERS if header != "ad_id"],
            [],
        )

        result = validate_bundle(bundle)

        self.assertFalse(result["valid"])
        self.assertTrue(any("ads.csv" in error and "ad_id" in error for error in result["errors"]))

    def test_context_start_date_after_end_date_is_an_error(self):
        bundle = self.make_bundle()
        invalid_context = {**CONTEXT, "start_date": "2026-07-01", "end_date": "2026-06-01"}
        (bundle / "context.json").write_text(
            json.dumps(invalid_context), encoding="utf-8"
        )

        result = validate_bundle(bundle)

        self.assertFalse(result["valid"])
        self.assertTrue(any("start_date" in error and "end_date" in error for error in result["errors"]))

    def test_forbidden_pii_header_is_an_error(self):
        bundle = self.make_bundle()
        write_csv(
            bundle / "ads.csv",
            ADS_HEADERS + ["customer_email"],
            [
                {
                    "ad_id": "ad-1",
                    "campaign_id": "campaign-1",
                    "ad_set_id": "adset-1",
                    "ad_name": "Customer proof video",
                    "status": "active",
                    "customer_email": "person@example.com",
                }
            ],
        )

        result = validate_bundle(bundle)

        self.assertFalse(result["valid"])
        self.assertTrue(any("customer_email" in error for error in result["errors"]))

    def test_creative_ad_id_must_exist_in_ads(self):
        bundle = self.make_bundle()
        write_csv(
            bundle / "creatives.csv",
            CREATIVE_HEADERS,
            [
                {
                    "creative_id": "creative-2",
                    "ad_id": "ad-missing",
                    "asset_type": "image",
                    "concept_id": "concept-2",
                }
            ],
        )

        result = validate_bundle(bundle)

        self.assertFalse(result["valid"])
        self.assertTrue(any("ad-missing" in error and "ads.csv" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
