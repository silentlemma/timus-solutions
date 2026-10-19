"""Phrases from a seed and a mode: mode 1 a few phrases at random, 2 a
real announcement in several languages with most phrases unknown, 3 a
number of phrases with many divisors and only two known phrases, 4 the
most phrases at random from a few languages, 5 the most phrases with a
single known one. Language names are 4 to 20 lowercase letters."""

import random
import string
import sys

MOST = 1000
FEW = 8
RICH = [720, 840, 960]
SHORT, LONG = 4, 20


def name(rng):
    while True:
        w = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(SHORT, LONG)))
        if w != "unknown":
            return w


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, FEW)
        langs = [name(rng) for _ in range(2)]
        phrases = [rng.choice(langs + ["unknown"]) for _ in range(n)]
    elif mode == 2:
        n = MOST
        k = rng.choice([d for d in range(1, n + 1) if n % d == 0])
        langs = [name(rng) for _ in range(k)]
        phrases = [langs[i // (n // k)] if rng.random() < 0.3 else "unknown" for i in range(n)]
    elif mode == 3:
        n = rng.choice(RICH)
        phrases = ["unknown"] * n
        for i in rng.sample(range(n), 2):
            phrases[i] = name(rng)
    elif mode == 4:
        n = MOST
        langs = [name(rng) for _ in range(FEW)]
        phrases = [rng.choice(langs + ["unknown"] * FEW * FEW) for _ in range(n)]
    else:
        n = MOST
        phrases = ["unknown"] * n
        phrases[rng.randrange(n)] = name(rng)
    if all(p == "unknown" for p in phrases):
        phrases[0] = name(rng)
    print(n)
    print("\n".join(phrases))


main()
