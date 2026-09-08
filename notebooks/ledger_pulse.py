#!/usr/bin/env python3
"""Map Azazels Ledger sheets onto a gravityPull pulse for gaia-visualizer.

Stage-12 wire: authenticated POST/WS onto The-Hive.

  GAIA_PULSE_TOKEN=secret python notebooks/ledger_pulse.py --ws ws://localhost:3000
  python notebooks/ledger_pulse.py --http http://localhost:3000 --geometry knot --pulse 1.6
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

NUMERAL = "137451921129154222"

GEOMETRIES = (
    "torus",
    "infinity",
    "hamiltonian",
    "triangular",
    "helix",
    "mobius",
    "lissajous",
    "klein",
    "hopf",
    "rose",
    "seifert",
    "blend",
    "trefoil",
    "stereo",
    "clifford",
    "enneper",
    "gyroid",
    "calabi",
    "figure8",
    "villarceau",
    "boy",
    "catenoid",
    "dini",
    "roman",
    "hyperbolic",
    "scherk",
    "knot",
    "pseudosphere",
)


def pulse_from_counts(sheet_count: int, existing: int, now: datetime | None = None) -> float:
    now = now or datetime.now(timezone.utc)
    circadian = 0.35 + 0.65 * abs(((now.hour + now.minute / 60) - 12) / 12)
    density = 0.4 + min(existing, sheet_count or 1) / max(sheet_count, 1) * 1.2
    numeral_nudge = (int(NUMERAL[-3:]) % 100) / 200
    value = circadian * 0.5 + density * 0.4 + numeral_nudge * 0.2
    return max(0.1, min(3.0, round(value, 3)))


def weave_from_counts(sheet_count: int, existing: int) -> float:
    ratio = min(existing, sheet_count or 1) / max(sheet_count, 1)
    return max(0.0, min(4.0, round(0.6 + ratio * 1.4, 3)))


def contract(
    geometry: str = "torus",
    sheet_count: int = 6,
    existing: int = 6,
    blend: float = 0.5,
    token: str | None = None,
) -> dict:
    geo = geometry if geometry in GEOMETRIES else "torus"
    payload = {
        "type": "gaia:targetState",
        "geometry": geo,
        "gravityPull": pulse_from_counts(sheet_count, existing),
        "toroidalWeave": weave_from_counts(sheet_count, existing),
        "lerp": 0.05,
        "blend": max(0.0, min(1.0, float(blend))),
        "numeral": NUMERAL,
    }
    tok = token if token is not None else os.environ.get("GAIA_PULSE_TOKEN", "")
    if tok:
        payload["token"] = tok
    return payload


def pulse_frame(pulse: float, token: str | None = None) -> dict:
    frame = {"type": "gaia:pulse", "pulse": max(0.1, min(3.0, float(pulse)))}
    tok = token if token is not None else os.environ.get("GAIA_PULSE_TOKEN", "")
    if tok:
        frame["token"] = tok
    return frame


def _post_json(url: str, payload: dict, token: str) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "content-type": "application/json",
            **({"x-gaia-token": token} if token else {}),
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            print(resp.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code}: {exc.read().decode('utf-8', errors='replace')}", file=sys.stderr)
        raise SystemExit(1)


def _ws_send(url: str, payload: dict) -> None:
    try:
        import websocket  # type: ignore
    except ImportError:
        print("websocket-client is required for --ws (pip install websocket-client)", file=sys.stderr)
        raise SystemExit(2)
    ws = websocket.create_connection(url, timeout=8)
    try:
        ws.send(json.dumps(payload))
        print(json.dumps(payload))
    finally:
        ws.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Authenticated ledger pulse → Hive")
    parser.add_argument("--geometry", default="blend")
    parser.add_argument("--sheets", type=int, default=6)
    parser.add_argument("--existing", type=int, default=6)
    parser.add_argument("--blend", type=float, default=0.5)
    parser.add_argument("--pulse", type=float, default=None, help="override gravity pulse")
    parser.add_argument("--http", default="", help="Hive origin, e.g. http://localhost:3000")
    parser.add_argument("--ws", default="", help="Hive WS, e.g. ws://localhost:3000")
    parser.add_argument("--token", default=None)
    args = parser.parse_args()

    token = args.token if args.token is not None else os.environ.get("GAIA_PULSE_TOKEN", "")
    payload = contract(args.geometry, args.sheets, args.existing, args.blend, token)
    if args.pulse is not None:
        payload["gravityPull"] = max(0.1, min(3.0, float(args.pulse)))

    if args.http:
        origin = args.http.rstrip("/")
        _post_json(f"{origin}/api/gaia/contract", payload, token)
        _post_json(f"{origin}/api/gaia/pulse", pulse_frame(payload["gravityPull"], token), token)
        return
    if args.ws:
        _ws_send(args.ws, payload)
        _ws_send(args.ws, pulse_frame(payload["gravityPull"], token))
        return
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
