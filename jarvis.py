import tensorflow as tf
import numpy as np
import librosa
import sounddevice as sd
import soundfile as sf
import openai
import os

# Load trained authentication model
model = tf.keras.models.load_model("voice_auth_model.h5")

openai.api_key = "your_openai_api_key" 

def record_and_authenticate():
    """Records the user's voice and authenticates their identity"""
    filename = "temp_voice.wav"
    samplerate = 16000
    duration = 3

    print("🔐 Speak to authenticate...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, audio, samplerate)
    
    # Extract MFCC features
    y, sr = librosa.load(filename, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    features = np.mean(mfcc.T, axis=0)

    # Predict user identity
    prediction = model.predict(np.expand_dims(features, axis=0))[0][0]
    
    if prediction > 0.5:
        print("Authentication successful! Access granted.")
        return True
    else:
        print("Authentication failed! Access denied.")
        return False

def chat_with_gpt(prompt):
    """Ask OpenAI GPT a question"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Main AI loop with authentication
if record_and_authenticate():
    while True:
        user_input = input("💬 Ask something (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"🤖 J.A.R.V.I.S.: {response}")
