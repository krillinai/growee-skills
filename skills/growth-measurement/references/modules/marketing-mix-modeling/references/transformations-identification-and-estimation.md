# Transformations, Identification, And Estimation

## Transformation Contract

For each media or growth input record raw unit, scaling, lag, carryover kernel, decay or duration, saturation or diminishing-return form, threshold, interaction, hierarchy, constraints, prior, parameter bounds, evidence, sensitivity range, version, and rationale.

Common families include:

| Need | Candidate forms | Main risk |
| --- | --- | --- |
| Carryover | Geometric adstock, Weibull survival, finite or distributed lag | One decay hides channel and market timing |
| Saturation | Hill, logistic, Michaelis-Menten, spline, monotone function | Sparse high-spend support creates unstable extrapolation |
| Threshold | Hurdle, piecewise, spline, explicit minimum exposure | Artificial thresholds can absorb noise or flighting |
| Interaction | Predeclared product, channel, market, or sequence term | Combinatorial overfit and weak identification |
| Hierarchy | Separate, partial pooling, random or fixed effects | Invalid exchangeability can erase local structure |

Do not choose a form because it is fashionable or default. Compare plausible forms against channel mechanism, timing, data support, diagnostics, experiments, stability, and decision sensitivity. Preserve prior and constraint sensitivity.

## Identification Register

| Threat | Diagnostic evidence | Permitted response | Residual limitation |
| --- | --- | --- | --- |
| Collinearity | Correlations, design rank, VIF, posterior dependence, unstable contribution | Group channels, partial pooling, informative evidence, planned variation | Individual effects may remain unresolved |
| Spend endogeneity | Budgets respond to demand, forecasts, outcomes, auctions, or local judgment | Experiments, instruments, timing, controls, bounds, explicit priors | Association may remain noncausal |
| Reverse causality | Search, retargeting, or spend follows existing intent | Lag structure, intent controls, experiments, shutdown or geo evidence | Harvesting and creation may not separate |
| Omitted variables | Price, promotion, inventory, distribution, product, competitor, macro shocks | Add defensible observed causes, fixed effects, sensitivity, bounds | Unobserved confounding remains |
| Measurement error | Changing platform coverage, privacy, invalid exposure, spend revisions | Reconcile sources, latent or error model, sensitivity, exclusion | Attenuation or bias may remain |
| Interference | Cross-market spillover, shared audiences, network or brand effects | Larger units, spillover terms, geographic or time designs | Stable-unit assumptions may fail |
| Structural break | Product, price, platform, market, policy, tracking, or behavior changes | Segment periods, varying parameters, refresh or retire | Old response may not transfer |

Highest fit does not resolve identification. Record what variation identifies each decision-relevant effect and what evidence would falsify it.

## Priors And Constraints

State the source, population, period, estimand, transformation, scale, uncertainty, and transfer argument for every informative prior or coefficient constraint. A vendor default, prior model, public benchmark, platform study, expert belief, or experiment can inform a prior only after compatibility review.

Positivity, monotonicity, diminishing returns, maximum carryover, and interaction restrictions are assumptions. Test their influence on contribution, response, and decisions. Do not force positive effects merely to make the output easier to allocate.

## Estimation Specification

Use a model family that matches outcome distribution, panel structure, hierarchy, seasonality, trend, lag, missingness, uncertainty, and decision. Frequentist and Bayesian approaches can both be valid; neither creates identification by itself.

Record outcome likelihood or error model, link, baseline, trend, seasonal terms, context variables, transformed media, hierarchy, interactions, priors or penalties, constraints, estimation algorithm, convergence criteria, random seed where relevant, software and code version, holdout rule, and output estimands.

Compare complexity against a reproducible naive or seasonal baseline and a simpler nested model. Do not select solely on training fit, one information criterion, one posterior summary, or a preferred contribution story.

## Contribution Reconciliation

Reconcile for each period and market:

```text
observed outcome
= modeled baseline and context contribution
+ modeled media and other input contribution
+ modeled interactions
+ residual or unexplained component
```

The equation is a reporting bridge, not proof that every component is causal. Show joint and unresolved components, uncertainty, covariance, prior sensitivity, and residual. The intercept or baseline is not automatically organic demand, and paid-media contribution is not automatically retained contribution.

## Response Support

For every response curve record observed spend and exposure distribution, effective sample support, flighting pattern, markets, periods, transformation, average and marginal estimand, uncertainty, covariance, saturation, and sensitivity. Distinguish interpolation from extrapolation. Refuse or visibly bound scenarios beyond supported ranges.
