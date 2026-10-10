"""Random kindergartens: a seed, N, the number of doors and a mode. Mode 0
places doors between random rooms, mode 1 repeats a few pairs of rooms
many times, mode 2 builds a ring of rooms with chords."""

import random
import sys

PAIRS = 5


def main():
    seed, n, doors, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    rows = [[] for _ in range(n)]
    pool = [tuple(rng.sample(range(n), 2)) for _ in range(PAIRS)]
    for k in range(doors):
        if mode == 1:
            u, v = rng.choice(pool)
        elif mode == 2 and k < n:
            u, v = k, (k + 1) % n
        else:
            u, v = rng.sample(range(n), 2)
        rows[u].append(v)
        rows[v].append(u)
    lines = [str(n)] + [" ".join(map(str, [len(r)] + sorted(x + 1 for x in r))) for r in rows]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
