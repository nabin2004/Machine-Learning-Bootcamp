# Getting started

## Requirements

- Python **3.11** (see [`.python-version`](../.python-version))
- A C compiler toolchain may be required for some wheels (e.g. `xgboost`, `lightgbm`) on Linux/macOS.

## Create the environment

From the repository root:

```bash
make setup
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

This creates `.venv/`, installs pinned dependencies from `requirements.txt`, and installs
`common` and `bootcamp_manim` in editable mode (`pip install -e .`).

## JupyterLab + RISE

```bash
make lab
```

Open any episode notebook under a phase folder or `ep00_bottom_up/`. For slideshow-style
intuition decks, see [rise_guide.md](rise_guide.md).

## Tests and notebooks (CI parity)

```bash
make test-all      # ruff + nbmake (all episode notebooks execute)
make test EP=phase_1_classical_ml/ep01_linear_regression   # nbmake for one episode tree
```

## Manim

See [manim_guide.md](manim_guide.md). Quick render for one episode:

```bash
make video EP=phase_1_classical_ml/ep01_linear_regression
```

## Authoring a new episode

```bash
make new-ep NAME=ep41_custom_topic PHASE=phase_2_deep_learning
```

See [episode_template.md](episode_template.md).
