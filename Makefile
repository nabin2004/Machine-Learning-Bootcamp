.PHONY: setup lab test test-all slides video new-ep lint format normalize-nb

PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python
JUPYTER := $(VENV)/bin/jupyter
MANIM := $(VENV)/bin/manim

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -U pip wheel
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

lab:
	$(JUPYTER) lab --notebook-dir=.

test:
	@test -n "$(EP)" || (echo "Usage: make test EP=phase_1_classical_ml/ep01_linear_regression" && exit 1)
	$(VENV)/bin/pytest --nbmake "$(EP)" --ignore-glob='**/tests/**'

test-all: lint
	$(VENV)/bin/pytest --nbmake ep00_bottom_up phase_1_classical_ml phase_2_deep_learning phase_3_scaling phase_4_capstones --ignore-glob='**/tests/**'

lint:
	$(VENV)/bin/ruff check common bootcamp_manim scripts
	$(VENV)/bin/ruff format --check common bootcamp_manim scripts

format:
	$(VENV)/bin/ruff format common bootcamp_manim scripts
	$(VENV)/bin/black common bootcamp_manim scripts

normalize-nb:
	$(PY) scripts/normalize_notebooks.py .

slides:
	@test -n "$(EP)" || (echo "Usage: make slides EP=phase_1_classical_ml/ep01_linear_regression" && exit 1)
	$(VENV)/bin/jupyter nbconvert --to slides "$(EP)/01_intuition.ipynb" --reveal-prefix=https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0

video:
	@test -n "$(EP)" || (echo "Usage: make video EP=phase_1_classical_ml/ep01_linear_regression" && exit 1)
	cd "$(EP)/videos" && $(MANIM) -ql scene.py

new-ep:
	@test -n "$(NAME)" || (echo "Usage: make new-ep NAME=ep41_foo PHASE=phase_2_deep_learning" && exit 1)
	@test -n "$(PHASE)" || (echo "Usage: make new-ep NAME=ep41_foo PHASE=phase_2_deep_learning" && exit 1)
	$(PY) scripts/new_episode.py --name "$(NAME)" --phase "$(PHASE)"
