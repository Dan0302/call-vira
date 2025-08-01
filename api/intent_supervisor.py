import openai
import os
from .load_prompt import load_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_user_intent(transcribed_text: str, customer_id: str = "default") -> dict:
    prompt = load_prompt("supervisor_prompt.txt", customer_id)
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": transcribed_text}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3
    )

    try:
        classification = response.choices[0].message.content.strip()
        return {"category": classification}
    except Exception as e:
        return {"category": "unclassified", "error": str(e)}