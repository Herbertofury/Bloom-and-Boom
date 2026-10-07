# Current build and verification

## Latest reference3 checkpoint — 7 October 2026

**Development preview; exact reference-art fidelity and stable-release readiness remain unaccepted.** Source/JAR/QA bundle delivered privately to the owner. Public redistribution and source-tree import await explicit approval.

### Changes and native inspection
- Mariglow, Verdalia and Nacrella now have curved petal normals, fuller roof flowers, twelve articulated chains, detailed Pie-driven jewel eyes and translucent lantern shells.
- Brighter vanilla-derived panel centers and reference-tinted foliage were retested in daylight and at night. No image generation was used. The requested Pie chest/rig remains intact; Cat assets and animation remain protected.
- Rear inspection prompted three extra roof blossoms. Actual final F2 captures cover the three variants, a rear view, night and charged state; the test world saved and the client exited zero.

### Verified checkpoint
- Java 17 / Gradle 8.8 offline build and reobfuscation: PASS, Minecraft 1.20.1 / Forge 47.4.23.
- Exact JAR: **534,413 bytes**, SHA256 `497dacf8d9db64850b75fb111c362664107d85670a57df041962f631d257b1a2`.
- Exact packaged JAR: dedicated-server startup, ten-family spawn, saved companion loading, world save and exit zero all PASS.
- Eight focused static suites PASS: 25 protected assets, unchanged Cat animation, 712 Pie formula samples, reference eyes/materials, resource graph, companion guards, Cat rest reset and reproducible material finishing.
- All 27 packaged Froglight material PNGs match source; twelve final textures reproduce byte-for-byte from hash-pinned inputs.
- Private bundle: **8,404,572 bytes**, SHA256 `8e5904434c9c1a431415518b909a2cbf293a509eaae824f18244225d0f767bbb`.

### Still open
Denser reference-like flower/foliage shapes, facial proportions and finer details need art acceptance. Existing ambient particles, especially Verdalia's happy-villager particles, differ from the concept sparkle style. Production-client, full gameplay, broader save compatibility, multiplayer and performance acceptance remain open. Official vanilla assets are incomplete in cloud QA; no sound/panorama or FPS claim is made. The public repository still contains documentation, not the recovered source tree or a release JAR.

Minecraft Dev Kit's reference catalog and authority guide are published, and [Validate Skills #60 passed](https://github.com/Herbertofury/Agent-Foundry/actions/runs/37574846858). Catalog/build success does not substitute for visual acceptance.

---

## Historical build notes

# Build & Testing

## Latest reference2 checkpoint — 7 October 2026

**Development candidate, not an accepted stable release or exact concept-art match.** The official name is Bloom & Boom; the internal `creeperella` save identity is preserved.

The source/JAR/QA development bundle was delivered privately to the owner. Public bundle publication is pending explicit approval.

### What changed

- Mariglow, Verdalia and Nacrella follow the approved clean Froglight references. No new AI-generated reference or material images were used for reference2; the earlier visual1 generated-texture pass is not an accepted fidelity target.
- Curved petal surfaces replace rectangular flower petals, with a full-head crown, roof flowers, ten articulated hanging chains and foot flowers.
- Reference eye geometry uses existing Pie blink/gaze channels. Body, chest and animation lineage remain intact.
- Refined body/face materials, shaded soles and tinted lanterns. Charged-state native QA exposed a white overlay hiding the textures; Froglight-only sparse tinted charge masks fix that issue without changing Cat's charge route.
- Original art was reconciled into 62 distinct images / 63 encodings, with approved targets, special states, baseline, inspiration, rejected history and pixel-identical duplicates kept distinct. The owner received a searchable comparison gallery.

### Verified evidence

- Java 17 / Gradle 8.8 build and production reobfuscation passed for Minecraft 1.20.1 / Forge 47.4.23.
- Exact JAR: **486,850 bytes**, SHA256 `37e7c9514d241b83d2f7c9b8439b107fb6d9e68e9e8097a125c0f680c5271565`.
- Exact packaged JAR passed isolated dedicated-server startup, ten-family spawn, saved-companion load, world save and exit-zero checks.
- Real development-client captures cover all three Froglights, Mariglow night, and the charged-overlay repair. The client saved and exited cleanly. These are native captures, not concept art or offline renders.
- Static checks passed for 25 protected assets, unchanged Cat animation, 712 sampled Pie formula evaluations, reference eye-channel reuse, UV/glow contracts, charged-mask coverage and companion input/owner-sync guards. All 21 packaged Froglight material images match the tested source bytes.
- Bundle: **7,293,921 bytes**, SHA256 `a81d55c488ec53f95f733efb967da5aeb497a42a6eae594b7c3a694c76facf83`.

### Remaining gates

Flower volume, face/lash detail and literal reference resemblance remain below the acceptance target. More angles, motion and production-client tests are needed, alongside broader gameplay/save compatibility and authenticated multiplayer. The cloud QA setup has an incomplete official Minecraft asset cache and earlier slow-tick/UI-timeout warnings; sound/panorama coverage and performance claims remain unverified.

The recovered source is available in the development bundle delivered to the owner. Public source publication, a normal browsable source-tree import and stable release publication remain open. Historical sections below describe their original checkpoints only.

Minecraft Dev Kit now has [hash-pinned reference selection and pixel-duplicate checks](https://github.com/Herbertofury/Agent-Foundry/blob/main/skills/minecraft-dev-kit/scripts/reference_catalog.py), with ten focused self-tests and a [reference-authority guide](https://github.com/Herbertofury/Agent-Foundry/blob/main/skills/minecraft-dev-kit/references/reference-exact-reconstruction.md). Catalog/build success does not substitute for visual acceptance.

---

## Requirements

- Java 17
- Minecraft Forge 1.20.1 development environment
- ForgeGradle-compatible Gradle installation
- Prepopulated Gradle/Minecraft dependencies for offline builds

## Build

Typical command:

```bash
gradle --offline --no-daemon clean build
```

Wrapper builds should use:

```bash
./gradlew build
```

when the official wrapper is restored.

## Current Build State — 2026-10-07

As of **7 October 2026**, the exact recovered source/toolchain and cache have been restored, fresh Java compilation and the Gradle production build/reobfuscation passed, and the branding-corrected candidate is **437,280 bytes**, SHA-256 `a95733e903a4afabe94e097c56724b65cb581b2e6138f73fcad41fefe71346df`. The archive passed integrity inspection and contains 76 classes. Display name and project URL are corrected; legacy registry identity, dependency ranges, credits and license are unchanged.

The exact packaged JAR booted in a separate Forge 47.4.23 / Minecraft 1.20.1 production dedicated server. All ten active family spawns, the legacy Blossom-to-Cherry alias and controlled Cherry Grove/Mushroom Fields ecology checks passed. The production server loaded the saved named charged Cat and its tested tame/sit/owner/bond state from the isolated development QA world. Both server runs saved and shut down cleanly. These focused checks do not certify all save migrations or real-player behavior.

The earlier Linux native-library blocker is being addressed with checksum-verified official LWJGL Linux artifacts and a native desktop launch. Client rendering and gameplay are still **not accepted**. Network-restricted authentication-key retrieval warnings occurred during server testing; authenticated multiplayer was not tested.

**Still required:** native client and production-client testing, genuine in-game screenshots, companion/whistle/transformation interactions, broader save compatibility, resolution of the existing Nacrella protection-hash discrepancy and missing historical Cat-pose fixture, recovered-source import and release publication. See [Status](STATUS.md) for the precise evidence boundary. Historical PASS receipts do not establish a fresh dev7 PASS.

See the [build wiki](https://github.com/Herbertofury/Bloom-and-Boom/wiki/Build-and-Testing) for the full native QA protocol.

## Offline Regression Testing

Available offline validation focuses on source-level safety:

- resource checks
- JSON validation
- registry contract checks
- malformed fixture detection
- broken reference detection

## Native QA Gate

A release candidate requires:

1. Build success.
2. JAR generation.
3. Forge client launch.
4. Variant/content verification.
5. Regression testing.
6. Release receipt.

## Honest Status Policy

Documentation distinguishes:

- accepted historical checkpoints
- recovered candidates
- unbuilt experiments
- verified tests
