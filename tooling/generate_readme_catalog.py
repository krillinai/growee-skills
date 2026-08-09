#!/usr/bin/env python3
"""Generate bilingual README catalog sections from catalog JSON files."""

from __future__ import annotations

import argparse
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


def extension_section(
    bundle: dict, skills_by_id: dict[str, dict], language: str
) -> str:
    if language == "en":
        lines = [
            "## Related Skills",
            "",
            "Add a related Skill only when the content marketing job requires it.",
            "",
            "| When you need to... | Add |",
            "| --- | --- |",
        ]
    else:
        lines = [
            "## 相关 Skill",
            "",
            "仅在内容营销任务需要时添加相关 Skill。",
            "",
            "| 当你需要…… | 添加 |",
            "| --- | --- |",
        ]

    for extension in bundle["extensions"]:
        skill = skills_by_id[extension["skill_id"]]
        lines.append(
            f"| {extension[f'job_{language}']} | {skill_link(skill, language)} |"
        )
    return "\n".join(lines)


def bundle_section(bundles: dict, language: str) -> str:
    bundle = bundles["bundles"][0]
    capability_count = len(bundle["skills"]) + len(bundle.get("integrations", []))
    if language == "en":
        lines = [
            "## Core Package",
            "",
            f"`{bundle['id']}` combines {capability_count} core capabilities. "
            f"{bundle['description_en']}",
        ]
    else:
        lines = [
            "## 核心组合",
            "",
            f"`{bundle['id']}` 包含 {capability_count} 个核心能力。"
            f"{bundle['description_zh']}",
        ]
    return "\n".join(lines)


def generated_block(
    catalog: dict,
    bundles: dict,
    language: str,
) -> str:
    skills_by_id = {skill["id"]: skill for skill in catalog["skills"]}
    bundle = bundles["bundles"][0]
    sections = [
        bundle_section(bundles, language),
        extension_section(bundle, skills_by_id, language),
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

    raise ValueError(f"{language} README is missing generated catalog markers")


def render(path: Path, language: str) -> str:
    catalog = load_json("skills.json")
    bundles = load_json("bundles.json")
    block = generated_block(catalog, bundles, language)
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
