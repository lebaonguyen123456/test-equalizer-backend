"""
filters.py

Define frequency bands and utility functions
for digital audio equalizer.
"""


def db_to_gain(db):
    """
    Convert gain from decibel (dB) to linear scale.

    Parameters
    ----------
    db : float
        Gain in decibel

    Returns
    -------
    gain : float
        Linear gain
    """
    return 10 ** (db / 20)


def get_frequency_bands():
    """
    Define frequency bands for equalizer (Hz).

    Returns
    -------
    bands : dict
        Dictionary of frequency bands
    """
    return {
        "bass": (20, 250),
        "mid": (250, 4000),
        "treble": (4000, 20000),
    }
