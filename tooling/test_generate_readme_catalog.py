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
            GENERATOR.load_json("integrations.json"),
            language,
        )

    def content_rows(self, text: str, heading: str) -> list[str]:
        section = text.split(heading, 1)[1].split("</table>", 1)[0]
        return [line for line in section.splitlines() if line.startswith("    <tr><td>")]

    def test_integrations_follow_the_playbook_categories(self):
        cases = (
            (
                "en",
                "### Content Production",
                "### Acquisition",
                "Video&nbsp;Translation&nbsp;&amp;&nbsp;Dubbing",
                "Social&nbsp;Media&nbsp;Publishing",
            ),
            (
                "zh",
                "### 内容生产",
                "### 获客",
                "视频翻译与配音",
                "社交媒体自动发布",
            ),
        )

        for language, content_heading, acquisition_heading, video, publishing in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                content_rows = self.content_rows(rendered, content_heading)
                acquisition_rows = self.content_rows(rendered, acquisition_heading)
                self.assertIn(video, content_rows[-1])
                self.assertIn(publishing, acquisition_rows[-1])
                self.assertNotIn(publishing, "\n".join(content_rows))
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

    def test_operating_scope_is_not_rendered(self):
        for language in ("en", "zh"):
            with self.subTest(language=language):
                rendered = self.render(language)
                self.assertNotIn("Choose your operating scope", rendered)
                self.assertNotIn("选择运营范围", rendered)
                self.assertNotIn("`content-growth`", rendered)

    def test_structure_note_reports_consolidated_surface(self):
        cases = (
            ("en", "27 top-level Skills", "59 specialist workflows"),
            ("zh", "27 个顶层 Skills", "59 个专业工作流"),
        )

        for language, skill_count, module_count in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                self.assertIn(skill_count, rendered)
                self.assertIn(module_count, rendered)

    def test_complete_catalog_is_expanded(self):
        cases = (
            (
                "en",
                "## Complete growth capability map",
                "### Growth Diagnosis",
            ),
            (
                "zh",
                "## 完整增长能力图谱",
                "### 增长诊断",
            ),
        )

        for language, heading, first_category in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                catalog = rendered.split(heading, 1)[1]
                self.assertIn(first_category, catalog)
                self.assertNotIn("<details>", catalog)
                self.assertNotIn("<summary>", catalog)
                self.assertNotIn("</details>", catalog)

    def test_sections_follow_the_growth_sequence(self):
        cases = (
            (
                "en",
                "## Follow the Growth Playbook",
                "## Complete growth capability map",
                (
                    "### Growth Diagnosis",
                    "### Acquisition",
                    "### Activation",
                    "### Retention",
                    "### Monetization",
                    "### Referral & Expansion",
                    "### Content Production",
                    "### Growth Foundations",
                ),
            ),
            (
                "zh",
                "## 按增长手册主线选择能力",
                "## 完整增长能力图谱",
                (
                    "### 增长诊断",
                    "### 获客",
                    "### 激活",
                    "### 留存",
                    "### 变现",
                    "### 推荐与扩张",
                    "### 内容生产",
                    "### 增长基础",
                ),
            ),
        )

        for language, chooser, catalog, headings in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                self.assertLess(rendered.index(chooser), rendered.index(catalog))
                positions = [rendered.index(heading) for heading in headings]
                self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
