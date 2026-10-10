"""Random fleets: a seed, N, M, the largest ship and a mode. The ships are
dealt into M rows at random and each row length is the sum of its ships,
so a placement exists. Mode 0 draws any lengths, mode 1 draws lengths from
a narrow band (many ways to fill a row partly, few to finish all rows),
mode 2 draws mostly equal ships with a few odd ones."""

import random
import sys

BAND = 3
ODD = 0.1


def main():
    seed, n, m, top, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    if mode == 1:
        low = rng.randint(1, max(1, top - BAND))
        ships = [rng.randint(low, min(top, low + BAND)) for _ in range(n)]
    elif mode == 2:
        common = rng.randint(1, top)
        ships = [rng.randint(1, top) if rng.random() < ODD else common for _ in range(n)]
    else:
        ships = [rng.randint(1, top) for _ in range(n)]
    owner = list(range(m)) + [rng.randrange(m) for _ in range(n - m)]
    rng.shuffle(owner)
    rows = [0] * m
    for s, r in zip(ships, owner):
        rows[r] += s
    lines = ["%d %d" % (n, m)] + [str(s) for s in ships] + [str(r) for r in rows]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
