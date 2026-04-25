# Episode template

Every episode is a **self-contained folder** with the same layout so learners always know
where to look.

## Layout

```
ep##_short_name/
├── README.md
├── 01_intuition.ipynb
├── 02_library_run.ipynb
├── 03_from_scratch.ipynb
├── 04_limits.ipynb
├── notes.md
├── scratch/
│   ├── __init__.py
│   └── core.py
└── videos/
    └── scene.py
```

## Act notebooks

| Notebook | Goal |
|----------|------|
| `01_intuition` | Geometry, loss, behaviour—**RISE** slideshow friendly, almost no code. |
| `02_library_run` | Minimal sklearn / PyTorch / HF pipeline; correct API usage. |
| `03_from_scratch` | Hand-rolled implementation; should mirror notebook 02 on seeded data. |
| `04_limits` | Where it breaks: imbalance, scaling, instability, shift, etc. |

## Library vs from-scratch

Use **Act 3** (`03_from_scratch.ipynb`) to compare against **Act 2** on the same seeded
data. `common.testing.print_side_by_side` / `assert_parity` are optional helpers when you
want explicit numeric checks in the notebook.

## `notes.md`

Maintain a two-column table mapping **math symbols** to **code identifiers** (same names
in equations and arrays). See [math_notation.md](math_notation.md).
