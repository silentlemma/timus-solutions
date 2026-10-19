"""Street popularities from a seed.

Mode 1: small grids with values 1 to 9. Mode 2: random sizes up to 10^5 with
any values. Mode 3: the largest grid with any values. Mode 4: two vertical
streets and 10^5 horizontal streets, random interior values and a unique
horizontal maximum on the penultimate street, capped by the left street.
"""

import random
import sys

MAX_SIDE = 10 ** 5
MAX_VALUE = 10 ** 9
SMALL_SIDE = 6
SMALL_VALUE = 9


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 4:
        print(2, MAX_SIDE)
        print(MAX_VALUE - 2)
        print(MAX_VALUE)
        horizontal = [rng.randint(1, MAX_VALUE - 2) for _ in range(MAX_SIDE)]
        horizontal[0] = horizontal[-1] = 1
        horizontal[-2] = MAX_VALUE - 1
        print("\n".join(map(str, horizontal)))
        return
    if mode == 1:
        n, m, top = rng.randint(2, SMALL_SIDE), rng.randint(2, SMALL_SIDE), SMALL_VALUE
    elif mode == 2:
        n, m, top = rng.randint(2, MAX_SIDE), rng.randint(2, MAX_SIDE), MAX_VALUE
    else:
        n, m, top = MAX_SIDE, MAX_SIDE, MAX_VALUE
    print(n, m)
    print("\n".join(str(rng.randint(1, top)) for _ in range(n + m)))


main()
