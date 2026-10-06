# Bloom & Boom Status

## Identity

Bloom & Boom is the public documentation home for Creeperella, a botanical Minecraft Forge 1.20.1 project.

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

Build verification is pending because the current environment lacks a working Gradle launcher/wrapper recovery path.

Native Minecraft client testing has not been claimed until a successful build exists.

NBT migration cannot be proven statically.

## Acceptance Gate

Before a release candidate:

1. Restore reproducible Gradle build.
2. Run compile/build tasks.
3. Produce JAR artifact.
4. Run native Minecraft QA.
5. Verify content, registry, and save behavior.
6. Publish only verified artifacts.
