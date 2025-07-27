# src/fashion_trend_intelligence/utils.py

import os
from pathlib import Path
from dotenv import load_dotenv

def get_hf_token():
    env_path = Path(__file__).resolve().parents[2] / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        token = os.environ.get("HF_TOKEN")
        if token and token.startswith("hf_"):
            return token
    raise RuntimeError(
        "Le token Hugging Face est introuvable dans le fichier .env à la racine du projet."
    )
HF_TOKEN = get_hf_token()
