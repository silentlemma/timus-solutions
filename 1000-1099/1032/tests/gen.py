"""Modes:

SEED N TOP: N independent random numbers from 1 through TOP (original mode).
late SEED N: shuffled nonzero prefix remainders, repeated only at the last value.
"""

import random
import sys


def main():
    if sys.argv[1] == "late":
        seed, n = map(int, sys.argv[2:4])
        if not 3 <= n <= 10000:
            raise ValueError("late mode requires 3 <= N <= 10000")
        rng = random.Random(seed)
        remainders = list(range(1, n))
        rng.shuffle(remainders)
        remainders.append(remainders[n // 2 - 1])
        values, previous = [], 0
        for remainder in remainders:
            value = (remainder - previous) % n
            if value + n <= 15000:
                value += n
            values.append(value)
            previous = remainder
        print("\n".join(map(str, [n] + values)))
        return

    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    print("\n".join([str(n)] + [str(rng.randint(1, top)) for _ in range(n)]))


if __name__ == "__main__":
    main()
