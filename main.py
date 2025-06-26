from audio_recorder import record_audio
from intent_extractor import speech_to_text, extract_intent
from tone_rewriter import rewrite_email
import librosa
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import os

# Load trained model
def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def predict_emotion(file_path):
    model = load_model("emotion_model.h5")
    features = extract_features(file_path).reshape(1, -1)

    # hardcoded label encoder (same as training)
    emotion_labels = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
    prediction = model.predict(features)
    predicted_label = emotion_labels[np.argmax(prediction)]
    print(f" Detected Emotion: {predicted_label}")
    return predicted_label

# Step 1: Record voice
audio_path = record_audio()

# Step 2: Predict emotion
emotion = predict_emotion(audio_path)

# Step 3: Convert voice to text
text = speech_to_text(audio_path)

# Step 4: Get intent (optional)
intent = extract_intent(text)

# Step 5: Rewrite message
if text:
    rewritten = rewrite_email(text, emotion)
    print("\n✉️ Final Rewritten Email:\n")
    print(rewritten)
