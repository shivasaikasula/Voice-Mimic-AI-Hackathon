from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# This part lets your website talk to this Python script
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key is now loaded securely from the .env file
MURF_API_KEY = os.getenv("MURF_API_KEY")

@app.post("/generate")
async def generate_audio(text: str = Form(...), voice_id: str = Form(...)):
    if not MURF_API_KEY:
        raise HTTPException(status_code=500, detail="MURF_API_KEY not set in environment variables")

    url = "https://api.murf.ai/v1/speech/generate"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": MURF_API_KEY
    }
    
    data = {
        "voiceId": voice_id,  # Example: "en-US-natalie"
        "text": text,
        "format": "MP3"
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # This returns a link to the audio file
    else:
        raise HTTPException(status_code=400, detail="Murf API Error")
