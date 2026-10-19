"""Medallists and forecasts from a seed and a mode: mode 1 a few
forecasters, 2 the most forecasters with random forecasts, 3 the most
forecasters guessing among the medallists only, 4 the most forecasters
with empty or tiny forecasts, 5 the most forecasters with full and
nearly right forecasts. Names are 1 to 30 letters, underscores, dots
and commas; every forecast gives a team at most one medal and each
medal to at most four teams."""

import random
import string
import sys

MOST = 100
FEW = 4
LONGEST = 30
PLACES = 12
PER_MEDAL = 4
MEDALS = ["gold", "silver", "bronze"]
CHARS = string.ascii_letters + "_.,"


def name(rng):
    return "".join(rng.choice(CHARS) for _ in range(rng.randint(1, LONGEST)))


def forecast(rng, mode, teams, pool):
    if mode == 4:
        size = rng.randint(0, 1)
    elif mode == 5:
        size = PLACES
    else:
        size = rng.randint(0, PLACES)
    chosen = rng.sample(teams if mode == 3 else pool, size)
    if mode == 5:
        chosen = list(teams)
        i, j = rng.sample(range(PLACES), 2)
        chosen[i], chosen[j] = chosen[j], chosen[i]
        return ["%s : %s" % (t, MEDALS[k // PER_MEDAL]) for k, t in enumerate(chosen)]
    kinds = [m for m in MEDALS for _ in range(PER_MEDAL)]
    rng.shuffle(kinds)
    return ["%s : %s" % (t, k) for t, k in zip(chosen, kinds)]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    names = set()
    while len(names) < PLACES * 2:
        names.add(name(rng))
    pool = sorted(names)
    rng.shuffle(pool)
    teams = pool[:PLACES]
    n = rng.randint(1, FEW) if mode == 1 else MOST
    lines = teams + [str(n)]
    for _ in range(n):
        lines_of = forecast(rng, mode, teams, pool)
        lines += [str(len(lines_of))] + lines_of
    print("\n".join(lines))


main()
