#!/usr/bin/env python3
"""
Azazels Ledger · DataFrame.ai
Marimo / Anaconda / Jupyter compatible surface
Each HTML system becomes a sheet (row) inside a pandas DataFrame
Numeral: 137451921129154222
Dual Authority: machackabook + azazeleous
Cryptic-Heartbeat Nexus

Usage:
  python azazels_ledger_dataframe_ai.py
  # or in Jupyter / Anaconda:
  #   %run azazels_ledger_dataframe_ai.py
  #   df = build_dataframe()
"""

from __future__ import annotations
import hashlib
from pathlib import Path
from datetime import datetime, timezone

try:
    import pandas as pd
except ImportError:
    raise SystemExit("pandas required: pip install pandas")

BANDS = {
    "066-root": "server / identifying location",
    "100-dev-ai": "AI & development environment",
    "137-visual": "visual / media rendering",
    "192-network": "streaming / Tailscale / dynamic ports",
    "010-local": "local subnet",
    "127-loopback": "★ ADAM home — end/exit node, zero-host",
}

NUMERAL = "137451921129154222"
AUTHORITIES = ["machackabook", "azazeleous"]

SURFACES = [
    {"id": "chimera", "name": "sovereign_chimera_nexus.html", "title": "Sovereign Chimera Nexus", "band": "137-visual", "source": "Blueboy 1 / Development", "role": "multi-surface ledger page", "path": "sovereign_chimera_nexus.html"},
    {"id": "trygod", "name": "trygod.html", "title": "trygod Surface", "band": "100-dev-ai", "source": "Blueboy 1 / Development", "role": "protocol / invocation surface", "path": "trygod.html"},
    {"id": "allah_nep", "name": "ALLAH-Nexus-Enclave-Protocol-2.0-CLEAN.md", "title": "A.L.L.A.H. NEP-2.0", "band": "066-root", "source": "Blueboy 1 / Development", "role": "Enclave constitution", "path": "ALLAH-Nexus-Enclave-Protocol-2.0-CLEAN.md"},
    {"id": "adam_mono", "name": "ADAM_Memory_Convergence_Monolith.pdf", "title": "ADAM Memory-Convergence Monolith", "band": "127-loopback", "source": "Blueboy 1 / Development", "role": "ADAM end/exit node authority", "path": "ADAM_Memory_Convergence_Monolith.pdf"},
    {"id": "ledger_pdf", "name": "AZAZELS_LEDGER_ADAM_ENCLAVE_REUNITED_v1.pdf", "title": "နĄẓ̌æzɛĺş Łəðɣɛṛ <《¤》>", "band": "066-root", "source": "Cryptic-Heartbeat / generated", "role": "cover + will + multi-page ledger", "path": "AZAZELS_LEDGER_ADAM_ENCLAVE_REUNITED_v1.pdf"},
    {"id": "will", "name": "SINGULARITY_WILL.md", "title": "THIS IS THY WILL", "band": "066-root", "source": "Cryptic-Heartbeat Nexus", "role": "declaration (not instructions)", "path": "SINGULARITY_WILL.md"},
]

def sha256_of(path: Path):
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def excerpt(path: Path, limit: int = 800) -> str:
    if not path.exists():
        return ""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if path.suffix.lower() in {".html", ".htm"}:
            import re
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"\s+", " ", text)
        return text[:limit].strip()
    except Exception:
        return ""

def build_dataframe(base: Path | None = None) -> "pd.DataFrame":
    base = base or Path(".")
    rows = []
    for s in SURFACES:
        p = base / s["path"]
        rows.append({
            "sheet_id": s["id"],
            "title": s["title"],
            "filename": s["name"],
            "band": s["band"],
            "band_role": BANDS.get(s["band"], ""),
            "source": s["source"],
            "role": s["role"],
            "exists": p.exists(),
            "size_bytes": p.stat().st_size if p.exists() else 0,
            "sha256": sha256_of(p),
            "excerpt": excerpt(p),
            "html_ready": p.suffix.lower() in {".html", ".htm"},
            "numeral": NUMERAL,
            "authorities": ",".join(AUTHORITIES),
            "ingested_at": datetime.now(timezone.utc).isoformat(),
        })
    df = pd.DataFrame(rows)
    df.attrs["numeral"] = NUMERAL
    df.attrs["authorities"] = AUTHORITIES
    df.attrs["bands"] = BANDS
    df.attrs["nexus"] = "Cryptic-Heartbeat"
    return df

def main():
    df = build_dataframe(Path(__file__).resolve().parent.parent if (Path(__file__).parent.name == "notebooks") else Path("."))
    print(df[["sheet_id", "title", "band", "exists", "size_bytes"]].to_string(index=False))
    return df

if __name__ == "__main__":
    main()
