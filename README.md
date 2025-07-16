# Fashion Trend Intelligence – Projet 2

## Contexte et objectifs

ModeTrends est une agence de conseil en marketing digital spécialisée dans la mode, collaborant avec des marques de luxe et des distributeurs de fast fashion dans plus de 30 pays. Face à l’explosion du marketing d’influence, le projet **“Fashion Trend Intelligence”** vise à :

1. **Segmentation vestimentaire**
   Identifier et isoler chaque pièce portée par des influenceurs sur Instagram.
2. **Analyse stylistique**
   Classifier les pièces par nature, couleur, texture et style.
3. **Agrégation de tendances**
   Compiler des milliers de publications pour détecter les tendances émergentes avant leur popularité.

---

## Ma mission – Projet 2

Ma responsabilité porte sur la **Segmentation vestimentaire**, selon quatre volets :

1. **Tester un modèle pré-entraîné**
   - Appeler l’endpoint serverless Hugging Face : `sayeed99/segformer_b3_clothes`.
   - Traiter un jeu de 50 images annotées pour récupérer les masques de segmentation.

2. **Évaluer mes performances**
   - Décoder les masques (RLE ou PNG).
   - Calculer des métriques pixel-wise : IoU, Dice Score, précision.
   - Présenter un rapport chiffré et des visualisations comparaison (original vs prédiction).

3. **Estimer le coût**
   - À partir des tarifs HF (serverless auto-scale vs endpoint dédié).
   - Calculer le coût pour **500 000 images** sur **30 jours**.
   - Proposer plusieurs scénarios (batch continu, répartition journalière, 24/7).

4. **Livrables**
   - **Notebooks**
     - `01_setup_env.ipynb` : configuration & test du token HF
     - `02_segmentation.ipynb` : appel API & calcul de métriques
     - `03_visualisation.ipynb` : visuels et analyses graphiques
   - **Code source** dans `src/fashion_trend_intelligence/`
   - **Slides** basées sur le template fourni
   - **Fiche d’auto-évaluation** complétée
   - **Ce README.md** synthétique

---

## Structure du dépôt

```
fashion-trend-intelligence/
├── .venv/                                # environnement Poetry
├── pyproject.toml & poetry.lock         # configuration et lock des versions
├── README.md                            # présentation du projet
├── environnement_poetry.md              # mes notes de configuration Poetry
├── data/
│   ├── images/                          # 50 images de test
│   └── annotations/                     # masques ground-truth
├── notebooks/
│   ├── 01_setup_env.ipynb
│   ├── 02_segmentation.ipynb
│   └── 03_visualisation.ipynb
├── src/
│   └── fashion_trend_intelligence/
│       ├── __init__.py
│       ├── segmentation.py              # fonctions segmentation & métriques
│       ├── cost_estimator.py            # calcul du coût HF
│       └── visualization.py             # helpers plotting
├── results/
│   ├── masks_pred/                      # masques générés
│   └── metrics.csv                      # IoU/Dice par image
├── slides/
│   └── mode_trends_template.pptx
└── docs/
    └── autoeval.md                      # fiche d’auto-évaluation
```

---

## Mise en place et installation

1. **Prérequis**
   - Python ≥ 3.9
   - Compte & token Hugging Face (portée “Inference Providers”)
   - Git, éditeur de code (VS Code, PyCharm…)

2. **Installer les dépendances**
   ```bash
   poetry install
   ```

3. **Activer l’environnement**
   ```bash
   poetry shell
   ```

4. **Vérifier l’import du package**
   ```bash
   python - << 'EOF'
   import fashion_trend_intelligence
   print("Import OK :", fashion_trend_intelligence.__file__)
   EOF
   ```

---

## Commandes rapides

- **Segmentation**
  ```bash
  poetry run segment --input data/images/img1.jpg \
                    --output results/masks_pred/img1_mask.png
  ```

- **Estimation du coût**
  ```bash
  poetry run evaluate_cost --images 500000 --days 30
  ```

- **Visualisation**
  ```bash
  poetry run viz --image data/images/img1.jpg \
                 --mask results/masks_pred/img1_mask.png
  ```

---

## Étapes suivantes

- Tester et valider mes notebooks.
- Compléter mes slides avec mes visualisations.
- Préparer la session de revue avec mon mentor.

*Notes rédigées par Damien G.*
