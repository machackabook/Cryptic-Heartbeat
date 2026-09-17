# Next stages — Stage 159 (2026-09-17 15:05 CDT)

Session paste hash `beec41f1` reconfirmed (same four-geometry `update(t)`). Living hash `7cd81012`.

## Do not change

- Four-geometry session switch: infinity | hamiltonian | triangular | torus.
- Per-frame lerp `0.05` and reused target vector in living source.
- Theta step `(0.01 + idx * 0.002) * gravityPull`.
- Minor radius `3 + toroidalWeave * 2`.

## Next work

1. Panel emitters: remaining Quine / NexusStudio editors → `emitGeometry` / `emitWeaveChange` / `emitPulse` / `emitLedger`.
2. InstancedMesh + GPU attributes for >1k nodes (gaia-visualizer).
3. Drive engram persist from `/api/gaia/engram` into `CRYPTIC-HEARTBEAT-NEXUS-ROOT`.
4. Remaining ledger-sheet sources behind the live HMAC pulse gate.
5. Promote klein / hopf / figure8 / trefoil into the session switch only after a paste includes those cases.
6. HeartbeatScan authorization on Hive HTTP mutation + WS.
7. Public band default `blend` on hamiltoniansingularity.ai (already wired; keep gated until host cutover).
