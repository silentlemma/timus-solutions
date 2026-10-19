"""An office from a seed and a mode: mode 1 a few teams and rooms of
close areas, 2 the most teams, each taking its own room and possibly
larger ones, 3 the most teams with wide random wishes, 4 the most teams
where one team fits no room, 5 the most teams with narrow wishes around
spread-out rooms, 6 the most teams with one pair of equal rooms, 7 the
most teams with a single seating where wishes reach both to smaller
and to larger rooms, 8 the most teams with dense nested wishes ending
at their assigned room, 9 the most teams all accepting the same n - 1
rooms but excluding the largest room. Teams are shuffled so that their
order says nothing."""

import random
import sys

MOST = 1000
FEW = 6
LARGEST = 10000
CLOSE = 8


def unique_wishes(rng, ranked):
    # the team of room q reaches rooms first..last; it may reach down to
    # room p only when no room between reaches up to q
    n = len(ranked)
    last = []
    wishes = []
    for q in range(n):
        if rng.random() < 0.5:
            low = q
            while low > 0 and last[low - 1] < q:
                low -= 1
            first = rng.randint(low, q)
            last.append(q)
        else:
            first = q
            last.append(rng.randint(q, min(n - 1, q + FEW)))
        a = rng.randint(ranked[first - 1] + 1, ranked[first]) if first else rng.randint(1, ranked[0])
        top = ranked[last[q] + 1] - 1 if last[q] + 1 < n else LARGEST
        wishes.append((a, rng.randint(ranked[last[q]], top)))
    return wishes


def other_wishes(rng, mode, ranked):
    n = len(ranked)
    wishes = []
    for q, size in enumerate(ranked):
        if mode == 1:
            a, b = sorted(rng.randint(1, CLOSE) for _ in range(2))
        elif mode == 2:
            a, b = size, ranked[rng.randint(q, min(n - 1, q + FEW))]
        elif mode == 3:
            a, b = sorted(rng.randint(1, LARGEST) for _ in range(2))
            a, b = min(a, size), max(b, size)
        else:
            gap = LARGEST // n
            a = max(1, size - rng.randint(0, gap))
            b = min(LARGEST, size + rng.randint(0, gap))
        wishes.append((a, b))
    if mode == 4:
        a = rng.randint(1, LARGEST)
        while a in ranked:
            a = rng.randint(1, LARGEST)
        wishes[rng.randrange(n)] = (a, a)
    return wishes


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST
    if mode in (8, 9):
        rooms = list(range(1, LARGEST, LARGEST // n))[:n - 1] + [LARGEST]
    elif mode == 1:
        rooms = [rng.randint(1, CLOSE) for _ in range(n)]
    else:
        rooms = rng.sample(range(1, LARGEST + 1), n)
    if mode == 6:
        rooms[1] = rooms[0]
    ranked = sorted(rooms)
    if mode == 8:
        wishes = [(1, size) for size in ranked]
    elif mode == 9:
        wishes = [(1, LARGEST - 1)] * n
    else:
        wishes = unique_wishes(rng, ranked) if mode == 7 else other_wishes(rng, mode, ranked)
    rng.shuffle(rooms)
    rng.shuffle(wishes)
    print(n)
    print(*rooms)
    for a, b in wishes:
        print(a, b)


main()
