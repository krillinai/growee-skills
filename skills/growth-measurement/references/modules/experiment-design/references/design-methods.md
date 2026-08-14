# Experiment Design Methods

## Choose The Evidence Design

Use a randomized controlled experiment when the intervention is ethical and reversible, assignment and exposure are controllable, the population supports useful sensitivity, outcomes mature in time, and interference is manageable.

Do not experiment with a severe known defect, deceptive or harmful treatment, legally prohibited action, irreversible migration, structurally inadequate population, or intervention whose spillovers invalidate individual comparison. Fix, review, simulate, pilot, or use another evidence design as appropriate.

Alternative designs include qualitative research for mechanisms, offline evaluation for risky systems, bounded pilots for feasibility, switchbacks for time-dependent systems, cluster or geo tests for spillovers, interrupted time series for one-system interventions, difference-in-differences with credible parallel trends, regression discontinuity around a real threshold, and matched comparisons with explicit residual confounding.

## Assignment And Exposure

Choose the unit that matches treatment delivery and interaction: user, account, household, team, seller, buyer, market, geography, inventory unit, or time block. Cluster and switchback designs reduce some interference but lower effective sample size and add correlation, carryover, and time-trend assumptions.

Separate:

- eligibility: who can enter assignment;
- assignment: which condition the unit is allocated to;
- exposure: whether and when the unit can experience the treatment;
- compliance: whether treatment was received as intended;
- analysis: which frozen population and estimator answer the decision.

Use intent-to-treat as the default causal analysis. Exposure or per-protocol analyses may diagnose mechanisms but can be biased when treatment affects exposure or compliance.

## Metrics And Guardrails

Choose one primary decision outcome unless a documented OEC combines measures. Use diagnostics to explain movement, guardrails to detect harm, invariants to detect defects, and long-term outcomes to validate proxies.

Do not use clicks, opens, completion, engagement, revenue, or another convenient proxy without a declared connection to customer and business value. Preserve quality, trust, reliability, support, retention, economics, fairness, and ecosystem guardrails relevant to the intervention.

## Power And Duration

Define the minimum meaningful effect before sample and duration. Require the metric type, baseline rate or variance, alpha, power, allocation, expected exclusions, clustering, repeated looks, and maturation. For cluster designs require cluster count, size distribution, and intracluster correlation or a justified bound.

Traffic divided by a desired duration is not a power calculation. Sample size divided by traffic is not a valid duration until eligibility, ramp, weekly cycles, maturation, delayed events, and attrition are included. Do not invent missing inputs.

## Quality Controls

Before interpretation verify deterministic assignment, variant delivery, event logging, identity, exclusions, data freshness, metric reproduction, invariant behavior, sample-ratio mismatch, and analysis-code version. Use A/A tests or historical checks when they answer a concrete platform-quality question.

Material SRM can arise from assignment defects, selective exposure, missing data, bots, identity errors, delayed events, or treatment-affected exclusions. Resolve or bound it before estimating treatment effects.

## Prelaunch Record

Freeze the contract and version before exposure. Record implementation owners, QA evidence, ramp plan, monitoring, stop conditions, incident path, rollback, and the exact state that will be analyzed. Changes after exposure begin require a timestamped amendment and exploratory label unless prespecified.
