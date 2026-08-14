# Sources, Lineage, And Bias

## Source Ledger

Create one row per atomic benchmark claim:

| Claim / value / unit | Original publisher / collector / sponsor | Source type / dataset / method | Population / frame / sample / response | Metric / period / market / version | Access / license / capture / freshness | Evidence state / limitation / contradiction |
| --- | --- | --- | --- | --- | --- | --- |

Preserve exact wording, value, range, percentile label, unit, definition, source URL or artifact ID, publication date, data collection period, capture date, effective period, correction, supersession, and expiry. Do not cite an article that quotes a report as if it collected the data.

## Trace And Deduplicate Lineage

Trace each claim to the earliest inspectable source and underlying dataset. Build a lineage graph across original collector, sponsor, publisher, licensed distributor, analyst model, press release, article, social post, slide, and internal reuse.

Treat sources as dependent when they share any material dataset, sample, methodology, model, publisher, vendor, or syndicated claim. Record overlap and effective independent evidence coverage. Five reports repeating one estimate remain one lineage.

Do not average incompatible quotations, count citation volume as truth weight, or select the most favorable version. Preserve corrections, restatements, revisions, contradictory values, withdrawn reports, and unfavorable evidence. Explain which source is used for which field and why.

## Source Types And Meaning

| Source | Can establish | Cannot establish alone |
| --- | --- | --- |
| Public filing or audited report | Disclosed metric under stated scope and accounting | Comparable customer value, private operations, or causality |
| Official product or pricing page | Visible product, package, price, and claim at capture | Realized price, adoption, retention, economics, or full availability |
| Vendor benchmark report | Results for the disclosed vendor population and method | Market truth or unbiased peer performance |
| Survey or panel | Responses for the declared frame, sample, fielding, and weighting | Observed behavior, complete coverage, or causal effect |
| Analyst or database estimate | Model output under disclosed sources and assumptions | Observed actual or exact private performance |
| Customer or case study | Attributable selected experience and conditions | Prevalence, reference distribution, or typical result |
| Review, press, or social report | Attributable statement or visible text | Verified underlying performance or independent confirmation |
| Supplied internal record | Bounded focal or peer evidence under its access and definition | Broader representativeness or permission for unrelated use |

Keep observed actual, preliminary actual, modeled estimate, forecast, target, survey response, selected case, and reported signal separate.

## Population And Sampling Audit

Record target population, sampling frame, selection method, invitation or inclusion process, eligible N, selected N, responding N, analyzed N, response rate definition, weighting, exclusions, missingness, attrition, collection mode, field dates, market, language, privacy, and uncertainty.

Preserve:

- undercoverage and overcoverage;
- self-selection and nonresponse;
- vendor-customer, paying-customer, active-user, community, and disclosed-company selection;
- customer, panel, and employee attrition;
- survivorship and failed-company absence;
- outcome-conditioned peer selection;
- publication and disclosure bias;
- look-ahead and use of current survivors in historical classes;
- case and marketing selection;
- unknown and unavailable groups.

A large sample does not repair an invalid frame. Weighting does not repair unmeasured selection, missing failures, construct differences, or incompatible definitions. A vendor's customers are not the market unless the reference claim is explicitly limited to those customers.

## Distribution And Percentile Evidence

Require the distribution basis: population, sample, weights, count, minimum, maximum, quantiles, ties, missingness, suppression, period, and method. Distinguish arithmetic mean, weighted mean, median, quartile, percentile, range, threshold, selected example, and modeled interval.

Do not infer top quartile from one point estimate, derive percentiles from a mean, or report a rank without the eligible reference distribution. When only aggregate bounds are supplied, preserve bounds and unavailable statistics. Report the focal count and denominator beside rates.

## Commercial Incentives And Conflicts

Record who funded, collected, analyzed, published, sold, and benefits from the benchmark. Preserve vendor eligibility, product usage, customer status, sponsorship, lead-generation, certification, award, ranking, paid placement, analyst relationship, and disclosure.

Commercial interest does not automatically invalidate evidence, but it changes the required corroboration and transfer boundary. Do not promote a vendor benchmark to independent market truth or use a certification as verified superiority.

## Access, Rights, And Freshness

Use only public, licensed, supplied, consented, or otherwise authorized evidence. Do not bypass authentication, paywalls, robots controls, rate limits, CAPTCHAs, private communities, contracts, or access restrictions; create deceptive accounts; accept terms; purchase data; contact analysts; or claim access that did not occur.

Record source owner, access state, license or permission, allowed use, capture date, collection period, effective date, update cadence, last verified date, freshness rule, correction path, expiry, archive, and downstream consumers. Mark restricted or stale evidence `unavailable` for uses it cannot support.

Create approval-ready source-access, licensing, procurement, or contact requests with object, purpose, owner, reviewer, approver, authorizer, executor, access, cost, rights, privacy, security, acceptance, expiry, and audit. Do not execute them.

## Evidence Review Gate

Before using a source, confirm:

1. the original source and dataset are inspectable or explicitly unavailable;
2. the claim, metric, population, period, market, method, and version are exact;
3. dependencies and duplicate lineages are reconciled;
4. coverage, selection, survivorship, response, publication, and commercial bias are visible;
5. distribution, sample size, uncertainty, missingness, and suppressions are sufficient for the intended claim;
6. access, license, rights, freshness, correction, and expiry support the use;
7. contradictions and unfavorable evidence remain visible.

If a gate fails, downgrade the comparison verdict rather than inventing confidence.
