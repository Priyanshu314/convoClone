from flask import Flask, request, jsonify
from twilio.rest import Client
import os
from model import get_assistant_response

app = Flask(__name__)

# Twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
twilio_client = Client(account_sid, auth_token)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        user_message = data['user_message']
        response = get_assistant_response(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/whatsapp', methods=['POST'])
def reply_whatsapp():
    incoming_msg = request.form.get('Body', '')
    from_number = request.form.get('From')

    response_text = get_assistant_response(incoming_msg)
    twilio_client.messages.create(
        body=response_text,
        from_=f'whatsapp:{twilio_number}',
        to=from_number
    )
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
