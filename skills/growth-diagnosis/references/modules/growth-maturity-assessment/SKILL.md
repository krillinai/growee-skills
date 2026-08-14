---
name: growth-maturity-assessment
description: Use when a team needs to assess recurring growth-decision capabilities across strategy, lifecycle, measurement, experimentation, infrastructure, organization, operations, risk, or learning; distinguish documented intent from implementation, adoption, reliability, decision use, and outcomes; expose capability dependencies and evidence gaps; or prioritize the smallest sufficient capability improvements without a universal maturity stage or composite score.
---

# Growth Maturity Assessment

Assess whether a bounded organization has the capabilities required for its current growth decisions. Treat maturity as decision-specific sufficiency supported by operating evidence, not a universal ladder, tool inventory, activity count, benchmark, or company score.

Read [capability-contract-and-evidence.md](references/capability-contract-and-evidence.md) before accepting any capability claim. Read [domains-states-and-assessment.md](references/domains-states-and-assessment.md) before evaluating domains or states. Read [dependencies-priorities-and-governance.md](references/dependencies-priorities-and-governance.md) before prioritizing, centralizing, automating, or transferring a pattern. Read [output-contract.md](references/output-contract.md) before delivery. Use [playbook-sources.md](references/playbook-sources.md) for the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `specification` | Evidence is absent or the assessment question, unit, consumer, or boundary is not yet stable |
| `assessment` | Evaluate a bounded set of capabilities for a named decision, constraint, or planning horizon |
| `audit` | Reconcile an existing maturity claim against artifacts, operating evidence, contradictions, controls, and outcomes |

Name one primary mode. If decision-critical evidence is missing, return an evidence-pending specification rather than manufacturing a finding.

## Freeze The Assessment Contract

Record independently:

- decision, assessed unit, product, customer, customer value, business model, stage, market, current constraint, and horizon;
- recurring growth decisions, their frequency and consequence, intended capability consumers, accountable owner, and review cadence;
- capability scope, exclusions, upstream dependencies, downstream uses, hard constraints, and external-action boundary;
- source, owner, version, as-of date, applicable period and entity, evidence state, compatibility, limitation, and expiry.

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Keep an attributable stakeholder statement without inspectable support as a `reported signal` with no evidence state. Preserve disagreement, counterevidence, failed work, non-use, incidents, exceptions, stale evidence, and unknowns.

Request only the smallest aggregate, redacted, or pseudonymous evidence that can change a capability finding, dependency, priority, or handoff. Do not request credentials, raw private communications, protected traits, sensitive employee records, or unrelated personal histories.

## Build Capability Records

Assess only capabilities needed by the scoped recurring decisions. Keep strategy, lifecycle, measurement, experimentation, infrastructure, organization, operations, risk, and learning records separate.

For each capability, record:

1. `need`: customer value, recurring decision, consumer, frequency, consequence, and smallest sufficient service;
2. `definition`: inputs, outputs, entities, semantics, interfaces, owner, controls, and acceptance criteria;
3. `provisioning`: approval, access, staffing, tooling, integration, and readiness without implying use;
4. `implementation`: inspectable working artifact or service within the declared scope;
5. `operation`: real cases, cycle time, quality, failures, exceptions, support, maintenance, cost, and recovery;
6. `adoption`: eligible consumers, repeat use, non-use, abandonment, queues, bypasses, and workarounds;
7. `reliability`: service level, data quality, incidents, degradation, fallback, and restoration evidence;
8. `decision integration`: bounded decisions changed, rejected, reversed, escalated, or stopped with reason codes;
9. `outcomes`: customer value, trust, retention, economics, guardrails, and causal limits;
10. `learning`: reusable decision records, corrections, expiry, transfer boundaries, and retirement.

Do not infer later states from earlier ones. A deck is not implementation; a license is not integration; access is not adoption; volume is not quality; confidence is not evidence; automation is not authority; revenue growth is not proof that every capability worked.

## Determine Decision-Specific Sufficiency

Never create one Growth Maturity Score, average domains, rank people or teams, fill missing evidence with zero, or assign a universal stage. Higher sophistication is not inherently better.

For each capability and decision, use one finding:

| Finding | Meaning |
| --- | --- |
| `sufficient` | Required state and hard constraints are supported for this decision and horizon |
| `conditional` | Use is bounded by named evidence, control, capacity, or review conditions |
| `insufficient` | A demonstrated gap prevents the required decision service |
| `blocked` | A noncompensable protection, dependency, or authority boundary fails |
| `not assessable` | Decision-critical evidence is unavailable or incompatible |
| `not applicable` | The capability is outside the declared decision and scope |

Show evidence coverage separately from capability condition. Preserve strengths, but never let them compensate for privacy, security, consent, accessibility, reliability, data quality, incident response, or customer-protection failures.

## Order Dependencies And Priorities

Trace customer entities, identity, permissions, sources, metric definitions, quality, experiment assignment and exposure, economics, decision rights, operating controls, adoption, reliability, and feedback before advanced prediction or automation.

Prioritize only when a gap constrains the declared decision or customer outcome. Compare `maintain`, `improve`, `standardize`, `keep local`, `compose`, `consolidate`, `retire`, `defer`, `route`, and `not applicable`. Prefer the smallest sufficient state after considering dependencies, evidence, customer value, risk, capacity, maintenance, management load, cost, adoption, and opportunity cost.

Separate finding, option, recommendation, decision, approval, initiative, action, verification, and result. Do not turn every gap into a project or invent dates, owners, budget, headcount, vendors, ROI, uplift, architecture, approvals, or implementation status.

## Route Specialist Work

This Skill owns the cross-domain assessment contract, evidence reconciliation, capability-state ledger, dependency view, decision-specific sufficiency findings, and handoffs. Route detailed work to the owning Skill:

- current constraint and 30-day triage: `growth-diagnosis`;
- lifecycle: `acquisition-strategy`, `activation`, `retention`, `monetization`, and `growth-loop-design`;
- metrics, data, cohorts, and models: `growth-measurement`, `retention`, and `growth-model-design`;
- experiments and causal claims: `growth-measurement` and `growth-operations`;
- systems, sourcing, and services: `growth-operations`;
- ownership, centralization, staffing, and decision rights: `growth-operations`;
- portfolio, capacity, investment, and initiatives: `growth-operations`;
- risk, change, learning, research, and surveys: `growth-operations`, `customer-research`.

Do not substitute this assessment for privacy, security, accessibility, legal, employment, finance, procurement, tax, regulatory, or AI-model review.

## Deliver In Order

Return:

1. mode, decision, assessed unit, customers, recurring decisions, consumers, horizon, owner, scope, and boundary;
2. capability ledger by domain with required state, evidence coverage, current finding, contradiction, blocker, and expiry;
3. artifact manifest and compatibility view;
4. dependency map with noncompensable constraints and evidence gates;
5. operating, adoption, reliability, decision-use, customer, economic, risk, and learning evidence;
6. smallest-sufficient dispositions prioritized by decision, constraint, value, dependencies, risk, capacity, and opportunity cost;
7. unresolved questions, specialist handoffs, approval-ready requests, residual obligations, and completion status.

For China work, answer in Simplified Chinese when requested and revalidate market, language, locale, currency, timezone, legal entity, product, customer, channel, platform, app distribution, identity, payment, invoice, data, consent, privacy, support, vendor, staffing, and decision rights. Translation and currency conversion do not transfer a capability, benchmark, or roadmap.

## External-Action Boundary

Create and read local artifacts only. Do not access authenticated planning, analytics, warehouse, product, experiment, CRM, billing, ad, lifecycle, creative, cloud, HR, finance, procurement, or communication systems; export private or production data; buy tools; change budgets; hire; reorganize; deploy automation; publish findings; or claim capability, customer, growth, or business improvement without separate authorization and verified downstream evidence.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm scope, decision, consumers, capability contracts, domains, evidence states, versions, compatibility, operating states, adoption, reliability, decision use, outcomes, costs, dependencies, blockers, risks, hard constraints, market boundaries, handoffs, expiry, external actions, residual obligations, and completion. Label anything unsupported `unavailable`; never silently complete it.
