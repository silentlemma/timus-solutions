"""One test from a seed and a mode: mode 1 a few objects with a small
vocabulary, mode 2 the most objects and sets with long lines, mode 3
repeated associations and objects without any."""

import random
import string
import sys

MOST = 1000
LONGEST = 250


def word(rng, letters):
    return "".join(rng.choice(string.ascii_lowercase[:letters]) for _ in range(rng.randint(1, 3)))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 8) if mode == 1 else MOST
    m = rng.randint(1, 8) if mode == 1 else MOST
    letters = 6 if mode == 2 else 3
    names = set()
    while len(names) < n:
        names.add("".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(3, 8))))
    names = sorted(names)
    print(n)
    for name in names:
        words = []
        for _ in range(rng.randint(0 if mode == 3 else 1, 60)):
            w = rng.choice(words) if mode == 3 and words and rng.random() < 0.3 else word(rng, letters)
            if len(name) + 2 + len(" ".join(words + [w])) > LONGEST:
                break
            words.append(w)
        print(name + ": " + " ".join(words))
    print(m)
    for _ in range(m):
        group = [rng.choice(names), rng.choice(names)]
        while rng.random() < 0.7:
            pick = rng.choice(names)
            if len(" ".join(group + [pick])) > LONGEST:
                break
            group.append(pick)
        print(" ".join(group))


main()
