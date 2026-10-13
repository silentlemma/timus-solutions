"""Queen positions: a seed, N, S and a mode.

Mode 1 draws every coordinate at random. Mode 2 puts every coordinate in
the middle. Mode 3 keeps coordinates near the middle so that many lengths
have many directions. Mode 4 shuffles successive distances from an edge,
choosing either side at random. Mode 5 puts one random coordinate in the
middle and all others at the upper edge, making one coordinate limit reach.
"""

import random
import sys


def main():
    seed, n, s, mode = (int(a) for a in sys.argv[1:5])
    rng = random.Random(seed)
    mid = (s + 1) // 2
    if mode == 1:
        c = [rng.randint(1, s) for _ in range(n)]
    elif mode == 2:
        c = [mid] * n
    elif mode == 4:
        c = []
        for i in range(n):
            distance = i % ((s + 1) // 2)
            c.append(1 + distance if rng.randrange(2) else s - distance)
        rng.shuffle(c)
    elif mode == 5:
        c = [s] * n
        c[rng.randrange(n)] = mid
    else:
        spread = max(1, s // 10)
        c = [rng.randint(max(1, mid - spread), min(s, mid + spread)) for _ in range(n)]
    print(n, s)
    print(" ".join(map(str, c)))


main()
