import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"


def play_song():
    note_pairs = notes.split('-')

    notes_list = []

    for pair in note_pairs:
        note, duration = pair.split(',')
        notes_list.append((note, int(duration)))

    iter_obj = iter(notes_list)

    for i in range(0, len(notes_list)):
        current_tav = next(iter_obj)
        print(current_tav)
        winsound.Beep(freqs[current_tav[0]], current_tav[1])


play_song()
