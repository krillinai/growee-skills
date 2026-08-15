# Evidence And Routing

Use this reference to set evidence states, preserve attribution, account for market context, calibrate confidence, and choose execution routes.

## Canonical Evidence States

Use these labels exactly in the working ledger and readable report:

| State | Meaning | Allowed use |
| --- | --- | --- |
| `verified` | Directly observed in a dated, inspectable public artifact or sufficiently attributable private artifact | Support or contradict a candidate constraint; preserve the source and limits |
| `inferred` | A reasoned mechanism or explanation not directly measured | Form a hypothesis or alternative; name the evidence needed to verify it |
| `unavailable` | Applicable evidence or capability was not supplied, could not lawfully be inspected, or failed | Record a limitation and acquisition step; never treat it as a negative finding |
| `not applicable` | Outside the declared product, market, segment, mode, or surface | Exclude it and state the scope reason when material |
| `reported signal` | A stakeholder statement without an inspectable source artifact | Preserve as context outside verified evidence; request the smallest corroborating artifact |

Do not silently upgrade a state. A URL is not verification unless its relevant content was inspected. A tool or account is not available unless access was actually established. A user statement about a metric can be a reported signal; an attached export with sufficient attribution can be verified.

## Map States To The Canonical Schema

The schema intentionally has no `evidence_state` property and rejects additional properties.

| Working state | Schema representation |
| --- | --- |
| `verified` supporting fact | `evidence.supporting[]`, with evidence type, finding, source, segment, period, and quality notes |
| `verified` conflicting fact | `evidence.contradictory[]` with the same attribution fields |
| `inferred` mechanism | `constraint.mechanism`, selection rationale, or an alternative constraint; add the verifying need to `evidence.missing_evidence[]` |
| `unavailable` input | One complete `evidence.missing_evidence[]` statement explaining what is missing, why it matters, and which decision it can change |
| `not applicable` input | Omit the optional schema property; preserve the declared scope in context or a quality note when needed |
| `reported signal` | Preserve it in rationale or an alternative's reason and add a corroboration request to missing evidence; do not serialize it as direct support |

Do not add a state field to an evidence item. Markdown may show explicit state labels, but its facts and conclusions must map to the JSON representations above.

## Public And Private Evidence

Begin with public evidence whenever it can advance the decision. Examples include product pages, pricing, onboarding documentation, public app listings, public status history, channel availability, public campaign artifacts, policies, and current primary regulatory or platform sources.

Public evidence cannot establish private traffic, conversion, cohort behavior, acquisition economics, revenue, motives, or causal impact. Mark those inputs unavailable unless supplied in an attributable artifact.

Treat a private artifact as verified only when it identifies enough of the following to reproduce its meaning:

- source system and artifact, export, or query ID;
- metric or event definition and unit;
- product surface, population, and exclusions;
- market, locale, channel, and segment;
- measurement period and comparison period;
- value, denominator, and sample size where applicable;
- retrieval or capture date and known quality limitations.

Private data is optional enhancement. A supplied export does not authorize direct account access. Minimize or redact credentials, tokens, cookies, personal data, customer records, and sensitive URLs.

## Contradictions And Confidence

Keep incompatible definitions separate. Do not average them, select the preferred source without justification, or call disagreement noise. State what must be reconciled and how the result could change the constraint.

The schema requires `constraint.confidence` between `0` and `1`; it does not define a score formula. Set the value only after writing the evidence ledger and selection rationale. Use a conservative value and state why. Confidence must fall when:

- evidence types or sources disagree;
- an important segment, market, cohort, or journey step is missing;
- samples are small, biased, stale, or poorly attributable;
- a mechanism rests on correlation or one public observation;
- measurement definitions conflict;
- a plausible alternative has not been distinguished.

Do not convert the constraint-comparison dimensions into an arithmetic score. Do not accept a requested confidence, benchmark, or causal statement merely because it makes the output look complete.

## Market And China Context

Establish market and locale before comparing channels, journeys, or economics. Treat availability and compliance as evidence questions, not assumptions.

For China, check only the surfaces relevant to the diagnosed product:

- Simplified Chinese language, terminology, customer support, and local trust expectations;
- local web, search, social, advertising, and content distribution channels;
- iOS and relevant local Android distribution rather than assuming Google Play coverage;
- payment methods, invoicing, pricing currency, and payer expectations;
- phone, identity, SSO, email, map, cloud, CDN, analytics, and other service dependencies;
- applicable content, advertising, licensing, data, privacy, cross-border, and sector rules;
- approval owners, data residency, and operational dependencies.

Use current direct sources for time-sensitive platform or regulatory claims. If a source is not available, mark the claim unavailable. Do not infer accessibility, legality, approval, or performance from a domain, language, office location, or prior general knowledge.

## Execution Routes

Choose the lowest route that can complete the proposed work safely:

| Route | Use for | Boundary |
| --- | --- | --- |
| `self_serve` | Bounded analysis, manual evidence collection, or a change the team can execute with existing access and decision rights | Supply method, owner, dependencies, and guardrails; the team performs the action |
| `growth_skills` | A reusable, auditable workflow in the Growth & Marketing Skills catalog | Name the specific Skill and handoff inputs; do not claim capabilities outside that Skill |
| `clawee_enterprise` | Persistent system access, custom data modeling, continuous execution, cross-team coordination, permissions and approvals, audit and governance, or multi-product/market work | State applicable `enterprise_requirements`, authorization owner, security/privacy constraints, and handoff evidence |

The presence of private evidence alone does not require enterprise routing. Direct access to private systems, persistent ingestion, regulated handling, cross-system identity, or ongoing execution often does.

For a mixed plan, label the route in each action's text or rationale and set the schema's single top-level route to the highest route needed. Never hide a usable self-serve result behind enterprise escalation.

## Authorization Boundary

Diagnosis is read-only by default. A bounded authenticated read still requires explicit task-level authorization that identifies the system, property/project/portal/account, scope, owner, decision, and guardrails unless the user already supplied the resulting artifact. Follow [core-read-only-tools.md](core-read-only-tools.md) for supported sources. External writes and consequential actions always require separate explicit authorization. This includes:

- authenticated access outside the explicitly approved read boundary;
- CRM, analytics, advertising, product, content, or sales-system changes;
- persistent connectors, scheduled agents, monitoring, or data synchronization;
- campaign, pricing, budget, publication, or deployment changes;
- outbound email, messages, tickets, or approval requests;
- high-volume collection or tests that could affect a service or customer.

An execution route, credential, or prior access does not itself authorize these actions.
