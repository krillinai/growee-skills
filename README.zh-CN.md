# AI 内容营销技能库

**用 AI 完成内容策划、创作、视频本地化、分发与转化优化**

由 [clawee.ai](https://clawee.ai/) 与 [KrillinAI](https://github.com/KrillinAI) 团队创作并维护。

[![GitHub Stars](https://img.shields.io/github/stars/krillinai/content-marketing-skills?style=flat-square&logo=github&label=Stars)](https://github.com/krillinai/content-marketing-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**[English](README.md) | [简体中文](README.zh-CN.md)**

面向创作者、创业者和小型营销团队，把一次选题变成可跨语言、跨平台分发并承接转化的内容资产。默认从 8 个核心能力开始，只在具体任务需要时添加相关 Skill。

## 内容营销流程

| 阶段 | 核心能力 | 完成的工作 |
| --- | --- | --- |
| 策划 | [`内容策略`](skills/content-strategy/) | 从客户问题、主题支柱和渠道约束形成内容计划 |
| 创作 | [`文案创作`](skills/copywriting/)、[`营销图片`](skills/marketing-image/)、[`营销视频`](skills/marketing-video/) | 产出文案、封面、视觉与视频素材 |
| 本地化 | [视频翻译与配音](https://github.com/krillinai/KrillinAI) | 使用 KrillinAI 完成转写、字幕翻译、AI 配音及横竖屏渲染 |
| 分发 | [社交媒体自动发布](https://github.com/krillinai/autosocial-skills)、[`营销活动规划`](skills/campaign-planning/) | 为渠道适配标题、描述、标签、发布时间和活动节奏 |
| 转化 | [`落地页诊断`](skills/landing-page-audit/) | 检查内容承诺、页面证据和下一步行动是否连贯 |

视频本地化应使用自有或已获授权的素材，并保留来源、声音、声明和发布权限的审查记录。

## 安装与使用

`skills/` 下的每个目录都是一个可独立安装的 Agent Skill。建议从内容策略开始，只安装当前任务需要的能力。

```bash
git clone https://github.com/krillinai/content-marketing-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R content-marketing-skills/skills/content-strategy "${CODEX_HOME:-$HOME/.codex}/skills/"
```

当一个任务可能匹配多个能力时，建议显式调用：

```text
使用 $content-strategy，围绕目标客户的问题制定接下来 30 天的内容计划。
```

对于其他兼容 Agent Skills 的客户端，将所选 `skills/<name>/` 目录复制或链接到对应的 Skill 目录即可。

<!-- BEGIN GENERATED: catalog -->
## 核心组合

`content-marketing` 包含 8 个核心能力。用一组聚焦的 AI 工作流完成内容策划、创作、本地化、分发与转化。

## 相关 Skill

仅在内容营销任务需要时添加相关 Skill。

| 当你需要…… | 添加 |
| --- | --- |
| 从可追溯的客户问题中寻找选题 | [`客户研究`](skills/customer-research/) |
| 从真实替代方案中发现内容空白 | [`竞争情报`](skills/competitive-intelligence/) |
| 让内容与清晰的市场定位保持一致 | [`市场定位`](skills/positioning/) |
| 在不改变事实含义的前提下完善现有文案 | [`文案编辑`](skills/copy-editing/) |
| 将内容适配为可追溯的广告创意 | [`广告创意`](skills/ad-creative/) |
| 将获得授权的客户证据转化为案例内容 | [`客户证据开发`](skills/customer-proof-development/) |
| 诊断内容与技术层面的搜索可见性 | [`SEO（搜索引擎优化）诊断`](skills/seo-audit/) |
<!-- END GENERATED: catalog -->

## 持续完善

本项目仍处于早期阶段。当前优先级是验证和完善 8 个核心内容营销能力；只有在现有能力无法覆盖一个明确、可复用的内容营销任务时，才新增公开 Skill。

## 参与贡献

欢迎参与贡献。一个有价值的 Skill 应当解决明确的内容营销任务，提供可执行的工作流，并产出可以评估的结果。

## 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。
