import numpy as np
import librosa

from utils import hz_to_note

# Parameters for segmentation and feature extraction
FRAME_LENGTH = 1024
HOP_LENGTH = 256
SILENCE_THRESHOLD = 0.02  # RMS below this is considered silence
MIN_BLOCK_DURATION = 0.1  # seconds
MIN_SILENCE_DURATION = 0.1  # seconds (100ms)


def segment_blocks(audio, sample_rate):
    """
    Segments audio into blocks (words/syllables) based on RMS energy.
    Returns list of (start_sample, end_sample) tuples.
    """
    rms = librosa.feature.rms(y=audio, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)[0]
    times = librosa.frames_to_time(np.arange(len(rms)), sr=sample_rate, hop_length=HOP_LENGTH)
    is_speech = rms > SILENCE_THRESHOLD
    blocks = []
    start = None
    for i, speech in enumerate(is_speech):
        if speech and start is None:
            start = i
        elif not speech and start is not None:
            # End of block
            end = i
            # Only keep if long enough
            if times[end-1] - times[start] >= MIN_BLOCK_DURATION:
                blocks.append((start, end))
            start = None
    if start is not None:
        end = len(is_speech)
        if times[end-1] - times[start] >= MIN_BLOCK_DURATION:
            blocks.append((start, end))
    # Convert frame indices to sample indices
    sample_blocks = [(int(times[s]*sample_rate), int(times[e-1]*sample_rate)) for s, e in blocks]
    return sample_blocks


def extract_features(audio, sample_rate):
    """
    Extracts features for each block: pitch, volume, time_between, volume_delta, pitch_contour.
    Returns a list of dicts, one per block.
    """
    blocks = segment_blocks(audio, sample_rate)
    features = []
    prev_end = 0
    prev_rms = None
    prev_pitch = None
    for i, (start, end) in enumerate(blocks):
        block_audio = audio[start:end]
        # Pitch (use librosa.yin)
        f0 = librosa.yin(block_audio, fmin=50, fmax=500, sr=sample_rate)
        pitch_hz = np.median(f0)
        pitch_note = hz_to_note(pitch_hz)
        # Volume (RMS, scale 1-10)
        rms = np.sqrt(np.mean(block_audio**2))
        volume = int(np.clip(rms * 100, 1, 10))
        # Time between blocks
        if i == 0:
            time_between = None
        else:
            time_between = (start - prev_end) / sample_rate
        # Volume delta
        if prev_rms is not None:
            volume_delta = rms - prev_rms
        else:
            volume_delta = 0
        # Pitch contour (simple: rising, falling, flat)
        if len(f0) > 1:
            if f0[-1] - f0[0] > 10:
                pitch_contour = 'rising'
            elif f0[0] - f0[-1] > 10:
                pitch_contour = 'falling'
            else:
                pitch_contour = 'flat'
        else:
            pitch_contour = 'flat'
        features.append({
            'start': start,
            'end': end,
            'pitch_hz': float(pitch_hz),
            'pitch_note': pitch_note,
            'volume': volume,
            'rms': float(rms),
            'time_between': float(time_between) if time_between is not None else None,
            'volume_delta': float(volume_delta),
            'pitch_contour': pitch_contour,
        })
        prev_end = end
        prev_rms = rms
        prev_pitch = pitch_hz
    return features 