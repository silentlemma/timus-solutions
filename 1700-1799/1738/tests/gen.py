"""One test from a seed and a mode.

1: up to 200 employees with random distinct pins.
2: 65536 employees with random distinct pins.
3: all 65536 pins in shuffled order.
4: a random number of employees with random distinct pins.
5: 65536 employees with pins in increasing hexadecimal order.
6: 10000 employees with decimal employee labels as pins, ending in 0000.
"""

import random
import sys

MOST = 65536
FEW = 200
HEX = "0123456789abcdef"


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        print(MOST)
        print("\n".join("%04x" % p for p in range(MOST)))
        return
    if mode == 6:
        n = 10000
        print(n)
        print("\n".join("%04d" % (p % n) for p in range(1, n + 1)))
        return
    n = rng.randint(2, FEW) if mode == 1 else MOST if mode in (2, 3) else rng.randint(2, MOST)
    pins = ["%04x" % p for p in rng.sample(range(len(HEX) ** 4), n)]
    if mode == 3:
        pins = ["%04x" % p for p in range(n)]
        rng.shuffle(pins)
    print(n)
    print("\n".join(pins))


main()
