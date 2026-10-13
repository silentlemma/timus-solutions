"""Sequences of 10 000 numbers: a seed and a mode. Mode 1 is random up to
10^9, mode 2 a shuffled 1 .. 10000, mode 3 random up to 20 000, mode 4 a
mix of progressions with different steps, mode 5 a long progression
ending at 10^9 among random numbers, mode 6 only 100 distinct values,
mode 7 random up to 10^5, mode 8 numbers whose base 3 digits are 0 and 1
only, which hold no three-term progression."""

import random
import sys

N = 10000
TOP = 10**9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        s = [rng.randint(1, TOP) for _ in range(N)]
    elif mode == 2:
        s = list(range(1, N + 1))
    elif mode == 3:
        s = [rng.randint(1, 2 * N) for _ in range(N)]
    elif mode == 4:
        s = []
        while len(s) < N:
            start, step = rng.randint(1, 10**6), rng.randint(1, 1000)
            s += [start + k * step for k in range(rng.randint(5, 300))]
        s = s[:N]
    elif mode == 5:
        step = 99991
        s = [TOP - k * step for k in range(N // 2)]
        s += [rng.randint(1, TOP) for _ in range(N - len(s))]
    elif mode == 6:
        values = rng.sample(range(1, TOP), 100)
        s = [rng.choice(values) for _ in range(N)]
    elif mode == 7:
        s = [rng.randint(1, 10 * N) for _ in range(N)]
    else:
        # bit patterns read in base 3
        s = rng.sample([int(bin(k)[2:], 3) for k in range(1, 2**18)], N)
    rng.shuffle(s)
    print(N)
    print(" ".join(map(str, s)))


main()
