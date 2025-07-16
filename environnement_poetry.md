# environnement_poetry.md

## 1. Pourquoi Poetry ?
- **Gestion intelligente des dépendances**  
  Évite le “dependency hell” en résolvant automatiquement les sous-dépendances.  
- **Environnements isolés**  
  Crée un venv par projet, sans polluer le Python global.  
- **PEP 621 & TOML**  
  Fichier `pyproject.toml` clair et standard pour toutes les métadonnées.

---

## 2. Initialisation du projet

```bash
# 1. Créer et entrer dans le dossier
mkdir fashion-trend-intelligence && cd fashion-trend-intelligence

# 2. Installer Poetry (via pipx)
pip install pipx
python3 -m pipx ensurepath
pipx install poetry

# 3. Initialiser pyproject.toml minimal
poetry init --no-interaction

# 4. Activer venv local dans .venv/
poetry config virtualenvs.in-project true
```

> **Raison** : projet propre, reproductible, facile à partager.

---

## 3. Dépendances d’exécution (runtime)

```bash
poetry add   requests        # appels HTTP vers HF Inference API  
  pillow          # chargement et pré-traitement d’images  
  numpy           # calculs numériques  
  matplotlib      # visualisations  
  pycocotools     # décodage RLE (COCO masks)  
  python-dotenv   # variables d’environnement (.env)  
  transformers    # inférence locale SegFormer  
  torch           # backend PyTorch pour transformers  
  huggingface-hub # client Inference Providers HF  
```

> **Pourquoi ces choix** :  
> - **requests** pour communiquer avec HF  
> - **Pillow/Numpy/Matplotlib** pour charger, traiter et afficher les images  
> - **pycocotools** pour décoder les masques au format RLE  
> - **transformers/torch** pour inférence locale (optionnel)  
> - **huggingface-hub** pour un accès serverless unifié

---

## 4. Dépendances de développement (dev)

```bash
poetry add --group dev   jupyterlab   # notebooks interactifs  
  ipykernel    # kernel Python dans Jupyter  
  pytest       # tests unitaires  
  flake8       # linting  
  black        # formatage automatique  
  pre-commit   # hooks Git  
```

> **Pourquoi ces outils** :  
> - Garantir un code propre et testé.  
> - Faciliter la collaboration (hooks, notebooks partagés).

---

## 5. Structure du projet

```
fashion-trend-intelligence/
├── .venv/                       
├── pyproject.toml               
├── poetry.lock                 
├── README.md  
├── .gitignore  
└── src/
    └── fashion_trend_intelligence/
        ├── __init__.py  
        ├── segmentation.py  
        ├── cost_estimator.py  
        └── visualization.py  
```

- **src/** : code packagé  
- **.gitignore** : ignore `.venv/`, `.env`, `__pycache__/`, etc.

---

## 6. Packaging & entrypoints

Dans `pyproject.toml` :

```toml
[tool.poetry]
packages = [
  { include = "fashion_trend_intelligence", from = "src" }
]

[tool.poetry.scripts]
segment       = "fashion_trend_intelligence.segmentation:main"
evaluate_cost = "fashion_trend_intelligence.cost_estimator:main"
viz           = "fashion_trend_intelligence.visualization:main"
```

- **Entrypoints** : commandes CLI `poetry run segment …`  
- **Packaging** : `poetry build` → `.whl` partageable

---

## 7. Installation & vérification

```bash
# Installer tout (runtime + dev + code)
poetry install

# Entrer dans l’environnement isolé
poetry shell

# Vérifier l’import du package
python - << 'EOF'
import fashion_trend_intelligence
print("OK :", fashion_trend_intelligence.__file__)
EOF

# Tester un entrypoint
poetry run segment --help
```

> Tu es maintenant prêt·e pour :  
> - tester le token HF  
> - appeler et évaluer SegFormer-clothes  
> - calculer métriques & coûts  
> - préparer notebooks et slides pour ton mentor.

---
*Notes rédigées par Damien G.*  
