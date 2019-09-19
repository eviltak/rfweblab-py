from unittest import TestCase

from rfweblab import Signal


class TestSignal(TestCase):
    def setUp(self) -> None:
        from phypy import modulators

        # Build the OFDM modulator and the signal
        ofdm = modulators.OFDM(n_subcarriers=600)

        self.signal = Signal(ofdm.use(n_symbols=10), ofdm.sampling_rate)

    def test_resample(self):
        sample_length = len(self.signal)
        sample_rate = self.signal.sample_rate

        new_sample_rate = int(200e6)
        resampled_signal = self.signal.resample(new_sample_rate)

        self.assertEqual(new_sample_rate, resampled_signal.sample_rate)

        import math
        self.assertEqual(math.ceil(sample_length / sample_rate * new_sample_rate), len(resampled_signal))

    def test_rms(self):
        pass
