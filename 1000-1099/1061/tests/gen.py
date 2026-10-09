"""Random buffers: a seed, N, K, the percentage of locked buffers and the
largest value. The states are written 80 to a line."""

import random
import sys

WIDTH = 80


def main():
    seed, n, k, locked, top = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    states = "".join(
        "*" if rng.randrange(100) < locked else str(rng.randint(0, top)) for _ in range(n)
    )
    lines = ["%d %d" % (n, k)] + [states[i : i + WIDTH] for i in range(0, n, WIDTH)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
