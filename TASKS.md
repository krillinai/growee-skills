# Find Growee Skills By Task

Describe the job you need to complete instead of browsing dozens of narrow capability names. The task alias catalog maps common English and Chinese requests to the existing 27 top-level Skills; it does not create additional installable Skills.

```bash
python3 tooling/find_skill.py "why are users churning"
python3 tooling/find_skill.py "为什么增长变慢"
python3 tooling/find_skill.py "analyze GA4 or PostHog" --json
```

The machine-readable directory is [`catalog/task-aliases.json`](catalog/task-aliases.json). Search results identify one primary Skill and a small set of related Skills. Start with the primary Skill; use related Skills only when the task crosses a real decision boundary.

## Common Starting Points

| User task | Primary Skill |
| --- | --- |
| Diagnose why growth is slowing | [`growth-diagnosis`](skills/growth-diagnosis/) |
| Choose acquisition channels or plan a campaign | [`acquisition-strategy`](skills/acquisition-strategy/) |
| Audit Google Ads or Meta Ads | [`paid-media-audit`](skills/paid-media-audit/) |
| Improve SEO or analyze Search Console | [`seo-audit`](skills/seo-audit/) |
| Improve onboarding and first value | [`activation`](skills/activation/) |
| Understand churn and retention cohorts | [`retention`](skills/retention/) |
| Improve pricing, LTV, or unit economics | [`monetization`](skills/monetization/) |
| Build a content and creative system | [`content-strategy`](skills/content-strategy/) |
| Define ICP and positioning | [`positioning`](skills/positioning/) |
| Analyze GA4, PostHog, attribution, or experiments | [`growth-measurement`](skills/growth-measurement/) |
| Prioritize initiatives and operate growth | [`growth-operations`](skills/growth-operations/) |

## 中文常见入口

| 用户任务 | 首选 Skill |
| --- | --- |
| 诊断增长为什么变慢 | [`growth-diagnosis`](skills/growth-diagnosis/) |
| 选择获客渠道或规划营销活动 | [`acquisition-strategy`](skills/acquisition-strategy/) |
| 诊断 Google Ads 或 Meta Ads | [`paid-media-audit`](skills/paid-media-audit/) |
| 提升 SEO 或分析 Search Console | [`seo-audit`](skills/seo-audit/) |
| 改进新手引导和首次价值 | [`activation`](skills/activation/) |
| 理解流失和留存同期群 | [`retention`](skills/retention/) |
| 改进定价、LTV 或单位经济 | [`monetization`](skills/monetization/) |
| 构建内容与创意体系 | [`content-strategy`](skills/content-strategy/) |
| 定义 ICP 与市场定位 | [`positioning`](skills/positioning/) |
| 分析 GA4、PostHog、归因或实验 | [`growth-measurement`](skills/growth-measurement/) |
| 确定增长项目优先级并运行增长体系 | [`growth-operations`](skills/growth-operations/) |
