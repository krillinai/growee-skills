---
name: cohort-analysis
description: Use when a CSV, event export, aggregate table, or analytics question needs time-, exposure-, behavior-, or state-based cohort definition, cohort matrix construction, maturity-aware comparison, mix decomposition, cohort LTV, or a calculation-ready cohort specification across product, marketing, sales, commerce, marketplace, lifecycle, or experiment work.
---

# Cohort Analysis

Define comparable cohorts and analyze supplied event or aggregate data at equal maturity. Keep observed movement separate from causal explanation, preserve unavailable evidence, and produce a reproducible decision record rather than a percentage-only heatmap.

Read [cohort-contract.md](references/cohort-contract.md) before requesting, normalizing, or calculating data. Read [analysis-methods.md](references/analysis-methods.md) before building matrices, comparing cohorts, decomposing mix, or analyzing value. Read [output-contract.md](references/output-contract.md) before delivering results. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Define a calculation-ready cohort, event, query, or aggregate-table contract when compatible data is unavailable |
| `analysis` | Build and interpret one canonical cohort view from supplied compatible data |
| `comparison` | Compare start periods, exposures, behaviors, states, markets, or decision-relevant segments at equal maturity |

Name one primary mode. A request may include secondary work, but keep metric construction, observed comparison, causal hypotheses, and proposed interventions visibly separate.

## Freeze The Cohort Contract

Record the decision and owner; entity and level; eligibility and exclusions; cohort basis and start event; qualifying outcome or value event; first, latest, every, or episode assignment; interval and cohort-age rule; numerator and denominator; observation and maturation windows; cutoff and timezone; identity and deduplication; re-entry and deletion; source, version, freshness, and late-arrival allowance; allowed segments; privacy threshold; and limitations.

Do not use `cohort` as a synonym for every customer group. A segment groups relatively durable attributes; a funnel represents value transitions; a cohort fixes a shared start, exposure, behavior, or state for comparable observation. Route durable customer qualification to `customer-research`, transition constraints to `growth-diagnosis`, and recurring-value mechanisms to `retention`.

## Validate Before Calculating

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may use `reported signal` with a blank evidence state.

Calculate only when entity, eligibility, identity, start, outcome, denominator, interval, cutoff, timezone, maturity, and definition version are compatible. Preserve missing values, zeroes, late events, duplicate identities, right censoring, unknown segments, and source discrepancies. When the gate fails, return a measurement or query specification instead of a synthetic number.

Never infer private cohort membership or performance from public product information. Never convert aggregate DAU, MAU, revenue, or transactions into cohort results without fixed membership and compatible age-based outcomes.

## Build Comparable Cohorts

1. Preserve one canonical total view and assign each eligible entity under the frozen assignment rule.
2. Translate calendar timestamps into cohort age using the declared interval and timezone.
3. Calculate only cells mature through the observation cutoff; label incomplete cells `unavailable` or explicitly partial.
4. Show eligible N, outcome N, rate or value, age, and maturity together.
5. Compare the same age and definition across cohort starts, exposures, behaviors, states, or segments.
6. Reconcile mutually exclusive segment counts to the canonical total and preserve an unknown bucket.
7. Decompose aggregate movement into composition change and within-group change before nominating a mechanism.

Keep exact, bounded, rolling, bracket, opportunity, survival, cumulative-value, and period-value definitions distinct. Keep user, workspace, account, product, order, subscription, revenue, contribution, and cost views distinct unless explicit joins support linked tables.

## Interpret And Route

A cohort table establishes what changed for a defined group at a defined age. It does not establish why the result changed or what an intervention caused. Preserve seasonality, customer mix, concurrent changes, instrumentation, product version, selection, regression to the mean, and survivorship as alternatives.

Route causal validation to `experiment-design`; first-value mechanisms to `activation`; recurring value, churn, resurrection, GRR, or NRR to `retention`; pricing, revenue, contribution, payback, or LTV policy to `monetization`; lifecycle copy to `lifecycle-marketing`; and broader constraint selection to `growth-diagnosis`.

## Deliver In Order

Return:

1. mode, decision, owner, and analysis boundary;
2. cohort contract and definition version;
3. source, evidence, data-quality, privacy, and reconciliation ledger;
4. canonical cohort matrix or calculation-ready specification;
5. segment, exposure, behavior, or state comparisons with maturity;
6. mix and within-group decomposition where supported;
7. findings, contradictory evidence, alternatives, and causal boundary;
8. measurement, validation, owner, and capability handoffs;
9. Playbook references and external-action boundary.

For China work, keep market, language, locale, timezone, product surface, identity, payment, channel, consent, and data availability separate. Do not infer WeChat, Mini Program, WeCom, Alipay, app-store, CRM, analytics, or cross-system identity conditions from market or language.

Analysis authorizes local artifacts only. Do not access accounts, query production systems, export customer data, alter identities or events, rewrite dashboards, launch experiments, send messages, change spend, modify customer state, or deploy without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, entity, eligibility, assignment, start, outcome, denominator, interval, cutoff, timezone, maturity, identity, version, source, and privacy boundary are explicit; counts reconcile or discrepancies remain visible; rates include numerators and denominators; immature cells remain unavailable; comparisons use equal ages and compatible definitions; canonical totals accompany cuts; mix is separated from within-group change; causal language follows evidence; handoffs do not duplicate adjacent Skills; Playbook sources are pinned; and no external action occurred.
