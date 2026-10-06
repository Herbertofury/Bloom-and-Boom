# Bloom & Boom project instructions

## Start here
- Read `docs/STATUS.md`, `docs/ROADMAP.md`, current issues, and the relevant build notes before substantive work. Make one quick to-do check, then implement the requested task; avoid repeated full-backlog scans.
- Keep the user's primary request first. Tackle related authorized to-dos alongside it, avoid collisions with active workers, and mark completion only with acceptance evidence. Canonical rule: https://github.com/Herbertofury/Agent-Foundry/blob/main/PRODUCT_INVARIANTS.md#19-project-to-do-awareness-without-task-drift
- Load only relevant instructions. Chat-facing skills are not agents or permission grants; do not paste the full skill catalog into every task.

## Compatibility and identity
- Official display name: **Bloom & Boom**. Preserve legacy `creeperella` registry, command and save identifiers unless a tested migration is explicitly required.
- Current target: Minecraft 1.20.1, Forge 47.4.23, Java 17. Adopt modern techniques within that compatibility envelope; do not silently upgrade the game's target.
- Preserve existing variants, animations, companion behavior, transformations and save data. Keep original asset credits and licenses.

## Acceptance and publication
- Check what is actually in the repository before running builds; source recovery is still tracked separately from this documentation hub.
- Distinguish static checks, reproducible compilation, development launch, production-JAR runtime, gameplay and save/reload proof. A ZIP or historical receipt is not a fresh runtime PASS.
- Use genuine in-game screenshots for project artwork. Never substitute generated illustrations for native QA evidence.
- Keep source/docs, the live GitHub Wiki and relevant to-do statuses synchronized at coherent checkpoints. Record the actual commit, artifact digest, passed/failed/not-run checks and next blocker.
- Do not modify Enderloom/AoA or another worker's active task as incidental work.
