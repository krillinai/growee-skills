# Popup Measurement And Experiments

## Event Contract

Define events for eligibility, assignment, trigger, render, viewability, exposure, interaction, dismissal type, close, form start, field error, submit, consent, success, destination, failure, opt-out, complaint, and suppression. Include popup and content version, page, source, audience, lifecycle, device, viewport, market, language, identity, session, experiment, timestamp, and reason.

Do not infer exposure from render. Define viewability and minimum exposure only when needed and justified. Do not record raw field values, message text, or unnecessary identifiers in analytics.

## Outcome Layers

Measure together:

- popup: exposure, comprehension proxy, interaction, dismissal, form and error;
- underlying task: page or product completion, abandonment, back, scroll, media, search, cart, or workflow;
- permission and delivery: valid consent, deliverability, unsubscribe, complaint, suppression, and channel cost;
- customer: qualified arrival, first value, time to value, retention, refund, support, and trust;
- business: retained revenue or contribution, full cost, cannibalization, and capacity;
- experience: accessibility, performance, errors, collisions, rage interactions, and repeated interruption;
- causal: effect under valid assignment, exposure, maturity, and interference assumptions.

## Diagnosis

Observed patterns narrow investigation:

- high exposure, low interaction: relevance, offer, message, proof, surface, or measurement;
- high interaction, low completion: form, permission, errors, price, expectation, or trust;
- high capture, low delivery: data quality, permission, channel, suppression, or fulfillment;
- high local conversion, harmed page task: interruption or denominator substitution;
- strong immediate result, weak downstream value: audience, incentive, promise, product, or maturity;
- mobile or assistive harm: layout, focus, keyboard, touch, motion, performance, or QA.

Do not assign cause from the pattern alone.

## Experiment Contract

Record decision, hypothesis, mechanism, eligible population, exclusions, randomization unit, assignment, exposure, control, treatment, primary outcome, diagnostics, guardrails, minimum meaningful effect, sample and duration assumptions, observation and maturation windows, identity, repeated exposure, interference, SRM, analysis, positive, negative, harmful and inconclusive rules, stop, rollback, owner, and follow-up.

Preserve treatment assignment and popup version through downstream readout. Check novelty, primacy, contamination, concurrent campaigns, page changes, cookie or consent changes, and device switching. Route detailed statistical design to `experiment-design`.
