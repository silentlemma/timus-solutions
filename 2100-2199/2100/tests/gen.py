"""Responses from a seed: mode 1 random names and options, mode 2 a party of
exactly 13 before the dummy."""

import random
import string
import sys

MAX_N = 20
NAME = 20
UNLUCKY = 13
HOSTS = 2


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    while True:
        n = rng.randint(1, MAX_N)
        plus = [rng.random() < 0.5 for _ in range(n)]
        if mode == 1 or HOSTS + n + sum(plus) == UNLUCKY:
            break
    print(n)
    for p in plus:
        name = "".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, NAME)))
        print(name + ("+one" if p else ""))


main()
