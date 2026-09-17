#!/usr/bin/env bash
set -euo pipefail
echo "[sSoS] env-check Cryptic-Heartbeat"
echo "numeral=137451921129154222"
test -f README.md && test -f SECURITY.md
echo "ok"
