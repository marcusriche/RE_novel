#!/usr/bin/env python3
"""Assemble the chapter files into the single deliverable manuscript and
report word counts (Word_Count_Actual feed).

Usage: python tools/build_manuscript.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MS = ROOT / "manuscript"

ORDER = (["00-front-matter.md"]
         + [f"ch{i:02d}.md" for i in range(1, 17)]
         + ["epilogue.md"])


def main() -> None:
    parts = []
    total = 0
    for name in ORDER:
        text = (MS / name).read_text(encoding="utf-8").strip()
        words = len(text.split())
        total += words
        parts.append(text)
        print(f"{name:<22} {words:>6}")
    out = MS / "CLEAN_EXIT.md"
    out.write_text("\n\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"{'TOTAL':<22} {total:>6}")
    print(f"built {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
