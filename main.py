#!/usr/bin/env python3
"""Entrant for make.fun's Absurd Micro-Startup Pitch-Off.

Writes the one-sentence pitch to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os
import pathlib

PITCH = (
    "SaaSGrave: an agent reads your SaaS invoices, finds tools nobody has "
    "logged into since the last reorg, cancels them and keeps 15% of "
    "year-one savings; CFOs pay us to ghost dead software."
)

def main() -> None:
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(PITCH, encoding="utf-8")

if __name__ == "__main__":
    main()
