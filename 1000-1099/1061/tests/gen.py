"""Deterministic buffer inputs, with states written 80 to a line.

Modes:
  SEED N K LOCKED TOP: random states; LOCKED is a percentage, TOP a digit.
  last N K: all nines except a final eight; only the last window is cheapest.
"""

import random
import sys

WIDTH = 80


def main():
    if sys.argv[1] == "last":
        n, k = map(int, sys.argv[2:4])
        assert 1 <= n <= 100000 and 1 <= k <= 10000
        states = "9" * (n - 1) + "8"
    else:
        seed, n, k, locked, top = (int(x) for x in sys.argv[1:6])
        rng = random.Random(seed)
        states = "".join(
            "*" if rng.randrange(100) < locked else str(rng.randint(0, top)) for _ in range(n)
        )
    lines = ["%d %d" % (n, k)] + [states[i : i + WIDTH] for i in range(0, n, WIDTH)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
