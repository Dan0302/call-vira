import json
from pathlib import Path

def create_customer_settings(customer_id: str, overrides: dict = None):
    config_path = Path(__file__).parent.parent / "config" / f"{customer_id}.json"
    default_settings_path = Path(__file__).parent.parent / "config" / "default_settings.json"

    # Lade die Default-Einstellungen
    with open(default_settings_path, "r", encoding="utf-8") as f:
        default_settings = json.load(f)

    # Falls overrides übergeben wurden, diese anwenden
    if overrides:
        default_settings.update(overrides)

    # Speichere die neue Konfigurationsdatei
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(default_settings, f, indent=2)

    print(f"Kundenkonfiguration für '{customer_id}' erfolgreich erstellt unter: {config_path}")
    return config_path

# Beispielhafte Nutzung:
if __name__ == "__main__":
    create_customer_settings("call-vira-demo")