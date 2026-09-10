#!/usr/bin/env bash
# Cryptic-Heartbeat env check — fail closed
set -euo pipefail
NUMERAL="137451921129154222"
echo "[env-check] numeral=$NUMERAL surface=Cryptic-Heartbeat"
need_cmds=(git bash date sha256sum)
for c in "${need_cmds[@]}"; do
  command -v "$c" >/dev/null || { echo "MISSING cmd: $c"; exit 1; }
done
mkdir -p docs scripts notebooks
[ -f README.md ] || { echo "MISSING README.md"; exit 1; }
echo "[env-check] ok utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit 0
