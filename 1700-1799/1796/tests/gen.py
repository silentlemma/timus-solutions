"""One test from a seed and a mode: mode 1 up to three notes of each
kind, mode 2 up to 1000 of each kind, and any price up to 1000.
Only inputs with at least one answer are printed: new values are drawn
until one turns up."""

import random
import sys

NOTES = [10, 50, 100, 500, 1000, 5000]
LIMIT = 1000
FEW = 3


def answers(counts, price):
    total = sum(c * note for c, note in zip(counts, NOTES))
    smallest = min(note for c, note in zip(counts, NOTES) if c > 0)
    return total // price - (total - smallest) // price


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = FEW if mode == 1 else LIMIT
    while True:
        counts = [rng.randint(0, top) if rng.random() < 0.5 else 0 for _ in NOTES]
        if not any(counts):
            continue
        price = rng.randint(1, LIMIT)
        if answers(counts, price) > 0:
            break
    print(*counts)
    print(price)


main()
