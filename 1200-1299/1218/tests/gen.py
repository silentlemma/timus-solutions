"""Jedi: a seed, N and a mode. Every parameter takes N different values.
Mode 1 draws them at random, mode 2 ranks all three parameters alike so
one Jedi beats everyone, mode 3 nearly alike so a few cycles appear."""

import random
import string
import sys

LIMIT = 100000
LONGEST = 30


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
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
