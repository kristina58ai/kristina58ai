#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_portfolio.py -- regenerate Profile README sections from portfolio.yml.

Single source of truth = portfolio.yml. This script rewrites two marker-delimited
sections in README.md (RU) and README.en.md (EN):

  <!-- PORTFOLIO:CONSTELLATION:START --> ... <!-- PORTFOLIO:CONSTELLATION:END -->
  <!-- PORTFOLIO:INDEX:START --> ... <!-- PORTFOLIO:INDEX:END -->

Only PUBLIC projects are rendered (private ones are never in portfolio.yml -- ADR-008).
Idempotent: safe to run on every push; content between markers is replaced.

Run: python scripts/gen_portfolio.py [root=.]
Dep: PyYAML (pip install pyyaml)
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("[FAIL] PyYAML required: pip install pyyaml")
    raise SystemExit(2)

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

# Localized labels per language
L = {
    "ru": {
        "status": {"planned": "⚪ планируется",
                    "in_progress": "\U0001f7e1 в работе",
                    "done": "\U0001f7e2 готово"},
        "th_project": "Проект",
        "th_status": "Статус",
        "th_coverage": "Компетенция",
    },
    "en": {
        "status": {"planned": "⚪ planned",
                    "in_progress": "\U0001f7e1 in progress",
                    "done": "\U0001f7e2 done"},
        "th_project": "Project",
        "th_status": "Status",
        "th_coverage": "Coverage",
    },
}


def node_id(pid: str) -> str:
    return re.sub(r"[^0-9A-Za-z_]", "_", pid)


def build_constellation(projects: dict) -> str:
    """Mermaid graph: public project nodes + undirected links from `links`."""
    lines = ["```mermaid", "graph LR"]
    for pid, p in projects.items():
        title = p.get("title", pid)
        cov = p.get("coverage", "")
        label = title if not cov else f"{title}<br/><small>{cov}</small>"
        lines.append(f'  {node_id(pid)}["{label}"]')
    seen = set()
    for pid, p in projects.items():
        for target in p.get("links", []):
            if target not in projects:
                continue
            pair = tuple(sorted((pid, target)))
            if pair in seen:
                continue
            seen.add(pair)
            lines.append(f"  {node_id(pair[0])} --- {node_id(pair[1])}")
    lines.append("```")
    return "\n".join(lines)


def build_index(projects: dict, lang: str) -> str:
    t = L[lang]
    out = [f"| {t['th_project']} | {t['th_status']} | {t['th_coverage']} |",
           "|---|---|---|"]
    for pid, p in projects.items():
        title = p.get("title", pid)
        repo = p.get("repo")
        name = f"[{title}]({repo})" if repo else title
        status = t["status"].get(p.get("status", "planned"), p.get("status", ""))
        cov = p.get("coverage", "")
        out.append(f"| {name} | {status} | {cov} |")
        # versions as sub-rows
        for v in p.get("versions", []):
            vtitle = v.get("title", v.get("id", ""))
            vrepo = v.get("repo")
            vname = f"&nbsp;&nbsp;└ [{vtitle}]({vrepo})" if vrepo else f"&nbsp;&nbsp;└ {vtitle}"
            vstatus = t["status"].get(v.get("status", "planned"), v.get("status", ""))
            out.append(f"| {vname} | {vstatus} | {v.get('stack','')} |")
    return "\n".join(out)


def replace_between(text: str, marker: str, payload: str) -> str:
    start = f"<!-- PORTFOLIO:{marker}:START -->"
    end = f"<!-- PORTFOLIO:{marker}:END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    replacement = f"{start}\n{payload}\n{end}"
    if not pattern.search(text):
        print(f"[WARN] markers {marker} not found -- skipped")
        return text
    return pattern.sub(replacement, text)


def process(readme: Path, lang: str, projects: dict) -> bool:
    if not readme.exists():
        print(f"[WARN] {readme.name} not found -- skipped")
        return False
    text = readme.read_text(encoding="utf-8")
    text = replace_between(text, "CONSTELLATION", build_constellation(projects))
    text = replace_between(text, "INDEX", build_index(projects, lang))
    readme.write_text(text, encoding="utf-8")
    print(f"[OK] {readme.name} regenerated ({lang})")
    return True


def main() -> int:
    data = yaml.safe_load((ROOT / "portfolio.yml").read_text(encoding="utf-8"))
    projects = {pid: p for pid, p in (data.get("projects") or {}).items()
                if p.get("visibility", "public") == "public"}
    if not projects:
        print("[FAIL] no public projects in portfolio.yml")
        return 1
    process(ROOT / "PROJECTMAP.md", "ru", projects)
    process(ROOT / "PROJECTMAP.en.md", "en", projects)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
