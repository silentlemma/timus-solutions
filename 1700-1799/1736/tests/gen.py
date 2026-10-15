"""One test from a seed and a mode: mode 1 the table of a random season
of up to 8 teams, mode 2 the same for 200 teams, mode 3 the season of 200
teams where every team beats all weaker ones, with points moved between
teams, so that the table is often impossible, mode 4 the
season where every team beats all weaker ones, with the two weakest
teams made level at the bottom so that it breaks, mode 5 that season
of 200 teams as it is."""

import random
import sys

WIN = 3
FEW = 8
MOST = 200
MOVES = 3


def season(rng, n):
    score = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            r = rng.randint(0, WIN)
            score[i] += r
            score[j] += WIN - r
    return score


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST
    if mode >= 3:
        score = [WIN * i for i in range(n)]
    if mode == 4:
        score[0] += 1
        score[1] -= 2
        score[2] += 1
    elif mode < 3:
        score = season(rng, n)
    if mode == 3:
        for _ in range(MOVES):
            i, j = rng.randrange(n), rng.randrange(n)
            step = rng.randint(1, WIN)
            if score[i] >= step and score[j] + step <= WIN * (n - 1):
                score[i] -= step
                score[j] += step
    score.sort(reverse=True)
    print(n)
    print(" ".join(map(str, score)))


main()
