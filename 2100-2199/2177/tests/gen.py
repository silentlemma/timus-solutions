import random
import sys

MIN_SUM = 3
MAX_SUM = 1_000_000_000
SMALL_MAX = 80
CLOSE_RANGE = 1_000
DECIMAL_BASE = 10


def quotient_pair(rng, mode):
    gap = rng.choice((rng.randint(2, SMALL_MAX), rng.randint(2, MAX_SUM // DECIMAL_BASE)))
    remainder = 0
    if mode == "remainder-one":
        remainder = 1
    elif mode == "remainder-half":
        remainder = gap // 2
    minimum = max(1, (MIN_SUM - remainder + gap - 1) // gap)
    maximum = (MAX_SUM - gap - remainder) // gap
    lower = rng.randint(minimum, maximum) * gap + remainder
    return lower, lower + gap


def generate(mode, rng):
    if mode == "small":
        return rng.randint(MIN_SUM, SMALL_MAX), rng.randint(MIN_SUM, SMALL_MAX)
    if mode == "random":
        return rng.randint(MIN_SUM, MAX_SUM), rng.randint(MIN_SUM, MAX_SUM)
    if mode == "equal":
        value = rng.randint(MIN_SUM, MAX_SUM)
        return value, value
    if mode == "consecutive":
        lower = rng.randint(MIN_SUM, MAX_SUM - 1)
        return lower, lower + 1
    if mode == "near-limit":
        return MAX_SUM - rng.randrange(CLOSE_RANGE), MAX_SUM - rng.randrange(CLOSE_RANGE)
    if mode == "wide-gap":
        return rng.randint(MIN_SUM, SMALL_MAX), MAX_SUM - rng.randrange(CLOSE_RANGE)
    if mode in ("multiple", "remainder-one", "remainder-half"):
        return quotient_pair(rng, mode)
    if mode == "odd":
        first = 2 * rng.randint(1, (MAX_SUM - 1) // 2) + 1
        second = 2 * rng.randint(1, (MAX_SUM - 1) // 2) + 1
        return first, second
    if mode == "even":
        first = 2 * rng.randint((MIN_SUM + 1) // 2, MAX_SUM // 2)
        second = 2 * rng.randint((MIN_SUM + 1) // 2, MAX_SUM // 2)
        return first, second
    if mode == "maximum":
        other = rng.choice((MIN_SUM, MAX_SUM, MAX_SUM - 1, MAX_SUM - 2))
        return MAX_SUM, other
    raise ValueError("unknown mode: " + mode)


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    first, second = generate(mode, rng)
    if rng.getrandbits(1):
        first, second = second, first
    print(first)
    print(second)


if __name__ == "__main__":
    main()
