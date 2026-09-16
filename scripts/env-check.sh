#!/usr/bin/env bash
set -euo pipefail
fail() { echo "ENV-CHECK FAIL: $*"; exit 1; }
[ -f README.md ] || fail "missing README.md"
SHA=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
[ -n "$SHA" ] || fail "empty SHA / point-zero null refused"
echo "ENV-CHECK OK repo=Cryptic-Heartbeat sha=$SHA numeral=137451921129154222 stage=147"
exit 0
