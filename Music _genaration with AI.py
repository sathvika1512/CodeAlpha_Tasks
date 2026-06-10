from music21 import converter

midi = converter.parse("sample.mid")
notes = []

for note in midi.flat.notes:
    notes.append(str(note.pitch))

print(notes)
