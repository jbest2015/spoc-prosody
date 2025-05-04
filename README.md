# S.P.O.C. System Prototype

## Overview
S.P.O.C. (Speech Prosody & Output Coding) is a system for real-time speech input, prosodic feature extraction (pitch, volume, timing), and annotated output in XML and compressed markup.

## Features
- Real-time microphone input (16kHz, mono)
- Extracts pitch, volume, timing per word/block
- Outputs S.P.O.C. XML and compressed notation

## Setup
```bash
pip install -r requirements.txt
```

## Run Prototype
```bash
python main.py
```

## Files
- `main.py`: Entry point
- `audio_input.py`: Microphone input
- `feature_extractor.py`: Feature extraction
- `annotation_output.py`: XML/compressed output
- `tone_classifier.py`: (Optional) Tone detection
- `utils.py`: Helpers

---

**Specs:** See the S.P.O.C. System Specification v1.0 