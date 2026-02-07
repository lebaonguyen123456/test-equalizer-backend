"""
realtime.py

Realtime audio equalizer:
Mic -> FFT EQ -> Speaker
"""

import sounddevice as sd

from audio.equalizer import apply_equalizer

# ===== CONFIG =====
SAMPLE_RATE = 44100
FRAME_SIZE = 1024

INPUT_DEVICE = 1
OUTPUT_DEVICE = 3

BASS_DB = 6
MID_DB = 0
TREBLE_DB = -3
# ==================


def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)

    # Mono signal
    signal = indata[:, 0]

    # Apply FFT equalizer
    output = apply_equalizer(
        signal, SAMPLE_RATE, bass_db=BASS_DB, mid_db=MID_DB, treble_db=TREBLE_DB
    )

    # Write to output buffer
    outdata[:, 0] = output


def main():
    print("Realtime Equalizer running...")
    print("Press Ctrl+C to stop")

    try:
        with sd.Stream(
            samplerate=SAMPLE_RATE,
            blocksize=FRAME_SIZE,
            channels=1,
            callback=audio_callback,
            device=(INPUT_DEVICE, OUTPUT_DEVICE),
        ):
            while True:
                sd.sleep(1000)
    except KeyboardInterrupt:
        print("\nRealtime Equalizer stopped.")


if __name__ == "__main__":
    main()
