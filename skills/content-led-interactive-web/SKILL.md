---
name: content-led-interactive-web
description: Design and build distinctive, content-led, high-interaction web experiences with an intentional visual-technology audition. Use for a new or substantial website, HTML page, landing page, editorial experience, portfolio, or interactive product surface where reader needs, an original visual direction, brand memory, and meaningful dynamic behavior matter. Do not use for a small bug fix, an isolated component, or a faithful visual clone unless the user also asks to rethink the experience.
---

# Content-Led Interactive Web

Create a website with an authored point of view, not a generic stack of familiar UI components. The job is to help a specific reader understand, feel, explore, decide, or remember something through an accessible, technically appropriate interactive experience.

This Skill distils the project's "HTML 擺脫死板 AI 味" method: begin with the reader's intended outcome, turn style into explicit design choices, compare genuinely different compositions before implementation, then test whether the reading path survives without decorative effects.

## Universal Direction, Not A House Style

This is a design decision system, not a preset aesthetic. For every task, derive the direction afresh from the reader situation, subject material, purpose, explicit style or brand cues, factual constraints, and intended after-feeling. Treat taste as deliberate editorial judgement: make visible trade-offs rather than defaulting to the safest fashionable template.

Never inherit a palette, composition, interaction pattern, or visual metaphor from an earlier result, bundled artifact, or example. A reference implementation can prove that a method is possible, but it cannot establish the next task's style. When the brief gives no style direction, label the resulting thesis as a content-grounded hypothesis and invite only the next material user decision.

## When This Skill Applies

- Apply automatically to requests to design, redesign, or substantially build a web experience where the visual and interactive direction is part of the requested outcome.
- Preserve the user's specified stack, content, brand constraints, privacy boundary, and authorization boundary. Do not make public research, external writes, tracking, deployment, or asset generation implicit unless the request has clearly made original visual production part of the delivered experience.
- A static document can be a valid fallback or an explicitly requested deliverable, but an experience governed by this Skill must not claim to meet a request for high interaction if it has no meaningful client-side state or reader action.

## Start With Evidence, Not a Style Label

Before proposing a layout, inspect the supplied brief, content, existing site, approved assets, and relevant repository conventions. Research facts or public references yourself when they are needed and authorized; do not ask the user for information that is available in the task materials or workspace.

Produce or hold internally a short design dossier. Read [the dossier format](references/design-dossier.md) when a new visual direction, a substantial redesign, or a non-trivial content surface is involved.

Never claim knowledge of a user's personal taste from one article, a generic trend, or a single visual reference. Use confirmed brand material, explicit preferences, and actual content evidence. If those are absent, label the design thesis as a reasoned hypothesis rather than personalisation.

## Bounded Design Frontier

Use the decision-tree and frontier principle adapted from `grill-me` / `grilling`, but do not turn ordinary design work into a relentless interview.

- Facts, content inspection, feasibility, and reference research are the agent's responsibility. Decisions that materially alter the experience remain the user's.
- Identify the currently decidable design frontier. Ask one compact round only when an unresolved decision would materially change the reader outcome, brand impression, content structure, core interaction, or acceptable technical cost.
- Ask the whole current frontier together, at most three questions. Number every question, state its practical consequence, and give a recommended answer. Do not ask questions whose answer depends on another unanswered question.
- If the brief already settles the frontier, proceed. If the user says to decide directly, record the chosen assumption and reason, then proceed. Do not wait for a ceremonial confirmation.
- After an answer, recompute only the next materially relevant frontier. Do not exhaustively traverse every possible branch.

Read [bounded design-frontier guidance](references/decision-frontier.md) whenever user expectations, brand expression, or interaction goals are materially open.

## Establish a Design Thesis Before Code

Translate the dossier into a testable thesis and five design layers: purpose, visual language, structural mechanism, visual tension, and anti-template boundaries. Do not use a wide style label such as "premium" or "futuristic" as a substitute for decisions.

Before writing HTML for a new or substantial experience, propose three directions that differ in reading path, information structure, primary interaction, and technical expression — not merely palette, typography, or decoration. For each, explain the signature moment, which familiar pattern it deliberately avoids, and the most likely way it could fail.

Normally let the user select or refine a direction. If the user has expressly delegated the choice, select the strongest direction against the dossier and state why. For a small, already-directed implementation, do not create artificial alternatives.

## Bound Visual Variation Into One Experience

Originality does not mean that every section receives a different art direction. Before building a substantial page that changes surface, palette, material treatment, layout tempo, or motion character across its journey, write a **Visual Range Contract**. Read [the visual-range-contract guide](references/visual-range-contract.md) whenever the proposed experience has more than one visual phase or the brief asks for a distinctive, experimental, or highly dynamic style.

- Name at least three stable visual anchors — for example type system, semantic colour roles, material or geometric grammar, spatial rhythm, motion physics, border logic, or image treatment. They must stay recognisably present through every phase.
- Map each content chapter to a visual mode, its permitted changes, retained anchors, and the semantic reason for its transition. A mode changes because the reader has crossed a meaningful content state, not because the page needs fresh decoration.
- The normal ceiling is **one to three visual modes**. Within a mode, change no more than two major dimensions at once: surface luminosity, active accent, information density, layout tension, or motion tempo. An intentional rupture can exceed the ceiling only when the dossier names its reader value, content trigger, retained anchors, cost, and recovery path.
- Keep a single typographic system, a bounded semantic palette, a consistent material/image world, and one coherent motion grammar unless the content explicitly makes contrast between systems the point. Do not let a section-level experiment silently become a second brand.
- If a section has no content-grounded reason to shift mode, inherit the previous mode. If a signature element is visually intense, let neighbouring elements become quieter instead of raising the intensity everywhere.

The contract constrains a page **after** its content-led thesis is chosen; it must never turn this Skill into a fixed house style or prevent an explicitly requested, content-justified break.

## Write Public Copy That Carries Its Own Weight

Public-facing website copy must make a reader-specific claim, explain what is true or useful, and give the next relevant attention move without borrowing authority from abstract praise or a cinematic but empty hook. Read [the public-web-copy guide](references/public-web-copy.md) when writing or materially revising visible website copy, headlines, CTAs, captions, feature explanations, or public URL text.

- Use a reversal such as “not A but B” only when its two sides make a material, supportable distinction. A reversal that merely restates the same thought in a more dramatic shape fails the contrast-proof test.
- Do not use a generic atmosphere, evaluation, or promise when a reader would learn more from a concrete subject, mechanism, limitation, evidence, decision, scope, or action.
- Apply the substitution and deletion tests to consequential copy. If it could describe unrelated brands unchanged, or can disappear without losing fact, stance, orientation, or action, rewrite or remove it.
- Preserve approved brand voice, legally required wording, quotations, and valid rhetorical contrast. These rules reduce empty AI-like language; they do not flatten a distinctive human voice into procedural prose.

## Technology Audition For A Distinctive Experience

Choose the visual-technology composition as deliberately as layout and typography. For every substantial experience, identify the subject's visual substrate — for example, spatial evidence, material transformation, time, sound, movement, archive, data, human gesture, or real-world place — before naming a technology.

For a brief that asks for a leading-edge, highly dynamic, immersive, or especially memorable result, run a technology audition before implementation:

1. Check the current platform facts needed for the candidate technologies in official documentation. Never say that a fixed Skill has exhausted the current web; browser capability, support, and the task's constraints must be checked when they matter.
2. Nominate three genuinely different **visual-engine combinations**. Each must name: reader action; changed state; visible effect; technology composition; thesis link; current capability/fallback; and a reason it is specific to this subject.
3. Select or recommend one combination. A finalist normally combines a reader-controlled timing or state layer with a visual/material engine; add sound, spatial hardware, or frame-level media only when that extra modality makes the subject more legible or memorable.
4. Record why the obvious safe answer was rejected. A hero plus feature-card grid, glass panel, generic gradient/glow, cursor effect, decorative particle field, or unmotivated parallax cannot be the experience's design thesis or signature moment.

Do not use a current technology as a badge. WebGPU, WebXR, WebCodecs, audio, 3D, and scroll effects are valid only when their particular capability is the strongest way to express the content; a mature CSS or DOM composition can still be the most sophisticated decision for a particular task. Read [the technology-audition guide](references/technology-audition.md) whenever the requested experience is visually ambitious, uses a non-baseline browser capability, or asks to avoid ordinary template design.

## Plan A Visual-Material Layer

Do not treat raster imagery as a decorative rescue for generic HTML. When an original image, photography-like scene, texture, composite, or transparent object would make the content's material, location, people, process, or brand after-feeling more legible, make it an explicit part of the design thesis.

- Before generating or selecting an asset, run the **Visual-Material Gap Check**: determine whether the reader would lose meaningful understanding, spatial/material presence, or a content-grounded brand impression without it. Keep the work code-native when the answer is no.
- Before accepting a hero-only image plan, create a **Section Asset Coverage Map** for every major content phase: classify it as `raster needed`, `code-native stronger`, or `inherits the established image world`. A single hero is valid only when the dossier explains why every later phase retains enough material and brand-memory value without another asset. This is a coverage judgement, not a numeric quota or a cap on creative range.
- When a page needs visual material, record an asset brief: reader job, thesis link, intended impression, subject and material, composition and copy-safe areas, responsive crop, interaction state, access/fallback path, asset provenance, and maintenance cost. Read [the visual-material guide](references/visual-assets.md) for a site with custom raster assets, an image-led direction, or stateful image treatment.
- Use the runtime's available image-generation capability only when the request authorizes visual asset creation and the chosen image role is concrete. Use supplied/approved references only for their named role; do not send private material elsewhere or imply permission to recreate a real person's likeness, a protected brand asset, or a licensed work.
- Generate or edit a purposeful asset set sized by the coverage map — never a default one-image answer and never a decorative quota. Keep literal copy, unique facts, controls, data, and essential instructions in semantic HTML; an image may carry mood, setting, subject, and material, but it must not become the sole home of meaning.
- Bind a stateful image to a real document state: a crop, reveal, layer, caption, or figure changes because a reader progresses, compares, chooses, or discovers something. A fixed full-bleed image can establish a world, but it is not by itself the requested interaction.
- Persist the final prompt, reference-image role, output path, intended page role, and known limitations alongside the design dossier or asset manifest so a later task can extend the same visual world without guessing.

## Build an Interactive Brand Experience

For a request that calls for high interaction or a non-static website, implement:

- one content-native, stateful core interaction that lets the reader explore, compare, manipulate, reveal, navigate, or make progress;
- a secondary exploration or orientation mechanism when it genuinely improves the journey;
- one deliberate brand-memory moment whose visual, sensory, or spatial impression follows from the content and brand thesis; and
- a semantic, keyboard-operable, low-motion path that retains the page's essential meaning and action.

Read [the interaction and brand contract](references/interaction-and-brand.md) before selecting advanced technology, animation, immersive graphics, persisted state, or a motion system. A dramatic effect may serve brand memory even when it does not alter data, but it still needs a named intended impression, a reason it belongs, and a safe fallback.

Use advanced web capabilities as progressive enhancement. View transitions should enhance a real document-state change; Canvas, WebGL, or WebGPU should make spatial relationships, data, simulation, or material presence more understandable — never act as an unsupported badge of technical sophistication. Feature-detect every non-baseline capability and keep the underlying experience usable without it.

## Verify the Actual Experience

Read [the review rubric](references/review-rubric.md) before claiming a substantive web experience is ready. Browser validation is required for a substantive visual web deliverable unless the runtime genuinely cannot render it; without that render, visual acceptance is unverified. Inspect the real rendered output and operate its meaningful states. For image-led work, verify the actual asset, crop, focal point, state transitions, contrast, load behaviour, and no-image path rather than accepting a prompt or concept image as proof. For a technology-auditioned direction, also verify the selected capability and the stated fallback in the actual target browsers. When a Visual Range Contract applies, inspect transitions at every mode boundary and verify that the declared anchors survive each one. A CSS rule, a static screenshot, or a claim from another agent does not establish interaction or visual acceptance.

### Set A Visual Acceptance Matrix

Before a readiness claim, record the supported viewports and reader-critical states in the design dossier or concise validation evidence. A user-specified device matrix wins. Otherwise test a narrow viewport in the 360–430px range, an intermediate/tablet layout when the page has one, and a standard desktop in the 1200–1440px range. Also test a wide desktop of at least 1600px whenever the composition uses viewport-relative sizing, `clamp()`, absolute layers, transformed graphics, asymmetrical space, a canvas, or a diagram whose proportions could change as it grows.

At every required view, ask whether the intended reading order survives: no readable copy, CTA, control, label, node, or evidence may be obscured by decorative type, a visual layer, or another semantic element. Name explicit copy-safe and interaction-safe zones before implementing an absolute, transformed, or pseudo-element composition. If a map, wheel, timeline, or spatial diagram cannot preserve labels, target size, and order on a narrow viewport, create a content-equivalent alternate composition; uniformly scaling it down, clipping it, or using negative margin is not a responsive fallback.

### Close The Visual Acceptance Loop

An observed acceptance failure is a delivery blocker, not a note to soften in the handoff. Before a ready claim:

1. State the concrete finding and the affected reader state, viewport, visual-mode boundary, asset treatment, or fallback.
2. Make the smallest content-preserving correction that addresses that finding; do not restart the art direction or add unrelated polish.
3. Re-inspect the affected rendered surface and its direct dependencies, including the relevant interaction state and low-motion or narrow-screen path when affected.
4. Use no more than **two focused correction cycles** for the same acceptance pass. If the experience still fails after those cycles, mark it **not ready**, state the remaining limitation and its reader impact, and obtain a user decision before widening the work. The limit prevents aesthetic churn; it never turns a known defect into an acceptable delivery.

Keep concise evidence of the finding, correction, and re-inspection with the deliverable or its design dossier. If browser validation is unavailable, report visual acceptance as unverified rather than inferred from source code.

When revising this Skill, use the [evaluation cases](references/evaluation-cases.md) to verify that the design-frontier guidance asks useful questions without blocking a sufficiently specified task, visual-range constraints preserve a single experience, and public-copy checks remove generic language without banning valid rhetoric.

Keep the outcome honest:

- describe intended brand memory as a hypothesis unless it has been evaluated with real readers;
- state visual, interaction, accessibility, performance, and browser-support gaps separately; and
- do not claim a live public or user-test result from a local prototype.
