# Funnel Contract

## Required Decision Context

Capture these fields independently:

- decision, decision date, owner, and action the analysis may change;
- final customer outcome, business outcome, and analysis horizon;
- entity and level: person, user, account, workspace, lead, opportunity, order, subscription, listing, supplier, location, or another explicit unit;
- canonical eligible starting population and why each unit had a credible opportunity to enter;
- state order or allowed transition graph;
- entry event, success event, timestamp, and customer-value interpretation for every state;
- step numerator, step denominator, end-to-end denominator, and retained cohort membership;
- observation window, maturation window, cutoff time, timezone, and data-latency allowance;
- identity, anonymous-to-known merge, cross-device, account membership, deduplication, and deletion rules;
- exclusion, bot, internal-user, fraud, cancellation, refund, error, and missing-data treatment;
- rules for re-entry, retries, skipped states, branches, reversals, resurrection, and repeated conversion;
- market, language, locale, product surface, source, campaign, promise, role, plan, and other decision-relevant segments;
- source artifacts, definition version, extraction or capture date, freshness, and owner;
- downstream value, retention, quality, trust, risk, capacity, support, and economic guardrails;
- known discrepancies, inaccessible sources, and limitations.

If one of these choices changes, version the contract. Do not compare a changed definition with the prior series as though the metric were continuous.

## State Dictionary

For every state record:

| Field | Requirement |
| --- | --- |
| State | Stable name and sequence or graph position |
| Meaning | Customer or operating transition represented |
| Entity | Unit that can enter and exit the state |
| Eligibility | Observable rule for a credible opportunity |
| Entry event | Exact event or record and timestamp |
| Success event | Exact event or record that reaches the next state |
| Window | Allowed time from entry to success |
| Maturity | Point at which the outcome is complete enough to read |
| Exclusions | Frozen rules, never post-result convenience filters |
| Re-entry | First, latest, every, or episode-based handling |
| Source | Event, table, report, file, or supplied artifact |
| Owner | Person or system accountable for the definition |

Do not use an interface screen as a state unless reaching it represents a meaningful decision. If users can loop, branch, skip, or return, specify a state-transition model rather than forcing one linear path.

## Evidence States

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. Use `reported signal` only for an attributable stakeholder statement without inspectable support.

- `verified` means the cited source supports the stated count, definition, event, or observation within its scope.
- `inferred` means a transparent transformation or interpretation is required.
- `unavailable` means the evidence was not supplied, accessible, mature, or compatible.
- `not applicable` means the field does not apply under the frozen contract.

A verified transition rate establishes an observed rate, not the cause of the transition or the effect of a proposed change.

## Reconciliation Invariants

Check these before interpretation:

- every numerator belongs to its stated denominator;
- sequential step counts do not increase unless the model permits re-entry, merging, or branching and labels it;
- end-to-end converters remain members of the canonical eligible start cohort;
- summed mutually exclusive segments equal the canonical total after documented unknowns;
- overlapping segments are not summed as though they were exclusive;
- event and aggregate extracts use the same identity, cutoff, timezone, and definition version;
- mature and immature units are reported separately;
- deleted, duplicated, merged, late, or missing records remain visible in reconciliation;
- skipped states, retries, reversals, and repeated conversions follow the frozen rules;
- calculated totals can be reproduced from the supplied artifacts.

If reconciliation fails, stop causal interpretation. Return the discrepancy, affected metrics, likely definition or pipeline sources, owner, and validation steps.

## Privacy And Data Minimization

Prefer aggregate or pseudonymous event records. Exclude direct identifiers, raw message content, credentials, signed links, payment credentials, private payloads, and unrelated histories unless explicitly necessary and authorized. Record the purpose, approved joins, access boundary, aggregation threshold, and retention scope.

Do not claim that a query, export, deletion, dashboard change, event repair, or identity merge occurred unless it was separately authorized and observed.

## Missing Data Boundary

Public product pages can support a draft state model, customer journey hypothesis, instrumentation specification, and risk inventory. They cannot establish private eligibility, traffic, conversion, cohort maturity, drop-off cause, retained quality, revenue contribution, or experiment results. When inputs are missing, deliver the contract and smallest evidence request rather than placeholder rates.
