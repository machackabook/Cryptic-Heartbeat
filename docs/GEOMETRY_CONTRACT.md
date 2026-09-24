# Geometry contract (LLM → visualizer)

```json
{
  "geometry": "torus | infinity | hamiltonian | triangular | helix | mobius | lissajous | klein | hopf | rose | seifert | blend | trefoil | stereo | clifford | enneper | gyroid | calabi | figure8 | villarceau | boy | catenoid | dini | roman | hyperbolic | scherk | knot | pseudosphere | cassini | lorenz | superformula",
  "gravityPull": 1.0,
  "toroidalWeave": 1.0,
  "lerp": 0.05,
  "blend": 0.5,
  "token": "optional-shared-gate"
}
```

- `geometry` is assigned by the LLM (`targetState.geometry`).
- `gravityPull` scales angular velocity: `theta += (0.01 + idx * 0.002) * gravityPull`.
- `toroidalWeave` scales the minor radius: `minor = 3 + toroidalWeave * 2`.
- Positions lerp at `lerp` (default `0.05`) per frame; never snap. Target vector is reused in the living source.
- `blend` mixes hamiltonian ↔ klein when `geometry === "blend"`.
- Chat kernel `update(t)` remains the reference for torus / infinity / hamiltonian / triangular.
- Stage-263: live chat (2026-09-23 20:17 CDT) reconfirmed session hash `beec41f1`. Living hash `7cd81012`. Klein / hopf / figure8 / trefoil not in session switch. CPU evaluate covers those extras (GPU ids 12 / 13 / 8 / 7). Visualizer auto GPU/TF at `nodes > 1024`. instanceOffset band `4096–16384` (`NODE_CAP`).

**Next** — keep session pin; wire ledger pulse (13), Drive engrams (14), public band (16), remaining panels (19), skip CPU instance matrices at 4k–16k (51-impl), HeartbeatScan (4-gov). Promote extras only after they appear in a chat paste.

Events on the visualizer window:

- `gaia:targetState` — full contract object
- `gaia:pulse` — `{ pulse }` mapped onto `gravityPull`
- `gaia:positions` — band-192 node stream + compact `kernel` seeds
- `gaia:kernel` — signed contract frame / theta-phi snapshot

Implementation: `machackabook/gaia-visualizer` → `src/chatKernel.js`.
Hive emitter: `The-Hive/geometryContract.ts`.
