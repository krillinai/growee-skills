# RevOps Audit Methods

## System Verdict

Assign exactly one end-to-end verdict:

| Verdict | Gate |
| --- | --- |
| `decision-ready` | Critical contracts and controls are operating, attributable, compatible, reconciled, and sufficient for the declared decision |
| `partially controlled` | Useful controls operate, but a material definition, workflow, reconciliation, quality, ownership, or governance dependency limits the decision |
| `reported only` | The current process is described primarily by stakeholder or dashboard reports without enough inspectable support |
| `not assessable` | The entity, motion, decision, or evidence boundary is too incomplete or incompatible to assign a control conclusion |

The verdict describes the declared decision and period, not the quality of a team or company.

## Workflow Record

For every transition capture:

```text
source and destination entity or state
eligibility and required buyer or customer evidence
trigger, non-trigger, acceptance, rejection, recycle, reversal, and expiry
input, output, owner, receiver, decision right, and service expectation
system, object, field, event, timestamp, and source of truth
queue, capacity, territory, priority, exception, escalation, and fallback
quality, reconciliation, monitoring, incident, and completion proof
```

Show branches and manual work. A documented process is not verified operation; a CRM field is not evidence that the process occurred correctly.

## Control Matrix

Audit controls across:

- entity, identity, hierarchy, lifecycle, and stage definitions;
- source, consent, suppression, attribution, and unknown handling;
- qualification, disqualification, buyer milestones, and no-decision;
- assignment, routing, queue, acceptance, rejection, recycle, and handoff;
- territory, ownership, partner, capacity, coverage, ramp, and exception;
- source of truth, required field, validation, integration, sync, latency, lineage, and snapshots;
- pipeline amount, close timing, stage, forecast category, probability basis, change, age, slippage, and loss;
- offer, price, discount, approval, quote, contract, order, subscription, invoice, payment, refund, revenue, and cash;
- implementation, first value, support, renewal, expansion, contraction, churn, and promise alignment;
- access, privacy, change control, audit, override, incident, rollback, retention, and retirement.

For each row record control state, evidence state, source, period, entity, owner, test, observed result, expected rule and basis, variance, impact, exception, counterevidence, remediation, and completion proof.

## Finding Severity

Prioritize by decision and customer harm, not cosmetic completeness:

| Severity | Meaning |
| --- | --- |
| `critical` | Current evidence supports material customer, financial, privacy, security, access, accounting, or irreversible operating risk requiring immediate accountable containment |
| `high` | A foundational definition, ownership, workflow, data, forecast, or reconciliation failure materially impairs near-term revenue decisions |
| `medium` | A repeated control weakness creates measurable delay, rework, leakage, inconsistency, or decision risk |
| `low` | A bounded improvement reduces friction or maintenance cost without blocking a material current decision |

Use `needs evidence` instead of severity when impact or failure is not verified. Do not call every missing field or manual step a defect.

## Diagnostic Rules

- Diagnose transition counts and absolute losses before rates alone.
- Separate seller activity from buyer or customer state.
- Separate process bypass from valid exception and local judgment.
- Separate missing data from observed zero and verified absence.
- Preserve unknown, unassigned, duplicate, suppressed, deleted, late, reversed, and disputed buckets.
- Compare compatible motions, segments, owners, cohorts, currencies, periods, stages, and maturity.
- Treat an SLA as a service hypothesis tied to customer value, capacity, priority, and operating hours, not a universal target.
- Treat territory, quota, and coverage as constrained allocation decisions, not proof of market opportunity.
- Trace a symptom to the earliest broken dependency before recommending tools or automation.

## Optional Score

Do not score by default. When explicitly requested:

1. declare dimensions, eligible checks, weights, evidence requirement, and version before scoring;
2. score only `verified` applicable checks;
3. connect every deduction to one finding and affected decision;
4. show evidence coverage as `verified eligible weight / total eligible weight`;
5. exclude `unavailable` and `not applicable` from the score denominator;
6. show unweighted control states and findings beside the score;
7. never compare scores across incompatible motions or versions.
