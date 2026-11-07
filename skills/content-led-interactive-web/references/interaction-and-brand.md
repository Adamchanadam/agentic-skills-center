# Interaction And Brand Contract

## Two Legitimate Values

Major interaction, motion, and immersive presentation may earn their place through either — or both — of these values:

1. **Meaning value:** It helps the reader understand, compare, explore, decide, navigate, or make progress.
2. **Brand-memory value:** It creates a distinctive, content-grounded impression that helps the reader recognise and remember the brand, worldview, or experience.

Brand-memory value is real value. It is not a loophole for arbitrary spectacle: the intended impression, signature moment, and connection to the design thesis must be named. A claim that readers actually remember it requires reader evidence; without that evidence, call it an intended effect.

## Contract For Each Major Experience Element

Record these fields for the core interaction, secondary mechanism, and signature moment:

| Field | Question |
|---|---|
| Trigger | What does the reader do, scroll to, choose, or encounter? |
| State | What meaningful UI, narrative, data, or spatial state changes? |
| Reader value | Does it create meaning value, brand-memory value, or both? |
| Thesis link | Which claim, tension, or confirmed brand cue does it express? |
| Feedback | How does the reader understand the result or their current place? |
| Fallback | What remains if motion, scripting, graphics acceleration, or the capability is unavailable? |
| Access | How do keyboard, touch, screen-reader, reduced-motion, zoom, and narrow-screen users complete the essential journey? |
| Cost | What are the performance, privacy, network, and maintenance implications? |

## Technology Tiers

Choose the lowest tier that can make the thesis tangible, then add enhancement only where it creates a clear new capability.

| Tier | Appropriate use | Required safeguard |
|---|---|---|
| Stateful web interface | URL/history state, semantic disclosure, comparison, filters, direct manipulation, and native control feedback. | The core task works with ordinary HTML, CSS, JavaScript, and keyboard input. |
| Motion and transition | Real document-state changes, temporal storytelling, focus movement, and deliberate material behavior. | Motion respects `prefers-reduced-motion`; a state change still happens without animation. |
| View Transition API | Preserve object identity across same-document states or same-origin document navigation. | Feature-detect it; navigation and state changes remain intelligible without the transition. |
| CSS scroll-driven animation | Let reader-controlled scroll or element visibility pace a narrative, reveal, material change, or data relationship. | Use `@supports`; scrolling must not be the only way to discover essential content or trigger an action. |
| Canvas / WebGL | Spatial explanation, dense data, responsive art direction, simulation, or a material interaction that text and DOM cannot express as well. | Keep the insight in DOM-accessible language and provide a non-GPU route. |
| OffscreenCanvas / worker rendering | Preserve input and text responsiveness while a generative, particle, data, or material canvas needs sustained work. | Move only measured heavy work off the main thread; retain a low-computation scene or static semantic alternative. |
| WebGPU | Computation or rendering whose scale, material, or simulation genuinely strengthens the reader's understanding or intended brand experience. | Feature-detect it, bound resources, test actual adapters, and ship a capable non-WebGPU experience. |
| WebCodecs | Frame-accurate, hardware-assisted media treatment where a normal video element cannot produce the intended interactive or visual result. | Use only with a codec/support plan and a conventional media or still-image path. |
| AudioWorklet | Reader-initiated reactive or generative sound that changes the experience's meaning or sensory identity. | Never autoplay; offer silence and equivalent visual/state feedback. |
| WebXR | A real physical-space, AR, or VR task where headset/device placement and spatial interaction are themselves the content. | Treat as experimental and hardware-specific; ship a complete 2D experience first. |

The fact that a technology is modern is not sufficient justification. Do not add a 3D canvas, scroll effect, persistence, audio, telemetry, or network request merely to signal sophistication.

For a current, high-impact technology selection, read [the technology-audition guide](technology-audition.md). It requires a deliberate combination and a rejection reason for the ordinary template answer; it does not require every tier.

## Anti-Patterns

- A click, hover, or scroll effect that leaves the reader with no new state, orientation, understanding, or intended sensory impression.
- A generic gradient, glow, card lift, or parallax effect whose removal changes neither the message nor the brand thesis.
- Motion that hides text, traps keyboard focus, starts unexpectedly without a reduction path, or forces performance-heavy graphics on all readers.
- Calling a local state, an animated logo, or a screenshot proof that the public brand effect has been validated.
