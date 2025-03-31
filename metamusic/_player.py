import sounddevice as sd

class _Player:
    def __init__(self, composition, sample_rate = 48000):
        self.composition = composition
        self.sample_rate = sample_rate

    def play(self):
        sd.play(self.composition, self.sample_rate)
        sd.wait()
