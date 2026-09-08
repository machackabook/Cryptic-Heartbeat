# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo", "pandas"]
# ///
"""
Azazels Ledger - Marimo Immersive Sheets
Each sheet = one full interactive HTML instance (sandboxed iframe via data URI)
Numeral 137451921129154222
Dual Authority: machackabook + azazeleous
Cryptic-Heartbeat Nexus

Run:
  pip install marimo pandas
  marimo edit azazels_ledger_marimo.py
  marimo run azazels_ledger_marimo.py
"""

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from pathlib import Path
    import base64
    import html as html_lib
    return base64, html_lib, mo, pd, Path


@app.cell
def _(Path):
    here = Path(__file__).resolve().parent if "__file__" in dir() else Path(".")
    candidates = [
        here,
        here / "artifacts",
        Path("/home/workdir/artifacts"),
        Path("."),
    ]
    BASE = next(
        (c for c in candidates if (c / "sovereign_chimera_nexus.html").exists()),
        here,
    )
    SURFACES = [
        {
            "id": "chimera",
            "title": "Sovereign Chimera Nexus",
            "band": "137-visual",
            "path": "sovereign_chimera_nexus.html",
            "role": "immersive ledger surface",
        },
        {
            "id": "trygod",
            "title": "trygod / YAHWEH OS LIVE COHERENCE",
            "band": "100-dev-ai",
            "path": "trygod.html",
            "role": "live coherence",
        },
        {
            "id": "will",
            "title": "THIS IS THY WILL",
            "band": "066-root",
            "path": "SINGULARITY_WILL.md",
            "role": "declaration",
        },
        {
            "id": "allah",
            "title": "A.L.L.A.H. NEP-2.0",
            "band": "066-root",
            "path": "ALLAH-Nexus-Enclave-Protocol-2.0-CLEAN.md",
            "role": "constitution",
        },
    ]
    return BASE, SURFACES


@app.cell
def _(BASE, SURFACES, base64, html_lib, pd):
    rows = []
    html_map = {}
    for s in SURFACES:
        p = BASE / s["path"]
        if not p.exists():
            continue
        raw = p.read_text(encoding="utf-8", errors="ignore")
        if p.suffix.lower() in {".md", ".txt"}:
            body = html_lib.escape(raw).replace("\n", "<br/>")
            raw = (
                "<!DOCTYPE html><html><head><meta charset='utf-8'>"
                "<style>body{background:#02040a;color:#e2e8f0;font-family:monospace;"
                "padding:24px;line-height:1.5}</style></head><body>"
                f"<h1 style='color:#00f3ff'>{html_lib.escape(s['title'])}</h1>"
                f"<div>{body}</div></body></html>"
            )
        b64 = base64.b64encode(raw.encode("utf-8", errors="replace")).decode("ascii")
        data_uri = f"data:text/html;base64,{b64}"
        html_map[s["id"]] = data_uri
        rows.append(
            {
                "sheet_id": s["id"],
                "title": s["title"],
                "band": s["band"],
                "role": s["role"],
                "size_bytes": len(raw),
                "html_ready": True,
                "numeral": "137451921129154222",
            }
        )
    df = pd.DataFrame(rows)
    return df, html_map


@app.cell
def _(df, mo):
    mo.md(
        f"""
# Azazels Ledger - Marimo Immersive Sheets

**Numeral** `137451921129154222`  
**Dual Authority** machackabook + azazeleous  
**Nexus** Cryptic-Heartbeat

Each sheet is a **live interactive HTML instance** (sandboxed iframe via data URI).  
Scripts and styles from the original HTML run inside the frame.

Sheets in DataFrame: **{len(df)}**
"""
    )
    return


@app.cell
def _(df, mo):
    table = mo.ui.table(df, selection="single", label="Select a sheet")
    table
    return (table,)


@app.cell
def _(html_map, mo, table):
    sel = table.value
    if sel is None or len(sel) == 0:
        out = mo.md("_Select a row in the table to load the immersive HTML instance._")
    else:
        row = sel.iloc[0]
        sid = str(row["sheet_id"])
        uri = html_map.get(sid, "")
        title = str(row["title"])
        band = str(row["band"])
        role = str(row["role"])
        frame = mo.Html(
            f"""
            <div style="border:1px solid #1e293b;border-radius:12px;overflow:hidden;background:#000">
              <div style="padding:8px 12px;font-size:11px;color:#94a3b8;background:#0f172a">
                <b style="color:#00f3ff">{title}</b>
                &nbsp;|&nbsp; band <span style="color:#fbbf24">{band}</span>
                &nbsp;|&nbsp; {role}
              </div>
              <iframe
                src="{uri}"
                style="width:100%;height:70vh;border:0;background:#000"
                sandbox="allow-scripts allow-same-origin allow-forms allow-modals allow-popups"
                title="{title}"
              ></iframe>
            </div>
            """
        )
        out = frame
    out
    return


@app.cell
def _(mo):
    mo.md(
        """
---
### How to run

```bash
pip install marimo pandas
marimo edit azazels_ledger_marimo.py
# or headless:
marimo run azazels_ledger_marimo.py
```

Standalone (no marimo required): open `azazels_immersive_sheets.html` in a browser.  
Each tab is one full interactive HTML instance.
"""
    )
    return


if __name__ == "__main__":
    app.run()
