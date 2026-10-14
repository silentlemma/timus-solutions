"""One test from SEED MODE.

random: four independent uniform values from 1 to 10000.
slow-petya: distant starting prices, Petya raises by 1, driver cuts by 2..9.
slow-driver: distant starting prices, Petya raises by 2..9, driver cuts by 1.
"""

import random
import sys

MAX_VALUE = 10000


def main():
    seed, mode = sys.argv[1:]
    rng = random.Random(int(seed))
    if mode == "random":
        values = [rng.randint(1, MAX_VALUE) for _ in range(4)]
    elif mode in ("slow-petya", "slow-driver"):
        a = rng.randint(1, 100)
        c = rng.randint(MAX_VALUE - 100, MAX_VALUE)
        step = rng.randint(2, 9)
        b, d = (1, step) if mode == "slow-petya" else (step, 1)
        values = [a, b, c, d]
    else:
        raise SystemExit(f"unknown mode: {mode}")
    print(*values)


if __name__ == "__main__":
    main()
