# AI Content Marketing Skills

**Use AI to plan, create, localize, distribute, and convert content**

Created and maintained by the teams behind [clawee.ai](https://clawee.ai/) and [KrillinAI](https://github.com/KrillinAI).

[![GitHub Stars](https://img.shields.io/github/stars/krillinai/content-marketing-skills?style=flat-square&logo=github&label=Stars)](https://github.com/krillinai/content-marketing-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**[English](README.md) | [简体中文](README.zh-CN.md)**

For creators, founders, and small marketing teams turning one idea into content that can be localized, distributed across channels, and connected to conversion. Start with eight core capabilities and add a related Skill only when the job requires it.

## Content Marketing Workflow

| Stage | Core capabilities | Work completed |
| --- | --- | --- |
| Plan | [`Content Strategy`](skills/content-strategy/) | Turn customer questions, content pillars, and channel constraints into a content plan |
| Create | [`Copywriting`](skills/copywriting/), [`Marketing Image`](skills/marketing-image/), [`Marketing Video`](skills/marketing-video/) | Produce copy, covers, visuals, and video assets |
| Localize | [Video Translation & Dubbing](https://github.com/krillinai/KrillinAI) | Use KrillinAI for transcription, subtitle translation, AI dubbing, and landscape or portrait rendering |
| Distribute | [Social Media Publishing](https://github.com/krillinai/autosocial-skills), [`Campaign Planning`](skills/campaign-planning/) | Adapt titles, descriptions, tags, timing, and campaign cadence for each channel |
| Convert | [`Landing Page Audit`](skills/landing-page-audit/) | Check that the content promise, page proof, and next action remain coherent |

Only localize video you own or are authorized to use, and preserve review records for source rights, voices, claims, and publication permissions.

## Install and use

Each directory under `skills/` is a standalone Agent Skill. Start with Content Strategy and install only the capabilities needed for the current job.

```bash
git clone https://github.com/krillinai/content-marketing-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R content-marketing-skills/skills/content-strategy "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Invoke an installed Skill explicitly when the task could match several capabilities:

```text
Use $content-strategy to build a 30-day content plan around our target customers' questions.
```

For another Agent Skills-compatible client, copy or link the selected `skills/<name>/` directory into that client's Skill directory.

<!-- BEGIN GENERATED: catalog -->
## Core Package

`content-marketing` combines 8 core capabilities. Plan, create, localize, distribute, and convert content with one focused set of AI workflows.

## Related Skills

Add a related Skill only when the content marketing job requires it.

| When you need to... | Add |
| --- | --- |
| Ground topics in attributable customer questions | [`Customer Research`](skills/customer-research/) |
| Find content gaps across real alternatives | [`Competitive Intelligence`](skills/competitive-intelligence/) |
| Align content with a clear market position | [`Positioning`](skills/positioning/) |
| Improve existing copy without changing its factual meaning | [`Copy Editing`](skills/copy-editing/) |
| Adapt content into traceable advertising concepts | [`Ad Creative`](skills/ad-creative/) |
| Turn permissioned customer evidence into case content | [`Customer Proof Development`](skills/customer-proof-development/) |
| Diagnose content and technical search visibility | [`SEO Audit`](skills/seo-audit/) |
<!-- END GENERATED: catalog -->

## Improving the Collection

This repository is at an early stage. The current priority is validating and refining the eight core content marketing capabilities. Add a public Skill only when the existing set cannot cover a clear, reusable content marketing job.

## Contributing

Contributions are welcome. A useful Skill should address a clear content marketing job, provide an actionable workflow, and produce outcomes that can be evaluated.

## License

This project is released under the [MIT License](LICENSE).
