"""Games from a seed and a mode: mode 1 deals 1000 from the whole deck,
mode 2 from a few ranks only (pairs, triples and draws are common), mode
3 often puts the players' own cards into the sleeve. Mode 4 deals two
flushes, mode 5 deals two straights, mode 6 tries all 2704 ordered sleeve
pairs against one fixed deal, and mode 7 mixes 20000 games from modes
1, 2, 4 and 5. All modes take a seed followed by the mode number."""

import random
import sys

GAMES = 1000
NAMES = [str(x) for x in range(2, 11)] + list("JQKA")
DECK = [n + s for n in NAMES for s in "SCDH"]
FEW = 3


def flushes(rng):
    first_suit, second_suit = rng.sample("SCDH", 2)
    first = [n + first_suit for n in rng.sample(NAMES, 3)]
    second = [n + second_suit for n in rng.sample(NAMES, 3)]
    return first + second


def straights(rng):
    first_low, second_low = rng.randrange(11), rng.randrange(11)
    first = [NAMES[i] + rng.choice("SCDH") for i in range(first_low, first_low + 3)]
    second = [
        NAMES[i] + rng.choice([s for s in "SCDH" if NAMES[i] + s not in first])
        for i in range(second_low, second_low + 3)
    ]
    rng.shuffle(first)
    rng.shuffle(second)
    return first + second


def structured(seed, mode):
    rng = random.Random(seed)
    games = []
    if mode == 6:
        deck = DECK[:]
        rng.shuffle(deck)
        six = ["7S", "8S", "9S", "3H", "3D", "2C"]
        for first in deck:
            for second in deck:
                games.append(six + [first, second])
    elif mode in (4, 5, 7):
        count = 20000 if mode == 7 else GAMES
        for _ in range(count):
            kind = rng.choice((1, 2, 4, 5)) if mode == 7 else mode
            pool = DECK
            if kind == 4:
                six = flushes(rng)
            elif kind == 5:
                six = straights(rng)
            else:
                if kind == 2:
                    names = rng.sample(NAMES, FEW)
                    pool = [c for c in DECK if c[:-1] in names]
                six = rng.sample(pool, 6)
            sleeve = [rng.choice(pool) for _ in range(2)]
            games.append(six + sleeve)
    else:
        raise ValueError("unknown mode")
    print("\n\n".join(
        "%s\n%s\n%s" % (" ".join(g[:3]), " ".join(g[3:6]), " ".join(g[6:]))
        for g in games
    ))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    if mode >= 4:
        structured(seed, mode)
        return
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
