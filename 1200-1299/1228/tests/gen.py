"""An array shape: a seed, the number of dimensions and the largest upper
bound. The bounds are drawn so that the array has fewer than 2^31 - 1
elements, leaving room for every later dimension to have two."""

import random
import sys

LIMIT = 2**31 - 1


def main():
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    bounds, total = [], 1
    for i in range(n):
        rest = 2 ** (n - 1 - i)
        k = rng.randint(1, top)
        while k > 1 and total * (k + 1) * rest >= LIMIT:
            k //= 2
        bounds.append(k)
        total *= k + 1
    factors = [1]
    for k in reversed(bounds[1:]):
        factors.append(factors[-1] * (k + 1))
    factors.reverse()
    lines = ["%d %d" % (n, total)] + [str(d) for d in factors]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
