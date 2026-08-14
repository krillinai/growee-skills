# Evidence And Scoring

## Evidence And Assessment States

Use evidence states `verified`, `inferred`, `unavailable`, or `not applicable`. Use `reported signal` only for an attributable statement without inspectable support and leave evidence state blank.

An assessed check receives:

- `pass`: 100% of fixed points;
- `partial`: 50% of fixed points;
- `fail`: 0% of fixed points;
- `unavailable`: excluded from earned and assessed max, included in all-applicable max;
- `not applicable`: excluded from both denominators.

Positive inference cannot pass. Directly adverse inference is partial until verified. Every partial or fail needs a finding; unavailable needs an evidence request, not a finding or deduction.

## Fixed Six-Dimension Card

| Dimension | ID | Check | Points |
| --- | --- | --- | ---: |
| Intent and message | LPA-INT-01 | Source promise and page message are continuous for the declared audience and intent | 5 |
| Intent and message | LPA-INT-02 | Product, category, audience, job, and page purpose are understandable | 5 |
| Intent and message | LPA-INT-03 | Primary value and relevant next step are visible without contradictory priorities | 5 |
| Intent and message | LPA-INT-04 | Market, language, locale, and page-specific context are coherent | 5 |
| Value and proof | LPA-VAL-01 | Value connects a meaningful outcome to the intended customer situation | 5 |
| Value and proof | LPA-VAL-02 | Differentiation is grounded in actual alternatives and available capabilities | 5 |
| Value and proof | LPA-VAL-03 | Proof is credible, attributable, current, and matched to the claim | 5 |
| Value and proof | LPA-VAL-04 | Claims, tradeoffs, trust, risk, and objections have clear boundaries | 5 |
| Hierarchy and content | LPA-HIR-01 | First viewport has a coherent hierarchy and no blocking clutter or overlap | 5 |
| Hierarchy and content | LPA-HIR-02 | Scanning order, labels, sections, and detail support the decision | 5 |
| Hierarchy and content | LPA-HIR-03 | Content answers necessary qualification, use, price, process, and expectation questions | 5 |
| Action and friction | LPA-ACT-01 | Primary CTA is specific, discoverable, consistent, and matched to commitment | 5 |
| Action and friction | LPA-ACT-02 | Form, signup, booking, cart, or checkout requests only decision-necessary effort | 5 |
| Action and friction | LPA-ACT-03 | Risk, reversibility, consent, privacy, price, and next-step expectations are visible | 5 |
| Action and friction | LPA-ACT-04 | Validation, error, success, recovery, and alternative paths are coherent | 5 |
| Experience and access | LPA-EXP-01 | Applicable mobile and responsive layouts remain readable and operable | 4 |
| Experience and access | LPA-EXP-02 | Measured performance and stability support the declared interaction | 4 |
| Experience and access | LPA-EXP-03 | Keyboard, semantics, labels, contrast, text alternatives, and focus are usable | 4 |
| Experience and access | LPA-EXP-04 | Access, rendering, links, controls, and technical states remain intact | 3 |
| Journey and learning | LPA-JRN-01 | The next page, product, sales, or service step preserves the promise | 4 |
| Journey and learning | LPA-JRN-02 | Events and metrics can distinguish qualified action, result, and downstream value | 3 |
| Journey and learning | LPA-JRN-03 | A testable hypothesis, guardrails, maturity, and decision rule can be specified | 3 |

Dimension totals are 20, 20, 15, 20, 15, and 10 for 100 overall points. Do not change weights for a page. Mark truly irrelevant checks `not applicable`; do not use that state to hide missing evidence.

## Fixed-Row Rule

When one check contains several required properties or members, enumerate them. If any required property or applicable member is unavailable, mark the entire check unavailable. When all are assessed, pass only if all pass, fail only if all fail, and partial for a mixture. Do not add subweights.

## Score And Coverage

```text
earned = sum of assessed awards
assessed max = sum of fixed points for pass, partial, and fail checks
all applicable max = assessed max + fixed points for unavailable checks
score = earned / assessed max * 100
coverage = assessed max / all applicable max * 100
```

Report two decimals and numerator/denominator. If assessed max is zero, score is `Not scored`. If all applicable max is zero, coverage is `Not scored`.

## Finding Record

Every partial or fail includes:

```yaml
id: page-slug-check-id-sequence
check_id: LPA-...
status: verified | inferred
scope: URL, state, viewport, audience, market, and source
evidence: exact observation, artifact, and date
impact: observed consequence; expected business effect labeled inferred
alternatives: credible competing explanations
action: owner-ready change or validation step
completion: observable proof the work is complete
effort: S | M | L
validation: metric, qualitative check, QA, or experiment with maturity and guardrails
```

Unavailable records list check ID, missing evidence, why unavailable, decision consequence, smallest collection step, owner, and effort.

## Priority

Order by verified blockers; verified high-deduction issues that affect qualified progression; dependencies that unlock multiple checks; small bounded fixes; then inferred experiments. Keep evidence acquisition separate from remediation. A high-impact inference is an urgent verification item, not a confirmed defect.

Do not promise uplift. Experiment plans define hypothesis, audience, source, unit, control, variant, primary metric, downstream guardrails, assignment, exposure, window, maturity, decision rule, stop rule, and rollback.
