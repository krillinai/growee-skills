# Standalone HTML Report

Use only when HTML, a visual report, or a browser-openable deliverable is requested. Create `{domain-slug}-landing-page-audit.html` as one offline, script-free file with inline CSS. HTML must preserve the underlying score, coverage, evidence states, findings, priority, actions, completion conditions, limitations, and sources exactly.

## Required Order

1. page identity, capture, audience, source, market, device, mode, and capability scope;
2. executive constraint and strongest verified opportunity;
3. score, evidence coverage, denominator math, and six-dimension trace;
4. inspected evidence and unavailable register;
5. prioritized findings with evidence, actions, completion, effort, and validation;
6. continuity map and dependency-sequenced roadmap;
7. experiment backlog, limitations, method, and sources.

## Brand Extraction

Derive the report palette and identity only from verified page evidence. Prefer a visible accepted logo, wordmark, favicon, computed CSS colors, and dominant product UI colors captured from the inspected page. Record source and date. If no safe logo or palette is available, use the page title as a text wordmark and a neutral palette. Do not invent brand assets.

Embed only a trusted, static, re-encoded raster logo within conservative byte, dimension, pixel, and aggregate budgets. Never embed SVG, animation, source HTML, CSS, remote fonts, scripts, or hotlinked media. If the asset cannot be safely decoded and re-encoded, show a text fallback and the rejection reason.

## Safety

HTML-escape all dynamic text and attributes. Permit sanitized `http:` or `https:` citation links only; add `rel="noopener noreferrer"` to new-window links. Reject `javascript:`, arbitrary `data:`, protocol-relative, and unknown schemes. The only data URL permitted is a validated trusted raster embedded as an inert `<img>`.

Do not include scripts, event handlers, forms, inputs, buttons, iframes, objects, embeds, SVG, MathML, audio, video, remote styles, remote fonts, meta refresh, base tags, credentials, cookies, private paths, raw personal data, or sensitive exports.

## Design

Match the page's product category and verified brand without copying its layout. Use restrained full-width sections, clear document hierarchy, compact score and coverage displays, readable tables, finding blocks, and responsive constraints. Do not nest cards. Long URLs, claims, evidence, and actions must wrap without overlap or truncation.

## Verification

Check one valid HTML document, required sections, domain, score and coverage math, at least one concrete action, no placeholders, safe URL schemes, no scripts or remote rendering dependencies, escaped dynamic content, and semantic parity with the audit record.

When browser capability exists, open locally and inspect desktop and mobile widths for clipping, overlap, wrapping, focus visibility, readable contrast, brand asset rendering, and nonblank content. State only checks actually performed. Otherwise report that structural verification passed and visual verification was unavailable.
