"""One test from a seed and a mode: mode 1 is a real game of 100000
balls, mode 2 a random order, mode 3 a real game with two balls swapped,
mode 4 takes the balls out in reverse order, mode 5 in the rolling order,
mode 6 is a small real game or a small random order."""

import random
import sys

LARGEST = 100000
SMALL = 8


def real(rng, n):
    pocket, out = [], []
    ball = 1
    while len(out) < n:
        if ball <= n and (not pocket or rng.random() < 0.5):
            pocket.append(ball)
            ball += 1
        else:
            out.append(pocket.pop())
    return out


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 6 else LARGEST
    if mode in (1, 3) or (mode == 6 and rng.random() < 0.5):
        order = real(rng, n)
        if mode == 3:
            i, j = rng.sample(range(n), 2)
            order[i], order[j] = order[j], order[i]
    elif mode == 4:
        order = list(range(n, 0, -1))
    elif mode == 5:
        order = list(range(1, n + 1))
    else:
        order = list(range(1, n + 1))
        rng.shuffle(order)
    print(n)
    print("\n".join(map(str, order)))


main()
