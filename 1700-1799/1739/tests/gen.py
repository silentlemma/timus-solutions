"""One test from a seed and a mode: mode 1 up to 7 fruit with aromas
built from multiples of 8 and of 32, so that many sets pass, mode 2 12
fruit with any aromas, mode 3 12 fruit with aromas that are multiples
of 40, so that sprays keep sums whole, mode 4 12 fruit with aromas that
are multiples of 32."""

import random
import sys

FEW = 7
MOST = 12
TOP = 1000
STEPS = (8, 32, 40, 64, 128, 256)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, FEW)
        step = rng.choice(STEPS)
        aromas = [step * rng.randint(1, TOP // step) for _ in range(n)]
    elif mode == 2:
        aromas = [rng.randint(1, TOP) for _ in range(MOST)]
    else:
        step = {3: 40, 4: 32}[mode]
        aromas = [step * rng.randint(1, TOP // step) for _ in range(MOST)]
    print(len(aromas))
    print(" ".join(map(str, aromas)))


main()
