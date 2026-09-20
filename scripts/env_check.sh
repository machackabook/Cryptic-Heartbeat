#!/usr/bin/env bash
set -euo pipefail
echo "[sSoS] env check $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "numeral=137451921129154222"
command -v git >/dev/null && git --version || echo "git missing"
command -v python3 >/dev/null && python3 --version || echo "python3 missing"
test -d .git && echo "git-dir=ok" || echo "git-dir=absent"
echo "[sSoS] env check complete — catalog only, no trust of foreign devices"
