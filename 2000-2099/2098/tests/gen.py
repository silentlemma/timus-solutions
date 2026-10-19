"""b, c, d, k, p from a seed: mode 1 small values, mode 2 any values, mode 3 the
largest values, mode 4 an exact tie between the two options."""

import random
import sys

MAX_B = 10 ** 5
MAX_C = 10 ** 4
MAX_K = 100
SMALL = 10
PERCENT = 100


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            b, c, d = rng.randint(1, SMALL * SMALL), rng.randint(1, SMALL), rng.randint(1, SMALL)
            k, p = rng.randint(1, SMALL), rng.randint(1, SMALL)
        elif mode == 3:
            b, c, d, k, p = MAX_B, MAX_C, MAX_C, MAX_K, MAX_K
        else:
            b, c, d = rng.randint(1, MAX_B), rng.randint(1, MAX_C), rng.randint(1, MAX_C)
            k, p = rng.randint(1, MAX_K), rng.randint(1, MAX_K)
        if mode != 4:
            break
        # a tie: b equals p percent of the usual insurance
        usual = k * c + d * k * (k + 1) // 2
        if usual * p % PERCENT == 0 and usual * p // PERCENT <= MAX_B:
            b = usual * p // PERCENT
            break
    print(b)
    print(c, d)
    print(k, p)


main()
