🎙️ Speech Pace & Clarity Analyzer

A Python Flask web application for analyzing measurable characteristics of a speech/audio recording. This project is developed for a Text and Speech Analysis course and demonstrates server-side audio processing using Python.

🎯 Objective

The objective is to build a speech-analysis application that receives an audio file through a web interface and uses a Python backend to extract basic acoustic properties.

The application demonstrates:

- Audio file upload
- Python-based WAV processing
- Speech/audio duration analysis
- Sample-rate detection
- Channel detection
- Peak amplitude measurement
- RMS energy measurement
- A simple clarity index
- Interactive waveform-style visualization

✨ Features

- Modern audio-studio interface
- Upload and preview a WAV recording
- Play/pause uploaded audio
- Python Flask backend
- Server-side audio analysis
- Automatic analysis report
- Responsive mobile-friendly design
- No database required
- GitHub-ready source code

🧠 How It Works

1. The user selects a WAV audio recording.
2. JavaScript sends the audio file to the "/analyze" Flask endpoint.
3. "app.py" temporarily stores the uploaded file.
4. Python reads the WAV metadata and PCM audio samples.
5. The backend calculates:
   - Duration
   - Sample rate
   - Number of channels
   - Peak amplitude
   - RMS energy
   - A simple clarity index
6. The results are returned as JSON.
7. JavaScript displays the analysis report.

🔬 Analysis Method

The application uses measurable audio characteristics instead of claiming to identify a person's actual emotion or psychological state.

RMS Energy

RMS energy provides an estimate of the overall signal strength.

Peak Amplitude

Peak amplitude indicates the highest measured signal level in the recording.

Clarity Index

The project combines signal-energy characteristics into a simple 0–100 educational index.

It should not be considered a medical, psychological, or professional speech diagnosis.

🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- WAV/PCM audio processing

📁 Project Structure

05-Speech-Pace-Clarity-Analyzer/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md

▶️ How to Run Locally

Step 1 — Install Python

Make sure Python 3 is installed.

Step 2 — Install dependencies

pip install -r requirements.txt

Step 3 — Run the Flask application

python app.py

Step 4 — Open the application

Open the following address in your browser:

http://127.0.0.1:5000

🎧 Supported Audio

The current lightweight version directly analyzes PCM WAV files.

MP3 and M4A support can be added later using FFmpeg or additional audio-processing libraries.

📚 Academic Relevance

This project demonstrates concepts related to Text and Speech Analysis:

- Speech signal handling
- Acoustic feature extraction
- Audio metadata analysis
- Signal energy
- Audio amplitude
- Web-based speech processing
- Client-server architecture
- Python-based backend processing

🚀 Future Improvements

- Add speech-to-text using an ASR model
- Calculate estimated words per minute
- Detect pauses and silence segments
- Add pitch and frequency analysis
- Add spectrogram visualization
- Support MP3 and M4A
- Add downloadable analysis reports
- Store previous analysis sessions

⚠️ Limitation

The clarity index is an educational signal-based measure. It does not determine actual speaking quality, emotions, health conditions, or psychological state.

📌 Project Information

Project: Speech Pace & Clarity Analyzer
Course: Text and Speech Analysis
Backend: Python Flask
Frontend: HTML, CSS, JavaScript
Project Type: Speech Analysis Web Application
