"""One test from a seed and a mode: mode 1 up to 200 employees with
random pins, mode 2 65536 employees with random pins, mode 3 65536
employees with pins that share most digits, mode 4 a random n."""

import random
import sys

MOST = 65536
FEW = 200
HEX = "0123456789abcdef"


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST if mode in (2, 3) else rng.randint(2, MOST)
    pins = ["%04x" % p for p in rng.sample(range(len(HEX) ** 4), n)]
    if mode == 3:
        pins = ["%04x" % p for p in range(n)]
        rng.shuffle(pins)
    print(n)
    print("\n".join(pins))


main()
