# 📧 Speech Emotion-Based Email Assistant

## Table of Contents
* [🌟 Overview](#-overview)
* [✨ Features](#-features)
* [🛠️ Technologies Used](#️-technologies-used)
* [🚀 Installation & Setup](#-installation--setup)
    * [Prerequisites](#prerequisites)
    * [Step-by-Step Installation](#step-by-step-installation)
    * [FFmpeg Setup (Crucial!)](#ffmpeg-setup-crucial)
* [💡 Usage](#-usage)
* [📂 Project Structure](#-project-structure)
* [🧠 Machine Learning Models](#-machine-learning-models)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)
* [📞 Contact](#-contact)

---

## 🌟 Overview

The Speech Emotion-Based Email Assistant is an intelligent Streamlit web application designed to streamline email drafting by leveraging the power of speech recognition and emotion detection. This tool allows users to either speak their email content or upload an audio file, which is then transcribed, analyzed for the speaker's emotional state, and used to generate an email draft with an appropriate tone.

This project addresses the common challenge of translating spoken thoughts into professional written communication, adding an emotional intelligence layer to ensure the message's tone aligns with the speaker's original intent or desired impact.

## ✨ Features

* **🎙️ Voice Recording:** Directly record your message using your microphone within the app.
* **⬆️ Audio File Upload:** Upload existing audio files (MP3, WAV, FLAC, OGG) for transcription and analysis.
* **📝 Accurate Speech-to-Text:** Utilizes Google's Web Speech API (via `speech_recognition` library) to convert spoken words into text.
* **🧠 Real-time Emotion Detection:** Analyzes the audio to identify the predominant emotion (e.g., angry, calm, happy, sad, neutral, surprised, fearful, disgust).
* **🔍 Intent Extraction (Placeholder):** A module to identify key intents or topics from the transcribed text, providing additional context.
* **📧 Emotion-Aware Email Drafting:** Generates an email draft, with the content and tone influenced by the detected emotion and extracted intent.
* **💻 Intuitive Streamlit Interface:** A user-friendly web interface for seamless interaction.

## 🛠️ Technologies Used

* **Python 3.x:** The core programming language.
* **Streamlit:** For building the interactive web application interface.
* **`sounddevice` & `wavio`:** For capturing and saving microphone audio.
* **`pydub`:** Essential for handling and converting various audio file formats (MP3, FLAC, OGG) to the required WAV format. Requires `ffmpeg`.
* **`speech_recognition`:** For performing Speech-to-Text (using Google's Web Speech API by default).
* **`librosa`:** For audio feature extraction (e.g., MFCCs) for the emotion classification model.
* **`TensorFlow`/`Keras`:** For building and loading the pre-trained Speech Emotion Recognition (SER) model.
* **`numpy`:** For numerical operations, especially with audio data.
* **`ffmpeg`:** An external audio/video converter (a system-level dependency required by `pydub` and recommended for robust audio handling).

## 🚀 Installation & Setup

Follow these steps to get the Speech Emotion-Based Email Assistant up and running on your local machine.

### Prerequisites

* Python 3.8+ (recommended)
* `pip` (Python package installer)
* **FFmpeg** (Crucial system-level dependency for audio processing)

### Step-by-Step Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```
    *(Replace `your-username/your-project-name` with your actual GitHub repository URL)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source ./.venv/bin/activate
        ```

4.  **Install Required Python Packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt`, create it by running the following commands after activating your virtual environment):*
    ```bash
    pip install streamlit sounddevice numpy wavio speechrecognition librosa tensorflow pydub soundfile
    pip freeze > requirements.txt
    ```

5.  **Place Your Pre-trained Models:**
    * Ensure your Keras emotion classification model (`emotion_model.h5`) is placed directly in the project's root directory (alongside `app.py`).
    * Similarly, ensure `intent_extractor.py` and `tone_rewriter.py` are present if they contain custom logic. If they are placeholders, the app will still run but with basic functionality.

### FFmpeg Setup (Crucial!)

`pydub` and robust audio handling require `ffmpeg` to be installed on your system and its executable path added to your system's `PATH` environment variable.

#### For Windows:
1.  **Download FFmpeg:**
    * Visit [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html).
    * Click on the **Windows icon**, then choose a build (e.g., "Windows builds from gyan.dev" and download `ffmpeg-release-essentials.7z`).
    * Extract the `.7z` file using a tool like 7-Zip or WinRAR. This will create a folder (e.g., `ffmpeg-xxxxxx-essentials_build`).
2.  **Rename & Move:** Rename this extracted folder to something simpler like `ffmpeg` (e.g., `C:\ffmpeg`).
3.  **Add to PATH:**
    * Search for "Environment Variables" in the Windows search bar and select "Edit the system environment variables".
    * In the "System Properties" window, click "Environment Variables...".
    * Under "System variables", find and select `Path`, then click "Edit...".
    * Click "New" and paste the full path to the `bin` folder *inside* your `ffmpeg` directory (e.g., `C:\ffmpeg\bin`).
    * Click "OK" on all windows to close them.
4.  **Verify:** Open a **NEW** Command Prompt or PowerShell window and type `ffmpeg -version`. If you see version details, you're good to go! If not, double-check your steps or restart your computer.

#### For macOS (using Homebrew):
```bash
brew install ffmpeg

#### For Linux (Debian/Ubuntu):
```bash
sudo apt update && sudo apt install ffmpeg

#### Run the Streamlit App:

```bash
streamlit run app.py

🧠 Machine Learning Models
Speech Emotion Recognition (SER): The project uses a deep learning model (expected to be a Keras model, emotion_model.h5) trained to classify emotions from audio features.
The emotion_classifier.py script likely contains the feature extraction pipeline (e.g., MFCCs, Chroma, Mel Spectrograms) that feeds into this model.
Speech-to-Text: Leverages robust cloud-based speech recognition (Google Web Speech API by default) for high accuracy transcription.
Intent Extraction & Email Rewriting: These modules (intent_extractor.py, tone_rewriter.py) are designed to further process the transcribed text and detected emotion to generate contextually relevant email drafts.
Their implementation details would depend on whether you've used rule-based systems, fine-tuned NLP models, or simple string manipulation.


🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

Fork the repository.
Create a new branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
(If you don't have a LICENSE file, consider adding one to your repository)

📞 Contact
Email - shubhadeep357@gmail.com
