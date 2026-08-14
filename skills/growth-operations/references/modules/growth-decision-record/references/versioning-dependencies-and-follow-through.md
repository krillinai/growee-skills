# Versioning, Dependencies, And Follow-Through

## Keep One Stable Identity

Assign one stable decision ID and an immutable version to every published state. Record author, accountable decision owner, authority, created time, evidence cutoff, source versions, change trigger, change summary, effective period, review, expiry, canonical status, and prior and superseding versions.

Do not overwrite an earlier record. Distinguish:

| Change | Use |
| --- | --- |
| Draft revision | The record is not yet relied on and no accountable decision or approval is being changed |
| Amendment | A bounded field changes prospectively without misrepresenting the prior decision |
| Correction | A factual or transcription error is fixed while preserving the original value, source, reason, author, and time |
| Refresh | New evidence, assumptions, conditions, outcomes, or authority require a new reviewable version |
| Supersession | A later accountable decision replaces the earlier record for an explicit scope and effective period |
| Closure | The decision no longer governs new work, while residual obligations remain traceable |

An amended, corrected, refreshed, or superseding record does not retroactively change what was knowable, recommended, decided, approved, or authorized.

## Establish Canonical Status

Define canonical status by decision ID, field, decision class, owner, authority, scope, customer, product, market, metric, resource, effective period, and system of record. Legal, finance, product, growth, risk, and executive artifacts can each be authoritative for different fields; none becomes universally canonical from title or seniority alone.

When records conflict:

1. freeze every source and version;
2. identify the exact conflicting fields and effective periods;
3. preserve each source owner, authority, scope, evidence, and limitation;
4. determine whether the records govern different decision classes;
5. route unresolved authority conflicts to an accountable owner;
6. publish a reconciliation or new version without deleting history;
7. identify downstream artifacts that must acknowledge, reopen, or remain unchanged.

Do not let consumers choose the most favorable version.

Maintain a contradiction and reconciliation ledger:

| Field / decision class | Source A / version / authority | Source B / version / authority | Exact conflict / overlapping scope | Governing rule or accountable resolution needed | Canonical result / effective date / unresolved state | Consumers to reopen / acknowledge / verify |
| --- | --- | --- | --- | --- | --- | --- |

Preserve legal, financial, product, growth, risk, and executive decision classes separately when they govern different questions. A reconciliation does not give one function authority over every field.

## Map Upstream Dependencies

| Dependency | Required record |
| --- | --- |
| Strategy and policy | Artifact ID, version, owner, applicable choice, effective period, and conflict |
| Customer and market evidence | Population, source, period, maturity, market, evidence state, and transfer limit |
| Metric, target, forecast, and opportunity | Definition, version, owner, cutoff, horizon, assumptions, and compatibility |
| Experiment and analysis | Design or method, tested population, result maturity, causal status, and limitation |
| Budget, capacity, and organization | Available resource, owner, period, approval, dependency, and opportunity cost |
| Product, system, vendor, and contract | Version, capability, obligation, constraint, renewal, exit, and authority |

Record dependency state as `required`, `available`, `incompatible`, `blocked`, `expired`, `superseded`, or `not applicable`. A dependency named in a plan is not proof that it is available.

## Map Downstream Consumers

Track every known plan, initiative, experiment, budget, product requirement, system configuration, policy, contract, communication, dashboard, forecast, report, or review that relies on the decision.

| Consumer field | Requirement |
| --- | --- |
| Identity | Consumer artifact, owner, version, system, and decision fields consumed |
| Applicability | Customer, product, market, metric, resource, and effective period |
| Propagation | Required update, owner, prerequisite, approver, earliest valid date, and expiry |
| Acknowledgement | `unrequested`, `requested`, `acknowledged`, `rejected`, `blocked`, `verified`, or `unavailable` |
| Divergence | Local override, conflicting version, rationale, authority, risk, and resolution |
| Verification | Independent evidence that the intended artifact or operating state changed |

An update request, acknowledgement, task state, deployment event, or dashboard movement is not proof that every consumer adopted the decision correctly.

## Govern Effective Period, Review, And Expiry

Define start and end time, approved scope, conditions precedent, continued-validity conditions, scheduled review, evidence maturity, stop and rollback rules, and expiry. Add event-driven triggers for material changes in strategy, customers, product, market, price, channel, platform, metric, evidence, regulation, contract, cost, cash, capacity, risk, incident, or dependency.

When a trigger fires, mark the record `review-required`, `paused-record`, `expired`, or another supported bounded state until an accountable refresh occurs. Do not silently renew approval or authorization.

## Separate Follow-Through States

For each downstream commitment record expected artifact or operating state, accountable owner, accepted scope, resource, dependency, approval, authorization, due or maturity date, evidence, guardrail, stop, rollback, verification owner, completion proof, escalation, and expiry.

Use `proposed`, `accepted`, `active`, `blocked`, `complete`, `cancelled`, `superseded`, or `expired` for commitments. Keep decision, approval, authorization, assignment, implementation, verification, outcome, causal estimate, and success separate. `Active`, `in progress`, a closed ticket, or a launch announcement is not completion proof.

## Preserve Ex-Ante And Ex-Post Layers

Keep the ex-ante record immutable: question, alternatives, evidence, counterevidence, assumptions, uncertainty, dissent, recommendation, decision, rationale, authority, conditions, and cutoff. Add later evidence in an ex-post layer with source, date, maturity, definition bridge, changed assumption, observed outcome, causal status, correction, follow-through state, and reopen decision.

Build explicit old-to-new bridges for changed data, definitions, metrics, assumptions, alternatives, decisions, approvals, authorizations, conditions, and corrections. Record which prior statements remain valid, which are invalid only prospectively, and which downstream consumers must reopen.

Evaluate decision quality using evidence and choices available at the cutoff. Evaluate execution, coordination, protection, outcome, and learning separately. A favorable result can follow a weak decision; an unfavorable result can follow a disciplined decision. Preserve luck, variance, external change, and unresolved causality. Route a full after-action analysis to `growth-operations`.

## Close Or Supersede Responsibly

Record final governing scope, effective end, superseding record, downstream disposition, archival state, retention, customer notice requirement, financial and contractual obligations, data and access handling, system and vendor decommissioning, verification, unresolved risk, and accountable owner. Closure stops new reliance; it does not erase residual obligations or prior decisions.
