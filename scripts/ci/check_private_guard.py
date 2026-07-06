#!/usr/bin/env python3
"""
check_private_guard.py -- guard against private-contour leakage (ADR-008).

A public repo must not mention private projects. Greps text files for forbidden
terms from `.private-guard` (one per line). If found, CI fails.

Exit: 0 -- clean; 1 -- a private mention found.
Run: python scripts/ci/check_private_guard.py [root=.]
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
GUARD_FILE = ROOT / ".private-guard"
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__",
             "_preview_example_project_repo"}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".py", ".json", ".txt", ".toml", ".cfg"}


def load_terms():
    if not GUARD_FILE.exists():
        return []
    out = []
    for line in GUARD_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line.lower())
    return out


def main():
    terms = load_terms()
    if not terms:
        print("[WARN] .private-guard empty or missing -- guard skipped")
        return 0
    hits = []
    for f in ROOT.rglob("*"):
        if f.is_dir() or any(part in SKIP_DIRS for part in f.parts):
            continue
        if f.suffix.lower() not in TEXT_SUFFIXES or f.name == ".private-guard":
            continue
        content = f.read_text(encoding="utf-8", errors="ignore").lower()
        for term in terms:
            if term in content:
                hits.append((f.relative_to(ROOT).as_posix(), term))
    if hits:
        print("[FAIL] PRIVATE LEAK: forbidden term in public repo:")
        for src, term in hits:
            print("   - {} contains '{}'".format(src, term))
        return 1
    print("[OK] Private guard: no leaks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
