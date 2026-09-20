# Team Enhance Pipeline — Cryptic-Heartbeat

Numeral origin: `137451921129154222`
Operating layer: Continuity Engine / sSoS

## What this repo now does on schedule

GitHub Actions workflow `.github/workflows/continuity-hourly.yml`:

- cron `0 * * * *` (hourly, GitHub may jitter)
- also `workflow_dispatch`
- writes an append-only stamp into `ledger/hourly-stamp.md`
- never deletes prior stamps

## Waterfall rule

A pull on this repo should trigger a *document* cascade only:
status files, env checks, security notes. It does **not** blindly push live code into sibling repos. Cross-repo writes require a PAT stored as `MESH_TOKEN` (not present by default — skeptical of network devices).

## Mesh siblings

- machackabook/gaia-visualizer
- machackabook/The-Hive
- machackabook/ENCLAVE-ADAM-REUNITED

## Local env check

```bash
bash scripts/env_check.sh
```

Google Drive remains the ethereal catalog, not a git remote. Bidirectional folder mesh is a *document* sync, not a force-push of binaries.
