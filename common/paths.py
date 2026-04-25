"""Filesystem helpers for notebooks, tests, and Manim scenes."""

from __future__ import annotations

from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    """Walk parents from *start* (default: cwd) until ``pyproject.toml`` is found."""
    here = (start or Path.cwd()).resolve()
    for path in [here, *here.parents]:
        if (path / "pyproject.toml").exists():
            return path
    msg = "Could not locate repository root (no pyproject.toml in parents)."
    raise RuntimeError(msg)
