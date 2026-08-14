# Planning Contract

## Boundary Record

Create the boundary before recommending structure. Do not backfill it from conclusions.

| Field | Required content |
| --- | --- |
| Mode | `new-site`, `restructure`, `migration`, or `focused` |
| Inventory source | Supplied artifact, approved candidate list, sitemap slice, crawl export, or manual capture ID |
| Capture | Timestamp plus frozen state, version, build, or commit when known |
| Scope | Included candidates, current URLs, old URLs, section, host, and protocol where material |
| Counts | Total known units and inspected units |
| Exclusions | Explicitly omitted URLs, sections, variants, assets, and systems |
| Market | Commercial or geographic audience, recorded independently |
| Language | Output or page language, recorded independently |
| Locale | Locale identifier, recorded independently |
| Limits | Partial capture, inaccessible systems, missing evidence, and implementation constraints |

An inventory unit is one declared page candidate or one declared raw URL, depending on mode. Preserve the submitted form of each URL. For migration parsing and server-rule grouping, use the raw-versus-request-source contract in [migration-and-validation.md](migration-and-validation.md). Do not silently erase case, trailing slashes, encodings, query parameters, or fragments to make two inventory entries appear equal.

### Coverage arithmetic

Let `K` be the count of unique known units in scope and `I` the count of unique inspected units.

```text
0 <= I <= K
inventory coverage = I / K, when K is known and greater than zero
uninspected count = K - I
```

If the full count is unknown, report `K = unknown`, the inspected count, and the sample rule; do not calculate a percentage. A partial inventory can support a bounded plan, but cannot establish site-wide completeness, absence, prevalence, or click depth.

## Evidence Register

Evidence state is exactly `verified`, `inferred`, `unavailable`, or `not applicable`:

| State | Meaning |
| --- | --- |
| `verified` | Directly inspectable in the captured inventory, page, response, supplied artifact, or measurement; record source, capture time, and scope |
| `inferred` | Reasoned interpretation; record its named basis and the step that would confirm it |
| `unavailable` | Applicable evidence was not captured, supplied, accessible, or authorized |
| `not applicable` | The evidence or check does not apply to the declared scope or mode |

Signal status is a separate field. When an attributable owner or stakeholder statement has no inspectable artifact, set signal status to `reported signal` and leave evidence state blank. Record the speaker or owner, statement, date when known, and scope. A reported signal is not evidence and must not be promoted to `verified` or presented as evidentiary support for an inference.

For `verified`, name the inspectable source, capture time, and bounded scope. For `inferred`, name its basis and confirmation step; if the basis includes a reported signal, keep that signal's evidence state blank. For `unavailable`, name the missing artifact or access and the decision it would inform. Missing private data remains `unavailable`; do not convert it to a defect, a zero, or a score deduction.

Public pages and supplied inspectable artifacts are the default evidence layer. If an owner supplies a private export, record its artifact ID, owner, generation time, covered period, URL and market scope, completeness statement, and privacy restrictions. Inspectable export facts may be `verified` within that scope. A statement that an unsupplied export exists remains a `reported signal` with blank evidence state. Avoid reproducing sensitive rows unnecessarily.

## Mode Reconciliation

### New site

Use one row per approved candidate: candidate ID, proposed parent, proposed URL, navigation role, evidence basis, and state. Every approved candidate must appear once. A missing customer task, content relationship, locale decision, or implementation constraint becomes a discovery gap; it is not permission to add invented pages.

### Restructure

Use one row per scoped current URL with exactly one decision:

- `keep`: retain URL and placement;
- `move`: retain the page identity but change placement or URL;
- `merge`: combine into one identified destination with source-by-source rationale;
- `retire`: remove without a replacement, with stated behavior and rationale;
- `needs-evidence`: keep the row unresolved until a named input is supplied.

Let `C` be unique scoped current URLs and `D` the decision rows.

```text
unique(D.source) = C
count(D) = count(C)
missing sources = C - D.source = empty
extra sources = D.source - C = empty
```

A shared destination is allowed only for an explicit `merge` supported by a relationship or intent rationale. Otherwise, distinct retained page identities require distinct destination URLs.

### Focused

Repeat the exact named page or section boundary in the deliverable. Review only relationships visible within that boundary. An external page may be named as a dependency, but must not be added to the plan or diagnosed without its own captured evidence.

## Structural Deliverables

### ASCII hierarchy

Show every scoped candidate or retained destination once in a plain-text tree. Put unresolved placement in a separate branch rather than hiding it.

```text
Home  /
|-- Documentation  /docs
|   |-- Start  /docs/start
|   `-- API  /docs/api
`-- Support  /support

Unresolved
`-- Legacy import  [parent needs evidence]
```

The tree is a proposed information relationship, not proof of search demand or ranking value.

### URL map

Include unit ID, current URL if one exists, decision, proposed URL, parent, market, language, locale, evidence state, signal status, and rationale. Check:

- every scoped unit appears once;
- every distinct retained page has one destination identity;
- no destination collision is hidden;
- a shared target has an explicit supported merge rationale;
- locale and market identity are not silently discarded;
- proposed targets belong to the declared target inventory or are clearly labeled candidates awaiting approval.

Choose readable, stable URLs from page identity, relationships, locale strategy, and router or CMS constraints. Do not apply a universal URL-length or directory-depth limit.

### Navigation specification

For each captured or proposed navigation surface, state its scope, audience or task, item labels, destinations, order basis, visibility rules, locale behavior, evidence state, and signal status. Separate global, section, utility, footer, mobile, and in-page navigation when they are actually in scope. Do not fill an uncaptured global menu from assumptions or force a fixed item count.

### Breadcrumb behavior

Specify which scoped page classes receive breadcrumbs, the root and intermediate hierarchy, label source, URL source, locale behavior, current-page treatment, and responsive or accessibility constraints when supplied. Each trail must agree with the proposed hierarchy and URL map. A captured breadcrumb on one page establishes that page's behavior only.

### Internal-link rules

Write relationship rules rather than quotas. Useful bases include parent-to-child discovery, sibling comparison needed for a user task, prerequisite-to-next-step flow, product-to-support connection, and replacement of old links after a move. For each rule, name source page class, target page class, placement context, anchor-label basis, locale constraint, and validation method. Do not prescribe universal link counts or fabricate link value.

## Missing Evidence And Implementation

List missing evidence as owner-ready requests: artifact, scope, period or version, and the decision it would inform. Keep private analytics, demand, rankings, conversion, backlinks, and logs optional unless the user explicitly makes a decision contingent on them.

Local implementation checks should cover inventory imports, route uniqueness, hierarchy data, navigation membership, breadcrumb derivation, internal-link updates, locale routing, and unresolved decision guards. Treat CMS, router, templates, production settings, and publishing as systems to hand off, not implicit authorization to edit them.
