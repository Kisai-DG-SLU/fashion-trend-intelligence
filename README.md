# Fashion Trend Intelligence – Projet 2

## Contexte et objectifs

ModeTrends est une agence de conseil en marketing digital spécialisée dans la mode, collaborant avec des marques de luxe et des distributeurs de fast fashion dans plus de 30 pays. Face à l’explosion du marketing d’influence, le projet **“Fashion Trend Intelligence”** vise à :

1. **Segmentation vestimentaire** : identifier et isoler chaque pièce portée par des influenceurs sur Instagram.  
2. **Analyse stylistique** : classifier les pièces par nature, couleur, texture et style.  
3. **Agrégation de tendances** : compiler des milliers de publications pour détecter les tendances émergentes avant leur popularité.  

---

## Ma mission – Projet 2

Dans ce projet, je suis chargé de la **Segmentation vestimentaire**, répartie en quatre volets :

1. **Appel d’un modèle pré-entraîné** : utiliser l’endpoint `sayeed99/segformer_b3_clothes` sur Hugging Face pour traiter un jeu de 50 images annotées et récupérer les masques de segmentation.  
2. **Évaluation des performances** : décoder les masques (RLE ou PNG) et calculer des métriques pixel-wise (IoU, Dice Score, précision), puis présenter un rapport chiffré et des visualisations comparatives.  
3. **Estimation du coût** : en se basant sur les tarifs HF (serverless auto-scale vs endpoint dédié), calculer le coût pour **500 000 images** pendant **30 jours**, et proposer plusieurs scénarios (batch continu, répartition journalière, 24/7).  
4. **Livrables** : notebooks, code source, slides, fiche d’auto‑évaluation et ce README synthétique.  

---

## Étapes du projet

1. **Étape 1 : Initialisation et configuration** :  
   - Mise en place du dépôt Git et du `.gitignore`.  
   - Création de `project_structure.md` décrivant l’arborescence.  
   - Exemple de Notebook de visualisation : `notebooks/00-viz-example.ipynb`.  

2. **Étape 2 : Configuration du token Hugging Face** ✅  
   - Génération d’un token HF avec la portée **Make calls to Inference Providers**.  
   - Stockage dans `.env` et en tant que secret GitHub.  
   - Chargement automatique avec `python-dotenv` et validation via `HfApi().whoami()` et `model_info()`.  

3. **Étape 3 : Préparation du jeu de données** *(à venir)*  

4. **Étape 4 : Script de segmentation via l’API** *(à venir)*  

5. **Étape 5 : Visualisation et analyse des résultats** *(à venir)*  

---

## Structure du dépôt

Pour l’arborescence détaillée, consultez : [project_structure.md](./docs/project_structure.md)

---

## Livrables

Déposez sur la plateforme, dans un dossier zip nommé `Requetez_des_services_IA_Guesdon_Damien`, les fichiers suivants :

| N° | Fichier                                     | Date (mmYYYY) |
| -- | ------------------------------------------- | ------------- |
| 1  | `Guesdon_Damien_1_notebook_072025.ipynb`    | 072025        |
| 2  | `Guesdon_Damien_2_presentation_072025.pptx` | 072025        |

En plus du ZIP, les éléments suivants sont attendus pour le suivi pédagogique :

- **Notebooks** (`.ipynb`) :  
  - `01_setup_env.ipynb` : configuration et test du token HF  
  - `02_segmentation.ipynb` : appel API et calcul des métriques  
  - `03_cost_estimation.ipynb` : estimation du coût HF  
  - `04_visualisation.ipynb` : visuels et analyses graphiques  
- **Code source** : dossier `src/fashion_trend_intelligence/`  
- **Slides** (`.pptx`) basées sur le template fourni  
- **Fiche d’auto-évaluation** complétée  
- **Ce README.md** synthétique  

---

*Notes rédigées par Damien G.*  
