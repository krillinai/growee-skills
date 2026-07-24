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
            GENERATOR.load_json("taxonomy.json"),
            GENERATOR.load_json("skills.json"),
            GENERATOR.load_json("bundles.json"),
            GENERATOR.load_json("integrations.json"),
            language,
        )

    def content_rows(self, text: str, heading: str) -> list[str]:
        section = text.split(heading, 1)[1].split("</table>", 1)[0]
        return [line for line in section.splitlines() if line.startswith("    <tr><td>")]

    def test_content_and_creative_places_integrations_at_the_edges(self):
        cases = (
            ("en", "### Content & Creative", "Video&nbsp;Translation&nbsp;&amp;&nbsp;Dubbing", "Social&nbsp;Media&nbsp;Publishing"),
            ("zh", "### 内容与创意", "视频翻译与配音", "社交媒体自动发布"),
        )

        for language, heading, first_name, last_name in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                rows = self.content_rows(rendered, heading)
                self.assertIn(first_name, rows[0])
                self.assertIn(last_name, rows[-1])
                self.assertNotIn("Companion integrations", rendered)
                self.assertNotIn("配套集成", rendered)

    def test_catalog_uses_skill_maturity_labels(self):
        cases = (
            ("en", "**Maturity:**", "<td>Preview</td>", "<td>Experimental</td>"),
            ("zh", "**成熟度：** ", "<td>预览版</td>", "<td>实验性</td>"),
        )

        for language, note, current_label, old_label in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                self.assertIn(note, rendered)
                self.assertIn(current_label, rendered)
                self.assertNotIn(old_label, rendered)


if __name__ == "__main__":
    unittest.main()
