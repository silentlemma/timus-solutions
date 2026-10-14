"""One test from a seed and a mode, with N distinct notes in increasing
order. Mode 1 takes 100 random notes, mode 2 grows the notes slowly
from 1, so the sums cover a long range before a gap, mode 3 takes few
small notes."""

import random
import sys

LARGEST = 100
TOP = 10**6
SMALL = 6


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        notes, reach = [], 0
        while len(notes) < LARGEST:
            note = min(TOP, rng.randint((notes[-1] if notes else 0) + 1, reach + 2))
            if notes and note <= notes[-1]:
                break
            notes.append(note)
            reach += note
    elif mode == 3:
        notes = sorted(rng.sample(range(1, SMALL * 2), rng.randint(1, SMALL)))
    else:
        notes = sorted(rng.sample(range(1, TOP + 1), LARGEST))
    print(len(notes))
    print(" ".join(map(str, notes)))


main()
