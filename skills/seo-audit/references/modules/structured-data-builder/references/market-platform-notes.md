# Market And Platform Notes

## Market Record

Record `market`, `language`, and `locale` independently before collection. Do not infer market from language, locale from domain, or language from operator location. `zh-SG` does not establish China as the market; `en-CN` does not establish Simplified Chinese.

For `China (CN)` plus Simplified Chinese, use native Simplified Chinese for the user-facing report and handoff. Keep source titles in their original language. Do not translate a provider's terminology into another provider's product contract.

## Source Record Contract

For every time-sensitive claim record: source ID, title, direct URL, publisher/product, exposed publication or update date, retrieval date, exact supported claim, limitation, and access state. `Unavailable` means the current inspected evidence did not establish the claim; it is not proof that the capability does not exist.

The following direct sources were retrieved and inspected on **2026-07-23**. Re-open them when executing a later request.

| ID | Direct official source | Publisher/product | Exposed date | Exact supported claim | Limitation and access state |
| --- | --- | --- | --- | --- | --- |
| `schema-schemas` | [`Schemas - Schema.org`](https://schema.org/docs/schemas.html) | Schema.org | Not exposed | The page describes Schema.org schemas as types associated with properties and arranged in a hierarchy. | Accessible. It defines vocabulary, not any search product's eligibility or presentation. |
| `schema-validator` | [`Schema Markup Validator`](https://validator.schema.org/) | Schema.org | Not exposed | The live page exposes a Schema.org markup validation interface. | Accessible on retrieval. A validation result concerns inspected vocabulary markup, not Google, Bing, or Baidu eligibility. |
| `google-product-snippet` | [`How To Add Product Snippet Structured Data`](https://developers.google.com/search/docs/appearance/structured-data/product-snippet) | Google Search Central / Product snippets | Last updated 2025-12-10 UTC | For Google's Product snippet eligibility, the inspected Product table requires `name` and one of `review`, `aggregateRating`, or `offers`; it distinguishes required from recommended properties. The page also says Google does not guarantee that features consuming structured data will appear in search results. | Accessible. Applies to the named Google result type and its documented conditions, not Bing, Baidu, rankings, traffic, or AI citations. Re-read the live tables for current required and recommended properties. |
| `bing-structured-data-help` | [`Bing Webmaster Tools - Help Documentation`](https://www.bing.com/webmasters/help/marking-up-your-site-with-structured-data-3a93e731) | Microsoft Bing Webmaster Tools | Not exposed | The retrieved page exposes only a generic Bing Webmaster Tools help title and description; no article text supporting a structured-data format, type, eligibility rule, or rich-presentation equivalence was exposed. | Partially accessible shell; the relevant article content is unavailable. Make no Bing structured-data eligibility claim from this capture and do not import Google's rules. |
| `baidu-structured-data-help` | [`结构化数据工具帮助_搜索学堂_百度搜索资源平台`](https://ziyuan.baidu.com/college/articleinfo?id=721) | 百度搜索资源平台 | 发布日期：2015-04-01 | The historical page describes a Baidu structured-data submission tool for listed open-data formats, says submitted fields should accurately follow the specification and agree with corresponding page content, and says Baidu does not guarantee structured-snippet display. | Accessible but historical. It does not establish current inline Schema.org or JSON-LD support, Product rich-result requirements, a public current validator, ranking effects, AI citation effects, or equivalence with Google. |

## Provider Rules

### Google

Use the exact current Search Central page for the requested result type. Keep vocabulary validity separate from Google eligibility and tool results. Do not generalize Product snippet rules to merchant listings, local results, events, articles, AI features, or another provider. Never promise that valid or eligible markup will be displayed.

### Bing

Use a current direct Microsoft/Bing page whose article text exposes the exact claim. The inspected URL above did not expose relevant article content, so current Bing format support, required/recommended properties, result-type eligibility, and equivalence with Google are `unavailable` in this source set. Provide the direct URL and a bounded owner/browser retry; do not substitute Google's validator.

### Baidu And China

Research in native Simplified Chinese when the requested language is Simplified Chinese. The accessible Baidu page is historical and describes a submission tool, not a current general contract for inline Schema.org JSON-LD. Therefore, within this inspected source set, all of the following are `unavailable`:

- current Baidu support for inline JSON-LD as a general mechanism;
- Google Product-to-Baidu Product eligibility equivalence;
- current Baidu required or recommended Schema.org properties;
- a current public Baidu rich-result validator equivalent to Google's tool;
- any promise of rich presentation, ranking, traffic, or AI citation.

Do not call Google validation a Baidu validation. Handoff by recording the intended Baidu product/surface, market `China (CN)`, language, locale, exact claim to verify, official URL attempted, access state, and owner. Ask the owner to supply a current direct official Baidu document or an inspectable authorized product result. Keep the generated JSON-LD limited to evidence-backed Schema.org vocabulary while labeling Baidu consumption and eligibility unverified.

## Access Boundaries

Public pages come first. Authenticated Search Console or webmaster tools, private exports, paid tools, CMS access, template edits, broad crawling, deployment, and production validation are optional separate actions. Never bypass login, CAPTCHA, robots controls, regional restrictions, or rate limits. A blocked or missing tool creates an unavailable validation layer, not permission to use another provider as a proxy.
