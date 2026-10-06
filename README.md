# 🌸 Creeperella: Bloom & Boom

![Bloom & Boom botanical pixel artwork](docs/assets/bloom-and-boom-banner.svg)

A botanical Minecraft Forge project where Creepers become living floral variants with themed identities, Bloom Bursts, and a long-term ReBloom lifecycle vision.

## 🌱 Project Identity

**Bloom & Boom** is the public home for **Creeperella**.

This repository is currently a documentation and project hub. It does **not yet contain the recovered development source tree**, and it does **not publish releases from unbuilt experiments**.

---

## ✨ Features & Design Goals

- 🌺 Floral Creeper variants with unique visual identities
- 💥 Themed Bloom Burst architecture
- 🍄 Shroomboom lineage and Froglight-inspired variant direction
- 🌸 ReBloom lifecycle design for future companion and progression systems
- 🎨 Art-first models, textures, materials, and effects

The approved design direction keeps a centralized themed burst system instead of creating disconnected explosion implementations.

---

## 📊 Current Status

| Area | Status |
| --- | --- |
| Project | Creeperella: Bloom & Boom |
| Minecraft target | 1.20.1 |
| Forge target | 47.4.23 |
| Stable lineage | Creeperella 1.5.0 |
| Verified development lineage | Creeperella 1.6.0-dev6+ |
| dev7-polish39 candidate | Recovered development candidate, not published release |
| Build status | Blocked in current environment: Gradle wrapper/executable recovery required |
| Native Minecraft QA | Pending successful build |

---

## 🧪 Verification Status

Completed offline work:

- source and resource audits
- registry contract regression harness work
- malformed resource and broken-reference fixture testing

Not claimed:

- successful Forge build
- generated release JAR
- native client/server validation
- save migration verification

NBT migration compatibility cannot be proven statically and remains runtime-only validation.

---

## 🛠 Building

A reproducible Forge development environment is required.

Typical command once dependencies and Gradle tooling are available:

```bash
gradle --offline --no-daemon clean build
```

Offline builds require prepopulated Gradle/Minecraft dependencies.

Current blocker:
- project wrapper/toolchain recovery is incomplete
- external Gradle recovery was blocked by DNS/network availability in the execution environment

---

## 📚 Documentation

- [Project Status](docs/STATUS.md)
- [Roadmap](docs/ROADMAP.md)
- [Build & Testing](docs/BUILD-AND-TESTING.md)

Wiki mirrors:
- Home
- Status
- Roadmap
- Build and Testing

---

## 🗺 Roadmap

### Current priorities

- [ ] Restore complete reproducible build workflow
- [ ] Validate dev7 candidate through real Forge build
- [ ] Complete ReBloom lifecycle implementation
- [ ] Expand Shroomboom/Froglight family systems
- [ ] Establish release verification pipeline

### Completed direction

- [x] Bloom & Boom identity established
- [x] Creeperella variant roadmap created
- [x] Centralized Bloom Burst direction defined

---

## 🤝 Contributions

Please preserve:

- Creeperella identity
- existing variant compatibility
- save safety
- visual consistency

Changes should include evidence of testing where possible.
