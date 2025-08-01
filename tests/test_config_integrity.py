import json
from pathlib import Path

def test_config_and_prompts():
    base = Path(__file__).parent.parent
    config_path = base / "config" / "call-vira-demo.json"
    prompts_dir = base / "prompts"
    prompt_files = [
        "welcome_prompt.txt",
        "fallback_prompt.txt",
        "goodbye_prompt.txt",
        "error_prompt.txt",
        "slow_response_prompt.txt"
    ]

    assert config_path.exists(), "Konfigurationsdatei fehlt: call-vira-demo.json"
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        assert "customer_name" in config, "customer_name fehlt in Konfiguration"
        assert config["logo_url"].startswith("/static/"), "Logo-Pfad ungültig"

    for file in prompt_files:
        path = prompts_dir / file
        assert path.exists(), f"Prompt-Datei fehlt: {file}"
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            assert len(content) > 0, f"Prompt-Datei leer: {file}"

    print("✅ Konfiguration und Prompts vollständig und korrekt.")

if __name__ == "__main__":
    test_config_and_prompts()