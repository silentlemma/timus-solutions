"""One test from a seed and a mode: an envelope and a card, both proper
triangles with sides up to 1000. Mode 1 draws both at random, mode 2
shrinks the envelope a little and shuffles the sides, mode 3 uses an
obtuse envelope, mode 4 small sides."""

import random
import sys

TOP = 1000
SMALL = 20


def proper(sides):
    a, b, c = sorted(sides)
    return a + b > c


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 4 else TOP
    while True:
        env = [rng.randint(1, top) for _ in range(3)]
        if mode == 3:
            a, b = rng.randint(top // 4, top // 2), rng.randint(top // 4, top // 2)
            env = [a, b, rng.randint(int((a * a + b * b) ** 0.5) + 1, a + b - 1)]
        if proper(env):
            break
    while True:
        if mode == 2:
            k = rng.uniform(0.85, 1.0)
            card = [max(1, round(x * k) + rng.randint(-2, 2)) for x in env]
            rng.shuffle(card)
        else:
            card = [rng.randint(1, max(env)) for _ in range(3)]
        if proper(card):
            break
    print(*env)
    print(*card)


main()
