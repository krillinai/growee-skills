# Cohort Analysis Output Contract

## Required Order

Return:

1. primary mode, decision, owner, cutoff, and external-action boundary;
2. cohort contract and definition version;
3. source, evidence, data-quality, privacy, and reconciliation ledger;
4. canonical cohort matrix or calculation-ready specification;
5. compatible comparisons with numerators, denominators, age, and maturity;
6. segment, exposure, behavior, state, or value cuts when decision-relevant;
7. aggregate-mix and within-group decomposition when supported;
8. findings, contradictory evidence, alternatives, limitations, and causal boundary;
9. measurement, validation, owner, and adjacent-Skill handoffs;
10. pinned Growth Playbook sources.

## Canonical Matrix

Use a table that keeps missingness visible:

| Cohort | Start | Eligible N | Age | Outcome N or value | Rate | Maturity | Source | Definition | Notes |
| --- | --- | ---: | --- | ---: | ---: | --- | --- | --- | --- |

Use `unavailable` for unsupported or immature values. Use zero only when verified coverage establishes a true zero. Mark partial cells explicitly and exclude them from final equal-age comparison unless the decision calls for a labeled provisional view.

## Comparison Ledger

For every claimed difference, state:

- compared cohorts and shared age;
- compatible entity, eligibility, start, outcome, denominator, timezone, and definition;
- absolute and percentage-point movement;
- group counts and contribution to canonical movement;
- mix, seasonality, version, selection, and measurement alternatives;
- uncertainty or sample limitation;
- whether the result is descriptive, predictive, or causally identified;
- decision the finding changes and evidence needed next.

## Evidence Boundary

Do not hide definition mismatches, unknown segments, small cells, missing events, late data, immature outcomes, discrepancies, or contradictory findings to simplify the output. Do not invent benchmarks, forecasts, causes, intervention effects, or external actions.

If supplied data cannot support a calculation, return the same structure with exact field, event, query, source, owner, validation, and maturity requirements needed to populate it.

## Privacy And Action Boundary

Exclude direct identifiers, credentials, private payloads, and unnecessary sensitive fields from the deliverable. Report only decision-required aggregate or pseudonymous evidence and apply the declared minimum cell threshold.

Local analysis does not authorize production queries, exports, dashboard edits, event changes, customer-state changes, experiments, messages, spend, publishing, or deployment. Record required permissions, privacy review, rollback, monitoring, and audit controls as unresolved handoffs.
