#!/usr/bin/env bash
set -euo pipefail
echo "[heartbeat] numeral=137451921129154222 utc=$(date -u +%FT%TZ)"
for d in docs notebooks scripts .github/workflows; do
  [[ -d "$d" ]] && echo "[ok] $d" || echo "[miss] $d"
done
echo "[heartbeat] catalog unknown. keep ledger full."
