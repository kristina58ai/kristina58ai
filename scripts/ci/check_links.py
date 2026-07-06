#!/usr/bin/env python3
"""
check_links.py -- internal (relative) Markdown link checker.

Catches broken relative links to files inside the repo: [text](path) and
[text](path#anchor). External links (http/https/mailto) and in-document
anchors (#...) are skipped.

templates/ and the local preview are skipped (placeholder links).

Exit: 0 -- all internal links resolve; 1 -- some are broken.
Run: python scripts/ci/check_links.py [root=.]
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "templates",
             "_preview_example_project_repo"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_external(t):
    return t.startswith(("http://", "https://", "mailto:", "#", "tel:"))


def main():
    broken = []
    for md in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip().split()[0]
            if is_external(target):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            if not (md.parent / path_part).resolve().exists():
                broken.append((md.relative_to(ROOT).as_posix(), target))
    if broken:
        print("[FAIL] Broken internal links found:")
        for src, tgt in broken:
            print("   - {} -> {}".format(src, tgt))
        return 1
    print("[OK] Internal links: all resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
