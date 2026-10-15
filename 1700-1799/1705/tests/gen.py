"""One test from a seed and a mode: mode 1 small n, mode 2 the most tests
with n up to 10^18, mode 3 n near squares and products s (s + 1)."""

import random
import sys

MOST_T = 30000
MOST_N = 10 ** 18
ROOT = 10 ** 9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(1, 10 ** 6) for _ in range(rng.randint(1, 100))]
    elif mode == 2:
        values = [rng.randint(1, MOST_N) for _ in range(MOST_T)]
    else:
        values = []
        while len(values) < MOST_T:
            s = rng.randint(2, ROOT - 1)
            values.append(s * s + rng.choice((-1, 0, 1, s - 1, s, s + 1, 2 * s)))
    print(len(values))
    print("\n".join(map(str, values)))


main()
