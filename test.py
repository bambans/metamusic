from metamusic._oscillator import _Oscillator
from metamusic._notes import _Note
from metamusic._player import _Player

# import numpy as np

sample_rate = 48000

NOTE = _Note()

# print(NOTE.notes_list)

wavetest = "sine"

OSC = _Oscillator(sample_rate=sample_rate)

# strange wave example
# wavetest = lambda t: (
#     np.sin(2 * np.pi * 220 * t) *         # base sine wave
#     np.sign(np.sin(2 * np.pi * 3 * t)) *  # modulate with low-freq square
#     np.cos(2 * np.pi * 0.5 * t) +         # add slow tremolo
#     0.3 * np.sin(2 * np.pi * 1500 * t**2) # pitch sweep / chirp
# )
# PLAYER = Player(composition = OSC.get_oscillator(
#       duration = 2,
#       amplitude = 0.5,
#       frequency = NOTE.note_to_freq("A4"),
#       wave = wavetest
#   ), sample_rate=sample_rate)
# PLAYER.play()

wavetest = "sine"
duration = 1
composition = OSC.normalize([
    OSC.get_oscillator(duration = duration, amplitude = 0.9, frequency = NOTE.note_to_freq("C4"), wave = wavetest),
    OSC.get_oscillator(duration = duration, amplitude = 0.8, frequency = NOTE.note_to_freq("E4"), wave = wavetest),
    OSC.get_oscillator(duration = duration, amplitude = 0.7, frequency = NOTE.note_to_freq("G4"), wave = wavetest),
    OSC.get_oscillator(duration = duration, amplitude = 0.6, frequency = NOTE.note_to_freq("B4"), wave = wavetest)
])

PLAYER = _Player(composition=composition, sample_rate=sample_rate)
PLAYER.play()
