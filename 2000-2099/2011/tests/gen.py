"""Usage: seed mode. Modes: same1, same3, minority_last, minority_first,
balanced, alternating, random. All produce 100 symbols with deterministic randomness.
"""

import random
import sys

COUNT = 100
ALPHABET = 3


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == "same1":
        values = [1] * COUNT
    elif mode == "same3":
        values = [ALPHABET] * COUNT
    elif mode == "minority_last":
        values = [1] * (COUNT - 1) + [2]
    elif mode == "minority_first":
        values = [2] + [1] * (COUNT - 1)
    elif mode == "balanced":
        values = [i % ALPHABET + 1 for i in range(COUNT)]
        rng.shuffle(values)
    elif mode == "alternating":
        values = [i % 2 + 1 for i in range(COUNT)]
    elif mode == "random":
        values = [rng.randint(1, ALPHABET) for _ in range(COUNT)]
    else:
        raise ValueError("unknown mode")
    return str(COUNT) + "\n" + " ".join(map(str, values)) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
