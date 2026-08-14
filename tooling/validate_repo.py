#!/usr/bin/env python3
"""Validate the complete Growee collection with standard-library tools."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG_DIR = ROOT / "catalog"
ALLOWED_STATUSES = {"experimental", "beta", "stable", "deprecated"}
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_LINK_RE = re.compile(r"\]\(([^)]+)\)")
BANNED_TERMS_RE = re.compile(r"mainland china|中国大陆", re.IGNORECASE)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def load_json(path: Path, report: Report) -> dict | None:
    try:
        with path.open(encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        report.error(f"{path.relative_to(ROOT)}: top-level JSON value must be an object")
        return None
    return value


def validate_catalog_maturity(
    skill_id: str, status: str, validation: dict, report: Report
) -> None:
    if status in {"beta", "stable"} and not all(
        validation.get(field) is True
        for field in ("structure", "eval_spec", "forward_tested")
    ):
        report.error(
            f"{skill_id}: {status} status requires structure, eval_spec, and "
            "forward_tested validation"
        )


def parse_frontmatter(path: Path, report: Report) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        report.error(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        report.error(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            report.error(f"{path.relative_to(ROOT)}: unsupported frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    if set(values) != {"name", "description"}:
        report.error(
            f"{path.relative_to(ROOT)}: frontmatter must contain only name and description"
        )
    return values


def validate_agent_metadata(skill_dir: Path, skill_id: str, report: Report) -> None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.is_file():
        report.error(f"{skill_id}: missing agents/openai.yaml")
        return
    text = path.read_text(encoding="utf-8")

    def field(name: str) -> str | None:
        match = re.search(rf'^\s+{re.escape(name)}:\s+"([^"]*)"\s*$', text, re.MULTILINE)
        return match.group(1) if match else None

    display_name = field("display_name")
    short_description = field("short_description")
    default_prompt = field("default_prompt")
    if not display_name:
        report.error(f"{skill_id}: missing interface.display_name")
    if short_description is None or not 25 <= len(short_description) <= 64:
        report.error(f"{skill_id}: short_description must contain 25-64 characters")
    if default_prompt is None or f"${skill_id}" not in default_prompt:
        report.error(f"{skill_id}: default_prompt must mention ${skill_id}")


def validate_local_links(skill_dir: Path, text: str, report: Report) -> None:
    for target in LOCAL_LINK_RE.findall(text):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (skill_dir / target).exists():
            report.error(f"{skill_dir.name}: broken local reference: {target}")


def validate_output_language_contract(
    skill_dir: Path, text: str, report: Report
) -> None:
    heading = "## Keep One Output Language"
    if text.count(heading) != 1:
        report.error(
            f"{skill_dir.name}: must contain exactly one '{heading}' section"
        )
        return

    section = text.split(heading, 1)[1]
    next_heading = re.search(r"^## ", section, re.MULTILINE)
    if next_heading:
        section = section[: next_heading.start()]
    for required in ("Simplified Chinese", "English", "multiple languages"):
        if required not in section:
            report.error(
                f"{skill_dir.name}: output language contract must mention {required}"
            )


def validate_eval_file(
    skill_dir: Path, global_ids: dict[int, str], report: Report
) -> int:
    path = skill_dir / "evals" / "evals.json"
    if not path.is_file():
        report.error(f"{skill_dir.name}: missing evals/evals.json")
        return 0
    data = load_json(path, report)
    if data is None:
        return 0
    if set(data) != {"skill_name", "evals"}:
        report.error(f"{skill_dir.name}: eval file must contain skill_name and evals only")
    if data.get("skill_name") != skill_dir.name:
        report.error(f"{skill_dir.name}: eval skill_name does not match directory")
    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        report.error(f"{skill_dir.name}: evals must be a non-empty array")
        return 0

    allowed_keys = {"id", "prompt", "expected_output", "assertions", "files"}
    required_keys = {"id", "prompt", "expected_output", "assertions"}
    seen_assertions: set[str] = set()
    for index, case in enumerate(evals):
        label = f"{skill_dir.name}: eval[{index}]"
        if not isinstance(case, dict):
            report.error(f"{label} must be an object")
            continue
        keys = set(case)
        if not required_keys <= keys or not keys <= allowed_keys:
            report.error(f"{label} has invalid keys")
        eval_id = case.get("id")
        if not isinstance(eval_id, int) or isinstance(eval_id, bool) or eval_id < 1:
            report.error(f"{label} id must be a positive integer")
        elif eval_id in global_ids:
            report.error(
                f"duplicate eval id {eval_id}: {global_ids[eval_id]} and {skill_dir.name}"
            )
        else:
            global_ids[eval_id] = skill_dir.name
        for key in ("prompt", "expected_output"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                report.error(f"{label} {key} must be a non-empty string")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or not assertions:
            report.error(f"{label} assertions must be a non-empty array")
        else:
            if len(assertions) != len(set(assertions)):
                report.error(f"{label} contains duplicate assertions")
            for assertion in assertions:
                if not isinstance(assertion, str) or not assertion.strip():
                    report.error(f"{label} assertions must be non-empty strings")
                elif assertion in seen_assertions:
                    report.error(f"{skill_dir.name}: duplicate assertion across eval cases")
                else:
                    seen_assertions.add(assertion)
        if "files" in case and not isinstance(case["files"], list):
            report.error(f"{label} files must be an array when present")
    return len(evals)


def extract_playbook_revisions(skill_id: str) -> list[str]:
    path = SKILLS_DIR / skill_id / "references" / "playbook-sources.md"
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    full = sorted(set(re.findall(r"\b[0-9a-f]{40}\b", text)))
    if full:
        return full
    return sorted(
        set(
            re.findall(
                r"(?:Growth Playbook )?(?:commit|revision)[^0-9a-f]+([0-9a-f]{7,39})",
                text,
                flags=re.IGNORECASE,
            )
        )
    )


def validate_catalog(skill_ids: set[str], report: Report) -> None:
    catalog = load_json(CATALOG_DIR / "skills.json", report)
    taxonomy = load_json(CATALOG_DIR / "taxonomy.json", report)
    bundles = load_json(CATALOG_DIR / "bundles.json", report)
    integrations = load_json(CATALOG_DIR / "integrations.json", report)
    if None in (catalog, taxonomy, bundles, integrations):
        return

    entries = catalog.get("skills")
    if catalog.get("schema_version") != "1.0" or not isinstance(entries, list):
        report.error("catalog/skills.json: invalid schema_version or skills array")
        return
    if catalog.get("default_status") not in ALLOWED_STATUSES:
        report.error("catalog/skills.json: invalid default_status")
    catalog_ids: list[str] = []
    category_by_skill: dict[str, str] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            report.error("catalog/skills.json: every skill entry must be an object")
            continue
        skill_id = entry.get("id")
        if not isinstance(skill_id, str) or not SKILL_NAME_RE.fullmatch(skill_id):
            report.error("catalog/skills.json: invalid skill id")
            continue
        catalog_ids.append(skill_id)
        if entry.get("path") != f"skills/{skill_id}/":
            report.error(f"{skill_id}: catalog path must match the skill directory")
        if entry.get("status") not in ALLOWED_STATUSES:
            report.error(f"{skill_id}: invalid catalog status")
        for key in ("name_en", "name_zh", "description_en", "description_zh"):
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                report.error(f"{skill_id}: catalog {key} must be a non-empty string")
        revisions = entry.get("playbook_revisions")
        if revisions != extract_playbook_revisions(skill_id):
            report.error(f"{skill_id}: catalog Playbook revisions are stale")
        category = entry.get("category")
        if isinstance(category, str):
            category_by_skill[skill_id] = category
        validation = entry.get("validation")
        if not isinstance(validation, dict) or set(validation) != {
            "structure",
            "eval_spec",
            "forward_tested",
        }:
            report.error(f"{skill_id}: invalid catalog validation state")
        elif (
            not isinstance(validation["structure"], bool)
            or not isinstance(validation["eval_spec"], bool)
            or (
                validation["forward_tested"] is not None
                and not isinstance(validation["forward_tested"], bool)
            )
        ):
            report.error(f"{skill_id}: catalog validation values have invalid types")
        else:
            validate_catalog_maturity(skill_id, entry.get("status"), validation, report)

    if len(catalog_ids) != len(set(catalog_ids)):
        report.error("catalog/skills.json: duplicate skill ids")
    if set(catalog_ids) != skill_ids:
        report.error("catalog/skills.json: catalog and skill directories differ")

    categories = taxonomy.get("categories")
    if taxonomy.get("schema_version") != "1.0" or not isinstance(categories, list):
        report.error("catalog/taxonomy.json: invalid schema_version or categories")
        return
    taxonomy_ids: list[str] = []
    category_ids: set[str] = set()
    for category in categories:
        if not isinstance(category, dict):
            report.error("catalog/taxonomy.json: category must be an object")
            continue
        category_id = category.get("id")
        if (
            not isinstance(category_id, str)
            or not SKILL_NAME_RE.fullmatch(category_id)
            or category_id in category_ids
        ):
            report.error("catalog/taxonomy.json: invalid or duplicate category id")
            continue
        category_ids.add(category_id)
        for key in ("name_en", "name_zh", "job_en", "job_zh"):
            if not isinstance(category.get(key), str) or not category[key].strip():
                report.error(f"{category_id}: taxonomy {key} must be a non-empty string")
        members = category.get("skills")
        starts = category.get("start_skills")
        if (
            not isinstance(members, list)
            or not members
            or not all(isinstance(item, str) for item in members)
        ):
            report.error(f"{category_id}: taxonomy skills must be a non-empty array")
            continue
        if (
            not isinstance(starts, list)
            or not starts
            or not all(isinstance(item, str) for item in starts)
            or not set(starts) <= set(members)
        ):
            report.error(f"{category_id}: invalid start_skills")
        taxonomy_ids.extend(members)
        for skill_id in members:
            if category_by_skill.get(skill_id) != category_id:
                report.error(f"{skill_id}: catalog and taxonomy categories differ")
    if len(taxonomy_ids) != len(set(taxonomy_ids)) or set(taxonomy_ids) != skill_ids:
        report.error("catalog/taxonomy.json: every skill must appear exactly once")

    bundle_rows = bundles.get("bundles")
    bundle_integration_refs: dict[str, list[str]] = {}
    if bundles.get("schema_version") != "1.0" or not isinstance(bundle_rows, list):
        report.error("catalog/bundles.json: invalid schema_version or bundles")
    else:
        bundle_ids: set[str] = set()
        for bundle in bundle_rows:
            bundle_id = bundle.get("id") if isinstance(bundle, dict) else None
            members = bundle.get("skills") if isinstance(bundle, dict) else None
            if (
                not isinstance(bundle_id, str)
                or not SKILL_NAME_RE.fullmatch(bundle_id)
                or bundle_id in bundle_ids
            ):
                report.error("catalog/bundles.json: invalid or duplicate bundle id")
                continue
            bundle_ids.add(bundle_id)
            for key in ("name_en", "name_zh", "description_en", "description_zh"):
                if not isinstance(bundle.get(key), str) or not bundle[key].strip():
                    report.error(f"{bundle_id}: bundle {key} must be a non-empty string")
            if (
                not isinstance(members, list)
                or not members
                or not all(isinstance(item, str) for item in members)
                or len(members) != len(set(members))
                or not set(members) <= skill_ids
            ):
                report.error(f"{bundle_id}: bundle contains unknown or missing skills")
            integration_refs = bundle.get("integrations", [])
            if (
                not isinstance(integration_refs, list)
                or not all(isinstance(item, str) for item in integration_refs)
                or len(integration_refs) != len(set(integration_refs))
            ):
                report.error(f"{bundle_id}: bundle contains invalid integrations")
            else:
                bundle_integration_refs[bundle_id] = integration_refs

    integration_rows = integrations.get("integrations")
    integration_ids: set[str] = set()
    if integrations.get("schema_version") != "1.0" or not isinstance(
        integration_rows, list
    ):
        report.error("catalog/integrations.json: invalid schema_version or integrations")
    else:
        for integration in integration_rows:
            if not isinstance(integration, dict):
                report.error("catalog/integrations.json: integration must be an object")
                continue
            integration_id = integration.get("id")
            if (
                not isinstance(integration_id, str)
                or not SKILL_NAME_RE.fullmatch(integration_id)
                or integration_id in integration_ids
            ):
                report.error("catalog/integrations.json: invalid or duplicate integration id")
                continue
            integration_ids.add(integration_id)
            for key in ("name_en", "name_zh", "description_en", "description_zh"):
                if not isinstance(integration.get(key), str) or not integration[key].strip():
                    report.error(
                        f"{integration_id}: integration {key} must be a non-empty string"
                    )
            if not str(integration.get("url", "")).startswith("https://"):
                report.error("catalog/integrations.json: integrations require HTTPS URLs")
            if integration.get("category") not in category_ids:
                report.error(
                    f"{integration_id}: integration category must match the taxonomy"
                )
            if integration.get("position") not in {"first", "last"}:
                report.error(
                    f"{integration_id}: integration position must be first or last"
                )
        for bundle_id, integration_refs in bundle_integration_refs.items():
            if not set(integration_refs) <= integration_ids:
                report.error(f"{bundle_id}: bundle contains unknown integrations")


def validate_banned_terms(report: Report) -> None:
    suffixes = {".md", ".json", ".yaml", ".yml", ".py"}
    roots = [ROOT / "README.md", ROOT / "README.zh-CN.md", SKILLS_DIR, CATALOG_DIR]
    paths: list[Path] = []
    for root in roots:
        if root.is_file():
            paths.append(root)
        else:
            paths.extend(path for path in root.rglob("*") if path.suffix in suffixes)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if BANNED_TERMS_RE.search(text):
            report.error(f"{path.relative_to(ROOT)}: use China / 中国, not Mainland China / 中国大陆")


def validate_generated_readmes(report: Report) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tooling" / "generate_readme_catalog.py"), "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        report.error(result.stdout.strip() or result.stderr.strip())


def run_script_tests(report: Report) -> None:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    tests = sorted((ROOT / "tooling").glob("test_*.py"))
    tests.extend(sorted(SKILLS_DIR.glob("*-ads-audit/scripts/test_validate_input_bundle.py")))
    for test in tests:
        result = subprocess.run(
            [sys.executable, str(test)],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            report.error(
                f"{test.relative_to(ROOT)} failed:\n{result.stdout}{result.stderr}"
            )


def main() -> int:
    report = Report()
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    skill_ids = {path.name for path in skill_dirs}
    global_eval_ids: dict[int, str] = {}
    eval_count = 0

    for skill_dir in skill_dirs:
        skill_id = skill_dir.name
        if not SKILL_NAME_RE.fullmatch(skill_id):
            report.error(f"{skill_id}: invalid skill directory name")
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.is_file():
            report.error(f"{skill_id}: missing SKILL.md")
            continue
        values = parse_frontmatter(skill_path, report)
        if values.get("name") != skill_id:
            report.error(f"{skill_id}: frontmatter name must match directory")
        description = values.get("description", "")
        if not description:
            report.error(f"{skill_id}: frontmatter description is required")
        if len(description.split()) > 70:
            report.warn(f"{skill_id}: trigger description exceeds 70 words")
        text = skill_path.read_text(encoding="utf-8")
        validate_local_links(skill_dir, text, report)
        validate_output_language_contract(skill_dir, text, report)
        validate_agent_metadata(skill_dir, skill_id, report)
        eval_count += validate_eval_file(skill_dir, global_eval_ids, report)

    validate_catalog(skill_ids, report)
    validate_banned_terms(report)
    validate_generated_readmes(report)
    run_script_tests(report)

    for path in ROOT.rglob("*"):
        if path.name in {".DS_Store", "__pycache__"} and ".git" not in path.parts:
            report.warn(f"local generated artifact present: {path.relative_to(ROOT)}")

    for warning in report.warnings:
        print(f"WARNING: {warning}")
    if report.errors:
        for error in report.errors:
            print(f"ERROR: {error}")
        print(
            f"Validation failed: {len(skill_dirs)} skills, {eval_count} evals, "
            f"{len(report.errors)} errors, {len(report.warnings)} warnings"
        )
        return 1
    print(
        f"Validation passed: {len(skill_dirs)} skills, {eval_count} evals, "
        f"{len(report.warnings)} warnings"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
