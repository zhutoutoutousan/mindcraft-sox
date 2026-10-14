#!/usr/bin/env python3
"""Serve a tmp/*.pdf over HTTP and print an ngrok public URL.

Requires NGROK_TOKEN (or ngrok already authed) and `ngrok` on PATH.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for p in here.parents:
        if (p / "CPU.md").is_file():
            return p
    sys.exit("ASK CPU.md not found")


def main() -> int:
    if len(sys.argv) != 2:
        print("ASK python .../serve_pdf_ngrok.py tmp/day-YYYY-MM-DD.pdf")
        return 2
    root = repo_root()
    pdf = Path(sys.argv[1])
    if not pdf.is_absolute():
        pdf = root / pdf
    if not pdf.is_file():
        print(f"ASK missing pdf {pdf}")
        return 2
    if not shutil.which("ngrok"):
        print("ASK ngrok not on PATH")
        return 2
    token = os.environ.get("NGROK_TOKEN") or os.environ.get("NGROK_AUTHTOKEN")
    if token:
        subprocess.run(["ngrok", "config", "add-authtoken", token], check=False, capture_output=True)
    serve = Path("/tmp/pdf-serve")
    serve.mkdir(parents=True, exist_ok=True)
    dest = serve / pdf.name
    shutil.copy2(pdf, dest)
    (serve / "index.html").write_text(
        f"<!DOCTYPE html><html lang=de><meta charset=utf-8>"
        f"<title>{pdf.name}</title><body style='font-family:Georgia;max-width:36rem;margin:3rem auto'>"
        f"<h1>PDF</h1><p><a href='/{pdf.name}'>{pdf.name} herunterladen</a></p></body></html>",
        encoding="utf-8",
    )
    # stop previous listeners on 8765 if we started them (best-effort)
    subprocess.run(["pkill", "-f", "http.server 8765"], check=False)
    subprocess.run(["pkill", "-f", "ngrok http 8765"], check=False)
    time.sleep(0.5)
    http = subprocess.Popen(
        [sys.executable, "-m", "http.server", "8765"],
        cwd=serve,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    ng = subprocess.Popen(
        ["ngrok", "http", "8765", "--log=stdout"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    url = None
    for _ in range(30):
        time.sleep(0.4)
        try:
            with urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels", timeout=1) as r:
                data = json.load(r)
            for t in data.get("tunnels", []):
                if t.get("public_url", "").startswith("https://"):
                    url = t["public_url"]
                    break
            if url:
                break
        except Exception:
            continue
    if not url:
        http.terminate()
        ng.terminate()
        print("ASK ngrok tunnel not ready")
        return 1
    print(url)
    print(f"{url}/{pdf.name}")
    print(f"pids http={http.pid} ngrok={ng.pid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
