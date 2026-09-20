#!/usr/bin/env bash
# Continuity env check — no secrets printed.
set -euo pipefail
echo "numeral=137451921129154222"
echo "repo=${GITHUB_REPOSITORY:-local}"
echo "ref=${GITHUB_REF:-unset}"
command -v git >/dev/null && git rev-parse --short HEAD || true
test -d ledger && echo "ledger=ok" || echo "ledger=missing"
exit 0
