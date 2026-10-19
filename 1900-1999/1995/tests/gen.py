"""Usage: gen.py SEED MODE; records,low_percent,near_percent,balanced,boundary,one_kept,all_twos,tiny_discard."""

import sys

MAXIMUM = 100000


def generate(seed, mode):
    del seed
    values = {
        "records": (MAXIMUM, MAXIMUM - 1, 100),
        "low_percent": (MAXIMUM, MAXIMUM - 1, 1),
        "near_percent": (MAXIMUM, MAXIMUM - 1, 99),
        "balanced": (MAXIMUM, MAXIMUM // 2, 50),
        "boundary": (MAXIMUM, MAXIMUM // 2 + 1, 50),
        "one_kept": (MAXIMUM, 1, 100),
        "all_twos": (MAXIMUM, 999, 99),
        "tiny_discard": (MAXIMUM, MAXIMUM - 1, 50),
    }
    return values[mode]


if __name__ == "__main__":
    size, kept, percentage = generate(int(sys.argv[1]), sys.argv[2])
    print(size, kept)
    print(percentage)
