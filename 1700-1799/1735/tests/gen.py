"""One test from a seed: random n and a k within a few of the smallest
largest count that works, on either side of it."""

import math
import random
import sys

LOW, HIGH = 3, 20
SPREAD = 3
TOP_WEIGHT = 10


def main():
    rng = random.Random(int(sys.argv[1]))
    n = rng.randint(LOW, HIGH)
    u = [0, 1]
    for m in range(1, n):
        u.append(2 * u[m] - u[m - round(math.sqrt(2 * m))])
    k = max(1, u[n] + rng.randint(-SPREAD, SPREAD))
    x = rng.randint(1, TOP_WEIGHT - 1)
    print(n, k, x, rng.randint(x + 1, TOP_WEIGHT))


main()
