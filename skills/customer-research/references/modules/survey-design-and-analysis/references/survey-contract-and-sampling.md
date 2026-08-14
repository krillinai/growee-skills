# Survey Contract And Sampling

## Decision And Construct Contract

Start with a decision that could change, not a preferred question or platform. Record:

| Field | Required boundary |
| --- | --- |
| Decision | Choice, owner, alternatives, date, consequence, reversibility, and evidence threshold |
| Construct | Included meaning, excluded meaning, adjacent constructs, operational definition, and known measurement risks |
| Estimand | Quantity, population, unit, period, instrument, aggregation, and comparison to estimate |
| Intended use | Descriptive, diagnostic, screening, comparison, tracking, modeling input, or decision support |
| Evidence | Supplied sources, versions, access, cutoff, evidence state, contradiction, and limitation |

Use one primary construct per decision-relevant item. Separate attitude, awareness, recall, satisfaction, effort, intention, recommendation, preference, reported behavior, and observed behavior. A respondent's answer verifies what was recorded under a declared question; it does not by itself verify the underlying event, cause, durability, or population prevalence.

Do not infer the construct from a metric label. Define the exact reference object, event, timeframe, respondent role, experience threshold, scale, and decision rule. Record proxy, criterion, convergent, discriminant, test-retest, and measurement-equivalence evidence when the consequence requires them.

## Population, Frame, And Unit

Keep these sets separate:

| Set | Definition |
| --- | --- |
| Target population | The entities to which the estimate is intended to apply |
| Sampling frame | The source from which eligible units can actually be selected |
| Selected sample | Units selected under the declared design before contact |
| Addressable sample | Selected units with a valid permitted contact route |
| Invited sample | Units sent an invitation under the fielding rules |
| Respondent sample | Units that supply any response |
| Qualified sample | Respondents meeting declared eligibility and quality rules |
| Analyzed sample | Qualified responses included for a specified estimate |

Record whether the unit is a person, user, account, household, buyer, administrator, employee, partner, transaction, case, market, or another entity. Preserve one-to-many identities, shared accounts, repeated respondents, duplicate contacts, proxy respondents, and unknown linkage. Do not count devices, addresses, sessions, and people interchangeably.

Define inclusion, exclusion, experience, tenure, exposure, geography, product, plan, role, lifecycle state, accessibility, language, and age boundaries before selection. Never exclude a valid member merely because the response would be unfavorable.

## Sampling Design And Coverage

Choose a design appropriate to the estimand and available frame:

| Design | Required evidence | Main limitation to expose |
| --- | --- | --- |
| Census attempt | Complete eligible frame, deduplication, contact permission, and nonresponse | A census invitation is not a census result |
| Simple or systematic probability | Known frame and inclusion mechanism | Undercoverage and nonresponse remain |
| Stratified | Declared strata, allocation, inclusion probability, and analysis weights | Empty or sparse strata and incompatible controls |
| Cluster or multistage | Stage units, probabilities, within-cluster selection, and clustering | Design effect and correlated response |
| Quota | Target cells, source, recruitment process, and within-cell selection | Quotas do not make nonprobability selection random |
| Purposive | Decision-relevant criteria, selector, variation sought, and exclusions | Composition supports discovery, not population prevalence |
| Panel | Panel source, recruitment, refresh, conditioning, attrition, and eligibility | Panel members can differ from the target population |
| Convenience or intercept | Exact source, exposure, timing, and self-selection | Results apply only to the observed bounded sample |
| Open link | Placement, reachable audience, forwarding, eligibility, duplication, and exposure | Inclusion and response probabilities are unknown |

Create a coverage ledger for undercoverage, overcoverage, duplicates, ineligible records, unreachable units, mode exclusion, language exclusion, accessibility exclusion, platform membership, survivorship, customer-only selection, active-user selection, and gatekeeper selection. State direction of possible bias only when supported; otherwise record it as unknown.

Do not label a follower, newsletter, power-user, employee, friend, open-link, or other convenience sample random or representative because it is large, balanced on a few quotas, collected from many countries, or weighted after collection. Representativeness is always relative to a defined population, frame, selection and response process, variables, period, and use. Preserve nonrespondents, unreachable units, refusals, declined participants, missing cells, and unavailable populations.

Report respondent composition, frame coverage, selection, nonresponse, and transfer limitations with every estimate. For a broader decision, specify the probability sample, frame repair, oversample, follow-up, nonresponse study, behavioral comparison, replication, or other validation required; do not invent a population margin of error or response probability.

## Sample Size And Precision

Do not choose sample size from a universal table alone. Record the primary estimand, acceptable decision error, confidence or posterior requirement, expected variability, baseline or prevalence assumption, minimum meaningful difference when comparing, allocation ratio, design effect, expected completion and eligibility, finite-population correction when material, weighting loss, subgroup minimums, repeated-measure correlation, attrition, and privacy suppression.

Use the largest requirement among primary decisions, then test feasibility. Distinguish:

- precision for one estimate;
- power for one prespecified comparison;
- minimum cells for safe reporting;
- qualitative cognitive-test or coding coverage;
- operational invitation volume after eligibility, delivery, start, and completion loss.

If a required input is missing, show scenarios and the exact evidence needed. Do not invent an expected response rate, effect size, population total, design effect, or certainty. A large raw `n` cannot repair frame error, nonresponse, construct error, fraud, or incompatible pooling.

## Recruitment, Consent, And Incentives

Record frame source, selector, recruitment channel, permission basis, sponsor, sender, invitation copy and version, eligibility disclosure, screener, frequency, reminders, suppression, field dates, time burden, support, accessibility, refusal, skip, withdrawal, and expiry. Keep research participation separate from service eligibility, employment, pricing, support, and product access.

Use minimum-necessary personal and sensitive data. Explain purpose, optionality, use, recipients, retention, correction, contact, and withdrawal in language appropriate to the population. Do not treat delivery, opening, starting, silence, or continued service use as consent.

For incentives, record eligibility, amount or range, currency, timing, owner, fulfillment, tax or platform uncertainty, refusal handling, fraud controls, and distortion risk. Never condition a reward on positive answers or disclosure beyond the necessary research task.

## Response-State Reconciliation

Reconcile counts in this order:

`frame -> eligible frame -> selected -> addressable -> invited -> delivered -> opened -> started -> eligible -> consented -> partial -> complete -> quality reviewed -> excluded or included -> analyzed`

Define each state, identity key, timestamp, mutually exclusive disposition, and residual. Open and consent may be unavailable depending on mode; do not infer them. A completion rate, response rate, cooperation rate, item response rate, eligibility rate, and analysis inclusion rate need separate numerators and denominators.

## Boundary With Customer Research

Use `customer-research` when the decision needs interviews, observation, diaries, support or review synthesis, mixed methods, participant discovery, or broader voice-of-customer work. Survey Design and Analysis owns the survey-specific construct, sample, instrument, fielding and statistical contract. A survey can be one method inside a broader research plan without absorbing that plan.
