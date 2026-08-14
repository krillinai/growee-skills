# Market And Search Notes

## Market Record

Record `market`, `language`, and `locale` independently. A Simplified Chinese page does not by itself establish China as the market, and a China-targeted property may contain more than one language or locale.

For China work requested in Simplified Chinese, use native Simplified Chinese in the user-facing plan and handoff. Keep official source titles in their published language. Do not translate a Google instruction into a Baidu or Bing rule.

## Architecture Contexts

A country domain, subdomain, subdirectory, or separate international domain may each be viable. Compare only options the owner supplies or approves, using evidence such as:

- market and locale ownership;
- hosting, regulatory, registration, and operational constraints;
- product and content parity;
- CMS, router, release, analytics, and support ownership;
- cross-property navigation and user tasks;
- migration cost and rollback capability;
- direct current official provider guidance for any provider-specific claim.

Do not declare `.cn`, `cn.example.com`, `example.com/zh-cn/`, or a separate domain universally superior. Keep implementation and legal questions as owner decisions when evidence is unavailable.

## Source Record Contract

For a time-sensitive migration or indexing statement, record title, direct URL, publisher and product, exposed publication or update date, retrieval date, exact supported claim, limitation, and access state. If exact current text cannot be inspected, set the claim to `unavailable`; never substitute another provider's documentation.

When the user supplies an attributable captured official-source record and asks for no new retrieval, preserve its title, URL, exposed date, retrieval date, claim, limitation, and access state as supplied. Label it a captured record and do not imply that it was reopened. If a bundled record has a different retrieval date or exposed date, keep the records separate rather than silently replacing either one.

The following direct official pages were retrieved on **2026-07-23**:

| ID | Title and direct URL | Publisher / product | Exposed date | Exact supported claim | Limitation / access state |
| --- | --- | --- | --- | --- | --- |
| `google-site-move` | [Site Moves and Migrations](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) | Google / Google Search Central | Last updated 2026-06-17 UTC | The inspected page directs owners to prepare a mapping from current URLs to new URLs, update internal links to the new URLs, and use server-side permanent redirects from old URLs to the new URLs indicated in the mapping when technically possible. | Public text accessible. This is guidance for the documented Google site-move context; it does not establish Bing or Baidu behavior or guarantee indexing, ranking, traffic, or conversion. |
| `bing-webmaster-help` | [Bing Webmaster Tools - Help Documentation](https://www.bing.com/webmasters/help) | Microsoft / Bing Webmaster Tools | Not exposed | An exact current product-specific migration rule was not exposed in the inspected public help shell; the claim is `unavailable`. | Partially accessible application shell. Do not infer a Bing mapping, redirect, indexing, or timing rule from Google or from generic interface strings. |
| `baidu-site-rewrite` | [网站改版_ 网站换域名状态下，使用本工具提交数据_站长工具_网站支持_百度搜索资源平台](https://ziyuan.baidu.com/rewrite/index) | 百度 / 百度搜索资源平台 | Not exposed | The inspected public text says the 网站改版 tool accepts submitted old-to-new relationships when a site's domain or directory changes, and says new and old links in submitted rewrite rules must use 301 redirects. | Partially accessible without login; additional content and submission actions require authentication. The page exposes no update date. Apply the statements only to this Baidu tool context; they do not establish general indexing outcomes, traffic transfer, timing, or equivalence with Google or Bing. |

Re-open official pages for a later retrieval date. If the exposed text, date, product, or access state changes, issue a new source record rather than silently carrying these claims forward.

## Provider Boundaries

### Google

Use current Google Search Central documentation only for the exact Google product and migration context. Keep mapping and redirect implementation separate from observed Google indexing outcomes. Search Console access and actions are optional private steps requiring separate authorization.

### Bing

The inspected public help shell did not establish an exact current migration rule. Mark Bing-specific mapping, redirect, submission, indexing, or timing claims `unavailable` until a direct Microsoft or Bing page exposes the relevant text. Do not use Google or Baidu as a proxy.

### Baidu

Use the public 网站改版 statements only within their stated tool context. An authenticated submission, verified-property inspection, or webmaster action requires separate explicit authorization. Because the page exposes no update date and only partial unauthenticated content, state that limitation beside every applied claim. Do not promise inherited evaluation, faster indexing, stable traffic, or a processing interval unless current direct text for that exact claim is inspectable.

## Access Boundary

Default work is a local plan. Broad crawling, authenticated analytics or webmaster tools, provider submissions, CMS or router changes, navigation and breadcrumb template edits, redirect deployment, canonical, alternate-language, sitemap or robots changes, DNS, publishing, and production validation require separate explicit authorization. Never bypass login, CAPTCHA, robots controls, regional restrictions, or rate limits.
