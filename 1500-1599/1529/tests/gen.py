"""One test from a seed and a mode, keeping the product of n + 1 within
10000. Mode 1 takes two edges, mode 2 three to five, mode 3 up to eight
short edges, mode 4 is small, mode 5 takes two to four nearly equal edges,
the slowest shape."""

import random
import sys

LIMIT = 10000
SMALL = 300


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    k = {1: 2, 2: rng.randint(3, 5), 3: rng.randint(6, 8)}.get(mode, rng.randint(1, 3))
    if mode == 5:
        k = rng.randint(2, 4)
        side = int(round(LIMIT ** (1 / k))) - 1
        while (side + 1) ** k > LIMIT:
            side -= 1
        edges = [side - rng.randint(0, 1) for _ in range(k)]
        print(k)
        print(*edges)
        return
    room = SMALL if mode == 4 else LIMIT
    edges = []
    for i in range(k):
        # leave at least a factor of 3 for each later edge
        top = room // 3 ** (k - 1 - i) - 1
        e = rng.randint(1 if mode == 4 else 2, max(1, top))
        edges.append(e)
        room //= e + 1
    print(k)
    print(*edges)


main()
