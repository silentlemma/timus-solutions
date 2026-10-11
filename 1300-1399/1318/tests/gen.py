"""5000 numbers of 128 bits: a seed and a mode. Mode 1 gives random
numbers, mode 2 short numbers with many repeats, mode 3 numbers sharing a
random prefix of random length, mode 4 numbers close to powers of ten,
mode 5 the high and the low halves taken from two small sets, mode 6
descending consecutive values below the 128-bit maximum, mode 7 balanced
clusters separated by the highest bit, mode 8 one decimal-threshold
outlier among 4999 values with a shared large prefix."""

import random
import sys

N = 5000
BITS = 128
HALF = 64
WORD = 32
PARTS = 4
POWERS = 38


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    base = rng.getrandbits(BITS)
    highs = [rng.getrandbits(HALF) for _ in range(70)]
    lows = [rng.getrandbits(HALF) for _ in range(70)]
    nums = []
    for i in range(N):
        if mode == 1:
            value = rng.getrandbits(BITS)
        elif mode == 2:
            value = rng.getrandbits(rng.randint(1, 12))
        elif mode == 3:
            value = base ^ rng.getrandbits(rng.randint(1, BITS))
        elif mode == 4:
            value = 10 ** rng.randint(1, POWERS) + rng.randint(-3, 3)
        elif mode == 6:
            value = (1 << BITS) - 1 - i
        elif mode == 7:
            value = (i % 2) << (BITS - 1) | rng.getrandbits(12)
        elif mode == 8:
            if i == N // 2:
                value = base ^ 10**POWERS
            elif i == 0:
                value = base
            else:
                value = base ^ rng.getrandbits(40)
        else:
            value = rng.choice(highs) << HALF | rng.choice(lows)
        nums.append(value)
    print(N)
    mask = (1 << WORD) - 1
    for value in nums:
        words = [value >> (WORD * (PARTS - 1 - p)) & mask for p in range(PARTS)]
        print(*words)


main()
