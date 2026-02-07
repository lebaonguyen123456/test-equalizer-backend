"""
main.py

Demo backend:
- Load audio file
- Apply FFT-based equalizer
- Visualize waveform & spectrum
- Save output audio
"""

from audio.audio_io import load_audio, save_audio
from audio.equalizer import apply_equalizer
from visualize import plot_waveform, plot_spectrum


# ====== CONFIG ======
INPUT_AUDIO_PATH = "uploads/audio_sample.mp3"
OUTPUT_AUDIO_PATH = "outputs/output_eq.mp3"

BASS_DB = 6
MID_DB = 0
TREBLE_DB = -3
# ====================


def main():
    # Load audio
    signal, sr = load_audio(INPUT_AUDIO_PATH)

    # Apply equalizer
    output = apply_equalizer(
        signal, sr, bass_db=BASS_DB, mid_db=MID_DB, treble_db=TREBLE_DB
    )

    # Visualization
    plot_waveform(signal, sr, "Original Signal")
    plot_waveform(output, sr, "Equalized Signal")

    plot_spectrum(signal, sr, "Original Spectrum")
    plot_spectrum(output, sr, "Equalized Spectrum")

    # Save output
    save_audio(OUTPUT_AUDIO_PATH, output, sr)

    print("Done!")
    print(f"Output saved to: {OUTPUT_AUDIO_PATH}")


if __name__ == "__main__":
    main()
