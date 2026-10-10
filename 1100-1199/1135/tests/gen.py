"""A row of N recruits split into lines of at most 255 characters: a seed,
N and a mode. Mode 0 is random, mode 1 puts everybody facing right before
everybody facing left (the most turns), mode 2 is already stable, mode 3
alternates, mode 4 has random lines of random length."""

import random
import sys

WIDTH = 255


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        row = ">" * (n // 2) + "<" * (n - n // 2)
    elif mode == 2:
        k = rng.randint(0, n)
        row = "<" * k + ">" * (n - k)
    elif mode == 3:
        row = "><" * (n // 2) + ">" * (n % 2)
    else:
        row = "".join(rng.choice("<>") for _ in range(n))
    lines = []
    pos = 0
    while pos < n:
        width = rng.randint(1, WIDTH) if mode == 4 else WIDTH
        lines.append(row[pos : pos + width])
        pos += width
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(lines)))


if __name__ == "__main__":
    main()
