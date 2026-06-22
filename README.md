# Multimodal Voice & Text Chatbot

A lightweight Flask web app built with **Python** that lets you chat with **Gemini 2.5 Flash** via text or voice — directly from your browser. Backend powered by Python (Flask), frontend is vanilla HTML/JS.

## Features

- 💬 **Text chat** with persistent conversation memory
- 🎙️ **Voice input** — speak into your mic, audio goes straight to Gemini's multimodal API
- 🔊 **Text-to-speech** response playback using the browser's native speech engine
- ⚡ Minimal setup — just a Python backend + a single HTML file

## Project Structure
.

├── bot.py          # Flask backend (chat + voice endpoints)

├── index.html      # Frontend UI (served by Flask)

├── .env            # Your API key 

├── requirements.txt

└── README.md

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Gemini API key**

Create a `.env` file in the root folder:
GEMINI_API_KEY=your_key_here

**4. Run the server**
```bash
python bot.py
```

**5. Open in browser**
http://localhost:5000

## How It Works

- **`/chat`** — Receives a text message, sends it to a persistent Gemini chat session, returns the reply.
- **`/voice`** — Receives a raw WebM audio blob from the browser mic, passes it directly to Gemini's multimodal input, returns the reply as text (then spoken aloud via Web Speech API).

## Requirements

- Python 3.9+
- A valid [Gemini API key](https://aistudio.google.com/app/apikey)

