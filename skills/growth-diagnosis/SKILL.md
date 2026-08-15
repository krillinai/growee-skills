---
name: growth-diagnosis
description: Use when work needs to diagnose primary constraints through funnel, anomaly, and maturity analysis, then route an evidence-backed 30-day plan.
---

# Growth Diagnosis

## Maintain Growee Context

At the start, read `.agents/growee-context.md` when it exists and apply [context-contract.md](references/context-contract.md). Reuse compatible product, customer, market, outcome, evidence, and routing facts instead of asking for them again, but surface stale definitions, dates, conflicts, and missing evidence. The file never grants system access or execution authority.

After completing a final diagnosis, create or replace `.agents/growee-context.md` using [growee-context-template.md](assets/growee-context-template.md). Keep it semantically aligned with the canonical diagnosis, exclude credentials and unnecessary personal or row-level data, and do not produce a final-looking context file during triage.

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Funnel Analysis](references/modules/funnel-analysis/SKILL.md)
- [Growth Anomaly Investigation](references/modules/growth-anomaly-investigation/SKILL.md)
- [Growth Maturity Assessment](references/modules/growth-maturity-assessment/SKILL.md)

Turn a growth symptom into one evidence-backed primary constraint, a 30-day decision plan, and an explicit execution route. Diagnose before prescribing tactics.

## Read The Contract

Read [evidence-and-routing.md](references/evidence-and-routing.md) before classifying evidence, setting confidence, working with private inputs, diagnosing China, or choosing an execution route. Read [core-read-only-tools.md](references/core-read-only-tools.md) before using GA4, PostHog, Search Console, HubSpot, Google Ads, or Meta Ads.

Read [output-contract.md](references/output-contract.md) before producing final JSON or Markdown. Read [context-contract.md](references/context-contract.md) before reading or writing `.agents/growee-context.md`. Use [protocol.schema.json](assets/protocol.schema.json) unchanged as the canonical machine-readable contract. Use [playbook-sources.md](references/playbook-sources.md) to cite the relevant Growth Playbook chapter by title and source text.

## Gate The Intake

Start with supplied context. Ask only for gaps that could change the diagnosis or next decision.

Require these fields before final protocol JSON:

- context: product, customer, business model, stage, and diagnosis area;
- outcome: metric definition, baseline, target, segment, and time window;
- evidence: inspectable supporting or contradictory evidence and explicit missing evidence;
- action context: decision window, owners or owner roles, dependencies, and guardrails.

Also establish market and locale before making market-dependent claims. Include them in the readable scope and encode locale alongside geography in the optional schema `context.market` string.

If any schema-required fact is unknown, stay in `triage`; preserve a user-declared area only as the candidate path. Return a bounded intake or evidence-acquisition plan; do not emit final protocol JSON. Never use `TBD`, `Unknown`, zero, an empty array, a made-up date, or an invented label merely to satisfy the schema.

Public evidence is sufficient to begin. Private data is an optional enhancement, not a prerequisite. Do not repeatedly request access the user has declined.

## Select One Mode

Use `triage` only before enough evidence exists to choose a schema diagnosis area. For a final diagnosis, select exactly one of these modes:

| Mode | Use when the target outcome is limited by | First checks |
| --- | --- | --- |
| `acquisition` | Qualified demand, reach, channel scale, or acquisition economics | Qualified and retained demand by channel, audience, promise, entry point, market, and cohort |
| `activation` | Reaching first value or a qualified next action | Intent, eligibility, Setup/Aha/Habit events, highest-loss transition, retained activation |
| `retention` | Return, repeated value, depth, resurrection, or expansion | Natural usage interval, cohort shape, activation path, recurring value, reliability |
| `monetization` | Healthy retained revenue, conversion, expansion, margin, or payback | User/payer/beneficiary roles, retained value, packaging, price, payment friction, economics |
| `growth-loops` | Participation, propagation, recipient value, cycle speed, or loop closure | Input, participant, payload, recipient, conversion, retention, incrementality, harms |
| `growth-system` | Consistent measurement, prioritization, execution, decisions, or learning | Outcome ownership, definitions, data quality, decision rights, dependencies, result reuse |

Serialize the last two modes as the schema enum values `growth_loops` and `growth_system`. Do not inflate a bounded area request into a full-company review. If several areas are plausible, use triage to find the outcome nearest the current constraint.

## Establish The Evidence Boundary

1. Declare product, customer, business model, stage, market, locale, segment, window, source inventory, and access limits.
2. Start with dated, inspectable public artifacts. Use lawful, bounded, read-only collection.
3. Accept private artifacts as verified only when attribution is sufficient under [evidence-and-routing.md](references/evidence-and-routing.md).
4. Label every working-ledger item exactly `verified`, `inferred`, `unavailable`, `not applicable`, or `reported signal`.
5. Preserve source identifiers, definitions, sample or population, segment, period, values, and quality limitations.
6. Surface disagreements. Do not average incompatible definitions or discard contradictory evidence.

When the user explicitly authorizes a named core source and a capable read-only path exists, collect only the bounded aggregate evidence allowed by [core-read-only-tools.md](references/core-read-only-tools.md). If access, authorization, or minimum scope is missing, request a bounded export or keep the evidence unavailable. Never treat a connected source as permission for writes, persistent sync, broader collection, or cross-system identity joins.

Do not invent data, benchmarks, causal claims, source access, metric definitions, or results. A public observation can verify what is visible; it cannot verify a private funnel, motive, or business effect.

Treat China as a first-class market context when relevant. Establish locale, channel and platform availability, app distribution, payments, identity or login dependencies, content and advertising rules, data handling, and sector-specific regulation from current sources. Never infer that a service is available, blocked, compliant, or effective from team location, domain, language, or general memory.

## Select The Constraint

Describe the symptom separately from the mechanism that could cause it. Compare candidates by outcome impact, evidence strength, reach, controllability within the decision window, learning value, and risk. These are judgment dimensions, not a numeric scoring model.

Name exactly one primary constraint only when the evidence supports selection. Record every plausible alternative with the evidence or priority reason it is not primary. If evidence cannot distinguish candidates, remain in triage and make the discriminating evidence request the immediate action.

Set the schema-required confidence value conservatively from `0` to `1`. Explain it with named supporting, contradictory, and missing evidence. Lower confidence for definition conflicts, small or biased samples, missing segments, weak attribution, stale sources, or untested mechanisms. Reject user-supplied confidence that evidence does not support. Do not output any other numeric growth, opportunity, or priority score unless a user-supplied metric or the schema requires it.

## Build The 30-Day Decision Plan

Order evidence acquisition before actions that depend on it. For every priority action include:

- the smallest action that can change a decision within 30 days;
- an accountable owner or explicit owner role;
- a real decision date inside the declared window;
- dependencies, success signal, and customer, trust, regulatory, operational, and economic guardrails;
- an execution route.

Make experiments decision-oriented. State a mechanism-based hypothesis, intervention or evidence-gathering test, primary metric, owner, duration, guardrails, and a decision rule that says what result will cause the team to ship, stop, iterate, collect more evidence, or change the diagnosis. Do not promise uplift.

## Route Execution

Choose the lowest sufficient route: `self_serve`, `growth_skills`, or `clawee_enterprise`. A mixed plan may label each action with its route; set the schema's single `execution.route` to the most demanding route required by the plan. Include owners, dependencies, guardrails, relevant Skill links, and allowed enterprise requirements.

When an action uses `growth_skills`, route it to the smallest owning artifact:

| Diagnosed action | Route |
| --- | --- |
| Metric contract, instrumentation, or decision-critical cross-source data defects | `growth-measurement` |
| One causal test or a cross-team experiment portfolio | `growth-measurement`, `growth-operations` |
| Medium-term choices, integrated planning, shared allocation, or one selected initiative | `growth-strategy`, `growth-operations` |
| One canonical decision or cross-initiative risk portfolio | `growth-operations` |
| Reusable cross-source learning, authorized change adoption, legacy retirement, or a completed-work retrospective | `growth-operations` |

Pass the evidence boundary, owner, decision use, dependencies, guardrails, and authorization state. Do not reproduce the specialist artifact inside the diagnosis.

A route is a recommendation, not authorization. Treat external writes, authenticated access, spend changes, publication, outbound messages, and persistent integrations as separate actions requiring explicit authorization. Do not perform them while producing a diagnosis.

## Deliver The Diagnosis

When intake is complete, include all of the following in both canonical JSON and readable Markdown when both are requested:

1. diagnostic context and target outcome;
2. exactly one primary constraint and alternative constraints;
3. supporting, contradictory, and missing evidence;
4. confidence and its evidence boundary;
5. prioritized 30-day actions;
6. decision-oriented experiments;
7. relevant Growth Playbook references by title and source text;
8. execution route, owners, dependencies, and guardrails.

Also write `.agents/growee-context.md` after a final diagnosis unless the user requests chat-only output or the environment cannot write files. This reusable handoff is not part of the protocol JSON schema and must not introduce facts absent from the canonical diagnosis.

Validate JSON against `assets/protocol.schema.json`. Keep Markdown semantically identical to JSON: same facts, values, source IDs, evidence meaning, constraint selection, actions, experiments, routes, and references. Presentation labels may explain schema buckets but may not add conclusions.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Before delivery, confirm that required input is complete; the mode is bounded; market and locale are explicit; direct observations are attributable; reported signals and inferences are not promoted to verified; contradictions and missing evidence are visible; exactly one primary constraint exists; confidence follows evidence; actions fit 30 days and have owners, dependencies, and guardrails; experiments change named decisions; schema validation passes; Markdown has semantic parity; Playbook links are relevant; `.agents/growee-context.md` was written only for a final diagnosis and contains no secrets or unnecessary personal data; and no external action was taken without separate authorization.
