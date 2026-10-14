"""One test from a seed and a mode: up to 100 teams. Mode 1 gives 100
different languages, mode 2 the same with english among them, mode 3
repeats one language once, mode 4 is small."""

import random
import sys

TEAMS = 100
SMALL = 5
LONGEST = 10


def language(rng):
    return "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, LONGEST)))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 4 else TEAMS
    langs = set()
    if mode == 2:
        langs.add("english")
    while len(langs) < n:
        langs.add(language(rng))
    langs = list(langs)
    if mode == 3:
        langs[rng.randrange(n)] = langs[rng.randrange(n)]
    rng.shuffle(langs)
    print(n)
    print("\n".join(langs))


main()
