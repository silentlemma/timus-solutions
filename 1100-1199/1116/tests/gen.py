"""Two random piecewise-constant functions: a seed, the interval counts of
both, the largest gap between intervals and the largest width. Neighbours
never share a value when they touch."""

import random
import sys

BOUND = 31999
VALUE = 100


def one(rng, n, gap, width):
    out = []
    x = -BOUND
    for _ in range(n):
        a = x + rng.randint(0, gap)
        b = a + rng.randint(1, width)
        if b > BOUND:
            break
        y = rng.randint(-VALUE, VALUE)
        while out and out[-1][1] == a and out[-1][2] == y:
            y = rng.randint(-VALUE, VALUE)
        out.append((a, b, y))
        x = b
    return " ".join([str(len(out))] + ["%d %d %d" % p for p in out])


def main():
    seed, n1, n2, gap, width = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    sys.stdout.write(one(rng, n1, gap, width) + "\n" + one(rng, n2, gap, width) + "\n")


if __name__ == "__main__":
    main()
