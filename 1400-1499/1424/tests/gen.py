"""Trips for 50 000 people: a seed and a mode. Mode 1 has random trips
on 100 000 stops with 1000 seats, mode 2 short random trips with one
seat, mode 3 everyone riding from the first stop to the last, mode 4
nested trips around the middle stop with 300 seats."""

import random
import sys

N = 100000
K = 50000


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    trips = []
    if mode == 1:
        m = 1000
        for _ in range(K):
            s = rng.randint(1, N - 1)
            trips.append((s, rng.randint(s + 1, N)))
    elif mode == 2:
        m = 1
        for _ in range(K):
            s = rng.randint(1, N - 1)
            trips.append((s, min(N, s + rng.randint(1, 20))))
    elif mode == 3:
        m = 1000
        trips = [(1, N)] * K
    else:
        m = 300
        for _ in range(K):
            d = rng.randint(1, N // 2 - 1)
            trips.append((N // 2 - d, N // 2 + d))
    print(N, m, K, rng.randint(1, 10000))
    print("\n".join("%d %d" % t for t in trips))


main()
