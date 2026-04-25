"""Lightweight timing helpers for Episode 0 and optimization lessons."""

from __future__ import annotations

import time
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any


@contextmanager
def timer(label: str = "block") -> Iterator[dict[str, float]]:
    """Context manager that records elapsed seconds in ``info['seconds']``."""
    info: dict[str, float] = {}
    t0 = time.perf_counter()
    try:
        yield info
    finally:
        info["seconds"] = time.perf_counter() - t0
        print(f"[timer] {label}: {info['seconds']:.6f}s")


class Timer:
    """Reusable stopwatch (start/stop/elapsed)."""

    def __init__(self) -> None:
        self._t0: float | None = None
        self._t1: float | None = None

    def start(self) -> None:
        self._t0 = time.perf_counter()
        self._t1 = None

    def stop(self) -> float:
        if self._t0 is None:
            msg = "Timer.start() was not called."
            raise RuntimeError(msg)
        self._t1 = time.perf_counter()
        return self.elapsed

    @property
    def elapsed(self) -> float:
        end = self._t1 if self._t1 is not None else time.perf_counter()
        if self._t0 is None:
            msg = "Timer.start() was not called."
            raise RuntimeError(msg)
        return end - self._t0


def nbytes(obj: Any) -> int:
    """Best-effort memory footprint for NumPy arrays (else ``sys.getsizeof``)."""
    import sys

    if hasattr(obj, "nbytes"):
        return int(obj.nbytes)  # type: ignore[no-any-return]
    return sys.getsizeof(obj)
