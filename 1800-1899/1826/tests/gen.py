"""One squad from a seed and a mode: mode 1 a few random soldiers,
mode 2 a hundred random soldiers, mode 3 a hundred with two fast ones
and the rest slow, so pairing the slow ones pays, mode 4 a hundred
with close times, so the fastest escorting everyone pays."""

import random
import sys

LIMIT = 100
SLOWEST = 600
SMALL = 8


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 1 else LIMIT
    if mode == 3:
        times = [rng.randint(1, 3), rng.randint(1, 5)]
        times += [rng.randint(SLOWEST // 2, SLOWEST) for _ in range(n - 2)]
    elif mode == 4:
        base = rng.randint(1, SLOWEST - 10)
        times = [base + rng.randint(0, 10) for _ in range(n)]
    else:
        times = [rng.randint(1, SLOWEST) for _ in range(n)]
    rng.shuffle(times)
    print(n)
    print("\n".join(map(str, times)))


main()
