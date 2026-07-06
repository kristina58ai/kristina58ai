#!/usr/bin/env python3
"""
check_bilingual.py -- bilingual parity check (ADR-003).

Rule: for every RU file `X.md` there must be an `X.en.md`, EXCEPT files matched
by the allowlist (glob patterns in `.bilingual-allowlist`).
`*.en.md` files are the EN versions themselves -- not checked.

Exit: 0 -- parity ok; 1 -- some RU file has no EN (outside allowlist).
Run: python scripts/ci/check_bilingual.py [root=.]
"""
import sys
import fnmatch
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
ALLOWLIST_FILE = ROOT / ".bilingual-allowlist"
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "templates",
             "_preview_example_project_repo"}


def load_allowlist():
    if not ALLOWLIST_FILE.exists():
        return []
    out = []
    for line in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def is_allowlisted(rel, patterns):
    return any(fnmatch.fnmatch(rel, p) for p in patterns)


def main():
    allowlist = load_allowlist()
    missing = []
    for md in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in md.parts):
            continue
        if md.name.endswith(".en.md"):
            continue
        rel = md.relative_to(ROOT).as_posix()
        if is_allowlisted(rel, allowlist):
            continue
        if not md.with_name(md.name[:-3] + ".en.md").exists():
            missing.append(rel)
    if missing:
        print("[FAIL] Bilingual parity broken -- no EN version for:")
        for m in sorted(missing):
            print("   - {} -> expected {}.en.md".format(m, m[:-3]))
        return 1
    print("[OK] Bilingual parity: every RU file has an EN version (or allowlisted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
