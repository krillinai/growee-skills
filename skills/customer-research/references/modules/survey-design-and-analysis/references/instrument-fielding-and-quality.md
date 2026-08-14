# Instrument, Fielding, And Response Quality

## Item-Purpose Map

Give every displayed or derived item a stable ID and version.

| Item / version | Construct / decision use | Eligible respondent / reference event / timeframe | Wording / stimulus / source | Options / scale / required state | Order / randomization / logic / piping | Analysis / denominator / removal consequence |
| --- | --- | --- | --- | --- | --- | --- |

Remove an item that has no distinct decision use, construct role, eligibility, or analysis rule. Preserve screening, consent, routing, quality, open-text, demographic, and outcome items as separate roles. Do not collect a variable merely because it may be interesting later.

## Wording Audit

Identify leading, loaded, assumptive, causal, double-barreled, hypothetical, and excessive-recall wording. Check every item for:

- one question, construct, reference object, and timeframe;
- language the target respondent can understand without internal terminology;
- neutral framing without desired answers, unsupported premises, blame, status pressure, or sponsor cues;
- answerability from the respondent's role, memory, access, and experience;
- recall demand, telescoping, recency, social desirability, acquiescence, and hypothetical bias;
- balanced treatment of positive, negative, neutral, absent, uncertain, and inapplicable states;
- sensitive or consequential content with necessity, optionality, explanation, and safe handling;
- exact stimulus, product, package, price, currency, market, and version when judgment depends on them.

Do not ask respondents to estimate facts they cannot observe. Prefer a concrete recent event over a general identity claim when the decision concerns experience. Separate unaided recall from aided recognition and measure unaided response before exposing answers or promotional stimuli.

## Response Options And Scales

Make options mutually exclusive and collectively adequate when possible. Define whether multiple selections are allowed, how order is assigned, whether `other` requires text, and how no-answer states behave. Never collapse valid zero, `none`, `not applicable`, `don't know`, `prefer not to answer`, optional skip, not shown, breakoff, invalid, and suppressed into one value.

Choose nominal, ordinal, count, amount, duration, frequency, probability, ranking, allocation, or open response according to the construct; do not default every item to an unlabeled 1-10 scale. For scales, record construct, number of points, direction, every visible label, endpoint meaning, midpoint meaning, reference period, forced or optional response, display, device behavior, and scoring. Preserve the original response before derived categories. Do not reverse direction silently, mix differently anchored scales, average ordinal labels as if interval properties were guaranteed without an explicit defensible assumption and sensitivity, or change labels while calling a series comparable.

Avoid overlapping numeric ranges, false precision, hidden defaults, forced sensitive responses, ambiguous frequency labels, unbounded top categories when the tail matters, and matrix designs that invite mobile failure or straightlining. Use a separate item when two dimensions can move independently. State how fixed or randomized order, single select, multi-select, ranking, and allocation change interpretation.

## Order, Randomization, Branching, And Piping

Record section order, item order, option order, randomization unit, seed or assignment where available, exclusions, fixed positions, branch conditions, loop limits, piping sources, validation, back navigation, save and resume, termination, and error states.

Use randomization to control order effects only when order is not part of the construct. Preserve fixed chronological, funnel, safety, comprehension, and dependency order where necessary. Separate stimulus exposure from unaided measurement and mask sponsor or condition only when compatible with consent and the decision.

Test every possible route with eligible, ineligible, skipped, missing, contradictory, maximum-selection, minimum-selection, mobile, assistive-technology, and resume cases. Log instrument version, assignment, displayed item and option order, path, timestamps, and termination state. A routed item denominator includes only respondents who were eligible and actually shown the item unless the estimand defines otherwise.

Do not pipe sensitive or identifying answers into later displays unless necessary and approved. Never reveal another person's answer, hidden account data, inferred protected status, or internal score.

## Localization, Accessibility, And Equivalence

Separate market, language, locale, script, reading level, cultural context, product, role, channel, device, and legal or operating environment. Literal translation, back translation, or identical layout alone does not establish construct or measurement equivalence.

Use a proportionate workflow: source-language review, translation, independent linguistic review, adjudication, terminology record, cognitive testing, accessibility review, device and bandwidth testing, pilot, and version approval. Test comprehension, retrieval, judgment, response mapping, sensitivity, text expansion, right-to-left behavior, input methods, screen readers, keyboard access, contrast, zoom, captions, error recovery, and assisted participation as applicable.

Before pooling or ranking markets, establish comparable constructs, frames, instruments, scales, stimuli, fielding modes, response processes, weights, timing, and analysis. Otherwise report markets separately and label the transfer gap.

## Cognitive Testing, Pilot, And Soft Launch

Define populations, tasks, evidence, issue classes, revision rules, owners, acceptance criteria, and version transitions for each stage:

| Stage | Test |
| --- | --- |
| Expert review | Construct coverage, wording, response options, logic, sensitivity, accessibility, privacy, and analysis compatibility |
| Cognitive test | Comprehension, retrieval, judgment, response mapping, terminology, recall, burden, and discomfort |
| Technical test | Routing, randomization, piping, validation, persistence, device, accessibility, capture, and export |
| Pilot | Recruitment, eligibility, duration, item missingness, breakoff, distributions, open text, quality rules, support, and analysis pipeline |
| Soft launch | Live delivery, identity, consent, routing, timing, missingness, breakoff, flags, data capture, incentives, support, and stop rules before scale |

Do not use pilot results to choose favorable wording or thresholds without recording the change and its consequence. Material revisions create a new instrument version and may make prior responses non-comparable. Preserve tested, rejected, approved, fielded, corrected, superseded, and expired versions.

## Invitation And Fielding Specification

Freeze sponsor, purpose, sender, audience, frame source, channel permission, subject or entry point, invitation and reminder versions, eligibility, time estimate, incentive, consent, support, accessibility, privacy, contact frequency, suppression, start and end, timezone, sample release batches, quotas, monitoring, pause and stop rules, incident path, and owner.

An invitation must not conceal consequential use, imply mandatory participation when voluntary, promise anonymity when identity can be linked, or threaten product, service, pricing, employment, or relationship consequences. Shared links require a declared identity, eligibility, duplication, forwarding, and abuse model.

## Response-Quality Plan

Predeclare applicable signals, thresholds, review, and disposition before outcome inspection:

| Signal | Required context |
| --- | --- |
| Duplicate or identity conflict | Identity source, shared-device or shared-account risk, repeated-wave rules, and review path |
| Bot, automation, or fraud | Recruitment source, challenge evidence, impossible patterns, incentive exposure, and false-positive risk |
| Speed | Routed content, task type, language, device, accessibility, reading burden, and distribution |
| Straightlining | Matrix design, legitimate consistency, scale count, variance, and complementary evidence |
| Inconsistency | Item equivalence, timeframe, routing, respondent knowledge, and plausible change |
| Attention check | Clear instruction, accessibility, language, consequence, and non-punitive alternatives |
| Open-text quality | Prompt, language, minimum necessary content, privacy, repetition, and human review |
| Breakoff or partial | Last displayed item, time, technical state, optionality, burden, and construct completeness |

Separate flag, review, exclusion, partial inclusion, weighting, sensitivity, and final disposition. Preserve response ID, raw values, timestamps, paths, flags, rule version, reviewer, reason, date, and reversible derived data. Protect legitimate fast, slow, consistent, assisted, nonnative, accessibility, and partial response patterns.

Report counts and estimates before and after exclusions. Never remove negative, contradictory, null, or inconvenient respondents, choose thresholds after seeing the preferred result, or call a cleaned convenience sample unbiased.
