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
- Positions lerp at `lerp` (default `0.05`) per frame; never snap. Target vector is reused.
- `blend` mixes hamiltonian ↔ klein when `geometry === "blend"`.
- Chat kernel `update(t)` remains the reference for torus / infinity / hamiltonian / triangular.
- Stage-9: `scherk`, `knot`, `pseudosphere`.
- Stage-10: peer fan-out + GPU attribute buffer.
- Stage-11: GLSL kernel (`evaluateKernel.glsl.js`) for the four chat geometries; packed theta/phi; `cassini`, `lorenz`, `superformula`.
- Stage-12: WebGL2 transform-feedback (`src/transformFeedback.js`) steps those four geometries on GPU. Node cap 16384 via `?tf=1&nodes=16384`.
- Stage-15-partial: TF kernel also steps helix, mobius, lissajous, trefoil, figure8, cassini, clifford, villarceau.

**Next**
- Stage-13: authenticated live `ledger_pulse.py` → Hive WS against live sheet counts.
- Stage-14: memory engrams into Drive `CRYPTIC-HEARTBEAT-NEXUS-ROOT`.
- Stage-15-rest: remaining manifolds on the TF path.
- Stage-16: hamiltoniansingularity.ai public band (`blend` default).

Events on the visualizer window:

- `gaia:targetState` — full contract object
- `gaia:pulse` — `{ pulse }` mapped onto `gravityPull`
- `gaia:positions` — band-192 node stream

Implementation: `machackabook/gaia-visualizer` → `src/geometry.js`, `src/Node.js`, `src/pulse.js`, `src/gpuBuffer.js`, `src/evaluateKernel.glsl.js`, `src/transformFeedback.js`.
Hive emitter: `The-Hive/geometryContract.ts` → `emitGaiaContract`.
Pulse CLI: `notebooks/ledger_pulse.py --http|--ws`.
