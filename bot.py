import os
from flask import Flask, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv; load_dotenv()

# Configures Flask to look for index.html in the same directory
app = Flask(__name__, template_folder='.', static_folder='.')

# 1. Initialize Gemini Client
# Make sure your environment variable is set: export GEMINI_API_KEY="your-key"
if "GEMINI_API_KEY" not in os.environ:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client()
# Create a persistent chat session to maintain conversation context
chat = client.chats.create(model="gemini-2.5-flash")

@app.route('/')
def index():
    """Serves the frontend interface file directly from the root folder."""
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: index.html not found in the current directory.", 404

@app.route('/chat', methods=['POST'])
def handle_chat():
    """Handles standard text incoming from the left sidebar panel."""
    data = request.json or {}
    user_message = data.get("message", "").strip()
    
    if not user_message:
        return jsonify({"error": "Empty message string"}), 400
    
    try:
        response = chat.send_message(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/voice', methods=['POST'])
def handle_voice():
    """Receives binary audio streams directly from the web browser's microphone."""
    if 'audio' not in request.files:
        return jsonify({"error": "No audio data found in payload"}), 400
    
    audio_file = request.files['audio']
    audio_bytes = audio_file.read()
    
    try:
        # Pass the raw WebM/Ogg audio directly to Gemini 2.5 Flash's multimodal framework
        response = chat.send_message(
            message=[
                types.Part.from_bytes(
                    data=audio_bytes,
                    mime_type="audio/webm",
                ),
                "The user spoke this audio query to you. Please synthesize a direct, highly conversational response.",
            ]
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start local development server
    app.run(debug=True, port=5000)