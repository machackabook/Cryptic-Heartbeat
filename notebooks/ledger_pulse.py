#!/usr/bin/env python3
"""Map Azazels Ledger sheets onto a gravityPull pulse for gaia-visualizer."""

from __future__ import annotations

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
)


def pulse_from_counts(sheet_count: int, existing: int, now: datetime | None = None) -> float:
    now = now or datetime.now(timezone.utc)
    circadian = 0.35 + 0.65 * abs(((now.hour + now.minute / 60) - 12) / 12)
    density = 0.4 + min(existing, sheet_count or 1) / max(sheet_count, 1) * 1.2
    numeral_nudge = (int(NUMERAL[-3:]) % 100) / 200  # 0 .. 0.495
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
) -> dict:
    geo = geometry if geometry in GEOMETRIES else "torus"
    return {
        "geometry": geo,
        "gravityPull": pulse_from_counts(sheet_count, existing),
        "toroidalWeave": weave_from_counts(sheet_count, existing),
        "lerp": 0.05,
        "blend": max(0.0, min(1.0, float(blend))),
        "numeral": NUMERAL,
    }


if __name__ == "__main__":
    print(contract())
