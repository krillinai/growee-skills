# Growee Context Contract

Use `.agents/growee-context.md` to carry a completed Growth Diagnosis into later Skills without making the user repeat stable context. This file is a compact handoff, not a data warehouse, full report, credential store, or source of permanent truth.

## When To Write

Write or replace the file after a final diagnosis is complete and the canonical diagnosis record is internally consistent. Do not create a final-looking context file during triage. If the environment cannot write local files or the user asks for chat-only output, return the same Markdown in a fenced block and state the intended path.

Use [../assets/growee-context-template.md](../assets/growee-context-template.md) unchanged as the heading contract. Create the `.agents/` directory when needed. Preserve one output language throughout the file.

## Required Content

Every file must include:

- schema version, update date, generating Skill, and diagnosis status;
- product, customer, business model, stage, market, locale, and decision window;
- outcome metric definition, baseline, target, segment, and time window;
- one primary constraint, confidence, mechanism, and alternatives;
- source inventory with source IDs, owners, capture or query dates, periods, definitions, and limitations;
- contradictory evidence, missing evidence, and access limits;
- ordered 30-day actions, owners, decision dates, routes, dependencies, and guardrails;
- recommended next Skills and the reason for each handoff.

Keep the file semantically aligned with the final diagnosis. A later Skill must be able to distinguish verified, inferred, unavailable, not applicable, and reported-signal information.

## Privacy And Security

Never write credentials, secrets, tokens, cookies, authorization codes, raw personal data, raw customer payloads, audience lists, unrestricted exports, or unnecessary row-level records. Prefer source identifiers and aggregated facts. Record where controlled evidence lives and who owns it instead of copying sensitive material into the context file.

## Reuse Rules

Later Skills may reuse a field only when its scope, definition, source, and date remain compatible with the current task. Treat the file as prior evidence, not authority:

1. read it before asking for repeated product, customer, market, outcome, constraint, or routing context;
2. state which fields are being reused;
3. surface stale, missing, contradictory, or incompatible fields;
4. let newer attributable evidence override older entries without erasing the conflict;
5. ask only for gaps that could change the current decision;
6. never infer system access or authorization from the file's existence.

Only Growth Diagnosis replaces the complete context contract by default. Other Skills may propose a dated addendum or ask the user to rerun Growth Diagnosis when the primary constraint materially changes; they must not silently rewrite the diagnosis.
