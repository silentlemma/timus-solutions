"""One graph from a seed and a mode: mode 1 picks each of the roads among
14 stops with a random probability, mode 2 keeps nine roads in ten, mode
3 one in five, mode 4 is a ring of 14 stops with a few chords."""

import random
import sys

STOPS = 14
DENSE, SPARSE = 0.9, 0.2
CHORDS = 3


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    pairs = [(a, b) for a in range(1, STOPS + 1) for b in range(a + 1, STOPS + 1)]
    if mode == 4:
        roads = {(i, i % STOPS + 1) for i in range(1, STOPS + 1)}
        roads |= set(rng.sample(pairs, CHORDS))
        roads = {(min(a, b), max(a, b)) for a, b in roads}
    else:
        chance = {1: rng.random(), 2: DENSE, 3: SPARSE}[mode]
        roads = {p for p in pairs if rng.random() < chance}
    roads = [(b, a) if rng.random() < 0.5 else (a, b) for a, b in sorted(roads)]
    rng.shuffle(roads)
    print(STOPS, len(roads))
    for a, b in roads:
        print(a, b)


main()
