# Customer Journey Analysis Output Contract

## Required Order

Return:

1. mode, journey ID and version, record state, current or target designation, decision, owners, product and offer, customers, roles, jobs, triggers, market, entry and exit boundaries, period, cutoff, review, expiry, privacy, and external-action boundary;
2. source ledger, evidence states, methods, populations, coverage, exclusions, contradictions, instrumentation boundary, missing evidence, and current-to-target version lineage;
3. participant roles, relationships, entities, identities, authority, access, value, burden, paths, exclusions, failure, recovery, and exit;
4. state definitions and graph with branches, skips, loops, pauses, retries, assisted paths, reversals, nonprogression, failure, cancellation, churn, exit, and re-entry as applicable;
5. touchpoint inventory, supply and response states, cross-channel continuity, permission, accessibility, localization, correction, expiry, duplication, contradiction, and missing interactions;
6. service blueprint linking customer actions, frontstage interactions, employee and partner work, backstage processes, systems, data, policies, permissions, owners, dependencies, handoffs, capacity, fallback, and recovery;
7. friction classifications, observed evidence, candidate mechanisms, counterevidence, customer and operating effects, accessibility, support, failure, recovery, cancellation, exit, and unresolved causes;
8. metric contracts, entities, denominators, identities, cohorts, windows, maturity, transition time, customer value, business outcome, guardrails, harm, and causal boundaries;
9. current-to-target gaps, recommendations, evidence plans, specialist handoffs, version, market, privacy and fairness governance, pinned Growth Playbook sources, approval-ready external actions, and completion record.

## Journey Contract And Sources

| Journey / version / mode / state | Current or target / decision / intended outcome | Product / offer / customer / roles / job / trigger | Market / entry / exit / period / cutoff | Owners / review / expiry | Privacy / action boundary |
| --- | --- | --- | --- | --- | --- |

| Source / owner / version / method | Role / population / product / market / period | Exact observation, report or claim | Evidence state / coverage / limitation | Contradiction / exclusion / missing evidence | Journey fields / downstream consumers |
| --- | --- | --- | --- | --- | --- |

Do not call supplied or instrumented sources complete without a coverage contract.

## Participant, Relationship, And Identity Map

| Role / entity / population | Job / trigger / alternative | Value / burden / risk | Authority / access / permission | Relationships / states / handoffs | Evidence / exclusion / failure / exit |
| --- | --- | --- | --- | --- | --- |

| Identity / source / namespace | Entity / key / version | Permission / retention / correction | Duplicate / shared / merge / split / unknown | Analytical linkage / customer continuity | Owner / evidence / limitation |
| --- | --- | --- | --- | --- | --- |

## State Graph

| State / version | Eligible entity / role | Entry rule / evidence | Job / value / owner / time boundary | Exit rule / next states | Failure / pause / cancellation / exit |
| --- | --- | --- | --- | --- | --- |

| Transition / origin / destination | Eligible population / trigger | Customer action / visible interaction | Backstage response / system / identity | Completion evidence / duration / owner | Failure / retry / reversal / next state |
| --- | --- | --- | --- | --- | --- |

Include a compact text graph after the tables when it makes branches, loops, failure, recovery, or exit materially easier to inspect. The graph does not replace definitions or evidence.

## Touchpoints And Continuity

| Touchpoint / version | Role / state transition / job | Content / claim / source | Channel / eligibility / permission | Timing / frequency / accessibility / locale | Response / delivery evidence / owner | Correction / fallback / expiry |
| --- | --- | --- | --- | --- | --- | --- |

| Continuity boundary | Prior context / receiving context | Identity / permission / state | Promise / status / next step | Loss / repetition / contradiction / delay | Owner / fallback / evidence / expiry |
| --- | --- | --- | --- | --- | --- |

Separate creation, delivery, viewability, exposure, interaction, comprehension, task completion and value.

## Service Blueprint

| State or transition | Customer action / evidence / value | Frontstage interaction / promise | Employee or partner action | Backstage process / queue / capacity | System / data / policy / permission | Owner / failure / fallback / recovery / proof |
| --- | --- | --- | --- | --- | --- | --- |

| Handoff / object / version | Sender / receiver / owner | Required context / minimum data / permission | Service expectation / acceptance | Failure / fallback / escalation | Acknowledgement / completion proof / residual owner |
| --- | --- | --- | --- | --- | --- |

## Friction, Failure, Recovery, Accessibility, And Exit

| Role / state / transition | Exact observation or report / source | Friction class / effort / delay / uncertainty / burden | Candidate mechanism / counterevidence / protection | Customer / operating effect / affected population | Disposition / next evidence / owner / guardrail |
| --- | --- | --- | --- | --- | --- |

| Failure or access condition | Detection / visibility / affected entity / severity | Help / workaround / retry / fallback / appeal | Technical resolution / customer resolution / service recovery | Trust / repeated value / departure / residual harm | Owner / evidence / guardrail / review |
| --- | --- | --- | --- | --- | --- |

| Pause, cancellation or exit state | Eligibility / choice / consequence / confirmation | Product / entitlement / billing / refund / access | Export / data / deletion / retention / downstream | Support / appeal / re-entry / residual obligation | Owner / evidence / correction / expiry |
| --- | --- | --- | --- | --- | --- |

Do not turn drop-off into cause, a closed ticket into resolution, technical recovery into trust, or obstruction into retention.

## Measurement And Causal Boundary

| Metric / version | Entity / role / eligible population | Numerator / denominator / state rule | Identity / source / timestamp | Market / channel / cohort / period / window | Maturity / exclusions / late data / suppression | Owner / quality / limitation / review |
| --- | --- | --- | --- | --- | --- | --- |

| Intervention hypothesis / mechanism | Target states / role / eligible population | Assignment / access / exposure / adoption | Customer / business outcome / maturity | Alternatives / concurrent changes / disconfirming evidence | Causal design / limitation / next evidence |
| --- | --- | --- | --- | --- | --- |

Do not average incompatible signals into a journey score. Activity, sequence and before-after movement do not prove value or causality.

## Current-To-Target Gap And Handoffs

| Journey field / current version | Target proposal / expected customer effect | Assumption / evidence / counterevidence | Dependency / risk / guardrail / stop | Specialist / expected artifact / acceptance | Decision / authorization / verification / expiry |
| --- | --- | --- | --- | --- | --- |

| Skill / owner | Question / affected journey fields | Supplied sources and versions | Expected artifact / evidence / acceptance | State / returned version / limitation / conflict | Acknowledgement / expiry / residual gap |
| --- | --- | --- | --- | --- | --- |

## Approval-Ready External Actions

| Proposed action / system / object / scope | Source version / decision / evidence | Owner / reviewer / approver / authorizer / executor / verifier | Preconditions / access / privacy / segregation | Dry run / stage / monitor / stop / rollback / correction | Completion proof / audit / expiry / residual obligation |
| --- | --- | --- | --- | --- | --- |

Specify requests only. Do not imply research, access, assignment, implementation, communication, exposure, adoption, completion, improvement, or impact.

## Completion Gate

Confirm journey ID, version, mode, state, current or target designation, decision, owners, product, offer, customers, roles, relationships, jobs, triggers, market, entry and exit, period, cutoff, sources, evidence states, coverage, exclusions, contradictions, identities, state definitions, branches, loops, pauses, retries, assisted paths, failures, recovery, cancellations, churn, exit, re-entry, touchpoints, supply and response states, continuity, frontstage, backstage, systems, data, policies, permissions, dependencies, handoffs, capacity, friction classifications, accessibility, support, metrics, denominators, cohorts, maturity, customer and business outcomes, causal limits, current-to-target gaps, specialist handoffs, versions, privacy, fairness, pinned sources, external actions, and completion are explicit; a linear or tracked path did not become the whole journey; roles and identities were not conflated; personas, emotions, causes, rates and scores were not invented; activity did not become value; obstruction did not become retention; routing did not become execution; and no external action occurred.
