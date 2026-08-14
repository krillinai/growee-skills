# Paths, Blueprint, Friction, And Measurement

## Contents

1. State graph and journey variants
2. Touchpoints and continuity
3. Service blueprint
4. Friction and opportunity evidence
5. Failure, recovery, accessibility, and exit
6. Transition and outcome measurement

## State Graph And Journey Variants

Model the journey as a directed graph. For each state record:

| State / version | Eligible entity and role | Entry rule and evidence | Customer job and value | Owner and time boundary | Exit rule / next states | Failure / pause / exit |
| --- | --- | --- | --- | --- | --- | --- |

For each transition record origin, destination, eligible population, trigger, customer action, visible interaction, backstage response, identity, source, timestamp rule, completion evidence, duration, failure, retry, reversal, owner, and metric version.

States must be mutually interpretable, not necessarily mutually exclusive. If a person, account, contract, or transaction can occupy several states, state the entity and parallel dimensions explicitly. Do not force product use, buying, payment, service, and account-health states into one ordinal label.

Include only applicable states among:

- problem trigger, passive or active discovery, peer or partner influence, evaluation, comparison and proof;
- qualification, buying-group alignment, approval, procurement, security, commercial agreement and payment;
- eligibility, invitation, access, setup, migration, first useful task, first value and repeated value;
- collaboration, habit, workflow adoption, renewal, expansion, contraction, advocacy or referral;
- confusion, block, failure, retry, workaround, support, recovery, pause, downgrade, cancellation, churn, exit and re-entry.

Preserve branches, skips, loops, reversals, pauses, parallel paths, assisted and self-serve paths, nonprogression, ineligibility, unknown state, and terminal exit. Do not label a universal stage list as observed evidence.

Define journey variants only when role, job, product, offer, entry source, service model, market, device, access, authority, failure mode, or other evidence changes the path or decision. Do not create variants from unsupported demographics or decorative personas.

## Touchpoints And Continuity

A touchpoint is a bounded customer-visible interaction or artifact, not every internal task.

| Touchpoint / version | Role / origin and destination state | Job / content / claim / source | Channel / eligibility / permission | Timing / frequency / accessibility / locale | Response / delivery evidence / owner | Correction / fallback / expiry |
| --- | --- | --- | --- | --- | --- | --- |

Track supply and response states separately:

```text
created -> reviewed -> approved -> available or scheduled -> sent or displayed
-> delivered -> viewable -> exposed -> interacted -> comprehended
-> task completed -> customer value -> repeated value
```

Not every touchpoint uses every state. Delivery, view, click, attendance, call, login, or closure proves only its defined signal. It does not prove comprehension, consent, task completion, problem resolution, customer value, or impact.

Audit continuity across channels and owners:

- consistent product, offer, claim, status, price, entitlement, timeline and next step;
- context carried forward without repeated customer effort or excessive personal-data sharing;
- identity and permission preserved or deliberately re-established;
- clear ownership, handoff acceptance, response expectation, escalation and fallback;
- duplicate, contradictory, inaccessible, expired, mistimed, coercive and unnecessary interactions;
- customer-visible status, correction, cancellation, support and recovery.

More interactions are not better. A useful path can remove, combine, resequence, explain, assist, or add a touchpoint depending on evidence.

## Service Blueprint

For each material state or transition map these layers:

| Layer | Required fields |
| --- | --- |
| Customer | Role, action, evidence, effort, value, failure and next state |
| Frontstage | Visible person, partner, product, message, artifact, channel, promise and status |
| Backstage | Workflow, queue, review, manual work, exception, owner, capacity and service expectation |
| System and data | Product, identity, entitlement, inventory, CRM, billing, payment, support, integration, vendor, event, source, interface and version |
| Policy and control | Eligibility, permission, consent, security, privacy, safety, contract, approval, audit, retention and appeal |
| Measurement | State evidence, metric version, timestamp, quality, maturity, failure and guardrail |

For every handoff define sender, receiver, object, exact state and version, required context, minimum data, permission, acceptance, time expectation, failure signal, fallback, escalation, acknowledgement, completion proof, and residual owner.

Map queues, workarounds, manual reconciliation, duplicate entry, partial automation, vendor dependency, capacity, blackout periods, incident ownership, downstream consumers, and residual obligations. A frontstage promise is not delivered value until the backstage and system state is verified for the relevant customer.

Do not infer internal systems, operating steps, owners, reliability, or service levels from public customer-facing pages. Mark unavailable fields and request the smallest decision-changing evidence.

## Friction And Opportunity Evidence

Friction is role- and context-specific effort, delay, uncertainty, repetition, interruption, cognitive load, coordination, access burden, financial burden, risk, or trust cost. Classify each item:

| Class | Meaning |
| --- | --- |
| `value-enabling` | Work integral to creating or tailoring customer value |
| `necessary` | Work required by a valid operating dependency |
| `protective` | Deliberate control for consent, trust, safety, security, fairness or customer protection |
| `avoidable` | Work or delay not required for value or a valid control |
| `transferred` | Internal convenience creates customer, partner or downstream work |
| `deceptive` | Obstruction, hidden choice, misdirection or coercion benefits the operator at customer expense |
| `unknown` | Evidence cannot distinguish the purpose or mechanism |

Record role, state or transition, exact observation or report, source, frequency or prevalence if supplied, affected population, customer and operating effect, candidate mechanisms, counterevidence, protection served, owner, uncertainty, and next discriminating evidence.

Keep these levels separate:

```text
observed loss or duration
reported difficulty
analyst interpretation
candidate mechanism
validated mechanism
root-cause claim
causal effect of an intervention
```

Do not name a root cause from sequence, correlation, one complaint, one aggregate loss, or stakeholder belief. Do not fabricate impact, effort, confidence, emotion or priority scores. If supplied scoring inputs are used, show definitions, evidence, formula, weights, missing fields and sensitivity; never let the score hide customer harm, controls, dependencies or uncertainty.

Compare possible dispositions: retain, explain, simplify, remove, combine, resequence, prefill, automate, provide choice, add assistance, create fallback, repair dependency, test, investigate, or route. A recommendation needs customer effect, operating effect, evidence, risk, dependency, owner, measurement, guardrail, stop and reversal condition.

## Failure, Recovery, Accessibility, And Exit

Map failure as a path, not a note:

```text
failure condition -> detection -> customer visibility -> containment
-> status and help -> retry, workaround, fallback or reversal
-> technical resolution -> customer task resolution -> service recovery
-> trust recovery -> repeated value, departure or residual harm
```

Record affected entity and population, severity, source, start, duration, owner, promise, channel, support, capacity, workaround, correction, compensation if applicable, appeal, guardrail, escalation, recovery proof and residual obligation. Ticket closure is not customer task resolution; technical recovery is not trust recovery or retained value.

For accessibility and inclusion, test role, ability, language, literacy, device, connectivity, identity, authority, time, environment and assisted-use conditions from attributable evidence. Map alternate format, keyboard or assistive access, caption or transcript, readable language, proxy or delegated path, low-bandwidth path, offline or human help, safe feedback, correction and appeal as applicable. Do not stereotype or claim legal compliance.

For exit, map pause, downgrade, cancellation intent, cancellation, contract end, export, refund, deletion request, entitlement end, access end, support, invoice and payment closure, retained data, downstream propagation, appeal, re-entry and residual obligations. Preserve clear choice, consequences, confirmation, status, timing and correction. Do not call obstruction, forced calls, hidden controls, repeated prompts, delayed refunds or blocked exports retention.

## Transition And Outcome Measurement

Every rate or duration needs:

| Metric / version | Entity / role / eligible population | Numerator / denominator / state rule | Identity / source / timestamp | Market / channel / cohort / period / window | Maturity / exclusions / late data / suppression | Owner / quality / limitation / review |
| --- | --- | --- | --- | --- | --- | --- |

Keep counts beside rates. Where relevant show transition-time distributions, not only averages. Preserve missing, unavailable, late, immature, censored, suppressed, revised, disputed, estimated, valid zero and not applicable states.

Measure separately:

1. source and journey-map coverage;
2. touchpoint availability, delivery, viewability and interaction;
3. eligibility, access, state entry, transition completion and failure;
4. effort, time, retries, workarounds, support and recovery;
5. first, repeated, retained, expanded or restored customer value;
6. trust, accessibility, safety, privacy, fairness and customer harm;
7. purchase, revenue, contribution, cash and other business outcomes;
8. assignment, exposure, adoption and causal effect of a journey intervention.

Do not average ad reach, page activity, messages, product events, tickets, NPS, renewal and revenue across people and accounts into one journey score. Do not fill unavailable evidence with zero. A before-and-after outcome can nominate a hypothesis; it does not prove the map or redesign caused the change.
