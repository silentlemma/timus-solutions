"""Horses for the stables: a seed, N, K and a mode. Mode 0 gives random
colours, mode 1 mostly white with a few black, mode 2 alternating colours,
mode 3 runs of one colour with random lengths."""

import random
import sys

FEW = 0.1


def main():
    seed, n, k, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 1:
        horses = [int(rng.random() < FEW) for _ in range(n)]
    elif mode == 2:
        horses = [i % 2 for i in range(n)]
    elif mode == 3:
        horses = []
        while len(horses) < n:
            horses += [rng.randint(0, 1)] * rng.randint(1, n // 10 + 1)
        horses = horses[:n]
    else:
        horses = [rng.randint(0, 1) for _ in range(n)]
    sys.stdout.write("%d %d\n" % (n, k) + "".join("%d\n" % c for c in horses))


if __name__ == "__main__":
    main()
