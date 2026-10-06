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

## Current Build State — 2026-10-06

A development candidate JAR has been independently downloaded and inspected:

- Size: **437,288 bytes**
- SHA-256: `061ff99e83e4ba40782b1c4e3353b03e551b73b58ab1b843b8cfd6d2289d147c`
- Archive integrity: PASS (336 entries)
- Metadata: legacy display name and old repository URL remain; this is **not the public release**.

A later branding-corrected JAR was reported, but has not been independently inspected in this workspace. Earlier build-work reports describe compilation/reobfuscation success and a development server reaching `Done`. Those reports are not a freshly repeated build or production-JAR acceptance test.

The reported native client blocker is `UnsatisfiedLinkError: Failed to locate library: liblwjgl.so`. Check Linux x86_64 LWJGL native classifiers and the matching runtime before retrying. A working Xvfb display alone does not resolve mismatched native libraries.

The current direct-work environment still needs the exact source/toolchain and dependencies restored. Keep these stages separate: artifact inspection, reproducible build, development launch, production-JAR launch, gameplay, and save/reload acceptance.

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
