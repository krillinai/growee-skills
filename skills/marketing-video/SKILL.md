---
name: marketing-video
description: Use when a team needs to brief, script, storyboard, generate, record, edit, render, repurpose, translate, subtitle, dub, optimize, audit, or govern marketing videos for websites, ads, social, product demos, customer stories, sales, PR, education, events, app stores, and campaign systems; or needs to choose video models, APIs, avatars, accounts, credentials, local runtimes, formats, and delivery workflows while preserving product truth, rights, accessibility, localization, lineage, and file QA.
---

# Marketing Video

Turn one bounded audience decision into truthful, comprehensible, accessible, production-ready video and purposeful adaptations. Optimize qualified customer understanding and downstream value, not video volume, opening-hook metrics, watch time, engagement, attributed conversion, or production polish alone.

## Read The Relevant References

- Read [video-contract.md](references/video-contract.md) before accepting product, claim, script, footage, person, voice, music, brand, channel, or rights evidence.
- Read [tools-and-dependencies.md](references/tools-and-dependencies.md) before selecting a video model, avatar service, API, editing application, programmatic renderer, local model, KrillinAI workflow, or delivery stack.
- Read [scripting-storyboard-and-production.md](references/scripting-storyboard-and-production.md) before scripting, storyboarding, recording, generating, editing, compositing, templating, or repurposing.
- Read [localization-rights-and-accessibility.md](references/localization-rights-and-accessibility.md) before transcription, translation, captions, subtitles, dubbing, voice work, market adaptation, or accessibility review.
- Read [delivery-qa-and-measurement.md](references/delivery-qa-and-measurement.md) before rendering, encoding, delivery, player QA, performance analysis, or retirement.
- Use [playbook-sources.md](references/playbook-sources.md) when citing the pinned Growth Playbook basis.

Do not load provider details merely to write a brief or script. Do load them when the user asks what tool, model, account, API, runtime, budget, or production path is needed.

## Select One Primary Mode

| Mode | Use | Media capability | External credentials |
| --- | --- | --- | --- |
| `brief` | Freeze communication, evidence, production, rights, delivery, and learning requirements | Not required | Not required |
| `script` | Create or revise the script, beats, storyboard, shot list, source plan, and acceptance criteria | Not required | Not required |
| `create` | Record, generate, animate, composite, edit, render, or encode actual local video files | Required | Depends on the selected production path |
| `adapt` | Translate, subtitle, dub, reframe, shorten, reconstruct, or repackage an existing video | Required only for the requested adaptation stages | Depends on transcription, translation, voice, editing, and rendering tools |
| `audit` | Review supplied video, script, project, captions, audio, rights, formats, lineage, or performance evidence | Playback and inspection capability | Not required unless separately retrieving private evidence |

Name one primary mode, decision, owner, audience, customer situation, video role, channel and placement, market, deadline, and external-action boundary. A requested file format is not a mode. Supporting steps may use another mode, but do not hide which mode owns completion.

## Run The Capability And Dependency Gate

`create` mode always requires a real video production or rendering capability. `adapt` requires only the capabilities needed for the declared operations. Neither mode always requires the user to configure an external API.

| Production path | Typical dependency | API / Key | Third-party account | Local runtime |
| --- | --- | --- | --- | --- |
| Agent-provided video capability | Tool must actually be available and return inspectable artifacts | Usually no user-managed Key; platform access may be handled | Usually none beyond the current environment | Tool-specific |
| External video generation or editing API | Provider, network, queue, quota, credits, supported inputs and outputs | Usually API Key, OAuth, or Token | Usually required | SDK, HTTP client, or supported tool |
| Avatar, presenter, voice, or dubbing service | Authorized identity, voice, script, language, and usage scope | API or OAuth for automation | Usually required | Browser or API client |
| Hosted editing or design application | Human or authorized integration access | Not needed for manual use; OAuth or Token may be needed for automation | Usually required | Browser or application |
| Programmatic video renderer | Template or code, assets, fonts, browser engine, renderer, and encoder | Usually none locally; cloud rendering may require credentials | Depends on hosting | Node.js, browser runtime, FFmpeg, or framework-specific tools |
| Local or self-hosted model | Compatible model, weights, GPU, memory, storage, and inference workflow | No external Key unless downloading or calling another service | Usually none | Often Python, GPU runtime, ComfyUI, FFmpeg, or equivalent |
| KrillinAI localization and rendering | Installed and authorized CLI capabilities plus source media and language inputs | Depends on configured upstream services | Depends on selected services | KrillinAI CLI and its required media tools |
| Deterministic edit, encode, or package | Source files, project instructions, captions, audio, graphics, and codecs | Usually none | Usually none | FFmpeg, ffprobe, media libraries, or equivalent |

Before production:

1. inventory the video-generation, audio, voice, transcription, translation, subtitle, image, browser, editing, rendering, and inspection capabilities actually available;
2. identify whether the path is built-in, external API, hosted application, programmatic renderer, local model, KrillinAI workflow, recording handoff, or deterministic edit;
3. record the provider or tool, interface, credential owner, network need, queue, quota, billing or credit constraint, output retention, local file access, and expected artifacts;
4. confirm local production is authorized and distinguish it from recording people, accessing private systems, publishing, account changes, or external execution;
5. verify essential product, script, footage, source, person, voice, music, rights, brand, claims, placement, and output constraints;
6. if a required stage is unavailable, complete the script, storyboard, prompts, edit decision list, source plan, and handoff without pretending that media was created.

Never ask the user to paste secrets into a prompt, script, report, subtitle, project file, metadata, or manifest. Ask them to configure credentials in the supported environment or use an already authorized tool. Check only whether access is available; do not expose secret values. API access does not establish footage, music, likeness, voice, training, publication, or platform rights.

When several paths are available, explain the tradeoff before choosing:

- text-to-video, image-to-video, video-to-video, reference, consistency, editing, extension, and lip-sync support;
- exact control over script, timing, camera, motion, product UI, text, graphics, captions, and layout;
- native audio, voice, music, sound effect, avatar, and multilingual support;
- duration, resolution, frame rate, ratio, transparency, codec, container, and project-file support;
- deterministic templates, batch rendering, personalization, reproducibility, and local file access;
- latency, asynchronous jobs, queue, rate limits, cost per second or minute, subscription, credits, and retry cost;
- model or asset retention, training use, identity controls, provenance, watermarking, and commercial terms;
- availability, payment, invoice, data routing, content review, and support in the target market, including China.

Do not present a model, price, maximum duration, API, platform specification, regional availability, or legal condition as current without a dated official source.

## Gather The Minimum Useful Input

Read existing product, brand, campaign, and market context before asking questions. Ask only for missing information that changes production or approval.

Required for every mode:

- objective, intended audience decision, owner, audience, situation, video role, destination, and CTA;
- channel, platform, placement, player, market, language, locale, deadline, duration range, and requested output;
- actual product workflow, offer, proof, claims, limitations, spoken copy, on-screen copy, and prohibited wording;
- available footage, screen recordings, images, logo, brand, fonts, graphics, audio, music, product captures, and examples;
- people, voices, likeness, music, footage, font, template, and generative-use rights, disclosures, approvals, and expiry;
- external-action boundary covering recording, system access, upload, publication, advertising, and account changes.

Additional `create` inputs:

- chosen or available production path, credentials status, budget or credits, candidate count, render limit, and deadline;
- script, storyboard or minimum beat plan, source plan, capture requirements, presenter or voice decision, and acceptance criteria;
- dimensions, ratio, safe area, resolution, frame rate, duration, container, codecs, audio, captions, thumbnail, file-size target, and naming.

Additional `adapt` inputs:

- rights-cleared source master, transcript status, target language and locale, caption and subtitle requirements, voice and dubbing scope, pronunciation, on-screen graphics, target placements, and local reviewer;
- operations requested independently: trim, re-edit, reframe, translate, subtitle, dub, lip-sync, replace graphics, replace product screen, change footage, render, or package.

Additional `audit` inputs:

- actual video, audio, caption, subtitle, transcript, thumbnail, project or inspectable captures;
- intended placement and player, source and rights records, current version, approval status, known performance evidence, and reported concerns.

If exact platform requirements are missing, request a current placement specification or mark it `unavailable`. Do not invent the latest duration, dimensions, safe areas, codecs, caption behavior, or review rules from memory.

## Choose The Production Approach

| Approach | Prefer when | Avoid when |
| --- | --- | --- |
| Real product or screen capture | The audience must inspect actual behavior, sequence, latency, controls, or UI | The product state is unavailable, private, unstable, or misleading |
| Recorded presenter, customer, or event | Authentic identity, testimony, expertise, demonstration, or documentary context matters | Consent, release, testimony, setting, or recording authorization is unresolved |
| Programmatic template | Exact text, branding, data, repeatability, personalization, or many controlled variants matter | The narrative and visual system are not defined |
| AI video generation | Original B-roll, visual metaphor, animation, transition, or impractical scene is needed | Exact product, person, place, documentary fact, long copy, or attributable data must be reproduced |
| AI avatar or synthetic presenter | Authorized repeatable delivery or multilingual presentation is appropriate | Authentic founder, customer, expert, or documentary presence is material to trust |
| Edit and repurpose | Rights-cleared long-form footage contains reusable moments | Context, claim, speaker meaning, or source integrity would be lost |
| Localization pipeline | A validated source needs subtitles, dubbing, graphics, format, and market reconstruction | Translation, voice, product, rights, or local review is unresolved |
| Hybrid production | Real product and deterministic layers need generated or licensed supporting media | Source classes cannot be clearly disclosed and traced |

Use generation for the layers that benefit from synthesis. Use real captures and deterministic composition for exact product UI, logos, text, charts, disclaimers, captions, callouts, and repeatable layout. Do not force one model or application to perform every stage.

## Handle Common Marketing Video Jobs

### Product Demo And Feature Announcement

- define the one workflow or decision the viewer must understand;
- use approved real product capture for inspectable behavior;
- script cursor, taps, states, delays, permissions, warnings, and representative data;
- add titles, callouts, zooms, highlights, and narration deterministically;
- keep generated footage to contextual or non-factual supporting layers.

### Explainer And Educational Video

- choose a treatment such as presenter, voiceover plus graphics, product walkthrough, mechanism animation, or hybrid;
- map every beat to a customer question, claim source, visual proof, and acceptance criterion;
- preserve comprehension without sound through captions and supporting visuals;
- use a template when the format will repeat.

### Social Short, Ad, And Campaign Variant

- verify the exact platform, account, placement, player, duration, ratio, safe area, caption, thumbnail, file, and review requirements;
- design the opening around the audience decision and evidence rather than a universal hook rule;
- create placement-specific edits and format adaptations instead of stretching one master everywhere;
- route concept hypothesis and test strategy to the Ad Creative module in `content-strategy` when needed.

### Customer Story, Interview, PR, And Event

- verify participant identity, testimony, source, releases, edit scope, market, media, paid use, term, and approval;
- preserve meaning and context when trimming or restructuring;
- distinguish documentary footage, reenactment, generated media, and illustrative B-roll;
- route evidence development to `customer-research` and public communications use to the Public Relations module in `content-strategy` when appropriate.

### Long-Form Repurposing

- index the source by topic, speaker, claim, timecode, context, and rights;
- select moments for a declared audience and destination rather than a generic virality score;
- produce an edit decision list before rendering;
- preserve qualifiers, speaker meaning, visual evidence, and source lineage;
- reconstruct captions, graphics, opening context, CTA, and format for each placement.

### Programmatic And Batch Video

- freeze the template schema, variable inputs, allowed ranges, fonts, assets, motion system, audio, duration, and validation rules;
- separate data-driven instances from creative concepts;
- render a small representative sample before a batch;
- validate missing data, overflow, long words, unsupported glyphs, blank assets, timing, and output naming;
- stop the batch when representative QA fails.

### Localization And Multilingual Delivery

- separate transcription, same-language captions, subtitle translation, transcreation, dubbing, voice replacement, lip-sync, graphics reconstruction, product-screen replacement, footage adaptation, and format adaptation;
- when installed and authorized, route subtitles to `krillinai-subtitle`, target-language dubbing to `krillinai-tts`, landscape rendering to `krillinai-render-horizontal`, portrait rendering to `krillinai-render-vertical`, and multi-stage work to `krillinai-pipeline`;
- preserve approved meaning, evidence, speaker identity, voice permission, product availability, offer, destination, and disclosure;
- require a target-language and market review of the mastered asset.

For China, keep WeChat Channels, Douyin, Xiaohongshu, Kuaishou, Bilibili, platform account, ad or organic status, review path, music, portrait, voice, font, product, payment, data, and market requirements separate.

## Freeze The Video Contract

Record product and available surface; audience, job, state, problem, belief, value pillar, angle, promise, offer, proof, objection, CTA, destination, video role, concept, narrative, edit and format lineage; script, visual, spoken line, on-screen text, claim, demonstration, source and timecode; brand, logo, colors, typography, motion language, product UI; footage, image, animation, music, sound, voice, person, creator, customer, property, trademark, copyright, license, release, derivative, synthetic state, disclosure and approval; channel, platform, account, placement, player, device, duration, dimensions, ratio, safe area, frame rate, container, codec, audio, caption, thumbnail and file requirements; language, locale, translation, transcreation, dubbing, lip sync, text expansion, accessibility and transcript; tool dependency, owner, version, review, output manifest, measurement, expiration and requested external action.

Use `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder or platform statement without inspectable support may be a `reported signal` with no evidence state. Missing private evidence is unavailable, not a penalty and not permission to invent it.

Never fabricate product behavior, UI, customer identity, quotation, testimonial, result, statistic, review, rating, certification, award, scarcity, price, endorsement, news coverage, documentary event, source ownership, release, platform rule, or performance. A conceptual or future-state product sequence must be visibly labeled and cannot imply current availability.

Classify missing inputs:

- `blocking`: production would become false, unsafe, unusable, or impossible;
- `deferrable`: a provisional script, storyboard, rough visual, or placeholder can be produced and labeled;
- `optional`: improves quality or confidence but is not needed for the current decision.

## Separate Concept, Narrative, Edit, And Format

Use this lineage:

```text
audience situation x problem or belief x value pillar x proof mechanism
-> concept and intended decision
-> narrative beats and production treatment
-> edit variants
-> format and localization adaptations
-> placement, destination, and qualified outcome
```

A concept changes the audience, problem, belief, value, objection, offer, proof, or explanatory mechanism. A narrative treatment changes how that concept unfolds through demonstration, story, presenter, interview, animation, or comparison. An edit variant changes opening shot, pacing, beat order, duration, CTA treatment, music, captions, B-roll, or presenter take while preserving the hypothesis. A format adaptation changes ratio, crop, safe area, resolution, language, subtitle or dubbing treatment, thumbnail, or placement packaging. File count is not concept diversity.

For an ordinary one-off task, propose a small set of meaningfully different treatments, select one, produce a rough or representative segment, then create only purposeful edit, placement, accessibility, or localization variants. Increase volume only when distribution and learning justify it.

## Script And Storyboard From Product Truth

Choose the video's job: demonstrate a real workflow, explain a mechanism, answer an objection, show attributable customer evidence, establish a use context, present an offer, educate, document, support recall, or another explicit role. When customers need to inspect the product, show an approved real product state rather than generic atmosphere or fabricated UI.

Map every spoken line, on-screen claim, demonstration, result, quote, statistic, comparison, and disclaimer to an attributable source and approval. Build narrative beats around the intended decision, not a universal hook formula. Do not invent a mandatory duration, opening-seconds rule, shot count, caption style, posting volume, or benchmark.

Create a beat-based or time-coded script, storyboard, and shot list detailed enough to reveal missing proof, footage, rights, product states, graphics, audio, localization, accessibility, and production dependencies. Keep visual, spoken words, on-screen text, sound, source, timing, and acceptance criteria synchronized.

## Produce From Traceable Sources

For recording, specify capture method, resolution and frame rate from the delivery contract, orientation, screen or camera area, camera movement, light, background, audio path, room tone, performance, product data, takes, releases, and backups.

For generation, specify subject, action, setting, camera, motion, duration, continuity, composition, lighting, materials, brand cues, copy-free regions, factual constraints, negative constraints, ratio, resolution, native audio decision, and intended post-processing.

For editing, specify source, in and out points, preserve list, sequence, crop, speed, stabilization, transition, color, audio, graphics, captions, mask or composite, disclosure, target format, and acceptance criteria.

For programmatic rendering, specify canvas, frame rate, timeline, scene schema, variable data, safe areas, fonts, layout, animation, media locators, audio, captions, responsive formats, render command, failure behavior, and naming.

Do not prompt for a living artist's exact style, counterfeit brand media, fake customers or documentary evidence, deceptive body or product outcomes, non-consensual intimate or sensitive depiction, or misleading impersonation. Do not reproduce competitor videos, remove watermarks or disclosures, expose private information, or treat public availability as reuse permission.

Use approved recordings for exact product behavior, logos, UI, charts, customer testimony, and factual events. Clearly disclose synthetic or materially altered people, voices, footage, or scenes when required. Never clone or imitate a voice, face, identity, or creator delivery without attributable scoped permission.

## Produce, Adapt, And Iterate Honestly

In `create` or `adapt` mode:

1. preserve source masters, project files, stems, captions, transcripts, and graphics in a versioned working location;
2. choose a low-cost appropriate path for tests and a suitable final path for delivery;
3. produce a storyboard sample, short representative segment, or small purposeful candidate set before a full render when feasible;
4. inspect actual visual, audio, caption, subtitle, and file artifacts rather than relying on tool responses;
5. compare the result against the frozen contract and acceptance criteria;
6. make targeted edits, deterministic overlays, subtitle corrections, or audio repairs instead of regenerating everything when possible;
7. create declared edit, ratio, caption, audio, language, and placement variants from an approved parent;
8. record tool or model, interface, prompt or edit instruction, source assets, project or workflow, render date, output ID, duration, dimensions, codecs, and lineage where available.

Do not claim a rendered file, transcript, subtitle, translation, dub, thumbnail, project, or QA pass exists without an inspectable artifact. Generative output is not automatically factual, original, rights-cleared, accessible, localized, approved, or ready to publish.

## Encode And Package Delivery

Choose container, video codec, audio codec, frame rate, bitrate or quality, resolution, color, caption method, and thumbnail from the actual destination requirements. Common technical options include MP4 or MOV containers, H.264, HEVC, AV1 or VP9 video, and AAC or Opus audio, but no option is universal.

Before running FFmpeg, ffprobe, a programmatic renderer, subtitle converter, or another media utility, confirm that it exists, inspect supported codecs, and work from preserved sources. Record commands, versions, and settings when reproducibility matters. Use deterministic transcode, crop, pad, overlay, audio, caption, and packaging steps where they are more reliable than regeneration.

Keep source master, mezzanine or edit master, platform exports, captions, subtitles, transcript, audio stems, thumbnail, project file, and manifest distinct. Do not silently recompress a previous delivery export into another final export when a suitable master exists.

For web delivery, define player context, poster, intrinsic dimensions, preload or loading behavior, caption tracks, controls, autoplay and mute assumptions, fallback, and performance budget. A valid video file does not prove the destination player is accessible or correctly configured.

## Localize The Whole Asset

Translate intended meaning, not isolated words. Preserve factual and commercial scope. Fit reading and speaking pace through supported rewriting, timing, pauses, shot changes, or graphics reconstruction; do not delete qualifications merely to make a dub fit.

Validate names, product terms, numbers, dates, prices, currency, units, pronunciation, speaker changes, meaningful non-speech audio, subtitles, dubbed delivery, on-screen text, fonts, glyphs, safe areas, product screens, offer, CTA, destination, market rights, and disclosures against the mastered asset.

Permission to record a person is not permission to clone, translate, alter, impersonate, advertise with, or reuse their voice. Do not imply that a translated synthetic voice is the person's original speech.

## Make Meaning Accessible

Provide accurate synchronized captions for meaningful speech and sound, a transcript where useful, sufficient contrast and text size at representative playback, audio-independent understanding for core decisions, and audio description or an equivalent when essential visual information is otherwise unavailable. Do not rely on sound, color, rapid cuts, or tiny embedded text as the only carrier of meaning.

Review flashing, motion, readability, speaker identification, non-speech audio, caption timing, line breaks, safe areas, and player context. Keep essential CTA and instructions available outside the video when the surrounding interface can carry them.

## Inspect Every Delivered File

Review actual exports at final dimensions and representative players. Verify:

- file opens, duration, dimensions, display aspect, orientation, frame rate, container, codecs, audio channels, size, metadata, and checksum where useful;
- no unintended black, blank, frozen, repeated, corrupted, or missing frames;
- no dropped audio, clipping, distortion, noise, unintended silence, drift, or lip-sync error;
- exact spoken and on-screen copy, product state, numbers, prices, labels, disclaimer, CTA, source, and destination continuity;
- person identity, testimony, synthetic state, disclosure, footage, music, voice, font, license, release, and expiry;
- logo geometry, color, typography, graphics, charts, animation, transitions, crop, focal point, and safe areas;
- caption and subtitle words, speakers, sounds, timing, line breaks, font, glyphs, contrast, placement, language tag, filename, and player behavior;
- translation, dub, pronunciation, meaning, voice, synchronization, product, offer, CTA, local destination, and market review;
- accessibility, transcript, audio-independent meaning, audio description, motion, and flashing review;
- thumbnail truth, crop, copy, product, rights, filename, version, lineage, project or master reference, and manifest.

Inspect the actual file with suitable playback and metadata tools. A timeline preview, successful API response, render job ID, or filename alone is not a QA pass.

## Learn Without Overclaiming

Map results to audience, concept, narrative, edit, format, locale, creator, placement, offer, and destination. Keep eligible delivery, viewable start, watch depth, qualified completion, interaction, response, first value, revenue, retention, refunds, contribution, accessibility, complaints, rights incidents, attribution, and causality separate. Platform delivery, watch time, completion, or attributed conversion does not prove video quality or incrementality when audience, auction, creator, placement, offer, page, budget, maturity, or exposure differs.

## Deliver In Order

Return:

1. mode, decision, owner, audience, video role, channel, placement, market, and action boundary;
2. production path and dependency report covering video, audio, subtitle and render capabilities; API, Key or Token; account; network; runtime; budget; quota; queue; and unavailable stages;
3. product, claim, script, source, footage, person, voice, music, brand, rights, approval, and limitation ledger;
4. concept, intended decision, narrative treatment, edit and format lineage;
5. script, storyboard, shot list, source plan, prompts, edit decision list, localization instructions, and production handoff;
6. actual local video, audio, caption, subtitle, transcript, thumbnail, project, and delivery manifest when artifacts were created;
7. localization, accessibility, format, player, encoding, placement, and file-QA matrix;
8. measurement, learning, update, expiration, retirement, approvals, handoffs, Playbook sources, and unresolved evidence.

For a simple request, keep the response compact but do not omit the production path, required dependencies, essential missing inputs, actual artifact status, or QA result.

## Preserve Market And Action Boundaries

For China work, keep China, language, locale, audience, product surface, provider, platform, account, placement, format, payment, invoice, data routing, content review, advertising, claims, creator or celebrity identity, portrait and voice rights, music, fonts, maps or national symbols, app distribution, and applicable rules separate. Do not infer provider availability, API access, account access, format requirements, review acceptance, rights, or legal conditions from China or Simplified Chinese.

This Skill may create, edit, localize, and render local files only when suitable capabilities are actually available and the task authorizes local production. Do not access cameras, microphones, cloud drives, asset libraries, editing tools, social, ad, CMS, DAM, email, marketplace, analytics, or customer systems without separate authorization; record people; scrape or download restricted media; acquire rights; contact participants; upload, publish, schedule, syndicate, advertise, or send videos; change live pages, campaigns, listings, product UI, accounts, or budgets; or claim approval, publication, delivery, performance, or results.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that mode, decision, audience, video role, production path, API and credential dependency, runtime, budget, concept, narrative, variants, script, storyboard, shots, product, claims, sources, footage, people, voices, music, brand, rights, channel, placement, formats, localization, accessibility, files, captions, audio, thumbnail, encoding, player, QA, lineage, measurement, owners, approvals, expiration, and action boundaries are explicit; public is not rights-cleared; generated is not factual proof; voice cloning requires scoped permission; captions are not automatically accurate; files are inspected before delivery; asset volume is not learning; and no unauthorized external action occurred.
