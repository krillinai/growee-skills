# Models And Journeys

## Attribution Views

| View | Useful operational question | Main limitation |
| --- | --- | --- |
| First touch | Where did the observable journey begin under this identity and window? | Misses later evaluation and re-entry; identity start may be incomplete |
| Last touch | Which eligible touch immediately preceded the outcome? | Overcredits closers, direct suppression rules, and captured intent |
| Linear | Which eligible touches appeared in the journey? | Equal weights are a convention, not evidence of equal contribution |
| Position based | How do declared opening and closing roles divide credit? | Weights are assumptions and can hide middle mechanisms |
| Time decay | Which recent touches receive more operating credit? | Decay and time basis are chosen, not causal truth |
| Platform or partner | What does one provider claim under its own rules? | Claims overlap and use provider identity, windows, and objectives |
| MMP or app rule | Which eligible app source receives install or event credit? | Web, restore, existing-account, SKAdNetwork, privacy, and provider views may differ |
| Opportunity or account source | Which source is attached to a lead, account, or opportunity? | Buying groups and prior product or content journeys are compressed |
| Algorithmic | What pattern does a versioned model assign under supplied data? | Leakage, opacity, missingness, confounding, and drift can mislead |

Do not use one view for every decision. Operational routing, partner settlement, campaign reporting, journey description, financial reconciliation, and causal allocation may require different views that share a common outcome and identity contract.

## Model Sensitivity Table

For every candidate model, report rule, decision use, eligible touches, identity coverage, lookback, direct and unknown handling, total outcomes, source credit, downstream value, stability, segment variation, reconciliation gap, interpretability, gaming risk, privacy, and limitations.

Disagreement is information. It reveals where credit depends on assumptions. Do not choose the model that produces the preferred channel ranking.

## Journey Rules

Freeze:

1. journey entity and start state;
2. eligible touchpoint families and exclusions;
3. identity resolution available at each touch;
4. event time, processing time, timezone, and late arrival;
5. lookback and conversion windows;
6. session and direct-return behavior;
7. campaign, channel, branded, partner, and internal precedence;
8. new, returning, reactivated, existing-customer, and expansion states;
9. conversion, first value, retained value, commercial, and refund maturity;
10. concurrent product, price, market, campaign, or tracking changes.

## B2B And Account Journeys

Separate person, contact, role, account, buying group, opportunity, product workspace, contract, subscription, payer, and beneficiary. An analyst, champion, admin, buyer, approver, procurement, security reviewer, executive, signer, and payer can contribute to one account journey without being interchangeable.

Define whether attribution supports lead routing, account source, opportunity influence, partner settlement, pipeline reporting, customer acquisition, or retained account value. Do not call content opens, seller touches, opportunity attribution, pipeline, bookings, or signatures realized customer value.

## App, Web, And Cross-Device Journeys

Keep web session, app-store discovery, ad click, install, first open, reinstall, restore, login, account creation, subscription, in-app order, web payment, and product value separate. Reconcile platform, MMP, app store, product, billing, and finance sources without summing claims.

State device and app instance, user and account identity, consent, new versus existing status, install and reattribution window, click and view precedence, privacy-preserving aggregate data, and cross-context join authority. A restored account is not necessarily a newly acquired customer.

## Marketplace, Network, And Portfolio Journeys

Preserve participant side, local network or market, transaction, supply or demand role, product, portfolio, and cannibalization. One source can acquire one participant while another mechanism creates the successful interaction. Route network and marketplace causal mechanisms to `growth-loop-design` and product-to-product expansion to `customer-expansion-strategy`.
