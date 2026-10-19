"""Arguments: seed mode. Modes 1..8 exercise large reliable-team outputs."""

import random
import sys

LIMIT = 1000


def generate(seed, mode):
    rng = random.Random(seed)
    if mode in (1, 3):
        values = [value for even in range(2, LIMIT + 1, 2) for value in (even, even)]
        if mode == 3:
            rng.shuffle(values)
    elif mode in (2, 8):
        values = [1] + [value for odd in range(3, LIMIT, 2) for value in (odd, odd)]
        if mode == 8:
            values.append(LIMIT)
            rng.shuffle(values)
    elif mode == 4:
        values = [1] * LIMIT
    elif mode == 5:
        values = [LIMIT] * LIMIT
    elif mode == 6:
        values = [LIMIT] * (LIMIT - 1)
    else:
        values = [rng.randint(1, LIMIT) for _ in range(LIMIT)]
    return values


if __name__ == "__main__":
    data = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(len(data))
    print("\n".join(map(str, data)))
