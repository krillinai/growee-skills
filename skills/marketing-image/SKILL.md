---
name: marketing-image
description: Use when a team needs to create, generate, edit, composite, adapt, optimize, audit, or govern marketing images for websites, ads, social, email, PR, sales, directories, product visuals, diagrams, charts, and campaign systems; or needs to choose image models, APIs, accounts, credentials, local runtimes, formats, and delivery workflows while preserving product truth, brand, claims, rights, accessibility, platform requirements, lineage, and file QA.
---

# Marketing Image

Turn one bounded communication decision into truthful, brand-coherent, accessible, production-ready image assets and purposeful adaptations. Optimize audience comprehension and qualified downstream value, not image count, aesthetic novelty, engagement, clicks, or attributed conversion alone.

## Read The Relevant References

- Read [image-contract.md](references/image-contract.md) before accepting product, copy, brand, source, rights, person, claim, data, or channel evidence.
- Read [tools-and-dependencies.md](references/tools-and-dependencies.md) before selecting an image provider, API, hosted application, design tool, local model, or optimization stack.
- Read [production-and-prompts.md](references/production-and-prompts.md) before briefing, generating, editing, compositing, templating, or adapting an image.
- Read [qa-localization-and-measurement.md](references/qa-localization-and-measurement.md) before localization, accessibility review, optimization, file export, delivery, or performance learning.
- Use [playbook-sources.md](references/playbook-sources.md) when citing the pinned Growth Playbook basis.

Do not load provider details merely to write a brief. Do load them when the user asks what tool, model, account, API, runtime, or budget is needed.

## Select One Primary Mode

| Mode | Use | Image capability | External credentials |
| --- | --- | --- | --- |
| `brief` | Define a production-ready image contract, concepts, sources, variants, QA, and handoff | Not required | Not required |
| `create` | Generate, edit, composite, template, resize, or optimize actual local files | Required | Depends on the selected tool |
| `audit` | Review supplied images and their placement, files, rights, lineage, and evidence | Viewing or inspection capability | Not required unless separately retrieving private evidence |

Name one primary mode, decision, owner, audience, customer situation, asset role, channel and placement, market, deadline, and external-action boundary. A task may include supporting steps from another mode, but do not hide which mode owns completion.

## Run The Capability And Dependency Gate

`create` mode always requires a real production capability. It does not always require the user to configure an external API.

| Production path | Typical dependency | API / Key | Third-party account | Local runtime |
| --- | --- | --- | --- | --- |
| Agent-provided image capability | Tool must actually be available in the current environment | Usually no user-managed Key; the platform may handle access | Usually none beyond the current environment | Tool-specific |
| External image API | Supported provider, network access, quota, and billing | Usually API Key, OAuth, or provider Token | Usually required | API client or supported tool |
| Hosted image or design application | Human or authorized integration access | Not needed for manual use; OAuth or Token may be needed for automation | Usually required | Browser or application |
| Local or self-hosted model | Compatible model, weights, disk, memory, and inference service | No external Key unless downloading or calling another service | Usually none | Often Python, GPU runtime, ComfyUI, or equivalent |
| Deterministic composition or optimization | Existing source assets and installed rendering utilities | Usually none | Usually none | ImageMagick, libvips/Sharp, `cwebp`, or equivalent |

Before production:

1. inventory the image-generation, editing, browser, design, scripting, and file-inspection capabilities actually available;
2. identify whether the chosen path is built-in, external API, hosted application, local model, or deterministic renderer;
3. record the tool or provider, interface, credential owner, network need, quota, billing or credit constraint, output rights, data handling, and expected file access;
4. confirm local creation is authorized and distinguish it from publishing, account changes, or external execution;
5. verify that essential source assets, rights, claims, product truth, copy, dimensions, and acceptance criteria are available;
6. if no suitable capability exists, complete the brief, prompts, source plan, and handoff without claiming that files were generated.

Never ask the user to paste secrets into a prompt, report, image metadata, or manifest. Ask them to configure credentials in the supported environment or use an already authorized tool. Check only whether access is available; do not expose secret values. API authentication does not establish source rights, brand approval, publication authority, or permission to use a person, product, or platform account.

When several production paths are available, explain the tradeoff before choosing:

- output quality and instruction following;
- reference-image, masking, inpainting, outpainting, background, and batch support;
- reliable text, logo, product UI, chart, and layout handling;
- brand consistency and repeatability across a campaign;
- supported ratio, resolution, transparency, vector, and file formats;
- latency, rate limits, cost per candidate, subscription, and retry cost;
- availability, payment, data routing, content rules, and support in the target market, including China;
- automation, local file access, provenance, retention, and deletion controls.

Do not present a model, price, platform specification, API, or regional availability as current without a dated official source. Provider examples are options to evaluate, not mandatory dependencies.

## Gather The Minimum Useful Input

Read existing product, brand, campaign, and market context before asking questions. Ask only for missing information that changes production or approval.

Required for every mode:

- objective, decision, owner, audience, situation, image role, destination, and desired next action;
- channel, platform, placement, market, language, locale, deadline, and requested output;
- product truth, offer, proof, claims, limitations, exact approved copy, and prohibited wording;
- available logo, brand colors, type, design system, product captures, source images, and examples;
- rights, licenses, people or likeness permissions, disclosure, approvals, and external-action boundary.

Additional `create` inputs:

- chosen or available production path, credentials status, budget or credits, candidate count, and iteration limit;
- dimensions, aspect ratio, safe area, crop behavior, resolution, transparency, color mode, format, file-size target, and naming;
- source files at sufficient quality, preserve list, edit mask or selection where applicable, and acceptance criteria.

Additional `audit` inputs:

- actual image files or inspectable captures, intended placement, surrounding copy, target dimensions, and destination;
- source and rights records, current version, approval status, known performance evidence, and reported concerns.

If exact dimensions or platform requirements are missing, either request the current placement specification or mark it `unavailable`. Do not invent the latest requirements from memory.

## Choose The Production Approach

| Approach | Prefer when | Avoid when |
| --- | --- | --- |
| AI generation | An original visual field, scene, illustration, texture, or conceptual metaphor is needed | Exact UI, logo, long copy, legal text, or attributable data must be reproduced |
| AI editing | A licensed source needs a bounded background, object, crop, lighting, or contextual change | The edit would misrepresent identity, product state, evidence, endorsement, or rights |
| Real screenshot plus composition | The audience must inspect the actual product or workflow | The product state is unavailable or the screenshot contains private data |
| Deterministic template | Brand consistency, exact typography, repeatable layout, or many size variants matter | The visual concept itself has not been decided |
| Data rendering | A chart, diagram, comparison, or infographic must remain attributable and exact | The underlying data, units, source, period, or uncertainty are missing |
| Licensed or commissioned source | Authentic people, places, products, or documentary context are required | License, release, derivative, market, or media rights are unresolved |

Use AI to create the parts that benefit from synthesis. Use deterministic composition for exact text, logos, interface captures, charts, disclaimers, alignment, and repeatable layout. Do not force one tool to perform every stage.

## Handle Common Marketing Image Jobs

### Website, Landing Page, Blog, And Open Graph

- decide whether the image demonstrates the real product, explains a mechanism, supports recognition, or establishes context;
- keep the focal point and essential content within the actual responsive crop and text-overlay region;
- provide explicit intrinsic dimensions, responsive variants, meaningful alt text, and a compressed web format;
- verify the Open Graph and social preview crop when that is part of the task;
- coordinate message and destination continuity with `activation` when conversion depends on the page.

### Social, Community, And Organic Distribution

- verify the current platform, account, placement, ratio, safe area, file, caption, and content-review requirements;
- create placement-specific compositions rather than stretching one universal file;
- test the image at actual feed size and on mobile, including avatar, UI, caption, and crop obstruction;
- for China, keep WeChat, Weibo, Xiaohongshu, Douyin, Bilibili, Kuaishou, language, account, review, ad status, and market requirements separate.

### Product Screenshots And Mockups

- capture or use an approved real product state at sufficient resolution;
- remove or replace private data before composition;
- add device frames, backgrounds, callouts, zooms, or annotations deterministically;
- label conceptual or future-state interfaces clearly;
- never ask a generative model to recreate an exact current UI and present it as real.

### Banners, Profiles, Directories, And Marketplace Listings

- verify current dimensions and obstruction zones for the exact destination;
- favor real product evidence and concise copy at small display sizes;
- preserve critical content across desktop, mobile, thumbnail, and cropped previews;
- route app-store screenshot strategy to `aso-audit` and directory submission packages to `seo-audit` where appropriate.

### Ads And Campaign Systems

- route audience, promise, proof, concept hypothesis, placement strategy, and test design to the Ad Creative module in `content-strategy` when needed;
- keep concept, composition, and execution variants separately identified;
- map every asset to campaign, audience, placement, offer, destination, and learning purpose;
- do not infer platform approval or performance from visual polish.

### Charts, Diagrams, And Infographics

- render from attributable structured data where possible;
- include labels, units, source, period, uncertainty, and a text equivalent;
- do not rely on color alone or use generative output for exact values;
- inspect every number and relationship after export.

## Freeze The Image Contract

Record product and available surface; audience, job, state, problem, value pillar, angle, offer, proof, CTA, destination, image role, concept and variant lineage; channel, platform, account, placement, format, dimensions, aspect ratio, safe area, crop, device, file type, size and quality; exact copy, language, locale, hierarchy, brand, logo, colors, typography, product UI, data, chart, source image, person, model, property, trademark, copyright, license, derivative, generative-use permission, disclosure, claim, approval, accessibility, alt text, owner, version, review, measurement, tool dependency, and requested external action.

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder or platform statement without inspectable support may be a `reported signal` with no evidence state. Never invent product UI, customer identity, quote, logo, result, statistic, certification, rating, award, scarcity, price, availability, before-and-after outcome, endorsement, source ownership, model release, or platform requirement.

Classify missing inputs:

- `blocking`: production would become false, unsafe, unusable, or impossible;
- `deferrable`: a provisional concept or placeholder can be produced and labeled;
- `optional`: improves quality or confidence but is not needed for the current decision.

## Separate Concept, Composition, And Variant

Define the concept before production:

```text
audience situation x problem or belief x value pillar x angle
-> truthful visual proof or explanatory mechanism
-> message hierarchy and next action
-> destination continuity and qualified outcome
```

A concept changes the customer, problem, value, proof, objection, offer, or visual mechanism. A composition changes the spatial system used to express it. An execution variant changes crop, ratio, background, framing, copy length, CTA treatment, language, or placement constraints while preserving the hypothesis. File count is not concept diversity.

Choose the image's job: show the real product, demonstrate a workflow, explain a mechanism, visualize attributable data, establish a setting, communicate an offer, provide editorial context, support recognition, or another explicit role. Do not substitute generic atmosphere for inspectable product evidence when the audience needs to evaluate the product.

For an ordinary one-off task, propose a small set such as two or three meaningfully different concepts, select one, then create only the purposeful placement or localization variants. Increase volume only when distribution and learning justify it.

## Produce From Traceable Sources

For generation, specify subject, action, environment, visual treatment, viewpoint, lighting, materials, color, depth, composition, copy-free regions, product requirements, factual boundaries, brand cues, negative constraints, ratio, resolution, and intended post-processing.

For editing, specify source asset, exact selection or mask, requested change, preserve list, rights, edge behavior, perspective, shadow, reflection, background, color, resolution, crop, metadata, and acceptance criteria.

For deterministic composition, specify canvas, grid, margins, safe areas, focal point, layers, source locators, typography, line breaks, logo clear space, alignment, responsive crop, export formats, and naming.

Do not prompt for living artists' exact style, counterfeit brand assets, deceptive documentary evidence, fake customers or endorsements, misleading body or product outcomes, or sensitive personal inference. Do not reproduce a competitor image, remove watermarks, expose private information, or use an accessible public image as proof of reuse rights.

Use a real supplied logo rather than regenerating it. Use approved product screenshots or a clearly labeled conceptual mockup; never let a generated UI imply available functionality. Build charts from attributable structured data with labels, units, source, period, and uncertainty. Route copy to `copywriting`, public communications usage to the Public Relations module in `content-strategy`, and localization claims to the appropriate market owner.

## Generate, Edit, And Iterate Honestly

In `create` mode:

1. preserve originals and create a versioned working location;
2. choose the lowest-cost appropriate capability for exploration and a suitable final capability for delivery;
3. generate or edit a small purposeful candidate set;
4. inspect the actual files, not only tool responses or filenames;
5. compare candidates against the frozen contract and acceptance criteria;
6. make targeted edits or deterministic overlays instead of regenerating everything when possible;
7. produce required placement, language, and format variants from the approved parent;
8. record tool or model, interface, prompt or edit instruction, source assets, date, output ID, dimensions, and lineage where available.

Do not claim an image exists without an inspectable file. Do not overwrite source assets. Do not treat generative output as automatically original, rights-cleared, accurate, accessible, approved, or ready to publish.

## Optimize And Package Files

Choose the output format by content and destination:

- use WebP or AVIF where supported for efficient web delivery, with an appropriate fallback when required;
- use JPEG for broadly compatible photographic delivery where transparency is unnecessary;
- use PNG for lossless screenshots, sharp interface detail, or transparency when file size remains acceptable;
- use SVG only for genuine vector assets with safe, inspectable content;
- preserve an editable source or layered template when the asset must be updated repeatedly.

Before running an optimization command, check that the utility exists and work on a copy. Typical options include ImageMagick, libvips or Sharp, `cwebp`, `avifenc`, `pngquant`, `oxipng`, and `jpegoptim`. Record the command or settings when reproducibility matters.

Resize to the largest actual display requirement rather than shipping an oversized master everywhere. Preserve aspect ratio unless the contract explicitly defines a crop. Remove unnecessary sensitive metadata, retain required attribution or color information, and compare visible quality before and after compression.

For web delivery, specify intrinsic width and height, responsive sources where needed, loading priority, lazy loading for eligible below-the-fold images, and the expected placement. Avoid layout shift and do not hide essential information only in pixels.

## QA Every Delivered Asset

Inspect at final pixel dimensions and representative placement. Verify:

- subject, product, person, object, anatomy, reflections, shadows, perspective, and artifacts;
- exact copy, spelling, numbers, price, disclaimer, line breaks, and text fit;
- hierarchy, focal point, crop, safe area, contrast, legibility, and destination continuity;
- real logo geometry, clear space, brand colors, typography, and prohibited elements;
- chart values, axes, units, legends, source, period, and uncertainty;
- locale, glyph support, text expansion, cultural context, product surface, and claims;
- alt text, text equivalent, decorative state, color independence, and actual-size accessibility;
- dimensions, color mode, transparency, format, file size, compression, metadata, naming, version, and checksum where useful;
- source rights, person permissions, approvals, disclosure, tool lineage, and external-action boundary.

Provide alt text according to the image's actual purpose and surrounding content; decorative images may need an empty alternative. Keep functional CTA controls and essential instructions outside image pixels.

## Learn Without Overclaiming

Map delivery results back to concept, composition, variant, audience, placement, message, offer, and destination. Keep viewability, attention, interaction, qualified response, first value, retention, refunds, contribution, accessibility, complaints, and causal evidence separate. Platform performance cannot prove image quality or incrementality when delivery, audience, offer, placement, page, or budget differs.

## Deliver In Order

Return:

1. mode, decision, owner, audience, image role, channel, placement, market, and action boundary;
2. production path and dependency report covering tool, API, Key or Token, account, network, runtime, budget, quota, and unavailable capabilities;
3. evidence, copy, claim, product, brand, source, rights, person, approval, and limitation ledger;
4. concept and visual mechanism with composition and variant lineage;
5. production brief, generation, edit, composition, or optimization instructions and source plan;
6. actual local output manifest when files were created, including filenames, dimensions, formats, sizes, source lineage, tool, version, and QA state;
7. placement, localization, accessibility, responsive delivery, file, and QA matrix;
8. measurement, learning, update, retirement, approvals, handoffs, Playbook sources, and unresolved evidence.

For a simple request, keep the response compact but do not omit the chosen production path, required dependencies, essential missing inputs, actual file status, or QA result.

## Preserve Market And Action Boundaries

For China work, keep China, language, locale, audience, product surface, provider, platform, account, placement, format, dimensions, payment, data routing, content review, advertising, claims, celebrity or creator identity, portrait rights, fonts, trademarks, map or national symbols, app distribution, and applicable rules separate. Do not infer provider availability, API access, account access, format requirements, image rights, content acceptance, or legal conditions from China or Simplified Chinese.

This Skill may create and edit local image files when a suitable capability is actually available and the task authorizes local creation. Do not access asset libraries, design tools, social, ad, CMS, DAM, email, marketplace, directory, analytics, or customer systems without separate authorization; scrape or download restricted images; acquire rights; contact people; upload, publish, schedule, syndicate, advertise, or send assets; change live pages, campaigns, listings, product UI, brand systems, or budgets; or claim approval, publication, delivery, performance, or results.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that mode, decision, audience, image role, production path, API and credential dependency, runtime, budget, concept, composition, variants, product truth, copy, claims, proof, sources, rights, people, brand, channel, placement, dimensions, safe areas, localization, accessibility, files, optimization, QA, lineage, measurement, owners, approvals, and action boundaries are explicit; public is not rights-cleared; generated is not factual proof; files are inspected before delivery; asset count is not learning; and no unauthorized external action occurred.
