# Evidence And Boundaries

## Evidence States

Use one of these states for every material claim:

| State | Meaning |
| --- | --- |
| `verified` | Directly supported by a supplied attributable source with compatible scope and date |
| `reported signal` | A stakeholder or source reports a condition that has not yet been independently verified |
| `inferred` | A reasoned interpretation with its assumptions and competing explanations visible |
| `unavailable` | Needed evidence was not supplied, was declined, cannot be accessed, or is not trustworthy enough |
| `not applicable` | The question does not apply to the declared decision or product context |

Do not turn `unavailable` into zero, average, healthy, poor, or failed. Missing private data is not a defect. Request the smallest privacy-safe evidence that could change the decision.

## Claim Controls

- Meta-reported attribution is operating evidence, not incrementality.
- Platform ROAS does not establish contribution, payback, retained value, or customer quality.
- A movement in CPA or results does not establish its cause.
- A screenshot verifies only the visible state, scope, and capture time.
- An account name, campaign name, or operator description does not verify structure or performance.
- A creative label does not verify the actual asset, concept, claim, creator, or usage rights.
- Algorithm descriptions and operating advice are time-bound interpretations unless current official documentation verifies the exact behavior.
- External benchmarks do not become decision thresholds without comparable definitions, market, maturity, economics, and prospective agreement.

Preserve counterevidence and unresolved discrepancies. Cite the local artifact and row, section, or capture date whenever practical.

## Unsupported Precision

Never invent or import a universal:

- campaign, ad-set, ad, or creative count;
- spend allocation or daily budget;
- CPM, CPC, CPA, CAC, ROAS, contribution, or payback target;
- frequency, fatigue, learning, scaling, or stopping threshold;
- attribution, maturation, cohort, or experiment window;
- audience size, reach, conversion rate, or incrementality estimate.

When economics are incomplete, do not compensate with a temporary platform threshold. Return the blocked decision, scenario formula, required inputs, and evidence plan.

## Privacy Gate

Do not process raw names, email addresses, phone numbers, postal addresses, customer or user IDs, lead lists, custom audiences, payment records, credentials, access tokens, API keys, client secrets, or passwords. Stop using the affected artifact, name the issue without reproducing sensitive values, and request a redacted or aggregated replacement.

Business outcomes should be aggregated by date, campaign, ad set, ad, market, or cohort at a privacy-safe level. Separate a system's internal entity ID from direct customer identifiers.

## Read-Only Boundary

This Skill may:

- read user-supplied local files;
- validate and normalize a local bundle;
- calculate descriptive measures from compatible fields;
- compare dated creative, landing, measurement, and business evidence;
- write a local audit, evidence request, or experiment plan.

This Skill must not:

- log into Meta or ask for login credentials;
- connect an ad account or obtain tokens;
- call the Marketing API or Graph API against a live account;
- create, edit, duplicate, publish, pause, or delete campaigns, ad sets, ads, or creatives;
- change bids, budgets, placements, objectives, attribution settings, or account configuration;
- upload audiences, customer lists, events, or conversions;
- edit landing pages, deploy tracking, contact customers, or make purchases;
- claim that an external action occurred.

A direct execution request uses `out-of-scope` mode. Decline the external action, retain any supported read-only diagnosis, and list the separate authorization, capability, data-governance, approval, monitoring, rollback, and audit-log controls required for an execution workflow. Do not provide click-by-click instructions that bypass the declared boundary.

## Action Language

Prefer: "collect", "verify", "reconcile", "segment", "design a test", "define a decision rule", "review after maturation", or "hand off for separately authorized execution".

Avoid: "set the budget to", "pause", "launch", "upload", "turn off", "scale by", or "target" unless quoting a user request and explicitly stating why this Skill does not execute it.

Every recommendation must identify the owner and completion proof. A recommendation is not evidence that the action was performed.
