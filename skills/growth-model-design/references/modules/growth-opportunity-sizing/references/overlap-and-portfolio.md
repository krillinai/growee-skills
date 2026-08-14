# Overlap And Portfolio

## Build An Opportunity Graph

Map each opportunity to:

- eligible customer, account, participant, or transaction population;
- entry and outcome states;
- growth and value mechanism;
- channel, product, market, and segment;
- retained customer and business value units;
- timing, dependencies, capabilities, costs, and capacity;
- other opportunities that share or change any of these elements.

Use the graph to distinguish one opportunity described twice from two genuinely independent opportunities.

## Classify Relationships

| Relationship | Treatment |
| --- | --- |
| Mutually exclusive | Compare as alternatives; do not add |
| Upstream and downstream | Size the chain once; show stage sensitivities |
| Population overlap | Use attributable set intersection or leave adjustment unavailable |
| Value overlap | Reconcile to one retained outcome or economic ledger |
| Cannibalization or substitution | Subtract displaced value and cost on compatible bases |
| Reinforcement | Keep interaction conditional until evidence establishes it |
| Shared capacity or dependency | Constrain combined reach and sequence prerequisites |
| Independent | Add only after entity, outcome, timing, and dependency checks pass |

Do not apply a standard overlap haircut. If customer-level evidence is unnecessary or unavailable, use privacy-preserving aggregate intersections, bounded scenario cases, or an unresolved overlap register.

## Report Portfolio Layers

Return:

1. **gross ranges:** each opportunity before overlap and portfolio constraints;
2. **attributable adjustments:** observed overlap, cannibalization, dependency, capacity, timing, or shared cost;
3. **adjusted portfolio range:** only the portion supported by compatible evidence;
4. **unresolved interaction:** material relationships that prevent a credible combined estimate.

Never hide unresolved overlap inside a confidence score. A portfolio total may remain unavailable while individual ranges remain useful.

## Compare Decisions

Compare opportunities on:

- customer value and retained outcome;
- net economic range and cash timing;
- evidence coverage and dominant sensitivity;
- time to evidence and time to value;
- capability, capacity, dependency, and concentration;
- reversibility, downside, customer harm, trust, and regulatory exposure;
- opportunity cost, expiry, and strategic fit.

Avoid unsupported composite scores. If arithmetic ranking is invalid, use explicit decision classes:

| Class | Meaning |
| --- | --- |
| `advance` | Evidence and prerequisites support the next bounded commitment |
| `validate` | A specific uncertainty must be resolved before commitment |
| `preserve` | Maintain a low-cost option while waiting for a trigger |
| `defer` | A prerequisite, capacity limit, or better use of resources blocks action |
| `reject` | Evidence or economics do not support further work under the current contract |
| `route` | Another specialist decision owns the next artifact |

For every class record owner, rationale, evidence gate, expiry, scale, cap, stop, fallback, and review trigger. Route final strategic portfolio choices to `growth-strategy` and the current primary constraint to `growth-diagnosis`.
