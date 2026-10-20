"""Heaps from "MODE SEED": mode 1 a few small heaps, mode 2 10^5 random
heaps and proportions, mode 3 10^5 heaps close to a multiple of the
proportion, mode 4 proportions with a common factor and huge values."""

import random
import sys

MAX_N = 10 ** 5
MAX_V = 10 ** 9
SMALL_N = 5
SMALL_V = 12
NOISE = 3


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, SMALL_N)
        s = [rng.randint(1, SMALL_V) for _ in range(n)]
        p = [rng.randint(1, SMALL_V) for _ in range(n)]
    elif mode == 2:
        n = MAX_N
        s = [rng.randint(1, MAX_V) for _ in range(n)]
        p = [rng.randint(1, MAX_V) for _ in range(n)]
    elif mode == 3:
        n = MAX_N
        p = [rng.randint(1, SMALL_V) for _ in range(n)]
        k = rng.randint(1, MAX_V // SMALL_V)
        s = [max(1, k * v + rng.randint(-NOISE, NOISE)) for v in p]
    else:
        n = MAX_N
        factor = rng.randint(2, SMALL_V)
        p = [factor * rng.randint(1, MAX_V // factor) for _ in range(n)]
        s = [rng.choice([1, MAX_V]) for _ in range(n)]
    print(n)
    print(*s)
    print(*p)


main()
