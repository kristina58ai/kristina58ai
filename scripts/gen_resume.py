#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_resume.py -- build resume.pdf from RESUME.md via pandoc (xelatex).

Cyrillic needs xelatex + a Unicode font (DejaVu Sans on CI). Leading HTML
comments are stripped before render. The cleaned intermediate goes to the
system temp dir (repo stays clean).

Local: python scripts/gen_resume.py   # needs pandoc + texlive-xetex + fonts-dejavu
CI: .github/workflows/resume.yml
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SRC = ROOT / "RESUME.md"
OUT = ROOT / "resume.pdf"
FONT = "DejaVu Sans"


def build():
    text = re.sub(r"<!--.*?-->\s*", "", SRC.read_text(encoding="utf-8"), flags=re.DOTALL)
    fd, tmp = tempfile.mkstemp(suffix=".md")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
    cmd = ["pandoc", tmp, "-o", str(OUT), "--pdf-engine=xelatex",
           "-V", "mainfont=" + FONT, "-V", "geometry:margin=2cm"]
    try:
        subprocess.run(cmd, check=True)
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def main():
    if not SRC.exists():
        print("[FAIL] RESUME.md not found")
        return 1
    try:
        build()
    except FileNotFoundError:
        print("[FAIL] pandoc missing: install pandoc + texlive-xetex + fonts-dejavu")
        return 2
    except subprocess.CalledProcessError as e:
        print("[FAIL] pandoc error:", e)
        return 3
    print("[OK] resume.pdf built")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
