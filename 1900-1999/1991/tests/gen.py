"""Usage: gen.py SEED MODE; modes: surplus,deficit,equal,alternating,cycle."""

import sys

MAXIMUM = 10000
SUPPLY = 100000


def generate(seed, mode):
    del seed
    capacity = 1 if mode == "surplus" else MAXIMUM
    if mode == "surplus":
        amounts = [SUPPLY] * MAXIMUM
    elif mode == "deficit":
        amounts = [0] * MAXIMUM
    elif mode == "equal":
        amounts = [capacity] * MAXIMUM
    elif mode == "alternating":
        amounts = [0, SUPPLY] * (MAXIMUM // 2)
    else:
        assert mode == "cycle"
        amounts = [0, capacity - 1, capacity, capacity + 1, SUPPLY] * (MAXIMUM // 5)
    return capacity, amounts


def render(capacity, amounts):
    return f"{len(amounts)} {capacity}\n" + " ".join(map(str, amounts)) + "\n"


if __name__ == "__main__":
    sys.stdout.write(render(*generate(int(sys.argv[1]), sys.argv[2])))
