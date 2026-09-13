#!/usr/bin/env bash
set -euo pipefail
# Continuity env check — refuse missing origin surfaces
need=(README.md SECURITY.md)
for f in "${need[@]}"; do
  if [[ ! -s "$f" ]]; then
    echo "env_check FAIL: $f missing or empty" >&2
    exit 1
  fi
done
echo "env_check OK numeral=137451921129154222"
