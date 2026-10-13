"""Trees of 100 000 cities: a seed and a mode. Mode 1 is a path in order,
mode 2 a path with shuffled names and roads, mode 3 a star, mode 4 a
random tree, mode 5 a complete binary tree, mode 6 a broom: a long path
ending in a star."""

import random
import sys

N = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        roads = [(v, v + 1) for v in range(1, N)]
    elif mode == 2:
        names = list(range(1, N + 1))
        rng.shuffle(names)
        roads = [(names[v], names[v + 1]) for v in range(N - 1)]
    elif mode == 3:
        roads = [(1, v) for v in range(2, N + 1)]
    elif mode == 4:
        roads = [(v, rng.randint(1, v - 1)) for v in range(2, N + 1)]
    elif mode == 5:
        roads = [(v // 2, v) for v in range(2, N + 1)]
    else:
        half = N // 2
        roads = [(v, v + 1) for v in range(1, half)]
        roads += [(half, v) for v in range(half + 1, N + 1)]
    if mode != 1:
        rng.shuffle(roads)
        roads = [(b, a) if rng.random() < 0.5 else (a, b) for a, b in roads]
    print(N, N - 1)
    print("\n".join("%d %d" % r for r in roads))


main()
