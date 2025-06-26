import speech_recognition as sr
from textblob import TextBlob
import nltk
nltk.download('punkt')

def speech_to_text(audio_file='user_voice.wav'):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ Transcribed Text: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return None
    except sr.RequestError:
        print("⚠️ Error with speech recognition service.")
        return None

def extract_intent(text):
    blob = TextBlob(text)
    keywords = blob.noun_phrases
    print(f"🔍 Extracted Intent Keywords: {keywords}")
    return keywords if keywords else ["general"]
