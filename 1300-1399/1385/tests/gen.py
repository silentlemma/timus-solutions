"""Generate one N: SEED MODE. Modes: small (21..99), medium (100..999),
large (4301..9998). Each mode samples uniformly using seeded randomness.
"""

import random
import sys

RANGES = {"small": (21, 99), "medium": (100, 999), "large": (4301, 9998)}


def main():
    seed = int(sys.argv[1])
    low, high = RANGES[sys.argv[2]]
    n = random.Random(seed).randint(low, high)
    sys.stdout.buffer.write(f"{n}\n".encode())


main()
