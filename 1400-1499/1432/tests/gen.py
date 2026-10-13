"""Tickets of 1500 digits: a seed and a mode. Mode 1 is random digits,
mode 2 random 8s and 9s, so the answer is near the end of the range or
missing, mode 3 nines in the first half and random small digits after,
mode 4 alternating 9 and 0, mode 5 zeros in the first half and nines in
the second."""

import random
import sys

L = 1500


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        s = "".join(rng.choice("0123456789") for _ in range(L))
    elif mode == 2:
        s = "".join(rng.choice("89") for _ in range(L))
    elif mode == 3:
        s = "9" * (L // 2) + "".join(rng.choice("0123") for _ in range(L // 2))
    elif mode == 4:
        s = "90" * (L // 2)
    else:
        s = "0" * (L // 2) + "9" * (L // 2)
    print(s)


main()
