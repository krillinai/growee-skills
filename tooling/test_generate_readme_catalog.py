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

    def test_content_growth_bundle_counts_skills_and_integrations(self):
        cases = (
            (
                "en",
                "| `content-growth` · Content Growth |",
                "| 8 |",
            ),
            (
                "zh",
                "| `content-growth` · 内容增长 |",
                "| 8 |",
            ),
        )

        for language, row_start, row_end in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                row = next(
                    line for line in rendered.splitlines() if line.startswith(row_start)
                )
                self.assertTrue(row.endswith(row_end))
                self.assertNotIn("`core-growth`", rendered)

    def test_complete_catalog_is_collapsed(self):
        cases = (
            (
                "en",
                "## Complete growth capability map",
                "Browse every Skill and integration by growth function",
            ),
            (
                "zh",
                "## 完整增长能力图谱",
                "按增长职能展开查看全部 Skill 与集成",
            ),
        )

        for language, heading, summary in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                catalog = rendered.split(heading, 1)[1]
                self.assertIn("<details>", catalog)
                self.assertIn(f"<summary>{summary}</summary>", catalog)
                self.assertIn("</details>\n<!-- END GENERATED: catalog -->", catalog)

    def test_sections_follow_the_growth_sequence(self):
        cases = (
            (
                "en",
                "## Follow the Growth Playbook",
                "## Choose your operating scope",
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
                "## 选择运营范围",
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

        for language, chooser, scopes, headings in cases:
            with self.subTest(language=language):
                rendered = self.render(language)
                self.assertLess(rendered.index(chooser), rendered.index(scopes))
                positions = [rendered.index(heading) for heading in headings]
                self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
