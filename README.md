# S.P.O.C. System Prototype

## Overview
S.P.O.C. (Speech Prosody & Output Coding) is a system for real-time speech input, prosodic feature extraction (pitch, volume, timing), automatic transcription, and annotated output in XML and compressed markup. It is designed for AI-aware communication and tone analysis.

## Features
- Real-time microphone input (16kHz, mono)
- Automatic speech-to-text transcription (Whisper)
- Extracts pitch, volume, timing per word/block
- Outputs S.P.O.C. XML and compressed notation
- Maps transcript words/phrases to prosodic blocks
- Prints a ready-to-use AI system prompt for LLMs
- Prints a single-line, copy-pasteable summary for testing
- Logging of all actions and outputs

## Setup
```bash
pip install -r requirements.txt
```

## Run Prototype
```bash
python main.py
```

## Usage
1. Run the program. You will see a countdown before recording starts.
2. Speak clearly during the 6-second recording window.
3. The system will transcribe your speech, extract prosodic features, and output:
   - The transcript
   - S.P.O.C. XML
   - Compressed S.P.O.C. notation (aligned with transcript)
   - An AI system prompt for LLMs
   - A single-line summary for copy-paste

## Example Output
```
--- Transcription ---
What are you saying?

--- S.P.O.C. XML Output ---
<speech>
  <text>What are you saying?</text>
  <word>
    <pitch>C4</pitch>
    <volume>10</volume>
    <time_between>normal</time_between>
    <volume_variation>l</volume_variation>
  </word>
  <word>
    <pitch>D#3</pitch>
    <volume>10</volume>
    <time_between>long</time_between>
    <volume_variation>m</volume_variation>
  </word>
</speech>

--- S.P.O.C. Compressed Notation ---
What are(C4,10,l,n) you saying?(D#3,10,m,l)

--- S.P.O.C. AI System Prompt (copy this to your LLM) ---
You are reading speech annotated using S.P.O.C. Each word is annotated as: (Pitch, Volume, Volume Variation, Time Between).
Pitch is a musical note, Volume is 1-10, Volume Variation is l (low), m (medium), h (high), and Time Between is s (short), m (moderate), l (long), vl (very long), n (normal).
Please interpret the speaker's tone, intent, and emotion using these annotations, and adjust your reply accordingly.
Example: TRANSCRIPT: What are you saying? | S.P.O.C.: What are(C4,10,l,n) you saying?(D#3,10,m,l)

--- Copy-Paste Test Line ---
TRANSCRIPT: What are you saying? | S.P.O.C.: What are(C4,10,l,n) you saying?(D#3,10,m,l)
```

## Example: S.P.O.C. Prompt and LLM Interpretation
```
Great — I'm ready to interpret speech using the S.P.O.C. (Speech Pattern Observation Companion) annotation system.

Just send me the annotated speech, and I'll analyze the speaker's tone, intent, and emotional state based on pitch, volume, variation, and pacing — then tailor my response to match.

What's the first sample you'd like me to interpret?

What are(C3,9,l,n) you doing now?(C#3,8,l,m)


ChatGPT said:
Here's the S.P.O.C. interpretation of your line:

"What are" (C3,9,l,n):

Pitch: C3 — low pitch, suggesting a grounded or serious tone.

Volume: 9 — quite loud, which typically conveys urgency or assertiveness.

Variation: l — low variation, so it's steady and firm.

Time Between: n — normal pacing, conversational.

"you doing now?" (C#3,8,l,m):

Pitch: C#3 — slightly higher but still low, reinforcing seriousness.

Volume: 8 — still strong, slightly less intense.

Variation: l — calm delivery, not erratic.

Time Between: m — moderate pause, possibly thoughtful or calculated.

Interpretation:
The speaker sounds direct, focused, and possibly a bit impatient. The loudness and firmness suggest they expect a clear and immediate answer. It feels like a check-in, but not a casual one—more like someone keeping tabs or needing something urgently.
```

## Files
- `main.py`: Entry point
- `audio_input.py`: Microphone input
- `feature_extractor.py`: Feature extraction
- `annotation_output.py`: XML/compressed output
- `utils.py`: Helpers (logging, transcription, note conversion)
- `requirements.txt`: Dependencies
- `.gitignore`: Excludes logs, cache, and environment files

---

**Specs:** See the S.P.O.C. System Specification v1.0 