<p align="center">
  <img src="Growee-logo.png" alt="Growee Skills logo" width="180">
</p>

<h1 align="center">Full-Lifecycle AI Growth Skills</h1>

<p align="center">AI-executable capabilities for growth diagnosis, content production, acquisition, activation, retention, monetization, and the systems beneath them.</p>

Growee Skills, by [KrillinAI](https://github.com/KrillinAI), is the open-source execution companion to Growth Playbook, a complete body of growth theory spanning frameworks, models, methods, and evidence. Growee Skills turns that body of knowledge into reusable Agent Skills for bounded growth work.

<p align="center">
  <a href="https://github.com/krillinai/growee-skills/stargazers"><img src="https://img.shields.io/github/stars/krillinai/growee-skills?style=flat-square&amp;logo=github&amp;label=Stars" alt="GitHub Stars"></a>
  <a href="https://clawee.ai"><img src="https://img.shields.io/badge/clawee.ai-Enterprise_Growth_Agent-6f42c1?style=flat-square" alt="clawee.ai"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT"></a>
</p>

<p align="center"><strong><a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a></strong></p>

## From diagnosis to compounding growth

Growee Skills follows the same mainline as Growth Playbook. Diagnosis identifies the current constraint. Foundations define the customer, market, value, and growth model. Content production turns that strategy into usable assets. The lifecycle stages move customers from discovery to first value, repeated value, revenue, and expansion. Growth systems make every stage measurable and repeatable.

<pre align="center">
+--------------------------------------------------------------+
|                       GROWTH DIAGNOSIS                       |
|            Constraint / Evidence / 30-Day Action             |
+--------------------------------------------------------------+
|
v
+--------------------------------------------------------------+
|                      GROWTH FOUNDATIONS                      |
|       PMF / ICP / Positioning / Journey / Growth Model       |
+--------------------------------------------------------------+
|
v
+--------------------------------------------------------------+
|                      CONTENT PRODUCTION                      |
|      Strategy / Copy / Creative / Proof / Localization       |
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
|                        GROWTH SYSTEMS                        |
| Metrics / Experiments / Data / Infrastructure / Organization |
|       Evidence / Governance / Agent Skills / Tools           |
+--------------------------------------------------------------+
|
v
Insights feed the next Growth Diagnosis
</pre>

| Layer | Core question | Role in Growee Skills |
| --- | --- | --- |
| Growth Diagnosis | What is the primary constraint now? | Turn symptoms into a bounded outcome, evidence ledger, 30-day action, and execution route |
| Growth Foundations | Who is the customer, what value matters, and how should growth work? | Establish PMF, ICP, positioning, journey, growth model, market, and strategic choices |
| Content Production | What evidence-backed messages and assets should exist? | Plan and produce copy, images, video, creative, customer proof, PR, and localized content |
| Acquisition | How does qualified demand discover and reach the product? | Design and audit channels, campaigns, search, paid media, partnerships, community, and outbound |
| Activation | How do new users reach first value? | Diagnose entry paths, landing experiences, friction, onboarding, and the next meaningful action |
| Retention | How do customers continue receiving value? | Analyze cohorts, engagement, lifecycle communication, customer health, churn, and resurrection |
| Monetization | How does customer value become durable, profitable revenue? | Design pricing and packaging, then reconcile LTV, payback, and unit economics |
| Referral & Expansion | How do customers and product activity create deeper value and new distribution? | Build referrals, loops, expansion paths, incentives, marketplaces, and network effects |
| Metrics & Experimentation | What changed, why, and with what confidence? | Define metrics and tracking, protect data quality, reconcile attribution, forecast, and test causality |
| Growth Infrastructure & Organization | How does the company make growth repeatable? | Operate planning, investments, decisions, reviews, learning, governance, infrastructure, and organization |

Measured customer behavior and business outcomes feed the next diagnosis. That feedback loop, rather than content volume or isolated campaign activity, is the unit of progress. Every Skill preserves evidence and operating boundaries: external publishing and account changes remain under user control, and rights, claims, consent, privacy, and approvals must remain explicit.

## Install and use

Each directory under `skills/` is a standalone Agent Skill. Adjacent methods are consolidated into 38 lifecycle-level Skills; specialized workflows live under `references/modules/` and load only when needed. Start with Growth Diagnosis, then install only the Skills that match the primary constraint and execution route.

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
| Define customer, market, fit, positioning, growth model, and strategic choices | [`Product-Market Fit & Journey`](skills/product-market-fit-assessment/), [`ICP & Positioning`](skills/positioning/) |
| Turn strategy, customer evidence, and proof into governed content and creative assets | [`Content Strategy & Customer Proof`](skills/content-strategy/), [`Copywriting & Editing`](skills/copywriting/), [`Marketing Video`](skills/marketing-video/) |
| Connect qualified demand to the product through channels, campaigns, search, paid media, partnerships, and outbound | [`Acquisition Strategy & Campaigns`](skills/acquisition-strategy/), [`SEO & Search Systems`](skills/seo-audit/) |
| Move qualified visitors and new users to first value and the next meaningful action | [`Activation & Conversion`](skills/activation/) |
| Sustain recurring value, understand cohorts and churn, and recover valuable customer relationships | [`Retention & Customer Health`](skills/retention/), [`Lifecycle Marketing`](skills/lifecycle-marketing/) |
| Convert customer value into durable revenue through pricing, packaging, LTV, and unit economics | [`Monetization & Economics`](skills/monetization/) |
| Create deeper value and new distribution through referrals, loops, expansion, marketplaces, and network effects | [`Growth Loops & Network Effects`](skills/growth-loop-design/), [`Customer Expansion Strategy`](skills/customer-expansion-strategy/) |
| Make growth observable, explainable, forecastable, and causally testable | [`Growth Metrics, Targets & Benchmarks`](skills/growth-metrics-design/), [`Tracking & Data Quality`](skills/tracking-plan/), [`Experiment Design`](skills/experiment-design/) |
| Build the planning, decision, data, operating, governance, and organizational systems that make growth repeatable | [`Growth Infrastructure & RevOps`](skills/growth-infrastructure-assessment/), [`Growth Organization Design`](skills/growth-organization-design/), [`Growth Reviews, Decisions & Risk`](skills/growth-operating-review/) |

## Choose your operating scope

Use Content Growth when content is the active constraint. Add a specialist bundle only when measurement, distribution, or operating capacity becomes the limiting factor.

| Scope | Description | Capabilities |
| --- | --- | ---: |
| `content-growth` · Content Growth | A focused content-marketing path connecting customer questions, content production, localization, distribution, and conversion. | 8 |
| `measurement-analytics` · Measurement & Analytics | Make growth observable and decision-ready through metrics, tracking, attribution, economics, forecasting, cohorts, and experiments. | 8 |
| `acquisition-distribution` · Acquisition & Distribution | Connect qualified demand to product value through channels, campaigns, search, conversion surfaces, partnerships, community, and outbound. | 8 |
| `growth-operating-system` · Growth Operating System | Turn growth decisions into a repeatable operating cadence across planning, capacity, investment, governance, reviews, learning, infrastructure, organization, and RevOps. | 8 |

## Complete growth capability map

<details>
<summary>Browse every Skill and integration by growth function</summary>

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
  </tbody>
</table>

### Content Production

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/content-strategy/">Content&nbsp;Strategy&nbsp;&amp;&nbsp;Customer&nbsp;Proof</a></td><td>Preview</td><td>Build content portfolios and permissioned customer proof across questions, claims, formats, channels, workflows, reuse, measurement, and governance</td></tr>
    <tr><td><a href="skills/copywriting/">Copywriting&nbsp;&amp;&nbsp;Editing</a></td><td>Preview</td><td>Write and edit evidence-led copy for pages, campaigns, products, offers, and localization while preserving factual meaning and recording material edits</td></tr>
    <tr><td><a href="skills/marketing-image/">Marketing&nbsp;Image</a></td><td>Preview</td><td>Brief, create, edit, adapt, audit, and govern truthful marketing images through concept lineage, product accuracy, copy, brand, claims, source rights, people, platform formats, localization, accessibility, file QA, and downstream learning</td></tr>
    <tr><td><a href="skills/marketing-video/">Marketing&nbsp;Video</a></td><td>Preview</td><td>Brief, script, storyboard, create, adapt, audit, and govern truthful marketing videos through product and claim accuracy, source footage, people, voice, music, rights, localization, accessibility, rendering QA, and downstream learning</td></tr>
    <tr><td><a href="skills/ad-creative/">Ad&nbsp;Creative</a></td><td>Preview</td><td>Research, design, brief, audit, compare, localize, and learn from traceable advertising concepts and purposeful variants with explicit customer evidence, claims, proof, rights, placements, landing paths, accessibility, downstream outcomes, and fatigue controls</td></tr>
    <tr><td><a href="skills/public-relations/">Public&nbsp;Relations</a></td><td>Preview</td><td>Plan, draft, audit, localize, and govern evidence-led PR narratives, press releases, media materials, spokesperson briefs, issue responses, facts, claims, quotes, rights, approvals, disclosures, corrections, coverage measurement, and crisis handoffs</td></tr>
    <tr><td><a href="https://github.com/krillinai/KrillinAI">Video&nbsp;Translation&nbsp;&amp;&nbsp;Dubbing</a></td><td>Integration</td><td>Localize videos with transcription, subtitle translation, AI dubbing, voice cloning, and landscape or portrait rendering.</td></tr>
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

### Metrics & Experimentation

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-metrics-design/">Growth&nbsp;Metrics,&nbsp;Targets&nbsp;&amp;&nbsp;Benchmarks</a></td><td>Preview</td><td>Design growth metrics, targets, and benchmarks with reproducible contracts, compatible baselines, uncertainty, ownership, and review rules</td></tr>
    <tr><td><a href="skills/tracking-plan/">Tracking&nbsp;&amp;&nbsp;Data&nbsp;Quality</a></td><td>Preview</td><td>Design tracking plans and audit data quality across events, identity, consent, lineage, reconciliation, monitoring, releases, and deprecation</td></tr>
    <tr><td><a href="skills/attribution-analysis/">Attribution&nbsp;&amp;&nbsp;Marketing&nbsp;Mix</a></td><td>Preview</td><td>Audit attribution and marketing mix models across journeys, media, identity, outcomes, reconciliation, incrementality, calibration, and uncertainty</td></tr>
    <tr><td><a href="skills/growth-forecasting/">Growth&nbsp;Forecasting</a></td><td>Preview</td><td>Build, audit, compare, back-test, calibrate, version, and govern decision-ready growth forecasts through explicit as-of snapshots, actual and forecast periods, drivers, assumptions, methods, uncertainty, revisions, bias, and market boundaries</td></tr>
    <tr><td><a href="skills/experiment-design/">Experiment&nbsp;Design</a></td><td>Preview</td><td>Decide when to experiment, design or review trustworthy causal and alternative evidence plans, and interpret mature results through explicit assignment, exposure, metrics, power, SRM, interference, guardrails, and decision rules</td></tr>
  </tbody>
</table>

### Growth Infrastructure & Organization

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-planning-cycle/">Growth&nbsp;Planning&nbsp;&amp;&nbsp;Allocation</a></td><td>Preview</td><td>Build integrated growth plans across strategy, capacity, investments, budgets, initiatives, dependencies, scenarios, approvals, and review cadence</td></tr>
    <tr><td><a href="skills/growth-operating-review/">Growth&nbsp;Reviews,&nbsp;Decisions&nbsp;&amp;&nbsp;Risk</a></td><td>Preview</td><td>Run growth reviews and govern decisions and risks through reconciled evidence, alternatives, authority, commitments, monitoring, and escalation</td></tr>
    <tr><td><a href="skills/growth-learning-system/">Growth&nbsp;Learning&nbsp;&amp;&nbsp;Change</a></td><td>Preview</td><td>Build growth learning, postmortems, and change systems with source lineage, causal boundaries, adoption, correction, follow-through, and retirement</td></tr>
    <tr><td><a href="skills/growth-infrastructure-assessment/">Growth&nbsp;Infrastructure&nbsp;&amp;&nbsp;RevOps</a></td><td>Preview</td><td>Assess growth infrastructure and RevOps across data, metrics, experiments, revenue entities, systems, handoffs, governance, and remediation</td></tr>
    <tr><td><a href="skills/growth-organization-design/">Growth&nbsp;Organization&nbsp;Design</a></td><td>Preview</td><td>Audit and design constraint-aligned outcome ownership, decision rights, central and embedded boundaries, staffing scenarios, initiative portfolios, operating cadence, maintenance ownership, organization health, and evidence-based reorganization triggers</td></tr>
    <tr><td><a href="skills/experiment-program-management/">Experiment&nbsp;Program&nbsp;Management</a></td><td>Preview</td><td>Audit, design, and refresh multi-team experimentation programs through decision-centered intake, portfolio selection, traffic and capacity, concurrency, preflight gates, quality incidents, maturity, follow-through, long-term validation, learning reuse, and governance</td></tr>
  </tbody>
</table>

</details>
<!-- END GENERATED: catalog -->

## Growth principles

- Diagnose the current constraint before choosing a channel, tactic, or tool.
- Establish customer, market, fit, positioning, and the growth model before scaling lifecycle activity.
- Treat content production as an execution layer that must connect to qualified acquisition and customer value.
- Manage acquisition, activation, retention, monetization, referral, and expansion as one lifecycle system.
- Use metrics, experiments, infrastructure, and organization to support every stage and feed evidence into the next diagnosis.

## Contributing

Growee Skills follows the structure and evidence standards of Growth Playbook. Add a Skill only when the existing collection cannot cover a clear, reusable growth decision. A contribution should define its Playbook layer, evidence inputs, executable workflow, inspectable output, measurement path, and operating boundaries.

## License

This project is released under the [MIT License](LICENSE).
