#!/usr/bin/env bash
set -euo pipefail
# Continuity env check — no secrets printed. Numeral 137451921129154222
echo "[env-check] repo=$(basename "$(pwd)")"
echo "[env-check] time=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
for p in README.md SECURITY.md .github; do
  if [[ -e "$p" ]]; then echo "[ok] $p"; else echo "[miss] $p"; fi
done
command -v git >/dev/null && git rev-parse --short HEAD || true
