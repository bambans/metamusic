import numpy as np
from metamusic._utils import is_lambda

class _Oscillator:
    def __init__(self, sample_rate: int = 48000):
        self.sample_rate = sample_rate

    def _duration(self, duration):
        return np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)

    def _osc_sine(self, duration, amplitude, frequency) -> np.ndarray:
        """
        Generates a sine wave with the given duration, amplitude, and frequency.

        Args:
            duration (float): The duration of the wave in seconds.
            amplitude (float): The amplitude of the wave.
            frequency (float): The frequency of the wave in Hz.

        Returns:
            numpy.ndarray: The generated sine wave.
        """
        return amplitude * np.sin(2 * np.pi * frequency * self._duration(duration))

    def _osc_square(self, duration, amplitude, frequency) -> np.ndarray:
        return amplitude * np.sign(np.sin(2 * np.pi * frequency * self._duration(duration)))

    def _osc_triangle(self, duration, amplitude, frequency) -> np.ndarray:
        return amplitude * (2 * np.abs(2 * (self._duration(duration) * frequency % 1) - 1) - 1)

    def _osc_sawtooth(self, duration, amplitude, frequency) -> np.ndarray:
        return amplitude * (2 * (self._duration(duration) * frequency % 1) - 1)

    def _osc_custom(self, duration, amplitude, frequency, wave_function=None) -> np.ndarray:
        """
        func should take a time array (t) and return a waveform in range [-1, 1].
        Example: lambda t: np.sin(2*np.pi*t) * np.cos(4*np.pi*t)
        """
        if wave_function is None:
            raise ValueError("You must provide a function for custom_wave.")
        return amplitude * wave_function(frequency * self._duration(duration))

    def normalize(self, oscillators):
        oscs = 0
        for osc in oscillators:
            oscs += osc
        return oscs / np.max(np.abs(oscs))

    def get_oscillator(self, duration, amplitude, frequency, wave) -> np.ndarray:
        if isinstance(wave, str):
            if wave == "sine":
                return self._osc_sine(duration, amplitude, frequency)
            elif wave == "square":
                return self._osc_square(duration, amplitude, frequency)
            elif wave == "triangle":
                return self._osc_triangle(duration, amplitude, frequency)
            elif wave == "sawtooth":
                return self._osc_sawtooth(duration, amplitude, frequency)
            else:
                raise ValueError("Invalid wave type")
        elif is_lambda(wave):
            return self._osc_custom(duration, amplitude, frequency, wave)
        else:
            raise ValueError("Invalid wave type")
