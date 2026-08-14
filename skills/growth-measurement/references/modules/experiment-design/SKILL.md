---
name: experiment-design
description: Use when a product, growth, marketing, pricing, lifecycle, content, channel, or operational decision needs an experiment plan, A/B test review, causal-design choice, power and maturation specification, experiment quality audit, or evidence-bounded result interpretation and decision rule.
---

# Experiment Design

Turn an important uncertainty into a trustworthy evidence design and an accountable decision. Use randomized experiments only when assignment, exposure, outcomes, ethics, reversibility, traffic, maturation, and interference make them appropriate; otherwise choose the strongest bounded alternative without relabeling it an experiment.

Read [experiment-contract.md](references/experiment-contract.md) for intake, evidence, privacy, and required fields. Read [design-methods.md](references/design-methods.md) before choosing units, assignment, metrics, power inputs, alternatives, or quality controls. Read [readout-methods.md](references/readout-methods.md) before interpreting results, segments, proxies, guardrails, or uncertainty. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `design` | Decide whether and how to run a controlled experiment or alternative evidence design |
| `review` | Audit a proposed or running design for decision fit, ethics, assignment, exposure, metrics, power, interference, and quality risks |
| `readout` | Interpret supplied mature results against the frozen specification and make a bounded decision recommendation |

Name one primary mode. Keep preregistered, amended, and exploratory analysis visibly separate.

## Gate The Experiment

Record the decision, owner, important uncertainty, mechanism, reversibility, legal and ethical boundary, eligible population, controllable intervention, measurable outcome, maturation horizon, traffic or sample constraints, and interference risk.

Do not default to an A/B test when a severe defect should be fixed, exposure cannot be controlled, the action is unethical or irreversible, traffic cannot support the required sensitivity, the outcome matures too late for the decision, or spillovers dominate. Recommend qualitative research, offline evaluation, simulation, bounded pilot, switchback, interrupted time series, difference-in-differences, regression discontinuity, or matched comparison only when its assumptions fit.

## Freeze The Contract Before Exposure

Specify eligibility; identity; randomization unit; assignment ratio and mechanism; exposure rule; control and treatment; OEC; primary outcome; diagnostics; guardrails; invariants; long-term validation; minimum meaningful effect; power inputs; expected exclusions; observation and maturation windows; interference; analysis population; missing-data rules; multiple-comparison and sequential rules; decision states; rollback; owner; and downstream follow-up.

Do not invent a minimum effect, baseline, variance, intracluster correlation, sample size, duration, power, result, or causal claim. If required inputs are unavailable, return the exact calculation specification and evidence request.

## Protect Experiment Integrity

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder-only statement may use signal status `reported signal` with a blank evidence state.

Validate eligibility, assignment, exposure, identity, exclusions, logging, metric computation, data freshness, invariants, maturation, and sample-ratio mismatch before interpreting effects. Preserve original assignment for intent-to-treat analysis. Do not condition the primary analysis on treatment-driven exposure, completion, survival, or post-assignment behavior.

Treat changes made after exposure begins as amendments. Unless the frozen plan permits them, label resulting analysis exploratory. Do not choose metrics, segments, exclusions, windows, or stopping points after seeing favorable results.

## Read Results As Decisions

Report sample counts, metric definitions, treatment and control values, absolute and relative effects where valid, uncertainty intervals, quality checks, guardrails, practical threshold, population boundary, maturity, and assumptions.

Statistical significance is not business value. Non-significance is not proof of no effect or equivalence. A surprising effect triggers denominator, logging, outlier, SRM, novelty, multiple-testing, and implementation checks before celebration.

Use predefined result states: meaningful benefit with guardrails passing; harm or guardrail breach; directionally useful but below threshold; practically flat under a valid equivalence or harm boundary; or inconclusive because power, maturity, quality, or assumptions failed. Document overrides and unresolved uncertainty.

## Route Domain Work

Experiment Design owns causal design and readout integrity, not the domain intervention. Route first-value questions to `activation`, recurring value to `retention`, commercial design to `monetization`, lifecycle messages to `lifecycle-marketing`, copy to `copywriting`, campaign strategy to `acquisition-strategy` when available, and broad constraint selection to `growth-diagnosis`.

## Deliver In Order

Return:

1. mode, decision, owner, and experiment gate;
2. evidence and assumption ledger;
3. frozen experiment or alternative-design contract;
4. metric dictionary and data-quality checks;
5. power, duration, and maturation specification;
6. implementation, interference, privacy, and risk controls;
7. analysis or readout plan;
8. decision rules, rollback, follow-up, and handoffs;
9. Playbook references and external-action boundary.

For China work, keep market, language, locale, product surface, identity, channel, platform, payment, consent, data handling, and applicable review separate. Do not infer platform availability, compliance, experiment permissibility, or data conditions from market or language.

Design, review, and readout authorize local artifacts only. Do not access production systems, assign real users, change exposure, launch or stop experiments, alter traffic, spend, prices, messages, product behavior, or data pipelines, or publish decisions without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, mechanism, eligibility, unit, assignment, exposure, variants, metrics, effect threshold, power inputs, maturity, exclusions, interference, quality checks, analysis population, and decision rules are explicit; preregistered and exploratory work are separated; SRM and guardrails are resolved before interpretation; uncertainty and tested-population limits remain visible; no causal language exceeds the design; Playbook sources are pinned; and no external action occurred.
