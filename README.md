# 🤖 Machine Learning Bootcamp

> **A complete, hands-on Machine Learning course designed for the YouTube channel — from zero to hero.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📺 About This Bootcamp

This bootcamp is a structured, beginner-friendly Machine Learning course delivered as a YouTube series.
Every module corresponds to one or more YouTube episodes and contains:

- **Concept explanations** with clean, commented code
- **Hands-on Jupyter notebooks** you can run locally or on Google Colab
- **Real-world datasets** and practical exercises
- **Exercises** at the end of each notebook to solidify understanding

---

## 🗂️ Curriculum

| Module | Topic | Notebooks |
|--------|-------|-----------|
| 01 | [Introduction to Machine Learning](Module_01_Introduction/) | `01_what_is_ml.ipynb`, `02_types_of_ml.ipynb` |
| 02 | [Python Libraries for ML](Module_02_Python_Libraries/) | `01_numpy.ipynb`, `02_pandas.ipynb`, `03_matplotlib_seaborn.ipynb` |
| 03 | [Data Preprocessing](Module_03_Data_Preprocessing/) | `01_data_preprocessing.ipynb` |
| 04 | [Supervised Learning – Regression](Module_04_Regression/) | `01_linear_regression.ipynb`, `02_polynomial_regression.ipynb`, `03_regularization.ipynb` |
| 05 | [Supervised Learning – Classification](Module_05_Classification/) | `01_logistic_regression.ipynb`, `02_knn.ipynb`, `03_decision_trees.ipynb`, `04_random_forest.ipynb`, `05_svm.ipynb` |
| 06 | [Model Evaluation & Validation](Module_06_Model_Evaluation/) | `01_model_evaluation.ipynb` |
| 07 | [Unsupervised Learning](Module_07_Unsupervised_Learning/) | `01_kmeans.ipynb`, `02_pca.ipynb` |
| 08 | [Neural Networks & Deep Learning](Module_08_Neural_Networks/) | `01_neural_networks_intro.ipynb`, `02_keras_basics.ipynb` |
| 09 | [Hyperparameter Tuning & Pipelines](Module_09_Hyperparameter_Tuning/) | `01_hyperparameter_tuning.ipynb`, `02_pipelines.ipynb` |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nabin2004/Machine-Learning-Bootcamp.git
cd Machine-Learning-Bootcamp
```

### 2. Set up the environment

**Option A – pip (recommended for beginners)**

```bash
pip install -r requirements.txt
```

**Option B – conda**

```bash
conda env create -f environment.yml
conda activate ml-bootcamp
```

### 3. Launch Jupyter

```bash
jupyter notebook
```

Or open any `.ipynb` directly in **VS Code**, **JupyterLab**, or **Google Colab**.

---

## ☁️ Run on Google Colab

Each notebook contains a **"Open in Colab"** badge at the top so you can run it instantly in your browser without any local setup.

---

## 📦 Requirements

See [`requirements.txt`](requirements.txt) for the full list. Core dependencies:

| Library | Purpose |
|---------|---------|
| `numpy` | Numerical computing |
| `pandas` | Data manipulation |
| `matplotlib` | Plotting |
| `seaborn` | Statistical visualization |
| `scikit-learn` | ML algorithms & utilities |
| `tensorflow` / `keras` | Deep learning |
| `jupyter` | Interactive notebooks |

---

## 📁 Repository Structure

```
Machine-Learning-Bootcamp/
├── README.md
├── requirements.txt
├── environment.yml
├── datasets/                        # Shared datasets used across modules
├── Module_01_Introduction/
├── Module_02_Python_Libraries/
├── Module_03_Data_Preprocessing/
├── Module_04_Regression/
├── Module_05_Classification/
├── Module_06_Model_Evaluation/
├── Module_07_Unsupervised_Learning/
├── Module_08_Neural_Networks/
└── Module_09_Hyperparameter_Tuning/
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request for:
- Bug fixes in notebooks
- Additional exercises or examples
- New module suggestions

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [scikit-learn documentation](https://scikit-learn.org)
- [TensorFlow / Keras documentation](https://keras.io)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- The amazing ML community 🌍

---

> ⭐ If you find this helpful, **star the repo** and **subscribe to the YouTube channel**!
