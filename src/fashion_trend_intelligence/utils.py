# src/fashion_trend_intelligence/utils.py

import os
from pathlib import Path

def get_hf_token():
    """
    Récupère le token Hugging Face à utiliser :
    - Priorité 1 : variable d'environnement HF_TOKEN (Colab, CI, export manual)
    - Priorité 2 : fichier .env à la racine du projet (local)
    - Sinon, lève une erreur explicite
    """
    token = os.environ.get("HF_TOKEN")
    if token and token.startswith("hf_"):
        return token

    try:
        from dotenv import load_dotenv
        env_path = Path(__file__).resolve().parents[1] / ".env"
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
            token = os.environ.get("HF_TOKEN")
            if token and token.startswith("hf_"):
                return token
    except Exception:
        pass

    raise RuntimeError(
        "Le token Hugging Face est introuvable. "
        "Définis la variable d'environnement HF_TOKEN (Colab/CI/Cloud) "
        "ou crée une fichier .env à la racine du projet."
    )

# Chargement automatique à l'import
HF_TOKEN = get_hf_token()
