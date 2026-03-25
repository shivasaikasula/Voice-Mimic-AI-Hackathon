const recordBtn = document.getElementById('recordBtn');
const textInput = document.getElementById('textInput');
const fileUpload = document.getElementById('fileUpload');
const player = document.getElementById('player');
const downloadBtn = document.getElementById('downloadBtn');
const resultSection = document.getElementById('result-section');

// --- 1. Speech to Text (Record Feature) ---
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    
    recordBtn.addEventListener('click', () => {
        recognition.start();
        recordBtn.innerText = "Listening...";
    });

    recognition.onresult = (event) => {
        textInput.value = event.results[0][0].transcript;
        recordBtn.innerText = "Record Voice";
    };
}

// --- 2. File Upload (Read Text File) ---
fileUpload.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (event) => {
        textInput.value = event.target.result;
    };
    reader.readAsText(file);
});

// --- 3. Generate Speech via Backend ---
async function makeMeTalk() {
    const text = textInput.value;
    const voice = document.getElementById('voiceId').value;

    if (!text) return alert("Please provide text first!");

    document.querySelector('.generate-btn').innerText = "Generating...";
    
    const formData = new FormData();
    formData.append('text', text);
    formData.append('voice_id', voice);

    try {
        const response = await fetch('http://127.0.0.1:8000/generate', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        if (data.audioFile) {
            player.src = data.audioFile;
            resultSection.style.display = 'block';
            player.play();

            // Setup Download
            downloadBtn.onclick = () => {
                const a = document.createElement('a');
                a.href = data.audioFile;
                a.download = "ai-cloned-voice.mp3";
                a.click();
            };
        }
    } catch (err) {
        alert("Check if your Python backend is running!");
    } finally {
        document.querySelector('.generate-btn').innerText = "✨ Generate AI Voice";
    }
}