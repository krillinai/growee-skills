---
name: survey-design-and-analysis
description: Use when a growth, product, customer, market, employee, or partner decision needs a survey or questionnaire designed, audited, localized, piloted, fielded, analyzed, weighted, compared over time, or governed; when response quality, missingness, denominators, uncertainty, NPS, CSAT, CES, open text, or stated-preference evidence needs review; or when survey results risk being treated as representative, behavioral, causal, or decision-complete without support.
---

# Survey Design And Analysis

Turn a decision into a traceable survey contract, instrument, fielding specification, analysis, and bounded interpretation. Treat a survey as a measurement process with selection, response, and construct limits, not as a form, a representative sample by default, a source of exact motives, or proof of behavior and causality.

Read [survey-contract-and-sampling.md](references/survey-contract-and-sampling.md) before defining constructs, populations, frames, samples, recruitment, consent, incentives, or response states. Read [instrument-fielding-and-quality.md](references/instrument-fielding-and-quality.md) before writing questions, options, scales, logic, localization, cognitive tests, pilots, invitations, or quality rules. Read [analysis-governance-and-actions.md](references/analysis-governance-and-actions.md) before cleaning, weighting, estimating, comparing, coding open text, interpreting domain instruments, transferring across markets, or specifying external actions. Follow [output-contract.md](references/output-contract.md) for every delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `design` | Define a decision, construct, sample, instrument, fielding plan, analysis plan, and acceptance gates |
| `audit` | Inspect an existing survey, response dataset, report, or recurring program for validity, comparability, risk, and missing evidence |
| `analysis` | Analyze supplied responses under explicit population, instrument, quality, denominator, weighting, uncertainty, and privacy contracts |
| `comparison` | Compare markets, segments, waves, panels, instruments, or interventions only after compatibility and maturity checks |

Name one primary mode. State the artifact as `draft`, `evidence-pending`, `review-ready`, `fielding-ready`, `fielding-pending`, `analysis-ready`, `decision-ready`, `approved-record`, `correction-required`, `superseded`, or `expired`. State does not prove approval, contact, consent, fielding, participation, analysis, decision, action, outcome, or impact.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. An attributable statement without inspectable support may remain a `reported signal` with no evidence state. Keep source, response, derived value, interpretation, recommendation, decision, approval, action, observed outcome, and causal estimate separate. Never invent respondents, responses, quotes, samples, weights, benchmarks, significance, owners, approvals, execution, or results.

Respond in the user's requested language; use Simplified Chinese when requested. Request only missing evidence that can change the construct, instrument, sample, fielding, analysis, interpretation, or decision.

## Freeze The Survey Contract

Record survey ID and version, mode and state, decision and owner, intended use and consequence, construct and operational definition, estimand, target population, sampling frame and unit, eligibility and exclusions, market and language, product and lifecycle context, recruitment and incentive, consent and privacy, mode and device, field period, instrument and analysis versions, source cutoff, reviewers, review and expiry, and external-action boundary.

Use the smallest survey unit whose construct, population, frame, instrument, fielding process, and decision can be interpreted coherently. Split surveys or report variants when role, product, market, language, mode, scale, stimulus, recruitment, eligibility, response process, or intended use differs materially. Do not pool incompatible units to manufacture precision.

## Design From Construct To Sample

Define what the construct includes, excludes, and could be confused with before writing questions. Map every item to a construct, decision use, eligible respondent, recall or reference period, analysis role, and removal consequence. One item cannot silently stand in for satisfaction, loyalty, recommendation, effort, behavior, retention, or revenue.

Reject omnibus truth scores and unsupported weights across incompatible constructs. Test whether a survey can answer each question before designing an item. Keep exploratory discovery separate from prevalence estimation and confirmatory measurement; narrow the survey or return an evidence-acquisition plan when the decision or construct is unresolved.

Specify target population separately from available contacts, sampling frame, selected sample, invited sample, respondents, qualified completes, and analyzed sample. Diagnose frame undercoverage, overcoverage, duplicate units, selection, mode, nonresponse, survivorship, incentive, and accessibility risks. A convenience, customer-only, active-user, community, email, or platform sample remains bounded even when large.

Set sample-size or precision requirements only from a declared estimand, decision threshold, expected variability, design, subgroup needs, expected response, finite population when relevant, weighting or clustering effect, attrition, and error tolerance. If inputs are unavailable, return a range or evidence request rather than a fabricated target.

## Build And Test The Instrument

Write neutral, singular, answerable questions with an explicit timeframe and reference object. Provide exhaustive, non-overlapping response options when the construct permits; distinguish `none`, valid zero, `not applicable`, `don't know`, `prefer not to answer`, skip, and not shown. Preserve scale direction, labels, anchors, comparability, and version.

Use order, randomization, branching, piping, validation, and termination only when they protect the construct and respondent experience. Never pipe sensitive answers unnecessarily, expose hidden data, randomize an inherently ordered construct, or let routing create undocumented denominators.

Require cognitive, linguistic, accessibility, device, pilot, and soft-launch evidence proportionate to consequence. Literal translation is not measurement equivalence. Preserve every tested, approved, fielded, corrected, and superseded instrument version.

## Field And Qualify Responses

Define sponsor, purpose, permissioned channel, invitation, sender, eligibility, identity control, reminder cadence, suppression, field period, support, incentive, consent, withdrawal, privacy, retention, correction, and incident handling. Separate addressable, selected, invited, delivered, opened, started, eligible, consented, partial, complete, excluded, and analyzed states. Delivery, opening, starting, silence, or product use is not consent or participation.

Predeclare quality checks and dispositions before viewing favorable outcomes. Preserve raw records and reversible derived datasets. Use response speed, straightlining, consistency, attention checks, duplicate, bot, fraud, open-text, and breakoff evidence in context; never exclude a respondent because the answer is negative or inconvenient.

## Analyze Without Overclaiming

Preserve every response and missingness state. Define item eligibility, exposure, valid response, inclusion, denominator, weighting, uncertainty, comparison, and multiplicity rules before selecting results. Show counts with rates, unweighted with weighted estimates, diagnostics, sparse cells, effective sample, sensitivity, counterevidence, and limitations.

Keep NPS, CSAT, CES, must-have surveys, Van Westendorp, Gabor-Granger, conjoint, and other stated-preference instruments method-specific. Survey Design and Analysis audits their measurement and analysis integrity; route product-market fit, pricing, customer experience, retention, referral, forecasting, economics, or causal decisions to their owning Skills.

For open text, preserve verbatim source, language, translation, redaction, code, theme, disagreement, and consent. Do not convert selected comments into prevalence, model labels into facts about respondents, or research permission into public customer-proof permission.

## Coordinate Specialist Work

Route broad multi-method, brand, churn, product, and experience research to `customer-research` and accountable domain specialists; segments and frames to `positioning`; metric contracts to `growth-metrics-design`; PMF interpretation to `product-market-fit-assessment`; pricing instruments and commercial decisions to `monetization`; cohorts to `retention`; retention and referral mechanisms to `retention` and `growth-loop-design`; forecasts to `growth-forecasting`; experiments and causal claims to `experiment-design`; behavioral instrumentation to `tracking-plan`; employee research and consequential performance decisions to authorized people-research, HR, privacy, legal, and fairness owners; and implementation to separately authorized owners.

This Skill owns the survey decision and construct contract, population and sampling boundary, questionnaire, fielding specification, response-state reconciliation, quality plan, missingness, weighting and uncertainty audit, open-text coding contract, comparison compatibility, reporting, and governance. Routing does not mean specialist analysis, approval, execution, or verification occurred.

## Deliver In Order

Follow [output-contract.md](references/output-contract.md). Return the survey contract and source ledger; population, frame, sample and recruitment; item-purpose map and instrument findings; localization, cognitive, pilot and fielding record; response states and quality dispositions; analysis, weighting, uncertainty, comparisons and open text; interpretation boundaries and specialist handoffs; privacy, version and market governance; approval-ready external actions; pinned sources; and completion record.

## External-Action Boundary

Create and read local artifacts only. Do not access survey, CRM, analytics, product, support, HR, identity, billing, payment, messaging, ad, or cloud systems; upload or export personal data; scrape sources; contact, recruit, invite, remind, reward, exclude, score, rank, or decide for people; launch or close a survey; change an instrument, sample, weight, dataset, dashboard, product, price, policy, or customer state; publish; send; spend; deploy; or claim fielding, participation, analysis, implementation, improvement, or impact without separate task-level authorization and controls.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm survey ID, versions, mode, state, decision, construct, estimand, population, frame, unit, eligibility, sample, recruitment, incentives, consent, privacy, language, locale, mode, instrument, wording, options, scales, logic, accessibility, cognitive testing, pilot, fielding, response states, quality, missingness, denominators, weighting, uncertainty, multiplicity, open text, comparisons, behavioral and causal limits, owners, handoffs, sources, evidence states, corrections, expiry, and action boundary are explicit; selection did not become representativeness; missing did not become zero; self-report did not become behavior; association or movement did not become cause; domain interpretation was not absorbed; and no external action occurred.
