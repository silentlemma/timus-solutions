"""200 000 records: a seed and a mode. Mode 1 swaps two digits of one
random record near the end, mode 2 has many records that fit the same
swap, so the first one is reported, mode 3 has a difference that no swap
explains, mode 4 sums correctly."""

import random
import sys

N = 200000
TOP = 2**31 - 1


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    records = [rng.randint(0, TOP) for _ in range(N)]
    true = list(records)
    if mode == 1:
        k = N - rng.randint(1, 100)
        records[k] = 1928374650
        true[k] = 1928734650  # the accountant swapped 7 and 3
    elif mode == 2:
        for k in range(N // 2, N):
            records[k] = true[k] = 1200000000
        true[N - 1] = 2100000000
    report = sum(true) + (rng.choice([1, 10, 17]) if mode == 3 else 0)
    print(N)
    print("\n".join(map(str, records)))
    print(report)


main()
