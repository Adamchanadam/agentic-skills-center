# Visual Material Guide

Use this reference when an original raster image, edited image, image sequence, photographic scene, texture, or transparent object may become part of the experience. Its aim is not to make every website image-led; it is to ensure that imagery strengthens a content-led direction when HTML, CSS, and vector graphics alone cannot carry the required material or emotional information.

## 1. Visual-Material Gap Check

Before producing an asset, answer all four questions:

1. **What cannot ordinary DOM/CSS express well here?** A physical material, an actual place, human scale, a specific object, a historical or cultural cue, or a sensory atmosphere are valid answers. "It needs to feel more premium" is not.
2. **What changes for the reader?** Name understanding value, brand-memory value, or both.
3. **What would fail if the image vanished?** If the answer is only that the page would look less decorated, do not generate it.
4. **What is the smallest asset set that creates the intended world?** Prefer one anchor image, one semantic figure, or a short deliberate state sequence over a gallery of unrelated illustrations.

Keep image generation out of factual charts, literal UI controls, dense labels, unique claims, and core instructional copy unless the image is independently checked and the same information exists in the DOM.

## 1.1 Section Asset Coverage Map

Do not treat a successful hero as proof that the rest of the journey has enough material presence. For each major content phase, record one of these decisions:

| Decision | Use when | What must be recorded |
| --- | --- | --- |
| `raster needed` | A concrete material, spatial, human, historical, or sensory cue makes the chapter's claim more tangible or memorable. | Asset role, copy-safe area, fallback, and whether it responds to a reader state. |
| `code-native stronger` | Precision, interaction, data/state change, comparison, label legibility, or responsive re-composition matter more than material depiction. | Why an image would weaken rather than clarify the chapter. |
| `inherits the established image world` | The preceding material world still carries forward and this chapter would gain nothing specific from another asset. | Which earlier asset/world it inherits and why the transition remains intentional. |

**Hero-Only Raster Is Not A Default.** It is acceptable only when the map records why every later major phase is `code-native stronger` or deliberately inherits the image world. “One image feels cleaner” is not sufficient evidence. Conversely, an image-rich direction has no fixed minimum or maximum count: add only assets whose individual role survives the gap check and whose shared material world remains coherent.

## 2. Asset Brief

For every retained raster asset, record this short contract in the design dossier or an asset manifest:

| Field | Required decision |
| --- | --- |
| Page role | World-setting anchor, semantic figure, stateful scene, material fragment, or another specific role. |
| Reader / thesis link | The reader outcome and central claim the asset makes more tangible. |
| Intended impression | The precise after-feeling or sensory cue; call it a hypothesis unless reader evidence exists. |
| Subject and material | What is visible, including material clues that distinguish it from stock imagery. |
| Composition | Viewpoint, focal area, responsive crop, and the areas reserved for real HTML copy or controls. |
| State binding | Which reader action changes the crop, figure, layer, reveal, caption, or image sequence. |
| Access and fallback | Alt / caption decision, no-image or low-bandwidth route, reduced-motion behaviour, and colour-contrast safeguard. |
| Provenance | Generation/edit prompt, reference-image role, output path, and any right/privacy constraint. |
| Cost and maintenance | Asset count, weight target, resizing needs, and future replacement risk. |

## 3. Produce Without Reverting To Stock Aesthetics

When the current runtime provides an image-generation tool and its use is authorized, use it as a visual-production tool rather than a style adjective machine.

- Write prompts as an art-direction brief: intended page role; scene/backdrop; subject; material; viewpoint and framing; light and mood; HTML copy-safe space; explicit avoid list; and no in-image text unless the text is independently verified.
- Generate a clean first candidate, inspect the actual result, then make one targeted change per iteration. Do not ask a later prompt to re-invent every element at once.
- Use a reference image only with a declared role — palette, medium, material, composition, edit target, or object to preserve. Do not treat a reference as blanket permission to copy its author, person, or brand.
- Retain the selected prompt and final asset path. Do not leave an asset referenced by the project only in a tool cache or conversation image.

## 4. Integrate The Image Into The Page

- A world-setting image may live behind a first view, but give it a deliberate crop and keep all real type and controls in the DOM.
- A semantic image should normally be a `figure` with a meaningful caption and appropriate alt text; a purely atmospheric image may use empty alt text only when adjacent DOM communicates its purpose.
- For stateful treatment, change the image's crop, layer, masking, figure/caption, or selected asset in response to a meaningful reader state. Respect reduced-motion settings and make the state legible without the transition.
- Supply appropriately sized sources and avoid forcing a large desktop image into a narrow viewport. When possible, allow a mobile-specific crop rather than merely shrinking the desktop composition.
- The no-image path must retain the hierarchy, content, and next action. Do not hide an essential comparison, proof, or instruction inside a raster.

## 5. Review Questions

- Does the Section Asset Coverage Map explain why each major phase needs raster, remains code-native, or deliberately inherits a previous image world — rather than quietly defaulting to one hero?
- Does the actual image have the composition, focal space, material specificity, and unwanted-element constraints in the asset brief?
- Is the asset visually part of this content, rather than a replaceable hero image for any other topic?
- Does each state-linked change reveal an actual reader state, rather than replaying a decorative animation?
- Do caption, alt, contrast, keyboard path, reduced-motion mode, narrow viewport, and no-image fallback preserve the essential journey?
- Have the prompt, asset role, and output path been retained, while avoiding a claim that local visual inspection proves reader recall?
