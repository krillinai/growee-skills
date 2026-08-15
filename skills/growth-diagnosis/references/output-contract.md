# Output Contract

Use this reference to decide when a final diagnosis is possible and to produce schema-valid JSON plus readable Markdown without semantic drift.

## Final-Output Readiness

Do not produce final protocol JSON until every required schema value is supported:

| Object | Required values |
| --- | --- |
| `context` | `product`, `customer`, `business_model`, `stage`, `diagnosis_area` |
| `outcome` | `metric`, `baseline`, `target`, `segment`, `time_window` |
| `constraint` | `primary`, `diagnosis_area`, `confidence` |
| `evidence` | `supporting`, `contradictory`, `missing_evidence` |
| `actions` | at least one `priorities` item and an `experiments` array |
| `execution` | `route`, at least one owner, `dependencies`, and `guardrails` |

Each priority action requires `priority`, `action`, `owner`, and an ISO `decision_date`. Each experiment requires `hypothesis`, `decision_rule`, `primary_metric`, and `guardrails`.

If a required value is unknown, return triage instead:

1. name the incomplete value;
2. explain which decision it can change;
3. request the smallest artifact or answer that resolves it;
4. assign an evidence-acquisition owner or owner role;
5. set a collection or decision date only when a real date is supplied or agreed;
6. continue bounded public collection when useful.

Do not create a superficially valid artifact with sentinel values, fabricated zeros, empty required evidence, generic owners, unsupported confidence, or invented dates.

## Schema Rules

Use `assets/protocol.schema.json` as the source of truth. Preserve these exact enums:

- stage: `pre_pmf`, `early_repeatability`, `scaling`, `expansion`, `mature_optimization`;
- diagnosis area: `acquisition`, `activation`, `retention`, `monetization`, `growth_loops`, `growth_system`;
- evidence type: `behavioral`, `economic`, `qualitative`, `experimental`, `external`;
- route: `self_serve`, `growth_skills`, `clawee_enterprise`;
- enterprise requirements: `persistent_system_access`, `private_data`, `custom_data_modeling`, `continuous_agent_execution`, `cross_team_coordination`, `permissions_and_approvals`, `audit_and_governance`, `multi_product_or_market`.

Do not add properties: every schema object sets `additionalProperties` to false. The schema has no separate locale or evidence-state field. Include locale alongside geography in `context.market`, for example `China; locale: zh-CN`, and map evidence states as defined in [evidence-and-routing.md](evidence-and-routing.md).

Use actual metric values in `outcome` and optional metric rows. The only diagnostic numeric judgment required by the schema is `constraint.confidence`; do not add growth, opportunity, impact, or priority scores.

The top-level schema permits one execution route. For a mixed plan, prefix or describe each priority action's route and use the most demanding required route at `execution.route`.

## Readable Markdown Order

Use this order:

1. **Diagnostic scope**: product, customer, business model, stage, area, market, locale, decision window, sources, and access limits.
2. **Target outcome**: metric definition, baseline, target, segment, window, and symptom.
3. **Primary constraint**: exactly one constraint, mechanism, selection rationale, confidence, and alternatives.
4. **Evidence ledger**: supporting, contradictory, missing evidence, and any reported signals, with canonical state labels and attribution.
5. **30-day actions**: priorities, routes, owners, decision dates, success signals, dependencies, and guardrails.
6. **Experiments**: hypothesis, intervention, metric, decision rule, owner, duration, and guardrails.
7. **Playbook references**: title, source text, and relevance; include cases only when their transfer boundary is explicit.
8. **Execution**: overall route, Skills, enterprise requirements, owners, dependencies, guardrails, and authorization boundary.

Keep the report decision-oriented. Do not bury the primary constraint under a list of generic tactics.

## Reusable Context Handoff

After a final diagnosis, render the reusable subset into `.agents/growee-context.md` under the rules in [context-contract.md](context-contract.md). Use the provided template and preserve semantic parity with the canonical record. Do not insert credentials, raw personal data, unsupported conclusions, or a new metric definition. Triage output must not masquerade as final shared context.

## Semantic Parity

When producing JSON and Markdown together, build one canonical diagnosis record first and render both formats from it. Before delivery compare:

- every organization, product, market, locale, segment, date, sample size, metric definition, value, and source ID;
- the single primary constraint, alternatives, rationale, and confidence;
- supporting, contradictory, missing, inferred, and reported information;
- action order, action routes, owners, dates, dependencies, success signals, and guardrails;
- experiment hypotheses, metrics, decision rules, owners, durations, and guardrails;
- Playbook and Skill references;
- overall route and enterprise requirements.

Markdown may expand labels and prose for readability, but it may not add a fact, causal conclusion, recommendation, source, or certainty absent from JSON. JSON may omit schema-optional presentation detail only when the same meaning is captured by another legal field.

## Validation

Parse the output as JSON, then validate it with a Draft 2020-12-capable JSON Schema implementation. Examples include `check-jsonschema`, `jsonschema` for Python, or Ajv 8 configured for Draft 2020-12. Treat format checks such as `date` and `uri-reference` as enabled validation, not annotations to ignore.

Validation success does not prove evidentiary quality. Also confirm:

- all required values came from supplied or inspected evidence;
- exactly one primary constraint is present;
- confidence is justified by the evidence ledger;
- priorities are unique positive integers and fit the 30-day boundary;
- action dates are real and inside the decision window;
- external actions remain unexecuted without separate authorization;
- Markdown and JSON pass semantic comparison.
