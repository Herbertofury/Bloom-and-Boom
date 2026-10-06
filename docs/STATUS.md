# Bloom & Boom Status

## Identity

**Bloom & Boom** is the official mod and project name. Legacy `creeperella` registry/save identifiers remain for compatibility.

This repository currently documents the project direction. It does not yet contain the recovered development source tree.

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

## Current Blockers

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

All 267 runtime-source files remain byte-identical to the recovered source archive. New checks are staged tooling only; no gameplay code, texture, expected protection hash or accepted release was replaced. Fresh compilation and native Minecraft acceptance are still open.
