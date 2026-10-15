#!/usr/bin/env python3
"""Regenerate README.md from data/papers.json and templates/README.template.md.

Usage:  python scripts/build_readme.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SECTIONS = [
    ("surveys", "Related Surveys"),
    ("background", "Background: Long-Context Models and Their Limits"),
    ("active", "Compute-Active Memory Compression"),
    ("inactive", "Compute-Inactive Memory"),
    ("transition", "State Transitions: Retrieval, Injection, and Intermediate States"),
    ("benchmarks", "Benchmarks and Evaluation"),
]

SUBSECTION_ORDER = {
    "surveys": ["Long-context LLMs", "Prompt compression, KV cache, and efficient serving",
                "RAG and agent memory", "Unified views of LLM memory"],
    "background": ["Long-context models and context extension", "Failure modes of long-context use"],
    "active": ["Input and prompt compression", "Compressed representations",
               "KV cache compression: heuristic eviction",
               "KV cache compression: query-, head-, and layer-aware selection",
               "KV cache compression: quantization, merging, and reuse",
               "KV cache compression: reasoning traces",
               "Architecture-level selective computation", "Serving-level cache and prefix management"],
    "inactive": ["Memory writing", "Memory organization", "Memory retrieval",
                 "Learned memory-management policies"],
    "transition": ["Retrieve-and-inject at the KV level", "Offloading and recall",
                   "Materialization and the parametric boundary", "Agent-side activation control",
                   "Memory security"],
    "benchmarks": ["Long-context understanding and retrieval", "KV-cache-centric evaluation",
                   "Long-term and agent memory", "Code and agent tasks"],
}


def anchor(text: str) -> str:
    a = text.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def row(p: dict) -> str:
    links = f"[[Paper]]({p['paper']})" if p["paper"] else ""
    if p.get("code"):
        links += f" [[Code]]({p['code']})"
    title = p["title"].replace("|", "\\|")
    return f"| {title} | {p['venue']} | {p['year']} | {links} |"


def main() -> None:
    papers = json.loads((ROOT / "data" / "papers.json").read_text(encoding="utf8"))
    toc, lists = [], []
    for sec, sec_title in SECTIONS:
        group = [p for p in papers if p["section"] == sec]
        if not group:
            continue
        toc.append(f"- [{sec_title}](#{anchor(sec_title)})")
        lists.append(f"### {sec_title}\n")
        subs = list(SUBSECTION_ORDER.get(sec, []))
        subs += sorted({p["subsection"] for p in group} - set(subs))
        for sub in subs:
            items = sorted((p for p in group if p["subsection"] == sub),
                           key=lambda p: (-p["year"], p["title"].lower()))
            if not items:
                continue
            toc.append(f"  - [{sub}](#{anchor(sub)})")
            lists.append(f"#### {sub}\n")
            lists.append("| Paper | Venue | Year | Links |\n|---|---|---|---|")
            lists.extend(row(p) for p in items)
            lists.append("")
    toc.extend(["- [Citation](#-citation)", "- [Contributing](#-contributing)"])
    template = (ROOT / "templates" / "README.template.md").read_text(encoding="utf8")
    out = (template.replace("{{COUNT}}", str(len(papers)))
                   .replace("{{TOC}}", "\n".join(toc))
                   .replace("{{LISTS}}", "\n".join(lists).rstrip() + "\n"))
    (ROOT / "README.md").write_text(out, encoding="utf8")
    print(f"README.md written with {len(papers)} papers.")


if __name__ == "__main__":
    main()
