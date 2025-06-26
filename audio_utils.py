# audio_utils.py
import streamlit as st
import sounddevice as sd
import wavio as wv
import numpy as np
import os
import wave # Crucial for WAV inspection
import speech_recognition as sr # Re-introducing speech_recognition

# --- Configuration for Audio Recording ---
SAMPLE_RATE = 16000  # Standard sample rate for speech recognition and emotion model
CHANNELS = 1         # Mono channel for speech
DTYPE = 'int16'      # 16-bit PCM

def record_and_transcribe_audio(filename="recorded.wav", duration=5):
    """
    Records audio, saves it as a WAV file, inspects its properties,
    and then attempts to transcribe it using speech_recognition.

    Args:
        filename (str): The name of the WAV file to save.
        duration (int): The duration of the recording in seconds.
    Returns:
        tuple: (bool, str) - (True if recording successful, transcribed text)
               or (False, None) if recording/transcription fails.
    """
    st.info(f"🎙️ Recording... Speak now for {duration} seconds!")
    recorded_audio_data = None
    try:
        # Start recording
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=DTYPE) as stream:
            audio_data, overflowed = stream.read(int(SAMPLE_RATE * duration))

        # Convert numpy array to int16 (if not already) and save
        recorded_audio_data_int16 = audio_data.astype(np.int16)
        wv.write(filename, recorded_audio_data_int16, SAMPLE_RATE, sampwidth=2)
        st.success("✅ Recording saved successfully!")

        # --- CRUCIAL: WAV File Properties for Debugging `speech_recognition` ---
        st.subheader("WAV File Properties (for speech_recognition debugging):")
        try:
            with wave.open(filename, 'rb') as wf:
                st.write(f"- Channels: {wf.getnchannels()}")
                st.write(f"- Sample Width (bytes): {wf.getsampwidth()} ({wf.getsampwidth() * 8}-bit)")
                st.write(f"- Frame Rate (Hz): {wf.getframerate()}")
                st.write(f"- Compression Type: {wf.getcomptype()} ({wf.getcompname()})")
                
                # Check for compatibility with common speech_recognition requirements
                if wf.getnchannels() != 1:
                    st.warning("  🚨 Warning: SpeechRecognition often prefers mono audio.")
                if wf.getsampwidth() != 2: # 2 bytes = 16-bit
                    st.warning("  🚨 Warning: SpeechRecognition often prefers 16-bit audio.")
                if wf.getframerate() != SAMPLE_RATE:
                    st.warning(f"  🚨 Warning: Sample rate mismatch. Expected {SAMPLE_RATE}, got {wf.getframerate()}.")
                if wf.getcomptype() != 'NONE':
                    st.warning("  🚨 Warning: SpeechRecognition requires uncompressed PCM (compression type 'NONE').")
                    
        except Exception as ex:
            st.error(f"Error inspecting WAV file properties: {ex}")
            st.warning("This indicates a problem with the WAV file format itself, which will cause speech_recognition to fail.")
            return False, None

        # --- Speech to Text using speech_recognition ---
        st.info("👂 Transcribing audio with speech_recognition...")
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            try:
                audio = r.record(source) # Read the entire audio file

                # Attempt with Google Web Speech API (Free, but rate-limited and less robust)
                try:
                    text = r.recognize_google(audio)
                    st.success("📝 Transcription via Google Web Speech API (default) successful!")
                    return True, text
                except sr.UnknownValueError:
                    st.warning("Google Web Speech API could not understand audio.")
                except sr.RequestError as e:
                    st.warning(f"Could not request results from Google Web Speech API service; {e}")

                # Optional: If you have Google Cloud credentials set up (from previous advice)
                # This is more robust and recommended if default Google API fails
                # try:
                #     from google.cloud import speech_v1p1beta1 as speech
                #     # This assumes GOOGLE_APPLICATION_CREDENTIALS env var is set
                #     # Or you can load credentials explicitly:
                #     # from google.oauth2 import service_account
                #     # credentials = service_account.Credentials.from_service_account_file("path/to/your/gcp_credentials.json")
                #     # client = speech.SpeechClient(credentials=credentials)
                #     # text = r.recognize_google_cloud(audio, client=client)
                #
                #     # Simpler: If you have GOOGLE_APPLICATION_CREDENTIALS set
                #     text = r.recognize_google_cloud(audio)
                #     st.success("📝 Transcription via Google Cloud Speech-to-Text API successful!")
                #     return True, text
                # except ImportError:
                #     st.info("google-cloud-speech library not found. Skipping Google Cloud STT.")
                # except sr.UnknownValueError:
                #     st.warning("Google Cloud Speech-to-Text could not understand audio.")
                # except sr.RequestError as e:
                #     st.warning(f"Could not request results from Google Cloud Speech-to-Text API service; {e}")
                # except Exception as e:
                #     st.warning(f"Error with Google Cloud Speech-to-Text setup: {e}")

                st.error("❌ Speech-to-text failed. No transcription obtained.")
                return False, None

            except sr.exceptions.AudioFileError as e:
                st.error(f"❌ SpeechRecognition AudioFileError: {e}")
                st.warning("This is the 'Audio file could not be read' error. Check the WAV properties above.")
                return False, None
            except Exception as e:
                st.error(f"❌ An unexpected error occurred during transcription: {e}")
                return False, None

    except Exception as e:
        st.error(f"❌ Error during recording: {e}")
        st.warning("Please ensure your microphone is connected and accessible.")
        return False, None