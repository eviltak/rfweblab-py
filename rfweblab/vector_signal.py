from __future__ import annotations

from nptyping import Array
from scipy import signal
import numpy as np


class Signal:
    def __init__(self, samples: Array[complex], sample_rate: int):
        self.samples = samples
        self.sample_rate = sample_rate

    def resample(self, new_sample_rate: int) -> Signal:
        new_samples = np.array(signal.resample_poly(self.samples, new_sample_rate, self.sample_rate))

        return Signal(new_samples, new_sample_rate)

    def rms(self) -> float:
        return np.sqrt(np.mean(np.abs(self.samples) ** 2))

    def __len__(self) -> int:
        return len(self.samples)
