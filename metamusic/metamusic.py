from _notes import _Note
from _oscillator import _Oscillator
from _player import _Player

class MetaMusic:
    def __init__(self, sample_rate=48000, music_duration=60, file_path=None):
        self.NOTE = _Note()
        self.OSCILLATOR = _Oscillator()
        self.sample_rate = sample_rate
        self.music_duration = music_duration
