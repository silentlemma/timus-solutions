import random
import sys

MOD = 998_244_353
MAX_N = 100_000
MAX_M = 800_000
SMALL_N = 32
SMALL_M = 48
SMALL_DEGREE = 8
MEDIUM_N = 2_048
MEDIUM_M = 4_096
MIN_POWER = 5
MAX_POWER = 11
ARGUMENT_COUNT = 3
MODE_SMALL_RANDOM = 1
MODE_POLYNOMIAL = 2
MODE_BOUNDARY_VALUES = 3
MODE_SINGLE_POINT = 4
MODE_MAX_RANDOM = 5
MODE_MAX_POLYNOMIAL = 6
MODE_MAX_N = 7
MODE_MAX_M = 8
MODE_TRANSFORM_BOUNDARY = 9
MODE_MAX_ZERO = 10
MODE_MAX_SPIKE = 11


def polynomial_values(rng, n):
    degree = rng.randrange(min(n, SMALL_DEGREE + 1))
    coefficients = [rng.randrange(MOD) for _ in range(degree + 1)]
    values = []
    for x in range(1, n + 1):
        value = 0
        for coefficient in coefficients:
            value = (value * x + coefficient) % MOD
        values.append(value)
    return values


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SMALL_RANDOM:
        n = rng.randint(1, SMALL_N)
        m = rng.randint(1, SMALL_M)
        values = [rng.randrange(MOD) for _ in range(n)]
    elif mode == MODE_POLYNOMIAL:
        n = rng.randint(1, SMALL_N)
        m = rng.randint(1, SMALL_M)
        values = polynomial_values(rng, n)
    elif mode == MODE_BOUNDARY_VALUES:
        n = rng.randint(1, SMALL_N)
        m = rng.randint(1, SMALL_M)
        choices = [0, 1, 2, MOD - 2, MOD - 1]
        values = [rng.choice(choices) for _ in range(n)]
    elif mode == MODE_SINGLE_POINT:
        n = 1
        m = rng.randint(1, SMALL_M)
        values = [rng.randrange(MOD)]
    elif mode == MODE_MAX_RANDOM:
        n, m = MAX_N, MAX_M
        values = [rng.randrange(MOD) for _ in range(n)]
    elif mode == MODE_MAX_POLYNOMIAL:
        n, m = MAX_N, MAX_M
        values = polynomial_values(rng, n)
    elif mode == MODE_MAX_N:
        n, m = MAX_N, 1
        values = [rng.randrange(MOD) for _ in range(n)]
    elif mode == MODE_MAX_M:
        n = rng.randint(1, SMALL_DEGREE)
        m = MAX_M
        values = [rng.randrange(MOD) for _ in range(n)]
    elif mode == MODE_TRANSFORM_BOUNDARY:
        boundary = 1 << rng.randint(MIN_POWER, MAX_POWER)
        n = max(1, min(MEDIUM_N, boundary + rng.randint(-2, 2)))
        m = rng.randint(1, MEDIUM_M)
        values = [rng.randrange(MOD) for _ in range(n)]
    elif mode == MODE_MAX_ZERO:
        n, m = MAX_N, MAX_M
        values = [0] * n
    elif mode == MODE_MAX_SPIKE:
        n, m = MAX_N, MAX_M
        values = [0] * n
        values[rng.randrange(n)] = rng.randrange(1, MOD)
    else:
        raise SystemExit("unknown mode")
    return n, m, values


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    n, m, values = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(n, m)
    print(" ".join(map(str, values)))


if __name__ == "__main__":
    main()
