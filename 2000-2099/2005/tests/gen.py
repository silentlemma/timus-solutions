"""Usage: gen.py SEED MODE; zero,limit,line,star,random."""

import random
import sys

POINTS = 5
LIMIT = 10000


def generate(seed, mode):
    if mode == "zero":
        return [[0] * POINTS for _ in range(POINTS)]
    if mode == "limit":
        return [[0 if i == j else LIMIT for j in range(POINTS)] for i in range(POINTS)]
    if mode == "line":
        positions = [0, LIMIT, LIMIT // 2, LIMIT // 4, LIMIT * 3 // 4]
        return [[abs(a - b) for b in positions] for a in positions]
    if mode == "star":
        weights = [0] + [LIMIT // 2] * (POINTS - 1)
        return [
            [0 if i == j else a + b for j, b in enumerate(weights)] for i, a in enumerate(weights)
        ]
    if mode != "random":
        raise ValueError("unknown mode")
    rng = random.Random(seed)
    distance = [[0] * POINTS for _ in range(POINTS)]
    for i in range(POINTS):
        for j in range(i):
            distance[i][j] = distance[j][i] = rng.randint(0, LIMIT)
    for k in range(POINTS):
        for i in range(POINTS):
            for j in range(POINTS):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


if __name__ == "__main__":
    for row in generate(int(sys.argv[1]), sys.argv[2]):
        print(*row)
