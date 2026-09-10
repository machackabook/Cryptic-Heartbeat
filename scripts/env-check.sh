#!/usr/bin/env bash
# Cryptic-Heartbeat env check — developing environment probe
set -euo pipefail
echo "surface=Cryptic-Heartbeat"
echo "numeral=137451921129154222"
echo "utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "pwd=$(pwd)"
echo "git=$(git rev-parse --short HEAD 2>/dev/null || echo none)"
command -v python3 >/dev/null && echo "python3=ok" || echo "python3=missing"
command -v git >/dev/null && echo "git=ok" || echo "git=missing"
test -d docs && echo "docs=ok" || echo "docs=missing"
test -f docs/LEDGER-STAMP.md && echo "ledger=ok" || echo "ledger=missing"
echo "point-zero=refused"
