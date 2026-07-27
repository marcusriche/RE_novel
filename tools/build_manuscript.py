#!/usr/bin/env python3
"""Assemble the chapter files into a single deliverable manuscript and
report word counts (Word_Count_Actual feed).

Usage:
    python tools/build_manuscript.py                # build every known book
    python tools/build_manuscript.py clean_exit     # build one book
    python tools/build_manuscript.py safe_passage
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BOOKS = {
    "clean_exit": {
        "dir": "manuscript",
        "out": "CLEAN_EXIT.md",
        "chapters": 16,
        "epilogue": True,
    },
    "safe_passage": {
        "dir": "manuscript_safe_passage",
        "out": "SAFE_PASSAGE.md",
        "chapters": 17,
        "epilogue": True,
    },
    "out_of_office": {
        "dir": "manuscript_out_of_office",
        "out": "OUT_OF_OFFICE.md",
        "chapters": 24,
        "epilogue": False,
    },
}


def order(n_chapters: int, epilogue: bool) -> list:
    parts = ["00-front-matter.md"] + [f"ch{i:02d}.md" for i in range(1, n_chapters + 1)]
    if epilogue:
        parts.append("epilogue.md")
    return parts


def build(key: str) -> int:
    spec = BOOKS[key]
    ms = ROOT / spec["dir"]
    parts, total = [], 0
    print(f"\n== {key} ==")
    for name in order(spec["chapters"], spec["epilogue"]):
        text = (ms / name).read_text(encoding="utf-8").strip()
        words = len(text.split())
        total += words
        parts.append(text)
        print(f"{name:<22} {words:>6}")
    out = ms / spec["out"]
    out.write_text("\n\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"{'TOTAL':<22} {total:>6}")
    print(f"built {out.relative_to(ROOT)}")
    return total


def main() -> None:
    keys = sys.argv[1:] or list(BOOKS)
    for key in keys:
        if key not in BOOKS:
            raise SystemExit(f"unknown book {key!r}; known: {', '.join(BOOKS)}")
        build(key)


if __name__ == "__main__":
    main()
