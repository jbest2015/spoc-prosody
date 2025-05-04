import sounddevice as sd
import numpy as np
import time

SAMPLE_RATE = 16000
CHANNELS = 1
BUFFER_SECONDS = 6


def record_buffer(duration=BUFFER_SECONDS, sample_rate=SAMPLE_RATE):
    """
    Records audio from the default microphone for the given duration (seconds).
    Returns a numpy array of shape (samples,).
    """
    print(f"Get ready to speak! Recording will start in 3 seconds...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print(f"Recording {duration} seconds of audio NOW!")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=CHANNELS, dtype='float32')
    sd.wait()
    print("Recording finished.")
    return np.squeeze(audio) 