# Build & Testing

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
