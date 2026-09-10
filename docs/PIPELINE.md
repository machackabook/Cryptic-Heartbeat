# PIPELINE

Hourly cron `23 * * * *` on Cryptic-Heartbeat is the heartbeat.

```
pull(heartbeat) → stamp(ledger) → dispatch(siblings) → enhance(next repo)
```

When `CASCADE_TOKEN` (classic PAT with `repo` scope) is set as a repository secret, a stamp fans `repository_dispatch` `continuity-cascade` to:

- The-Hive
- nexus-repo-sync
- gaia-visualizer

Drive folder `CRYPTIC-HEARTBEAT-NEXUS-ROOT` is the ethereal continuum house.
Device SD / Termux remains the developing environment.

Team enhance moves to the next repo after each successful stamp.
Meta advances the version line.
Equalizer formats.

Point-zero null returns are refused.
