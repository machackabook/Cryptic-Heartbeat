# Security posture — Cryptic-Heartbeat

**Authority:** source code only. Devices are untrusted until verified.
**Numeral:** `137451921129154222`

## Rules

1. Never commit tokens, cookies, Part-15 capture dumps, or voiceprints.
2. `CASCADE_TOKEN` lives only as a GitHub Actions secret with `repo` + `workflow` scope.
3. Ledger stamps are append-only intent; do not rewrite prior generations.
4. Env checks (`scripts/env-check.sh`) must fail closed on missing dirs.
5. Drive is the ethereal continuum. GitHub is the open node. SD / Termux is the developing environment.
6. Waterfall dispatch is best-effort; a failed sibling does not roll back this generation.
7. Catalog the unknown. Do not invent credentials. Do not leak session cookies.

## Verify

```bash
bash scripts/env-check.sh
bash scripts/cascade-mesh.sh
```

© Dual Authority · 2026
