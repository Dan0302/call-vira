import requests
import os

WHISPER_API_URL = "https://api.openai.com/v1/audio/transcriptions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_path: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    with open(file_path, "rb") as audio_file:
        files = {
            "file": (file_path, audio_file, "audio/wav"),
            "model": (None, "whisper-1")
        }
        response = requests.post(WHISPER_API_URL, headers=headers, files=files)

    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        raise Exception(f"Transkription fehlgeschlagen: {response.status_code} – {response.text}")