"""A random pattern: a seed, N, M, the percentages of empty cells on the
front and on the back, and optionally the characters of the other cells
(by default "/", "\\" and "X", with equal chances)."""

import random
import sys


def main():
    seed, n, m, front_empty, back_empty = (int(x) for x in sys.argv[1:6])
    cells = sys.argv[6] if len(sys.argv) > 6 else "/\\X"
    rng = random.Random(seed)
    lines = ["%d %d" % (n, m)]
    for empty in (front_empty, back_empty):
        for _ in range(n):
            row = "".join(
                "." if rng.randrange(100) < empty else rng.choice(cells) for _ in range(m)
            )
            lines.append(row)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
