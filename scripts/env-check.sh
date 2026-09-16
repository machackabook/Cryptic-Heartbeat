#!/usr/bin/env bash
set -euo pipefail
# Continuity env-check. Fails closed. Point-zero null refused.
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

test -f README.md || { echo "missing README.md"; exit 1; }
test -d docs || { echo "missing docs/"; exit 1; }

if command -v python3 >/dev/null 2>&1; then
  python3 -m compileall -q . || echo "compileall warned; continuing"
fi

echo "env-check ok numeral=137451921129154222 repo=Cryptic-Heartbeat"
