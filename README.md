# 🌸 Bloom & Boom

A botanical Minecraft Forge project where Creepers become living floral variants with themed identities, Bloom Bursts, and a long-term ReBloom lifecycle vision.

> Actual in-game screenshots will be used for project artwork once native runtime captures are available. No illustrated placeholder banner is used.

## 🌱 Project Identity

**Bloom & Boom** is the official project and display name.

Legacy internal registry/save identifiers remain preserved unless a tested migration is explicitly required.

This repository is currently a documentation and project hub. It does **not yet contain the recovered development source tree**, and it does **not publish releases from unbuilt experiments**.

---

## ✨ Features & Design Goals

Existing Creeperella lineage features include:

- 🌺 Floral Creeper variants with unique identities
- 💥 Themed Bloom Burst architecture
- 💣 Demolition Buddies
- 🍬 Treat interactions
- 🎵 Fuse Whistle behavior
- 🔄 Reusable blasts and reform systems
- 💾 Transform and save-state preservation

Future ReBloom extensions:

- lifecycle progression systems
- deeper companion mechanics
- additional variant evolution paths

The approved design direction keeps a centralized themed burst system instead of creating disconnected explosion implementations.

---

## 📊 Current Status

| Area | Status |
| --- | --- |
| Project | Bloom & Boom |
| Minecraft target | 1.20.1 |
| Forge target | 47.4.23 |
| Stable lineage | Creeperella 1.5.0 |
| Verified development lineage | Creeperella 1.6.0-dev6+ |
| dev7-polish39 candidate | Recovered development candidate, not published release |
| Build status | Awaiting recovered native build workflow/toolchain |
| Native Minecraft QA | Pending dev7 validation |

---

## 🧪 Verification Status

Completed offline work:

- source and resource audits
- registry contract regression harness work
- malformed resource and broken-reference fixture testing

Verified historical native work exists for earlier accepted checkpoints.

Not claimed for current dev7 candidate:

- successful Forge build
- generated release JAR
- native client/server validation
- save migration verification

NBT migration compatibility cannot be proven statically and requires runtime testing.

---

## 🛠 Building

A reproducible Forge development environment is required.

Typical command once dependencies and Gradle tooling are available:

```bash
gradle --offline --no-daemon clean build
```

Offline builds require prepopulated Gradle/Minecraft dependencies.

---

## 📚 Documentation

- [Project Status](docs/STATUS.md)
- [Roadmap](docs/ROADMAP.md)
- [Build & Testing](docs/BUILD-AND-TESTING.md)

---

## 🗺 Roadmap

### Current priorities

- [ ] Restore complete reproducible build workflow
- [ ] Validate dev7 candidate through real Forge build
- [ ] Complete ReBloom lifecycle implementation
- [ ] Expand Shroomboom/Froglight family systems
- [ ] Add Cow Creeper variant
- [ ] Establish release verification pipeline

### Completed direction

- [x] Bloom & Boom identity established
- [x] Creeperella variant roadmap created
- [x] Centralized Bloom Burst direction defined

---

## 🤝 Contributions

Please preserve:

- Bloom & Boom identity
- existing registry/save compatibility
- existing variant behavior
- visual consistency

Changes should include evidence of testing where possible.
