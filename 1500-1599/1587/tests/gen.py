"""One test from a seed and a mode: up to 50000 marks from -3 to 3. Mode 1
mixes in zeros, mode 2 has none, mode 3 is all threes (the longest
answer), mode 4 lone negative marks between zeros, mode 5 is short."""

import random
import sys

MOST = 50000
SHORT = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SHORT) if mode == 5 else MOST
    if mode == 1:
        marks = [
            rng.choice([-3, -2, -1, 0, 1, 2, 3])
            if rng.random() < 0.01
            else rng.choice([-3, -2, 2, 3])
            for _ in range(n)
        ]
    elif mode == 2:
        marks = [rng.choice([-3, -2, -1, 1, 2, 3]) for _ in range(n)]
    elif mode == 3:
        marks = [3] * n
    elif mode == 4:
        marks = [0 if i % 2 else rng.choice([-3, -2, -1]) for i in range(n)]
    else:
        marks = [rng.randint(-3, 3) for _ in range(n)]
    print(n)
    print(*marks)


main()
