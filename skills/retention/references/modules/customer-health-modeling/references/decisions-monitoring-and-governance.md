# Decisions, Monitoring, And Governance

## Decision Interface

For every model use record:

| Field | Required content |
| --- | --- |
| Decision | Permissible question, alternatives and excluded uses |
| Population | Eligible entity, lifecycle, product, market, horizon and exclusions |
| Signal | Model and threshold version, score or probability, uncertainty and reason codes |
| Capacity | Receiving role, review volume, service capacity, timing and opportunity cost |
| Protection | Suppressions, blockers, abstention, customer choice, accessibility and guardrails |
| Control | Human review, override, correction, appeal, audit, expiry and fallback |
| Learning | Action exposure, later outcome, causal boundary, feedback and re-read |

Keep signal, recommendation, decision, approval, authorization, action and outcome separate. A green score cannot renew or expand an account; a red score cannot authorize contact, discount, denial, price change or reduced service.

## Threshold And Capacity Design

Choose a threshold or band only after defining outcome prevalence, calibration, uncertainty, false-positive and false-negative consequence, receiving capacity, action cost, customer effect, expected maturity, review and fallback. Show counts and base rates at each candidate threshold.

Prefer `review`, `monitor`, `abstain`, `not eligible`, `suppressed`, `evidence pending` or outcome-specific language over universal red, amber and green. Do not copy industry thresholds across products, contracts, horizons, markets or decisions.

## Reason Codes And Suppressions

Reason codes must identify observable pre-cutoff evidence, model version, direction, window, source and limitation. They are not causal explanations or customer-facing accusations. Do not expose sensitive attributes, confidential internal opinions or inferred emotions.

Suppress or require accountable review for:

- active incidents, unresolved complaints, security or privacy reviews;
- implementation, migration, training, incomplete access or not-yet-due value opportunities;
- prior decline, do-not-contact, consent, authority or channel restrictions;
- missing, stale, contradictory, immature or out-of-distribution evidence;
- inaccessible or unsupported actions, capacity overflow and service unavailability;
- pricing, renewal, denial, employment or other consequential decisions;
- model drift, source incident, calibration breach or expired version.

Record the eligible owner and evidence required to clear a suppression. Do not silently exclude unfavorable outcomes from validation.

## Monitoring

Monitor by version and outcome horizon:

1. eligible population, hierarchy and lifecycle mix;
2. feature distribution, source coverage, missingness and availability;
3. label prevalence, maturity, delay, censoring and revision;
4. discrimination, calibration, lift, gains and threshold counts;
5. group and market performance, error and evidence coverage;
6. suppressions, abstentions, overrides and reviewer disagreement;
7. action exposure, capacity, customer impact and later outcomes;
8. feedback loops, intervention contamination and policy changes.

Define monitoring window, expected variation, trigger, owner, review, recalibration, refresh, fallback, repair and retirement rules. Never retrain only after complaint or silently change thresholds to preserve performance.

## Version And Change Register

Version customer hierarchy, eligibility, outcome, labels, feature definitions, data vintages, missingness, training population, algorithm, parameters, calibration, thresholds, reason codes, suppressions, decision use, owners and monitoring. Preserve candidate, validation-pending, approved-record, active-record, blocked, superseded and retired states.

Record data, definition, product, price, contract, market, source, model, policy, action and outcome changes. Preserve old predictions, actual outcomes, overrides, misses and decisions. Build a revision bridge rather than rewriting history.

## Original And Expanded Scope

For expansion uses, preserve original product value, adjacent need, new scope, authority, readiness, implementation, support, capacity, commercial state, retained total-customer value and cannibalization. A healthy core account is not automatically ready for every product; one expansion signal does not prove whole-account health. Route strategy and operational use to `customer-expansion-strategy`.

For retention uses, preserve natural opportunity, repeated value, reliability, customer need, contract and lifecycle. A risk prediction does not explain churn. Route diagnosis and intervention design to `retention`.

## Market Transfer

Revalidate customer and contract hierarchy, product value, roles, lifecycle, identity, telemetry, CRM, support, payment, invoice, renewal and churn states, features, labels, prevalence, source availability, model, calibration, threshold, service capacity, privacy, owners and actions in each market.

For China, separate market, legal entity, language, locale, currency, timezone, product, platforms, identity, payment, invoice, data, consent, privacy, support and locally accountable review. Use current direct evidence and local expertise. Translation and currency conversion do not validate transfer. Avoid legal, tax, regulatory, provider, accounting, approval, causal or performance conclusions.

## Privacy, Fairness, And External Actions

Use aggregate, redacted, pseudonymous, minimum-necessary and small-cell-suppressed evidence. Define purpose, authority or consent, access, joins, aggregation, retention, deletion, correction, audit, fairness, accessibility, dissent, appeal and independent review.

Do not use direct identifiers, private messages, recordings, keystrokes, precise locations, health, protected traits, compensation, employee reviews, payment details, private customer content or full histories when bounded evidence suffices. Do not score or rank named users, customers or employees; infer vulnerability; deny service; personalize price; pressure sales; set workloads; or make employment, credit, insurance, health, housing or similar decisions.

The default deliverable is a local specification, audit, validation, monitoring record or approval-ready handoff. Do not access systems, export data, deploy models, score or route accounts, trigger messages, alter service, renewals, prices or records, publish dashboards or claim improvement.
