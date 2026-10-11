"""Stones: a seed, N, a step d and a direction (1 ascending, 0
descending). Distinct weights are put in sorted order and then shuffled
within each class of positions modulo d, so K = d - 1 works and usually
nothing larger does; d = 0 shuffles them all."""

import random
import sys

TOP = 130000


def main():
    seed, n, d, up = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    stones = sorted(rng.sample(range(1, TOP + 1), n), reverse=not up)
    if d == 0:
        rng.shuffle(stones)
    else:
        for r in range(d):
            part = stones[r::d]
            rng.shuffle(part)
            stones[r::d] = part
    sys.stdout.write("\n".join([str(n)] + [str(x) for x in stones]) + "\n")


if __name__ == "__main__":
    main()
