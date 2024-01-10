import librosa
import numpy as np
import os
import joblib

def extract_mfcc(file_path, n_mfcc=40):
    """Extracts MFCC features from an audio file"""
    y, sr = librosa.load(file_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfcc.T, axis=0)  # Averaging over time

def process_dataset():
    """Extracts MFCC features from all voice samples"""
    data = []
    labels = []
    users = {"user1": 0, "user2": 1}  # Assign labels

    for user, label in users.items():
        folder = f"dataset/{user}/"
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            features = extract_mfcc(file_path)
            data.append(features)
            labels.append(label)

    return np.array(data), np.array(labels)

# Process dataset and save features
X, y = process_dataset()
joblib.dump((X, y), "voice_features.pkl")

print("Feature extraction complete! Data saved as voice_features.pkl")
