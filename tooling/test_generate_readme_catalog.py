import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "generate_readme_catalog", ROOT / "tooling" / "generate_readme_catalog.py"
)
GENERATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(GENERATOR)


class GeneratedCatalogTest(unittest.TestCase):
    def render(self, language: str) -> str:
        return GENERATOR.generated_block(
            GENERATOR.load_json("skills.json"),
            GENERATOR.load_json("bundles.json"),
            language,
        )

    def test_content_marketing_bundle_counts_skills_and_integrations(self):
        cases = (
            ("en", "`content-marketing` combines 8 core capabilities."),
            ("zh", "`content-marketing` 包含 8 个核心能力。"),
        )

        for language, expected in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                self.assertIn(expected, rendered)

    def test_related_skills_are_curated(self):
        expected_ids = (
            "customer-research",
            "competitive-intelligence",
            "positioning",
            "copy-editing",
            "ad-creative",
            "customer-proof-development",
            "seo-audit",
        )

        for language in ("en", "zh"):
            with self.subTest(language=language):
                rendered = self.render(language)
                for skill_id in expected_ids:
                    self.assertIn(f"skills/{skill_id}/", rendered)
                extension_rows = [
                    line
                    for line in rendered.splitlines()
                    if line.startswith("| ") and "skills/" in line
                ]
                self.assertEqual(len(extension_rows), len(expected_ids))

    def test_public_catalog_excludes_growth_and_full_collection(self):
        for language in ("en", "zh"):
            with self.subTest(language=language):
                rendered = self.render(language)
                self.assertNotIn("Growth", rendered)
                self.assertNotIn("增长", rendered)
                self.assertNotIn("Complete Skill Catalog", rendered)
                self.assertNotIn("完整技能目录", rendered)
                self.assertNotIn("growth-operating-system", rendered)


if __name__ == "__main__":
    unittest.main()
