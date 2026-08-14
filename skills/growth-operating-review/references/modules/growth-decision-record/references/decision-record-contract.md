# Growth Decision Record Contract

## Freeze Record Identity

| Field | Required record |
| --- | --- |
| Identity | Stable decision ID, version, mode, state, title, exact question, decision type, canonical version, prior version, and non-goals |
| Accountability | Proposer, recommender, accountable decision owner, contributors, reviewers, approvers, authorizers, executor roles, verification owner, stop authority, and escalation |
| Scope | Products, business models, customers, participant roles, markets, locales, metrics, resources, time horizon, included choice, and exclusions |
| Time | Evidence period, cutoff, decision date, effective period, maturity, scheduled review, event triggers, expiry, pause, close, and supersession |
| Lineage | Strategy, metric, target, forecast, opportunity, experiment, analysis, budget, policy, contract, plan, and prior-decision versions |
| Governance | Evidence, source, privacy, market, approval, authorization, communication, system, spend, publication, and external-action boundaries |

One record covers one choice with one decision owner, authority path, alternative set, effective period, reversibility boundary, and intended outcome. Split the record when these differ. Link related decisions with dependency IDs and sequence rather than hiding several choices under one title.

## Use Explicit Record States

| State | Meaning |
| --- | --- |
| `draft` | Scope or required record fields are incomplete |
| `evidence-pending` | The question is bounded but material evidence or alternatives remain unavailable |
| `decision-ready` | Alternatives, evidence, tradeoffs, owner, authority, and conditions support an accountable decision |
| `decided-record` | An attributable decision owner selected an option for a bounded scope |
| `approval-pending` | A decision exists but required approval is not verified |
| `approved-record` | Attributable approval exists for a bounded version and effective period |
| `authorized-record` | Separate authority permits a named external action under conditions |
| `active-record` | Supplied evidence says authorized follow-through is in effect; implementation and impact remain separate |
| `review-required` | A scheduled or event-driven trigger invalidates continued reliance until accountable review |
| `paused-record` | A decision or action is held while obligations and reopen conditions remain |
| `closed-record` | Accountable closure and residual obligations are recorded |
| `superseded` | A later version replaces this record while preserving its history |
| `expired` | Evidence, assumptions, approval, authority, or effective period lapsed |

Never infer a later state from an earlier one.

## Apply The Readiness Gate

| Field or transition | Minimum attributable basis |
| --- | --- |
| `decided-record` | Exact question, bounded scope, selected alternative, accountable decision owner, decision authority, date, rationale, and conditions |
| `approved-record` | Required approval class, attributable approver, exact version and scope approved, conditions, effective period, and expiry basis |
| `authorized-record` | Named external action, system and scope, authorizer authority, prerequisites, controls, effective period, and expiry |
| `active-record` | Supported authorized version plus supplied evidence that follow-through is currently in effect |
| Canonical status | Stable ID, field or decision class, source-of-record rule, owner, authority, scope, version, and effective period |
| Owner or assignment | Named or role-based accountability, authority, explicit acceptance, capacity, scope, and period |
| Confidence or score | Defined construct, method, compatible evidence, calibration or sensitivity, owner, version, and limitations |
| Effective date, review, or expiry | Attributable governing source, authority, exact scope, conditions, timezone and counting convention, version, and approval state |
| Acknowledgement or propagation | Exact consumer and version, attributable response or independent system evidence, date, scope, and verification |

If the minimum basis is absent, keep the record `draft` or `evidence-pending` and the governing field `unavailable`. Preserve requested values in a separate request ledger without calculating relative dates, creating proposed commitments, assigning owners, or implying acceptance. Urgency, seniority, silence, output completeness, and a user-specified value do not satisfy this gate.

## Preserve Source And Evidence States

Use only `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. A statement may remain a `reported signal` when speaker, role, date, exact wording, context, and limitations are attributable but independent support is absent.

For every source record source ID, type, owner or author, date, version, as-of time, market, product, population, period, definition, maturity, evidence state, claim supported, limitations, contradictions, and correction.

A message, meeting note, vote, attendance list, lack of objection, repeated phrase, analogy, dashboard screenshot, or senior belief supports only what it directly shows. It does not prove consensus, authority, causality, approval, or execution.

## Separate Action States

```text
proposal or request
-> analysis
-> recommendation
-> accountable decision
-> specialist approval
-> legal, financial, employment, contract, or system authorization
-> assignment and resource availability
-> execution
-> completion proof
-> mature outcome
```

Record source, owner, authority, scope, conditions, effective period, expiry, evidence, and version for each state. Leave unsupported states unavailable.

## Decompose Multi-Decision Requests

Create separate records when decisions differ by accountable owner, approver, authority, alternative set, affected population, resource, reversibility, effective date, or outcome. Preserve a parent decision graph with prerequisites, sequencing, conflicts, shared assumptions, and downstream consumers.

Shared context belongs in versioned source artifacts. Do not copy it into divergent records without lineage.
