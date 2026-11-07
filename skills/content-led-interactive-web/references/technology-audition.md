# Technology Audition Guide

Use this reference when a task calls for a frontier, highly dynamic, immersive, visually striking, or explicitly anti-template web experience. It is a selection method, not a catalogue to implement in full.

## Current-Fact Rule

Web capabilities change. Before promising a non-baseline capability, check current official platform documentation and the target browser/device envelope. At the time of this guide's latest review, useful official starting points include:

- [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) for same-document and same-origin cross-document continuity.
- [CSS scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines) for reader-paced visual time without a JavaScript scroll loop.
- [OffscreenCanvas](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas) for moving suitable canvas work off the main thread.
- [WebGPU](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) and current implementation notes from [Chrome for Developers](https://developer.chrome.com/docs/web-platform/webgpu/overview) for high-scale rendering or simulation.
- [WebCodecs](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) for frame-level, hardware-assisted media processing.
- [AudioWorklet](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet) for reader-initiated low-latency sound processing.
- [WebXR](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API) only for a genuine AR/VR spatial task; it remains experimental and is not Baseline.

Do not turn this list into a claim of exhaustive currency. It is a prompt to inspect the actual current platform before committing a technology, asset pipeline, or support promise.

## Start With The Visual Substrate

Name the irreducible thing the reader should perceive or manipulate before selecting a rendering system:

| Substrate | Possible reader experience | Strong candidate families |
| --- | --- | --- |
| Transformation through time | Scrub, scroll, compare, or inhabit a changing state. | View Transitions, scroll-driven CSS, Web Animations API, frame media. |
| Spatial or material relationship | Inspect depth, scale, light, force, simulation, or an object from more than one view. | SVG/DOM first; Canvas/WebGL, WebGPU only when the added depth is material. |
| Dense evidence or living system | Filter, probe, alter parameters, and see consequences. | Semantic interface plus Canvas/WebGL/WebGPU; worker rendering when measurement shows contention. |
| Moving-image craft | Step through, remix, or expose the construction of a filmic sequence. | HTML media first; WebCodecs when per-frame control changes the experience. |
| Sound as meaning | Initiate, mix, or spatially relate sound to a visible state. | Web Audio / AudioWorklet, with silence as a first-class route. |
| Physical place or scale | Position, walk around, or place an object in a real/immersive environment. | WebXR only when a 2D simulation would erase the actual task. |

## Compose, Do Not Stack

For the three candidate directions, propose combinations in this form:

> **Reader action → state/narrative clock → visual/material engine → optional sensory layer → semantic evidence and fallback.**

Examples of composition grammar, not style presets:

- A reader filters a disputed claim → View Transition carries the selected evidence into focus → SVG/DOM evidence expands into a controlled WebGL material field → plain comparison table remains available.
- A reader scrolls an oral history → CSS view timeline reveals its temporal strata → reader starts an AudioWorklet sound layer → transcript and chapter controls remain complete without audio or motion.
- A reader varies a design parameter → direct manipulation changes a simulation → WebGPU renders the high-detail material model on capable hardware → a precomputed 2D result shows the same consequence elsewhere.

Do not add technologies merely because they coexist. Each layer must either create a new reader capability or a named, content-grounded after-feeling that the preceding layer cannot provide.

## Candidate Families And Boundaries

| Family | Choose it when | Reject it when | Required proof |
| --- | --- | --- | --- |
| View Transition API | Identity across selection, editing, comparison, or navigation is central. | The screen swap has no semantic relationship. | Actual supported and unsupported state change. |
| CSS scroll-driven animation | Reader pacing is the story's clock. | Scroll merely makes objects move. | `@supports`, reduced-motion route, and content reachable without exact scroll choreography. |
| Canvas / WebGL / WebGPU | Depth, density, material behavior, simulation, or scale is essential. | A still or DOM composition communicates the point equally well. | Feature detection, performance envelope, focus/input route, non-GPU representation. |
| OffscreenCanvas | Measured canvas work blocks page responsiveness. | It is added speculatively or prevents simple fallbacks. | Worker lifecycle, reduced work path, responsive input under load. |
| WebCodecs | Per-frame control is genuinely part of interaction or visual craft. | A normal media element would produce the same reader result. | Codec/device plan and media/still fallback. |
| AudioWorklet | User-chosen sound changes interpretation or identity. | Audio is atmospheric wallpaper. | Explicit initiation, mute/silence route, visible feedback, no autoplay. |
| WebXR | A headset or physical placement is the subject. | It is merely a more impressive 3D viewer. | Device permissions, 2D completion path, hardware-specific test. |

## Rejection Ledger

Before implementation, write one sentence for each rejected default that would otherwise be tempting:

- Why a hero plus feature-card grid would flatten this subject.
- Why generic glass, glow, gradient, particle field, cursor effect, card lift, or parallax would be an interchangeable decoration here.
- Why the selected combination gives this reader a more particular visual or sensory encounter.

If no credible rejection reason exists, simplify the direction rather than pretending that novelty has been earned.

## Delivery Gate

An ambitious visual composition is ready to implement only when its dossier includes: the selected combination, rejected candidates, official facts checked, feature detection, target support envelope, resource/asset budget, keyboard and reduced-motion route, no-GPU/no-audio/no-XR route as applicable, and a concrete browser test that can falsify the intended effect.
