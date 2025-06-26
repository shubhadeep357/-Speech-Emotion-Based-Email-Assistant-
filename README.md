
# 📧 Speech Emotion-Based Email Assistant

---

## Table of Contents
* [🌟 Overview](#-overview)
* [✨ Features](#-features)
* [🛠️ Technologies Used](#️-technologies-used)
* [🚀 Installation & Setup](#-installation--setup)
    * [Prerequisites](#prerequisites)
    * [Step-by-Step Installation](#step-by-step-installation)
    * [FFmpeg Setup (Crucial!)](#ffmpeg-setup-crucial)
* [💡 Usage](#-usage)
* [🧠 Machine Learning Models](#-machine-learning-models)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)
* [📞 Contact](#-contact)

---

## 🌟 Overview

The Speech Emotion-Based Email Assistant is an intelligent Streamlit web application designed to streamline email drafting by leveraging the power of speech recognition and emotion detection. This tool allows users to either speak their email content or upload an audio file, which is then transcribed, analyzed for the speaker's emotional state, and used to generate an email draft with an appropriate tone.

This project addresses the common challenge of translating spoken thoughts into professional written communication, adding an emotional intelligence layer to ensure the message's tone aligns with the speaker's original intent or desired impact.

---

## ✨ Features

* 🎙️ Voice Recording: Directly record your message using your microphone within the app.
* ⬆️ Audio File Upload: Upload existing audio files (MP3, WAV, FLAC, OGG) for transcription and analysis.
* 📝 Accurate Speech-to-Text: Utilizes Google's Web Speech API (via `speech_recognition` library) to convert spoken words into text.
* 🧠 Real-time Emotion Detection: Analyzes the audio to identify the predominant emotion (e.g., angry, calm, happy, sad, neutral, surprised, fearful, disgust).
* 🔍 Intent Extraction (Placeholder): A module to identify key intents or topics from the transcribed text, providing additional context.
* 📧 Emotion-Aware Email Drafting: Generates an email draft, with the content and tone influenced by the detected emotion and extracted intent.
* 💻 Intuitive Streamlit Interface: A user-friendly web interface for seamless interaction.

---

## 🛠️ Technologies Used

* Python 3.x
* Streamlit
* sounddevice & wavio
* pydub
* speech_recognition
* librosa
* TensorFlow/Keras
* numpy
* ffmpeg

---

## 🚀 Installation & Setup

### Prerequisites

* Python 3.8+ (recommended)
* pip
* FFmpeg

### Step-by-Step Installation

1. Clone the Repository:
    ```bash
    git clone https://github.com/your-username/your-project-name.git
    cd your-project-name
    ```

2. Create a Virtual Environment:
    ```bash
    python -m venv .venv
    ```

3. Activate the Virtual Environment:
    - Windows:
        ```bash
        .\.venv\Scriptsctivate
        ```
    - macOS/Linux:
        ```bash
        source ./.venv/bin/activate
        ```

4. Install Required Packages:
    ```bash
    pip install -r requirements.txt
    ```

If `requirements.txt` is missing:
    ```bash
    pip install streamlit sounddevice numpy wavio speechrecognition librosa tensorflow pydub soundfile
    pip freeze > requirements.txt
    ```

5. Place Pre-trained Models:
    - Place `emotion_model.h5` and other custom files like `intent_extractor.py` in the root directory.

### FFmpeg Setup (Crucial!)

Refer to official docs or [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html).

---

## 💡 Usage

```bash
streamlit run app.py
```

App will launch at `http://localhost:8501`

---

## [Streamlit App Interface Picture]

Replace this with your app screenshot:  
`![Streamlit App Interface](images/app_screenshot.png)`

---

## 🧠 Machine Learning Models

- Emotion Detection: Uses MFCC + Keras model.
- Speech-to-Text: Google Web API.
- Email Rewriting: Custom logic based on emotion and intent.

---

## 🤝 Contributing

Contributions welcome! Fork → Branch → Commit → Pull Request.

---

## 📄 License

MIT License

---

## 📞 Contact

 Shubhadeep Saha - shubhadeepsaha357@gmail.com

