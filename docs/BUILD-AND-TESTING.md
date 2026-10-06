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

## Current Build State

Current documentation does not claim a successful build.

Known blocker:

- Gradle wrapper/tool recovery remains incomplete in the available environment.
- Native Minecraft QA is pending a successful build.

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
