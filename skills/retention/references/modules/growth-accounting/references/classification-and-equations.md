# Classification And Equations

Use mutually exclusive classes and retain unresolved records until evidence supports a class. Test equations in absolute units before calculating rates.

## Classification Precedence

A practical precedence is:

1. exclude entities outside declared eligibility;
2. isolate transfers, migrations, acquisitions, disposals, reclassifications, deletions, and corrections;
3. mark insufficient identity, history, observation, or maturity `unresolved`;
4. classify first-ever qualified entry `new` only with sufficient prior history;
5. classify qualified return after the declared inactive interval `resurrected`;
6. classify active at both compatible states `retained`;
7. classify mature opening entities crossing the declared inactive or terminated state `churned`.

Use `reactivated` for a short lapse if the product contract distinguishes it from resurrection. Preserve cancellations pending grace, paused contracts, seasonal dormancy, account transfers, and product migrations separately when they do not meet churn or resurrection definitions.

## Active-Entity Bridge

Under one compatible scope:

```text
opening active = retained + churned + opening transfers or corrections
closing active = retained + new + resurrected + closing transfers or corrections
net active change = new + resurrected - churned + net adjustments
```

Show an opening and closing residual. An equation can fail because of overlapping classes, missing entities, inconsistent cutoffs, identity changes, incomplete history, late data, or a wrong opening or closing source. Do not plug a residual into `other` without an attributable definition.

## Recurring-Value Bridge

Use one entity, currency, value basis, and period:

```text
closing recurring value
= opening recurring value
+ new + resurrection + expansion
- contraction - churn
+ FX + acquisition or disposal + migration + reclassification + correction
```

Expansion and contraction apply to the compatible opening customer base. New and resurrection belong outside that base. Churn removes the declared opening value under the bridge policy. Preserve partial churn, downgrade, seat reduction, usage decline, price change, refunds, and credits according to the chosen value contract.

## Metric Contracts

| Metric | Contract |
| --- | --- |
| Logo retention | Retained opening entities / eligible opening entities |
| Logo churn | Mature churned opening entities / eligible mature opening entities |
| Gross value retention | Compatible opening value after contraction and churn, before expansion / eligible opening value |
| Net value retention | Compatible opening value after expansion, contraction, and churn / eligible opening value |
| New share | New closing entities or value / declared compatible closing or movement base |
| Resurrection share | Resurrected closing entities or value / declared compatible closing or movement base |
| Net growth | Closing minus opening compatible value / opening compatible value |

Name numerator, denominator, entity, value basis, window, maturity, exclusions, rounding, and source. Do not use one formula across subscriptions, low-frequency products, seasonal businesses, marketplaces, and usage models without validating opportunity and state semantics.

## History, Maturity, And Revision

First observed is not first-ever when history is truncated. Missing and suppressed are not inactive. An entity is not churned until the declared observation, grace, latency, and maturity conditions are met. Version classifications and actuals; preserve late events, identity corrections, refunds, reversals, and definition changes in a revision bridge rather than rewriting prior releases.
