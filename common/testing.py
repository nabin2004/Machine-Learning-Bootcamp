"""Parity helpers: compare library vs from-scratch outputs."""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray


def assert_parity(
    a: NDArray | float,
    b: NDArray | float,
    *,
    atol: float = 1e-5,
    rtol: float = 1e-5,
) -> None:
    """Assert ``a`` and ``b`` are close (NumPy semantics)."""
    np.testing.assert_allclose(a, b, atol=atol, rtol=rtol)


def print_side_by_side(
    name_a: str,
    value_a: Any,
    name_b: str,
    value_b: Any,
    *,
    precision: int = 6,
) -> None:
    """Pretty-print two values for demos (truncates large arrays)."""

    def _fmt(x: Any) -> str:
        if isinstance(x, np.ndarray):
            if x.size <= 12:
                return np.array2string(x, precision=precision, suppress_small=True)
            flat = x.ravel()[:6]
            return f"ndarray shape={x.shape} head={np.array2string(flat, precision=precision)} …"
        return repr(x)

    print(f"{name_a:>16} : {_fmt(value_a)}")
    print(f"{name_b:>16} : {_fmt(value_b)}")
