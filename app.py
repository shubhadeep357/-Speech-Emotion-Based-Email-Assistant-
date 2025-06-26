import streamlit as st
from audio_recorder import record_audio
from intent_extractor import speech_to_text, extract_intent
from tone_rewriter import rewrite_email
from emotion_classifier import extract_features
from tensorflow.keras.models import load_model
import numpy as np
import os

# Load model
model = load_model("emotion_model.h5")
emotion_labels = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

st.set_page_config(page_title="Speech Emotion Email Assistant", page_icon="📧", layout="centered")

st.title("📧 Speech Emotion-Based Email Assistant")
st.markdown("Talk to your assistant and let it draft an emotionally aware email for you.")

if st.button("🎙️ Record Voice (5 seconds)"):
    filename = record_audio()
    st.success(f"Voice recorded and saved as `{filename}`.")

    # Emotion Detection
    features = extract_features(filename).reshape(1, -1)
    prediction = model.predict(features)
    predicted_emotion = emotion_labels[np.argmax(prediction)]
    st.markdown(f"**🧠 Detected Emotion:** `{predicted_emotion}`")

    # Speech to Text
    text = speech_to_text(filename)
    if text:
        st.markdown(f"**📝 Transcribed Text:**\n> {text}")

        # Intent (optional)
        intent = extract_intent(text)
        st.markdown(f"**🔍 Intent Tags:** `{', '.join(intent)}`")

        # Rewritten Email
        rewritten = rewrite_email(text, predicted_emotion)
        st.markdown("**✍️ Suggested Email:**")
        st.code(rewritten)
    else:
        st.error("Could not transcribe audio.")
