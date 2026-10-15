"""One test from a seed and a mode: mode 1 names of one to three letters
from "ab", often impossible, mode 2 16 problems with random names over a
few letters, mode 3 16 problems built to have an answer, mode 4 long
names sharing a prefix."""

import random
import sys

MOST = 16
LONGEST = 20
CHOICES = 3


def word(rng, letters, low, high):
    return "".join(rng.choice(letters) for _ in range(rng.randint(low, high)))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 6) if mode == 1 else MOST
    used = set()
    names = []
    for _ in range(n):
        options = []
        while len(options) < CHOICES:
            if mode == 1:
                w = word(rng, "abc", 1, 3)
            elif mode == 4:
                w = "code" + word(rng, "ab", 1, LONGEST - 4)
            else:
                w = word(rng, "abcdefghij", 1, 4)
            if w not in used:
                used.add(w)
                options.append(w)
        names.append(options)
    order = list(range(1, n + 1))
    rng.shuffle(order)
    if mode == 3:
        # one name per problem, sorted along the order, so an answer exists
        picks = sorted(rng.choice(names[i]) for i in range(n))
        for rank, p in enumerate(order):
            options = [w for w in names[p - 1] if w not in picks] + [picks[rank]]
            names[p - 1] = [w for w in options if w != picks[rank]][:CHOICES - 1] + [picks[rank]]
            rng.shuffle(names[p - 1])
    print(n)
    for options in names:
        print(*options)
    print(*order)


main()
