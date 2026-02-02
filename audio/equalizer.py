"""
equalizer.py

FFT-based audio equalizer.
"""

import numpy as np
from audio.filters import db_to_gain, get_frequency_bands


def apply_equalizer(signal, sr, bass_db=0, mid_db=0, treble_db=0):
    """
    Apply FFT-based equalizer to audio signal.

    Parameters
    ----------
    signal : np.ndarray
        Input mono audio signal
    sr : int
        Sample rate
    bass_db : float
        Gain for bass band (dB)
    mid_db : float
        Gain for mid band (dB)
    treble_db : float
        Gain for treble band (dB)

    Returns
    -------
    output : np.ndarray
        Equalized audio signal
    """

    # Number of samples
    N = len(signal)

    # FFT (real-valued)
    spectrum = np.fft.rfft(signal)

    # Frequency axis
    freqs = np.fft.rfftfreq(N, d=1.0 / sr)

    # Convert dB to linear gain
    gains = {
        "bass": db_to_gain(bass_db),
        "mid": db_to_gain(mid_db),
        "treble": db_to_gain(treble_db),
    }

    # Apply gain for each frequency band
    for band, (low_freq, high_freq) in get_frequency_bands().items():
        band_indices = (freqs >= low_freq) & (freqs < high_freq)
        spectrum[band_indices] *= gains[band]

    # Inverse FFT
    output = np.fft.irfft(spectrum, n=N)

    return output
