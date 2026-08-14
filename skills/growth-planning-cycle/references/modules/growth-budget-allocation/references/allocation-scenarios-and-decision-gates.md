# Allocation Scenarios And Decision Gates

## Build Conditional Scenarios

Use scenarios only for uncertainties that change an allocation, sequence, reserve, or gate. Do not create optimistic-only narratives, invent probabilities, or average conditional futures into a false expected return.

| Scenario field | Requirement |
| --- | --- |
| Condition | Named internal or external state, not merely good, base, or bad |
| Assumptions | Compatible entities, periods, currencies, accounting and cash bases, formulas, units, and ranges |
| Evidence | Supporting, contradictory, unavailable, maturity, freshness, and transfer limits |
| Portfolio effect | Customer value, incremental economics, cash, capacity, dependencies, overlap, risk, and protected obligations |
| Trigger | Observable signal, threshold or qualitative condition, source, owner, and maturity |
| Response | Preserve, fund, stage, cap, reduce, pause, stop, reserve, reject, or reopen |
| Control | Review date, approver, cap, stop, rollback, expiry, correction, and residual obligation |

Use calibrated probabilities only when a separately valid forecasting or risk process supplies them. Show formulas, substituted values, ranges, rounding, and sensitivity. Unsupported precision is not rigor.

Identify:

- `robust commitments` that remain justified across plausible scenarios;
- `protected reserves` for governed obligations and uncertainty;
- `contingent commitments` activated only after evidence and approval;
- `hedges` that bound a shared or asymmetric downside;
- `options` that preserve future choice at acceptable cost;
- `irreversible commitments` that require the strongest evidence and authority.

A scenario cannot supply missing current-state evidence by assumption. Do not use a hypothetical floor, reserve, approval, capacity, deadline, sequence, or return threshold as the recommended base allocation. Keep hypothetical quantities inside a labeled scenario and only when the user supplied or explicitly authorized the assumptions.

## Set Allocation Bands

Do not impose an equal split or universal core, adjacent, exploratory, system, channel, lifecycle, product, or market ratio. Derive bands from the declared strategy and constraint, verified envelope, required protections, credible alternatives, incremental evidence, marginal economics, cash, capacity, dependencies, risk, reversibility, and time to decision-changing evidence.

Pass the numeric readiness gate in [budget-allocation-contract.md](budget-allocation-contract.md) before specifying any recommended band. If it fails, return qualitative pool roles, incompatibilities, the first limiting gate, and evidence needed to derive bands. Do not create exact amounts, percentages, normalized weights, ceilings, reserves, dates, phases, approvers, or hurdle rates merely because the user requests a complete allocation.

For each band define minimum viable resource, proposed range, maximum exposure, period, purpose, decision served, owner, prerequisites, measurement, maturity, positive, negative, harmful, invalid, and inconclusive outcomes, next decision, cap, stop, rollback, expiry, and residual obligations.

Prefer reversible, discriminating commitments before expensive or irreversible scale. Do not label an annual commitment or full rollout a pilot. A learning band is valid only when its evidence can change the next allocation.

## Apply Decision Gates

Use these states independently: `verified ready`, `bounded band only`, `specified not verified`, `verified blocker`, `unavailable`, or `not applicable`. Do not average gates into a score.

1. **contract:** one decision, owner, envelope, scope, bases, horizon, cutoff, versions, and authority;
2. **availability:** resources reconcile from request through protected and discretionary states without double booking;
3. **strategic and customer value:** selected strategy, customer value, repeated or protected outcome, alternatives, and exclusions align;
4. **evidence:** definitions, sources, maturity, validity, contradiction, incrementality, and transfer support the proposed band;
5. **economics and cash:** full and marginal costs, contribution, payback, timing, working capital, downside, and funding are compatible;
6. **capacity and dependency:** build, operate, support, govern, maintain, exit, shared constraints, and concentration are feasible;
7. **protection and risk:** customer, employee, reliability, accessibility, trust, privacy, security, compliance, fraud, and residual obligations are controlled;
8. **governance:** decision rights, approvers, measurement, review, correction, stop, rollback, expiry, audit, and external-action boundaries exist.

Name the first decision-limiting gate and the smallest evidence, capability, resource, approval, or design change that could reopen it. An upside estimate cannot override a verified protection, cash, authority, or legal-review blocker.

## Make Allocation Decisions

Use one decision state per allocation unit:

| Decision | Meaning |
| --- | --- |
| `preserve` | Keep the current governed resource while monitoring named evidence or obligations |
| `fund` | Recommend the bounded band because all limiting gates are satisfied |
| `stage` | Commit only the next reversible evidence-producing band |
| `cap` | Maintain or grow only to a defined exposure ceiling |
| `reduce` | Lower future avoidable resources while protecting transition and residual obligations |
| `pause` | Hold new commitment while preserving a bounded option or required service |
| `stop` | End future commitment with responsible exit and proof |
| `reserve` | Hold capacity for a protected, contingent, or uncertainty purpose |
| `reject` | Do not allocate under the current evidence and decision boundary |
| `unresolved` | Required compatibility, evidence, authority, resource, or protection remains unavailable |

A recommendation is not approval. Approval is not authorization. Authorization is not transfer or spend. Spend is not implementation or impact.

## Build The Reallocation Bridge

For `reallocate`, preserve the current approved allocation and record each proposed change:

| Field | Required record |
| --- | --- |
| Source | Current allocation unit, amount or resource, state, period, owner, avoidability, recovery, and obligations |
| Destination | Proposed unit, amount or band, period, owner, prerequisites, capacity, and readiness |
| Trigger | New mature evidence, cost, cash, constraint, risk, strategy, obligation, or expiry change |
| Effect | Customer, business, economic, cash, capacity, dependency, overlap, protection, risk, and opportunity-cost change |
| Authority | Decision owner, reviewers, approvers, effective date, conditions, and segregation of duties |
| Control | Evidence gate, cap, stop, rollback, correction, audit, maturity, expiry, and next review |

Do not move resources from an immature, underpowered, selectively reported, invalid, incompatible, or guardrail-harming result. Preserve the current allocation, reduce exposure, or request a bounded evidence band until the decision is supportable.

If the current approved allocation or discretionary source pool is unavailable, do not quantify preservation, reduction, evidence bands, or destination deltas. Mark the change `unresolved` and specify the record needed to reopen it.

## Check Portfolio Coherence

Confirm the proposal does not overload the same team, customer, market, channel, platform, vendor, data source, partner, product surface, measurement system, or cash period; duplicate outcomes; violate strategy exclusions; starve protected work; create conflicting incentives; or leave exit obligations unfunded. Show unresolved conflicts instead of forcing a complete allocation.
