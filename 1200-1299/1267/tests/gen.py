"""A metro line: a seed and a mode. Mode 1 draws short gaps and periods,
mode 2 gaps and periods up to 10^5, mode 3 many zero gaps (stations at
the same place). N is 16 in every second test."""

import random
import sys

STATIONS = 16
TOP = 10**5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = STATIONS if seed % 2 == 0 else rng.randint(1, STATIONS)
    top = 20 if mode == 1 else TOP
    if mode == 3:
        gaps = [rng.choice([0, 0, rng.randint(1, top)]) for _ in range(n - 1)]
    else:
        gaps = [rng.randint(0, top) for _ in range(n - 1)]
    period = rng.randint(1, top)
    first_up, first_down = rng.randint(0, period), rng.randint(0, period)
    sys.stdout.write(
        "%d\n%s\n%d\n%d %d %d\n"
        % (n, " ".join(map(str, gaps)), rng.randint(1, n), period, first_up, first_down)
    )


if __name__ == "__main__":
    main()
