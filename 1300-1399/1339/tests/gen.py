"""250000 boys and as many girls: a seed and a mode. Mode 1 gives random
likes, mode 2 one cycle through all children, mode 3 one long path that
ends with a child who likes nobody, mode 4 no likes at all, mode 5 only
couples who like each other, mode 6 shuffled three-child paths in both
directions with many free ends and a mutual couple at the size boundary."""

import random
import sys

K = 250000
CHANCE = 0.6  # how often a child likes someone in mode 1


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    boys, girls = [0] * K, [0] * K
    order_b = list(range(1, K + 1))
    order_g = list(range(1, K + 1))
    rng.shuffle(order_b)
    rng.shuffle(order_g)
    if mode == 1:
        for i in range(K):
            if rng.random() < CHANCE:
                boys[i] = order_g[i]
            if rng.random() < CHANCE:
                girls[i] = order_b[i]
    elif mode in (2, 3):
        # boy order_b[i] likes girl order_g[i], who likes boy order_b[i + 1]
        for i in range(K):
            if i + 1 < K or mode == 2:
                boys[order_b[i] - 1] = order_g[i]
                girls[order_g[i] - 1] = order_b[(i + 1) % K]
    elif mode == 5:
        for i in range(K):
            boys[order_b[i] - 1] = order_g[i]
            girls[order_g[i] - 1] = order_b[i]
    elif mode == 6:
        for i in range(0, K - 2, 3):
            # One boy-boy path and one girl-girl path leave opposite-sex ends.
            boys[order_b[i] - 1] = order_g[i]
            girls[order_g[i] - 1] = order_b[i + 1]
            girls[order_g[i + 1] - 1] = order_b[i + 2]
            boys[order_b[i + 2] - 1] = order_g[i + 2]
        for i in range(K - K % 3, K):
            boys[order_b[i] - 1] = order_g[i]
            girls[order_g[i] - 1] = order_b[i]
    print(K)
    print(*boys)
    print(*girls)


main()
