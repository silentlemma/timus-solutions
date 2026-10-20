import random
import sys


MAX_SIZE = 100_000
MAX_VALUE = 1_000_000_000
SMALL_SIZE = 10
SMALL_VALUE = 10
PLATEAU_LENGTH = 10
ARGUMENT_COUNT = 3
SMALL_RANDOM = 1
LARGE_RANDOM = 2
EARLY_FALL = 3
PLATEAUS = 4
LARGE_PREFIXES = 5
IMPOSSIBLE = 6
MANY_CANDIDATES = 7


def boundary_queries(rng, a, b, count):
    choices = [1, MAX_VALUE]
    prefix = 0
    for own, other in zip(a, b):
        prefix += own - other
        for offset in (-1, 0, 1):
            value = prefix + offset
            if 1 <= value <= MAX_VALUE:
                choices.append(value)
    return [rng.choice(choices) for _ in range(count)]


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == SMALL_RANDOM:
        n = rng.randint(1, SMALL_SIZE)
        q = rng.randint(1, SMALL_SIZE)
        a = [rng.randint(0, SMALL_VALUE) for _ in range(n)]
        b = [rng.randint(0, SMALL_VALUE) for _ in range(n)]
        d = boundary_queries(rng, a, b, q)
    elif mode == LARGE_RANDOM:
        n = q = MAX_SIZE
        a = [rng.randint(0, MAX_VALUE) for _ in range(n)]
        b = [rng.randint(0, MAX_VALUE) for _ in range(n)]
        d = boundary_queries(rng, a, b, q)
    elif mode == EARLY_FALL:
        n = q = MAX_SIZE
        a = [0] * n
        b = [0] * n
        a[0] = MAX_VALUE
        b[rng.randrange(1, n - 2)] = MAX_VALUE
        a[-2] = a[-1] = MAX_VALUE
        d = [rng.randint(1, MAX_VALUE) for _ in range(q)]
    elif mode == PLATEAUS:
        n = q = MAX_SIZE
        a = []
        b = []
        for index in range(n):
            if index % PLATEAU_LENGTH == 0:
                a.append(rng.randint(1, SMALL_VALUE))
                b.append(0)
            else:
                speed = rng.randint(0, MAX_VALUE)
                a.append(speed)
                b.append(speed)
        d = boundary_queries(rng, a, b, q)
    elif mode == LARGE_PREFIXES:
        n = q = MAX_SIZE
        a = [MAX_VALUE] * n
        b = [0] * n
        d = [rng.choice((1, MAX_VALUE - 1, MAX_VALUE)) for _ in range(q)]
    elif mode == IMPOSSIBLE:
        n = q = MAX_SIZE
        a = [0] * n
        b = [MAX_VALUE] * n
        d = [rng.randint(1, MAX_VALUE) for _ in range(q)]
    elif mode == MANY_CANDIDATES:
        n = q = MAX_SIZE
        a = [rng.randint(1, MAX_VALUE) for _ in range(n)]
        b = [speed - 1 for speed in a]
        d = list(range(1, n + 1))
        rng.shuffle(d)
    else:
        raise SystemExit("unknown mode")
    return n, q, a, b, d


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    n, q, a, b, d = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(n, q)
    print(*a)
    print(*b)
    print(*d)


if __name__ == "__main__":
    main()
