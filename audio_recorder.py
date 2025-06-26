import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(duration=5, filename='user_voice.wav'):
    fs = 44100  # Sample rate
    print("🎙️ Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print(f" Recording saved as {filename}")
    return filename
