# Search Console Read-Only Access

Use Google Search Console only after explicit task-level authorization names the verified property, owner, decision, date window, dimensions, search type, filters, and query limit and a capable connector or API path is available. Require `https://www.googleapis.com/auth/webmasters.readonly`. If any gate is missing, request a bounded export or mark the evidence unavailable.

Allowed reads include the property inventory, bounded Search Analytics queries, sitemap inventory, and URL inspection results when the available read path supports them. Never submit or delete a sitemap, request indexing, change users or ownership, change settings, or expand the query beyond the approved boundary.

Record property, query timestamp, requested and returned dates, timezone, search type, dimensions, filters, aggregation type, row limit, data state, freshness, anonymized-query effects, and unavailable rows. Search Console evidence describes Google-reported search performance for that property and boundary; it does not establish causality, total demand, user intent, ranking for unqueried contexts, or business impact.
