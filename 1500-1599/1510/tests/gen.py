"""One test from a seed and a mode, N near 500000 unless small, with one value
on just over half of the notes. Mode 1 shuffles the notes, mode 2 puts
the majority last, mode 3 puts it first and all other notes distinct,
mode 4 is small, and mode 5 has exactly 500000 notes in three long runs:
the largest value surrounds a repeated rival with a two-vote margin."""

import random
import sys

LARGEST = 500000
TOP = 10**9
SMALL = 9


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        major = LARGEST // 2 + 1
        first = rng.randint(LARGEST // 8, 3 * LARGEST // 8)
        notes = [TOP] * first + [TOP - 1] * (LARGEST - major) + [TOP] * (major - first)
        data = "%d\n%s\n" % (LARGEST, "\n".join(map(str, notes)))
        sys.stdout.buffer.write(data.encode("ascii"))
        return
    n = rng.randint(1, SMALL) if mode == 4 else LARGEST - rng.randint(0, 1)
    major = n // 2 + 1
    value = rng.randint(0, TOP)
    if mode == 3:
        others = rng.sample(range(TOP + 1), n - major + 1)
        others = [x for x in others if x != value][: n - major]
    else:
        others = [rng.randint(0, TOP) for _ in range(n - major)]
    notes = [value] * major
    if mode == 2:
        notes = others + notes
    elif mode == 3:
        notes = notes + others
    else:
        notes += others
        rng.shuffle(notes)
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(map(str, notes))))


main()
