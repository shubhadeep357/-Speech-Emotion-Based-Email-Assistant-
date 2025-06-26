import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import load_model

DATA_PATH = "ravdess_data/"
EMOTIONS = {
    '01': 'neutral',
    '02': 'calm',
    '03': 'happy',
    '04': 'sad',
    '05': 'angry',
    '06': 'fearful',
    '07': 'disgust',
    '08': 'surprised'
}

def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def load_data():
    X, y = [], []
    print("📥 Scanning folders for .wav files...")
    for folder in os.listdir(DATA_PATH):
        folder_path = os.path.join(DATA_PATH, folder)
        if not os.path.isdir(folder_path):
            continue
        for file in os.listdir(folder_path):
            if file.endswith(".wav"):
                emotion_code = file.split("-")[2]
                if emotion_code in EMOTIONS:
                    label = EMOTIONS[emotion_code]
                    file_path = os.path.join(folder_path, file)
                    try:
                        features = extract_features(file_path)
                        X.append(features)
                        y.append(label)
                    except Exception as e:
                        print(f"❌ Failed to process {file_path}: {e}")
    print(f"✅ Loaded {len(X)} audio samples.")
    return np.array(X), np.array(y)

def build_model(input_shape, num_classes):
    model = Sequential([
        Dense(256, input_shape=(input_shape,), activation='relu'),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def train_model():
    print("🔍 Loading dataset...")
    X, y = load_data()

    if len(X) == 0:
        print("❌ ERROR: No audio data found! Make sure 'ravdess_data/' is populated correctly.")
        return

    print("🔧 Encoding labels...")
    le = LabelEncoder()
    y_encoded = to_categorical(le.fit_transform(y))

    print("📊 Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    print("🧠 Building the model...")
    model = build_model(input_shape=X.shape[1], num_classes=y_encoded.shape[1])

    print("🏋️ Training started...")
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

    print("💾 Saving trained model to emotion_model.h5")
    model.save("emotion_model.h5")
    print("✅ Emotion model trained and saved successfully!")

    return le

# Run the function directly
train_model()
