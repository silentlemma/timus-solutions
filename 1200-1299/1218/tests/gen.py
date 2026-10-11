"""Jedi: a seed, N and a mode. Every parameter takes N different values.
Mode 1 draws them at random, mode 2 ranks all three parameters alike so
one Jedi beats everyone, mode 3 nearly alike so a few cycles appear.
Mode 4 draws random parameters with deterministic names; mode 5 builds a
strongly connected tournament with an N-1-edge shortest win path (N >= 3),
30-letter names and shuffled input order."""

import random
import string
import sys

LIMIT = 100000
LONGEST = 30


def extended(seed, n, mode):
    rng = random.Random(seed)
    if mode == 4:
        columns = [rng.sample(range(-LIMIT, LIMIT + 1), n) for _ in range(3)]
    else:
        assert n >= 3
        # Two rankings reverse alternating adjacent pairs; the third is reversed.
        first = list(range(n))
        second = list(range(n))
        for i in range(0, n - 1, 2):
            first[i], first[i + 1] = first[i + 1], first[i]
        for i in range(1, n - 1, 2):
            second[i], second[i + 1] = second[i + 1], second[i]
        columns = [[-i for i in range(n)], first, second]
    order = list(range(n))
    rng.shuffle(order)
    lines = [str(n)]
    for i in order:
        suffix = string.ascii_uppercase[i // 26] + string.ascii_lowercase[i % 26]
        name = "J" * (LONGEST - 2) + suffix
        lines.append("%s %d %d %d" % (name, *(column[i] for column in columns)))
    sys.stdout.write("\n".join(lines) + "\n")


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    if mode in (4, 5):
        extended(seed, n, mode)
        return
    rng = random.Random(seed)
    columns = []
    for _ in range(3):
        values = sorted(rng.sample(range(-LIMIT, LIMIT + 1), n))
        if mode == 1:
            rng.shuffle(values)
        elif mode == 3:
            for _ in range(n // 10 + 1):
                i = rng.randrange(n - 1) if n > 1 else 0
                if n > 1:
                    values[i], values[i + 1] = values[i + 1], values[i]
        columns.append(values)
    names = set()
    while len(names) < n:
        size = rng.randint(1, LONGEST)
        names.add("".join(rng.choice(string.ascii_letters) for _ in range(size)))
    names = list(names)
    rng.shuffle(names)
    order = list(range(n))
    rng.shuffle(order)
    lines = [str(n)] + [
        "%s %d %d %d" % (names[i], columns[0][i], columns[1][i], columns[2][i]) for i in order
    ]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
