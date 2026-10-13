"""1000 games from a seed and a mode: mode 1 deals from the whole deck,
mode 2 from a few ranks only (pairs, triples and draws are common), mode
3 often puts the players' own cards into the sleeve."""

import random
import sys

GAMES = 1000
NAMES = [str(x) for x in range(2, 11)] + list("JQKA")
DECK = [n + s for n in NAMES for s in "SCDH"]
FEW = 3


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    games = []
    for _ in range(GAMES):
        if mode == 2:
            names = rng.sample(NAMES, FEW)
            pool = [c for c in DECK if c[:-1] in names]
        else:
            pool = DECK
        six = rng.sample(pool, 6)
        if mode == 3:
            sleeve = [rng.choice(six if rng.random() < 0.5 else DECK) for _ in range(2)]
        else:
            sleeve = [rng.choice(pool) for _ in range(2)]
        games.append("%s\n%s\n%s" % (" ".join(six[:3]), " ".join(six[3:]), " ".join(sleeve)))
    print("\n\n".join(games))


main()
