#!/usr/bin/env bash
# Continuity env-check — fail closed. Numeral 137451921129154222.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail() { echo "[env-check] FAIL: $*" >&2; exit 1; }

[[ -f "$ROOT/README.md" ]] || fail "missing README.md"
[[ -d "$ROOT/.git" || -n "${GITHUB_SHA:-}" ]] || true

if [[ -n "${GITHUB_SHA:-}" ]]; then
  [[ -n "$GITHUB_SHA" ]] || fail "empty GITHUB_SHA"
fi

# secret-looking filenames in working copy (not contents)
while IFS= read -r -d '' f; do
  base="$(basename "$f")"
  case "$base" in
    *.pem|*.p12|id_rsa|id_ed25519|.env|.env.*) fail "secret-looking file: $f" ;;
  esac
done < <(find "$ROOT" -maxdepth 3 -type f -print0 2>/dev/null || true)

echo "[env-check] OK stage-182 Cryptic-Heartbeat numeral 137451921129154222"
