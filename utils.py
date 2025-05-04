import numpy as np
import datetime
import whisper
import tempfile
import soundfile as sf

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
A4_FREQ = 440.0
A4_INDEX = 9 + 4 * 12  # MIDI note number for A4


def hz_to_note(freq):
    if freq <= 0 or np.isnan(freq):
        return 'N/A'
    # MIDI note number
    midi = int(round(12 * np.log2(freq / A4_FREQ) + 69))
    octave = midi // 12 - 1
    note = NOTE_NAMES[midi % 12]
    return f"{note}{octave}"


def log_event(message: str, to_console: bool = True):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] {message}\n"
    with open('spoc.log', 'a') as f:
        f.write(log_message)
    if to_console:
        print(f"[LOG] {message}")


def transcribe_audio(audio, sample_rate):
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(suffix='.wav') as f:
        sf.write(f.name, audio, sample_rate)
        result = model.transcribe(f.name)
    return result['text'] 