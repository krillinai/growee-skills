# Growth & Marketing Skills

**Reusable, AI-Executable Skills for Growth & Marketing**

By [clawee.ai](https://clawee.ai/), an Enterprise Growth Agent platform.

[![GitHub Stars](https://img.shields.io/github/stars/krillinai/growth-skills?style=flat-square&logo=github&label=Stars)](https://github.com/krillinai/growth-skills/stargazers)
[![Growth Playbook](https://img.shields.io/badge/Growth-Playbook-1f883d?style=flat-square)](https://github.com/krillinai/growth-playbook)
[![clawee.ai](https://img.shields.io/badge/clawee.ai-Enterprise_Growth_Agent-6f42c1?style=flat-square)](https://clawee.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

> Created and maintained by [KrillinAI](https://github.com/KrillinAI), an AI team focused on content intelligence and global growth. [Growth Playbook](https://github.com/krillinai/growth-playbook) is the open-source knowledge companion to Growth & Marketing Skills, providing the frameworks, cases, and methods that these reusable AI execution capabilities put into practice.

**[English](README.md) | [简体中文](README.zh-CN.md)**

An open collection of reusable skills for growth and marketing work. Growth & Marketing Skills helps practitioners and AI agents turn marketing knowledge into repeatable workflows across the entire growth lifecycle.

## What It Covers

- **Content & Creative** - Research, ideation, copywriting, editing, marketing images, video, and content distribution.
- **Research & Market Intelligence** - Customer research, competitive intelligence, market sizing, segmentation, and positioning.
- **Strategy & Planning** - Growth strategy, market entry, go-to-market, product launches, campaigns, and prioritization.
- **Measurement & Experimentation** - Metrics, tracking, data quality, analytics, forecasting, attribution, and experiments.
- **Lifecycle & Monetization** - Activation, engagement, retention, lifecycle marketing, pricing, monetization, expansion, and referrals.
- **Acquisition & Distribution** - Paid media, search, app-store and generative-search optimization, outbound, partnerships, communities, directories, and landing pages.
- **Operations & Governance** - Operating reviews, decisions, risk, learning, change, infrastructure, organization design, and revenue operations.

## Install and use

Each directory under `skills/` is a standalone Agent Skill. Install only the Skills needed for the current job so selection stays clear and context remains focused.

```bash
git clone https://github.com/krillinai/growth-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R growth-skills/skills/growth-diagnosis "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Invoke an installed Skill explicitly when the task could match several capabilities:

```text
Use $growth-diagnosis to identify our primary growth constraint and route the next analysis.
```

For another Agent Skills-compatible client, copy or link the selected `skills/<name>/` directory into that client's Skill directory.

<!-- BEGIN GENERATED: catalog -->
## Choose by job

| When you need to... | Start with |
| --- | --- |
| Create, adapt, and govern messages and media | [`Copywriting`](skills/copywriting/), [`Content Strategy`](skills/content-strategy/), [`Ad Creative`](skills/ad-creative/) |
| Understand customers, markets, alternatives, and buying contexts | [`Customer Research`](skills/customer-research/), [`Positioning`](skills/positioning/), [`Competitive Intelligence`](skills/competitive-intelligence/) |
| Choose direction, size commitments, and build decision-linked plans | [`Growth Diagnosis`](skills/growth-diagnosis/), [`Growth Strategy`](skills/growth-strategy/), [`Growth Planning Cycle`](skills/growth-planning-cycle/) |
| Define, measure, explain, forecast, and causally validate growth | [`Growth Metrics Design`](skills/growth-metrics-design/), [`Funnel Analysis`](skills/funnel-analysis/), [`Experiment Design`](skills/experiment-design/) |
| Improve first value, recurring value, revenue, expansion, and compounding mechanisms | [`Activation`](skills/activation/), [`Retention`](skills/retention/), [`Monetization`](skills/monetization/) |
| Plan, audit, and improve channels, campaigns, conversion surfaces, and distribution | [`Acquisition Strategy`](skills/acquisition-strategy/), [`Campaign Planning`](skills/campaign-planning/), [`Landing Page Audit`](skills/landing-page-audit/) |
| Operate decisions, systems, risks, learning, change, and organizational capacity | [`Growth Operating Review`](skills/growth-operating-review/), [`Growth Decision Record`](skills/growth-decision-record/), [`Growth Risk Management`](skills/growth-risk-management/) |

## Focused bundles

Install a focused bundle instead of loading the entire collection when the job is bounded.

| Bundle | Description | Skills |
| --- | --- | ---: |
| `core-growth` · Core Growth | A compact starting set for diagnosing, measuring, and improving the growth lifecycle. | 12 |
| `content-creative` · Content & Creative | Writing, editing, visual production, creative strategy, PR, and customer proof. | 8 |
| `measurement-analytics` · Measurement & Analytics | Metrics, tracking, data quality, attribution, economics, forecasting, cohorts, and experiments. | 16 |
| `acquisition-distribution` · Acquisition & Distribution | Channel strategy, campaigns, paid-media audits, search, conversion surfaces, partnerships, community, and outbound. | 19 |
| `growth-operating-system` · Growth Operating System | Capability assessment, planning, capacity, investment, governance, reviews, learning, change, infrastructure, organization, and RevOps. | 17 |

## Skill Catalog

### Content & Creative

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="https://github.com/krillinai/KrillinAI">Video&nbsp;Translation&nbsp;&amp;&nbsp;Dubbing</a></td><td>Integration</td><td>Localize videos with transcription, subtitle translation, AI dubbing, voice cloning, and landscape or portrait rendering.</td></tr>
    <tr><td><a href="skills/copywriting/">Copywriting</a></td><td>Experimental</td><td>Write evidence-led page, campaign, product, offer, and localization copy with explicit audience, market, language, locale, channel, and claim-source controls</td></tr>
    <tr><td><a href="skills/copy-editing/">Copy&nbsp;Editing</a></td><td>Experimental</td><td>Review and edit existing copy for clarity, hierarchy, voice, claims, accessibility, CTA, and market, locale, and channel fit while preserving factual meaning and recording exact edits</td></tr>
    <tr><td><a href="skills/marketing-image/">Marketing&nbsp;Image</a></td><td>Experimental</td><td>Brief, create, edit, adapt, audit, and govern truthful marketing images through concept lineage, product accuracy, copy, brand, claims, source rights, people, platform formats, localization, accessibility, file QA, and downstream learning</td></tr>
    <tr><td><a href="skills/marketing-video/">Marketing&nbsp;Video</a></td><td>Experimental</td><td>Brief, script, storyboard, create, adapt, audit, and govern truthful marketing videos through product and claim accuracy, source footage, people, voice, music, rights, localization, accessibility, rendering QA, and downstream learning</td></tr>
    <tr><td><a href="skills/content-strategy/">Content&nbsp;Strategy</a></td><td>Experimental</td><td>Build, audit, and operate evidence-led content portfolios through customer questions, content roles, pillars, claims and proof, native formats and channels, product paths, editorial workflows, reuse, measurement, refresh, and retirement</td></tr>
    <tr><td><a href="skills/ad-creative/">Ad&nbsp;Creative</a></td><td>Experimental</td><td>Research, design, brief, audit, compare, localize, and learn from traceable advertising concepts and purposeful variants with explicit customer evidence, claims, proof, rights, placements, landing paths, accessibility, downstream outcomes, and fatigue controls</td></tr>
    <tr><td><a href="skills/public-relations/">Public&nbsp;Relations</a></td><td>Experimental</td><td>Plan, draft, audit, localize, and govern evidence-led PR narratives, press releases, media materials, spokesperson briefs, issue responses, facts, claims, quotes, rights, approvals, disclosures, corrections, coverage measurement, and crisis handoffs</td></tr>
    <tr><td><a href="skills/customer-proof-development/">Customer&nbsp;Proof&nbsp;Development</a></td><td>Experimental</td><td>Turn attributable, permissioned customer evidence into credible case studies, testimonials, reference briefs, outcome stories, and reusable proof units with exact quote, metric, causality, privacy, approval, lineage, freshness, and withdrawal controls</td></tr>
    <tr><td><a href="https://github.com/krillinai/autosocial-skills">Social&nbsp;Media&nbsp;Publishing</a></td><td>Integration</td><td>Automate video publishing to Xiaohongshu, Douyin, Kuaishou, and WeChat Channels with reusable titles, descriptions, tags, and metadata.</td></tr>
  </tbody>
</table>

### Research & Market Intelligence

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/customer-research/">Customer&nbsp;Research</a></td><td>Experimental</td><td>Plan responsible customer research, synthesize attributable interviews, reviews, surveys, support, win/loss, and behavioral evidence, and translate bounded findings and counterevidence into decision-ready customer insight</td></tr>
    <tr><td><a href="skills/survey-design-and-analysis/">Survey&nbsp;Design&nbsp;&amp;&nbsp;Analysis</a></td><td>Experimental</td><td>Design, audit, localize, field, analyze, compare, and govern decision-linked surveys through explicit constructs, populations, sampling frames, instruments, response states, quality rules, missingness, weighting, uncertainty, and interpretation boundaries</td></tr>
    <tr><td><a href="skills/competitive-intelligence/">Competitive&nbsp;Intelligence</a></td><td>Experimental</td><td>Map, research, compare, and monitor decision-relevant alternatives through attributable sources, explicit freshness, product and price versions, capability and availability states, customer evidence, change controls, uncertainty, and ethical access boundaries</td></tr>
    <tr><td><a href="skills/positioning/">Positioning</a></td><td>Experimental</td><td>Build, audit, or revise evidence-bounded positioning through scoped buying situations, real alternatives, capability-to-value proof chains, best-fit and exclusion conditions, category decisions, message architecture, and validation plans</td></tr>
    <tr><td><a href="skills/icp-segmentation/">ICP&nbsp;Segmentation</a></td><td>Experimental</td><td>Discover, define, validate, and govern decision-changing customer segments and ICPs with observable rules, explicit exclusions, compatible value and economic evidence, differentiated paths, and privacy and fairness controls</td></tr>
    <tr><td><a href="skills/product-market-fit-assessment/">Product-Market&nbsp;Fit&nbsp;Assessment</a></td><td>Experimental</td><td>Assess, measure, or revalidate bounded product-market fit claims by reconciling problem, first-value, repeated-value, must-have survey, segment, economic, distribution, Four Fits, and guardrail evidence without inventing a universal score or certification</td></tr>
    <tr><td><a href="skills/customer-journey-analysis/">Customer&nbsp;Journey&nbsp;Analysis</a></td><td>Experimental</td><td>Map, audit, and redesign evidence-bounded customer journeys and service blueprints across participant roles, state paths, touchpoints, continuity, backstage dependencies, friction, failure, recovery, accessibility, exit, measurement, and causal boundaries</td></tr>
    <tr><td><a href="skills/market-sizing/">Market&nbsp;Sizing</a></td><td>Experimental</td><td>Build, audit, and reconcile evidence-bounded market estimates through explicit customer and economic units, total-to-attainable demand layers, compatible top-down and bottom-up methods, source lineage, overlap, serviceability, reachability, scenarios, sensitivity, and uncertainty</td></tr>
  </tbody>
</table>

### Strategy & Planning

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-diagnosis/">Growth&nbsp;Diagnosis</a></td><td>Experimental</td><td>Identify the primary growth constraint from attributable evidence and route a market-aware 30-day decision plan across acquisition, activation, retention, monetization, growth loops, and growth systems</td></tr>
    <tr><td><a href="skills/growth-maturity-assessment/">Growth&nbsp;Maturity&nbsp;Assessment</a></td><td>Experimental</td><td>Assess decision-specific growth capabilities across strategy, lifecycle, measurement, experimentation, infrastructure, organization, operations, risk, and learning through separate evidence for definition, implementation, operation, adoption, reliability, decision use, and outcomes without a universal stage or composite score</td></tr>
    <tr><td><a href="skills/growth-strategy/">Growth&nbsp;Strategy</a></td><td>Experimental</td><td>Audit, design, and refresh evidence-bounded 6-18 month growth choices across customers, markets, value, mechanisms, economics, capabilities, portfolio, sequencing, exclusions, scenarios, and review triggers</td></tr>
    <tr><td><a href="skills/growth-model-design/">Growth&nbsp;Model&nbsp;Design</a></td><td>Experimental</td><td>Map, audit, calculate, version, and scenario-test business-specific growth models connecting customer value, lifecycle behavior, channels, Four Fits, economics, propagation, reinvestment, capacity, guardrails, and decision-relevant constraints</td></tr>
    <tr><td><a href="skills/growth-planning-cycle/">Growth&nbsp;Planning&nbsp;Cycle</a></td><td>Experimental</td><td>Build, audit, and refresh coherent annual, quarterly, or rolling growth planning cycles by reconciling strategy, metrics, targets, forecasts, opportunities, investments, portfolios, initiatives, capacity, budget boundaries, decision calendars, approvals, and operating reviews</td></tr>
    <tr><td><a href="skills/growth-capacity-planning/">Growth&nbsp;Capacity&nbsp;Planning</a></td><td>Experimental</td><td>Build, audit, and refresh evidence-bounded capacity plans across demand, workload, people, skills, systems, vendors, inventories, customer and experiment exposure, queues, throughput, service, shared constraints, utilization, reserves, scenarios, triggers, and approval-ready gap options</td></tr>
    <tr><td><a href="skills/growth-opportunity-sizing/">Growth&nbsp;Opportunity&nbsp;Sizing</a></td><td>Experimental</td><td>Size, audit, and compare growth opportunities through compatible baselines, eligible populations, bounded change, reach, retained value, net economics, timing, sensitivity, overlap, capacity, risk, and decision-changing evidence without invented uplift or double counting</td></tr>
    <tr><td><a href="skills/growth-investment-case/">Growth&nbsp;Investment&nbsp;Case</a></td><td>Experimental</td><td>Audit, build, and refresh decision-ready cases for bounded growth investments through explicit baselines, alternatives, customer value, evidence, incremental benefits and costs, cash, capacity, risks, scenarios, gates, and approval boundaries</td></tr>
    <tr><td><a href="skills/growth-budget-allocation/">Growth&nbsp;Budget&nbsp;Allocation</a></td><td>Experimental</td><td>Audit, design, and reallocate cross-functional growth budgets and resources through reconciled availability, protected obligations, comparable customer value, incremental and marginal economics, cash, capacity, overlap, scenarios, evidence gates, and approval boundaries</td></tr>
    <tr><td><a href="skills/growth-initiative-planning/">Growth&nbsp;Initiative&nbsp;Planning</a></td><td>Experimental</td><td>Build, audit, and replan feasible 30-90 day execution plans for one selected growth initiative through decision lineage, bounded outcomes, workstreams, dependencies, capacity, evidence gates, commitments, risks, change rules, and authorization boundaries</td></tr>
    <tr><td><a href="skills/market-entry-strategy/">Market&nbsp;Entry&nbsp;Strategy</a></td><td>Experimental</td><td>Assess, compare, sequence, and pilot new markets through explicit market units, seven readiness gates, beachhead selection, local product and commercial adaptation, distribution, operations, data governance, retained economics, stop rules, and exit protections</td></tr>
    <tr><td><a href="skills/go-to-market-strategy/">Go-to-Market&nbsp;Strategy</a></td><td>Experimental</td><td>Audit, design, compare, sequence, and govern repeatable product-market systems across customers, positioning, offers, motions, routes, buying paths, first and repeated value, delivery, measurement, retained economics, readiness, pilots, and scale gates</td></tr>
    <tr><td><a href="skills/product-launch-strategy/">Product&nbsp;Launch&nbsp;Strategy</a></td><td>Experimental</td><td>Audit, design, stage, compare, measure, and govern product or feature launches through explicit release units, readiness gates, audience ladders, access and exposure states, first and repeated value, operating controls, and evidence-led expansion decisions</td></tr>
  </tbody>
</table>

### Measurement & Experimentation

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-metrics-design/">Growth&nbsp;Metrics&nbsp;Design</a></td><td>Experimental</td><td>Audit KPIs and North Star candidates, design value-linked metric constellations and evidence-labeled trees, and specify reproducible contracts, guardrails, targets, lineage, quality, and governance without inventing benchmarks or causality</td></tr>
    <tr><td><a href="skills/growth-target-setting/">Growth&nbsp;Target&nbsp;Setting</a></td><td>Experimental</td><td>Audit, design, reconcile, and refresh growth outcome targets, input commitments, thresholds, aspirations, and guardrails through versioned metrics, baselines, forecasts, opportunities, hierarchy, capacity, tradeoffs, incentives, ownership, and review rules</td></tr>
    <tr><td><a href="skills/growth-benchmark-analysis/">Growth&nbsp;Benchmark&nbsp;Analysis</a></td><td>Experimental</td><td>Source, audit, normalize, compare, and monitor internal, peer, industry, vendor, survey, modeled, and case benchmarks through explicit reference classes, metric compatibility, lineage, bias, maturity, uncertainty, and transfer limits</td></tr>
    <tr><td><a href="skills/growth-anomaly-investigation/">Growth&nbsp;Anomaly&nbsp;Investigation</a></td><td>Experimental</td><td>Triage, investigate, and review unexpected metric changes through frozen contracts, source reconciliation, maturity, expected variation, contribution-preserving decomposition, timelines, candidate mechanisms, causal boundaries, and controlled resolution</td></tr>
    <tr><td><a href="skills/tracking-plan/">Tracking&nbsp;Plan</a></td><td>Experimental</td><td>Design, audit, or migrate implementation-ready event and property schemas with explicit value states, source truth, identity, consent, lineage, reconciliation, QA, release, rollback, and deprecation controls</td></tr>
    <tr><td><a href="skills/growth-data-quality-audit/">Growth&nbsp;Data&nbsp;Quality&nbsp;Audit</a></td><td>Experimental</td><td>Audit decision-critical growth data and design quality controls across population coverage, completeness, identity, uniqueness, semantic validity, timeliness, maturity, lineage, source reconciliation, revisions, incidents, monitoring, privacy, and governance</td></tr>
    <tr><td><a href="skills/attribution-analysis/">Attribution&nbsp;Analysis</a></td><td>Experimental</td><td>Audit, design, compare, and reconcile attribution through explicit outcome, identity, source, journey, touchpoint, lookback, model, unknown-state, downstream-value, revenue, quality, privacy, and incrementality boundaries</td></tr>
    <tr><td><a href="skills/marketing-mix-modeling/">Marketing&nbsp;Mix&nbsp;Modeling</a></td><td>Experimental</td><td>Specify, build, audit, calibrate, compare, and refresh aggregate Marketing Mix Models through reconciled outcomes, media and context panels, adstock, saturation, identification, experiments, validation, contribution, response support, uncertainty, and decision-bounded budget scenarios</td></tr>
    <tr><td><a href="skills/ltv-analysis/">LTV&nbsp;Analysis</a></td><td>Experimental</td><td>Audit, calculate, forecast, compare, validate, and govern customer lifetime value through explicit entities, cohorts, original denominators, value and cost bases, maturity, censoring, horizons, model assumptions, uncertainty, calibration, and decision boundaries</td></tr>
    <tr><td><a href="skills/unit-economics-analysis/">Unit&nbsp;Economics&nbsp;Analysis</a></td><td>Experimental</td><td>Audit, model, compare, and govern CAC variants, matched-cohort contribution and LTV, accounting and cash payback, marginal returns, freemium and marketplace economics, portfolio mix, scenarios, uncertainty, and decision boundaries</td></tr>
    <tr><td><a href="skills/growth-forecasting/">Growth&nbsp;Forecasting</a></td><td>Experimental</td><td>Build, audit, compare, back-test, calibrate, version, and govern decision-ready growth forecasts through explicit as-of snapshots, actual and forecast periods, drivers, assumptions, methods, uncertainty, revisions, bias, and market boundaries</td></tr>
    <tr><td><a href="skills/growth-accounting/">Growth&nbsp;Accounting</a></td><td>Experimental</td><td>Reconcile period-to-period customer and recurring-value growth into retained, new, resurrected, churned, expanded, and contracted movements with explicit entity, identity, maturity, value, adjustment, mix, and causal boundaries</td></tr>
    <tr><td><a href="skills/cohort-analysis/">Cohort&nbsp;Analysis</a></td><td>Experimental</td><td>Define time-, exposure-, behavior-, or state-based cohorts; build maturity-aware matrices from supplied event or aggregate data; compare compatible groups; and separate mix shifts from within-cohort change without inventing causal conclusions</td></tr>
    <tr><td><a href="skills/engagement-analysis/">Engagement&nbsp;Analysis</a></td><td>Experimental</td><td>Analyze zero-inclusive, value-bearing frequency, depth, breadth, quality, and concentration distributions across natural opportunities and product topologies without turning activity into retention, Product-Market Fit, causality, or impact</td></tr>
    <tr><td><a href="skills/experiment-design/">Experiment&nbsp;Design</a></td><td>Experimental</td><td>Decide when to experiment, design or review trustworthy causal and alternative evidence plans, and interpret mature results through explicit assignment, exposure, metrics, power, SRM, interference, guardrails, and decision rules</td></tr>
    <tr><td><a href="skills/funnel-analysis/">Funnel&nbsp;Analysis</a></td><td>Experimental</td><td>Analyze conversion and absolute loss across value states with frozen entities, eligibility, events, denominators, windows, maturity, and cohorts; distinguish observed drop-off from cause, diagnose constraints, and design evidence-bounded improvements</td></tr>
  </tbody>
</table>

### Lifecycle & Monetization

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/activation/">Activation</a></td><td>Experimental</td><td>Define and analyze first value, diagnose onboarding and activation-path constraints, and design evidence-bounded interventions across entry states, product levels, and consumer, B2B, marketplace, AI, low-frequency, or assisted products</td></tr>
    <tr><td><a href="skills/lifecycle-marketing/">Lifecycle&nbsp;Marketing</a></td><td>Experimental</td><td>Plan, draft, review, and localize evidence-bounded welcome, activation, transactional, retention, win-back, and campaign messaging across email, SMS, WeChat Official Accounts, Mini Program subscription messages, WeCom, and WhatsApp with explicit classification, permission, suppression, and external-action controls</td></tr>
    <tr><td><a href="skills/retention/">Retention</a></td><td>Experimental</td><td>Define and analyze cohorts, diagnose recurring-value, churn, and resurrection mechanisms, and design evidence-bounded retention systems across user, account, product, and revenue levels</td></tr>
    <tr><td><a href="skills/customer-health-modeling/">Customer&nbsp;Health&nbsp;Modeling</a></td><td>Experimental</td><td>Specify, build, audit, validate, calibrate, monitor, and refresh decision-specific customer and account health models through explicit hierarchies, outcomes, prediction times, features, labels, censoring, leakage, calibration, capacity thresholds, reason codes, drift, privacy, and safe action boundaries</td></tr>
    <tr><td><a href="skills/customer-expansion-strategy/">Customer&nbsp;Expansion&nbsp;Strategy</a></td><td>Experimental</td><td>Audit, design, prioritize, measure, and govern value-led expansion inside existing customers across active seats, usage, workflows, products, teams, product-qualified signals, adoption and commercial reconciliation, retained contribution, and customer protection</td></tr>
    <tr><td><a href="skills/monetization/">Monetization</a></td><td>Experimental</td><td>Map user, buyer, and payer value; analyze offers, packaging, pricing, paid conversion, retained revenue, and unit economics; and design evidence-bounded commercial systems with migration, fairness, and market controls</td></tr>
    <tr><td><a href="skills/pricing-and-packaging-strategy/">Pricing&nbsp;&amp;&nbsp;Packaging&nbsp;Strategy</a></td><td>Experimental</td><td>Audit, research, design, validate, migrate, and govern offers, package architecture, price metrics, prices, terms, discounts, free and trial paths, retained economics, experiments, and customer protections</td></tr>
    <tr><td><a href="skills/referral-program-design/">Referral&nbsp;Program&nbsp;Design</a></td><td>Experimental</td><td>Design, audit, measure, and govern value-led referral programs through sender and recipient value, triggers, permissions, destination continuity, rewards, identity, retained quality, incrementality, economics, fraud, trust, and operations</td></tr>
    <tr><td><a href="skills/incentive-system-design/">Incentive&nbsp;System&nbsp;Design</a></td><td>Experimental</td><td>Audit, design, taper, or stop rewards, discounts, credits, subsidies, referrals, loyalty, progress, status, and structural incentives using retained incremental contribution, full cost, post-incentive behavior, fraud, cannibalization, fairness, and trust</td></tr>
    <tr><td><a href="skills/growth-loop-design/">Growth&nbsp;Loop&nbsp;Design</a></td><td>Experimental</td><td>Audit whether a mechanism closes, measure value-producing transitions, and design evidence-bounded collaboration, referral, content, marketplace, data, or reinvestment loops without executing external actions</td></tr>
    <tr><td><a href="skills/marketplace-growth-strategy/">Marketplace&nbsp;Growth&nbsp;Strategy</a></td><td>Experimental</td><td>Diagnose, cold-start, optimize, replicate, govern, or stop two-sided and multi-sided marketplaces through atomic market units, side-specific state paths, local liquidity, matching, fulfillment, quality, retention, incentives, participant and platform economics, trust, and evidence-gated expansion</td></tr>
    <tr><td><a href="skills/network-effects-strategy/">Network&nbsp;Effects&nbsp;Strategy</a></td><td>Experimental</td><td>Audit, cold-start, strengthen, replicate, govern, or stop network effects using bounded network units, participant value, core interactions, hard sides, local liquidity, quality, retention, multi-homing, congestion, defensibility, causal evidence, and market-specific graduation gates</td></tr>
  </tbody>
</table>

### Acquisition & Distribution

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/acquisition-strategy/">Acquisition&nbsp;Strategy</a></td><td>Experimental</td><td>Audit, design, compare, sequence, scale, cap, or stop acquisition channels and portfolios using customer intent, source-to-retained-value quality, channel-model fit, attribution and incrementality, full and marginal economics, saturation, dependency, capacity, and market-entry evidence</td></tr>
    <tr><td><a href="skills/campaign-planning/">Campaign&nbsp;Planning</a></td><td>Experimental</td><td>Turn a bounded objective into an evidence-based audience, positioning, offer, channel, journey, asset, budget, measurement, launch, and postmortem plan without assuming account access or executing the campaign</td></tr>
    <tr><td><a href="skills/partnership-marketing/">Partnership&nbsp;Marketing</a></td><td>Experimental</td><td>Assess, design, pilot, govern, and exit accountable co-marketing, co-selling, channel, affiliate, integration, marketplace, and ecosystem partnerships through shared-customer value, contributions, rights, data, attribution, economics, operations, and customer protection</td></tr>
    <tr><td><a href="skills/community-growth-strategy/">Community&nbsp;Growth&nbsp;Strategy</a></td><td>Experimental</td><td>Audit and design value-led communities through explicit participant roles, membership and lifecycle states, onboarding, useful interactions, programming, contribution, moderation, operating capacity, platform resilience, product paths, measurement, and trust</td></tr>
    <tr><td><a href="skills/sales-enablement/">Sales&nbsp;Enablement</a></td><td>Experimental</td><td>Build, audit, localize, govern, and measure evidence-led seller and buyer assets mapped to buying situations, qualification, milestones, claims, proof, alternatives, implementation, realized value, and versioned field learning</td></tr>
    <tr><td><a href="skills/landing-page-audit/">Landing&nbsp;Page&nbsp;Audit</a></td><td>Experimental</td><td>Audit source-to-page continuity, value, proof, hierarchy, CTA, forms, friction, mobile experience, accessibility, downstream quality, and measurement readiness with a fixed six-dimension score and separate evidence coverage</td></tr>
    <tr><td><a href="skills/popup-optimization/">Popup&nbsp;Optimization</a></td><td>Experimental</td><td>Design, audit, localize, and experiment on respectful popup, modal, banner, slide-in, and interstitial experiences through explicit relevance, eligibility, triggers, frequency, suppression, consent, dismissal, accessibility, mobile, performance, downstream value, and guardrails</td></tr>
    <tr><td><a href="skills/meta-ads-audit/">Meta&nbsp;Ads&nbsp;Audit</a></td><td>Experimental</td><td>Audit supplied Ads Manager CSVs, creative inventories, landing pages, measurement evidence, and aggregated business outcomes without accessing or changing a live Meta account</td></tr>
    <tr><td><a href="skills/google-ads-audit/">Google&nbsp;Ads&nbsp;Audit</a></td><td>Experimental</td><td>Audit supplied Google Ads campaign, conversion, Search, Shopping, Performance Max, creative, destination, measurement, and aggregated business evidence without accessing or changing a live account</td></tr>
    <tr><td><a href="skills/tiktok-ads-audit/">TikTok&nbsp;Ads&nbsp;Audit</a></td><td>Experimental</td><td>Audit supplied international TikTok Ads structure, short-video creative, Spark Ads rights, destination, event, attribution, and aggregated business evidence without accessing or changing a live account</td></tr>
    <tr><td><a href="skills/douyin-ads-audit/">Douyin&nbsp;Ads&nbsp;Audit</a></td><td>Experimental</td><td>Audit supplied Douyin advertising evidence across Ocean Engine, Qianchuan, DOU+, creative and creator rights, product or livestream commerce, conversion, attribution, and aggregated business outcomes without live account access</td></tr>
    <tr><td><a href="skills/seo-audit/">SEO&nbsp;Audit</a></td><td>Experimental</td><td>Diagnose technical, content, and search visibility issues with evidence-backed recommendations</td></tr>
    <tr><td><a href="skills/programmatic-seo/">Programmatic&nbsp;SEO</a></td><td>Experimental</td><td>Validate, design, audit, launch-plan, and govern scalable search page systems through explicit intent, reliable supply, useful templates, page states, quality gates, bounded rollout, downstream value, maintenance, and retirement</td></tr>
    <tr><td><a href="skills/aso-audit/">ASO&nbsp;Audit</a></td><td>Experimental</td><td>Diagnose App Store and Google Play visibility, listing, creative, and conversion issues with evidence-backed recommendations</td></tr>
    <tr><td><a href="skills/geo/">GEO&nbsp;Audit</a></td><td>Experimental</td><td>Assess website readiness for AI-generated search with evidence-based scoring, while separately measuring observed mentions and citations across bounded query panels</td></tr>
    <tr><td><a href="skills/structured-data-builder/">Structured&nbsp;Data&nbsp;Builder</a></td><td>Experimental</td><td>Generate, audit, repair, or template evidence-traced JSON-LD from visible page content or attributable authoritative data, with provider-specific validation and market-aware limitations</td></tr>
    <tr><td><a href="skills/search-site-planner/">Search&nbsp;Site&nbsp;Planner</a></td><td>Experimental</td><td>Plan or review bounded site hierarchies, navigation, URLs, breadcrumbs, internal links, and migration mappings with complete inventory reconciliation and market-aware validation</td></tr>
    <tr><td><a href="skills/directory-submissions/">Directory&nbsp;Submissions</a></td><td>Experimental</td><td>Select, prepare, audit, update, and govern accurate high-value directory listings through entity identity, eligibility, categories, claims, assets, rights, verification, duplicates, paid disclosure, tracking, freshness, and qualified downstream value</td></tr>
    <tr><td><a href="skills/b2b-outbound-messaging/">B2B&nbsp;Outbound&nbsp;Messaging</a></td><td>Experimental</td><td>Draft evidence-based one-to-one B2B messages, bounded sequences, follow-ups, and native localization for market-appropriate permitted channels with explicit permission, stop-state, privacy, and action boundaries</td></tr>
  </tbody>
</table>

### Operations & Governance

<table>
  <thead>
    <tr><th width="32%">Skill</th><th width="12%">Status</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="skills/growth-operating-review/">Growth&nbsp;Operating&nbsp;Review</a></td><td>Experimental</td><td>Build, audit, and refresh decision-focused weekly, monthly, or quarterly growth reviews that reconcile customer value, lifecycle, accounting, economics, forecasts, anomalies, experiments, portfolios, risks, decisions, and commitments without turning status into impact</td></tr>
    <tr><td><a href="skills/growth-decision-record/">Growth&nbsp;Decision&nbsp;Record</a></td><td>Experimental</td><td>Build, audit, and refresh one canonical, versioned growth decision record that preserves alternatives, evidence, assumptions, uncertainty, dissent, authority, conditions, dependencies, downstream consumers, follow-through, outcomes, corrections, expiry, and supersession without rewriting history or implying execution</td></tr>
    <tr><td><a href="skills/growth-risk-management/">Growth&nbsp;Risk&nbsp;Management</a></td><td>Experimental</td><td>Build, audit, and refresh cross-initiative growth risk portfolios through explicit risk states, evidence, appetite, tolerances, limits, interactions, concentration, controls, treatments, acceptance, monitoring, escalation, closure, and residual obligations without inventing scores or replacing specialist judgment</td></tr>
    <tr><td><a href="skills/growth-learning-system/">Growth&nbsp;Learning&nbsp;System</a></td><td>Experimental</td><td>Build, audit, and refresh governed libraries of reusable growth learning through source lineage, bounded learning units, context, contradictions, deduplication, retrieval, freshness, rights, reuse, decision linkage, correction, and retirement without turning summaries, citations, or usage into truth or impact</td></tr>
    <tr><td><a href="skills/growth-change-management/">Growth&nbsp;Change&nbsp;Management</a></td><td>Experimental</td><td>Build, audit, and refresh bounded transitions for authorized growth changes through affected populations, readiness, capacity, communications, enablement, support, migration, rollout, adoption, stabilization, legacy retirement, and outcome evidence without treating announcements, training, access, or launch as impact</td></tr>
    <tr><td><a href="skills/growth-postmortem/">Growth&nbsp;Postmortem</a></td><td>Experimental</td><td>Build, audit, and refresh evidence-bounded postmortems for completed, stopped, harmful, or inconclusive growth work by preserving original decisions, reconciling outcomes and economics, bounding causal claims, separating decision from result quality, and turning findings into governed learning and follow-up</td></tr>
    <tr><td><a href="skills/growth-infrastructure-assessment/">Growth&nbsp;Infrastructure&nbsp;Assessment</a></td><td>Experimental</td><td>Assess data, metric, experiment, decision, execution, creative, and governance capabilities; decide what to centralize or keep local; compare build, buy, compose, consolidate, or retire options; and prioritize a dependency-ordered infrastructure roadmap</td></tr>
    <tr><td><a href="skills/growth-organization-design/">Growth&nbsp;Organization&nbsp;Design</a></td><td>Experimental</td><td>Audit and design constraint-aligned outcome ownership, decision rights, central and embedded boundaries, staffing scenarios, initiative portfolios, operating cadence, maintenance ownership, organization health, and evidence-based reorganization triggers</td></tr>
    <tr><td><a href="skills/revops-audit/">RevOps&nbsp;Audit</a></td><td>Experimental</td><td>Audit revenue entities, lifecycle definitions, buyer progress, routing, ownership, handoffs, systems, pipeline, forecasting, commercial and finance reconciliation, customer value, renewals, expansion, controls, and dependency-ordered remediation</td></tr>
    <tr><td><a href="skills/experiment-program-management/">Experiment&nbsp;Program&nbsp;Management</a></td><td>Experimental</td><td>Audit, design, and refresh multi-team experimentation programs through decision-centered intake, portfolio selection, traffic and capacity, concurrency, preflight gates, quality incidents, maturity, follow-through, long-term validation, learning reuse, and governance</td></tr>
  </tbody>
</table>
<!-- END GENERATED: catalog -->

## The Growth Lifecycle

The collection is designed to support connected workflows from first contact to compounding growth:

**Discover → Acquire → Activate → Convert → Retain → Expand**

## Growing the Collection

This repository is at an early stage. New skills will be added as practical, reusable workflows are developed and validated.

## Contributing

Contributions are welcome. A useful skill should address a clear growth or marketing problem, provide an actionable workflow, and produce outcomes that can be evaluated. Contribution guidelines and skill conventions will evolve with the collection.

## License

This project is released under the [MIT License](LICENSE).
