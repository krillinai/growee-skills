# Analysis, Governance, And Actions

## Preserve Raw And Derived States

Keep immutable raw responses separate from labeled, redacted, translated, recoded, scored, weighted, modeled, excluded, and reporting datasets. Record dataset ID and version, instrument version, extraction cutoff, transformation rule, code or query version, author, reviewer, affected rows, reason, and correction lineage.

Never overwrite raw answers, backfill a baseline, silently change scoring, or delete unfavorable results. A correction creates a new version and preserves the superseded output, downstream consumers, notification need, and residual effect.

## Missingness And Denominators

Preserve at least: structurally not shown, optional skip, item nonresponse, refusal, `don't know`, `not applicable`, breakoff, invalid, suppressed, unavailable, and valid zero. Do not replace any of these with zero or dissatisfaction.

For every estimate record item ID and version, eligible population, displayed count, valid-response rule, included partials, missingness states, exclusions, unweighted denominator, weighted denominator when used, and reconciliation residual. Analyze missingness by relevant path, item, source, device, language, market, role, and lifecycle state without inventing reasons.

Define partial-response inclusion per construct and analysis before outcome selection. A respondent can be included for one estimate and excluded from another when eligibility and observed items differ. Report the rule and denominator each time.

## Weighting Contract

Do not weight without a defensible target and compatible variables. Record:

- estimand, target population, sample design, inclusion model, and weighting purpose;
- source, owner, version, period, and quality of control totals or probabilities;
- variables, coding, missingness, compatibility, and relationship to selection or outcome;
- design, nonresponse, poststratification, raking, calibration, propensity, trimming, pooling, and normalization choices;
- base and final weights, convergence, empty cells, range, distribution, trimming, design effect, and effective sample size.

Report unweighted and weighted counts and estimates, sensitivity to choices, and residual bias. Do not invent population totals, inclusion probabilities, targets, cells, or weights. Weighting does not repair frame undercoverage, unmeasured selection, construct error, fraudulent responses, incompatible fielding, or all nonresponse bias. When the contract is unavailable or invalid, keep the analysis unweighted and bounded.

## Estimation, Uncertainty, And Multiple Comparisons

Predeclare primary and exploratory estimands, hypotheses, comparisons, subgroups, transformations, minimum cells, uncertainty method, weighting, clustering, repeated measures, interim looks, stopping, and multiplicity handling. Report counts, denominators, estimates, intervals or another appropriate uncertainty representation, design basis, missingness, and limitations.

Address multiple items, outcomes, subgroups, markets, waves, models, thresholds, and looks through predeclaration, adjustment, shrinkage, validation, or explicit exploratory labels. Preserve unfavorable, null, contradictory, harmful, unstable, and unavailable results.

Do not equate statistical significance with practical value, `p > 0.05` with no difference, a confidence interval with the probability that the fixed parameter lies inside it, or two decimal places with population precision. Suppress or pool sparse cells only under declared, privacy-safe, decision-compatible rules. Require replication or additional evidence before acting on a post-hoc favorable subgroup.

## Named Instruments And Domain Boundaries

### NPS, CSAT, And CES

Keep recommendation, satisfaction, effort, loyalty, referral, retention, and revenue distinct. Record exact wording, scale, anchors, reference event, eligibility, timing, product, market, language, mode, instrument version, and item denominator. Derive promoter, passive, detractor, satisfied, or effort categories only under the specified instrument.

Check frame, nonresponse, tenure, lifecycle, channel, market, product, language, and case mix before comparison. Keep open-text reasons attributable and separate from the numeric score. Declared recommendation is not observed referral; one response is not durable loyalty; score movement does not cause retention or revenue. Route customer experience mechanisms to `customer-research`, metrics to `growth-metrics-design`, retention to `retention`, referral to `growth-loop-design`, and causal validation to `experiment-design`.

### Must-Have, Pricing, And Choice Surveys

Do not certify PMF from a very-disappointed threshold or declare an optimal price, demand forecast, or market share from survey output alone.

For a must-have survey, check core-value exposure, eligibility, segment, role, tenure, recruitment, response process, wording, reasons, survivorship, nonresponse, retention, willingness to pay, and economics. Route fit interpretation to `product-market-fit-assessment`.

For Van Westendorp, check all four items, currency, package and product stimulus, price range, logical consistency, frame, sample, weighting, sparse regions, and uncertainty. For Gabor-Granger, check package stimulus, tested prices, order, purchase context, response scale, frame, sample, weighting, and stated-versus-observed demand. For conjoint or discrete choice, check alternatives, attributes, levels, tasks, randomization, prohibitions, holdouts, model, uncertainty, and external validity. Route strategy to `monetization`, economics to `monetization`, behavioral validation to authorized experiments, and forecasting to `growth-forecasting`.

Preserve instrument result, domain interpretation, observed behavior, economics, forecast, decision, and causal effect as separate records.

## Open-Text Coding

Preserve response ID, exact text, item, language, respondent context, instrument version, consent boundary, redaction, translation, translator or method, and uncertainty. Keep raw text, redacted text, translation, code, theme, interpretation, model output, and decision implication separate.

Define a codebook with code ID, definition, inclusion, exclusion, examples, counterexamples, multi-code, unknown, disagreement, reviewer, revision, and audit rules. Double-code or adjudicate where consequence warrants it. Preserve negative, contradictory, rare, harmful, ambiguous, uncodable, and unavailable responses.

Never invent, improve, combine, or attribute a quote not supplied verbatim. Treat automated sentiment, emotion, intent, toxicity, or theme labels as fallible model outputs, not respondent facts. Phrase or theme counts in selected open text do not establish population prevalence. Research consent does not authorize identifiable publication or customer proof; route public proof to `content-strategy` under separate permission.

## Longitudinal And Causal Boundaries

Separate repeated cross-sections, cohorts, panels, pre-post studies, interrupted time series, and randomized experiments. For comparison, freeze population, frame, sample, mode, instrument, scale, language, market, product, field timing, weights, analysis, and source versions. Identify new, repeat, refreshed, missing, attrited, ineligible, exposed, unexposed, and unmatched respondents.

Preserve panel conditioning, survivorship, attrition, mode, seasonality, mix, product, channel, policy, competitor, and concurrent-change alternatives. Do not compare changing respondent mixes as a panel or backfill a baseline after seeing outcomes.

Survey movement and intention do not prove intervention effect, retention, demand, or revenue. A causal claim requires a declared intervention, eligible unit, assignment or credible counterfactual, access, exposure, contamination, outcome, maturity, guardrails, missingness, and analysis. Route design and effect estimation to `experiment-design`, cohort maturity to `retention`, and forecasts to `growth-forecasting`.

## Privacy, Fairness, And Market Transfer

Minimize collection, linkage, retention, access, exports, and reporting of personal or sensitive data. Separate anonymous, pseudonymous, confidential, and identifiable states. Record purpose, lawful and ethical authority, consent, access, encryption, retention, deletion, correction, incident response, reporting thresholds, and downstream consumers using current direct sources and accountable specialists.

Do not collect or expose health, income, precise location, protected traits, named ratings, or other consequential data without a necessary authorized purpose and controls. Do not use survey responses or inferred labels to score or rank named people for employment, pricing, service, credit, insurance, safety, or another consequential decision.

For China and every market transfer, separate market, language, locale, script, currency, legal entity, product, platform, channel, device, frame, recruitment, incentive, consent, privacy, retention, owner, and approval. Do not copy another market's instrument, sample, benchmark, weight, privacy terms, platform, or conclusion. Require current direct sources and locally accountable research, privacy, legal, security, and domain review. Do not make legal or compliance conclusions.

## Approval-Ready External Actions

Specify, but do not execute, survey-platform configuration, sample export, contact, invitation, reminder, incentive, fielding, pause, close, analysis, reporting, correction, dashboard, and archive requests. Each request needs object and version, scope, source decision, owner, reviewer, approver, authorizer, executor, verifier, access, privacy, dry run, test, monitoring, stop, rollback, correction, completion proof, expiry, and residual obligation.

Do not log in, upload contacts, configure a live survey, send invitations, issue rewards, analyze unavailable responses, update dashboards, contact participants, or imply that any action or outcome occurred.
