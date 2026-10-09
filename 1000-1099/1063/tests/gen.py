"""Random dominoes: a seed, N and the mode. random: any faces; doubles:
mostly dominoes with equal faces (many separate groups); few: faces from
a small random set; odd: dominoes arranged to leave many odd faces."""

import random
import sys

FACES = 6


def main():
    seed, n, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    if mode == "few":
        faces = rng.sample(range(1, FACES + 1), rng.randint(2, 4))
    else:
        faces = list(range(1, FACES + 1))
    rows = []
    for _ in range(n):
        a = rng.choice(faces)
        if mode == "doubles" and rng.randrange(5):
            b = a
        elif mode == "odd":
            b = FACES + 1 - a
        else:
            b = rng.choice(faces)
        rows.append((a, b) if rng.randrange(2) else (b, a))
    sys.stdout.write("\n".join([str(n)] + ["%d %d" % r for r in rows]) + "\n")


if __name__ == "__main__":
    main()
