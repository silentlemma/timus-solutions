import random
import sys

MAX_SEATS = 1000
MAX_PERCENT = 100
SMALL_LIMIT = 16
DENSITY_DENOMINATOR = 4
ARGUMENT_COUNT = 3

SMALL = 1
RANDOM = 2
BALANCED = 3
LEFT_HEAVY = 4
RIGHT_HEAVY = 5
SPARSE = 6
DENSE = 7
EDGE = 8
SINGLE = 9
OCCUPIED = 10
ALMOST_EMPTY = 11
ALMOST_FULL = 12
EXTREME_PERCENTAGES = (0, 1, MAX_PERCENT // 2, MAX_PERCENT - 1, MAX_PERCENT)


def random_row(size, position, rng, empty_numerator, denominator):
    seats = ["0" if rng.randrange(denominator) < empty_numerator else "1" for _ in range(size)]
    seats[position] = "2"
    return "".join(seats)


def generate(mode, seed):
    rng = random.Random(seed)
    percent = rng.randrange(MAX_PERCENT + 1)
    if mode == SINGLE:
        return percent, "2"
    if mode == SMALL:
        size = rng.randrange(1, SMALL_LIMIT + 1)
        position = rng.randrange(size)
        return percent, random_row(size, position, rng, 1, 2)
    if mode == RANDOM:
        size = rng.randrange(1, MAX_SEATS + 1)
        position = rng.randrange(size)
        numerator = rng.randrange(1, DENSITY_DENOMINATOR)
        row = random_row(size, position, rng, numerator, DENSITY_DENOMINATOR)
        return percent, row
    if mode == OCCUPIED:
        position = rng.randrange(MAX_SEATS)
        row = "1" * position + "2" + "1" * (MAX_SEATS - position - 1)
        return percent, row
    if mode == EDGE:
        position = rng.choice((0, MAX_SEATS - 1))
        return percent, random_row(MAX_SEATS, position, rng, 1, 2)
    if mode in (SPARSE, DENSE):
        numerator = 1 if mode == SPARSE else DENSITY_DENOMINATOR - 1
        position = rng.randrange(MAX_SEATS)
        row = random_row(MAX_SEATS, position, rng, numerator, DENSITY_DENOMINATOR)
        return percent, row
    if mode in (BALANCED, LEFT_HEAVY, RIGHT_HEAVY, ALMOST_EMPTY, ALMOST_FULL):
        position = MAX_SEATS // 2
        if mode == LEFT_HEAVY:
            position = MAX_SEATS - 2
        elif mode == RIGHT_HEAVY:
            position = 1
        elif mode == ALMOST_EMPTY:
            percent = MAX_PERCENT - 1
        elif mode == ALMOST_FULL:
            percent = 1
        else:
            percent = EXTREME_PERCENTAGES[seed % len(EXTREME_PERCENTAGES)]
        row = "0" * position + "2" + "0" * (MAX_SEATS - position - 1)
        return percent, row
    raise ValueError("unknown generator mode")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    percent, row = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(len(row), percent)
    print(row)


if __name__ == "__main__":
    main()
