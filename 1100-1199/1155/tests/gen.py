"""Duons in the eight chambers: a seed and a mode. Mode 0 draws counts and
then evens out the two sides of the cube, mode 1 leaves the sides uneven,
mode 2 puts everything into one pair of opposite corners and a few
neighbours."""

import random
import sys

TOP = 100
EVEN = [0, 2, 5, 7]
ODD = [1, 3, 4, 6]
OPPOSITE = {0: 6, 2: 4, 5: 3, 7: 1}


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        counts = [0] * 8
        u = rng.choice(EVEN)
        counts[u] = counts[OPPOSITE[u]] = rng.randint(1, TOP)
    else:
        counts = [rng.randint(0, TOP) for _ in range(8)]
        if mode == 0:
            gap = sum(counts[i] for i in EVEN) - sum(counts[i] for i in ODD)
            side = ODD if gap > 0 else EVEN
            gap = abs(gap)
            for i in side:
                add = min(TOP - counts[i], gap)
                counts[i] += add
                gap -= add
            if gap:
                for i in EVEN if side is ODD else ODD:
                    take = min(counts[i], gap)
                    counts[i] -= take
                    gap -= take
    sys.stdout.write(" ".join(map(str, counts)) + "\n")


if __name__ == "__main__":
    main()
