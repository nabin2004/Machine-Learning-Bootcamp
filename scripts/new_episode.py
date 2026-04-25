#!/usr/bin/env python3
"""Create a new episode from ``templates/episode_template`` or bootstrap the full curriculum."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

EPISODE_DIR_RE = re.compile(r"^ep\d{2}_[a-z0-9_]+$")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def substitute(text: str, *, title: str, folder: str) -> str:
    return text.replace("{{EPISODE_TITLE}}", title).replace("{{EPISODE_FOLDER}}", folder)


def infer_title(folder: str) -> str:
    if folder == "ep00_bottom_up":
        return "Episode 0 — ML from the bottom up"
    parts = folder.split("_", 1)
    if len(parts) == 2 and parts[0].startswith("ep"):
        return parts[1].replace("_", " ").title()
    return folder


def copy_episode(*, template: Path, dest: Path, title: str, folder: str) -> None:
    shutil.copytree(template, dest)
    for path in dest.rglob("*"):
        if path.is_dir():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".ico", ".webp"}:
            continue
        try:
            data = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        path.write_text(substitute(data, title=title, folder=folder), encoding="utf-8")


def bootstrap(*, force: bool) -> int:
    root = repo_root()
    template = root / "templates" / "episode_template"
    curriculum_path = root / "scripts" / "curriculum.json"
    rows = json.loads(curriculum_path.read_text(encoding="utf-8"))
    created = 0
    for row in rows:
        phase = row["phase"]
        folder = row["folder"]
        title = row["title"]
        dest = root / folder if phase is None else root / phase / folder
        if dest.exists() and not force:
            print(f"skip (exists): {dest}")
            continue
        if dest.exists() and force:
            shutil.rmtree(dest)
        copy_episode(template=template, dest=dest, title=title, folder=folder)
        print(f"created: {dest}")
        created += 1
    print(f"bootstrap done ({created} created, others skipped unless --force).")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bootstrap", action="store_true", help="create all episodes from curriculum.json"
    )
    parser.add_argument(
        "--force", action="store_true", help="overwrite existing episode folders (dangerous)"
    )
    parser.add_argument("--name", help="folder basename, e.g. ep41_custom_topic")
    parser.add_argument("--phase", help="phase directory, e.g. phase_2_deep_learning")
    parser.add_argument("--title", help="human-readable title (inferred from --name if omitted)")
    args = parser.parse_args(argv)

    if args.bootstrap:
        return bootstrap(force=args.force)

    if not args.name or not args.phase:
        parser.error("--name and --phase are required unless --bootstrap is set")

    if not EPISODE_DIR_RE.match(args.name):
        print(f"error: --name must match {EPISODE_DIR_RE.pattern}", file=sys.stderr)
        return 2

    root = repo_root()
    template = root / "templates" / "episode_template"
    dest = root / args.phase / args.name
    if dest.exists():
        print(f"error: destination already exists: {dest}", file=sys.stderr)
        return 1

    title = args.title or infer_title(args.name)
    copy_episode(template=template, dest=dest, title=title, folder=args.name)
    print(f"created: {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
