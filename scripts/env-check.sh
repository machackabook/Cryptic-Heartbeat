#!/usr/bin/env bash
set -euo pipefail
fail() { echo "ENV-CHECK FAIL: $1" >&2; exit 1; }
[ -f README.md ] || fail "missing README.md"
[ -s README.md ] || fail "empty README.md"
sha=$(git rev-parse HEAD 2>/dev/null || true)
[ -n "${sha}" ] || fail "empty SHA"
echo "ENV-CHECK OK sha=${sha} repo=Cryptic-Heartbeat numeral=137451921129154222"
