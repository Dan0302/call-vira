from flask import Flask, request
from .twiml_call import generate_twiml_response
from .load_customer_config import load_customer_config
import logging

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def extract_customer_id(data):
    return data.get('To', '').split('@')[0].replace('+', '').lower() or 'default'

def handle_call():
    try:
        call_data = request.form.to_dict()
        customer_id = extract_customer_id(call_data)
        customer_config = load_customer_config(customer_id)
        print("📞 Eingehender Anruf:", call_data)
        response_xml = generate_twiml_response(call_data)
        return response_xml, 200, {"Content-Type": "text/xml"}
    except Exception as e:
        logging.exception("Fehler im Webhook:")
        return "<Response><Say>Ein Fehler ist aufgetreten.</Say></Response>", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
