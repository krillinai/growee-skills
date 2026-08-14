# Analysis Methods

Analyze only the supplied, validated evidence. Use formulas to describe the account's own history, not to introduce external targets.

## Dependency Order

```text
decision and economic boundary
-> input and measurement integrity
-> account and delivery structure
-> creative concept coverage
-> landing and offer continuity
-> customer quality and business reconciliation
-> bounded findings and next evidence
-> 30-day tests with owners and decision rules
```

If an upstream dependency is unavailable, continue with supported downstream observations but state which decisions cannot be made.

## Account And Delivery Structure

Use stable IDs, not names alone. Inventory campaigns, ad sets, ads, objectives, statuses, destinations, dates, and result definitions. Describe how spend, impressions, clicks, results, and attributed revenue are distributed across campaign, ad set, ad, concept, market, and time when the data supports those levels.

Useful descriptive calculations include:

- spend share = entity spend / comparable total spend;
- impression share = entity impressions / comparable total impressions;
- CPM = spend / impressions x 1,000;
- click-through rate = clicks / impressions;
- cost per click = spend / clicks;
- landing-page-view rate = landing page views / clicks;
- platform result rate = reported results / the declared eligible denominator;
- platform cost per result = spend / reported results;
- platform ROAS = attributed revenue / spend.

Label denominators, currency, date window, attribution setting, and unavailable values. A zero denominator produces `unavailable`, not zero or infinity.

Concentration is a distribution, not automatically a defect. Show the share held by the largest entities and concepts, how that distribution changes through time, and what customer or operational risk follows. Do not impose a fixed maximum share or campaign count.

## Creative Concepts And Variants

Map each creative by:

| Layer | Question |
| --- | --- |
| Persona | Whose situation or constraint is represented? |
| Pillar | Which durable value territory is being tested? |
| Angle | Which customer belief or value hypothesis makes the pillar relevant? |
| Offer | What exchange or next step is proposed? |
| Proof | What attributable evidence supports the claim? |
| Format | How is the idea delivered? |
| Hook | What earns the next moment of attention? |
| Creator | Who delivers the message, and what is verified about them? |
| Rights | Is usage permission documented for the market and placement? |

Treat a new persona, problem, promise, proof mechanism, or value hypothesis as a possible new concept. Treat crops, opening frames, caption lengths, aspect ratios, edits, and CTA wording as variants unless the underlying hypothesis changes.

Report concept coverage and execution coverage separately. A large number of files can still represent one concept; one concept can also contain insufficient execution evidence.

### Fatigue Signals

Require a comparable time series and visible delivery context. Possible signals include sustained deterioration in response or qualified outcome, repeated delivery to a bounded audience, rising cost with stable measurement, or loss of concept diversity. Check spend, reach, impressions, placements, objective, attribution setting, offer, landing page, market, seasonality, auction conditions, and tracking changes before assigning a cause.

Use `fatigue signal`, not `fatigue confirmed`, unless the evidence distinguishes creative decay from delivery, audience, landing, offer, measurement, or market changes. Do not use a universal frequency threshold.

## Landing And Offer Continuity

For the ad and its dated destination, compare audience state, problem, promise, offer, price, proof, objections, CTA, language, locale, device path, and next value. Record redirects, broken states, unavailable pages, and page changes during the audit window.

A mismatch is verified only when both sides are captured and comparable. A suspected page-speed, form, checkout, or tracking issue remains `inferred` until measured. Never edit or deploy a page from this audit.

## Measurement And Reconciliation

Create a definition ledger for events, result type, attribution setting, time zone, currency, deduplication, identity, new-customer logic, refund treatment, cost scope, contribution, retained value, maturation, and experiment design.

Keep four views separate:

1. delivery: what Meta reports serving and charging;
2. attribution: which conversions Meta assigns under a declared setting;
3. business reconciliation: what commerce, CRM, finance, or product systems record under their own definitions;
4. incrementality: what a credible counterfactual design estimates would not otherwise have occurred.

Do not force these views to match. Reconcile window, entity mapping, currency, timezone, cancellations, refunds, taxes, shipping, discounts, duplicated events, modeled events, view-through credit, consent loss, late outcomes, and unavailable records. The residual difference is a finding to explain, not a number to hide.

Only call a result incremental when a credible experiment or causal design supports that claim. Attribution alone does not establish causality.

## Customer Quality And Economics

Prefer the declared qualified outcome over raw platform conversions. When definitions and scope are aligned, calculate:

- new-customer acquisition cost = eligible media cost / qualified new customers;
- refund-adjusted revenue = gross revenue - refunds;
- contribution = refund-adjusted revenue - cost of goods - declared variable costs;
- contribution after media = contribution - eligible media cost;
- payback = cumulative matured contribution compared with acquisition cost;
- retained-value view = qualified cohort value at the declared maturation window.

Expose all included and excluded costs. Do not infer customer status, retention, margin, capacity, or payback from Meta-reported purchases or ROAS. If downstream linkage is unavailable, state that scaling or allocation cannot be governed by customer economics yet.

## Reported Performance Changes

Translate a statement such as "performance fell" into a testable observation: metric, definition, entity, market, comparison window, attribution setting, magnitude, and source. Mark the initial statement `reported signal`.

Check in this order:

1. definition, export, tracking, attribution, and reporting changes;
2. date-window comparability, maturation, seasonality, and market events;
3. spend and delivery mix;
4. creative concept and execution mix;
5. destination, offer, price, inventory, and operational changes;
6. customer quality, refunds, contribution, and retained value;
7. causal evidence.

Return competing explanations and the smallest discriminating evidence. Do not jump from a correlated movement to a campaign action.

## Findings And 30-Day Plan

Each finding should contain:

| Field | Requirement |
| --- | --- |
| Observation | What the evidence shows, without causal inflation |
| Impact | Which declared decision or outcome it affects |
| Source | File, row range, screenshot, system, and capture date |
| Evidence state | One allowed state |
| Action | Local analysis, evidence acquisition, or test design |
| Completion proof | Artifact or result that shows the action is complete |
| Owner | Accountable role or team |
| Effort | Relative effort or declared estimate, not invented certainty |

Sequence the 30-day plan around evidence dependencies. Include review dates, guardrails, stopping conditions, and decision rules. A decision rule must use the organization's declared economics or a prospectively agreed experiment threshold; never fabricate CPA, ROAS, frequency, creative-count, or budget rules.
