# Growth Postmortem Contract

## Reviewed Unit

Define one unit before review:

- initiative, experiment, campaign, launch, pricing or packaging change, market entry, incentive, partnership, growth-system change, incident, or planning period;
- unit ID and version, source decision, accountable owner, product, customer, participant roles, market, locale, start and end, exposure and maturity windows, state, scope, exclusions, and related units;
- eligibility and inclusion rule, including completed, stopped, cancelled, expired, harmful, invalid, inconclusive, active, and never-launched states;
- intended postmortem decisions, required approver, evidence cutoff, correction cutoff, review date, next refresh, and expiry.

Do not combine units merely because they share a quarter, team, metric, or executive sponsor. Use a portfolio view only after each unit has a stable identity and compatible evidence.

## Select Reviews Consistently

Define the complete population and trigger for mandatory, sampled, or optional postmortems before outcomes are selected. Useful triggers include material customer or economic exposure, an unexpected outcome, guardrail breach, irreversible commitment, large resource use, important uncertainty resolved or left unresolved, repeated failure, reusable capability change, or a portfolio decision.

Include positive, negative, flat, harmful, inconclusive, invalid, stopped, cancelled, expired, active, and never-launched work when the trigger applies. If sampling is necessary, preserve the frame, method, exclusions, missing cases, and bias. Do not select only stories useful for celebration or blame.

## Source Artifact Manifest

| Artifact | Required fields |
| --- | --- |
| Strategy and constraint | ID, version, customer, market, choice, exclusion, mechanism, owner, cutoff |
| Decision | question, alternatives, evidence, uncertainty, rationale, owner, approver, date, expiry |
| Metrics | entity, eligibility, numerator, denominator, window, cohort, maturity, source, version |
| Baseline and target | definition, value, period, segment, source, basis, owner, approval state |
| Forecast and scenario | vintage, as-of date, horizon, assumptions, method, range, owner, use |
| Opportunity and economics | unit, eligible population, value basis, costs, cash, timing, uncertainty |
| Plan and initiative | outcome, workstreams, milestones, capacity, budget, dependencies, guardrails, stop rules |
| Implementation and exposure | release, eligibility, assignment, exposure, adoption, change, rollback, verification |
| Outcomes and incidents | customer, business, economic, quality, trust, harm, support, maturity, correction |
| Follow-up | decision, proposed owner, approval, artifact, evidence gate, proof, review, expiry |

For every artifact preserve source, owner, date, version, as-of and evidence cutoff, effective period, state, market, segment, entity, limitations, contradictions, amendment, superseded version, and decision served.

## Evidence States

Use exactly:

- `verified`: attributable evidence directly supports the bounded claim;
- `inferred`: explicit reasoning connects evidence to a claim but does not directly verify it;
- `unavailable`: required evidence is absent, inaccessible, immature, incompatible, or not supplied;
- `not applicable`: the field does not apply to the declared unit and decision.

Keep a participant's attributable account as a `reported signal` until corroborated. Do not use labels such as complete, approved, severe, successful, failed, causal, adopted, or closed as evidence states.

## State And Outcome

Postmortem state:

- `draft`: contract exists but review is incomplete;
- `evidence-pending`: required outcomes, corrections, maturity, or specialist evidence is unavailable;
- `review-ready`: the record is complete enough for accountable interpretation and decisions;
- `accepted`: an attributable accountable owner accepted the bounded findings and decisions;
- `actions-open`: accepted follow-up commitments remain unresolved;
- `closed`: required review obligations and actions have completion, supersession, cancellation, or expiry records;
- `superseded`: a later version replaces this record without erasing it;
- `expired`: the review no longer supports the intended decision.

Classify each outcome dimension separately as `beneficial`, `harmful`, `flat`, `directional`, `inconclusive`, `invalid`, `not mature`, or `unavailable`, with evidence and scope. Do not reduce customer, business, economic, quality, risk, or learning outcomes to one success label.

## Authority Boundary

Record who may review, decide, approve, authorize, execute, verify, and accept follow-up work. These may be different roles. A postmortem owner, facilitator, contributor, meeting attendee, comment, recommendation, or action row does not prove decision authority, acceptance, authorization, or execution.
