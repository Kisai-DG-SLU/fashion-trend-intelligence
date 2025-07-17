# src/fashion_trend_intelligence/config.py
import os
from dotenv import load_dotenv

# Charge les variables d'environnement depuis .env
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("❌ Le token HF n'est pas défini dans .env")
