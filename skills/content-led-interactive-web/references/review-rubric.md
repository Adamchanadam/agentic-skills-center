# Review Rubric

Use this after a substantial implementation and before a readiness claim. It is a falsification guide, not a scorecard that can prove taste automatically.

## 1. Thesis And Reader Path

- Can the first view make the reader's situation and next useful attention move clear?
- Does the hierarchy give the central claim, evidence, and action deliberately different weight?
- If colour, animation, icons, and decorative imagery are removed, does the reading path still make sense?

## 2. Originality Through Decisions

- Can the design thesis explain the composition, material language, asymmetry, and anti-template choices?
- Would swapping in unrelated SaaS, portfolio, or research content leave the same page mostly unchanged? If yes, the structure may still be generic.
- Are repeated cards, familiar hero grids, glass effects, gradients, or motion present because the content demands them rather than as the default answer?

## 3. Visual Range Integrity

- If the sections were reordered, would they still visibly belong to one experience rather than several unrelated art directions?
- Does every change of surface, palette, material behaviour, density, layout tension, or motion tempo align with a documented reader/content phase?
- Do the declared anchors — type, semantic colour roles, material or geometric grammar, spatial rhythm, motion physics, or image treatment — visibly survive every mode boundary?
- Is the page within its declared one-to-three mode ceiling? If not, does the intentional-rupture record name reader value, trigger, anchors, cost, and recovery?
- Has any intense signature moment been balanced by quieter surrounding material, rather than making every chapter compete at maximum volume?

## 4. Interaction And Brand Memory

- Does the core interaction produce a meaningful state change and explain its result?
- Does every major brand-memory effect have a named intended impression and thesis link?
- Is the signature moment specific enough that it could become recognisable, rather than simply more intense than the rest of the page?
- Is actual reader recall clearly separated from an untested design hypothesis?

## 5. Visual Material

- If raster imagery is used, can its asset brief explain why HTML/CSS alone was insufficient and why this image belongs to the content?
- Does a Section Asset Coverage Map explain each major phase as `raster needed`, `code-native stronger`, or deliberately inheriting an earlier material world? A hero-only image must be a recorded choice, not an unexamined default.
- Does the actual image preserve the promised subject, material, composition, focal/copy-safe space, and avoid constraints?
- Does every stateful crop, reveal, or image swap correspond to a reader state that remains legible without motion?
- Are literal text, unique facts, data, and essential instructions still in the DOM rather than trapped inside a bitmap?

## 6. Technology Audition And Distinction

- For a visually ambitious brief, are there three materially different visual-engine combinations with an explicit selected/rejected rationale, rather than three decorative variations?
- Does the selected composition turn a subject-specific substrate — material, place, time, evidence, gesture, sound, or spatial relation — into something the reader can perceive or manipulate?
- Is the signature moment structurally different from a hero-card-grid, glass panel, generic glow, decorative particle field, cursor trick, or parallax default? If it resembles one, is there a documented content reason?
- Were support claims checked in current official platform documentation, and were feature detection, resource limits, and the fallback exercised in the actual build?

## 7. Usability And Resilience

- Can essential content and actions be reached by keyboard, touch, zoom, narrow screens, and reduced-motion preferences?
- Do advanced visuals have feature detection and a non-blocking fallback?
- Are text contrast, visible focus, semantic naming, load cost, and input latency appropriate to the task?

## 8. Visual Collision And Proportion

- At every required viewport, can each readable heading, paragraph, CTA, control, node label, evidence label, and caption occupy a clear visual space without overlapping a decorative word, image, node, or another semantic element?
- Do absolute layers, pseudo-elements, transforms, clipping, negative margins, and responsive scaling preserve the declared copy-safe and interaction-safe zones in the rendered page, rather than only in source intent?
- As the viewport changes, do the intended relationships keep their hierarchy — for example diagram to labels, headline to evidence, control to result, and image to copy — rather than making one layer visually dominate or shrink into noise?
- When a wheel, map, timeline, or spatial diagram becomes too dense, does the narrow view use its recorded alternate composition instead of merely shrinking, clipping, or overlapping the desktop version?

## 9. Evidence

- Inspect the real rendered surface at the relevant breakpoints and operate the primary states.
- Inspect every declared visual-mode boundary in the rendered page; do not accept a token table as proof that the range is coherent.
- For image-led work, inspect the delivered asset file as well as the integrated rendered crop, mobile treatment, fallback state, and actual load behaviour.
- Check that requested effects exist in the actual DOM/CSS/JavaScript and browser behavior, not only in a handoff message or code intention.
- For every review-triggered correction, retain the initial finding, the narrowly changed scope, and the re-inspection result.
- Retain rendered evidence for every viewport in the Visual Acceptance Matrix, including the widest required view. A single attractive desktop screenshot cannot represent responsive acceptance.
- Report visual acceptance, interaction acceptance, accessibility evidence, performance evidence, and public/user-test evidence separately. Do not let a passing local screenshot stand in for live deployment or reader validation.

## 10. Acceptance Remediation Loop

- A failed question in this rubric is an acceptance issue. Do not relabel it as an aesthetic preference merely to ship the page.
- Name the reader-facing symptom and its affected state before changing code: for example, an obscured action on a narrow screen, a mode transition that breaks the visual anchors, an unreadable crop, a disorienting animation, or an unusable fallback.
- Correct the cause with the smallest relevant change. Preserve the approved content, thesis, and declared visual range unless the finding proves one of those decisions is itself the cause.
- Re-check the affected state and direct dependencies after each correction. Run at most two focused correction cycles for one readiness pass; do not keep adding decorative tweaks after the original issue is resolved.
- If an issue remains after the second cycle, or the required rendered validation cannot be performed, the outcome is **not ready** or **visual acceptance unverified**. State the limitation, reader impact, and the user decision needed; never use a readiness claim to conceal it.
