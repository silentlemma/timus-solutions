"""One test from a seed and a mode. Mode 1: random roads in a house of up
to 12 doors, from and to the two doors farthest apart. Mode 2: the largest
house with the most inner houses and many roads, random doors. Mode 3: a
chain like the first example, door i joined to door i + 1 of any house,
from the first door to the last. Mode 4: a small random labyrinth, the
doors farthest apart."""

import random
import sys

MOST_DOORS = 20
MOST_HOUSES = 5
INF = float("inf")


def distances(n, k, roads):
    """the door-to-door distances of the outer house, by the fixed point"""
    size = (k + 1) * n
    inside = [[INF] * n for _ in range(n)]
    while True:
        w = [[INF] * size for _ in range(size)]
        for (h1, d1), (h2, d2) in roads:
            u, v = h1 * n + d1, h2 * n + d2
            w[u][v] = w[v][u] = 1
        for h in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    w[h * n + i][h * n + j] = min(w[h * n + i][h * n + j], inside[i][j])
        for i in range(size):
            w[i][i] = 0
        for mid in range(size):
            for i in range(size):
                if w[i][mid] < INF:
                    for j in range(size):
                        if w[i][mid] + w[mid][j] < w[i][j]:
                            w[i][j] = w[i][mid] + w[mid][j]
        nxt = [row[:n] for row in w[:n]]
        if nxt == inside:
            return inside
        inside = nxt


def random_roads(rng, n, k, want):
    doors = [(h, d) for h in range(k + 1) for d in range(n)]
    want = min(want, len(doors) * (len(doors) - 1) // 2)  # no more roads than pairs
    roads = set()
    while len(roads) < want:
        a, b = rng.sample(doors, 2)
        if (b, a) not in roads:
            roads.add((a, b))
    return sorted(roads)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        n, k = MOST_DOORS, MOST_HOUSES
        roads = random_roads(rng, n, k, 6 * n)
        ends = (rng.randrange(n), rng.randrange(n))
    elif mode == 3:
        # as in the first example: odd door d to d + 1 in the outer house,
        # so an inner house leads from d to d + 1 as well; the even steps
        # hop between inner houses, and the ends join the outer house
        n, k = 2 * rng.randint(2, MOST_DOORS // 2), rng.randint(1, MOST_HOUSES)
        house = rng.randint(1, k)  # the inner house the path is in
        roads = [((0, 0), (house, 1))]
        for d in range(1, n - 2):
            if d % 2:
                roads.append(((0, d), (0, d + 1)))
            else:
                nxt = rng.randint(1, k)
                roads.append(((house, d), (nxt, d + 1)))
                house = nxt
        roads.append(((house, n - 2), (0, n - 1)))
        ends = (0, n - 1)
    else:
        n = rng.randint(2, 12 if mode == 1 else 5)
        k = rng.randint(0, 3 if mode == 1 else 2)
        roads = random_roads(rng, n, k, rng.randint(n, 3 * n))
        dist = distances(n, k, roads)
        pairs = [(dist[i][j], i, j) for i in range(n) for j in range(n) if dist[i][j] < INF]
        _, i, j = max(pairs)
        ends = (i, j)
    print(n, k)
    print(len(roads))
    for (h1, d1), (h2, d2) in roads:
        print("%d.%d - %d.%d" % (h1, d1, h2, d2))
    print(*ends)


main()
