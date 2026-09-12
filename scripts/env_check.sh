#!/usr/bin/env bash
set -euo pipefail
echo "sSoS env check — Cryptic-Heartbeat"
echo "numeral=137451921129154222"
echo "pwd=$(pwd)"
command -v git >/dev/null && git rev-parse --short HEAD || true
missing=0
for f in README.md SECURITY.md docs/WATERFALL-MESH.md docs/ledgers/heartbeat.jsonl .github/workflows/hourly-continuity.yml .github/workflows/cascade.yml; do
  if [[ -f "$f" ]]; then
    echo "ok $f"
  else
    echo "missing $f"
    missing=1
  fi
done
if grep -RInE '(ghp_|github_pat_|AKIA[0-9A-Z]{16}|BEGIN (RSA |OPENSSH )?PRIVATE KEY)' . --include='*.yml' --include='*.md' --include='*.json' --include='*.jsonl' --include='*.sh' 2>/dev/null | grep -v env_check.sh; then
  echo "ALERT: secret-shaped string in tree"
  exit 2
fi
echo "secret-shape scan: clean"
exit "$missing"
