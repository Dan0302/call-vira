from flask import Response

def generate_twiml_response(call_data):
    # Platzhalter: Begrüßungsausgabe
    say_text = "Willkommen bei Call-VIRA. Bitte sprechen Sie nach dem Signal."
    response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Vicki" language="de-DE">{say_text}</Say>
    <Record maxLength="30" action="/webhook/transcribe" method="POST" />
</Response>"""
    return Response(response, mimetype='text/xml')