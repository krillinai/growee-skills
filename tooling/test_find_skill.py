#!/usr/bin/env python3

import unittest

from find_skill import find


class FindSkillTests(unittest.TestCase):
    def test_exact_english_task(self):
        self.assertEqual(find("why are users churning")[0]["primary_skill"], "retention")

    def test_exact_chinese_task(self):
        self.assertEqual(find("提升激活")[0]["primary_skill"], "activation")

    def test_tool_name_alias(self):
        matches = find("analyze GA4 or PostHog")
        self.assertEqual(matches[0]["primary_skill"], "growth-measurement")
        self.assertEqual(len(matches), 1)

    def test_partial_query(self):
        self.assertEqual(find("Google Ads")[0]["primary_skill"], "paid-media-audit")

    def test_unknown_task(self):
        self.assertEqual(find("quantum lattice compiler")[0:1], [])


if __name__ == "__main__":
    unittest.main()
