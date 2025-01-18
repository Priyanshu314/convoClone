import os

# Twilio Credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

# Model Configurations
MODEL_NAME = "unsloth/Llama-3.2-3B-Instruct"
