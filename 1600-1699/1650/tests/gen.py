"""One test from a seed and a mode: mode 1 a few people and cities with
round fortunes that often tie, mode 2 the largest sizes, mode 3 two equal
fortunes chasing each other between two cities."""

import random
import sys

MOST_PEOPLE = 10000
MOST_DAYS = 50000
MOST_MOVES = 50000
BILLION = 10**9
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def word(rng, low, high):
    return "".join(rng.choice(LETTERS) for _ in range(rng.randint(low, high)))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m, k, towns = rng.randint(1, 6), rng.randint(1, 30), rng.randint(0, 20), 4
    elif mode == 2:
        n, m, k, towns = MOST_PEOPLE, MOST_DAYS, MOST_MOVES, 3000
    else:
        n, m, k, towns = 2, rng.randint(2, 30), 0, 2
    people = set()
    while len(people) < n:
        people.add(word(rng, 1, 20))
    people = sorted(people, key=lambda p: rng.random())
    cities = set()
    while len(cities) < towns:
        cities.add(word(rng, 1, 20))
    cities = sorted(cities)
    lines = [str(n)]
    where = {}
    for i, p in enumerate(people):
        money = rng.randint(1, 3) * BILLION if mode != 2 else rng.randint(1, 100 * BILLION)
        where[p] = cities[i] if mode == 3 else rng.choice(cities)
        lines.append("%s %s %d" % (p, where[p], 5 * BILLION if mode == 3 else money))
    if mode == 3:
        days = [day for day in range(1, m) if rng.random() < 0.5]
    else:
        days = sorted(rng.randint(1, max(1, m - 1)) for _ in range(k)) if m > 1 else []
    moves, moved = [], set()
    for day in days:
        who = rng.choice(people)
        choices = cities + [word(rng, 1, 20)] if mode == 1 else cities
        to = rng.choice(choices)
        if (day, who) in moved or to == where[who]:
            continue  # one trip a day, and always to another city
        moved.add((day, who))
        where[who] = to
        moves.append((day, who, to))
    lines.append("%d %d" % (m, len(moves)))
    lines += ["%d %s %s" % mv for mv in moves]
    print("\n".join(lines))


main()
