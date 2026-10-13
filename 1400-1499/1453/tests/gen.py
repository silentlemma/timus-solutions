"""Queen positions: a seed, N, S and a mode. Mode 1 draws every coordinate
at random, mode 2 puts every coordinate in the middle, mode 3 keeps the
coordinates near the middle so that many lengths have many directions."""

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
    else:
        spread = max(1, s // 10)
        c = [rng.randint(max(1, mid - spread), min(s, mid + spread)) for _ in range(n)]
    print(n, s)
    print(" ".join(map(str, c)))


main()
