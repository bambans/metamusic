from math import log2
from typing import Final
from re import fullmatch

class _Note:
    def __init__(self, A4 = 440):
        self.A4 = A4 or 440
        self.MIN_MIDI = 0
        self.MAX_MIDI = 135
        self.notes: Final = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.ENHARMONIC_EQUIVALENTS: Final = {
            "C": ["C", "B#", "Dbb"],
            "C#": ["C#", "Db"],
            "D": ["D", "C##", "Ebb"],
            "D#": ["D#", "Eb"],
            "E": ["E", "Fb", "D##"],
            "F": ["F", "E#", "Gbb"],
            "F#": ["F#", "Gb"],
            "G": ["G", "F##", "Abb"],
            "G#": ["G#", "Ab"],
            "A": ["A", "G##", "Bbb"],
            "A#": ["A#", "Bb"],
            "B": ["B", "Cb", "A##"]
        }
        self.notes_list = []
        self.generate_midi_note_list(start = self.MIN_MIDI, end = self.MAX_MIDI)

    def _normalize_note(self, note):
            # Use regex to split note name from octave
            match = fullmatch(r"([A-Ga-g][#b♯♭]*)(-?\d+)", note)
            if not match:
                raise ValueError(f"Invalid note format: {note}")

            name_part = match.group(1).capitalize()
            octave_part = match.group(2)

            # Normalize enharmonic name
            for key, aliases in self.ENHARMONIC_EQUIVALENTS.items():
                if name_part in aliases:
                    return key, octave_part, f"{key}{octave_part}"

            raise ValueError(f"Unknown note name: {note}")

    def freq_to_midi(self, freq):
        if freq <= 0:
            raise ValueError("Frequency must be positive.")
        return round(69 + 12 * log2(freq / self.A4))

    def midi_to_freq(self, midi_note):
        if midi_note < self.MIN_MIDI or midi_note > self.MAX_MIDI:
            raise ValueError(f"MIDI note out of range: {midi_note}")
        return self.A4 * (2 ** ((midi_note - 69) / 12))

    def midi_to_note_name(self, midi):
        note = self.notes[midi % 12]
        octave = (midi // 12) - 1
        return f"{note}{octave}"

    def note_to_midi(self, note_name):
        midi = self.notes.index(note_name[0]) + 12 * (int(note_name[1]) + 1)
        return midi

    def note_to_freq(self, note_name):
        midi = self.note_to_midi(self._normalize_note(note_name))
        return self.midi_to_freq(midi)

    def generate_midi_note_list(self, start, end):
        for midi in range(start, end + 1):
            freq = self.midi_to_freq(midi)
            name = self.midi_to_note_name(midi)
            self.notes_list.append({
                "midi": midi,
                "note": name,
                "frequency": round(freq, 2)
            })
