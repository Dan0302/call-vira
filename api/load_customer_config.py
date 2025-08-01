import json
from pathlib import Path

CONFIG_DIR = Path(__file__).parent.parent / "config"

def load_customer_config(customer_id: str = None) -> dict:
    if customer_id:
        customer_file = CONFIG_DIR / f"{customer_id}.json"
        if customer_file.exists():
            with open(customer_file, "r", encoding="utf-8") as f:
                return json.load(f)

    # Fallback auf Default
    default_file = CONFIG_DIR / "default_settings.json"
    if default_file.exists():
        with open(default_file, "r", encoding="utf-8") as f:
            return json.load(f)

    raise FileNotFoundError("Keine passende Konfigurationsdatei gefunden.")