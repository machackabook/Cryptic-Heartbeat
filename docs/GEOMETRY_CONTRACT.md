# Geometry contract (LLM → visualizer)

```json
{
  "geometry": "torus | infinity | hamiltonian | triangular | helix | mobius",
  "gravityPull": 1.0,
  "toroidalWeave": 1.0,
  "lerp": 0.05
}
```

- `geometry` is assigned by the LLM (`targetState.geometry`).
- `gravityPull` scales angular velocity: `theta += (0.01 + idx * 0.002) * gravityPull`.
- `toroidalWeave` scales the minor radius: `minor = 3 + toroidalWeave * 2`.
- Positions lerp at `lerp` (default `0.05`) per frame; never snap.

Events on the visualizer window:

- `gaia:targetState` — full contract object
- `gaia:pulse` — `{ pulse }` mapped onto `gravityPull`

Implementation: `machackabook/gaia-visualizer` → `src/geometry.js`, `src/Node.js`, `src/pulse.js`.
Hive emitter: `The-Hive/geometryContract.ts` → `emitGaiaContract`.
