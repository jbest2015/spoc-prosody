import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from audio_input import record_buffer, SAMPLE_RATE
from feature_extractor import extract_features
from annotation_output import features_to_xml, features_to_compressed
from utils import log_event, transcribe_audio


def main():
    log_event("Starting S.P.O.C. pipeline.")
    log_event("Recording audio buffer.")
    audio = record_buffer()
    log_event("Audio recorded. Transcribing.")
    transcribed_text = transcribe_audio(audio, SAMPLE_RATE)
    log_event(f"Transcribed text: {transcribed_text}")
    print("\n--- Transcription ---")
    print(transcribed_text)
    log_event("Extracting features.")
    features = extract_features(audio, SAMPLE_RATE)
    log_event(f"Extracted {len(features)} feature blocks.")
    print("\n--- S.P.O.C. XML Output ---")
    xml_output = features_to_xml(features, text=transcribed_text)
    print(xml_output)
    log_event("Generated XML output.")
    print("\n--- S.P.O.C. Compressed Notation ---")
    compressed_output = features_to_compressed(features)
    print(compressed_output)
    log_event(f"Generated compressed notation output: {compressed_output}")
    # Print a single-line summary for easy copy-paste
    print("\n--- Copy-Paste Test Line ---")
    print(f"TRANSCRIPT: {transcribed_text.strip()} | S.P.O.C.: {compressed_output}")
    log_event(f"Copy-paste test line: TRANSCRIPT: {transcribed_text.strip()} | S.P.O.C.: {compressed_output}")

if __name__ == "__main__":
    main() 