#!/usr/bin/env bash
set -euo pipefail
echo "sSoS env check — Cryptic-Heartbeat"
echo "numeral=137451921129154222"
echo "pwd=$(pwd)"
command -v git >/dev/null && git rev-parse --short HEAD || true
for f in README.md SECURITY.md; do
  if [[ -f "$f" ]]; then echo "ok $f"; else echo "missing $f"; fi
done
