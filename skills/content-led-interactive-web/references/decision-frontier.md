# Bounded Design Frontier

This is a humane adaptation of `grill-me` / `grilling` for web design. Its purpose is to make important expectation and goal choices visible before they become expensive implementation assumptions.

## Build A Small Decision Tree

Start from five potential roots:

1. **Reader win** — what changes for the reader after the visit?
2. **Brand impression** — what should remain in memory, and what should the site never resemble?
3. **Content mediation** — which claim, evidence, sequence, or tension governs the page?
4. **Participation** — what meaningful action or state change makes this an experience rather than a static page?
5. **Practical envelope** — which devices, accessibility preferences, time, performance, stack, and privacy limits govern the solution?

Only create branches when their answer changes a design decision. Treat verified task material as settled. Do not ask the user to rediscover facts that can be inspected or researched safely.

## Ask The Current Frontier, Not Everything

A frontier contains only decisions whose prerequisites are already settled. Ask a round only if proceeding would otherwise require a material, hidden assumption. Keep it to one to three questions.

Use this exact shape when questions are necessary:

```markdown
❓ **Q1 — <decision>**: <why this changes the reader experience; concise choices when useful>

➡️ **建議：<answer>** — <reason grounded in the current content or constraint>.
```

Ask related, independent frontier questions in the same round. Hold a dependent question until its prerequisite is answered. After the user responds, update the small decision tree and either proceed or ask only the newly unblocked material decision.

## When Not To Ask

Proceed without questions when the brief, existing product contract, approved references, or an explicit “you decide” instruction settles the choice. State the decisive evidence or assumption in the design dossier.

Do not ask about implementation mechanisms, file locations, browser facts, or public references that the agent can inspect. Do not force choices when the alternatives would not materially change the outcome. Do not keep questioning after the design thesis and chosen direction are sufficiently determined to build safely.

## Decision Stop

The design frontier is complete when every live branch that materially affects the requested experience is either evidenced, selected by the user, or explicitly delegated. That is a build condition, not an extra approval gate when the user already authorized implementation.
