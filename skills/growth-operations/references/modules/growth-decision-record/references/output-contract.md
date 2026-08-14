# Growth Decision Record Output Contract

## Required Order

Return:

1. mode, decision ID and version, record state, exact question, decision type, intended use, owners, authority, scope, products, customers, markets, periods, cutoff, privacy, review, expiry, and external-action boundary;
2. source, evidence, contradiction, assumption, uncertainty, definition, version, access, and correction ledger;
3. current-state and do-nothing baseline plus credible alternatives, exclusions, common comparison bases, and reopen conditions;
4. customer value and harm, evidence, economics, cash, capacity, timing, dependencies, opportunity cost, reversibility, risks, residual obligations, and sensitivity;
5. recommendation, accountable decision, rationale, counterevidence, dissent, unresolved issues, conditions, resource boundary, and risk acceptance;
6. decision, review, approval, authorization, funding, assignment, implementation, verification, outcome, causal estimate, and success states;
7. effective period, scheduled and event-driven review, expiry, stop, rollback, correction, pause, close, and supersession rules;
8. upstream dependency, downstream consumer, artifact version, acknowledgement, divergence, propagation request, and independent verification register;
9. immutable version history, ex-ante and ex-post layers, follow-through, outcomes, corrections, decision-quality boundary, and reopen state;
10. governance, market and privacy boundaries, specialist handoffs, pinned Growth Playbook sources, approval-ready external actions, and completion record.

## Decision Contract

| Decision / version / mode / state | Question / type / intended use | Owner / authority / reviewers / approvers | Scope / exclusions / products / customers / markets | Period / cutoff / effective / review / expiry | Privacy / sources / action boundary |
| --- | --- | --- | --- | --- | --- |

One row governs one bounded choice. Split decisions that differ in owner, authority, alternatives, effective period, reversibility, or outcome.

## Source And Evidence Ledger

| Source / owner / date / version | Claim / definition / population / period | Evidence state / access / maturity | Supporting evidence / counterevidence / contradiction | Assumption / uncertainty / transfer limit | Correction / consumer / next evidence |
| --- | --- | --- | --- | --- | --- |

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing claims. Keep attributable but unsupported statements as reported signals. Do not invent consensus, confidence, causality, approval, or execution.

Keep requested states, owners, scores, confidence, relative dates, durations, deadlines, acknowledgements, and actions in a separate request ledger until the readiness gate passes. Do not calculate calendar dates from relative requests or populate them as proposals merely to complete the record.

## Alternatives And Tradeoffs

| Alternative / scope / exclusions | Customer value / harm / mechanism | Evidence / counterevidence / assumptions | Economics / cash / capacity / opportunity cost | Risk / dependency / reversibility / residual obligation | Decision state / rationale / reopen / expiry |
| --- | --- | --- | --- | --- | --- |

Include the current-state baseline and credible smaller, staged, reversible, preserve, defer, partner, build, buy, compose, pause, stop, salvage, or exit options as applicable. Keep incompatible bases separate. Do not use strawmen or invented scores.

## Decision And Authority Record

| Recommendation / owner | Accountable decision / owner / date | Rationale / evidence / counterevidence | Dissent / unresolved issue / tradeoff accepted | Review / approval / authorization / risk acceptance | Conditions / resource / effective / expiry |
| --- | --- | --- | --- | --- | --- |

Leave unsupported states unavailable. Decision is not approval; approval is not authorization; authorization is not execution.

## Conditions, Risks, And Lifecycle

| Condition or risk / affected population | Evidence / uncertainty / severity basis | Prevention / mitigation / monitoring | Owner / reviewer / acceptance authority | Effective / review / trigger / expiry | Stop / rollback / correction / residual obligation |
| --- | --- | --- | --- | --- | --- |

Do not compensate noncompensable harm or verified blockers with financial upside.

## Dependencies And Downstream Consumers

| Dependency or consumer / owner | Artifact / system / version / field | Required state / change / prerequisite | Acknowledgement / divergence / conflict | Effective / due / review / expiry | Verification / escalation / supersession |
| --- | --- | --- | --- | --- | --- |

Do not overwrite conflicts, silently copy changes, or claim downstream propagation.

## Version, Follow-Through, And Outcome Record

| Version / date / author / trigger | Preserved ex-ante record | New evidence / correction / changed assumption | Commitment / state / owner / proof | Outcome / maturity / causal status | Consumer reopen / supersession / residual |
| --- | --- | --- | --- | --- | --- |

Keep decision quality, execution quality, outcome quality, and luck separate. `In progress`, a closed task, or a favorable result is not proof of correct implementation or causal success.

## Approval-Ready External Actions

| Proposed action / system / scope | Decision version / evidence / conditions | Owner / approver / authorizer / executor | Access / dependency / privacy / risk checks | Dry run / monitor / stop / rollback / audit | Verification / completion proof / expiry |
| --- | --- | --- | --- | --- | --- |

Specify requests only. Do not imply approval, authorization, execution, or results.

## Completion Gate

Confirm decision ID, version, mode, state, question, type, intended use, owner, authority, roles, scope, exclusions, products, customers, markets, metrics, resources, periods, cutoff, sources, evidence states, definitions, maturity, contradictions, assumptions, uncertainty, current-state baseline, credible alternatives, comparison bases, customer value and harm, economics, cash, capacity, opportunity cost, dependencies, reversibility, risk, residual obligations, recommendation, decision, rationale, dissent, unresolved issues, review, approval, authorization, conditions, effective period, expiry, triggers, stop, rollback, correction, upstream versions, downstream consumers, acknowledgement, divergence, propagation, immutable history, ex-ante and ex-post layers, follow-through, outcomes, causal status, decision quality, market transfer, privacy, fairness, handoffs, pinned sources, external actions, and completion are explicit or unavailable with the missing basis recorded; unrelated choices were not combined; silence was not consensus; beliefs were not evidence; targets, forecasts, budgets, plans, decisions, approvals, and actuals were not conflated; causal claims did not exceed evidence; scoring did not replace judgment; unsupported governing, numeric, date, ownership, acknowledgement, and propagation fields were not populated; relative requests were not converted into calendar commitments; downside and dissent were not hidden; history was not rewritten; outcomes did not determine ex-ante quality; personal data was minimized; no unsupported action state was invented; and no external action occurred.
