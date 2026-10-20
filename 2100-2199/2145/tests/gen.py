"""Students, problems and p from a seed: mode 1 small random values for a
brute-force check, mode 2 the maximum n with random values, mode 3 the
maximum n where every student solves every problem, mode 4 the maximum n
where the problems are just one step too hard for one student."""

import random
import sys

MAX_N = 10 ** 5
MAX_V = 10 ** 9
SMALL_N = 7
SMALL_V = 5
PRIME = 999999937  # a prime below 10^9, so n! does not vanish modulo it


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        a = [rng.randint(0, SMALL_V) for _ in range(n)]
        b = [rng.randint(0, SMALL_V) for _ in range(n)]
        p = rng.randint(1, MAX_V)
    elif mode == 2:
        n = MAX_N
        a = [rng.randint(0, MAX_V) for _ in range(n)]
        b = [x - rng.randint(0, x) for x in a]
        rng.shuffle(b)
        p = rng.randint(1, MAX_V)
    elif mode == 3:
        n = MAX_N
        a = [MAX_V] * n
        b = [rng.randint(0, MAX_V) for _ in range(n)]
        p = PRIME
    else:
        n = MAX_N
        a = sorted(rng.randint(1, MAX_V) for _ in range(n))
        b = a[:]
        b[rng.randrange(n)] += 1
        rng.shuffle(a)
        p = rng.randint(1, MAX_V)
    print(n)
    print(*a)
    print(*b)
    print(p)


main()
