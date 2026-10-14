"""One test from a seed and a mode: 2^N wrestlers with random names.
Mode 1 takes N = 10 and up to 40 prefectures, mode 2 a random N and few
prefectures, mode 3 N = 10 and a largest prefecture of exactly a power of
two, mode 4 names and prefectures of 30 letters."""

import random
import string
import sys

TOP = 10
MANY = 40
LONGEST = 30


def word(rng, length):
    return "".join(rng.choice(string.ascii_letters) for _ in range(length))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, TOP) if mode == 2 else TOP
    size = 1 << n
    length = LONGEST if mode == 4 else rng.randint(1, LONGEST)
    pool = [word(rng, length) for _ in range(rng.randint(1, 3 if mode == 2 else MANY))]
    prefectures = [rng.choice(pool) for _ in range(size)]
    if mode == 3:
        big = 1 << rng.randint(0, n)
        prefectures = [pool[0]] * big + [word(rng, length) + "x" for _ in range(size - big)]
        rng.shuffle(prefectures)
    print(n)
    for p in prefectures:
        print(word(rng, length), p)


main()
