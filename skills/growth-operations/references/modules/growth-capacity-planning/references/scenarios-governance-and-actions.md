# Scenarios, Governance, And Actions

## Capacity Scenarios

Build only scenarios that can change a decision. Keep observed demand, forecast, target, plan, commitment, and scenario separate.

| Scenario field | Required content |
| --- | --- |
| Identity | Name, version, owner, horizon, market, service, as-of and expiry |
| Condition | Trigger, supplied demand series, assumptions, contradictions, uncertainty |
| Load | Work items, mix, peaks, timing, service classes, workload conversions |
| Capacity | Effective, reserved, allocatable, shared, surge, contingency, and recovery capacity by native unit |
| Result | Constraint, queue or service range, gap or surplus, sensitivity, residual risk |
| Decision | Robust commitment, reversible option, irreversible commitment, latest useful date, stop and recovery rule |

Use base, upside, downside, surge, stress, recovery, or other names only when their conditions are defined. Do not invent probabilities, average incompatible scenarios, size to a maximum without consequence analysis, or call a target, plan, forecast, and upside scenario independent demand.

## Gap And Option Register

When compatible demand exceeds effective capacity, state the gap by unit, service, period, market, evidence, and uncertainty. Compare options without selecting or executing them:

| Option | Examples | Evidence to compare |
| --- | --- | --- |
| Remove or reduce demand | Eliminate low-value work, reduce scope, improve eligibility | Customer effect, protected obligations, decision authority |
| Shape flow | Smooth arrivals, sequence work, change batch or service class | Variability, queue, lead time, fairness, deadline consequence |
| Improve effective capacity | Reduce rework, standardize, cross-train, automate | Demonstrated throughput, quality, ramp, maintenance, failure |
| Add external capacity | Buy, outsource, reserve supplier or infrastructure capacity | Lead time, restrictions, reliability, lock-in, cost, exit |
| Add internal capacity | Hire, redeploy, change organization | Skill, hiring time, ramp, management load, long-term need |
| Change service | Adjust promise, admission, hours, region, or quality within authorization | Customer harm, accessibility, contractual and operating constraints |
| Accept risk | Preserve current state temporarily | Accountable acceptance, limit, trigger, monitoring, expiry, recovery |

For each option preserve lead time, ramp, reversibility, reliability, dependency, cost basis, customer and employee effect, privacy and safety, trigger, acceptance evidence, approver, residual gap, residual risk, and exit. Route hiring, budget, organization, investment, procurement, infrastructure, prioritization, and initiative scheduling to their owners. Do not invent vendors, amounts, headcount, dates, owners, or approvals.

## Domain Boundaries

### Experimentation

Separate eligible experimental units, assignment, exposure, traffic, duration, maturation, interference, control reuse, novelty, sample ratio mismatch, guardrails, customer attention, platform throughput, analyst review, engineering work, and decision capacity. Capacity does not authorize unlimited concurrency or promise wins. Route design to `growth-measurement` and the portfolio to `growth-operations`.

### B2B And Revenue Operations

Separate lead, contact, account, opportunity, contract, implementation, user, seat, case, renewal, and revenue entities. Define stage-specific arrival, workload, skill, service, acceptance, completion, product, segment, territory, language, timezone, complexity, handoff, and ramp. Do not combine them into one account-capacity number or assign territories and quotas. Route operational design to `growth-operations`.

### Product And Cloud Systems

Define request, workload shape, concurrency, peak, product path, region, latency distribution, memory, database, network, rate limit, dependencies, saturation, retries, errors, timeouts, degradation, failover, incidents, recovery, cost, quotas, load tests, monitoring, stop, and rollback. Separate theoretical, tested, reliable, surge, and recovered capacity. Average CPU or provider quota is not end-to-end certification. Route implementation and reliability approval to accountable technical owners.

### Marketplaces

Define participant sides, local network, geography, time, product, listing or inventory freshness, availability, positioning, concurrency, perishability, transferability, demand opportunity, match, fulfillment, cancellation, quality, incentives, multi-homing, concentration, participant economics, trust, and support. Keep liquidity, operational capacity, system capacity, GMV, inventory, and staff separate. Route network, inventory, pricing, economics, and market decisions to their owners.

## Market Transfer

Revalidate customer, product, market, platforms, demand, workload, calendars, skills, providers, vendors, costs, holidays, lead times, support, service, data access, privacy, owners, and evidence in each market.

For China, separate legal entity, language, locale, currency, timezone, product, app distribution, identity, payment, invoice, data, consent, privacy, staffing, vendors, holidays, support, and local review. Use current direct evidence and locally accountable expertise. Do not copy US ratios, providers, service levels, calendars, or capacity targets. Translation and currency conversion are not operational validation. Avoid legal, labor, tax, regulatory, provider, approval, accounting, or performance conclusions.

## Workforce Privacy And Fairness

Use aggregate, redacted, pseudonymous, minimum-necessary, and small-cell-suppressed evidence. Define purpose, accountable basis, authority or consent where applicable, access, retention, deletion, correction, audit, fairness, accessibility, employee health, dissent, appeal, and independent review.

Do not ingest private messages, keystrokes, health data, protected traits, compensation, reviews, precise locations, private customer data, or full histories to score people. Do not rank named individuals for productivity or capacity or use a capacity model to set workloads, deny leave, change compensation, or make employment decisions.

## External Actions

The default deliverable is a local specification, audit, option register, monitoring contract, or approval-ready handoff. Do not access authenticated systems; export or join private data; change staffing, budgets, quotas, schedules, priorities, systems, or infrastructure; sign, assign, hire, procure, deploy, publish, send, or contact people; or claim improvement. Record requested action, accountable owner, evidence, approver, prerequisites, safeguards, rollback, verification, and residual obligations for separate authorization.
