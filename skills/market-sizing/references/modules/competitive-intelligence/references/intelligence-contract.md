# Intelligence Contract

Use this contract before collecting or comparing evidence. Split the contract whenever one row cannot describe the products, customers, situations, markets, or dates being compared.

## Decision Boundary

| Field | Required definition |
| --- | --- |
| Decision | The choice this intelligence may inform and choices it cannot make |
| Owner | Accountable role, reviewers, and decision date |
| Product unit | Company, product, edition, module, service, bundle, platform, and version |
| Customer unit | User, buyer, payer, administrator, account, beneficiary, and buying group |
| Buying situation | Job, trigger, current workflow, urgency, criteria, and switching state |
| Market | Country or region, language, locale, category, segment, channel, and route to market |
| Alternative boundary | Included, excluded, emerging, disputed, and unknown alternatives with reasons |
| Time | Evidence cutoff, observation window, freshness rule, review date, and horizon |
| Action | Analysis allowed now and separately authorized external actions |

## Alternative Taxonomy

Map alternatives by the same customer job, not by visual product similarity:

| Type | Examples | Boundary question |
| --- | --- | --- |
| Direct | Products positioned for the same job and buying situation | Does the same buyer evaluate them together? |
| Adjacent | Products solving part of the job or entering from another workflow | Under which use case can they substitute? |
| General tool | Horizontal tools configurable for the job | What setup or expertise closes the gap? |
| Internal build | Existing or proposed in-house software or workflow | What build, maintenance, risk, and opportunity cost apply? |
| Manual | Spreadsheets, documents, messaging, labor, or fragmented tools | What pain makes change worth the switching cost? |
| Service | Agency, consultant, managed service, or outsourcing | Is the customer buying an outcome rather than software? |
| Partner | Bundled, channel, integration, or ecosystem solution | Which commercial and access conditions change choice? |
| Inaction | Delay, tolerate the problem, or do nothing | Why is no change currently rational? |

Preserve emerging and unknown alternatives. An excluded alternative needs a decision-relevant reason, not a preferred narrative.

## Evidence Ledger

Every evidence-bearing row includes:

- claim or observation in exact bounded language;
- entity, product, edition, capability or offer, customer, market, and version;
- publisher and source type;
- artifact ID or URL, capture date, publication date, and effective date where known;
- method, population, sample, and denominator where relevant;
- evidence state, freshness, confidence, limitation, contradiction, and next verification;
- privacy, rights, access, owner, and requested action.

Use only:

- `verified`: directly inspectable evidence supports the bounded claim;
- `inferred`: evidence supports a stated interpretation but not direct verification;
- `unavailable`: required evidence is missing, inaccessible, stale beyond use, or not supplied;
- `not applicable`: the field cannot apply to the declared unit and reason.

`Reported signal` identifies an attributable statement with no inspectable support. It is not a fifth evidence state. `Unknown`, blank, zero, and `false` cannot substitute for unavailable.

## Evidence Separation

Keep these layers distinct:

```text
vendor or stakeholder claim
-> documented capability or offer
-> observed availability or experience
-> customer-reported experience
-> verified behavior or outcome
-> causal effect
-> decision implication
```

Evidence at one layer does not prove a later layer. A public customer logo does not prove current use, realized value, contract size, retention, or endorsement. A review does not establish prevalence. A patent, job post, or partnership does not establish a roadmap. A missing page does not establish absence.

## Compatibility Gate

Before comparing, align or explicitly preserve differences in customer and buying units, job, segment, product and offer version, market, language, channel, platform, date, capability state, plan and entitlement, price unit, currency, tax, commitment, source type, method, sample, and evidence maturity.

If incompatibility would change the decision, split the comparison or mark it unavailable. Do not average away incompatible definitions.
