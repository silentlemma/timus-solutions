"""Random athletes: a seed, N and the mode. random: speeds from 1 to
10000; close: speeds from 9990 to 10000 (nearly equal times); divisors:
speeds among the divisors of 60, so that many inverse speeds are exact
midpoints of others; front: the three speeds add up to a constant, which
gives many possible winners; twins: random profiles in shuffled duplicate
pairs (use even N), so nobody can win alone; flat: random first and second
speeds with the third fixed at 1, reducing the race to two varying stages."""

import random
import sys

LIMIT = 10000
DIVISORS = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]


def main():
    seed, n, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    rows = []
    for _ in range(n):
        if mode == "twins":
            if _ < (n + 1) // 2:
                row = [rng.randint(1, LIMIT) for _ in range(3)]
            else:
                row = rows[_ - (n + 1) // 2][:]
        elif mode == "flat":
            row = [rng.randint(1, LIMIT), rng.randint(1, LIMIT), 1]
        elif mode == "close":
            row = [rng.randint(LIMIT - 10, LIMIT) for _ in range(3)]
        elif mode == "divisors":
            row = [rng.choice(DIVISORS) for _ in range(3)]
        elif mode == "front":
            v = rng.randint(1, LIMIT - 2)
            u = rng.randint(1, LIMIT - 1 - v)
            row = [v, u, LIMIT - v - u]
        else:
            row = [rng.randint(1, LIMIT) for _ in range(3)]
        rows.append(row)
    if mode == "twins":
        rng.shuffle(rows)
    sys.stdout.write("\n".join([str(n)] + [" ".join(map(str, r)) for r in rows]) + "\n")


if __name__ == "__main__":
    main()
