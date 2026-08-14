# Vocabulary And Validation

## Keep Authorities Separate

Schema.org defines vocabulary terms and their relationships. It does not define whether Google, Bing, Baidu, or another product will consume a type, require a property, show a feature, rank a page, or cite a source.

A search provider's documentation applies only to its named product, result type, market or locale conditions, and documented date. Do not use one provider's validator or requirements as evidence for another provider. Do not use an old or archived page to fill gaps in a current rule without labeling it historical.

## Select Vocabulary

For every emitted term:

1. open its current direct Schema.org definition;
2. confirm the entity supports the selected type;
3. confirm the property is defined for that type or an inherited type;
4. preserve the expected JSON value kind, including arrays, numbers, booleans, URLs, nested nodes, and `@id` references;
5. record the term URL and retrieval date when the interpretation is material or disputed.

The most specific plausible type is not necessarily supported. Prefer a broader supported type over a narrow invented classification. A vocabulary-valid property is still unusable when its value lacks evidence.

## Validate In Layers

Run each applicable layer and report it independently:

| Layer | Check | What a pass establishes | What it does not establish |
| --- | --- | --- | --- |
| JSON | Parse the exact raw and delivered JSON text | Syntactic JSON validity | Factual support, vocabulary validity, eligibility |
| Trace | Reconcile every property, array item, node, and edge | Evidence coverage | Provider consumption |
| Vocabulary | Inspect current Schema.org definitions or validator | Vocabulary conformance within inspected checks | Search-product eligibility |
| Product | Use the exact current direct official provider/result-type documentation and tool | Only the claims that source or tool exposes | Display, ranking, traffic, or citation |
| Embedding | Parse final HTML and extracted script text | The delivered embedding remains one parseable data block | Production deployment correctness |
| Deployment | Inspect the separately authorized live URL after release | Observed live markup at that time | Guaranteed future presentation |

If a validator is inaccessible, record its name, direct URL, attempted time, access result, and unperformed checks. Continue with lower layers that are available. Never report one tool's result as another tool's result.

## Search-Product Claims

Before stating eligibility, required properties, recommended properties, supported types, warnings, or result behavior:

1. identify provider, exact product and result type, market if scoped, and requested claim;
2. retrieve the current direct official page, not a snippet or third-party summary;
3. inspect the relevant visible text and exposed editorial update date;
4. record title, direct URL, publisher/product, exposed date or `not exposed`, retrieval date, exact supported claim, and limitation/access state;
5. quote or accurately bound only the inspected claim;
6. mark any gap `unavailable`.

Required and recommended property lists change. Re-read the live exact product table at execution time rather than copying a list from this Skill. A validator warning is not automatically a required-property failure. Passing required properties may be necessary for eligibility but never guarantees display.

## Conflicts And Dates

Prefer current direct official product text for current product claims. A recent third-party post does not override an undated current official page. An archived official page may document history only. When current official sources conflict, preserve both records, narrow the claim to their intersection if exact, and mark the unresolved part unavailable.

HTTP `Date`, `Last-Modified`, cache age, generated build metadata, and retrieval time are not editorial update dates. Record `not exposed` unless the page itself exposes a publication or update date.

## Deterministic Checks

Use a real JSON parser on every emitted JSON-LD block or fixture. Compare the parsed result, not the formatted text, against the property ledger. Confirm:

- JSON types and array cardinality are unchanged;
- Unicode and escaped values round-trip exactly;
- URLs remain byte-for-byte as supplied unless an evidenced canonical value replaces them;
- all `@id` references resolve to the intended node or a deliberate external identifier;
- no unsupported placeholder, rating, review, offer, FAQ, person, organization, date, address, identifier, price, or availability slipped into output;
- repair change IDs reconcile one-to-one with actual semantic differences.

Do not claim a successful check that was not performed. State commands, tools, access state, observed result, and remaining limitation.
