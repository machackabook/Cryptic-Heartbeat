#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "[cryptic-heartbeat env-check] ${ROOT}"
test -f "${ROOT}/README.md"
echo ok
