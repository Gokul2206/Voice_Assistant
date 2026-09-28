# 🎤 Simple Voice Assistant

A lightweight Python voice assistant that listens to voice commands, processes them, and performs simple tasks like telling the time, opening websites, or playing music.

---

## 🚀 Features
- Speech recognition (Google Speech API via `speechrecognition`)
- Text-to-speech responses (`pyttsx3`)
- Commands:
  - Tell time and date
  - Open YouTube or Google
  - Play local music
  - Greetings
  - Exit on "stop"/"quit"

---

## 📂 Project Structure
```
voice_assistant/
│
├── main.py              # Entry point
├── speech_utils.py      # Speech recognition & TTS
├── commands.py          # Command handling
├── config.py            # Configuration (paths, settings)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice_assistant.git
   cd voice_assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the assistant:
   ```bash
   streamlit run main.py
   ```

---

## 🛠️ Configuration
Edit `config.py` to set your music folder path:
```python
MUSIC_FOLDER = "C:/Users/Public/Music"
```

---

## 🎯 Usage
- Say **"time"** → Assistant tells the current time.
- Say **"date"** → Assistant tells today’s date.
- Say **"open YouTube"** → Opens YouTube in browser.
- Say **"open Google"** → Opens Google in browser.
- Say **"play music"** → Plays first song in your music folder.
- Say **"hello"** → Assistant greets you.
- Say **"stop"/"exit"/"quit"** → Ends the assistant.

---

## 📌 Notes
- Requires a working microphone.
- Internet connection needed for speech recognition.
- Tested on Python 3.8+ (Windows).
```