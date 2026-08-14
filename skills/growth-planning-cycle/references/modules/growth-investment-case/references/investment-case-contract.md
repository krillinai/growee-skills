# Investment Case Contract

## Freeze One Decision Unit

An investment case governs one bounded future resource commitment. Record this contract before calculating value or recommending a decision.

| Field | Required definition |
| --- | --- |
| Mode | `audit`, `build`, or `refresh` |
| Decision | The exact commitment, release, continuation, expansion, pause, or exit decision |
| Owner | One accountable decision owner plus contributors, reviewers, and approvers |
| Scope | Product, customer, market, capability, program, asset, or operating unit and explicit exclusions |
| Horizon | Start, decision date, operating period, benefit maturity, terminal or exit period, and evidence cutoff |
| Baseline | Current-state and do-nothing path, including residual value, costs, risks, and obligations |
| Options | Preferred option plus credible smaller, staged, build, buy, partner, preserve, defer, stop, or exit alternatives |
| Resource unit | Cash, people, specialist time, customer exposure, data, capacity, management attention, or other constrained input |
| Target outcomes | Customer and business outcomes with entities, definitions, windows, and maturity |
| Strategy link | The versioned strategic choice, constraint, or portfolio bet this decision supports |
| External boundary | Local artifacts allowed; approval, systems, spend, contracts, contact, publication, and deployment excluded unless separately authorized |

Split cases when investments have materially different customers, products, markets, owners, economic bases, time horizons, risks, or decisions. A portfolio summary may coordinate cases, but it must not average incompatible units into one score.

## Evidence States

Use exactly:

- `verified`: attributable and inspectable within the declared source, version, and cutoff;
- `inferred`: reasoned from named evidence with assumptions and alternatives visible;
- `unavailable`: required but not supplied, accessible, mature, compatible, or measurable;
- `not applicable`: excluded by the contract with a reason.

Use `reported signal` for an attributable claim that is not independently verified. Keep actual, estimate, forecast, scenario, target, plan, benchmark, attribution, causal estimate, approval, zero, missing, immature, censored, and suppressed distinct.

For each material input preserve source, owner, date, lineage, entity, population or sample, segment, market, product and price version, period, currency, accounting and value basis, value or range, evidence state, freshness, limitation, contradiction, and next check.

Public artifacts verify visible claims and conditions at a dated capture. They do not establish private demand, behavior, conversion, retention, capacity, costs, contribution, cash, causal effect, readiness, approval, or outcomes.

## Establish The Baseline

The baseline is not automatically zero. Include:

- customer and business outcomes expected without the decision;
- existing product, program, contract, team, system, asset, and capability states;
- committed, unavoidable, avoidable, recoverable, and exit costs;
- residual revenue, contribution, cash, value, capacity, risk, and obligations;
- organic change, market change, decay, seasonality, and known concurrent initiatives;
- the evidence and uncertainty behind the path.

Exclude sunk cost from forward value except where a prior asset creates a current salvage, reuse, tax, contractual, or exit consequence. Do not continue an investment merely to recover sunk cost.

## Define Strategic Alignment

Record the selected strategy version, customer and market arena, value and mechanism thesis, portfolio class, exclusion boundaries, and capability commitment. Alignment is a gate, not a substitute for customer value, economics, feasibility, or risk. A strategically aligned proposal may still be deferred or rejected; an attractive standalone return may still conflict with an explicit strategy or crowd out a stronger option.

Route company-level arenas, portfolio, and exclusions to `growth-strategy`; the current primary constraint to `growth-diagnosis`; one product-market motion to `go-to-market-strategy`; and organization structure to `growth-organization-design`.

## Recommendation Semantics

Use one of these only when evidence distinguishes it:

| State | Meaning |
| --- | --- |
| `approve` | Evidence supports the defined commitment subject to named approval and controls |
| `bounded pilot` | A reversible, capped test can resolve a named decision uncertainty |
| `preserve option` | A limited commitment retains future choice at acceptable cost |
| `defer` | Prerequisites, timing, capacity, or evidence make the decision premature |
| `reject` | The bounded option fails a named value, strategic, economic, risk, or feasibility condition |
| `unresolved` | Available evidence cannot distinguish options; the next discriminating evidence is explicit |

These are analytical recommendations, never approvals, authorizations, budget releases, or executed decisions. Record decision owner, required approvers, conditions, expiry, and what new evidence can change the state.
