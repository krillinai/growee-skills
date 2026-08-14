# Popup Experience And Accessibility

## Surface Selection

| Surface | Use only when | Main risk |
| --- | --- | --- |
| Inline | Content belongs in the page flow | Can be overlooked or disrupt hierarchy |
| Banner or bar | Message is broadly relevant without focus capture | Persistent space and mobile obstruction |
| Contextual prompt | A recent action makes the next step useful | Incorrect state or premature prompting |
| Slide-in | Secondary action can remain nonblocking | Covers controls or distracts from reading |
| Modal | A relevant decision justifies temporary focus | Interruption, accessibility, lost task state |
| Full interstitial | A critical or deliberate gate requires full attention | Severe task blocking and abuse potential |

Prefer the least interruptive surface that can serve the decision.

## State Model

Define:

```text
eligible -> assigned -> trigger condition met -> rendered -> viewable
-> exposed -> interacted, dismissed, expired, or failed
-> form attempted -> validation -> submitted
-> consent recorded where applicable -> destination or fulfillment
-> first value -> repeated value -> suppression or later eligibility
```

Include unsupported, offline, slow, duplicate, already-completed, opted-out, denied, collision, orientation-change, keyboard-only, screen-reader, zoom, error, retry, and stale-state paths.

## Accessibility QA

Verify:

- semantic dialog or appropriate non-dialog structure;
- programmatic name and useful description;
- logical focus entry and visible focus;
- contained focus only when the surface is modal;
- keyboard operation and Escape or documented critical exception;
- clear close control with an adequate target;
- background inertness for modal content;
- focus return to a sensible origin;
- screen-reader announcement without repetition;
- contrast, readable type, zoom, reflow, and no clipped text;
- touch targets, safe areas, keyboard viewport, orientation, and mobile reach;
- reduced motion, pause or stop, no flashing, and no motion-dependent meaning;
- errors linked to fields and preserved input on correction.

Do not use a tiny, low-contrast, delayed, moving, mislabeled, or deceptive close control.

## Content And Form

State one relevant value, supportable claim, proof where needed, transparent action, and honest dismissal. Keep the form to fields needed for the declared value and permission. Explain what happens next. Do not request phone, email, company, role, or other data merely because a platform makes the field available.

Preserve page-to-popup and popup-to-destination continuity. An incentive, discount, deadline, scarcity, customer count, rating, or guarantee requires exact evidence and conditions.

## Performance And Collision

Define payload, script source, load timing, rendering dependency, layout reservation, error fallback, timeout, third-party failure, observability, and removal. Avoid blocking primary content, input delay, cumulative layout shift, repeated network calls, and hydration mismatches.

Maintain a surface-priority registry across consent, service, safety, product, support, lifecycle, survey, marketing, and experimentation messages. One overlay should not hide another required action.
