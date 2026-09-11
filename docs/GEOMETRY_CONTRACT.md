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
- Stage-47: live chat (2026-09-10 20:13 CDT) reconfirmed session hash `beec41f1`. Living hash `7cd81012`. Klein not in session switch.

**Next** — see `docs/STAGE47.md` and `docs/NEXT_STAGES.md`.

Events on the visualizer window:

- `gaia:targetState` — full contract object
- `gaia:pulse` — `{ pulse }` mapped onto `gravityPull`
- `gaia:positions` — band-192 node stream + compact `kernel` seeds
- `gaia:kernel` — signed contract frame / theta-phi snapshot

Implementation: `machackabook/gaia-visualizer` → `src/chatKernel.js`.
Hive emitter: `The-Hive/geometryContract.ts`.
