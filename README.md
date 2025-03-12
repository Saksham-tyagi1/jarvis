# Voice Authentication System

## Overview
This project implements a **voice-based authentication system** that extracts features from voice recordings and uses them for user verification. The system captures voice samples, processes them to extract key features, and utilizes machine learning models for authentication.

## Features
- **Voice Recording**: Captures audio samples from the user.
- **Feature Extraction**: Uses signal processing techniques to extract unique voice features.
- **Authentication Model**: Compares extracted features against precomputed voice patterns.
- **Real-time Verification**: Allows users to authenticate themselves through their voice.

## Project Structure
```
Voice_Authentication/
│── extract_features.py     # Extracts features from voice recordings
│── jarvis.py              # Main script for handling authentication
│── record_voice.py        # Records user voice samples
│── test_voice.py          # Tests authentication with a sample voice
│── voice_features.pkl     # Precomputed voice feature dataset
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/Saksham-tyagi1/jarvis.git
cd Voice_Authentication
```

### 2. Set Up Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### **Recording a Voice Sample**
```bash
python record_voice.py
```

### **Extracting Voice Features**
```bash
python extract_features.py
```

### **Testing Authentication**
```bash
python test_voice.py
```

## Technologies Used
- **Python** (Core Language)
- **SpeechRecognition** (Voice Processing)
- **Librosa** (Feature Extraction)
- **SciPy & NumPy** (Signal Processing)
- **Machine Learning Models** (For Authentication)

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request!

## License
This project is licensed under the MIT License.

---
### **Author:** Saksham Tyagi

