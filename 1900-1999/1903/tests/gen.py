"""Generate seed/mode: 1 small; 2 equal; 3 first rank; 4 last rank; 5 middle;
6 almost all; 7 three classes; 8 random; 9 singleton; 10 almost all equal."""

import random
import sys

MAX_COUNT = 5000
MAX_CLASS = 5000
SMALL_COUNT = 10


def generate(seed, mode):
    rng = random.Random(seed)
    n = SMALL_COUNT if mode == 1 else MAX_COUNT
    selected = n // 2
    classes = list(range(1, n + 1))
    identified = n // 2
    position = selected // 2
    if mode == 1:
        classes = [rng.randrange(1, MAX_CLASS + 1) for _ in range(n)]
        selected = rng.randrange(1, n)
        identified = rng.randrange(1, n + 1)
        position = rng.randrange(1, selected + 1)
    elif mode in (2, 10):
        classes = [rng.randrange(1, MAX_CLASS + 1)] * n
        if mode == 10:
            selected = n - 1
        identified = rng.randrange(1, n + 1)
        position = rng.randrange(1, selected + 1)
    elif mode == 3:
        position = 1
    elif mode == 4:
        position = selected
    elif mode == 5:
        pass
    elif mode == 6:
        selected = n - 1
        identified = rng.randrange(1, n + 1)
        position = rng.randrange(1, selected + 1)
    elif mode == 7:
        classes = [rng.choice((1, MAX_CLASS // 2, MAX_CLASS)) for _ in range(n)]
        selected = 2 * n // 3
        identified = rng.randrange(1, n + 1)
        classes[identified - 1] = MAX_CLASS // 2
        position = rng.randrange(1, selected + 1)
    elif mode == 8:
        classes = [rng.randrange(1, MAX_CLASS + 1) for _ in range(n)]
        identified = rng.randrange(1, n + 1)
        position = rng.randrange(1, selected + 1)
    elif mode == 9:
        selected, position = 1, 1
        identified = rng.randrange(1, n + 1)
    else:
        raise ValueError("Unknown mode")
    return n, selected, classes, identified, position


def main():
    n, selected, classes, identified, position = generate(*map(int, sys.argv[1:]))
    print(n, selected)
    print(*classes)
    print(identified, position)


if __name__ == "__main__":
    main()
