# Project Title
This project demonstrates an AI assistant with WhatsApp integration for context-aware responses using Twilio and a fine-tuned Llama model.

## Features
- Real-time WhatsApp message processing
- Context-aware responses
- Flask API for predictions

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables:
   ```bash
   export TWILIO_ACCOUNT_SID="your_account_sid"
   export TWILIO_AUTH_TOKEN="your_auth_token"
   export TWILIO_NUMBER="your_twilio_number"
   ```
4. Run the application:
   ```bash
   python api.py
   ```

## Usage
- Send messages via WhatsApp to interact with the assistant.
- Use the `/predict` endpoint for API-based predictions.

## File Structure
- `api.py`: Defines API routes.
- `model.py`: Handles model inference.
- `utils.py`: Includes utility functions.
- `config.py`: Configuration settings.
- `requirements.txt`: Python dependencies.
- `README.md`: Project overview and instructions.
