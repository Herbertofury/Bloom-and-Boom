# Shared guidance now routed through Athena

This scoped transition pins Athena guidance 2.0.1 at `11e212bb88abd7e010c8974f35ec629032a2a843`. The root router changes only its shared-adapter path and canonical invariant URL. The latter is pinned to `0131c820ba311459b6f197965b8cc074512ded1a`, whose canonical policies are unchanged at the installation commit.

All 32 prior non-router tracked files remain byte-for-byte preserved, including the complete legacy `.agents/foundry` snapshots/lock, project-local `bloom-native-fidelity` skill, CLAUDE import, historical build/skill/CI links and assets. No source bundle was unpacked, no Minecraft artifact rebuilt, and no skill installed. Modhunter and other consumers were untouched.

The explicit Athena transition tool reviewed plan digest `074378525a4b7bb11483e54941c34d227def8084502ebb67924f8dfb371c6c97` before writing. All sixteen canonical snapshots and the exact separately reviewed router were verified afterward. Tests retain hashes of the original non-router files and check exact router/pin completeness on Windows and Linux. This proves repository routing and byte preservation, not behavioral superiority or a live coding-agent/gameplay acceptance run.

## Recovery and remaining gates

The isolated PR can be reverted through normal Git recovery; original files and legacy lock remain. Do not delete legacy files to bypass generic Athena adoption's refusal of legacy locks. The explicit transition tool's injected-failure test demonstrates exception rollback only, not crash/power-loss atomicity. Ongoing managed coexistence updates, actual target-agent discovery/behavior, skill packaging/propagation and full source-history retirement remain separate gates. Agent-Foundry is not certified safe to delete.
