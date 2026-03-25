# 🎙️ Voice Mimic AI

> An AI-powered web app that converts your text (or spoken voice) into a cloned AI voice using the **Murf AI API**.
>**[Click here to open](https://voice-mimic-ai-website.vercel.app/)**
---

## 🎥 Demo

> 📹 **[Click here to watch the demo video](https://drive.google.com/file/d/1v1I3czWbYlzWEdmWmb5JmLjUhqAFLBvg/view?usp=sharing)**

---

## 📖 Overview

**Voice Mimic AI** lets users:
- 🗣️ **Type or speak** any text
- 🎭 **Choose an AI voice persona** (Natalie, Marcus, Gabriel)
- 📁 **Upload a `.txt` file** to convert its content to speech
- 🔊 **Generate and play** a realistic AI-cloned voice
- 📥 **Download** the output as an MP3

Built with a **FastAPI** Python backend and a plain **HTML/CSS/JS** frontend. The voice synthesis is powered by the [Murf AI API](https://murf.ai/).

---

## 🛠️ Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python, FastAPI     |
| Voice API | Murf AI             |
| Speech Input | Web Speech API (Browser built-in) |

---

## 🔌 API Usage

This project uses the **[Murf AI Text-to-Speech API](https://murf.ai/resources/docs/)** to generate human-like voice audio from text.

### Endpoint
```
POST https://api.murf.ai/v1/speech/generate
```

### Request Headers
```json
{
  "Content-Type": "application/json",
  "api-key": "YOUR_MURF_API_KEY"
}
```

### Request Body
```json
{
  "voiceId": "en-US-natalie",
  "text": "Hello, this is a voice clone!",
  "format": "MP3"
}
```

### Response
```json
{
  "audioFile": "https://cdn.murf.ai/generated/your-audio-file.mp3"
}
```

### Available Voice IDs
| Voice ID         | Description          |
|------------------|----------------------|
| `en-US-natalie`  | Natalie – Cheerful   |
| `en-US-marcus`   | Marcus – Professional|
| `en-UK-gabriel`  | Gabriel – British    |

The backend in `app.py` forwards the user's text and selected voice to the Murf API and returns the audio URL to the frontend, where it is played and made available for download.

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.8+
- A [Murf AI account](https://murf.ai/) with an API key

### 1. Clone the Repository
```bash
git clone https://github.com/shivasaikasula/Voice-Mimic-AI-Hackathon.git
cd Voice-Mimic-AI-Hackathon
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
```bash
# Copy the example env file
cp .env.example .env
```
Now open `.env` and replace the placeholder with your real Murf API key:
```
MURF_API_KEY=your_actual_murf_api_key_here
```

### 4. Run the Backend Server
```bash
uvicorn app:app --reload
```
The server will start at `http://127.0.0.1:8000`

### 5. Open the Frontend
Simply open `index.html` in your browser (no server needed for frontend).

---

## 🔐 Environment Variables

| Variable       | Description                        |
|----------------|------------------------------------|
| `MURF_API_KEY` | Your Murf AI API key               |

⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`. Only `.env.example` (with a placeholder) is committed to the repo.

---

## 📁 Project Structure

```
Voice-Mimic-AI-Hackathon/
├── app.py              # FastAPI backend — handles Murf API calls
├── index.html          # Main UI
├── style.css           # Styling
├── script.js           # Frontend logic (speech input, API call, playback)
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
├── .gitignore          # Excludes .env and other clutter
└── README.md           # You're reading it!
```

---

## 🏷️ Tags
`murf-ai` `text-to-speech` `voice-cloning` `fastapi` `hackathon`
