import tensorflow as tf
import numpy as np
import librosa
import joblib
import sounddevice as sd
import soundfile as sf

# Load trained model
model = tf.keras.models.load_model("voice_auth_model.h5")

def record_and_predict():
    """Records user's voice and predicts identity"""
    filename = "test_audio.wav"
    
    # Record voice
    print("Recording... Speak now!")
    samplerate = 16000
    duration = 3
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, audio, samplerate)
    print(f"Recording saved as {filename}")

    # Extract MFCC features
    y, sr = librosa.load(filename, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    features = np.mean(mfcc.T, axis=0)

    # Predict user identity
    prediction = model.predict(np.expand_dims(features, axis=0))[0][0]
    
    if prediction > 0.5:
        print("🔐 Voice Authenticated as User 2")
    else:
        print("🔐 Voice Authenticated as User 1")

# Run the authentication
record_and_predict()
