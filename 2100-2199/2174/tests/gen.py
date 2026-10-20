"""Notes from "MODE SEED": mode 1 a few small notes, mode 2 500 random
notes with as many odd as even ones, mode 3 500 notes built from prime
pairs and ones, mode 4 500 notes with too many odd ones."""

import random
import sys

MAX_N = 500
MAX_C = 10 ** 6
SMALL_N = 8
SMALL_C = 12


def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = 2 * rng.randint(1, SMALL_N // 2)
        notes = [rng.randint(1, SMALL_C) for _ in range(n)]
    elif mode == 2:
        half = MAX_N // 2
        notes = [2 * rng.randint(0, MAX_C // 2 - 1) + 1 for _ in range(half)]
        notes += [2 * rng.randint(1, MAX_C // 2) for _ in range(half)]
    elif mode == 3:
        notes = []
        while len(notes) < MAX_N:
            if rng.randint(0, SMALL_N) == 0:
                notes += [1, 1]
                continue
            even = 2 * rng.randint(1, MAX_C // 2)
            odd = 2 * rng.randint(0, MAX_C // 2 - 1) + 1
            if is_prime(even + odd):
                notes += [even, odd]
    else:
        notes = [2 * rng.randint(1, MAX_C // 2 - 1) + 1 for _ in range(MAX_N // 2 + 2)]
        notes += [2 * rng.randint(1, MAX_C // 2) for _ in range(MAX_N // 2 - 2)]
    rng.shuffle(notes)
    print(len(notes))
    print(*notes)


main()
