# Bloom & Boom Status

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

## Historical reference2 checkpoint — 7 October 2026

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

## Identity

**Bloom & Boom** is the official mod and project name. Legacy `creeperella` registry/save identifiers remain for compatibility.

This repository currently documents the project direction. It does not yet contain the recovered development source tree.

## Latest visual and interaction checkpoint - 7 October 2026

Candidate **1.6.0-dev7-polish39-visual1** targets Minecraft 1.20.1 / Forge 47.4.23 / Java 17. It is a development candidate, not a stable release. This dated section supersedes older pending-client/build statements below; older receipts remain historical evidence.

### What changed

- Cinderella, Mariglow, Verdalia, and Nacrella have refreshed 128x64 texture atlases and matching emissive masks.
- The three froglight variants use the shared family body/feet mesh again, replacing the stretched independent shell. Their botanical crowns and themed palettes remain.
- Sparse glow masks have zero RGB outside emissive texels, preventing additive-render washout.
- Cat assets and its animation section remain unchanged. A regression gate checks 25 protected assets and the original Cat animation section.
- Retains inputfix1: empty-handed companion commands run only for the main-hand event; client ownership synchronization fixes owner-sensitive interaction feedback without changing legacy save keys.

### Verified

- Offline Gradle 8.8 build and reobfuscation passed.
- Packaged JAR: **451,653 bytes**, SHA-256 `27bba9f74c2e8140b1559e3f219d1c37ad7999fb99a05274f0c349e687a15cb4`.
- This exact JAR booted a production dedicated server, spawned all ten active family variants, loaded the existing QA companion, saved, and exited cleanly.
- A native development client rendered the four refreshed variants. Actual in-game screenshot pairs were captured; the QA world saved and the client exited with code 0.
- Static checks passed: 134 runtime JSON resources, four UV/glow contracts, protected Cat/assets, main-hand/owner guards, Cat rest reset, and 712 sampled Pie animation formula evaluations. These are not 712 gameplay scenarios.
- Earlier inputfix1 native tests exercised tame/bond progress, Follow/Stay, whistle binding/actions, Cat-to-Cherry transformation, and companion save/reload.

### Remaining gates

- Charged/night/movement visual matrix and broader gameplay, multiplayer, and mod compatibility.
- Complete official Minecraft assets for sound/menu QA; the cloud cache is incomplete. No security checks were disabled and no Minecraft assets are redistributed.
- Recovered-source import into this repository and any public release publication remain open.
- Historical Nacrella hash mismatch and the absent older Cat-pose fixture remain recorded below. New art does not turn old failed checks into passing receipts.

The visual1 development bundle was delivered directly to the owner with source, JAR, checksums, screenshots, and test results. The GitHub repository remains a documentation hub pending source import.

---

## Verified build and server checkpoint - 7 October 2026

This checkpoint supersedes the earlier dependency/build blockers recorded below. The repository remains a documentation hub until the recovered source is imported; no public release is claimed.

- Fresh Java 17 compilation passed, with 26 deprecation warnings and no compiler errors.
- Gradle 8.8 production build passed, including `reobfJar`.
- Produced candidate: **437,280 bytes**, SHA-256 `a95733e903a4afabe94e097c56724b65cb581b2e6138f73fcad41fefe71346df`.
- The packaged metadata now says **Bloom & Boom** and links to this repository. The `creeperella` mod/save identity, dependency ranges, credits and license text are unchanged.
- The exact packaged JAR started on a separate **Forge 47.4.23 / Minecraft 1.20.1 production dedicated server**, not only a development classpath.
- Production-server checks passed: 10/10 active family spawns; legacy Blossom-to-Cherry alias; Cherry Grove spawn weight 18/group 1-2 with no natural Blossom entry; Mushroom Fields Boomshroom weight 10/group 1-2. Biomes were set explicitly in a disposable QA world; this is not a natural-spawn frequency benchmark.
- A named charged Cat persisted across a development-server restart. The production JAR then loaded its saved tame/sit flags, synthetic owner UUID and bond value correctly. This is a focused persistence check, not complete save-migration or player-interaction certification.
- Both development and production servers saved and shut down cleanly. Existing user worlds were not used.

**Still open:** native client rendering/screenshots, interactive companion/whistle/transformation QA, broader save compatibility, source import and release publication. The earlier Nacrella protection-hash discrepancy and missing historical Cat-pose fixture are still unresolved. Network-restricted authentication-key retrieval warnings occurred during server startup; authenticated multiplayer was not tested.

## Evidence Levels

### Accepted lineage

- Creeperella 1.5.0: stable baseline.
- Creeperella 1.6.0-dev6: verified development checkpoint direction.
- Forge 47.4.23 / Minecraft 1.20.1 target.

### Candidate work

- Creeperella 1.6.0-dev7-polish39: recovered development candidate.
- Not a release.
- Not published as a JAR.
- Requires build and native verification before acceptance.

### Experimental work

- ReBloom visual experiments and offline harness improvements remain development work.
- Experimental work does not supersede accepted checkpoints.

## Verified Offline Work

Completed without claiming a Minecraft build:

- resource/source audits
- registry contract harness improvements
- malformed JSON fixture checks
- broken reference fixture checks
- dependency namespace handling tests

## Earlier recovery blockers

An independently inspected dev7 candidate JAR exists (437,288 bytes; SHA-256 `061ff99e83e4ba40782b1c4e3353b03e551b73b58ab1b843b8cfd6d2289d147c`). Archive integrity passed, but its public display metadata still needs correction.

Build success and development-server startup were reported in earlier work; reproduction in the current environment remains pending. Native client work reported a missing Linux LWJGL library (`liblwjgl.so`). Production-JAR gameplay, clean save/reload and genuine in-game screenshots remain unverified.

See [Build & Testing](BUILD-AND-TESTING.md) for evidence levels and the remaining gates.

NBT migration cannot be proven statically.

## Acceptance Gate

Before a release candidate:

1. Restore reproducible Gradle build.
2. Run compile/build tasks.
3. Produce JAR artifact.
4. Run native Minecraft QA.
5. Verify content, registry, and save behavior.
6. Publish only verified artifacts.

## Expanded recovery checks — 6 October 2026

A fresh direct audit of the recovered dev7-polish39 candidate ran 17 existing scripts: 15 passed, one failed, and one could not complete because its historical fixture is missing. Some scripts wrap overlapping checks; these are not 17 independent gameplay tests.

- Passed: exact 45-file source-pack inventory, 48 spawn-egg model states, Cherry standalone assets and legacy Blossom routing, Froglight family/material checks, Boomshroom, Cat source geometry, Pie source fidelity, sampled Pie/Cherry formulas, Cat gait/personality checks, and deterministic model regeneration.
- Failed: Shroomboom protection check expects Nacrella texture SHA-256 `f3c8a72ba144d4fb0ed91f5990944cb0d6473f8450f4c6eb1fe52bc03811c7ae`; recovered source and inspected JAR contain `88801b8ad90f41a2180f1f8033dbafc53b198fda425f1c02d453b6b625a055ad`. This discrepancy predates the direct audit. Preserve both the historical expectation and current texture until provenance/visual acceptance is reconciled.
- Blocked: Cat rest-pose polish test requires absent `pose-history/1.4.17-before/CreeperellaModel.java`. No substitute fixture was fabricated.
- The bundled source checksum list is stale relative to seven of its 264 listed source entries, mainly Nacrella art and two model classes. Do not treat that list as a current acceptance receipt.
- A separate staged resource-graph checker parsed all 134 runtime JSON files and found no missing explicit local model/texture paths. Seven negative/positive fixtures passed, including malformed JSON, duplicate keys and missing references. External Minecraft assets, inherited texture-variable bindings, registries and save migration are outside this checker’s proof.

At the 6 October audit checkpoint, all 267 runtime-source files were byte-identical to the recovered source archive. New checks are staged tooling only; no gameplay code, texture, expected protection hash or accepted release was replaced. Fresh compilation and native Minecraft acceptance are still open.
