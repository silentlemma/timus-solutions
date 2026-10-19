"""One set of teams from a seed and a mode: mode 1 a few teams from a
small pool of names, mode 2 a hundred teams from a large pool, mode 3 a
hundred teams forming a long chain away from Isenbaev."""

import random
import string
import sys

LIMIT = 100
SMALL = 6
CHAMPION = "Isenbaev"


def surname(rng):
    tail = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(0, 9)))
    return rng.choice(string.ascii_uppercase) + tail


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    count = rng.randint(1, SMALL) if mode == 1 else LIMIT
    pool = {CHAMPION}
    while len(pool) < (8 if mode == 1 else 2 * LIMIT + 1):
        pool.add(surname(rng))
    pool = sorted(pool)
    teams = []
    if mode == 3:
        chain = [CHAMPION] + rng.sample([p for p in pool if p != CHAMPION], 2 * LIMIT)
        for t in range(count):
            teams.append(chain[2 * t:2 * t + 3] if 2 * t + 3 <= len(chain) else rng.sample(pool, 3))
    else:
        for _ in range(count):
            teams.append(rng.sample(pool, 3))
    rng.shuffle(teams)
    print(count)
    for team in teams:
        rng.shuffle(team)
        print(*team)


main()
