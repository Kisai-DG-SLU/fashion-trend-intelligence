# Projet\_et\_structure\_initiale

Ce document retrace à la fois l'**historique** des choix initiaux pour configurer l’environnement Poetry et la structure du projet **Fashion Trend Intelligence**, ainsi que la **structure finale** retenue pour organiser le code, les données, les notebooks et la documentation.

---

## 1. Installation et initialisation avec Poetry

### 1.1 Pourquoi Poetry ?

- **Gestion intelligente des dépendances** : évite le « dependency hell » en résolvant automatiquement les sous-dépendances.
- **Environnement isolé** : chaque projet dispose d’un virtualenv dédié, sans interférence avec le système.
- **Format TOML & PEP 621** : `pyproject.toml` standard pour définir métadonnées et dépendances.

### 1.2 Initialisation du projet

```bash
# Installer Poetry (via pipx)
pip install pipx
python3 -m pipx ensurepath
pipx install poetry

# Initialiser le fichier pyproject.toml
poetry init --no-interaction

# Configurer l'environnement virtuel dans le projet
poetry config virtualenvs.in-project true
```

> **Note** : ensuite, `poetry install` installe les dépendances et `poetry shell` active l’environnement.

### 1.3 Dépendances d'exécution (runtime)

Ajouter les bibliothèques nécessaires pour le fonctionnement principal :

- **requests** : envoyer des requêtes HTTP à l’API Hugging Face.
- **python-dotenv** : chargement des variables d’environnement depuis `.env`.
- **huggingface-hub** : client d’inférence serverless pour le modèle SegFormer.
- **transformers**, **torch** : support d’inférence locale et traitement des tenseurs.
- **Pillow** : lecture et manipulation d’images.
- **NumPy** : calculs numériques sur les masques de segmentation.
- **Matplotlib** : création de visualisations et superposition de masques.
- **pycocotools** : calcul de métriques précises (IoU, Dice) sur des masques.

```bash
poetry add \
  requests python-dotenv huggingface-hub transformers torch \
  Pillow numpy matplotlib pycocotools
```

### 1.4 Dépendances de développement (dev)

Installer les outils pour prototypage, tests et qualité de code :

- **jupyterlab**, **ipykernel** : environnements notebook interactifs.
- **pytest** : exécution des tests unitaires.
- **flake8** : linting pour garantir la conformité PEP 8.
- **black** : formatage automatique du code.
- **pre-commit** : hooks Git pour lancer lint et format avant chaque commit.

```bash
poetry add --group dev \
  jupyterlab ipykernel pytest flake8 black pre-commit
```

### 1.5 Packaging et entrypoints

Déclaration des packages et scripts pour usage CLI. Cela **permettra** de lancer facilement les fonctionnalités :

```toml
[tool.poetry]
packages = [ { include = "fashion_trend_intelligence", from = "src" } ]

[tool.poetry.scripts]
segment       = "fashion_trend_intelligence.segmentation:main"
evaluate_cost = "fashion_trend_intelligence.cost_estimator:main"
viz           = "fashion_trend_intelligence.visualization:main"
```

> **À venir** : implémentation des scripts et tests d’intégration CI.

---

## 2. Architecture et structure finale du projet

```
fashion-trend-intelligence/
├── LICENSE
├── README.md                                  # Présentation du projet et instructions de démarrage
├── .gitignore                                 # Fichiers et dossiers ignorés par Git
├── .env.example                               # Modèle de configuration des variables d'environnement
├── .python-version                            # Version Python utilisée
├── pyproject.toml                             # Configuration Poetry et métadonnées du projet
├── poetry.lock                                # Verrou des versions des dépendances
│
├── docs/                                      # Documentation et supports
│   ├── fiche_auto_evaluation.pdf
│   ├── project_structure.md                   # Historique et guide initial de la structure
│   └── support_presentation_ModeTrends.pptx
│
├── data/                                      # Données du projet
│   ├── control/                               # Données générées de contrôle pour référence après train
│   ├── raw/                                   # Données brutes immuables
│   │   ├── annotations/                       # Masks (annotations ground-truth)
│   │   └── images/                            # Photos d’influenceurs
│   └── processed/                             # Données transformées (générées via scripts)
│       └── masks_colorized/                   # Masques segmentés générés colorisés
│
├── notebooks/                                 # Notebooks Jupyter pour chaque étape
│   ├── 00_huggingface_api_cloth_seg.ipynb     # Exemple appel API HuggingFace pour la segmentation
│   ├── 00_viz-example.ipynb                   # Exemple de visualisation
│   ├── 01_setup_env.ipynb                     # Configuration & test du token HF
│   ├── 02_segmentation.ipynb                  # Appel API & calcul de métriques
│   ├── 03_cost_estimation.ipynb               # Estimation du coût HF
│   └── 04_visualisation.ipynb                 # Visuels et analyses graphiques
│
├── src/                                       # Code source du package réutilisable
│   └── fashion_trend_intelligence/
│       ├── __init__.py
│       ├── config.py                          # Variables centralisées du projet
│       ├── cost_estimation.py                 # Estimation du coût d’inférence pour un volume d’images
│       ├── segmentation.py                    # Appelle le modèle et génère les masks
│       ├── utils.py                           # Fonctions utilitaires (ex. chargement variables environnement)
│       └── visualization.py                   # Génère et sauvegarde les visuels de segmentation
│
├── tests/                                     # Tests unitaires pour chaque module
│   ├── test_cost_estimation.py
│   ├── test_segmentation.py
│   └── test_visualization.py
│
└── .github/                                   # Configuration GitHub Actions
    └── workflows/
        └── ci.yml                             # CI : macos-latest, Python 3.13.2, Poetry, Black, flake8, pytest
```

### 2.1 Détail des choix et usages

- **docs/** : centralise toute la documentation hors code et facilite la revue.
- **data/raw** vs **data/processed** : préserve les données originales et trace les transformations.
- **notebooks/** : jalons pédagogiques et prototypage rapide avant industrialisation du code.
- **src/** : API Python stable, prête à être packagée et réutilisée via CLI ou intégration.
- **tests/** : valident les fonctions clés et garantissent la qualité du code (TDD).
- **CLI scripts (entrypoints)** : interface simple pour lancer segmentation, estimation de coût et visualisation.
- **CI** : assure la conformité du code (lint, format), la validité des tests et l’installation isolée via Poetry.

### 2.2 Choix SMART

- **Spécifique** : répartition claire des responsabilités entre dossiers et modules.
- **Mesurable** : indicateurs automatisés via tests, lint et CI.
- **Atteignable** : placeholders et templates créés, scripts à implémenter.
- **Réalisable** : technologies standard (Poetry, Hugging Face, pytest).
- **Temporel** : progression notebook par notebook pour décomposer le travail.

---

Ce document permettra à mon mentor de comprendre l’historique des choix, l’architecture cible et la feuille de route pour la suite du projet.

