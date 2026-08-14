# Migration And Validation

## URL Identities And Ledgers

A **raw inventory URL** is the exact scoped URL as supplied, including any fragment. Reconcile every unique raw inventory URL once because fragments can express distinct user intent.

An **HTTP request source** is the raw URL with its fragment removed while retaining scheme, host, port, path, and query exactly as supplied. Remove nothing else. Group server rules by HTTP request source because fragments are not sent in HTTP requests.

Maintain two linked ledgers:

1. The raw-intent ledger contains raw URL, HTTP request source, fragment if present, user intent, server-rule ID, and separate destination-anchor behavior.
2. The server-disposition ledger contains one row per unique HTTP request source with exactly one explicit disposition:

| Disposition | Required fields |
| --- | --- |
| `preserve` | Exact request source, same destination request URL, preservation rationale |
| `redirect` | Exact request source, exact target, redirect rationale, target evidence |
| `retire` | Exact request source, intended response or removal behavior, rationale |
| `hold-needs-evidence` | Exact request source, missing input, owner, and resolution condition |

`hold-needs-evidence` is an explicit reconciliation disposition, not a deployable redirect. Any hold blocks release readiness even when raw and request-source set/count reconciliation passes. Preserve URLs when page identity, locale, and implementation support preservation. Do not recommend an otherwise unsupported cosmetic URL change. Once a URL change is approved or already occurring, the old request source still needs one disposition and normally an exact redirect even when the approved rationale is cosmetic. Do not send unmatched pages to the homepage without evidence that the homepage satisfies the source intent.

Multiple raw fragment variants that collapse to one HTTP request source cannot produce competing server targets. Give their shared request source one approved path-level server disposition and record each raw variant's destination-anchor behavior separately. Query parameters remain part of the HTTP request source until evidence supports an explicit transformation or removal.

## Reconciliation Formulas

Let `R` be unique raw scoped URLs, `I` the raw-intent rows, `S` the unique HTTP request sources derived from `R`, and `M` the server-disposition rows.

```text
count(I) = count(R)
count(unique(I.raw_url)) = count(R)
R - I.raw_url = empty
I.raw_url - R = empty
I.request_source = request_source(I.raw_url)
count(M) = count(S)
count(unique(M.request_source)) = count(S)
S - M.request_source = empty
M.request_source - S = empty
redirect rows with empty target = 0
redirect rows with missing rationale = 0
hold count = count(M where disposition = hold-needs-evidence)
reconciliation ready = all raw and request-source equalities pass
release ready = reconciliation ready AND hold count = 0 AND required pre-release checks pass
```

Report every failed equality with the exact rows. Do not announce reconciliation readiness while a raw URL or request source is missing, duplicated, or outside scope. Do not announce release readiness while hold count is greater than zero; set/count success never overrides a hold.

For distinct destinations, require destination uniqueness unless multiple sources are intentionally merged into one target. A many-to-one merge is not inherently ambiguous; it becomes acceptable only when the target exists, all source intents are reconciled, locale and market remain appropriate, and each source row contains its own merge rationale.

## Redirect Graph Review

Model each redirect as a directed edge in the request-source server mapping. Remove target fragments for graph-node comparison while retaining scheme, host, port, path, and query. Run these checks:

1. **Missing row:** a raw URL lacks an intent row, or a unique request source lacks a server-disposition row.
2. **Duplicate source:** a raw URL appears twice in the intent ledger, or one request source has multiple server rows even when targets match.
3. **Ambiguous target:** one request source has competing server targets, target identity is unclear, or a shared target lacks an explicit merge rationale.
4. **Target existence:** target is neither in the approved target inventory nor an explicitly approved external destination.
5. **Loop:** following request-source server edges returns to a previously visited request source, including self-loops.
6. **Chain:** a target request source is itself a redirect request source. Resolve to the intended final destination before release unless a documented platform constraint requires otherwise.
7. **Query handling:** each material parameter remains in request-source identity and is preserved, transformed, or dropped through an explicit rule with examples and rationale.
8. **Fragment handling:** group raw fragment variants by request source, reject competing server targets within a group, and validate each destination anchor separately.
9. **Locale and market:** source and target market, language, and locale are compared independently; any loss or consolidation needs an explicit approved rationale.
10. **Orphan target:** an approved destination lacks expected navigation, breadcrumb, or internal-link discovery within the bounded target graph, or the proposed target is absent from that inventory.

Keep graph observations separate from search-product claims. A clean mapping does not guarantee crawling, indexing, rankings, traffic, or conversion.

## Navigation And Breadcrumb Parity

For every retained or replacement destination, compare the captured old and proposed new user path:

- relevant navigation surface and label;
- parent and sibling relationships;
- breadcrumb root, intermediate nodes, label, and URL;
- inbound internal links required by declared tasks;
- locale switch or market handoff when in scope;
- destination page identity and response behavior.

Parity does not require identical markup or menu position. It requires an explicit decision about whether the task and relationship remain available. Mark uncaptured old or new behavior `unavailable`; do not assume parity.

## Implementation Ledger

Prepare a local ledger with owner, system, change, dependency, preview artifact, approval state, rollback action, and completion condition. Include only applicable systems:

- route or CMS records;
- redirect configuration;
- navigation data and templates;
- breadcrumb data and templates;
- body and component internal links;
- locale routing;
- canonical, alternate-language annotations, sitemaps, and robots controls;
- monitoring or validation queries.

The planner may specify these changes without executing them. Editing or deploying any listed system needs separate explicit authorization.

## Validation Sequence

### Before release

1. Freeze raw old and target inventories and rerun both raw and request-source reconciliation formulas.
2. Parse every source and target; derive request sources without fragments while retaining all other exact components and locale fields.
3. Verify target existence and intended response in an authorized preview environment.
4. Detect raw duplicates, request-source duplicates, missing rows, competing fragment-group targets, loops, chains, unsupported homepage mappings, and unresolved holds.
5. Compare hierarchy, navigation, breadcrumbs, and internal links against the approved plan.
6. Exercise representative query transformations and destination fragments.
7. Require hold count zero before release readiness.
8. Record a rollback trigger, responsible owner, configuration backup or reversal, and restoration validation.

### After an authorized release

Validate every old HTTP request source, final target, response path, navigation, breadcrumb, internal link, locale behavior, and query example. Validate each raw fragment variant's destination-anchor behavior separately. When authorized, also check canonical and sitemap state plus material error logs or supplied webmaster reports. Record capture time and inspected count. A sample supports only sample-level conclusions.

Do not claim production validation from a worksheet, local config, staging capture, or inaccessible console. Authentication, Search Console or webmaster actions, deployment, DNS, publishing, and production checks remain separate authorized actions.

## Rollback Record

State the release identifier, trigger conditions, decision owner, reversible configuration or content artifact, reversal steps, expected restoration behavior, and post-rollback checks. If rollback is not technically possible, label that constraint before release; do not omit the risk because timing is tight.
