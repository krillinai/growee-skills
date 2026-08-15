<div align="center">
  <img src="Growee-logo-compact.png" alt="Growee Skills logo" width="320">
  <h1>Full-Lifecycle AI Growth Skills</h1>
</div>

<p align="center">AI-executable capabilities for growth diagnosis, acquisition, activation, retention, monetization, referral and expansion, content production, and growth foundations.</p>

Growee Skills, by [KrillinAI](https://github.com/KrillinAI), is the open-source execution companion to Growth Playbook, a complete body of growth theory spanning frameworks, models, methods, and evidence. Growee Skills turns that body of knowledge into reusable Agent Skills for bounded growth work.

<p align="center">
  <a href="https://github.com/krillinai/growee-skills/stargazers"><img src="https://img.shields.io/github/stars/krillinai/growee-skills?style=flat-square&amp;logo=github&amp;label=Stars" alt="GitHub Stars"></a>
  <a href="https://clawee.ai"><img src="https://img.shields.io/badge/clawee.ai-Enterprise_Growth_Agent-6f42c1?style=flat-square" alt="clawee.ai"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT"></a>
</p>

<p align="center"><strong><a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a></strong></p>

## From diagnosis to compounding growth

Growee Skills follows the same mainline as Growth Playbook. Diagnosis identifies the current constraint. Lifecycle Skills move customers from discovery to first value, repeated value, revenue, and expansion. Content production supplies the messages and assets for that work. Growth foundations clarify the customer, market, value, and growth model while providing the measurement, experimentation, planning, infrastructure, and organization that make every stage testable and repeatable.

<pre align="center">
+--------------------------------------------------------------+
|                       GROWTH DIAGNOSIS                       |
|            Constraint / Evidence / 30-Day Action             |
+--------------------------------------------------------------+
|
v
GROWTH LIFECYCLE
+--------------------+  +--------------------+  +--------------------+  +--------------------+  +--------------------+
|    ACQUISITION     |  |     ACTIVATION     |  |     RETENTION      |  |    MONETIZATION    |  | REFERRAL / SHARING |
| Channels / Search  |  | Landing / Onboard  |  |  Cohorts / Churn   |  | Pricing / Package  |  | Referrals / Loops  |
|  Paid / Partners   |  |  Friction / Value  |  | Lifecycle / Health |  |   LTV / Payback    |  |   Word of Mouth    |
+--------------------+  +--------------------+  +--------------------+  +--------------------+  +--------------------+
|
v
+--------------------------------------------------------------+
|                      CONTENT PRODUCTION                      |
|      Strategy / Copy / Creative / Proof / Localization       |
+--------------------------------------------------------------+
|
v
+--------------------------------------------------------------+
|                      GROWTH FOUNDATIONS                      |
| PMF / ICP / Positioning / Journey / Strategy / Growth Model  |
|   Metrics / Experiments / Data / Attribution / Forecasting   |
|      Planning / Infrastructure / Organization / RevOps       |
+--------------------------------------------------------------+
|
v
Insights feed the next Growth Diagnosis
</pre>

| Layer | Core question | Role in Growee Skills |
| --- | --- | --- |
| Growth Diagnosis | What is the primary constraint now? | Turn symptoms into a bounded outcome, evidence ledger, 30-day action, and execution route |
| Acquisition | How does qualified demand discover and reach the product? | Design and audit channels, campaigns, search, paid media, partnerships, community, and outbound |
| Activation | How do new users reach first value? | Diagnose entry paths, landing experiences, friction, onboarding, and the next meaningful action |
| Retention | How do customers continue receiving value? | Analyze cohorts, engagement, lifecycle communication, customer health, churn, and resurrection |
| Monetization | How does customer value become durable, profitable revenue? | Design pricing and packaging, then reconcile LTV, payback, and unit economics |
| Referral & Expansion | How do customers and product activity create deeper value and new distribution? | Build referrals, loops, expansion paths, incentives, marketplaces, and network effects |
| Content Production | What evidence-backed messages and assets should exist? | Plan and produce strategy, copy, images, video, campaign creative, customer proof, public communications, and localized content |
| Growth Foundations | Who is the customer, what value matters, and how should growth be measured and operated? | Establish PMF, ICP, positioning, journey, strategy, metrics, experiments, data quality, attribution, forecasting, planning, infrastructure, organization, governance, and RevOps |

Measured customer behavior and business outcomes feed the next diagnosis. That feedback loop, rather than content volume or isolated campaign activity, is the unit of progress. Every Skill preserves evidence and operating boundaries: external publishing and account changes remain under user control, and rights, claims, consent, privacy, and approvals must remain explicit.

## Install and use

Each directory under `skills/` is a standalone Agent Skill. The collection exposes 27 top-level Skills across diagnosis, the customer lifecycle, content production, and growth foundations. Another 59 specialist workflows live under `references/modules/` and load only when their parent Skill routes to them. Start with Growth Diagnosis, then install only the top-level Skills that match the primary constraint and execution route.

```bash
git clone https://github.com/krillinai/growee-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R growee-skills/skills/growth-diagnosis "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Invoke an installed Skill explicitly when the task could match several capabilities:

```text
Use $growth-diagnosis to identify our primary growth constraint and define the next evidence-backed decision.
```

Once the constraint is clear, replace `growth-diagnosis` with the relevant Skill name. For another Agent Skills-compatible client, copy or link the selected `skills/<name>/` directory into that client's Skill directory.

<!-- BEGIN GENERATED: catalog -->
## Follow the Growth Playbook

| Growth decision | Start with |
| --- | --- |
| Identify the primary constraint and choose the smallest evidence-backed execution route | [`Growth Diagnosis`](skills/growth-diagnosis/) |
| Connect qualified demand to the product through channels, campaigns, search, paid media, partnerships, and outbound | [`Acquisition Strategy & Campaigns`](skills/acquisition-strategy/), [`SEO & Search Systems`](skills/seo-audit/) |
| Move qualified visitors and new users to first value and the next meaningful action | [`Activation & Conversion`](skills/activation/) |
| Sustain recurring value, understand cohorts and churn, and recover valuable customer relationships | [`Retention & Customer Health`](skills/retention/), [`Lifecycle Marketing`](skills/lifecycle-marketing/) |
| Convert customer value into durable revenue through pricing, packaging, LTV, and unit economics | [`Monetization & Economics`](skills/monetization/) |
| Create deeper value and new distribution through referrals, loops, expansion, marketplaces, and network effects | [`Growth Loops & Network Effects`](skills/growth-loop-design/), [`Customer Expansion Strategy`](skills/customer-expansion-strategy/) |
| Turn strategy, customer evidence, and proof into governed content and creative assets | [`Content Strategy & Creative`](skills/content-strategy/), [`Copywriting & Editing`](skills/copywriting/), [`Marketing Video`](skills/marketing-video/) |
| Define customer, market, fit, positioning, growth model, measurement, experimentation, and operating foundations | [`Product-Market Fit & Journey`](skills/product-market-fit-assessment/), [`ICP & Positioning`](skills/positioning/), [`Growth Measurement & Experimentation`](skills/growth-measurement/), [`Growth Operations & Infrastructure`](skills/growth-operations/) |

## Complete growth capability map

**Structure:** This map lists 27 top-level Skills. They route to 59 specialist workflows under `references/modules/` and load those modules only when needed.

**Maturity:** Preview Skills need real-world validation; Validated Skills have passed realistic forward tests; Stable Skills have demonstrated repeatable use.

### Growth Diagnosis

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-diagnosis/">Growth&nbsp;Diagnosis</a></td><td>Preview</td><td>Diagnose primary constraints through funnel, anomaly, and maturity analysis, then route an evidence-backed 30-day plan</td></tr>
  </tbody>
</table>

### Acquisition

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/acquisition-strategy/">Acquisition&nbsp;Strategy&nbsp;&amp;&nbsp;Campaigns</a></td><td>Preview</td><td>Design acquisition portfolios and bounded campaigns across audience, offer, channels, journeys, assets, economics, measurement, and operating constraints</td></tr>
    <tr><td><a href="skills/partnership-marketing/">Partnerships&nbsp;&amp;&nbsp;Community</a></td><td>Preview</td><td>Design accountable partnerships and communities around shared customer value, roles, contribution, trust, operations, economics, and product paths</td></tr>
    <tr><td><a href="skills/sales-enablement/">Sales&nbsp;Enablement&nbsp;&amp;&nbsp;Outbound</a></td><td>Preview</td><td>Build evidence-led sales enablement and permitted B2B outbound messaging across buying situations, claims, proof, sequences, localization, and stop states</td></tr>
    <tr><td><a href="skills/paid-media-audit/">Paid&nbsp;Media&nbsp;Audit</a></td><td>Preview</td><td>Audit supplied Google, Meta, TikTok, and Douyin advertising evidence without live account access or external changes</td></tr>
    <tr><td><a href="skills/seo-audit/">SEO&nbsp;&amp;&nbsp;Search&nbsp;Systems</a></td><td>Preview</td><td>Audit and design SEO, programmatic pages, site architecture, structured data, and directory presence with evidence-backed quality and rollout controls</td></tr>
    <tr><td><a href="skills/aso-audit/">ASO&nbsp;Audit</a></td><td>Preview</td><td>Diagnose App Store and Google Play visibility, listing, creative, and conversion issues with evidence-backed recommendations</td></tr>
    <tr><td><a href="skills/geo/">GEO&nbsp;Audit</a></td><td>Preview</td><td>Assess website readiness for AI-generated search with evidence-based scoring, while separately measuring observed mentions and citations across bounded query panels</td></tr>
    <tr><td><a href="https://github.com/krillinai/autosocial-skills">Social&nbsp;Media&nbsp;Publishing</a></td><td>Integration</td><td>Automate video publishing to Xiaohongshu, Douyin, Kuaishou, and WeChat Channels with reusable titles, descriptions, tags, and metadata.</td></tr>
  </tbody>
</table>

### Activation

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/activation/">Activation&nbsp;&amp;&nbsp;Conversion</a></td><td>Preview</td><td>Define first value and improve activation across onboarding, landing pages, popups, friction, accessibility, measurement, and experiments</td></tr>
  </tbody>
</table>

### Retention

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/retention/">Retention&nbsp;&amp;&nbsp;Customer&nbsp;Health</a></td><td>Preview</td><td>Analyze and improve retention through cohorts, growth accounting, engagement, recurring value, churn, resurrection, and customer health</td></tr>
    <tr><td><a href="skills/lifecycle-marketing/">Lifecycle&nbsp;Marketing</a></td><td>Preview</td><td>Plan, draft, review, and localize evidence-bounded welcome, activation, transactional, retention, win-back, and campaign messaging across email, SMS, WeChat Official Accounts, Mini Program subscription messages, WeCom, and WhatsApp with explicit classification, permission, suppression, and external-action controls</td></tr>
  </tbody>
</table>

### Monetization

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/monetization/">Monetization&nbsp;&amp;&nbsp;Economics</a></td><td>Preview</td><td>Design and audit monetization across offers, pricing, packaging, LTV, CAC, unit economics, payback, migration, and customer protection</td></tr>
  </tbody>
</table>

### Referral & Expansion

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-loop-design/">Growth&nbsp;Loops&nbsp;&amp;&nbsp;Network&nbsp;Effects</a></td><td>Preview</td><td>Design and audit referrals, incentives, growth loops, marketplaces, and network effects through participant value, closure, economics, trust, and governance</td></tr>
    <tr><td><a href="skills/customer-expansion-strategy/">Customer&nbsp;Expansion&nbsp;Strategy</a></td><td>Preview</td><td>Audit, design, prioritize, measure, and govern value-led expansion inside existing customers across active seats, usage, workflows, products, teams, product-qualified signals, adoption and commercial reconciliation, retained contribution, and customer protection</td></tr>
  </tbody>
</table>

### Content Production

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/content-strategy/">Content&nbsp;Strategy&nbsp;&amp;&nbsp;Creative</a></td><td>Preview</td><td>Build content portfolios, permissioned customer proof, advertising creative, and public communications across questions, claims, formats, channels, workflows, measurement, and governance</td></tr>
    <tr><td><a href="skills/copywriting/">Copywriting&nbsp;&amp;&nbsp;Editing</a></td><td>Preview</td><td>Write and edit evidence-led copy for pages, campaigns, products, offers, and localization while preserving factual meaning and recording material edits</td></tr>
    <tr><td><a href="skills/marketing-image/">Marketing&nbsp;Image</a></td><td>Preview</td><td>Brief, create, edit, adapt, audit, and govern truthful marketing images through concept lineage, product accuracy, copy, brand, claims, source rights, people, platform formats, localization, accessibility, file QA, and downstream learning</td></tr>
    <tr><td><a href="skills/marketing-video/">Marketing&nbsp;Video</a></td><td>Preview</td><td>Brief, script, storyboard, create, adapt, audit, and govern truthful marketing videos through product and claim accuracy, source footage, people, voice, music, rights, localization, accessibility, rendering QA, and downstream learning</td></tr>
    <tr><td><a href="https://github.com/krillinai/KrillinAI">Video&nbsp;Translation&nbsp;&amp;&nbsp;Dubbing</a></td><td>Integration</td><td>Localize videos with transcription, subtitle translation, AI dubbing, voice cloning, and landscape or portrait rendering.</td></tr>
  </tbody>
</table>

### Growth Foundations

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/product-market-fit-assessment/">Product-Market&nbsp;Fit&nbsp;&amp;&nbsp;Journey</a></td><td>Preview</td><td>Assess product-market fit and customer journeys across problem, first and repeated value, path friction, service dependencies, and evidence boundaries</td></tr>
    <tr><td><a href="skills/positioning/">ICP&nbsp;&amp;&nbsp;Positioning</a></td><td>Preview</td><td>Define evidence-backed ICPs, segments, positioning, exclusions, category choices, messages, and validation plans</td></tr>
    <tr><td><a href="skills/growth-model-design/">Growth&nbsp;Model&nbsp;&amp;&nbsp;Opportunity</a></td><td>Preview</td><td>Design growth models and size opportunities across lifecycle behavior, economics, reach, capacity, overlap, scenarios, and risk</td></tr>
    <tr><td><a href="skills/customer-research/">Customer&nbsp;Research&nbsp;&amp;&nbsp;Surveys</a></td><td>Preview</td><td>Plan and synthesize customer research and decision-linked surveys with explicit sampling, evidence, consent, uncertainty, and interpretation boundaries</td></tr>
    <tr><td><a href="skills/market-sizing/">Market&nbsp;Intelligence&nbsp;&amp;&nbsp;Sizing</a></td><td>Preview</td><td>Research alternatives and size markets with attributable competitive evidence, compatible market units, scenarios, and uncertainty</td></tr>
    <tr><td><a href="skills/growth-strategy/">Growth&nbsp;&amp;&nbsp;Market&nbsp;Strategy</a></td><td>Preview</td><td>Make evidence-bounded growth and market-entry choices across customers, markets, mechanisms, capabilities, sequencing, pilots, and stop rules</td></tr>
    <tr><td><a href="skills/go-to-market-strategy/">Go-to-Market&nbsp;&amp;&nbsp;Launch</a></td><td>Preview</td><td>Design and govern go-to-market systems and product launches across audience, offer, motion, readiness, exposure, value, measurement, and scale gates</td></tr>
    <tr><td><a href="skills/growth-measurement/">Growth&nbsp;Measurement&nbsp;&amp;&nbsp;Experimentation</a></td><td>Preview</td><td>Design and audit metrics, targets, tracking, data quality, attribution, forecasts, and causal experiments as one evidence-backed growth measurement system</td></tr>
    <tr><td><a href="skills/growth-operations/">Growth&nbsp;Operations&nbsp;&amp;&nbsp;Infrastructure</a></td><td>Preview</td><td>Plan and operate growth across allocation, reviews, decisions, learning, infrastructure, organization, RevOps, and experiment programs</td></tr>
  </tbody>
</table>
<!-- END GENERATED: catalog -->

## Growth principles

- Diagnose the current constraint before choosing a channel, tactic, or tool.
- Manage acquisition, activation, retention, monetization, referral, and expansion as one lifecycle system.
- Treat content production as an execution layer that must connect to qualified acquisition and customer value.
- Use foundations to establish the customer, market, fit, positioning, growth model, measurement, experimentation, infrastructure, and organization behind every lifecycle decision, then feed evidence into the next diagnosis.

## Contributing

Growee Skills follows the structure and evidence standards of Growth Playbook. Add a top-level Skill only when no existing parent can own a clear, reusable growth decision; otherwise add or improve an on-demand module within the nearest parent Skill. A contribution should define its Playbook layer, evidence inputs, executable workflow, inspectable output, measurement path, and operating boundaries.

## License

This project is released under the [MIT License](LICENSE).
