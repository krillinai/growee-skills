# Comparison And Change Analysis

Build comparisons for a declared choice. A universal competitor matrix combines incompatible decisions and ages quickly.

## Comparison Frame

For each criterion define:

- customer, job, buying situation, and consequence;
- criterion and acceptable evidence;
- product, edition, plan, entitlement, market, platform, and version;
- observation and effective dates;
- state, value, unit, evidence, limitation, and contradiction;
- importance source, blocker rule, sensitivity, and owner.

Criteria can include workflow fit, capability, availability, integration, setup, migration, quality, reliability, performance, security and trust evidence, service, support, ecosystem, distribution, contract, price, switching, and customer outcome. Include a criterion only when it can change the decision.

## Capability State Model

Keep the following states separate:

| State | Meaning |
| --- | --- |
| `announced` | A dated source describes an intended or introduced capability |
| `documented` | Current official material describes behavior and scope |
| `observed` | Authorized direct observation confirms behavior under recorded conditions |
| `beta or limited` | Access is restricted by account, invitation, geography, platform, or readiness |
| `generally available` | Evidence supports broad release within the declared market and plan boundary |
| `deprecated or removed` | Dated evidence supports withdrawal or end-of-life within the declared scope |
| `unavailable evidence` | The required state cannot be established |
| `not applicable` | The capability cannot apply to the declared product or decision |

Capability presence does not prove quality, reliability, integration depth, customer adoption, realized value, or differentiation. Record dependencies, limits, setup, usage caps, support, failure states, and proof separately.

## Price And Offer Normalization

Preserve each original offer before normalization. Record customer and billing unit, quantity, usage, package, included limits, overage, minimum, commitment, contract term, currency, exchange-rate source and date, tax treatment, payment frequency, discount, promotion, implementation, migration, support, service, partner, and exit costs.

Compare bounded scenarios rather than one artificial unit:

```text
scenario total cost
= recurring fixed charges
+ expected metered usage and overages
+ required implementation and support
+ decision-relevant migration and operating costs
- evidenced eligible discounts or credits
```

Do not infer negotiated terms from list price, convert quote-only offers to zero, or call cheapest best value. Keep list, promotional, negotiated, legacy, and realized price states separate. Currency conversion enables arithmetic, not market equivalence.

## Scoring And Ranking

Prefer a criterion ledger, blocker view, and scenarios over one score. If a decision owner requires scoring:

1. define the exact choice and eligible alternatives;
2. derive criteria and direction from customer and operating evidence;
3. expose weights, transformations, missingness, and blocker rules;
4. keep evidence coverage separate from performance score;
5. run weight, missing-data, and scenario sensitivity;
6. show where rank changes and where alternatives are indistinguishable;
7. retain the underlying evidence and tradeoffs.

Never give unavailable evidence zero, use feature counts as value, average a verified blocker away, or present a weighted total as objective truth.

## Change Detection

Compare compatible snapshots and preserve both. A change row includes entity, product or offer version, market, field, prior and current states, source lineage, publication, capture, announced and effective dates, confidence, customer and decision consequence hypotheses, counterinterpretations, severity, owner, expiry, and next check.

Use these change states: `added`, `changed`, `removed`, `unchanged`, `reversed`, `rumored`, `disputed`, and `unknown`. Page wording, URL structure, missing documentation, screenshots, and sales reports may reflect measurement or publishing changes rather than product changes.

## Monitoring Rules

- Alert only when a verified or explicitly labeled signal crosses a declared decision threshold.
- Deduplicate repeated sources that share one origin.
- Require greater corroboration for claims with greater customer, legal, reputational, financial, or roadmap consequence.
- Expire rumors, stale claims, temporary promotions, and unverified states.
- Reopen the relevant decision; do not automatically change product, price, campaign, budget, positioning, or sales claims.
- Record false positives, missed changes, delayed verification, and decisions unaffected by the signal to improve the monitoring system.

Hiring, patents, partnerships, executive comments, and anonymous reports support bounded scenarios only. State what future observable evidence would strengthen, weaken, or falsify each scenario.
