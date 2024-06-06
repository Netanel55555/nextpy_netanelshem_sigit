class MusicNotes:
    FREQUENCIES = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
    MAX_OCTAVE = 4

    def __init__(self):
        self.index = 0
        self.current_octave = 0

    def __iter__(self):
        self.index = 0
        self.current_octave = 0
        return self

    def __next__(self):
        if self.index >= len(self.FREQUENCIES):
            self.index = 0
            self.current_octave += 1
            if self.current_octave > self.MAX_OCTAVE:
                raise StopIteration

        frequency = self.FREQUENCIES[self.index]
        self.index += 1
        return frequency * (2 ** self.current_octave)

def main():
    note_frequencies = iter(MusicNotes())

    for frequency in note_frequencies:
        print(frequency)

if __name__ == '__main__':
    main()
