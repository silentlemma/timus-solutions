"""A strip from a seed.

Mode 1: a short strip whose length is a power of two. Mode 2: the longest
strip of length 2^18 at random. Mode 3: a long strip of mostly one colour.
Mode 4: the longest strip, 5 * 10^5, which folds only twice.
Mode 5: a random strip of length 3 * 2^17, ending at odd length after 17 folds.
"""

import random
import sys

SMALL = 4
LONGEST = 2 ** 18
MAX_N = 5 * 10 ** 5


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n = {1: 2 ** rng.randint(0, SMALL), 2: LONGEST, 3: LONGEST}.get(mode, MAX_N)
    if mode == 5:
        n = 3 * 2 ** 17
    weights = "AB" if mode != 3 else rng.choice(["AAAAAAAB", "ABBBBBBB"])
    print(n)
    for _ in range(2):
        print("".join(rng.choice(weights) for _ in range(n)))


main()
