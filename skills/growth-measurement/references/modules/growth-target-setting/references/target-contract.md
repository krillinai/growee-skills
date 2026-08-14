# Target Contract

## Freeze The Decision

Record this contract before proposing, comparing, approving, or reviewing a target.

| Field | Required definition |
| --- | --- |
| Target identity | Set ID, target ID, version, `audit`, `design`, or `refresh` mode |
| Decision | What commitment, allocation, escalation, or review the target governs |
| Ownership | One accountable outcome owner, contributors, and required approver |
| Scope | Company, product, market, segment, lifecycle, motion, team, and explicit exclusions |
| Time | Baseline as-of, effective date, target period, outcome window, maturity date, review, and expiry |
| Metric | Version, type, role, entity, eligibility, formula, identity, source, segment, market, currency, and accounting basis |
| Context | Customer value, strategy version, forecast origin and version, opportunity, capacity, dependencies, and risks |
| External boundary | Local artifacts allowed; system access, mutation, data export, contact, publication, spend, and deployment excluded unless separately authorized |

Do not silently change entity, eligibility, denominator, formula, identity, window, maturity, segment, market, currency, accounting basis, or period. A readable goal name is not a metric contract.

## Evidence States

Use exactly:

- `verified`: attributable and inspectable within the declared source, version, and cutoff;
- `inferred`: reasoned from named evidence with assumptions and alternatives visible;
- `unavailable`: required but not supplied, accessible, mature, compatible, or approved;
- `not applicable`: excluded by the frozen contract with a reason.

Keep actual, baseline, benchmark, estimate, forecast, scenario, opportunity, target, plan, budget, quota, approval, action, completion, and result separate. Record source, owner, date, version, population, market, period, maturity, value, limitation, contradiction, and next check.

## Define The Metric

For each target specify:

| Element | Requirement |
| --- | --- |
| Customer or business meaning | Value state, stock, flow, quality, economics, capacity, or guardrail represented |
| Entity and eligibility | Unit, participant roles, inclusion, exclusion, and original denominator |
| Formula and identity | Numerator, denominator, deduplication, hierarchy, and joins |
| Window and maturity | Observation period, outcome window, censoring, finalization, and late-data policy |
| Source and version | System of record, transformation, lineage, quality, revision, and owner |
| Segment and market | Decision-relevant slice, locale, product, plan, channel, and exclusions |
| Decision rule | Target value or state, threshold, guardrail, breach, stop, reset, and review |

An immature cohort or incomplete period is unavailable, not zero. Freeze metric versions across the target period or create an explicit break and reconciliation.

## Approval Semantics

A proposed target is not approved, adopted, funded, entered into systems, or accepted by its owner. Record proposal, review, approval, effective, superseded, expired, and retired states separately with attributable evidence. Approval of a target does not approve its plans, budgets, experiments, prices, hiring, incentives, or customer actions.
