from pathlib import Path

PROMPT_DIR = Path(__file__).parent.parent / "prompts"

def load_prompt(prompt_name: str, customer_id: str = "default") -> str:
    # Versuche mandantenspezifischen Prompt
    custom_path = PROMPT_DIR / customer_id / prompt_name
    if custom_path.exists():
        return custom_path.read_text(encoding="utf-8").strip()

    # Fallback auf Standard
    fallback_path = PROMPT_DIR / "default" / prompt_name
    if fallback_path.exists():
        return fallback_path.read_text(encoding="utf-8").strip()

    raise FileNotFoundError(f"Prompt '{prompt_name}' nicht gefunden für Kunde '{customer_id}'.")