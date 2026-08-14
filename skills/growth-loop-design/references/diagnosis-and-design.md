# Diagnosis And Design

Diagnose the current value and closure evidence before choosing mechanics. A popular loop pattern is not a product strategy.

## Contents

- [Diagnose The Weak Transition](#diagnose-the-weak-transition)
- [Select A Constraint](#select-a-constraint)
- [Design From Value](#design-from-value)
- [Design Contract](#design-contract)
- [Family Design Checks](#family-design-checks)
- [Incentives And Rewards](#incentives-and-rewards)
- [30-Day Validation Plan](#30-day-validation-plan)
- [Routing](#routing)
- [External Execution Gate](#external-execution-gate)

## Diagnose The Weak Transition

Start with what is observed:

| Observed pattern | Competing checks |
| --- | --- |
| Low participation | Source value, eligibility, awareness, motivation, timing, effort, trust, measurement |
| High output, few qualified inputs | Output usefulness, relevance, overlap, reachability, permissions, delivery, spam controls |
| Inputs arrive, response is weak | Context, credibility, recipient job, channel, landing state, fatigue, market fit |
| Response is strong, realized value is weak | Product readiness, permissions, setup, promise continuity, supply, trust, support |
| Value is reached, retention is weak | Recipient quality, natural cadence, recurring value, incentives, cohort maturity, measurement |
| Retention is healthy, re-entry is weak | Value-producing opportunity, collaboration or contribution fit, discoverability, capacity, cycle delay |
| Attributed loop outcomes are strong, total lift is weak | Organic overlap, self-selection, cannibalization, assignment, identity, counterfactual evidence |
| Gross yield is strong, economics or trust are weak | Rewards, fraud, support, variable cost, refunds, complaints, platform or recipient harm |

An observed transition rate identifies where loss appears, not why. Keep measurement changes, customer mix, seasonality, market events, platform policy, and system incidents visible.

## Select A Constraint

Name one primary constraint only when:

1. the transition is measured with compatible mature evidence;
2. the mechanism is plausibly connected to the qualified next-cycle outcome;
3. evidence distinguishes it from important alternatives;
4. the constraint can change within the decision horizon;
5. removing it does not violate value, trust, economics, capacity, or safety guardrails.

Otherwise return a ranked alternative set and make the smallest discriminating evidence the priority action. Do not name the lowest conversion rate, longest delay, smallest side, or largest volume as the constraint by default.

## Design From Value

Use this order:

```text
existing source value
-> receiving entity or system value
-> qualified next input
-> natural value-producing action
-> useful output
-> context and delivery
-> realized value
-> retained quality or matured economics
-> credible re-entry
-> measurement and validation
```

Do not start with an invite button, referral reward, sharing prompt, content quota, marketplace subsidy, ad budget, AI generation volume, or personalization model. Those are possible mechanics after prerequisites are supported.

## Design Contract

For each proposed mechanism, record:

| Field | Requirement |
| --- | --- |
| Hypothesis | How a declared value-producing action creates a qualified later input |
| Family | Collaboration, referral, content, marketplace, reinvestment, data, or another bounded family |
| Entities and value | Source, recipient or receiving system, payer or administrator, platform, and business value |
| Eligibility | Who can participate, who should not, and what opportunity exists |
| Action and output | Natural job, useful artifact or resource, and qualification rule |
| Context and response | How the next input arrives and what relevant action follows |
| Closure | Realized value, retained quality or matured economics, and later participation |
| Evidence | Verified facts, signals, inferences, unavailable inputs, and counterevidence |
| Measures | Transition counts, quality, cycle time, economics, saturation, and guardrails |
| Risks | Trust, abuse, cannibalization, congestion, privacy, fairness, operations, dependency, and decay |
| Validation | Owner, eligible population, evidence or experiment, maturity, decision rule, stop rule, and completion proof |

Offer multiple mechanism hypotheses only when their value and prerequisites differ. Do not produce a long feature backlog to compensate for missing mechanism evidence.

## Family Design Checks

### Collaboration Or Referral

- Has the source received enough value to share credibly?
- Does the payload carry an artifact, role, context, or proof that helps the recipient?
- Are relevance, permission, recipient control, and social trust preserved?
- Does recipient value strengthen the original relationship or create a later natural opportunity?
- Are organic behavior, prompted behavior, rewards, overlap, retained quality, and abuse separable?

### Content Or UGC

- Does a real demand or customer job select the topic or contribution?
- Why will a qualified contributor create, review, or refresh the output?
- What makes the output useful, original, attributable, correctable, and discoverable?
- Does discovery lead to recipient value and retained demand rather than traffic alone?
- Can moderation, decay, rights, spam, misinformation, and platform dependency remain controlled?

### Marketplace Or Network

- What works before the network is large?
- What is the smallest network unit and successful core interaction?
- Which side, asset, trust condition, or behavior constrains value now?
- Does added relevant participation improve selection, speed, quality, trust, or economics?
- Can an adjacent unit reach healthy value without permanent subsidy or fragmenting the core?

### Paid Reinvestment Or Sales Capacity

- Is the qualified outcome mature and connected to retained contribution?
- Are marginal acquisition cost, payback, cash timing, capacity, saturation, and downside visible?
- What approval converts matured contribution into a bounded later investment?
- Does the later investment reach a comparable qualified cohort?
- Is attributed demand separated from incremental demand and channel concentration?

### Data Or Product Improvement

- Is data collection necessary, permissioned, representative, and bounded?
- Which observable product outcome improves and for whom?
- Does improvement create realized customer value and later adoption or retention?
- Are excluded populations, bias, drift, gaming, feedback amplification, safety, and overrides monitored?
- Is the mechanism reproducible by competitors or dependent on outside platforms?

## Incentives And Rewards

Rewards can compensate effort or reinforce product value, but can also purchase low-quality action. Before proposing them, require:

- sender and recipient value without the reward;
- organic behavior baseline and a credible counterfactual;
- reward eligibility, cost, accounting, timing, taper, and stop rule;
- recipient activation and post-reward retention;
- self-referral, multi-account, device, payment, graph, collusion, and fraud controls;
- cannibalization, portfolio effects, trust, fairness, and applicable review.

Do not issue rewards, create referral codes, or recommend a universal incentive amount.

## 30-Day Validation Plan

Order work by dependency:

1. freeze entities, eligibility, value, events, identity, cohorts, and windows;
2. reconcile current transition counts and missingness;
3. collect the smallest customer, operational, economic, trust, or system evidence that distinguishes mechanisms;
4. preregister a bounded test when causal evidence is needed;
5. preserve assignment through activation, retention, contribution, and guardrail maturity;
6. review the verdict and decide whether to stop, revise, extend, or hand off.

Every action needs an owner, decision date, dependency, guardrail, and completion proof. Every experiment needs the eligible unit, assignment, exposure, primary metric, downstream quality, guardrails, maturation, interference treatment, decision rule, and stop or rollback rule. Route the full design to `experiment-design`.

Do not set an uplift, K-factor, participation, conversion, cycle-time, payback, saturation, or budget threshold unless it comes from declared business requirements or a prospectively approved design.

## Routing

| Need | Route |
| --- | --- |
| Transition and denominator analysis | `growth-diagnosis` |
| First value and onboarding | `activation` |
| Recurring value, churn, or resurrection | `retention` |
| Pricing, rewards economics, contribution, or payback | `monetization` |
| Customer motivation, jobs, trust, or mechanism research | `customer-research` |
| Causal test design and interpretation | `experiment-design` |
| Campaign journey or asset requirements | `acquisition-strategy` |
| Primary constraint across the complete growth system | `growth-diagnosis` |

Growth Loop Design can specify a required message, product surface, reward, event, campaign, or experiment. It does not create, publish, send, issue, deploy, or launch it.

## External Execution Gate

Do not access production systems, private graphs, contacts, CRM, analytics, warehouses, billing, payments, ads, messaging, publishing, referral platforms, experiments, or product configuration. Do not upload contacts, auto-invite recipients, issue codes or rewards, buy media, change pricing, deploy events, alter ranking, publish content, or claim execution.

An operational handoff must separately establish task-level authorization, system capability, least privilege, consent, privacy and abuse review, financial and product approval, eligible population, monitoring, incident ownership, stop and rollback controls, audit logs, and result maturation.
