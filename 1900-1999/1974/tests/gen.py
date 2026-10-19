"""Print seed mode: dense, alternating, binary, random, cyclic,
short_source, short_queries, mixed, aliases. Lengths reach 1000 and m=100.
All enharmonic spellings are generated, including octave-boundary aliases.
"""
import random
import sys


NOTE_COUNT = 96
OCTAVE_SIZE = 12
LENGTH_LIMIT = 1000
SONG_LIMIT = 100
CANONICAL = ('C', 'C+', 'D', 'D+', 'E', 'F', 'F+', 'G', 'G+', 'A', 'A+', 'B')
ALIASES = {1: 'D-', 3: 'E-', 4: 'F-', 5: 'E+', 6: 'G-', 8: 'A-', 10: 'B-'}


def spelling(pitch, variant):
    octave, semitone = divmod(pitch, OCTAVE_SIZE)
    octave += 1
    if variant % 2:
        if semitone in ALIASES:
            return str(octave) + ALIASES[semitone]
        if semitone == 0 and octave > 1:
            return str(octave - 1) + 'B+'
        if semitone == OCTAVE_SIZE - 1 and octave < NOTE_COUNT // OCTAVE_SIZE:
            return str(octave + 1) + 'C-'
    return str(octave) + CANONICAL[semitone]


def build(seed, mode):
    rng = random.Random(seed)
    if mode == 'dense':
        source = [47] * LENGTH_LIMIT
        songs = [[47] * LENGTH_LIMIT for _ in range(SONG_LIMIT)]
    elif mode == 'alternating':
        source = [0, 47] * (LENGTH_LIMIT // 2)
        songs = [[(0, 47)[(i + phase) % 2] for i in range(LENGTH_LIMIT)]
                 for phase in range(SONG_LIMIT)]
    elif mode == 'binary':
        source = [rng.choice((11, 12)) for _ in range(LENGTH_LIMIT)]
        songs = [[rng.choice((11, 12)) for _ in range(LENGTH_LIMIT)] for _ in range(SONG_LIMIT)]
    elif mode == 'random':
        source = [rng.randrange(NOTE_COUNT) for _ in range(LENGTH_LIMIT)]
        songs = [[rng.randrange(NOTE_COUNT) for _ in range(LENGTH_LIMIT)] for _ in range(SONG_LIMIT)]
    elif mode in ('cyclic', 'aliases'):
        source = [i % NOTE_COUNT for i in range(LENGTH_LIMIT)]
        songs = [[(i + (phase if mode == 'cyclic' else 0)) % NOTE_COUNT
                  for i in range(LENGTH_LIMIT)] for phase in range(SONG_LIMIT)]
    elif mode == 'short_source':
        source = [47]
        songs = [[rng.randrange(NOTE_COUNT) for _ in range(LENGTH_LIMIT)] for _ in range(SONG_LIMIT)]
    elif mode == 'short_queries':
        source = [i % NOTE_COUNT for i in range(LENGTH_LIMIT)]
        songs = [[i % NOTE_COUNT] for i in range(SONG_LIMIT)]
    elif mode == 'mixed':
        source = [rng.randrange(NOTE_COUNT) for _ in range(LENGTH_LIMIT)]
        songs = [[rng.randrange(NOTE_COUNT) for _ in range(1 + i * (LENGTH_LIMIT - 1)
                                                         // (SONG_LIMIT - 1))]
                 for i in range(SONG_LIMIT)]
    else:
        raise ValueError('Unknown maximal melody mode')
    return source, songs


def render(seed, source, songs):
    serial = seed
    lines = []
    for melody in [source, *songs]:
        words = []
        for pitch in melody:
            words.append(spelling(pitch, serial + serial // NOTE_COUNT))
            serial += 1
        lines.append(str(len(melody)) + ' ' + ' '.join(words))
    return lines[0] + '\n' + str(len(songs)) + '\n' + '\n'.join(lines[1:]) + '\n'


if __name__ == '__main__':
    task_seed = int(sys.argv[1])
    sys.stdout.write(render(task_seed, *build(task_seed, sys.argv[2])))
