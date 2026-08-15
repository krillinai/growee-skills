<p align="center">
  <img src="Growee-logo.png" alt="Growee Skills logo" width="180">
</p>

<h1 align="center">全生命周期AI增长技能合集</h1>

<p align="center">覆盖增长诊断、获客、激活、留存、变现、分享传播、内容生产与增长基础的 AI 可执行能力。</p>

Growee Skills 由 [KrillinAI](https://github.com/KrillinAI) 创作并维护，是 Growth Playbook（增长手册）的开源执行层。Growth Playbook 是一套完整的增长理论体系，涵盖框架、模型、方法与证据；Growee Skills 则把这套知识转化为可复用的 Agent Skills，用于边界明确的增长工作。

<p align="center">
  <a href="https://github.com/krillinai/growee-skills/stargazers"><img src="https://img.shields.io/github/stars/krillinai/growee-skills?style=flat-square&amp;logo=github&amp;label=Stars" alt="GitHub Stars"></a>
  <a href="https://clawee.ai"><img src="https://img.shields.io/badge/clawee.ai-Enterprise_Growth_Agent-6f42c1?style=flat-square" alt="clawee.ai"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT"></a>
</p>

<p align="center"><strong><a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a></strong></p>

## 从诊断到增长复利

Growee Skills 与 Growth Playbook 使用同一条主线。增长诊断先识别当前约束；生命周期 Skills 推动客户从发现产品走向首次价值、持续价值、收入和扩张；内容生产为这些工作提供信息与资产；增长基础明确客户、市场、价值与增长模型，并提供让每个阶段可验证、可重复的测量、实验、规划、基础设施与组织能力。

<pre align="center">
+--------------------------------------------------------------+
|                           增长诊断                           |
|                   约束 / 证据 / 30 天行动                    |
+--------------------------------------------------------------+
|
v
增长生命周期
+--------------------+  +--------------------+  +--------------------+  +--------------------+  +--------------------+
|        获客        |  |        激活        |  |        留存        |  |        变现        |  |      分享传播      |
| 渠道 / 搜索 / 广告 |  |   落地页 / 引导    |  |  同期群 / 参与度   |  | 定价 / 套餐 / LTV  |  | 推荐 / 分享 / 循环 |
|    合作 / 社区     |  |  摩擦 / 首次价值   |  |  生命周期 / 流失   |  | 回收期 / 单位经济  |  |  口碑 / 网络效应   |
+--------------------+  +--------------------+  +--------------------+  +--------------------+  +--------------------+
|
v
+--------------------------------------------------------------+
|                           内容生产                           |
|              策略 / 文案 / 创意 / 证明 / 本地化              |
+--------------------------------------------------------------+
|
v
+--------------------------------------------------------------+
|                           增长基础                           |
|       PMF / ICP / 定位 / 客户旅程 / 战略 / 增长模型          |
|                 指标 / 实验 / 数据 / 归因 / 预测              |
|                 规划 / 基础设施 / 组织 / 收入运营               |
+--------------------------------------------------------------+
|
v
洞察回流到下一轮增长诊断
</pre>

| 层级 | 核心问题 | Growee Skills 中的作用 |
| --- | --- | --- |
| 增长诊断 | 当前最主要的增长约束是什么？ | 把表面症状转化为边界明确的结果、证据台账、30 天行动与执行路径 |
| 获客 | 有效需求如何发现并到达产品？ | 设计和诊断渠道、营销活动、搜索、广告、合作、社区与外联 |
| 激活 | 新用户如何到达首次价值？ | 诊断入口路径、落地体验、摩擦、新手引导与下一项关键行动 |
| 留存 | 客户如何持续获得价值？ | 分析同期群、参与度、生命周期沟通、客户健康、流失与召回 |
| 变现 | 客户价值如何转化为可持续且有利润的收入？ | 设计定价与套餐，并对账 LTV、回收期与单位经济 |
| 推荐与扩张 | 客户和产品活动如何创造更深价值与新分发？ | 构建推荐、增长循环、扩张路径、激励、多边市场与网络效应 |
| 内容生产 | 应该生产哪些有证据支撑的信息和资产？ | 规划并生产文案、图片、视频、创意、客户证据、公共关系与本地化内容 |
| 增长基础 | 客户是谁、什么价值重要、增长应如何测量和运行？ | 建立 PMF、ICP、定位、客户旅程、战略、指标、实验、数据质量、归因、预测、规划、基础设施、组织、治理与收入运营体系 |

可衡量的客户行为和业务结果会回流到下一轮诊断。真正的进展单位是这条反馈闭环，而不是内容数量或孤立的营销活动。所有 Skill 都保留证据与操作边界：外部发布和账户修改仍由用户控制，权利、声明、同意、隐私与审批必须保持明确。

## 安装与使用

`skills/` 下的每个目录都是一个可独立安装的 Agent Skill。合集提供 27 个顶层 Skills，覆盖增长诊断、客户生命周期、内容生产与增长基础；另有 59 个专业工作流存放在 `references/modules/` 中，仅在所属 Skill 路由到它们时加载。先从增长诊断开始，再只安装与首要约束和执行路径匹配的顶层 Skill。

```bash
git clone https://github.com/krillinai/growee-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R growee-skills/skills/growth-diagnosis "${CODEX_HOME:-$HOME/.codex}/skills/"
```

当一个任务可能匹配多个能力时，建议显式调用：

```text
使用 $growth-diagnosis，识别当前最主要的增长约束，并定义下一项有证据支撑的决策。
```

明确约束后，将示例中的 `growth-diagnosis` 替换为对应 Skill 名称。对于其他兼容 Agent Skills 的客户端，将所选 `skills/<name>/` 目录复制或链接到对应的 Skill 目录即可。

<!-- BEGIN GENERATED: catalog -->
## 按增长手册主线选择能力

| 增长决策 | 建议从这里开始 |
| --- | --- |
| 识别首要增长约束，并选择最小且有证据支撑的执行路径 | [`增长诊断`](skills/growth-diagnosis/) |
| 通过渠道、营销活动、搜索、广告、合作与外联，把有效需求连接到产品 | [`获客策略与营销活动`](skills/acquisition-strategy/)、[`SEO 与搜索系统`](skills/seo-audit/) |
| 推动有效访客和新用户到达首次价值与下一项关键行动 | [`激活与转化`](skills/activation/) |
| 维持持续价值，理解同期群与流失，并修复有价值的客户关系 | [`留存与客户健康`](skills/retention/)、[`生命周期营销`](skills/lifecycle-marketing/) |
| 通过定价、套餐、LTV 与单位经济，把客户价值转化为可持续收入 | [`变现与单位经济`](skills/monetization/) |
| 通过推荐、增长循环、客户扩张、多边市场与网络效应创造更深价值和新分发 | [`增长循环与网络效应`](skills/growth-loop-design/)、[`客户扩张策略`](skills/customer-expansion-strategy/) |
| 把战略、客户证据与证明转化为受治理的内容和创意资产 | [`内容策略与创意`](skills/content-strategy/)、[`文案创作与编辑`](skills/copywriting/)、[`营销视频`](skills/marketing-video/) |
| 定义客户、市场、匹配、定位、增长模型、测量、实验与运营基础 | [`产品市场匹配与客户旅程`](skills/product-market-fit-assessment/)、[`ICP 与市场定位`](skills/positioning/)、[`增长测量与实验`](skills/growth-measurement/)、[`增长运营与基础设施`](skills/growth-operations/) |

## 选择运营范围

选择与当前约束匹配的最小组合。数量仅代表顶层 Skills 与集成入口；专业工作流保留在所属 Skill 内，仅在需要时加载。

| 范围 | 说明 | 入口数量 |
| --- | --- | ---: |
| `content-growth` · 内容增长 | 把客户问题、内容生产、本地化、分发与转化连接起来的内容营销路径。 | 8 |
| `measurement-analytics` · 测量与分析 | 通过指标、追踪、归因、经济性、预测、同期群与实验，让增长可观察、可用于决策。 | 4 |
| `acquisition-distribution` · 获客与分发 | 通过渠道、营销活动、搜索、转化界面、合作、社区与外联，把有效需求连接到产品价值。 | 8 |
| `growth-operating-system` · 增长运营体系 | 通过规划、承载能力、投入、治理、复盘、学习、基础设施、组织与收入运营，把增长决策变成可重复的运行节奏。 | 3 |

## 完整增长能力图谱

<details>
<summary>按增长职能展开查看全部 Skill 与集成</summary>

**结构：** 本图谱展示 27 个顶层 Skills；59 个专业工作流保留在 `references/modules/` 中，由所属 Skill 按需加载。

**成熟度：** 预览版仍需真实任务验证；已验证版本已通过具有代表性的前向测试；稳定版已经过重复使用验证。

### 增长诊断

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-diagnosis/">增长诊断</a></td><td>预览版</td><td>通过漏斗、异常与成熟度分析诊断首要约束，并制定有证据支撑的 30 天执行路径</td></tr>
  </tbody>
</table>

### 获客

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/acquisition-strategy/">获客策略与营销活动</a></td><td>预览版</td><td>围绕受众、产品方案、渠道、旅程、资产、经济性、测量与运营约束设计获客组合和边界明确的营销活动</td></tr>
    <tr><td><a href="skills/partnership-marketing/">合作伙伴与社区增长</a></td><td>预览版</td><td>围绕共同客户价值、角色、贡献、信任、运营、经济性与产品路径设计可问责的合作伙伴和社区体系</td></tr>
    <tr><td><a href="skills/sales-enablement/">销售赋能与外联</a></td><td>预览版</td><td>围绕购买情境、声明、证据、沟通序列、本地化与停止状态构建证据驱动的销售赋能和许可型 B2B 外联</td></tr>
    <tr><td><a href="skills/paid-media-audit/">付费媒体诊断</a></td><td>预览版</td><td>在不访问实时账户或执行外部更改的前提下，诊断用户提供的 Google、Meta、TikTok 与抖音广告证据</td></tr>
    <tr><td><a href="skills/seo-audit/">SEO&nbsp;与搜索系统</a></td><td>预览版</td><td>以有证据支撑的质量与发布控制诊断和设计 SEO、程序化页面、站点架构、结构化数据与目录展示</td></tr>
    <tr><td><a href="skills/aso-audit/">ASO（应用商店优化）诊断</a></td><td>预览版</td><td>基于可验证证据诊断 App Store 与 Google Play 的可见性、商店页面、素材及转化问题，并提供优化建议</td></tr>
    <tr><td><a href="skills/geo/">GEO（生成式引擎优化）诊断</a></td><td>预览版</td><td>基于证据评估网站面向 AI（人工智能）生成式搜索的准备度，并通过边界明确的查询面板独立观测品牌提及与引用表现</td></tr>
    <tr><td><a href="https://github.com/krillinai/autosocial-skills">社交媒体自动发布</a></td><td>集成</td><td>使用可复用的标题、描述、标签和元数据，将视频自动发布到小红书、抖音、快手和微信视频号。</td></tr>
  </tbody>
</table>

### 激活

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/activation/">激活与转化</a></td><td>预览版</td><td>定义首次价值，并围绕新手引导、落地页、弹窗、摩擦、无障碍、测量与实验改进激活</td></tr>
  </tbody>
</table>

### 留存

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/retention/">留存与客户健康</a></td><td>预览版</td><td>通过同期群、增长核算、参与度、重复价值、流失、复活与客户健康分析并改进留存</td></tr>
    <tr><td><a href="skills/lifecycle-marketing/">生命周期营销</a></td><td>预览版</td><td>在明确消息分类、渠道许可、抑制状态与外部操作边界的前提下，规划、撰写、审校和本地化覆盖欢迎、激活、事务服务、留存、召回与活动推广的邮件、短信、微信公众号、小程序订阅消息、企业微信和 WhatsApp 沟通</td></tr>
  </tbody>
</table>

### 变现

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/monetization/">变现与单位经济</a></td><td>预览版</td><td>围绕产品方案、定价、套餐、LTV、CAC、单位经济、回收期、迁移与客户保护设计并诊断变现</td></tr>
  </tbody>
</table>

### 推荐与扩张

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-loop-design/">增长循环与网络效应</a></td><td>预览版</td><td>围绕参与者价值、闭环、经济性、信任与治理设计并诊断推荐、激励、增长循环、多边市场与网络效应</td></tr>
    <tr><td><a href="skills/customer-expansion-strategy/">客户扩张策略</a></td><td>预览版</td><td>围绕活跃席位、使用深度、工作流、产品、团队、产品合格扩张信号、采用与商业结果对账、留存贡献和客户保护，审计、设计、排序、测量并治理既有客户关系内的价值扩张</td></tr>
  </tbody>
</table>

### 内容生产

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/content-strategy/">内容策略与创意</a></td><td>预览版</td><td>围绕问题、声明、格式、渠道、工作流、测量与治理，构建内容组合、已获授权的客户证据、广告创意与公共传播</td></tr>
    <tr><td><a href="skills/copywriting/">文案创作与编辑</a></td><td>预览版</td><td>为页面、营销活动、产品、优惠与本地化创作和编辑证据驱动的文案，同时保留事实含义并记录重要修改</td></tr>
    <tr><td><a href="skills/marketing-image/">营销图片</a></td><td>预览版</td><td>围绕概念谱系、产品准确性、文案、品牌、声明、素材权利、人物、平台格式、本地化、无障碍、文件 QA（质量保证）与下游学习，对真实可信的营销图片进行简报、创作、编辑、适配、诊断与治理</td></tr>
    <tr><td><a href="skills/marketing-video/">营销视频</a></td><td>预览版</td><td>围绕产品与声明准确性、源素材、人物、声音、音乐、权利、本地化、无障碍、渲染 QA（质量保证）与下游学习，对真实可信的营销视频进行简报、脚本、分镜、创作、适配、诊断与治理</td></tr>
    <tr><td><a href="https://github.com/krillinai/KrillinAI">视频翻译与配音</a></td><td>集成</td><td>完成视频转写、字幕翻译、AI 配音、声音克隆及横竖屏渲染，支持多语言内容本地化。</td></tr>
  </tbody>
</table>

### 增长基础

<table>
  <thead>
    <tr><th width="32%">技能</th><th width="12%">状态</th><th>说明</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/product-market-fit-assessment/">产品市场匹配与客户旅程</a></td><td>预览版</td><td>围绕问题、首次与重复价值、路径摩擦、服务依赖和证据边界评估产品市场匹配与客户旅程</td></tr>
    <tr><td><a href="skills/positioning/">ICP&nbsp;与市场定位</a></td><td>预览版</td><td>定义有证据支撑的 ICP、客户分群、定位、排除条件、品类选择、信息与验证计划</td></tr>
    <tr><td><a href="skills/growth-model-design/">增长模型与机会测算</a></td><td>预览版</td><td>围绕生命周期行为、经济性、触达、承载能力、重叠、情景与风险设计增长模型并测算机会</td></tr>
    <tr><td><a href="skills/customer-research/">客户研究与调查</a></td><td>预览版</td><td>规划并综合客户研究和决策型调查，明确抽样、证据、同意、不确定性与解释边界</td></tr>
    <tr><td><a href="skills/market-sizing/">市场情报与规模测算</a></td><td>预览版</td><td>使用可归因的竞争证据、兼容的市场单元、情景与不确定性研究替代方案并测算市场规模</td></tr>
    <tr><td><a href="skills/growth-strategy/">增长与市场策略</a></td><td>预览版</td><td>围绕客户、市场、机制、能力、排序、试点与停止规则制定证据边界清晰的增长和市场进入策略</td></tr>
    <tr><td><a href="skills/go-to-market-strategy/">市场进入与产品发布</a></td><td>预览版</td><td>围绕受众、产品方案、路径、准备度、曝光、价值、测量与扩量门槛设计并治理市场进入和产品发布</td></tr>
    <tr><td><a href="skills/growth-measurement/">增长测量与实验</a></td><td>预览版</td><td>把指标、目标、追踪、数据质量、归因、预测与因果实验作为一套证据驱动的增长测量系统进行设计和诊断</td></tr>
    <tr><td><a href="skills/growth-operations/">增长运营与基础设施</a></td><td>预览版</td><td>围绕资源配置、复盘、决策、学习、基础设施、组织、收入运营与实验项目规划并运营增长</td></tr>
  </tbody>
</table>

</details>
<!-- END GENERATED: catalog -->

## 增长原则

- 先诊断当前约束，再选择渠道、战术或工具。
- 把获客、激活、留存、变现、推荐与扩张作为同一个生命周期系统管理。
- 把内容生产视为执行层，并确保它连接到有效获客和客户价值。
- 用增长基础明确每项生命周期决策背后的客户、市场、匹配、定位、增长模型、测量、实验、基础设施与组织，并把证据带回下一轮诊断。

## 参与贡献

Growee Skills 遵循 Growth Playbook（增长手册）的结构与证据标准。只有在现有父级 Skill 无法承载一项明确、可复用的增长决策时，才新增顶层 Skill；其他情况应在最接近的父级 Skill 中新增或完善按需模块。贡献内容应定义其所属手册层级、证据输入、可执行工作流、可检查输出、测量路径和操作边界。

## 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。
