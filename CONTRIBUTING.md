# Contributing

Content Marketing Skills accepts focused Agent Skills that solve a clear content marketing job with an executable workflow, explicit evidence boundaries, inspectable outputs, and realistic evaluation cases. Existing specialist Skills outside the public content marketing set remain available for maintenance, but they are not the default path for new additions.

## Repository Structure

Keep Skill directories flat and independently installable:

```text
skills/<skill-name>/
├── SKILL.md
├── agents/openai.yaml
├── evals/evals.json
└── references/
```

Add `scripts/` only for deterministic or repeatedly implemented operations. Add `assets/` only when the Skill directly uses those files in its output. Do not add a README, changelog, installation guide, or other process documentation inside a Skill directory.

## Skill Requirements

- Use a short lowercase hyphenated name that describes the recognizable job.
- Keep YAML frontmatter to `name` and `description` only.
- Make the trigger description specific enough to distinguish adjacent Skills.
- State the primary modes, required inputs, evidence states, outputs, external-action boundary, and completion gate.
- Keep one output language across headings, prose, tables, labels, and actions. Match the requested language, translate ordinary jargon in Simplified Chinese deliverables, and separate explicitly requested multilingual versions instead of mixing languages within sentences or tables.
- Treat missing private evidence as `unavailable`; do not invent it or penalize its absence.
- Use `China` or `中国` consistently for the market name.
- Keep market, language, locale, platform, account, permissions, data, and current rules separate.
- Pin attributable Growth Playbook sources when the Skill derives material methods from the Playbook.
- Add pressure cases that test missing evidence, incompatible data, market transfer, false precision, authority boundaries, and prohibited external actions.

## Catalog And Status

Every Skill must appear exactly once in `catalog/taxonomy.json` and once in `catalog/skills.json`. Catalog status values use internal identifiers while the README presents user-facing maturity labels:

- `experimental` displays as **Preview / 预览版**. The Skill is structurally complete and has evaluation cases, but still needs representative real-world validation.
- `beta` displays as **Validated / 已验证**. The Skill has passed realistic forward tests, including relevant language, market, missing-evidence, and boundary cases, and its outputs have been reviewed.
- `stable` displays as **Stable / 稳定版**. The Skill has demonstrated repeatable use across multiple representative tasks, with documented dependencies, stable output contracts, regression coverage, and no known critical issue.
- `deprecated` displays as **Deprecated / 已弃用**. The Skill is no longer recommended and should identify its replacement or migration path.

New Skills start as `experimental`. Set `validation.forward_tested` to `true` only after recording and reviewing realistic runs. The validator rejects `beta` and `stable` status unless structure, evaluation specification, and forward testing are all complete. Promotion to `stable` additionally requires maintainer review of the qualitative criteria above.

Update English and Simplified Chinese catalog names and descriptions in `catalog/skills.json`. Do not edit generated README tables directly.

## Validation

Run:

```bash
python3 tooling/generate_readme_catalog.py
python3 tooling/validate_repo.py
```

The validator checks Skill structure, Agent metadata, local references, eval shape and global IDs, catalog coverage, taxonomy, bundles, Playbook revision records, generated README freshness, China terminology, and executable validator tests.

## Pull Requests

Keep one Skill or one collection-level structural change per pull request where practical. Explain the user job, boundary with adjacent Skills, reusable resources, evaluation coverage, Playbook basis, and validation performed.
