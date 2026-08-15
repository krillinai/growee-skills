---
name: customer-research
description: Use when work needs to plan and synthesize customer research and decision-linked surveys with explicit sampling, evidence, consent, uncertainty, and interpretation boundaries.
---

# Customer Research & Surveys

## Reuse Growee Context

At the start, read `.agents/growee-context.md` when it exists. Reuse only product, customer, market, outcome, constraint, evidence, and routing fields whose scope, definition, source, and date remain compatible; state what is reused and surface conflicts or staleness before asking for decision-changing gaps. The file grants no system access or execution authority, and this Skill must not silently rewrite the primary diagnosis.

## Integrated Capabilities

This Skill consolidates adjacent workflows behind one trigger. Use the main workflow for core requests. When a request matches a module below, read that module before executing it:

- [Survey Design & Analysis](references/modules/survey-design-and-analysis/SKILL.md)

Turn a decision-relevant customer question into a responsible research plan, attributable evidence, bounded synthesis, and actionable learning. Work from public artifacts, supplied research, or approved private inputs. Missing interviews, transcripts, analytics, or customer access are `unavailable`, never a reason to fabricate quotes, motives, prevalence, or certainty.

Read [research-contract.md](references/research-contract.md) for intake, evidence, consent, privacy, and output requirements. Read [methods-and-sampling.md](references/methods-and-sampling.md) before choosing participants, interviews, surveys, observation, public review analysis, or mixed methods. Read [synthesis-and-decisions.md](references/synthesis-and-decisions.md) before coding, quoting, forming themes, comparing segments, or recommending decisions. Use [playbook-sources.md](references/playbook-sources.md) to cite the pinned Growth Playbook basis.

## Select One Mode

| Mode | Use |
| --- | --- |
| `plan` | Define the decision, research question, method, sample, recruitment, screener, guide, consent, and analysis plan |
| `synthesis` | Code and synthesize supplied interviews, calls, surveys, reviews, support, win/loss, churn, or observational artifacts |
| `decision` | Translate bounded research findings, counterevidence, and uncertainty into product, growth, marketing, segment, or evidence-acquisition decisions |

Name one primary mode. Keep raw evidence, participant reports, researcher interpretation, and decision recommendation visibly separate.

## Freeze The Research Contract

Record the decision and owner; research question; customer, account, role, market, language, locale, lifecycle state, and unit; inclusion and exclusion rules; known hypotheses and counterhypotheses; method; sample and recruitment frame; incentive; consent and recording status; source artifacts; capture dates; translation; privacy boundary; analysis plan; decision date; and evidence limitations.

Start with the decision, not a generic desire to understand users. Research questions must be answerable by the selected method and capable of changing a named action.

## Protect Evidence Meaning

Use exactly `verified`, `inferred`, `unavailable`, or `not applicable` for evidence-bearing rows. A stakeholder-only summary without inspectable support may use signal status `reported signal` with a blank evidence state.

`verified` can establish that an attributable participant made a statement or an artifact contains text; it does not establish that the statement is objectively true, representative, causal, or prevalent. Preserve exact source IDs, dates, participant criteria, prompts, context, and limitations.

Never invent or improve quotes, participants, motives, jobs, segments, counts, frequencies, saturation, preferences, willingness to pay, causes, or outcomes. Use verbatim quotes only when exact text is supplied. Mark paraphrases as paraphrases and translations as translations.

## Choose Methods For The Question

Use interviews, observation, diary or workflow review, win/loss, churn, support, public review analysis, surveys, behavioral data, or mixed methods according to the decision. Interviews explain experience and mechanisms; surveys can estimate bounded prevalence when the construct, sampling frame, wording, and response process are credible; behavioral and economic evidence test whether reported patterns appear in outcomes.

Sample for decision-relevant variation, not convenience alone. Include successful, failed, churned, non-converting, different-role, and negative cases when they can distinguish hypotheses. Do not turn every difference into a segment; a segment must change a real product, positioning, channel, service, sales, or monetization decision.

## Conduct Without Leading

Ask about concrete past situations, triggers, alternatives, actions, constraints, outcomes, decision criteria, workarounds, and consequences before requesting opinions or solutions. Avoid embedding the desired feature, benefit, cause, or price in the question. Hypothetical intent is not observed behavior.

Separate facilitator notes from participant words. Record interruptions, missing context, recruitment source, incentive, language, translation, and whether another person influenced the response.

## Synthesize With Counterevidence

Create atomic evidence units with source ID, participant or artifact context, exact quote or bounded paraphrase, code, theme, evidence state, and limitation. Show support, contradiction, negative cases, sample coverage, and unresolved alternatives for every major finding.

Do not report a qualitative theme as a population percentage. Report counts only with a clear denominator and sampling boundary. Saturation means new evidence is no longer materially changing the current decision model under the sampled range; it is not universal proof.

## Route Execution

Customer Research owns research design and synthesis, not implementation. Route positioning decisions to an appropriate positioning capability or `growth-diagnosis`, first-value work to `activation`, recurring value to `retention`, commercial research to `monetization`, experiments to `growth-measurement`, copy to `copywriting`, lifecycle messages to `lifecycle-marketing`, and campaign execution to `acquisition-strategy` when available.

## Deliver In Order

Return:

1. mode, decision, owner, and research boundary;
2. research contract and source inventory;
3. sample, recruitment, consent, and privacy plan or record;
4. method, screener, guide, coding, and analysis plan as applicable;
5. evidence ledger with exact attribution;
6. findings, counterevidence, negative cases, and limitations;
7. decision implications and alternatives;
8. next evidence, owner, review date, and handoffs;
9. Playbook references and external-action boundary.

For China work, keep market, language, locale, product surface, identity, channel, platform, recruitment source, consent, recording, incentives, translation, and data conditions separate. Do not infer WeChat, Xiaohongshu, Douyin, app-store, payment, community access, or research permission from market or language.

Planning, synthesis, and decision work authorize local artifacts only. Do not access private communities or accounts, scrape restricted sources, recruit or contact participants, schedule interviews, record sessions, issue incentives, upload private data, change CRM states, publish findings, or send messages without separate task-level authorization and capability review.

## Keep One Output Language

Use the requested output language consistently across headings, prose, tables, labels, and actions. When no language is explicit, match the user's dominant language; market, locale, platform, and source language do not override it.

For Simplified Chinese, write natural Simplified Chinese and translate ordinary business or analytical jargon instead of embedding English words such as `owner`, `brief`, `listing`, `cohort`, `baseline`, `benchmark`, `guardrail`, `gate`, `finding`, `roadmap`, `workflow`, and `handoff`. Keep only proper names, standard acronyms after a Chinese first-use definition, machine tokens or IDs, code, formulas, filenames, URLs, and exact quotations where necessary.

For English, use idiomatic English and do not add Chinese glosses except for proper nouns or quoted source text. Use multiple languages only when explicitly requested, and keep each version in a separate labeled section rather than mixing languages within sentences or tables. Do not alternate languages for emphasis or perceived expertise.

## Completion Gate

Confirm that the decision, unit, population, sample boundary, method, sources, consent, language, translation, evidence states, raw-versus-interpreted distinction, counterevidence, negative cases, counts, and limitations are explicit; quotes are exact and attributable; small or biased samples are not generalized; segments change decisions; privacy is minimized; recommendations do not exceed evidence; Playbook sources are pinned; and no external action occurred.
