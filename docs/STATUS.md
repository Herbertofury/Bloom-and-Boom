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
