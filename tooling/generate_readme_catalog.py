#!/usr/bin/env python3
"""Generate bilingual README catalog sections from catalog JSON files."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "catalog"


def load_json(name: str) -> dict:
    with (CATALOG_DIR / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def skill_link(skill: dict, language: str) -> str:
    label = skill[f"name_{language}"]
    return f"[`{label}`]({skill['path']})"


def table_name(value: str) -> str:
    return html.escape(value).replace(" ", "&nbsp;")


def chooser_section(
    taxonomy: dict, skills_by_id: dict[str, dict], language: str
) -> str:
    if language == "en":
        lines = [
            "## Explore professional extensions",
            "",
            "| When you need to... | Start with |",
            "| --- | --- |",
        ]
    else:
        lines = [
            "## 按专业任务查找扩展",
            "",
            "| 当你需要…… | 建议从这里开始 |",
            "| --- | --- |",
        ]

    for category in taxonomy["categories"]:
        job = category[f"job_{language}"]
        links = ", ".join(
            skill_link(skills_by_id[skill_id], language)
            for skill_id in category["start_skills"]
        )
        lines.append(f"| {job} | {links} |")
    return "\n".join(lines)


def bundle_section(bundles: dict, language: str) -> str:
    if language == "en":
        lines = [
            "## Recommended bundles",
            "",
            "Start with Content Growth. Select a specialist bundle only when the job requires it.",
            "",
            "| Bundle | Description | Capabilities |",
            "| --- | --- | ---: |",
        ]
    else:
        lines = [
            "## 推荐组合",
            "",
            "建议从内容增长开始，仅在任务需要时安装专业组合。",
            "",
            "| 组合 | 说明 | 能力数量 |",
            "| --- | --- | ---: |",
        ]

    for bundle in bundles["bundles"]:
        capability_count = len(bundle["skills"]) + len(bundle.get("integrations", []))
        lines.append(
            f"| `{bundle['id']}` · {bundle[f'name_{language}']} | "
            f"{bundle[f'description_{language}']} | {capability_count} |"
        )
    return "\n".join(lines)


def catalog_section(
    taxonomy: dict,
    skills_by_id: dict[str, dict],
    integrations: dict,
    language: str,
) -> str:
    title = "## Complete Skill Catalog" if language == "en" else "## 完整技能目录"
    status_heading = "Status" if language == "en" else "状态"
    skill_heading = "Skill" if language == "en" else "技能"
    description_heading = "Description" if language == "en" else "说明"
    status_labels = {
        "experimental": "Preview" if language == "en" else "预览版",
        "beta": "Validated" if language == "en" else "已验证",
        "stable": "Stable" if language == "en" else "稳定版",
        "deprecated": "Deprecated" if language == "en" else "已弃用",
    }
    integration_status = "Integration" if language == "en" else "集成"
    if language == "en":
        maturity_note = (
            "**Maturity:** Preview Skills need real-world validation; Validated Skills "
            "have passed realistic forward tests; Stable Skills have demonstrated "
            "repeatable use."
        )
    else:
        maturity_note = (
            "**成熟度：** 预览版仍需真实任务验证；已验证版本已通过具有代表性的前向测试；"
            "稳定版已经过重复使用验证。"
        )
    summary = (
        "Browse every Skill and integration"
        if language == "en"
        else "展开查看全部 Skill 与集成"
    )
    lines = [title, "", "<details>", f"<summary>{summary}</summary>", "", maturity_note, ""]

    for category in taxonomy["categories"]:
        category_integrations = [
            integration
            for integration in integrations["integrations"]
            if integration["category"] == category["id"]
        ]
        lines.extend(
            [
                f"### {category[f'name_{language}']}",
                "",
                "<table>",
                "  <thead>",
                f'    <tr><th width="32%">{skill_heading}</th><th width="12%">{status_heading}</th><th>{description_heading}</th></tr>',
                "  </thead>",
                "  <tbody>",
            ]
        )
        for integration in category_integrations:
            if integration["position"] != "first":
                continue
            name = table_name(integration[f"name_{language}"])
            description = html.escape(integration[f"description_{language}"])
            lines.append(
                f'    <tr><td><a href="{integration["url"]}">{name}</a></td>'
                f"<td>{integration_status}</td><td>{description}</td></tr>"
            )
        for skill_id in category["skills"]:
            skill = skills_by_id[skill_id]
            name = table_name(skill[f"name_{language}"])
            description = html.escape(skill[f"description_{language}"])
            status = status_labels.get(skill["status"], html.escape(skill["status"]))
            lines.append(
                f'    <tr><td><a href="{skill["path"]}">{name}</a></td>'
                f"<td>{status}</td><td>{description}</td></tr>"
            )
        for integration in category_integrations:
            if integration["position"] != "last":
                continue
            name = table_name(integration[f"name_{language}"])
            description = html.escape(integration[f"description_{language}"])
            lines.append(
                f'    <tr><td><a href="{integration["url"]}">{name}</a></td>'
                f"<td>{integration_status}</td><td>{description}</td></tr>"
            )
        lines.extend(["  </tbody>", "</table>", ""])
    lines.append("</details>")
    return "\n".join(lines).rstrip()


def generated_block(
    taxonomy: dict,
    catalog: dict,
    bundles: dict,
    integrations: dict,
    language: str,
) -> str:
    skills_by_id = {skill["id"]: skill for skill in catalog["skills"]}
    sections = [
        bundle_section(bundles, language),
        chooser_section(taxonomy, skills_by_id, language),
        catalog_section(taxonomy, skills_by_id, integrations, language),
    ]
    return (
        "<!-- BEGIN GENERATED: catalog -->\n"
        + "\n\n".join(sections)
        + "\n<!-- END GENERATED: catalog -->"
    )


def replace_block(text: str, block: str, language: str) -> str:
    begin = "<!-- BEGIN GENERATED: catalog -->"
    end = "<!-- END GENERATED: catalog -->"
    if begin in text and end in text:
        before, remainder = text.split(begin, 1)
        _, after = remainder.split(end, 1)
        return before.rstrip() + "\n\n" + block + "\n\n" + after.lstrip("\n")

    start_heading = "## How to choose" if language == "en" else "## 如何选择"
    end_heading = "## The Growth Lifecycle" if language == "en" else "## 增长全生命周期"
    start = text.index(start_heading)
    finish = text.index(end_heading)
    return text[:start].rstrip() + "\n\n" + block + "\n\n" + text[finish:]


def render(path: Path, language: str) -> str:
    taxonomy = load_json("taxonomy.json")
    catalog = load_json("skills.json")
    bundles = load_json("bundles.json")
    integrations = load_json("integrations.json")
    block = generated_block(taxonomy, catalog, bundles, integrations, language)
    return replace_block(path.read_text(encoding="utf-8"), block, language)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="Fail when generated README content is stale"
    )
    args = parser.parse_args()

    targets = [(ROOT / "README.md", "en"), (ROOT / "README.zh-CN.md", "zh")]
    stale = []
    for path, language in targets:
        expected = render(path, language)
        current = path.read_text(encoding="utf-8")
        if current != expected:
            stale.append(path.name)
            if not args.check:
                path.write_text(expected, encoding="utf-8")

    if stale and args.check:
        print("Stale generated README content: " + ", ".join(stale))
        return 1
    if stale:
        print("Updated generated README content: " + ", ".join(stale))
    else:
        print("Generated README content is current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
