import soundfile as sf
import sounddevice as sd
import os

def record_audio(filename, duration=3, samplerate=16000):
    """Records audio for a given duration"""
    print(f"Recording... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, audio, samplerate)
    print(f"Recording saved as {filename}")

# Create folders for storing voice samples
os.makedirs("dataset/user1", exist_ok=True)
os.makedirs("dataset/user2", exist_ok=True)

# Record multiple samples for each user
for i in range(5):
    record_audio(f"dataset/user1/sample_{i}.wav")
    record_audio(f"dataset/user2/sample_{i}.wav")
