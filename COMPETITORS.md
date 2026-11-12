# Comparable mods and companion-design benchmarks

## Identity

[Bloom & Boom](README.md) is a botanical Creeper project with themed bursts, existing companion interactions and planned ReBloom lifecycle depth. Preserve the Creeperella save/registry lineage and centralized burst architecture. Its private development bundle is not published by this research pass.

| Reference and primary source | Relevant reference scope | Our evaluation goal |
|---|---|---|
| [Creeper Overhaul](https://www.curseforge.com/minecraft/mc-mods/creeper-overhaul) | Author-maintained Creeper-variant project | Compare variant recognizability and environment fit. Bloom & Boom should explain companion state and burst intent beyond appearance alone; that is a target, not proven superiority. |
| [The Aether](https://github.com/The-Aether-Team/The-Aether) | Adventure ecosystem/source reference | Study coherent creature roles in exploration. Evaluate whether botanical variants offer readable, distinct interactions rather than redundant collectible skins. |

## Focused evaluation backlog

- [ ] Variant recognition: identify family, charged state, fuse/burst intent and friendly ownership in daylight, darkness and crowded scenes without relying solely on color.
- [ ] Companion trust: owner/non-owner interactions, both-hand input, transformation, death, unload/reload and multiplayer reconnect retain identity and do not trigger unwanted destructive behavior.
- [ ] Burst clarity and safety: compare every family through the centralized system, including griefing configuration and nearby friendly actors. Retain failures.
- [ ] ReBloom proposal review: lifecycle stages must make the next action clear and preserve existing variants, not erase progress to manufacture novelty.
- [ ] Measure visual fidelity, sound, frame cost and server tick cost separately. A successful offline build or sampled animation formula does not establish in-game polish.

**Priority:** accepted appearance, sound and full gameplay/compatibility tests before adding more families. Existing [status](docs/STATUS.md), [roadmap](docs/ROADMAP.md) and reconstruction evidence remain the source of implementation truth.

## Evidence and maintenance contract

Reviewed 2026-11-12. This is a public-source design comparison, not a hands-on benchmark, exhaustive market ranking, feature acceptance, or permission to copy code/assets. Source pages may describe newer loaders or editions than our target. Recheck exact versions, licenses and integration boundaries before implementation. Preserve approved identity and existing progress; do not replace working systems merely because a competitor exists.

During each daily review, check linked official release notes/issues and update only material changes. Record source date, observation, relevance, proposed experiment and result separately. Retain failed comparisons and the last-good evidence. Community complaints are leads, not established product defects. New speculative features remain proposals until approved. Before claiming improvement, compare the same workload and retain latency/frame-time, memory, correctness and recovery results on the actual project build.

## Review log

- 2026-11-12: initial repository-scoped comparison index; official sources reviewed at documentation level. No gameplay, performance or compatibility tests run in this pass. No implementation or native GitHub Wiki publication claimed.

## Candidate foundations, concrete reuse and shared work

| Candidate | Reuse boundary | Differentiation experiment |
|---|---|---|
| Existing Creeperella lineage and centralized Bloom Burst system | Preserve IDs, companion ownership, saved transformations and existing family behavior. Extend the working burst dispatcher instead of adding per-family parallel implementations. | Run all family/state transitions through one reproducible matrix; compare visual clarity, save continuity and server costs with the last-good candidate. |
| [GeckoLib](https://github.com/bernie-g/geckolib) | Candidate animation controllers, easings and sound/particle keyframes for original assets; first inventory current animation machinery. | One companion idle → fuse → burst → reform prototype, with remote-player synchronization and disabled-effects fallback, before any migration. |
| [Creeper Overhaul](https://www.curseforge.com/minecraft/mc-mods/creeper-overhaul) | Variant identity and biome presentation reference, not a code/art donor. | Evaluate whether a user can distinguish family, ownership and imminent action at gameplay distance without relying on color. |

**License gates:** GeckoLib current [MIT license](https://github.com/bernie-g/geckolib/blob/main/LICENSE) was read at blob `491454db53d5a2166d8a472d07cc8b60e6d016fb`; exact target dependency still needs review. Creeper Overhaul code/asset reuse is **not cleared** by this page. Existing recovered lineage assets retain their own notices and permission requirements; private bundles are not publication-ready merely because a public comparator exists.

### Shared-work proposals

- JetSetCraft/AoA: common original animation-event test vocabulary (pose owner, event identity, timing, reload/reconnect outcome) could reduce repeated mistakes. Do not force every mod onto one animation engine.
- Hearth and Haul: share companion ownership and unload/reload regression scenarios, while keeping living creature state separate from storage capabilities.
- Engineering Atlas: retain visual/performance comparisons and failed evidence; screenshots must identify the precise game/JAR and scene.

- [ ] Establish the current animation and save-state baseline before selecting a new framework.
- [ ] Implement no new family solely to match a competitor; prioritize fidelity and complete companion behavior already promised.

### Reuse admission gates

These are **candidate foundations and experiments**, not selected dependencies or measured improvements. Before reuse: pin the exact version/commit and loader; inspect its source and dependency tree; record code, asset, trademark and redistribution terms separately; keep required notices; verify permission where terms are restrictive or unclear. Public visibility is not a license. A current default-branch license is evidence for that snapshot, not every historical release. Prefer an upstream dependency/API or a small original adapter over a fork when it preserves compatibility. Do not copy proprietary game assets or publish private fixtures.

For every admitted experiment retain baseline and candidate artifacts, representative native workloads, correctness/feature parity, cold/warm latency, p95 frame/tick time, memory, interrupted-save/recovery evidence and rollback. Promote only after the actual target improves without losing requirements. Cross-project sharing below is an interface proposal, not permission to change another project's implementation or declare integration complete.
