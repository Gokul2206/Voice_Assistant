import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

def speak(text):
    """Reinit engine each call — avoids pyttsx3 stale loop bug."""
    print("🔊 Speaking:", text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen(duration=5, samplerate=16000):
    audio_data = sd.rec(int(duration * samplerate),
                        samplerate=samplerate,
                        channels=1,
                        dtype='int16')
    sd.wait()

    if np.max(np.abs(audio_data)) > 0:
        audio_data = np.int16(audio_data / np.max(np.abs(audio_data)) * 32767)

    audio_bytes = audio_data.tobytes()
    audio = sr.AudioData(audio_bytes, samplerate, 2)

    try:
        return recognizer.recognize_google(audio).lower()
    except (sr.UnknownValueError, sr.RequestError):
        return ""