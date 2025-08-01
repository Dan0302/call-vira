import openai
import os
from .transcribe_whisper import transcribe_audio
from .tts_response import synthesize_speech
from .intent_supervisor import classify_user_intent
from .load_prompt import load_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

def process_call(audio_file_path: str, customer_config: dict) -> str:
    # Transkription
    transcribed_text = transcribe_audio(audio_file_path)
    intent = classify_user_intent(transcribed_text, customer_config.get('customer_name', 'default'))
    print(f"🔎 Supervisor-Klassifikation: {intent}")

    # GPT-Antwort generieren
    system_prompt = load_prompt('system_prompt.txt', customer_config.get('customer_name', 'default'))
    category = intent.get('category', 'normal_request')
    if category == 'kind':
        system_prompt += ' Sprich langsam und freundlich mit einem Kind.'
    elif category == 'old_or_confused':
        system_prompt += ' Wiederhole ggf. Fragen und achte auf klare, ruhige Sprache.'
    elif category == 'wrong_number':
        system_prompt += ' Weise freundlich darauf hin, dass die Nummer falsch gewählt wurde.'
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcribed_text}
        ]
    )
    reply_text = response.choices[0].message.content.strip()

    # TTS-Ausgabe erzeugen
    voice = customer_config.get("voice", "Vicki")
    output_audio = synthesize_speech(reply_text, voice_id=voice)
    return output_audio