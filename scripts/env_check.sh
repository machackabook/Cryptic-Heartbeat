#!/usr/bin/env bash
# Cryptic-Heartbeat env check — no secrets printed.
set -euo pipefail
echo "Cryptic-Heartbeat env check"
echo "numeral=137451921129154222"
echo "cwd=$(pwd)"
echo "date_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
command -v python3 >/dev/null && python3 --version || echo "python3: missing"
command -v git >/dev/null && git --version || echo "git: missing"
test -d .github/workflows && echo "workflows: present" || echo "workflows: missing"
test -f README.md && echo "readme: present" || echo "readme: missing"
echo "status=ok"
exit 0
