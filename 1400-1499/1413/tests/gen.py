"""A million key presses: a seed and a mode. Mode 1 is random keys
without 0, mode 2 random keys with a single 0 near the end, mode 3 only
the diagonal key 9, mode 4 keys that wander and come almost back."""

import random
import sys

SIZE = 10**6


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        keys = [rng.choice("12346789") for _ in range(SIZE)]
    elif mode == 2:
        keys = [rng.choice("123456789") for _ in range(SIZE)]
        keys[SIZE - rng.randint(2, 1000)] = "0"
    elif mode == 3:
        keys = ["9"] * SIZE
    else:
        half = [rng.choice("12346789") for _ in range(SIZE // 2)]
        back = {"1": "9", "2": "8", "3": "7", "4": "6", "6": "4", "7": "3", "8": "2", "9": "1"}
        keys = half + [back[k] for k in half]
        keys[-1] = "5"
        rng.shuffle(keys)
    print("".join(keys))


main()
