# src/fashion_trend_intelligence/utils.py

from pathlib import Path
from dotenv import load_dotenv
import os

# Charge automatiquement le fichier .env à la racine du dépôt
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env", override=False)

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("La variable HF_TOKEN est introuvable : vérifiez votre fichier .env")
