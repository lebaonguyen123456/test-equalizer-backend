"""
features.py

Extract audio features for music genre classification
"""

import numpy as np
import librosa


def extract_mfcc(signal, sr, n_mfcc=13):
    """
    Extract MFCC features from audio signal

    Parameters
    ----------
    signal : np.ndarray
        Audio signal
    sr : int
        Sample rate
    n_mfcc : int
        Number of MFCC coefficients

    Returns
    -------
    features : np.ndarray
        Mean MFCC feature vector
    """
    mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = np.mean(mfcc, axis=1)
    return mfcc_mean
