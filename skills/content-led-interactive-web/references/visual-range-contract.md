# Visual Range Contract

Use this when a web experience deliberately changes visual phase across its reading journey. It keeps a page from becoming a sequence of unrelated art directions while leaving room for content-led contrast.

## Purpose

A visual mode is a bounded state of the same experience, not a chance to introduce another brand. It may shift lightness, density, accent, composition, or motion to mark a real content change: uncertainty to evidence, archive to interpretation, possibility to decision, or observation to action.

The contract applies after a design thesis has been chosen. It does not choose the thesis, impose a palette, or ban a justified rupture.

## Record The Contract

### 1. Stable Anchors

Name at least three anchors that must survive every mode. Choose the anchors that genuinely express the thesis:

- typographic hierarchy and voice;
- semantic colour roles, such as evidence, action, warning, and connection — not merely a list of swatches;
- material, image, icon, line, or geometric grammar;
- spatial rhythm, density, alignment logic, or border language;
- motion physics, easing character, interaction feedback, and reduced-motion alternative;
- illustration, photography, or generated-asset art direction.

An anchor must be recognisable in the rendered page. “It feels premium” is not an anchor.

### 2. Variation Map

Use a compact table before code.

| Content phase | Reader state | Mode | Allowed change | Anchors retained | Why the boundary belongs |
|---|---|---|---|---|---|
| Entry | orient / feel the promise | `night inquiry` | lower lightness, one active accent, slower atmospheric motion | type, line grammar, material world | the reader is meeting the question |
| Method | classify / compare | `paper relay` | light surface and denser information | type, semantic accents, thread/line grammar | the reader is separating evidence from ideas |
| Exit | commit / act | `signal close` | one high-energy action surface, reduced density | type, cobalt connection cue, motion easing | the reader moves from understanding to a repeatable action |

The labels above are examples, not a preset. A simple experience may have one mode; a typical rich editorial page has no more than three. A mode must name both the content state and the visual treatment.

### 3. Limits

- At one boundary, vary no more than two major dimensions: surface luminosity, active accent, information density, layout tension, or motion tempo. Keep the other dimensions anchored.
- Retain one image/material world. A new image set or rendering treatment needs a stated role in the same world; otherwise it is a new art direction.
- Use one motion grammar: compatible easing, duration family, response-to-input logic, and low-motion behaviour. A chapter may become calmer or denser, but it should not suddenly behave like a different product.
- Let accents keep their semantic job across the page. A colour cannot mean evidence in one chapter and a random decoration in the next.
- Do not use each section to demonstrate a new component trend, display treatment, or typeface. One signature moment earns contrast; surrounding content supplies the quiet needed to notice it.

## Intentional Rupture

Exceed the normal ceiling only when contrast is the actual subject — for example, a before/after comparison, a historical break, a contradictory voice, or a required campaign sequence. Record:

1. the exact reader value of the rupture;
2. the content trigger and the screen where it starts;
3. the anchors that remain legible during it;
4. its accessibility, performance, and maintenance cost; and
5. how the page returns the reader to the primary visual system.

Without all five, collapse the variation back into an existing mode.

## Review Questions

- If the page sections were rearranged, would they still clearly belong to the same experience?
- Does every mode boundary coincide with a shift in reader task, evidence type, or emotional argument?
- Can a reader name the recurring visual grammar without seeing the dossier?
- Has an intensive signature moment been balanced by quieter neighbouring content?
- If a visual change is removed, does the content boundary become less legible? If not, it is probably decorative drift.

## Implementation Hint

Encode the contract in a small set of global semantic tokens. Mark mode boundaries explicitly — for example with a `data-visual-phase` attribute — and override only the documented mode tokens. Do not fork the whole component system or create untracked, per-section colours, fonts, shadows, and animations.
