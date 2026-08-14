# Experiment Contract

## Required Decision Context

Capture these fields independently:

- decision, decision date, owner, and actions for positive, negative, harmful, flat, and inconclusive results;
- important uncertainty, mechanism, evidence, and credible alternatives;
- legal, ethical, privacy, accessibility, fairness, customer-harm, and reversibility boundary;
- eligible population, entry state, market, locale, product surface, and tested population limits;
- randomization or assignment unit, ratio, method, salt or version where available, and allocation owner;
- exposure rule, first possible exposure, contamination risks, and noncompliance handling;
- control, treatment, implementation dependencies, and rollback state;
- OEC, primary outcome, diagnostics, guardrails, invariants, and long-term outcome;
- minimum meaningful effect and whether it is absolute, relative, economic, or non-inferiority based;
- baseline or variance, allocation, alpha, power, clustering, expected exclusions, and repeated-look assumptions;
- observation, ramp, stabilization, maturation, follow-up, and stopping windows;
- identity, deduplication, missing-data, bot, internal-user, and exclusion rules;
- interference, spillover, novelty, seasonality, carryover, and concurrent-change risks;
- analysis population, estimator, covariates, multiple-comparison rules, segment plan, and uncertainty interval;
- source IDs, owners, capture dates, definitions, populations, and limitations.

Public product information can support a draft mechanism, eligibility model, risk inventory, and evidence-design specification. It cannot establish private traffic, baseline, variance, assignment quality, exposure, outcomes, power, SRM, or causal effects.

## Evidence States

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. Use `reported signal` only for attributable stakeholder statements without inspectable supporting evidence.

Keep assumptions explicit and testable. A design assumption is not verified merely because the experiment requires it.

## Metric Dictionary

For every metric include name, role, decision, entity, eligibility, numerator, denominator, event definition, direction, window, cutoff, maturity, source, missingness, sensitivity, expected mechanism, and failure condition. For composite OECs, document components, weights, trade-offs, and veto rules.

Do not redefine metrics after results are visible. Preserve both the frozen definition and any amended or exploratory definition.

## Privacy And Data Minimization

Use aggregate or pseudonymous records whenever direct identity is unnecessary. Exclude names, raw email addresses, phone numbers, credentials, signed links, private payloads, unrelated histories, and sensitive attributes not required by the design. Record purpose, access scope, retention scope, and approved joins. Do not claim deletion, assignment, exposure, suppression, or rollback already occurred.

## Output Boundary

If a required gate fails, return the known contract, exact missing inputs, strongest feasible evidence alternative, assumptions, risks, and next decision. Do not fabricate a sample size, duration, effect, statistical threshold, or launch-ready state.
