"""One test from a seed and a mode, N = 100 unless small. Hidden weights
are a random permutation; mode 1 weighs random pairs, mode 2 weighs every
pair, mode 3 none, mode 4 is small, mode 5 weighs neighbouring layers of
a random width and mode 6 weighs few pairs of close weights."""

import random
import sys

LARGEST = 100
SMALL = 10
NEAR = 5


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 4 else LARGEST
    weight = list(range(n))
    rng.shuffle(weight)
    density = rng.random()
    width = rng.randint(1, n)
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if weight[i] <= weight[j]:
                continue
            if mode == 2:
                weigh = True
            elif mode == 3:
                weigh = False
            elif mode == 5:
                weigh = weight[i] // width == weight[j] // width + 1
            elif mode == 6:
                weigh = weight[i] - weight[j] <= NEAR and rng.random() < density
            else:
                weigh = rng.random() < density * density
            a[i][j] = int(weigh)
    print(n)
    for row in a:
        print(" ".join(map(str, row)))


main()
