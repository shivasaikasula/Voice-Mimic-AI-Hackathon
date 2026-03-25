from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# This part lets your website talk to this Python script
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# PASTE YOUR KEY HERE
MURF_API_KEY = "ap2_22fd3ae3-193e-4bce-a4c5-54031373a434"

@app.post("/generate")
async def generate_audio(text: str = Form(...), voice_id: str = Form(...)):
    url = "https://api.murf.ai/v1/speech/generate"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": MURF_API_KEY
    }
    
    data = {
        "voiceId": voice_id, # Example: "en-US-natalie"
        "text": text,
        "format": "MP3"
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json() # This returns a link to the audio file
    else:
        raise HTTPException(status_code=400, detail="Murf API Error")