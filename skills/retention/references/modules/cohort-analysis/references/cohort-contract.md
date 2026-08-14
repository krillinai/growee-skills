# Cohort Contract

## Required Decision Context

Capture these fields independently:

- decision, decision date, owner, and action the analysis may change;
- entity and level: user, account, workspace, household, lead, opportunity, order, subscription, listing, supplier, location, product, logo, revenue, contribution, or another explicit unit;
- canonical eligibility, inclusion, exclusion, and credible-opportunity rule;
- cohort basis: start time, exposure, behavior, product state, transaction, activation, acquisition, experiment assignment, or another declared basis;
- start event and timestamp; first, latest, every, or episode assignment rule;
- qualifying outcome, value event, state, revenue, contribution, cost, or cumulative-value definition;
- numerator, denominator, interval, cohort-age calculation, window, and maturity rule;
- observation cutoff, timezone, source latency, and late-arrival allowance;
- identity, anonymous-to-known merge, cross-device, account membership, deduplication, deletion, and re-entry rules;
- market, product version, acquisition source, campaign, role, plan, exposure, and other decision-relevant cuts;
- source artifacts, owners, extraction dates, definition version, freshness, and limitations;
- privacy purpose, approved joins, minimum cell size, access boundary, and output aggregation.

If a material definition changes, version the contract. Restate compatible history or show a visible series break instead of presenting two definitions as one continuous metric.

## Cohort, Segment, And Funnel

| Structure | Defining rule | Decision use |
| --- | --- | --- |
| Cohort | Shared start, exposure, behavior, or state observed at common age | Compare outcomes at equal maturity |
| Segment | Relatively durable customer or account attributes | Choose different product, service, message, or market paths |
| Funnel or state model | Ordered or permitted value transitions | Locate loss, delay, and constraints |

A segment can cut a cohort and a funnel can be compared across cohorts. Do not turn an analytical cohort into an ICP or persona without durable value, qualitative, economic, and decision evidence.

## Input Shapes

Accept either compatible aggregate tables or pseudonymous event records.

Minimum aggregate fields:

| Field | Requirement |
| --- | --- |
| `cohort_id` | Stable start, exposure, behavior, or state group |
| `cohort_start` | Timestamp or period under the declared timezone |
| `cohort_age` | Elapsed interval or opportunity count |
| `eligible_n` | Original or verified opportunity denominator |
| `outcome_n` or `outcome_value` | Compatible numerator or value |
| `maturity` | Mature, partial, right-censored, or unavailable |
| `segment` | Optional decision-relevant cut with unknown preserved |
| `source_version` | Attributable extract and definition version |

Minimum event fields:

- pseudonymous entity ID;
- cohort-start event and timestamp;
- qualifying outcome event, timestamp, and value when applicable;
- entity, identity, eligibility, exclusion, and assignment fields;
- only decision-required segment and exposure fields;
- source version, extraction cutoff, and timezone.

Do not request raw names, email addresses, phone numbers, credentials, payment credentials, signed links, full message bodies, private documents, precise locations, sensitive attributes, or unrelated histories when aggregates or pseudonymous records are sufficient.

## Evidence And Missing Data

Use `verified`, `inferred`, `unavailable`, or `not applicable` for every evidence-bearing row. Use `reported signal` only for an attributable stakeholder statement without inspectable support.

Public product information can support a draft entity, start, outcome, cadence, and data specification. It cannot establish private membership, rates, value, cohort LTV, churn, segment performance, or cause. Missing data is `unavailable`, not zero.
