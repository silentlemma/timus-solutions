import random
import sys


MAX_VALUE = 10**9
MAX_COUNT = 18
SMALL_LIMIT = 200
DENSE_STEP_LIMIT = 40
DENSE_START_LIMIT = 300
LATE_WINDOW = 1000
SPARSE_STEP = 31600
SPARSE_WINDOW = 100
MODE_SMALL = 1
MODE_RANDOM = 2
MODE_DENSE = 3
MODE_HUGE_LCM = 4
MODE_EQUAL_STEPS = 5
MODE_BOUNDARIES = 6
MODE_NESTED = 7
MODE_COPRIME = 8
MODE_EUCLID = 9
MODE_GCD = 10
MODE_LATE = 11
MODE_POWERS = 12
MODE_SPARSE = 13
MODE_SHIFTED = 14
MODE_ANTICHAIN = 15
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61)
ANTICHAIN_STEPS = (
    1785,
    1938,
    3230,
    1794,
    2470,
    7735,
    3003,
    4845,
    5313,
    11362,
    24871,
    9614,
    4862,
    2090,
    3315,
    3135,
    858,
    8645,
)
LARGE_PRIMES = (
    999999937,
    999999929,
    999999893,
    999999883,
    999999797,
    999999761,
    999999757,
    999999751,
    999999739,
    999999733,
    999999677,
    999999667,
    999999613,
    999999607,
    999999599,
    999999587,
    999999541,
    999999527,
)


def make_case(mode, rng):
    if mode == MODE_SMALL:
        limit = rng.randint(1, SMALL_LIMIT)
        count = rng.randint(1, MAX_COUNT)
        pairs = [(rng.randint(1, SMALL_LIMIT), rng.randint(1, SMALL_LIMIT)) for _ in range(count)]
    elif mode == MODE_RANDOM:
        limit = rng.randint(1, MAX_VALUE)
        pairs = [(rng.randint(1, MAX_VALUE), rng.randint(1, MAX_VALUE)) for _ in range(MAX_COUNT)]
    elif mode == MODE_DENSE:
        limit = MAX_VALUE
        pairs = [
            (rng.randint(1, DENSE_START_LIMIT), rng.randint(1, DENSE_STEP_LIMIT))
            for _ in range(MAX_COUNT)
        ]
    elif mode == MODE_HUGE_LCM:
        limit = MAX_VALUE
        common = rng.randint(1, SMALL_LIMIT)
        pairs = [(common, step) for step in LARGE_PRIMES]
    elif mode == MODE_EQUAL_STEPS:
        limit = MAX_VALUE
        step = rng.randint(2, SMALL_LIMIT)
        residue = rng.randint(1, step)
        pairs = [(residue + rng.randint(0, SMALL_LIMIT) * step, step) for _ in range(MAX_COUNT)]
        pairs[-1] = (residue % step + 1, step)
    elif mode == MODE_BOUNDARIES:
        limit = rng.choice((1, MAX_VALUE - 1, MAX_VALUE))
        starts = (1, limit, min(MAX_VALUE, limit + 1), MAX_VALUE)
        steps = (1, MAX_VALUE - 1, MAX_VALUE)
        pairs = [(rng.choice(starts), rng.choice(steps)) for _ in range(MAX_COUNT)]
    elif mode == MODE_NESTED:
        limit = MAX_VALUE
        first = rng.randint(1, SMALL_LIMIT)
        step = rng.randint(1, SMALL_LIMIT)
        pairs = [
            (first + rng.randint(0, SMALL_LIMIT) * step, step * rng.randint(1, 10))
            for _ in range(MAX_COUNT)
        ]
        pairs[0] = (first, step)
    elif mode == MODE_COPRIME:
        limit = MAX_VALUE
        pairs = [(rng.randint(1, step), step) for step in SMALL_PRIMES]
    elif mode == MODE_EUCLID:
        limit = MAX_VALUE
        fibonacci = [1, 2]
        while fibonacci[-1] + fibonacci[-2] <= MAX_VALUE:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        common = rng.randint(1, SMALL_LIMIT)
        pairs = [(common, step) for step in fibonacci[-MAX_COUNT:]]
    elif mode == MODE_GCD:
        limit = MAX_VALUE
        pairs = []
        for _ in range(MAX_COUNT):
            step = 2 * rng.randint(1, SMALL_LIMIT)
            first = rng.randint(1, SMALL_LIMIT)
            pairs.append((first, step))
    elif mode == MODE_LATE:
        limit = MAX_VALUE
        pairs = [
            (limit - rng.randint(0, LATE_WINDOW), rng.randint(1, SMALL_LIMIT))
            for _ in range(MAX_COUNT)
        ]
    elif mode == MODE_POWERS:
        limit = MAX_VALUE
        common = rng.randint(1, SMALL_LIMIT)
        pairs = [(common + (1 << index), 1 << index) for index in range(MAX_COUNT)]
    elif mode == MODE_SPARSE:
        limit = MAX_VALUE
        pairs = [
            (rng.randint(1, SPARSE_WINDOW), SPARSE_STEP + rng.randint(0, SPARSE_WINDOW))
            for _ in range(MAX_COUNT)
        ]
    elif mode == MODE_SHIFTED:
        limit = MAX_VALUE
        common = rng.randint(MAX_VALUE // 2, MAX_VALUE - DENSE_START_LIMIT)
        pairs = [(common - rng.randint(0, 10) * step, step) for step in SMALL_PRIMES]
    elif mode == MODE_ANTICHAIN:
        limit = MAX_VALUE
        pairs = [(1, step) for step in ANTICHAIN_STEPS]
    else:
        raise ValueError("unknown mode")
    rng.shuffle(pairs)
    return limit, pairs


def main():
    mode, seed = map(int, sys.argv[1:])
    limit, pairs = make_case(mode, random.Random(seed))
    print(limit, len(pairs))
    for first, step in pairs:
        print(first, step)


if __name__ == "__main__":
    main()
