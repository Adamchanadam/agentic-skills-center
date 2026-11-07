# Design Dossier

Use this before proposing a new visual direction or a substantial redesign. It is evidence and a working design brief, not a new product specification.

## 1. Reader And Outcome

- **Reader situation:** Who arrives, what do they know, and what is competing for their attention?
- **Reader exit state:** What should they understand, feel, decide, remember, or be ready to do?
- **Content job:** Is this primarily an explanation, an editorial reading journey, a product decision, a portfolio, an exploration tool, or something else?
- **Journey:** What must appear first, what can be discovered later, and where should the reader intentionally pause or act?

## 2. Content Spine

- **Central claim or promise:** One sentence the page must make credible.
- **Supporting beats:** The evidence, examples, comparison, story, data, or action that earns the claim.
- **Content hierarchy:** What deserves dominance, what belongs at the edge, and what can stay hidden until requested?
- **Accuracy boundary:** Facts that must remain intact, content that may be restructured, and unknowns that need explicit labelling.

## 3. Design Thesis

Write one sentence in this form: “For <reader>, this experience makes <outcome> feel possible by treating <content> as <metaphor or editorial stance>, not as <generic alternative>.”

Then make the five layers concrete:

| Layer | Required decision |
|---|---|
| Purpose | Why this page exists for this reader now. |
| Visual language | Editorial, material, spatial, typographic, or cultural cues that serve the thesis. |
| Structural mechanism | How hierarchy, scrolling, panels, sequence, comparison, or scene changes arrange the content. |
| Visual tension | What stays quiet and what becomes emphatic; where deliberate asymmetry, density, or pause belongs. |
| Anti-template boundary | Familiar structures or effects that would betray the thesis. |

## 4. Visual Range Contract

Use this when the page changes visual phase. Read [the visual-range-contract guide](visual-range-contract.md) before selecting colours or effects section by section.

- **Stable anchors:** Name at least three visible anchors that survive every phase: type, semantic colour roles, material or geometric grammar, spatial rhythm, motion physics, border language, or image treatment.
- **Mode ceiling:** State whether the experience uses one, two, or three modes. More than three requires an intentional-rupture record with reader value, trigger, retained anchors, cost, and return path.
- **Variation map:** For every mode, record content phase, reader state, permitted changes, retained anchors, and why that boundary belongs. A shift needs a content reason, not a need for novelty.
- **Intensity budget:** State the one signature moment that may become intense and how surrounding phases stay quiet enough to make it memorable.
- **Implementation boundary:** Name the global semantic tokens and which mode-scoped tokens may change. Do not allow section-local colours, type systems, image treatments, or motion behaviours outside that map.

## 5. Brand-Memory Hypothesis

Do not write “memorable” by itself. Name the intended after-feeling, the signature moment that may create it, and its evidence.

- **Intended impression:** for example, calm authority, tactile curiosity, precise optimism, or rebellious warmth.
- **Signature moment:** the one reveal, transition, interaction, composition, material behavior, or soundscape that should make the page recognisable.
- **Why it belongs:** how it expresses the central claim, product promise, or confirmed brand material.
- **Evidence level:** confirmed preference, approved reference, content-derived hypothesis, or unverified experiment.

## 6. Visual Acceptance Matrix

Record how the finished composition will be falsified in a real browser. A declared device matrix overrides this default; otherwise cover a narrow 360–430px view, an intermediate/tablet view when the layout changes there, a 1200–1440px desktop, and a 1600px-or-wider desktop whenever viewport-relative sizing, absolute layers, transformed graphics, asymmetry, canvas, or a growing diagram could alter the composition.

- **Reader-critical states:** Name the view, interaction, mode boundary, asset state, low-motion state, or fallback where a reader could lose orientation or action.
- **Copy-safe and interaction-safe zones:** For every absolute, transformed, pseudo-element, or layered composition, name which areas must remain clear for readable copy, controls, evidence, labels, and touch targets. Decorative material cannot enter those areas unless it is intentionally the only content and remains legible.
- **Proportion check:** State which relationship must remain intelligible as space expands or contracts: headline to evidence, diagram to labels, control to outcome, image to copy, or dense information to pause.
- **Narrow-view recomposition:** If a spatial diagram cannot retain label legibility, order, and target size, state the equivalent linear, segmented, expandable, or otherwise re-composed narrow-view path. Scaling the complete diagram is not a plan.
- **Evidence:** List the exact viewports and states to inspect, the expected outcome, and which evidence will show pass, failure, correction, and re-inspection.

## 7. Feasibility And Boundaries

Record the target stack, performance envelope, devices, browser range, accessibility needs, data/privacy restrictions, approved assets, existing design system, and authorization limits. Treat unknown constraints as assumptions, not as permission to add a dependency, telemetry, external service, or generated asset.

## 8. Visual-Material Plan

Use this section only when a raster asset would make a concrete contribution to the thesis. Read [the visual-material guide](visual-assets.md) before creating or selecting custom imagery.

- **Gap:** What material, spatial, human, historical, or sensory information does DOM/CSS alone fail to carry?
- **Asset coverage map:** For every major content phase, classify `raster needed`, `code-native stronger`, or `inherits the established image world`. A hero-only decision must explain every later classification; it is never the unexplained default.
- **Asset set:** Name the smallest adequate set: world-setting anchor, semantic figure, stateful sequence, transparent material fragment, or none.
- **Per-asset brief:** Record its reader/thesis link, intended impression, subject/material, composition and copy-safe space, responsive crop, state binding, fallback, provenance, and maintenance cost.
- **Prompt continuity:** Keep the retained prompt and reference-image role with the output path, so future assets can extend the visual world deliberately.
- **Text boundary:** State which literal text, facts, actions, and data remain exclusively in HTML.

## 9. Technology Audition

Use this for a visually ambitious, highly interactive, immersive, or anti-template task. Read [the technology-audition guide](technology-audition.md) before making the shortlist.

- **Visual substrate:** Which aspect of this subject needs to be felt or manipulated — space, material, time, evidence, sound, gesture, data, archive, or place?
- **Three combinations:** For each candidate, state reader action, state change, visible effect, technology composition, thesis link, support/fallback, estimated cost, and why it could not be swapped unchanged into an unrelated site.
- **Chosen composition:** Name the timing/state layer and visual/material engine; name any intentional audio, media, 3D, device, or spatial layer.
- **Safe-default rejection:** State which familiar template or generic effect was rejected and why it would flatten this subject.
- **Reality check:** Record the official sources checked, target browser/device envelope, feature detection, low-motion/non-GPU path, and any unresolved implementation risk.

## 10. Direction Comparison

For each of the three directions, compare the first view, reading path, information structure, primary interaction, signature moment, technology composition, anti-template decision, fallback, and likely failure. Different colours, a different shader, or a new animation on an otherwise unchanged hero-card-grid layout are not different directions.
