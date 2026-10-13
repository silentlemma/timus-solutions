"""Numbers of 2000 digits: a seed and a mode. Mode 1 is random digits,
mode 2 a long run of nines after a few digits, mode 3 the largest number
of its digit sum, which has no next one, mode 4 a single 1 among zeros
near the end."""

import random
import sys

K = 2000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        digits = [rng.randint(0, 9) for _ in range(K)]
    elif mode == 2:
        digits = [0, 3] + [9] * (K - 5) + [0, 0, 0]
    elif mode == 3:
        total = rng.randint(1, 9 * K)
        digits = []
        for _ in range(K):
            digits.append(min(9, total))
            total -= digits[-1]
    else:
        digits = [0] * K
        digits[K - 5] = 1
    print("".join(map(str, digits)))


main()
