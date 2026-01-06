import numpy as np
from music21 import stream, note

notes_data = [60, 62, 64, 65, 67, 69, 71, 72]
durations = [0.25, 0.5, 1.0]

generated_notes = np.random.choice(notes_data, size=60)
generated_durations = np.random.choice(durations, size=60)

music_stream = stream.Stream()

for pitch, dur in zip(generated_notes, generated_durations):
    n = note.Note(pitch)
    n.duration.quarterLength = dur
    music_stream.append(n)

music_stream.write('midi', fp='generated_music.mid')

print("AI Music Generated Successfully!")
