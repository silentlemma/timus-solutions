"""One test from a seed and a mode: up to 1000 shop names of letters and
spaces. Mode 1 draws 1000 names from a pool of 50, mode 2 gives 1000
different names, mode 3 uses names that differ only in their spaces."""

import random
import string
import sys

SHOPS = 1000
POOL = 50
LONGEST = 30


def name(rng):
    size = rng.randint(1, LONGEST)
    letters = [rng.choice(string.ascii_letters + " ") for _ in range(size)]
    # keep the ends as letters, so no line starts or ends with a space
    letters[0] = rng.choice(string.ascii_letters)
    letters[-1] = rng.choice(string.ascii_letters)
    return "".join(letters)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        pool = [name(rng) for _ in range(POOL)]
        names = [rng.choice(pool) for _ in range(SHOPS)]
    elif mode == 2:
        seen = set()
        while len(seen) < SHOPS:
            seen.add(name(rng))
        names = list(seen)
        rng.shuffle(names)
    else:
        names = []
        for _ in range(SHOPS):
            gaps = [rng.randint(1, 3) for _ in range(3)]
            names.append("A" + " " * gaps[0] + "B" + " " * gaps[1] + "C" + " " * gaps[2] + "D")
    print(len(names))
    print("\n".join(names))


main()
