"""Deterministic company sizes.

random SEED N LOW HIGH: N independent sizes uniformly in [LOW, HIGH].
dominant SEED N PEAK: one company of PEAK, at a random position, and
N-1 random companies small enough that at least two prepared gifts are needed.
"""

import random
import sys


def main():
    mode = sys.argv[1]
    seed, n, *args = map(int, sys.argv[2:])
    assert 1 <= n <= 500
    rng = random.Random(seed)
    if mode == "random":
        low, high = args
        assert 1 <= low <= high <= 500
        sizes = [rng.randint(low, high) for _ in range(n)]
    elif mode == "dominant":
        (peak,) = args
        assert 2 <= n < peak <= 500
        other_max = min(20, (peak - 2) // (n - 1))
        sizes = [rng.randint(1, other_max) for _ in range(n - 1)]
        sizes.insert(rng.randrange(n), peak)
    else:
        raise ValueError("unknown mode: " + mode)
    print(n)
    print(*sizes)


if __name__ == "__main__":
    main()
