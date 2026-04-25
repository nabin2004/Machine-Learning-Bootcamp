#!/usr/bin/env python3
"""Add missing cell ids and normalize notebooks (nbformat >= 5.1)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import nbformat
from nbformat.validator import normalize


def iter_notebooks(root: Path) -> list[Path]:
    skip_parts = {".venv", "venv", "__pycache__", ".git"}
    out: list[Path] = []
    for path in root.rglob("*.ipynb"):
        if any(part in skip_parts for part in path.parts):
            continue
        out.append(path)
    return sorted(out)


def raw_cells_missing_ids(path: Path) -> bool:
    """Check on-disk JSON so we do not rely on nbformat's transparent id repair on read."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    return any("id" not in cell for cell in raw.get("cells", []))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "roots",
        nargs="*",
        default=["."],
        help="directories to scan (default: current directory)",
    )
    args = parser.parse_args()
    cwd = Path.cwd()
    updated = 0
    for root_str in args.roots:
        root = (cwd / root_str).resolve()
        for path in iter_notebooks(root):
            if not raw_cells_missing_ids(path):
                continue
            nb = nbformat.read(path, as_version=4)
            _, nb_norm = normalize(nb)
            nbformat.write(nb_norm, path)
            print(f"normalized: {path.relative_to(cwd)}")
            updated += 1
    print(f"done ({updated} notebooks updated).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
