---
name: icp-segmentation
description: Use when a team needs to discover, define, audit, validate, compare, operationalize, govern, or retire customer segments or an Ideal Customer Profile; distinguish markets, accounts, roles, personas, use cases, cohorts, lifecycle states, and propensity scores; create observable eligibility and exclusion rules; compare segment activation, retention, economics, buying paths, or service burden; or design differentiated product and go-to-market paths with privacy and fairness controls.
---

# ICP Segmentation

Group customers only when an observable difference should change a decision. Define an ICP as versioned conditions under which a customer is likely to realize, retain, and economically support intended value, not as a logo wish list or firmographic filter. Start from public or supplied evidence; private analytics, CRM, warehouse, billing, or research data are optional.

Read [segment-contract.md](references/segment-contract.md) before defining units, rules, evidence, overlap, or outputs. Read [discovery-and-validation.md](references/discovery-and-validation.md) before comparing groups, defining an ICP, creating paths, or using a model. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `discover` | Form a small set of decision-relevant segment hypotheses from qualitative, behavioral, buying, value, and economic evidence |
| `define` | Create reproducible Segment Specifications, an ICP Contract, exclusions, identification rules, and path requirements |
| `audit` | Evaluate existing segments, ICPs, scores, routing, or paths for evidence, leakage, overlap, value, complexity, privacy, and fairness |

Name one primary mode and one decision the segmentation must change. If a group changes no action, call it an analytical cut rather than an operating segment.

## Freeze Unit And Decision

Record the decision, owner, product, market, route, time horizon, and review date. Keep market, account or household, role or participant, job or use case, transaction, lifecycle state, cohort, and model score separate. Define user, buyer, payer, admin, approver, supplier, creator, and beneficiary relationships where relevant.

Never mix user, account, transaction, market, or role denominators. Do not call a role or persona an ICP, a mature-outcome cohort a prospective segment, or a propensity score a causal treatment rule.

## Protect Evidence And Classification

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder statement without inspectable support may use signal status `reported signal` with a blank evidence state.

Never invent customer traits, prevalence, sample sizes, segment performance, willingness to pay, retention, economics, identification accuracy, causal lift, or reachable audience. `verified` establishes only what an attributable artifact supports within its population, unit, definition, window, maturity, and date.

Define every segment with an eligibility rule, identification rule available at decision time, exclusions, unknown handling, overlap policy, evidence, counterevidence, owner, version, and review trigger. A segment defined by future renewal may support retrospective analysis but cannot route a new customer unless earlier signals are validated.

## Build Decision-Changing Segments

Segment on differences in problem and job, actual alternatives, ability to realize value, behavior, buying process, route, value and economics, environment, or risk only when the difference changes treatment. Firmographics and demographics can help identify customers but rarely establish fit alone.

For each candidate, connect:

```text
decision -> observable customer condition -> segment rule -> evidence -> differentiated action -> downstream value and guardrails
```

Specify need, fit, repeated value, economics, access, readiness, and exclusion for the ICP. Preserve failure, churn, non-conversion, exceptional service, contradiction, and poor-fit evidence instead of learning only from advocates.

## Validate Before Routing

Compare compatible and equally mature activation, time to value, repeated value, retention or renewal, expansion, contribution, service burden, failure, and trust outcomes. Report rates and absolute volume. Check selection, missingness, overlap, leakage, concentration, changing mix, and definition drift.

Prefer one shared default plus conditional guidance, an assisted path when justified, and explicit exclusions where value cannot be delivered. Add a path only when it changes a real experience and its incremental downstream value can exceed operational, privacy, fairness, and comprehension costs.

For predictive models, freeze target, eligible population, observation and outcome windows, pre-treatment features, calibration, precision, recall, unknowns, group errors, capacity, drift, overrides, and later validation. Prediction of conversion does not show who benefits from treatment.

## Deliver In Order

Return:

1. mode, decision, owner, product, market, unit, horizon, and review date;
2. source, definition, evidence, counterevidence, and data-quality ledger;
3. hierarchy of market, account, role, job, state, cohort, and model concepts;
4. candidate Segment Specifications with observable rules, exclusions, overlap, and unknown handling;
5. ICP Contract covering need, fit, behavior, economics, access, readiness, and exclusion;
6. compatible qualitative, activation, retention, buying, service, and economic comparison;
7. differentiated path, shared default, routing, fallback, and guardrails;
8. validation, classification quality, experiment, governance, and retirement plan;
9. owners, handoffs, Playbook references, and external-action boundary.

Route customer evidence acquisition to `customer-research`, positioning implications to `positioning`, cohort construction to `retention`, primary-constraint selection to `growth-diagnosis`, causal path tests to `experiment-design`, activation paths to `activation`, retention work to `retention`, commercial paths to `monetization`, campaign audiences to `acquisition-strategy`, and permitted one-to-one B2B execution to `sales-enablement`.

For China work, keep market, language, locale, product surface, participant unit, platform, channel, device, app distribution, payment, identity, consent, data access, applicable review, and competitive context separate. Do not infer a platform, payment method, regulatory condition, or customer trait from market or language. Use only decision-necessary sensitive data after appropriate privacy, fairness, legal, and ethical review.

This Skill creates local artifacts only. Do not access private systems, enrich or upload customer lists, score named people or accounts, change CRM routing, contact customers, alter product paths or prices, launch experiments, or claim that a segment was deployed without separate task-level authorization.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, unit, hierarchy, rules, timing, exclusions, unknowns, overlap, evidence, maturity, rates and volume, downstream value, economics, route, paths, classification quality, privacy, fairness, owner, version, and review triggers are explicit; future-outcome leakage is absent; personas and cohorts are not mislabeled as ICPs; model prediction is not treated as causality; and no external action occurred.
