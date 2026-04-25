# Machine Learning Bootcamp

A **Karpathy-style** bootcamp over the full ML → deep learning → modern training → capstones arc. Each episode follows the same **four-act** structure: Intuition → Library run → From scratch → Limits.

- **Curriculum index**: [CURRICULUM.md](CURRICULUM.md)  
- **Teaching principles**: [PHILOSOPHY.md](PHILOSOPHY.md)  
- **Setup**: [docs/getting_started.md](docs/getting_started.md)

## Quickstart

```bash
make setup          # create .venv and install deps
source .venv/bin/activate
make lab            # JupyterLab (RISE for slideshows)
make test-all       # ruff + nbmake (notebooks execute cleanly)
```

## Repository layout

| Path | Role |
|------|------|
| `ep00_bottom_up/` | Episode 0: NumPy, broadcasting, einsum, seeds, profiling |
| `phase_1_classical_ml/` … `phase_4_capstones/` | Episodes 1–40 by theme |
| `common/` | Shared utilities: seeds, toy data, plotting, small comparison helpers |
| `bootcamp_manim/` | Shared Manim style + reusable scenes (does **not** replace the `manim` PyPI package) |
| `templates/episode_template/` | Copy this to author a new episode (`make new-ep`) |

## Episode anatomy

Each episode folder contains:

- `01_intuition.ipynb` — RISE-ready, conceptual  
- `02_library_run.ipynb` — library API, minimal code  
- `03_from_scratch.ipynb` — NumPy or raw autograd  
- `04_limits.ipynb` — failure cases and constraints  
- `scratch/core.py` — importable implementation  
- `videos/scene.py` — Manim scene stub  
- `notes.md` — notation ↔ code variable table  

## Makefile cheatsheet

```bash
make new-ep NAME=ep41_foo PHASE=phase_2_deep_learning
make test EP=phase_1_classical_ml/ep01_linear_regression
make slides EP=phase_1_classical_ml/ep01_linear_regression
make video EP=phase_1_classical_ml/ep01_linear_regression
```

## License

[MIT](LICENSE)
