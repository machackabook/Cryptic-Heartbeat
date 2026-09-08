# Geometry contract (LLM → visualizer)

```json
{
  "geometry": "torus | infinity | hamiltonian | triangular | helix | mobius | lissajous | klein | hopf | rose | seifert | blend | trefoil | stereo | clifford | enneper | gyroid | calabi | figure8 | villarceau | boy | catenoid",
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
- `clifford` is the S3 Clifford torus, stereographically projected to R3.
- Stage-6: `enneper`, `gyroid`, `calabi`, `figure8`.
- Stage-7: `villarceau` (interlocking torus circles), `boy` (RP2 immersion), `catenoid` (catenoid↔helicoid associate family).
- Node scale follows `gravityPull` in the visualizer.
- Chat kernel `update(t)` remains the reference for torus / infinity / hamiltonian / triangular.

Events on the visualizer window:

- `gaia:targetState` — full contract object
- `gaia:pulse` — `{ pulse }` mapped onto `gravityPull`
- `gaia:positions` — band-192 node stream

Implementation: `machackabook/gaia-visualizer` → `src/geometry.js`, `src/Node.js`, `src/pulse.js`.
Hive emitter: `The-Hive/geometryContract.ts` → `emitGaiaContract`.
