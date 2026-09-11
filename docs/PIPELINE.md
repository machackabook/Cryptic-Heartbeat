# Cascade Pipeline — Speedway

Hourly cron + pull-triggered waterfall.

## Triggers
- `schedule` cron on each repo (staggered minutes so they do not collide)
- `repository_dispatch` type `continuity-cascade` from sibling hop
- manual `workflow_dispatch`

## Env checks (device + Drive mesh)
1. Confirm `.github/workflows` present
2. Confirm `docs/` writable for stamp only (no secrets)
3. Confirm `scripts/env-check.sh` is executable in clones
4. Drive folder `CRYPTIC-HEARTBEAT-NEXUS-ROOT` is the ethereal continuum (manual / rclone / Drive connector — never embed tokens)

## Pull → push waterfall
A successful pull / hourly run stamps this repo then (when `CASCADE_TOKEN` exists as an Actions secret) dispatches the next hop.
Token never enters the tree.

## Quality bar (equalizer)
- README states numeral, hop, cascade files
- SECURITY.md present
- No credentials in tracked files
- Ledger append-only
