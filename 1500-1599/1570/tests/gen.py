"""One test from a seed and a mode: a menu and a company. Mode 1 is 100
dishes and 20 friends, mode 2 makes many dishes equally good per rouble,
mode 3 has dishes too small to feed even one person, mode 4 is small."""

import random
import sys

DISHES = 100
FRIENDS = 20
SMALL = 5


def name(rng, taken):
    while True:
        word = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 30)))
        if word not in taken:
            taken.add(word)
            return word


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 4 else DISHES
    m = rng.randint(1, SMALL) if mode == 4 else FRIENDS
    taken = set()
    print(n, m)
    for _ in range(n):
        if mode == 2:
            # price 100 roubles per person, so many orders cost the same
            fill = rng.randint(1, 100) * 100
            price = fill // 10
        elif mode == 3:
            fill = rng.randint(100, 999)
            price = rng.randint(1, 10000)
        else:
            fill = rng.randint(100, 10000)
            price = rng.randint(1, 10000)
        print(name(rng, taken), price, "%d.%03d" % (fill // 1000, fill % 1000))


main()
