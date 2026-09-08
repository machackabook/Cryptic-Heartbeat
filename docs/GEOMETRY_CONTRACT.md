# Geometry contract (LLM → visualizer)

```json
{
  "geometry": "torus | infinity | hamiltonian | triangular",
  "gravityPull": 1.0,
  "toroidalWeave": 1.0
}
```

- `geometry` is assigned by the LLM (`targetState.geometry`).
- `gravityPull` scales angular velocity: `theta += (0.01 + idx * 0.002) * gravityPull`.
- `toroidalWeave` scales the minor radius: `minor = 3 + toroidalWeave * 2`.
- Positions are never snapped; they lerp at `0.05` per frame.

Implementation: `machackabook/gaia-visualizer` → `src/geometry.js`, `src/Node.js`.
